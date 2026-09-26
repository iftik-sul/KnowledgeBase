---
project: OstadLagbo
module: ratings-and-trust
type: ui
status: current
updated: 2026-09-26
id: OL-RNT-UI-001
derived_from: /OstadLagbo/modules/ratings-and-trust/requirements/ratings-and-trust-requirements.md
owner: Iftikher
---

# Ratings & Trust — UI

Screens for rating an Ostad, the Ostad's reply, reporting across every reportable surface, and blocking with its private list. Conventions per [UI Overview](/OstadLagbo/ui-overview.md); behaviour and endpoints per [RNT API](/OstadLagbo/modules/ratings-and-trust/api/ratings-and-trust-api.md); the profile the reviews sit on is OSP ui; the surfaces that invoke report/block are OSP, SGP, and OFR ui.

This module owns two shared surfaces every other module reaches into: the **report sheet** and the **block action**. Both **resolve a person from the handle the caller holds** (an `ostad_id`, a `shagred_id`, or — for a lapsed Shagred — an `offer_id`), and neither ever returns another user's account id or a reporter's identity.

## Group A — Rating an Ostad (RNT-01, 02, 03, 05)

### Rate / edit your review
- **Purpose:** a Shagred who has connected with an Ostad leaves or edits their one review.
- **Shell:** Shagred — reached from the **Ostad's public profile** (a "Rate this Ostad" affordance, or "Edit your review" when one exists) once a **connection** exists; also linkable from a connection/chat.
- **Structure:** a **1–5 star** selector (required) and a **written review** (required, ≤600 chars, counter) — star-only cannot be submitted (RNT-02).
- **Eligibility & states:** the affordance appears **only when the Shagred holds a connection** with this Ostad (accepted offer — unlocks immediately on connecting, RNT-01); no connection → no rating path (`forbidden`); **one rating per pair, ever** — a second attempt is refused (`conflict`), and this holds even after an admin removes a review (the slot stays consumed, RNT-06); editing is **unlimited** and recomputes the aggregate live.
- **States:** **loading** → submit disabled with progress; the idempotency key means a double tap cannot consume the one-per-pair slot twice. **Empty** → not applicable; the form is the content. **Error** → `forbidden` (no connection) should be unreachable, since the affordance is only rendered with a connection — if it appears, the client says the rating isn't available rather than explaining the eligibility rule; `conflict` (the slot is already used) switches the screen to **edit** the existing review instead of refusing; `state_conflict: rating_removed` shows *"this review was removed by moderation"* and offers no resurrection; a lost connection **preserves the typed review** and retries (NFR-02) — a 600-character review lost to a dropped request is the kind of failure that stops someone reviewing again.
- **Data & actions:** `POST /v1/ratings {ostad_id, stars, review_text}` (idempotency key); `PATCH /v1/ratings/{id}` to edit. If the review was **removed by moderation**, edit returns `state_conflict: rating_removed` → the client shows "this review was removed by moderation" and offers no resurrection.
- **No delete:** there is **no** user action to delete a review (RNT-05) — account-cycling cannot erase it; only admin removal does.

## Group B — The reviews list and the Ostad's reply

### Reviews list (component on the public profile)
- **Where:** the reviews section of the Ostad's public profile (OSP ui); this module owns the component.
- **Structure:** reviews `created_at` newest first — each with its **stars**, **written review**, the reviewer's **first initial only** (e.g. **"R."** — never the full name; CL-028), the date, and the **Ostad's reply beneath** where present. The viewer's **own** review (if any) is marked for quick **Edit** (Group A).
- **States:** **loading** → skeleton rows inside the profile, so the rest of the profile renders without waiting on reviews. **Empty** → **"New"** rather than a zero score (MAP-02 uses the same treatment on preview cards) — a new Ostad must not look badly rated. Where the viewer holds a connection, the empty state carries the **Rate this Ostad** action. **Error** → the reviews section alone shows a retry; a failed reviews read never blocks the profile around it.
- **Data:** `GET /v1/ostads/{id}/ratings` (removed reviews never appear; readable when the profile is — approved incl. paused, else "not available").

### Ostad reply
- **Purpose:** the Ostad answers a review, once, publicly.
- **Shell:** Ostad — from their own reviews (on their profile).
- **Structure:** a reply field (≤600 chars) beneath the review; edit in place.
- **States:** **one reply per review** — a second is refused (`conflict`); a reply to a **removed** review is refused (`state_conflict: rating_removed`); a reply is **removed automatically** if its review is removed (it simply disappears).
- **Data:** `POST` / `PATCH /v1/ratings/{id}/reply`.

## Group C — Reporting (RNT-07)

