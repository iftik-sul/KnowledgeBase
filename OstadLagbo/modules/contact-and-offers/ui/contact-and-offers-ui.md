---
project: OstadLagbo
module: contact-and-offers
type: ui
status: current
updated: 2026-09-26
id: OL-OFR-UI-001
derived_from: /OstadLagbo/modules/contact-and-offers/requirements/contact-and-offers-requirements.md
owner: Iftikher
---

# Contact & Offers — UI

Screens for sending an offer, the two offer inboxes, the accept/decline/withdraw actions, the 1:1 chat, and contact reveal. Conventions per [UI Overview](/OstadLagbo/ui-overview.md); behaviour and endpoints per [OFR API](/OstadLagbo/modules/contact-and-offers/api/contact-and-offers-api.md); the Ostad profile a Shagred offers from is OSP ui; the Shagred card an Ostad sees is SGP ui; report and block are RNT ui.

Two shapes govern everything here: **only a Shagred initiates** (an Ostad has no contact-initiation surface anywhere), and **`offer` is transient while `connection` is permanent** — the offer inbox is where offers live and die; the chat is where a connection lives on.

## Group A — Sending an offer (OFR-01)

### Send offer
- **Purpose:** a Shagred sends a free-text message to an Ostad to start a connection.
- **Shell:** Shagred — from an **Ostad's public profile** (OSP ui) and preview card.
- **Structure:** a free-text message field (≤500 chars, counter shown); a note that the Ostad will see the Shagred's profile once sent (SGP-05), and that **if the Ostad accepts, the Shagred's phone number and any verified email will be shared with them (and the Ostad's with the Shagred)** — the informed-consent counterpart to the Ostad's acceptance confirmation (OFR-04); send.
- **States — the action is disabled or refused before it is sent where possible:** **paused Ostad** → the offer action is disabled with the not-accepting notice (`state_conflict: ostad_not_accepting`); **incomplete Shagred profile** → routed to Shagred setup (`state_conflict: profile_incomplete`, SGP ui); **a pending offer to this Ostad already exists** → the action points to the existing offer (`conflict: duplicate_pending_pair`); **five pending offers already** → a clear "resolve one first" message (`conflict: pending_limit_reached`); a blocked/absent Ostad → the profile was already "not available" (opacity).
- **States:** **loading** → the send action shows progress and is disabled, so a double tap cannot produce two offers (the idempotency key is the guarantee; the disabled button is the courtesy). **Empty** → not applicable; the composer always has content to show. **Error** → `state_conflict: pending_offer_exists` explains an offer to this Ostad is already open and links to it; `state_conflict: offer_cap_reached` names the 5-pending cap and links to Sent offers to withdraw one; `state_conflict: profile_incomplete` routes to Shagred setup and returns here; `forbidden` (blocked, paused, suspended, or no longer discoverable) shows one neutral **"This Ostad isn't available right now"** — never distinguishing a block from a pause, per RNT-08 opacity. On a dropped connection the message is **queued and retried** (NFR-02), never silently lost.
- **Data & actions:** `POST /v1/offers {ostad_id, message}` (idempotency key) → a `pending` offer; the Ostad is pushed "offer received"; the Shagred lands in their sent-offers inbox on the new item.
- **Never shows:** no Ostad-initiated equivalent exists — there is no "message this Shagred" anywhere (OFR-01).

## Group B — The offer inboxes (OFR-09)

The **Offers** tab, one per role, with badge counts (OFR-03 notification principle).

### Sent offers — Shagred
- **Shell:** Shagred shell → **Offers** tab.
- **Structure:** every offer the Shagred sent, `created_at` newest first, each with the **Ostad** card (public: photo, name, verified badge) and its live state — **pending** (with "N days remaining"), accepted, declined, expired, withdrawn; tap-through to the Ostad profile always works.
- **Actions:** **Withdraw** on a pending item (`POST /v1/offers/{id}/withdraw`); an **accepted** item links into the chat; after a decline/expiry/withdrawal the Shagred **may re-offer immediately** (the Ostad profile's send action is live again — repeat-pestering is the Ostad's block to wield, not a cooldown).
- **States:** **loading** → skeleton rows. **Empty** → *"You haven't sent any offers yet"* with a one-tap **Find an Ostad** action returning to the map — the empty inbox is the Shagred's main activation surface, so it carries the next step rather than an apology (ui overview: never a blank screen). **Error** → a retry affordance keeping any already-loaded page; a withdraw that fails leaves the item pending and offers retry, never a state the server disagrees with.
- **Data:** `GET /v1/offers/sent`.

### Received offers — Ostad
- **Shell:** Ostad shell → **Offers** tab (the Ostad home).
- **Structure:** **pending offers first**, soonest-to-expire on top, each with "N days remaining" and **Take / Decline** actions, then resolved history. The **Shagred card depends on the offer's state:**
  - **pending / accepted** → the Shagred card shows (SGP ui: name, photo, gender, District + Thana, joined) with tap-through;
  - **declined / expired / withdrawn** → **no Shagred identity** — the card is gone; only the **offer message and dates** remain, with **Report** and **Block** actions that target the **offer id** (RNT ui resolves the Shagred; the Ostad never sees them again).
- **Actions:** **Take** → the acceptance confirmation (Group C); **Decline** (`POST /v1/offers/{id}/decline`, no reason required); Report/Block on any offer via the offer id.
- **States:** **loading** → skeleton rows, pending section first. **Empty** → for an **approved** Ostad, *"No offers yet"* with a line pointing at the things that earn them — completing the profile (OSP-09) and staying un-paused (OSP-11); for a **pending** Ostad, the review-status message instead, because no offer can arrive before approval and an empty inbox would otherwise read as failure. **Error** → retry, preserving loaded pages; a Take or Decline that fails leaves the offer pending and retryable.
- **Data:** `GET /v1/offers/received`.

**Transitions are retry-safe:** re-tapping Take on an already-accepted offer opens the existing connection; a `state_conflict` appears only when the offer has since moved to a *different* terminal state (e.g., it expired before the Ostad tapped) — the client shows that state and refreshes the list.

## Group C — Acceptance (OFR-04)

### Acceptance confirmation
- **Purpose:** the Ostad confirms, understanding that contact details will be exchanged.
- **Entry:** **Take** on a pending received offer.
- **Structure:** a confirmation that plainly states **your phone number and any verified email will be shared with this Shagred, and theirs with you — this cannot be undone** (OFR-04; a consent surface). Confirm / cancel.
- **States:** **loading** → confirm disabled with progress while the five-write acceptance transaction commits; it either completes or does not, so there is no partial state to render. **Error** → `state_conflict` (withdrawn, expired, or already resolved while this screen was open) explains what changed and returns to Received offers, refreshed — the commonest real case, since an offer can expire between opening the screen and confirming; `forbidden` (the Shagred deleted, was suspended, or a block landed) shows the neutral unavailable copy and dismisses.
- **Data & actions:** confirm → `POST /v1/offers/{id}/accept` (idempotency key) → the connection, the chat thread, and the offer message as its first message are created together; contact is now revealed both ways; the Shagred is pushed "accepted" → both parties land in the new chat.
- **Never shows:** contact **before** acceptance — a number is revealed only at this moment, never earlier (OFR-04).

## Group D — The chat (OFR-05, 06, 07)

### Chat thread
- **Purpose:** the 1:1 conversation for a connection — the connection's living surface.
- **Shell:** both roles → **Chats** tab → a thread.
- **Structure:** a **contact header/details** — the counterpart's name and photo, and their **revealed phone and verified email** (present only while a connection exists and no block stands; `null`/absent, shown as "deleted account", once the counterpart deletes — OFR-04/06); the message list (the **offer's text is the first message**, for context); and a **composer** for **text and voice notes only** — no images, documents, or video exist in the UI (OFR-05).
- **Voice-note messages** render an inline **player** — a play control and the duration — streamed from a short-lived signed URL; text messages render as bubbles.
- **Message states:** each message shows **sent / delivered / read** ticks; with exactly two participants, "read" means the counterpart read it. Delivery is a live Realtime channel (the API is the only writer; the client posts the message and the receipt).
- **Voice notes:** an in-app recorder **capped at 2 minutes**, compressed before upload; a longer recording cannot be sent (enforced client-side and re-validated server-side).
- **Frozen state (OFR-06):** when the thread is frozen — a **block**, a **suspension**, or the counterpart's **deletion** — the composer is replaced by a **banner** and the **history stays readable**; a send attempt returns `state_conflict: thread_frozen:unavailable` (block or suspension — neutral) or `:deleted` (CL-030). No freeze notice is ever written into the chat. **The banner respects opacity (RNT-08):** to the **blocked** party it is strictly neutral ("You can no longer message this person") and **never** attributes the freeze to a block; only the **blocker** — who placed it and sees it in their own block list — sees it framed as their own block; a **suspension** freeze is likewise neutral to the counterpart (moderation status never leaks); a **deletion** shows "deleted account" (OFR-06). Unblock or reinstatement restores the composer with no further step.
- **No edit or delete:** there is **no** message edit or delete action anywhere — chat history is moderation evidence (OFR-05, CL-015). Report is per-message via the message's overflow action (RNT ui, citing the message).
- **States:** **loading** → the header and the message list load separately; the header first, so the contact details a user opened the chat for are never behind the history. **Empty** → cannot occur: the offer text is always the first message (OFR-04). **Frozen** → a neutral banner and a disabled composer; the history stays readable (OFR-06). The banner never names a block (CL-030, RNT-08 opacity) — only `deleted` is disclosed, as **"deleted account"**. **Error** → a failed send marks that message **failed with a retry action**, leaving it in place rather than discarding what the user typed; `forbidden` on a thread that froze mid-session swaps the composer for the banner without losing scroll position; offline shows the indicator and keeps the loaded history readable (NFR-02). A voice note that fails to upload stays retryable and is never silently dropped.
- **Data & actions:** `GET /v1/chat/threads/{id}` (header + contact), `GET .../messages` (history, readable even when frozen), `POST .../messages` (text `{body}` or voice `{upload_id, duration}` via the upload-ticket flow), `POST .../receipts` (delivered/read). New messages push (suppressed while that chat is open on-screen).
- **Never shows:** the thread to anyone but its two participants; contact before acceptance or after a block; any edit/delete affordance; admin never appears here (admin sees cited messages only through a report, ADM ui).

