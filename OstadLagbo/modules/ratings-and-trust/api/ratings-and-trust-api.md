---
project: OstadLagbo
module: ratings-and-trust
type: api
status: current
updated: 2026-09-25
id: OL-RNT-API-001
derived_from: /OstadLagbo/modules/ratings-and-trust/requirements/ratings-and-trust-requirements.md
owner: Iftikher
---

# Ratings & Trust — API

Endpoints for ratings and their replies, reporting, and blocking. Conventions per [API Overview](/OstadLagbo/api-overview.md); entities, the block predicate, and eligibility rules per [RNT Data Model](/OstadLagbo/modules/ratings-and-trust/data-model/ratings-and-trust-data-model.md). This module writes the `block` row that four other models read as a predicate, and it is the endpoint the OFR api hands its **offer-id-targeted** report and block to — where an Ostad acts on a Shagred whose identity has already lapsed and the API resolves the account server-side without re-exposing them.

## The resolution rule, stated once

Reports and blocks name a **person**, but the client never holds that person's account id (identifier rule). Every write here therefore accepts the handle the caller actually has and **resolves the account server-side**:

- an **`ostad_id`** (public profile id) — anyone holds it;
- a **`shagred_id`** (profile id) — an Ostad holds it only while the Shagred is visible (SGP-05);
- an **`offer_id`** — the Ostad's own party object, held **after visibility has lapsed**; only the Ostad recipient of that offer may use it, and the API resolves it to the Shagred's account (and, for a report, to the `shagred_profile` target) without returning who they are. **For a report, the offer is also retained on the report as `via_offer_id`** (RNT-DM), so the moderator can read the offer's message as evidence — the target stays `shagred_profile`; `via_offer_id` is an evidence pointer, not the target.

This is how an Ostad reports or blocks the sender of a declined, expired, or withdrawn offer (the OFR handoff). The resolved `reported_account_id` / `blocked_account_id` is stored; it is never sent back to any user. Any write whose resolved target is the caller themself is rejected (`validation_failed` — `blocker ≠ blocked`, no self-report).

## Endpoints — ratings (RNT-01, 02, 03, 05)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/ratings` | A **Shagred** who **holds a connection** with the Ostad (accepted offer — the eligibility proof, RNT-01); accepts `Idempotency-Key` | `{ ostad_id, stars, review_text }` — `stars` 1–5, `review_text` **required** (≤600 chars); star-only is refused (RNT-02) | The created `rating`; the API sets `connection_id` to the pair's connection as proof and recomputes the Ostad's `rating_avg`/`rating_count` (RNT-03) | `validation_failed` (stars outside 1–5, empty or oversized review); `forbidden` (caller is not a Shagred, or holds no connection with this Ostad — rating is gated on connection); `conflict` (a rating for this pair already exists, **including a removed one** — the slot is consumed, RNT-06); `not_found` (no such Ostad — opacity) |
| `PATCH /v1/ratings/{id}` | The **author** Shagred (RNT-01) | `{ stars?, review_text? }` | The updated rating; `updated_at` stamped; aggregate recomputed | `validation_failed`; `state_conflict` (`reason: "rating_removed"` — see below); `not_found` (not the author, or no such rating) |
| `GET /v1/ostads/{id}/ratings` | **Anyone, incl. guests** (reviews are public, MAP-03) — readable exactly when the Ostad's public profile is (approved, **including paused**); `not_found` otherwise | `?limit=&cursor=` | The Ostad's reviews where `removed_at IS NULL`, `created_at desc`, each with `stars`, `review_text`, date, the reply where present, and the reviewer's **`reviewer_initial`** (e.g. `"R."`) — never the full name (CL-028). The caller's own review (if any) is flagged `own: true` so the client offers edit | `not_found` (Ostad suspended, unapproved, or purged — opacity) |