### Report sheet (shared surface)
- **Purpose:** any registered user flags content for moderation; invoked from every reportable surface.
- **Invoked from (each passes the right handle):** an **Ostad profile** (`ostad_id`; any registered user); a **Shagred** — always by the **`offer_id`** of the specific offer, since every context in which an Ostad sees a Shagred (a received offer, a chat) sits inside an offer/connection, and that offer's message is the report's evidence (`via_offer_id`); it works whether the card is still visible or has lapsed, and only an Ostad who holds/held the offer can (OFR/SGP ui); a **chat message** (its overflow action, citing that message — OFR ui); a **review** or **reply** (`rating`/`rating_reply`; any registered viewer). *(The API also accepts a bare `shagred_id` while the Shagred is visible; the UI has no context that needs it.)*
- **Structure:** a **category** picker — *Fake profile / Inappropriate content / Harassment / Scam or fraud / Safety concern / Other* — and a free-text **detail** field, **required when the category is Other**; submit.
- **States:** guests never see a report action (they are registered first, MAP-03); a **duplicate open report** on the same target is refused (`conflict`); a target that no longer exists or is hidden by a block returns the neutral "not available" (`not_found`, opacity).
- **Data & actions:** `POST /v1/reports {target_type, target_id | offer_id, category, detail?, cited_message_ids?}` → `{status: "open"}`, a brief "thanks, our team will review this" acknowledgement.
- **Never shows:** the report is **one-way** — the reporter is **never** shown its resolution, and their identity is **never** revealed to the reported account or anyone but admin (RNT-07). A hidden-Shagred report resolves the Shagred server-side; the reporter never re-sees the profile.

## Group D — Blocking (RNT-08)

### Block action
- **Purpose:** cut all contact and visibility with another user, immediately.
- **Invoked from:** an **Ostad profile** (any registered user may block any Ostad); a **Shagred** — by the **`offer_id`** from the received-offer entry or chat (an Ostad who received their offer), visible or lapsed alike; either party of a connection may block the other (a Shagred blocks their Ostad by `ostad_id`).
- **Structure:** a short confirmation naming what blocking does — **the chat freezes to read-only, you each vanish from the other's discovery and profile, and no new offer can pass either way** — and that it is reversible from Settings. Confirm / cancel.
- **States:** re-blocking an already-blocked pair is a no-op success; a self-block is refused (`validation_failed`); an Ostad blocking a Shagred with **no offer between them** is refused (`forbidden`); every effect lands **within one request cycle** via the other modules' predicates (chat freeze OFR, visibility SGP, discovery/favourites MAP).
- **Data & actions:** `POST /v1/blocks {ostad_id | shagred_id | offer_id}` (idempotency key).
- **Never shows:** **the blocked party is never notified** and no screen ever tells them a block exists — the effects present only as absence (no pin, no profile, a neutral frozen chat), per the opacity rule everywhere.

### Block list (Settings)
- **Shell:** both roles → Profile/Settings → **Blocked users**.
- **Structure:** the caller's **private** list — each blocked party's profile card and the date; an **Unblock** action. This is the **only** surface anywhere that reveals a block, and only to its author.
- **States:** **Unblock** restores discovery and favourites (the pins/entries reappear), but **frozen chats stay frozen** — a new connection needs a new offer (RNT-08). Only the blocker can unblock.
- **Data & actions:** `GET /v1/blocks`; `DELETE /v1/blocks/{id}`.

## Trust signals (RNT-09)

The **verified badge** is displayed wherever a profile or card appears (OSP/MAP/SGP components) and is granted **solely** by admin (ADM-03); this module adds no other badge. Profile completion is OSP's.

## Flows

**Rate after connecting.** A connection exists → the Ostad's profile shows "Rate this Ostad" → stars + written review → submit → the aggregate updates live; later, "Edit your review" revises it. A second, separate rating is impossible — one per pair, forever.

**Report a review.** A viewer opens an Ostad's reviews → a review looks fake → the review's report action opens the sheet (`target_type: rating`) → category + detail → submit → a thank-you; the reporter never learns the outcome, and if admin removes it, the review and any reply vanish from the profile and aggregate while the pair's slot stays consumed.

**Block a pestering Shagred.** A declined offer's entry (no Shagred identity) → **Block** via the offer id → confirm → within one request cycle they can send no new offer and each is invisible to the other → later, from **Blocked users**, Unblock restores discovery but the old chat, if any, stays frozen.

## What this module's screens never show

No screen reveals a reporter's identity, or a report's resolution, to anyone but admin; no screen tells a blocked party a block exists, or lets anyone but the blocker see or lift it; no screen returns another user's account id (report and block resolve the handle server-side); no screen deletes a rating or reply, lets a user edit another's, or edit content admin has removed; no rating path exists without a connection, or a second time for a pair; and no guest can rate, reply, report, or block.
