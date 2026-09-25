---
project: OstadLagbo
module: contact-and-offers
type: api
status: current
updated: 2026-09-25
id: OL-OFR-API-001
derived_from: /OstadLagbo/modules/contact-and-offers/requirements/contact-and-offers-requirements.md
owner: Iftikher
---

# Contact & Offers — API

Endpoints for the offer lifecycle, the 1:1 chat, contact reveal, and their inboxes — the module that holds the platform's success unit, the **connection**. Conventions per [API Overview](/OstadLagbo/api-overview.md); entities, the state machine, and the freeze predicate per [OFR Data Model](/OstadLagbo/modules/contact-and-offers/data-model/contact-and-offers-data-model.md). Two commitments from the data model shape every endpoint here: **`offer` is transient, `connection` is permanent**, and **contact reveal is a read rule, not a stored copy.**

## Two things that are not endpoints

- **Chat delivery is a direct Supabase Realtime channel** (API Overview), not an API poll. The client subscribes to its own threads over Realtime (RLS-scoped, and the RLS policy additionally requires the subscriber's account status to be `active`, so a suspended party receives no delivery). **The API remains the only writer** — every message, receipt, and system marker is an API call; Realtime is read-only.
- **Two scheduled jobs run the parts of the lifecycle no user triggers** (Supabase pg_cron, ADR-001): the **expiry job** transitions `pending` offers to `expired` at `expires_at`, and the **day-5 reminder job** sends the single pending-expiry push (`reminder_sent_at` guards it to once). Both fire whether or not either party opens the app (OFR-02, OFR-03).

## Endpoints — the offer lifecycle

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/offers` | A registered **Shagred** (Ostads cannot initiate — OFR-01); accepts `Idempotency-Key`. Policy checks, all at insert: recipient satisfies the discoverability predicate, is **not paused** (OSP-11), and has **no block** either way (OFR-01) | `{ ostad_id, message }` — free text, ≤500 chars | `{ id, status: "pending", expires_at }` — a `pending` offer; sending grants the Ostad visibility of the Shagred's profile (SGP-05) and pushes "offer received" | `validation_failed` (message empty or >500); `forbidden` (caller is an Ostad); `state_conflict` (`reason: "ostad_not_accepting"` — paused, public state); `conflict` (`reason: "duplicate_pending_pair"` or `reason: "pending_limit_reached"`); `not_found` (no such approved Ostad, **or a block exists** — opacity rule) |
| `POST /v1/offers/{id}/accept` | The recipient **Ostad**, offer `pending`, **neither account suspended** (ADM-08); accepts `Idempotency-Key` (it creates a connection) | — | `{ connection_id, thread_id }` — runs the acceptance transaction (below); reveals contact both ways; pushes "accepted" to the Shagred | `not_found` (not the recipient, or no such offer — opacity); `state_conflict` (offer is in a **different** terminal state — see idempotency note); `suspended` |
| `POST /v1/offers/{id}/decline` | The recipient **Ostad**, offer `pending`, not suspended | — | `{ id, status: "declined" }` — `resolution_source: ostad`; lapses visibility (SGP-05); the Shagred may re-offer immediately (OFR-02); pushes "declined" | `not_found`; `state_conflict` (different terminal state); `suspended` |
| `POST /v1/offers/{id}/withdraw` | The **Shagred** who sent it, offer `pending`, not suspended | — | `{ id, status: "withdrawn" }` — `resolution_source: shagred`; lapses visibility (SGP-05); re-offer permitted immediately (OFR-02) | `not_found` (not the sender, or no such offer — opacity); `state_conflict` (different terminal state); `suspended` |
| `GET /v1/offers/{id}` | Either party to the offer | — | The offer with live `status`, `message`, timestamps, and `expires_at` when pending. The counterpart projection follows visibility (below) | `not_found` (not a party, or no such offer) |

**Transition idempotency.** The three transitions are safe to retry: **re-issuing the action that would reach the offer's *current* state is an idempotent success** — a repeated `accept` returns the existing `{connection_id, thread_id}`, a repeated `decline`/`withdraw` returns that same terminal status. `state_conflict` is returned only when the offer sits in a **different** terminal state than the action would produce (declining an offer already accepted, accepting one already expired). Terminal states remain immutable (OFR-02); this rule only makes retries idempotent, it never re-opens a resolved offer.

**Why `conflict` carries a `reason`.** The closed error enum has one `conflict` code (API Overview) but `POST /v1/offers` has two distinct uniqueness refusals — the per-pair pending rule (a partial unique index) and the 5-pending global cap (a service-layer count). Both are 409 `conflict`; `details.reason` tells them apart so the client shows the right message. *(Judgment call — flagged for review.)*

## Endpoints — the offer inboxes (OFR-09)

The two lists differ in what the counterpart projection contains, because visibility is asymmetric: **Ostads are public; Shagreds are visible to an Ostad only while an offer between them is live** (SGP-05).

| Endpoint | Caller | Response |
|---|---|---|
| `GET /v1/offers/sent` | Shagred | Their offers, `created_at desc`, cursor-paginated. Each carries the **Ostad** projection (public: `ostad_id`, `display_name`, `photo_url`) — tap-through always works — plus live `status`, and `expires_at` on pending (the client renders "N days remaining"). Pending items carry the withdraw action |
| `GET /v1/offers/received` | Ostad | Their offers, **pending first ordered `expires_at asc`** (soonest to expire on top), then resolved, cursor-paginated. Each carries `message`, `status`, timestamps, and accept/decline on pending. The **Shagred projection depends on status** (next paragraph) |

**The Shagred projection in the received list, by status** — this is the lapsed-offer rule made concrete:

- **`pending` or `accepted`:** the Shagred is visible (SGP-05) — the entry carries `shagred_id`, `display_name`, `photo_url`, and area, with tap-through to the profile.
- **`declined`, `expired`, `withdrawn`:** visibility has **lapsed** — the entry carries **no Shagred identity** (no id, name, photo, or area). What remains is the Ostad's own data: the **`message` text, the status, and the timestamps** — and the entry still supports **report and block**, which target the **`offer_id`** (the Ostad's own party object); the RNT api resolves the Shagred account server-side without re-exposing them (identifier rule; RNT api). An Ostad can therefore act on an abusive lapsed offer without ever seeing again whose it was.

## The acceptance transaction

`POST /v1/offers/{id}/accept` performs the data model's five writes in **one commit** (OFR-04) — partial success is not a valid state:

1. insert `connection` (copying both account ids and display-name snapshots)
2. insert `chat_thread` (its two participants fixed)
3. insert the offer's `message` as the first `chat_message` (`kind: text`, sender = the Shagred — they are their words)
4. update `offer.status = accepted`
5. insert the `ostad_history_entry` (SGP-DM)

After commit: the connection and phone-reveal analytics events are emitted (ADM-12, exactly once each), the "accepted" push goes to the Shagred, and **contact is now revealed both ways** — not by copying anything, but because the reveal read rule (below) now passes.

## Endpoints — chat (OFR-05, OFR-07)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `GET /v1/chat/threads` | A participant (both roles) | `?limit=&cursor=` | The inbox: threads where the caller is a participant, `last_message_at desc`. Each: `thread_id`, counterpart `display_name`, counterpart `photo_url` if live, unread count, `last_message_at`, and `frozen` + `frozen_reason` when the writable predicate fails. A counterpart in `pending_deletion` or `purged` shows as **"deleted account"** with no photo (OFR-06) | — |
| `GET /v1/chat/threads/{id}` | A participant | — | The thread header: counterpart `{ profile_id?, display_name, photo_url? }`; **`contact`** — `{ phone, email? }` — present **iff a connection exists between the two accounts and no block exists** (the reveal read rule, OFR-04), and `null` when a block stands or the counterpart is in `pending_deletion`/`purged` (shown as "deleted account", OFR-06); `frozen` + `frozen_reason` | `not_found` (caller is not a participant — opacity) |
| `GET /v1/chat/threads/{id}/messages` | A participant | `?limit=&cursor=` | Messages newest-first, cursor-paginated — readable **even when the thread is frozen** (history persists, OFR-06). `voice` messages carry a **short-lived signed download URL** (API Overview media) and `voice_duration_seconds`; a message from a party in `pending_deletion`/`purged` shows sender as "deleted account" (OFR-06) | `not_found` (not a participant) |
| `POST /v1/chat/threads/{id}/messages` | A participant, **thread writable** (predicate below); accepts `Idempotency-Key` | `text`: `{ kind: "text", body }` (≤ engineering cap). `voice`: `{ kind: "voice", upload_id, duration_seconds }` — the bytes were already `PUT` to Storage via an upload ticket (`POST /v1/uploads`, purpose `voice_note`); the API re-validates codec and **duration ≤120 s** at consumption (OFR-05) | The created `chat_message`; broadcast to the counterpart over Realtime; pushes "new message" (suppressed while that chat is open, OFR-03) | `validation_failed` (empty/oversized body; voice over 120 s or wrong codec; any attachment kind other than text/voice — none exists, OFR-05); `state_conflict` (`reason: "thread_frozen:<clause>"` — `blocked` / `suspended` / `deleted`, from the failing predicate clause); `not_found` (not a participant) |
| `POST /v1/chat/threads/{id}/receipts` | A participant | `{ up_to_message_id, state: "delivered" \| "read" }` | Stamps `delivered_at`/`read_at` on the counterpart's messages up to that id (the API is the only writer; the stamp then broadcasts over Realtime). With exactly two participants, `read` unambiguously means the counterpart read it (OFR-DM) | `not_found` (not a participant) |

**No message is ever editable or deletable** (OFR-05, CL-015): the api exposes no `PUT` or `DELETE` on a message. Chat history is moderation evidence. The only mutations are the receipt timestamps above and retention purges.

**`system` messages** (freeze/unfreeze notices) are inserted by the platform as a side effect of block, suspension, unblock, and reinstatement events in other modules — there is **no user-facing endpoint** that writes a `system` message.

## The writable predicate, at the API boundary

`POST …/messages` is admitted only when the data model's query-time predicate passes — nothing about freezing is stored (OFR-DM):

```
writable  iff  no block between the two participants (RNT-08)
          AND  neither account is suspended (ADM-08)
          AND  neither account is pending_deletion or purged (OFR-06)
```

A failing clause becomes the `state_conflict` reason the client shows ("You can no longer message this person"), and the header/inbox `frozen_reason`. Because nothing is stored, unblock or reinstatement restores writability with no bookkeeping; a deletion-frozen thread stays frozen permanently (the tombstone status never changes).

## Instrumentation (OFR-08)

Every event this module owes ADM-12/13 is written **server-side by the API** at the moment of the action (never client-reported), each under the analytics rules of the overview (no phone, name, or coordinates):

- **Offer transitions** — sent, accepted, declined, expired (from the job), withdrawn — each with the offer's **response time** (`resolved_at − created_at`) on resolution, and `resolution_source`.
- **Connections** — one per acceptance, exactly once; the per-pair uniqueness is inherent (one connection per accepted offer).
- **Phone reveals** — emitted at acceptance, when reveal becomes irreversible (1:1 with connections, but counted distinctly per OFR-08).
- **Messages and voice notes sent** — one per `POST …/messages`, tagged `text` or `voice`.

In-app counterparts (inbox states, unread badges) derive from this module's rows, not from analytics or delivery status, so a notifications-denied user misses nothing (OFR-03).

## Admin access to chat — only through a report (OFR-07)

No admin endpoint accepts a bare `thread_id`. The **sole** admin path into chat content originates from a `report` (RNT) citing specific `chat_message` ids: the ADM api returns those messages plus ±10 neighbours in the same thread and **writes a `chat_context_viewed` audit entry** (ADM-17) as a side effect. Defined in the ADM api; named here so this module's privacy boundary is complete.

## Deletion and suspension cascades (REG-12, CL-019, ADM-08)

Not endpoints of this module, but the transitions its rows obey when REG/ADM act on an account:

- **Entering `pending_deletion` or termination:** every `pending` offer the account is party to resolves in the same transaction — `withdrawn` if it is the sender, `declined` if it is the recipient — `resolution_source: deletion`. Recovery within 30 days does **not** restore them (OFR-DM). Accepted offers are untouched; their threads freeze via the predicate, and the counterpart is shown as "deleted account" (OFR-06).
- **Suspension:** `accept`/`decline`/`withdraw`/message-send are refused (`suspended` / `state_conflict`), but `expires_at` keeps running — a pending offer can expire mid-suspension.

## Flows

**Offer to connection.** Shagred opens an Ostad profile → `POST /v1/offers {ostad_id, message}` → Ostad gets a push and sees it in `GET /v1/offers/received` with the Shagred now visible → `POST /v1/offers/{id}/accept` → the five-write commit creates the connection, thread, and first message → both `GET /v1/chat/threads/{id}` now return the counterpart's `contact` → they message over `POST …/messages` with delivery over Realtime.

**A lapsed abusive offer.** Shagred sends an offensive `message` → Ostad declines → in `GET /v1/offers/received` the entry now shows the message and status but **no Shagred identity** → the Ostad taps "report" → the RNT api takes the **`offer_id`**, resolves the Shagred server-side, and files the report against them without re-revealing who they were.

**Block freezes a live chat.** A participant blocks the other (RNT) → the next `POST …/messages` fails `state_conflict reason: "thread_frozen:blocked"` → both still read history via `GET …/messages` → the header's `contact` is now `null` → if the block is later lifted, the very next send succeeds, no bookkeeping.

## What this module does not expose

No endpoint lets an Ostad initiate contact with a Shagred; no endpoint reveals a Shagred's identity on a declined, expired, or withdrawn offer (only the message, status, and the `offer_id` for report/block survive); no endpoint copies phone or email onto any row — contact is always a live read gated by connection-and-no-block; no endpoint edits or deletes a message, or lets a user write a `system` message; no admin endpoint opens a thread without a report citing its messages; no endpoint returns a thread or message to anyone but its two participants; and contact reveal never precedes acceptance (OFR-04).