**No user can delete a rating** (RNT-05): there is no `DELETE`. Account-cycling cannot erase a review; only admin content removal (ADM-07) sets `removed_at`, and even then the row persists and keeps the pair's slot consumed (RNT-06). Editing is unlimited and always recomputes the aggregate.

**Actions on a removed rating are refused.** Once admin has set `removed_at`, `PATCH /v1/ratings/{id}` and any reply write return `state_conflict` (`reason: "rating_removed"`) — an author's edit can never resurrect moderation-removed content into display or the aggregate, and the removal stays final (RNT-06).

## Endpoints — the Ostad's reply (RNT-04)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/ratings/{id}/reply` | The **Ostad** who received the rating (`rating.ostad_account_id`); accepts `Idempotency-Key` | `{ reply_text }` — ≤600 chars | The created `rating_reply`, shown beneath the review | `validation_failed`; `conflict` (a reply already exists — one per review, structurally); `state_conflict` (`reason: "rating_removed"`); `not_found` (not the Ostad, or no such rating) |
| `PATCH /v1/ratings/{id}/reply` | The reply's Ostad | `{ reply_text }` | The updated reply | `validation_failed`; `state_conflict` (`reason: "rating_removed"`); `not_found` |

A reply carries no rating value and is **removed automatically when its rating is removed** (cascade, RNT-04) — there is no user delete path and no way for an orphaned reply to render.

## Endpoints — reporting (RNT-07)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/reports` | Any **registered** user (a guest has no token → `unauthorized`; the client routes them to registration, RNT-07). Per-target eligibility below; accepts `Idempotency-Key` | `{ target_type, target_id \| offer_id, category, detail?, cited_message_ids? }` | `{ id, status: "open" }` — the report enters ADM-07's queue; `reported_account_id` is resolved and stored, **never returned** | `validation_failed` (missing `detail` when `category = other`; empty `cited_message_ids`, or ids spanning more than one thread, for a `chat_message` report; self-report; malformed target); `forbidden` (caller not eligible for this target — below); `conflict` (an **open** report by this reporter on this target already exists — RNT-DM); `not_found` (target does not exist, or a block hides it — opacity) |

**`target_type` values and who may report each** (RNT-07):

- **`ostad_profile`** (`target_id` = `ostad_id`) — any registered user.
- **`shagred_profile`** — an Ostad who **holds or has held** an offer from that Shagred (offer-history check, *any* status — reportability does not lapse with visibility, RNT-DM). Addressed by **`shagred_id`** while visible, or by **`offer_id`** once identity has lapsed; the API resolves either to the `shagred_profile` target and the Shagred's account, and when addressed by `offer_id` stores that offer as `via_offer_id` so the moderator can read its message as evidence (ADM api).
- **`chat_message`** (`target_id` = the primary message; `cited_message_ids` ≥1, including `target_id`, **all in one thread the reporter participates in**) — a **participant** of that thread. This array is the *only* thing that later unlocks the admin's ±10-message context read (OFR-DM, ADM-07); the thread is derived from it, never supplied.
- **`rating`** / **`rating_reply`** (`target_id` = that row) — any registered viewer.

**Reporter anonymity is absolute** (RNT-07): no endpoint anywhere returns `reporter_account_id` to any user, including the reported account — it is served only to admin surfaces (ADM api). A reporter is not shown their report's later resolution; reports are one-way into moderation. *(Judgment call — if reporters should track their own reports, that is a scope addition; flagged.)*

## Endpoints — blocking (RNT-08)

