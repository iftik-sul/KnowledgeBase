---
project: OstadLagbo
module: contact-and-offers
type: data-model
status: current
updated: 2026-09-25
id: OL-OFR-DM-001
derived_from: /OstadLagbo/modules/contact-and-offers/requirements/contact-and-offers-requirements.md
owner: Iftikher
---

# Contact & Offers — Data Model

Entities owned: `offer`, `connection`, `chat_thread`, `chat_message`. Conventions per [Data Model Overview](/OstadLagbo/data-model-overview.md). This model holds the platform's success unit — the connection — and the relationship machinery around it. Its central design commitment: **`offer` is transient, `connection` is permanent.** An offer is a request that resolves one way or another; a connection is a fact that, once true, is never untrue (Overview rule 2). Revised 2026-09-13 after the cross-layer review: reminder flag added; symmetric purge of non-accepted offers; the retention claim about SGP-DM corrected. Revised 2026-09-25: inbox-display clarification vs OFR-06 (below).

**Identifier convention for this model:** every party reference is a `user_account` id (the identity spine, Overview rule 1). Where an Ostad's *profile* is needed for a join, `ostad_profile_id` is carried additionally — never instead.

## offer

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| shagred_account_id | uuid → user_account | The sender; always role = shagred (OFR-01: Ostads cannot initiate) |
| ostad_account_id | uuid → user_account | The recipient's account |
| ostad_profile_id | uuid → ostad_profile | The recipient's profile, for joins |
| message | text | Free text, proposed cap 500 chars (OFR-01); becomes the first chat message on acceptance (OFR-04) |
| status | enum: `pending` \| `accepted` \| `declined` \| `expired` \| `withdrawn` | State machine below |
| created_at | timestamp | Also the expiry anchor |
| expires_at | timestamp | `created_at` + 7 days; **immutable once set** |
| reminder_sent_at | timestamp, nullable | Set by the day-5 reminder job (OFR-03) so it fires once; null until then |
| resolved_at | timestamp, nullable | Set on any terminal transition |
| resolution_source | enum: `ostad` \| `shagred` \| `expiry_job` \| `deletion` \| null | Who or what resolved it — distinguishes a Shagred's withdraw from a deletion-triggered one, for analytics |

