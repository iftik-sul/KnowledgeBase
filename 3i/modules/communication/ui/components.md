---
project: 3i
module: communication
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CMN-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Communication — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## Message Bubble

Used on: [Chat Room](screens/chat-room.md), [Admin Moderation Queue](screens/admin-moderation-queue.md) (read-only context view).

Author display name (self, or the [Guardian Attribution Tag](#guardian-attribution-tag) when on-behalf-of), content, timestamp. A **tombstoned** message renders as a visible gap marker ("This message was removed") rather than disappearing from the flow — per [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md), a gap is more honest than silently reflowing the conversation. A **filtered** message is never rendered to other participants at all; only the sender sees their own withheld state, inline, at time of send.

## Guardian Attribution Tag

Used on: [Message Bubble](#message-bubble).

Renders *"[Guardian name] (guardian of [Learner name])"* — the exact format [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md) specifies, reused verbatim by [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md) for reviews. Never abbreviated or truncated to just the guardian's name — the whole point is that a reader can always tell a child is not the one speaking.

## Notification Row

Used on: [Notification Centre](screens/notification-centre.md).

Category icon, title, body (with any named learner profile bolded — FR-NOT-04), timestamp, read/unread visual state. Selecting an unread row marks it read; the centre never auto-marks-read on open of the whole list, since a guardian scanning several at once shouldn't lose track of which they'd actually looked at individually.