## Group E — The chats inbox

### Chats list
- **Shell:** both roles → **Chats** tab.
- **Structure:** threads the user is in, most-recent activity first, each with the counterpart's name (live, or **"deleted account"** once they've left), photo where live, an **unread count**, the last-message preview, and a **frozen** indicator where applicable.
- **States:** **loading** → skeleton rows. **Empty** → for a Shagred, *"No conversations yet — send an offer to start one"* with the map action; for an Ostad, *"No conversations yet"* pointing at the Offers tab. A chat list is empty until a first offer is accepted, so for both roles this state is the **normal** early experience, not an error. **Error** → retry with loaded threads kept; offline keeps the list readable from cache with the offline indicator (NFR-02).
- **Data:** `GET /v1/chat/threads`. Unread badges derive from the data, so a notifications-denied user misses nothing (OFR-03).

## Notifications (OFR-03)

Push, each with an in-app counterpart: **Ostad** — offer received, a day-5 pending-expiry reminder; **Shagred** — accepted, declined; **both** — new chat message, suppressed while that chat is on-screen. No per-category preferences (OS-level only, CL-015); inbox states and unread badges are the in-app counterpart.

## Flows

**Offer to connection to chat.** Shagred opens an Ostad profile → **Send offer** (message ≤500) → the offer is pending in Sent offers; the Ostad is pushed → the Ostad's **Received offers** shows it with the Shagred card → **Take** → the acceptance confirmation (contact will be shared) → confirm → the chat opens for both, the offer text as its first message, phone and verified email in the header → they chat with text and voice notes.

**A declined, then reported, offer.** Shagred sends an offensive message → the Ostad **Declines** → in Received offers the entry now shows the message and dates but **no Shagred identity** → the Ostad taps **Report** → RNT ui files it against the offer id, resolving the Shagred without re-revealing them.

**A block freezes a live chat.** A participant blocks the other (RNT ui) → the chat's composer becomes a banner; both keep reading the history; the contact header clears → if the block is lifted, the composer returns immediately.

## What this module's screens never show

No screen lets an Ostad start contact with a Shagred; no screen reveals a Shagred's identity on a declined, expired, or withdrawn offer (only the message, dates, and the offer-id report/block survive); no screen shows contact before acceptance, or after a block, or for a deleted counterpart; no screen offers to edit or delete a message; no screen shows a thread or message to anyone but its two participants, and no admin surface appears in a chat; and no screen exposes an offer's or connection's counterpart's account id.