**Constraints:**
- **One pending offer per (shagred, ostad) pair:** partial unique index on (`shagred_account_id`, `ostad_account_id`) where `status = pending`. Enforces OFR-01 structurally.
- **Global cap of 5 pending per Shagred:** a count-check at creation, not a constraint (counts aren't expressible as unique indexes) — the service layer refuses the 6th. Acknowledged limitation: a race between two simultaneous creations could theoretically admit a 6th; acceptable at MVP scale.
- **Recipient eligibility at creation:** the discoverability predicate (OSP-DM) minus the viewer-block clause, plus a separate block check — evaluated at insert, never cached (OFR-01, OSP-11).

### Offer state machine

```
                    ┌──────────► accepted ──► (connection created)
                    │
   pending ─────────┼──────────► declined      (Ostad action, or Ostad's deletion request / termination)
                    │
                    ├──────────► withdrawn     (Shagred action, or Shagred's deletion request / termination)
                    │
                    └──────────► expired       (scheduled, at expires_at)
```

`pending` is the only non-terminal state. **Terminal states are immutable** — no transition leaves them (OFR-02). Expiry is a **scheduled transition**: a job runs against `expires_at`, so it fires whether or not either party opens the app (OFR-02 acceptance). Re-offering after any terminal state is a **new row**, never a reopened one.

**Suspension (ADM-08):** `accept`/`decline`/`withdraw` are refused while either account's status is `suspended` — a service-layer check against `user_account.status`, not a stored offer state — but `expires_at` keeps running; a pending offer may expire during a suspension.

**Deletion request or termination (REG-12, CL-019, OL-RET-001):** at the moment an account enters `pending_deletion`, or is terminated, every pending offer it is party to resolves immediately — `withdrawn` if the affected account is the sender, `declined` if it is the recipient Ostad — with `resolution_source = deletion`. **Recovery within the 30-day window does not restore them**; re-offering is one action, while a resurrected stale offer would confuse both parties. Accepted offers are untouched (the connection governs them).

## connection

Created by exactly one event: an offer's transition to `accepted`. No other path creates one.

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| offer_id | uuid → offer | The accepted offer; 1:1 |
| shagred_account_id / ostad_account_id | uuid / uuid → user_account | Copied from the offer at creation — **denormalized deliberately** so the connection stands alone as a fact if the offer row is later purged. These references remain valid after a party purges, because REG-DM retains purged accounts as tombstone rows |
| ostad_profile_id | uuid, nullable → ostad_profile | For joins; nulled when the profile row is deleted at the Ostad's purge |
| connected_at | timestamp | The acceptance timestamp; feeds `ostad_history_entry.connected_at` (SGP-DM) and ADM-12's connection count |
| shagred_display_name_snapshot / ostad_display_name_snapshot | string / string | Captured at creation so the record stays readable after either party purges |
| anonymized | boolean | Set when a party purges (retention, below) |

The thread is reached from the connection through `chat_thread.connection_id` — one direction only; the connection carries no back-reference.

**What acceptance does atomically (OFR-04):** insert `connection` → insert `chat_thread` → insert the offer's message as the first `chat_message` (kind `text`, sender = the Shagred — it is their words) → update `offer.status = accepted` → insert `ostad_history_entry` (SGP-DM). **Five writes, one commit**; partial success is not a valid state. The connection analytics event is emitted after commit.

**Contact reveal is a read rule, not a stored copy.** Phone and verified email are revealed mutually on acceptance (OFR-04, CL-011) — but nothing is copied onto the connection. The chat header reads `user_account.phone` and `user_account.email` (where `email_verified_at` is set) for the counterpart, and the policy layer permits that read **iff a connection exists between the two accounts and no block exists**. Copying would create a second source of truth that goes stale on phone change (REG-07) and would survive a block. "Irreversible" (OFR-04) is about the human having seen it, not the schema retaining it.

## chat_thread

One per connection; created atomically with it.

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| connection_id | uuid → connection | 1:1; the only link between the two |
| participant_a_account_id / participant_b_account_id | uuid / uuid → user_account | **Exactly two participants**, fixed at creation — the structural basis of OFR-07's "readable only by its two participants." There is no third slot |
| last_message_at | timestamp, nullable | Denormalized cache for inbox ordering; maintained on message insert; recomputable from `chat_message` |
| block_frozen_at | timestamp, nullable | Set when either participant blocks the other; **not cleared on unblock** — the thread stays frozen (RNT-08, CL-023), cleared only when a new accepted offer forms a new connection. null = writable, subject to the suspension/deletion predicate |

**Freeze state — block is stored, suspension/deletion are predicate.** Whether a thread accepts new messages combines one **stored** flag (block) with query-time predicates (suspension, deletion). `chat_thread` gains a nullable `block_frozen_at` timestamp for this.

```
thread is writable  iff
  chat_thread.block_frozen_at is null                            (RNT-08, stored)
  AND neither participant's user_account.status is suspended     (ADM-08)
  AND neither participant's user_account.status is pending_deletion or purged   (OFR-06)
```

**Block is persistent (CL-023, RNT-08).** Blocking sets `chat_thread.block_frozen_at` on the pair's thread and it is **not** cleared by unblocking — unblocking restores only discoverability, so the old thread stays frozen. Messaging resumes only when a **new offer is accepted** between the two accounts, which forms a new connection and clears `block_frozen_at` (a fresh, writable thread). **Suspension and deletion stay query-time:** a suspended participant freezes the thread until reinstated; a deletion/termination tombstone freezes it permanently. A frozen thread is readable by participants (history persists) and rejects inserts; the UI derives the "why frozen" message from the failing clause (block / suspended / deleted).

## chat_message

| Field | Type | Rules |
|---|---|---|
| id | uuid | |
| thread_id | uuid → chat_thread | |
| kind | enum: `text` \| `voice` | The offer's first message is `text`. **There is no `system` kind** — a freeze is conveyed by the thread's frozen state and a neutral client banner, never by a stored message (CL-030) |
| sender_account_id | uuid → user_account | **Required, and constrained to the thread's two participants at the database level** |
| body | text, nullable | Required for `text`; null for `voice` |
| voice_ref | storage ref, nullable | Required for `voice`; null otherwise. Compressed, ≤2 min (OFR-05 default; NFR-04 budget) |
| voice_duration_seconds | int, nullable | ≤120 enforced by constraint |
| sent_at | timestamp | |
| delivered_at / read_at | timestamps, nullable | Message states (OFR-05 engineering default); with exactly two participants, `read_at` unambiguously means the counterpart read it |

**Immutability (OFR-05, CL-015):** no update or delete path exists for `chat_message` from any user-facing interface. Messages are moderation evidence; the only mutations are the delivery/read timestamps and retention purges.

## Read rules the policy layer enforces (OFR-07)

- A thread and its messages are readable **only** by its two participants — checked on every read against `participant_a/b_account_id`.
- A thread failing the writable predicate is readable by participants but rejects inserts.
- **Admin never reads a thread directly.** The only admin read path originates from a `report` (RNT) citing specific `chat_message` ids: the policy layer returns those messages plus ±N neighbors in the same thread (N = engineering default, proposed 10) and **writes a `chat_context_viewed` audit entry** (ADM-DM) as a side effect. No endpoint accepts a bare `thread_id` from an admin surface.
- A **block** between participants freezes the thread via the predicate *and* removes the counterpart's contact details from the chat header — the reveal read rule requires no block.

## Notification delivery (OFR-03)

Every push this module emits — offer received, day-5 reminder, accepted, declined, new message — resolves the recipient's active `device_push_token` rows (REG-DM) and renders in `user_account.preferred_locale`. In-app counterparts (inbox states, badges) are derived from this model's rows, not from delivery status, so a user with notifications denied misses nothing.

## Inbox reads (OFR-09)

**Shagred sent-offers list:** `offer where shagred_account_id = :me`, ordered `created_at desc`, each with live `status` and, for pending, `expires_at` (client renders "N days remaining"). **Ostad received-offers list:** `offer where ostad_account_id = :me`, pending first ordered `expires_at asc` (soonest-to-expire on top), then resolved. **Chat list (both roles):** `chat_thread where :me ∈ participants`, ordered `last_message_at desc`, each with the counterpart's display name (the live profile where it exists; a counterpart in `pending_deletion` or `purged` shows to the other participant as **"deleted account"** per OFR-06) and an unread count (`chat_message where read_at is null and sender_account_id ≠ :me`).

**Snapshot vs. live display (clarification, 2026-09-25).** The `shagred_display_name_snapshot` / `ostad_display_name_snapshot` on `connection` back the connection **record** — keeping it readable for admin, history (SGP-DM), and analytics after a party purges. They are **not** the live inbox/chat display shown to the *other participant*: once a counterpart enters `pending_deletion` or `purges`, that participant sees them as **"deleted account"** (OFR-06), not the snapshot name. The two surfaces serve different readers.

## Retention behavior (OL-RET-001 mapping)

| Entity | Rule |
|---|---|
| offer | **Declined / expired / withdrawn:** retained 12 months for analytics, then aggregate-only. **Accepted:** retained as long as its connection exists. **Non-accepted offers purge at day 30 when *either* party purges** — they are both parties' data, and neither the sender's nor the recipient's leaving should leave a dangling request on the other's list |
| connection | **Persists, anonymized.** When either party purges (day 30), `anonymized = true`; the account references stay valid (REG-DM tombstones) and the display-name snapshots carry the display. The row is deleted only when **both** parties have purged **and** no rating references it (RNT-05). *(Corrected 2026-09-13: the earlier claim that an anonymized `shagred_profile` persists on the strength of connection references was wrong — connections reference the account tombstone, not the profile; the profile purges outright, per SGP-DM.)* |
| chat_thread + chat_message | **Persist while either participant's account exists.** When one party deletes, the thread freezes via the predicate; their messages remain readable to the other with the sender shown as "deleted account" (OFR-06). **Full thread purge 90 days after the second party is gone.** Voice-note storage objects delete with their message rows in the same operation; orphans swept by ADM-18; out of backups within 90 days (NFR-07) |
| Legal hold | A `legal_hold` on either account (REG-DM) suspends every purge above for the offers, connection, and thread involving that account, until released |

## Queries this model must serve

Pending-offer existence per pair (partial unique index); pending-offer count per Shagred (the 5-cap); offer-creation eligibility (discoverability predicate + block + suspension + pause, all at insert); the **expiry job** (`offer where status = pending and expires_at ≤ now`, batched) and the **day-5 reminder job** (`pending and created_at + 5d ≤ now and reminder_sent_at is null` — OFR-03); deletion-request and termination offer resolution (all pending offers for an account, in one transaction with the account change); the acceptance transaction (five writes, one commit); the thread-writable predicate on every message insert; participant check on every read; unread counts per thread; report-context read (message ids → ±N neighbors, audit-logged); counterpart contact reveal (connection exists ∧ no block); both inbox reads; push-token and locale resolution for every notification; connection counts and offer-outcome shares for ADM-12/13 and OSP-12 (from analytics events, cross-checkable against this model).