| Endpoint | Caller & policy check | Request | Response | Errors |
|---|---|---|---|---|
| `POST /v1/blocks` | Any **registered** user; accepts `Idempotency-Key` | one of `{ ostad_id }` / `{ shagred_id }` / `{ offer_id }` (resolution rule above) | `{ id }` — an active `block` row; **naturally idempotent** (re-blocking an active pair returns the same success, no `conflict`). Every effect — chat freeze, visibility severance, discovery/favorites hiding, offer refusal, contact-reveal withdrawal — lands within this request cycle via the other models' predicates (RNT-08) | `validation_failed` (self-block); `forbidden` (an Ostad blocking a Shagred with no offer between them — the only gated case; a Shagred cannot reach another Shagred to block, so no such path exists); `not_found` (no such target — opacity) |
| `GET /v1/blocks` | The blocker | `?limit=&cursor=` | The blocker's **private** block list: each entry the blocked party's profile projection and `created_at`. This is the only surface that reveals a block, and only to its author (RNT-08) | — |
| `DELETE /v1/blocks/{id}` | The **blocker** only (RNT-08) | — | `204` — sets `revoked_at`; discovery and favorites reappear via the predicates, but **frozen chats stay frozen** (a new connection needs a new offer, RNT-08); idempotent | `not_found` (not the blocker, or no such block) |

**Who may block whom** (RNT-08): any registered user may block any Ostad from a profile (including an Ostad blocking another Ostad); an Ostad may block any Shagred whose offer they received; either party of a connection may block the other. **The blocked party is never notified** and no read path exposes to them that a block exists — the effects present only as absence (no pin, no profile, a frozen chat with no stated cause on their side; API Overview opacity rule).

## Instrumentation (RNT-10)

Written **server-side by the API** at the moment of each action, under the overview's analytics rules:

- **Ratings** — created and edited, with star value, and review participation measured against the pair's connection (so ADM-15 can track what share of connections leave a review).
- **Reports** — created, tagged by `category` and `target_type` (surface). **Report *outcomes*** are emitted by the ADM api on resolution (it owns the resolution write), cross-checkable against this module's rows.
- **Blocks** — created and reversed.

## Effects owned elsewhere (named for completeness)

- **Report resolution** — the queue, the verdict (`dismissed`/`warned`/`suspended`/`content_removed`), the `moderation_action`, and the audit entries are the **ADM api**. `content_removed` on a `rating`/`rating_reply` sets `removed_at` here and recomputes the aggregate.
- **The block predicate** — written here, read by OSP (discoverability), SGP (visibility), MAP (discovery + favorites), and OFR (thread writability + contact reveal). This module never enforces those effects itself; it only owns the row they all check.
- **The verified badge** is granted solely by ADM-03; this module adds no badges (RNT-09).

## Flows

**Rate after connecting.** Offer accepted → connection exists → the Shagred opens the Ostad profile → `POST /v1/ratings {ostad_id, stars, review_text}` → the aggregate on `GET /v1/ostads/{id}` updates → later `PATCH /v1/ratings/{id}` to revise, recomputing again. A second `POST` for the same Ostad returns `conflict` — one rating per pair, forever.

**Block from a lapsed offer.** An Ostad's received-offers list shows a withdrawn offer with no Shagred identity (OFR) → the Ostad taps "block" → `POST /v1/blocks {offer_id}` → the API resolves the Shagred's account, writes the block → from the next request cycle the two are invisible to each other everywhere and no new offer can pass either way. The Shagred is never told.

**Report a review, then admin removes it.** A viewer taps "report" on a review → `POST /v1/reports {target_type: "rating", target_id, category, detail}` → it enters ADM-07's queue → an admin resolves `content_removed` (ADM api) → `removed_at` is set here, the review and its reply vanish from `GET /v1/ostads/{id}/ratings` and the aggregate, but the row persists and the pair's rating slot stays consumed; a later edit attempt by the author returns `state_conflict: rating_removed`.

## What this module does not expose

No endpoint returns a reporter's identity to anyone but admin; no endpoint tells the blocked party a block exists, or lets anyone but the blocker see or revoke it; no endpoint returns another user's account id (reports and blocks resolve handles server-side); no endpoint deletes a rating or reply, or lets a user edit another's, or edit content admin has removed; no rating can be created without a connection, or a second time for a pair; no guest can rate, reply, report, or block; and reviews persist through blocks and account deletion (anonymized), removable only by admin.
