---
project: OstadLagbo
module: contact-and-offers
type: requirements
status: current
updated: 2026-08-30
id: OL-OFR-REQ-001
derived_from: /OstadLagbo/reference/baseline/mvp-scope-v1.0.md
owner: Iftikher
---

# Contact & Offers — Requirements

Derived from MVP Scope Baseline v1.0 §4. Governs the offer lifecycle, the in-app chat, phone reveal, and their notifications. Shagred-profile visibility follows SGP-05; reporting and blocking are created in `ratings-and-trust`; report handling in `admin-review`; connection analytics in ADM-12.

## OFR-01 Sending an offer

A registered Shagred sends an offer from an Ostad's profile as a **free-text message** (proposed cap 500 characters). Constraints: **one pending offer per Shagred→Ostad pair** at a time, and **a global cap of 5 pending offers** per Shagred across all Ostads — sending a 6th is refused with a clear message until one resolves. Sending grants the Ostad visibility of the Shagred's profile per SGP-05. Ostads cannot initiate contact with Shagreds by any path.

**Acceptance:** the 6th simultaneous pending offer is refused; a second pending offer to the same Ostad is impossible; no Ostad-initiated contact surface exists.

## OFR-02 Offer lifecycle

States: **pending → accepted / declined / expired / withdrawn.**

- **Accepted** — by the Ostad; triggers OFR-04.
- **Declined** — by the Ostad; no reason required. The Shagred **may re-offer immediately** (repeat-pestering is handled by the Ostad's block, not by cooldowns).
- **Expired** — automatically at 7 days pending; counts as unanswered, not declined; re-offer permitted.
- **Withdrawn** — the Shagred may cancel a pending offer at any time; re-offer permitted.

Declined, expired, and withdrawn all lapse profile visibility per SGP-05. Terminal states are immutable — an expired offer cannot be accepted late; connecting requires a fresh offer.

**Acceptance:** state transitions occur exactly as listed and no others; expiry fires without either party opening the app; each state change stamps its timestamp.

## OFR-03 Notifications

Push notifications (baseline §7): Ostad — offer received, and a **pending-expiry reminder** (proposed: day 5 of 7, engineering default); Shagred — offer accepted, offer declined; both — new chat message (suppressed while that chat is open on-screen). Every push has an in-app counterpart (offer inbox states, chat badges) so a denied-notifications user misses nothing permanently.

## OFR-04 Acceptance effects

Acceptance atomically: opens the 1:1 chat; **reveals phone numbers mutually** — each party sees the other's verified number in the chat header/details; makes profile visibility durable per SGP-05; records the **connection** with timestamp (the ADM-12 success unit); notifies the Shagred. The offer text becomes the first message in the thread for context. The reveal is by nature irreversible — a number seen is seen — and the acceptance confirmation states that the Ostad's/Shagred's number will be shared.

**Acceptance:** both numbers visible to both parties immediately after acceptance and never before; the connection event is recorded exactly once per acceptance.

## OFR-05 Chat

One chat thread per connection. Content: **text messages and voice notes** — no images, documents, or video in MVP. Voice notes are capped (proposed 2 minutes) and compressed client-side before upload, consistent with the platform's storage cost posture. Messages persist server-side (moderation evidence, risk R-03) and deliver across devices; offline recipients get push per OFR-03. Message states: sent / delivered / read (proposed as engineering-standard). Chats have no expiry — the thread persists for the life of the relationship.

**Acceptance:** a 2-minute-plus voice note cannot be sent; messages survive reinstall and device switch; no attachment type beyond voice exists in UI or API.

## OFR-06 Ending and freezing

No "end relationship" mechanism exists in MVP; **block is the termination instrument** (created per `ratings-and-trust`): blocking freezes the chat for both sides (read-only history, no new messages), severs profile visibility per SGP-05, and prevents any new offer between the pair in either direction while the block stands. Admin suspension freezes chats per ADM-08. Account deletion by either party closes the thread for the deleted side and shows "deleted account" to the other, who keeps their history.

## OFR-07 Chat privacy and moderation access

Chat is private between its two participants. Admin access to chat content happens **only through reports**: when a report cites messages, admin review sees the cited messages with limited surrounding context (proposed: ±10 messages, engineering default) per ADM-07. No admin surface browses chats at large; every admin viewing of chat context is audit-logged per ADM-17.

**Acceptance:** no dashboard path opens a chat absent a report referencing it; audit entries exist for each report-context view.

## OFR-08 Instrumentation obligations

This module emits the ADM-12/13 events: offers sent / accepted / declined / expired / withdrawn with response times, connections, messages and voice notes sent, phone reveals, and per-pair connection uniqueness. These events exist from first release.

## Proposed technical defaults summary

Offer text cap, expiry-reminder day, voice-note duration cap and codec, message-state mechanics, and report-context window are engineering defaults, changeable without founder re-approval. The offer caps (1 per pair, 5 global), the lifecycle states, 7-day expiry, immediate re-offer policy, mutual reveal timing, text+voice-only chat, block-as-termination, and report-only admin access change only with founder approval.
