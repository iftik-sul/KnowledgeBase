---
project: OstadLagbo
module: support
type: ui
status: current
updated: 2026-09-26
id: OL-SUP-UI-001
derived_from: /OstadLagbo/modules/support/requirements/support-requirements.md
owner: Iftikher
---

# Support — UI

Screens for the Help & Support entry, creating a ticket, the ticket list and thread, and the suspension appeal. Conventions per [UI Overview](/OstadLagbo/ui-overview.md); behaviour and endpoints per [SUP API](/OstadLagbo/modules/support/api/support-api.md); ticket *handling* is the admin dashboard (ADM ui); abuse reporting is the separate RNT report flow, never a ticket.

Two things anchor these screens: a **ticket is a private thread with support, not a chat** (no delivery/read ticks, no voice notes — SUP-05), and the **appeal ticket is the one thing a suspended account can create** — this module is the working door behind the ToS §7 appeal promise.

## Group A — Help & Support entry (SUP-01)

### Help & Support screen
- **Purpose:** the user's door to help, their tickets, and the legal documents.
- **Shell:** Shagred and Ostad shells (including a **pending** Ostad) → Profile/Settings → **Help & Support**. **Guests do not see it** — the store listing and the public contact email are their channel.
- **Structure:** **Create a ticket**, **My tickets** (history and open threads), and links to **Terms** and **Privacy** (`GET /v1/legal/*`).
- **States:** **loading** → the entry list renders immediately; only the unread indicator on **My tickets** waits on data. **Empty** → not applicable; this screen is navigation. **Error** → if the ticket count cannot be read the entries still work, unbadged — help must never be unreachable because a badge query failed, least of all for a suspended user whose only route out is an appeal.
- **Never shows:** to a guest at all.

## Group B — Creating a ticket (SUP-02)

### Create a ticket
- **Purpose:** open a support request in one of five categories.
- **Structure:** a **category** picker — *Account & login / Verification & review / Technical problem / Appeal a decision / Other*; a free-text **description** (≤1,000 chars, counter); and **one optional image** (a screenshot, via the upload-ticket flow — OSP image rules) shown only to support and admin. A quiet line steers abuse elsewhere: **to report a user, a message, or a review, use the Report action on that profile, chat, or review (RNT ui) — a ticket is for help, not moderation** (SUP-05).
- **States:** submit confirms in-app and drops the user on the new ticket in "My tickets"; a **sixth open ticket** is refused with "resolve one first" (`conflict: open_ticket_limit`) — **appeals are exempt** from this cap.
- **The "Appeal a decision" category here** is for an active user contesting a **warning** (optionally referencing that action) or a **content removal** (described in text — removals aren't linkable). A **suspension** appeal is a different door — the Group D path from the suspension notice, where the contested action is required and a suspended user can reach nothing else.
- **Data & actions:** `POST /v1/support/tickets {category, description, attachment_upload_id?, related_moderation_action_id?}`.
- **Never shows:** the attachment to any other user — it is owner-and-admin only.

## Group C — My tickets and the thread (SUP-03)

### My tickets
- **Shell:** Help & Support → **My tickets**.
- **Structure:** the user's tickets, most-recent activity first, each with its **category**, **state** (open / resolved), and an **unread-reply indicator** (any admin or system message the user hasn't opened).
- **States:** **loading** → skeleton rows. **Empty** → *"No tickets yet"* with the **Create a ticket** action — and for a **suspended or terminated** user reaching this from the suspension shell, the **Appeal this decision** action instead, since an appeal is the only write they have (SUP-04, rule 7). **Error** → retry, keeping loaded pages; for a suspended user a failure here must still leave the appeal route reachable from the notice screen, because this list is not their only door to it.
- **Data:** `GET /v1/support/tickets`. Unread badges derive from the data, so a notifications-denied user misses nothing (SUP-03, OFR-03 principle).

### Ticket thread
- **Purpose:** the private back-and-forth with support.
- **Structure:** the thread — the **description rendered as the first message**, then messages tagged **you / support / system**, each with time; the **attachment** (if any) as an owner-only signed image; and a **reply** composer (**text only** — no voice, no read/delivery ticks; this is not chat, SUP-05). System notes appear for auto-close events.
- **States:** **open** → reply freely; **resolved** → a reply **within 14 days reopens** the ticket (the composer stays available with a note that replying will reopen); **past 14 days** → the composer is replaced by a prompt to **start a new ticket** (`state_conflict: reopen_window_closed`). Opening the thread clears the unread indicator.
- **No edit or delete:** support threads are operational records — there is no message edit or delete, and the user cannot resolve a ticket themselves (only an admin resolves, with a closing reply; SUP-DM).
- **Data & actions:** `GET /v1/support/tickets/{id}` (thread + attachment), `POST /v1/support/tickets/{id}/messages {body}` (reply / reopen), `POST /v1/support/tickets/{id}/read` (clear unread). Admin replies arrive by push (ticket-reply category).
- **Never shows:** the thread or attachment to anyone but its owner and admin; no delivery/read state (it is not chat).

## Group D — Appeal from suspension (SUP-04)

### Appeal (from the suspension shell)
- **Purpose:** the one write a suspended account can make — contest the decision.
- **Shell:** the **suspension-notice shell** (REG ui) — the only screen a suspended or terminated user reaches — via **"Appeal this decision"**.
- **Structure:** an appeal composer — the description (why the decision should be reconsidered) and the optional screenshot — pre-set to the **Appeal** category and bound to the contested action; submit.
- **States:** creating the appeal grants **no other app access**; the suspended user can then **read and reply to their own tickets** (the appeal and any earlier ones) and do nothing else. The appeal is **exempt from the open-ticket cap**, and only **one open appeal per contested decision** is allowed (a second is refused).
- **Data & actions:** `POST /v1/support/tickets {category: "appeal", related_moderation_action_id, description, attachment_upload_id?}` → reaches the admin queue flagged as an appeal (ADM-22); then the same thread screen (Group C) to follow it.
- **Fallback:** a banned/deleted user who cannot log in has the **public contact email** as their channel (stated on the store listing and legal pages), not this screen.
- **Never shows:** anything else in the app while suspended — only the notice, the appeal, the user's own tickets, language, and logout.

## Notifications (SUP-06 counterparts, OFR-03 principle)

An **admin reply** pushes to the ticket owner (with its in-app unread indicator); a ticket resolved by an admin carries the closing reply. No per-category preferences (OS-level only). Ticket-created / resolution-time / reopen metrics are emitted server-side (ADM-15) and are not a user-facing surface.

## Flows

**Ask for help.** Settings → Help & Support → Create a ticket → pick *Technical problem*, describe it, attach a screenshot → submit → it appears in My tickets as open → an admin replies (push) → open the thread (unread clears) → reply → the admin resolves with a closing note → 10 days later a follow-up reply reopens it; a month later, the thread offers a new ticket instead.

**Appeal a suspension.** Suspended login → the suspension shell → **Appeal this decision** → describe why → submit → the appeal reaches the admin queue flagged as an appeal → follow it in-thread; nothing else in the app opens until the account is reinstated.

## What this module's screens never show

No ticket, thread, or attachment is visible to anyone but its owner and admin; a guest never sees Help & Support at all; a ticket is never real-time chat (no voice, no delivery/read state); no user edits, deletes, or resolves a ticket; a suspended account reaches nothing here beyond creating an appeal and reading/replying to its own tickets; and tickets never stand in for the abuse-report flow — the app points that need to RNT's report action.
