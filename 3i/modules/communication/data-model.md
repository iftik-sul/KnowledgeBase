---
project: 3i
module: communication
type: data-model
status: current
updated: 2026-08-23
id: 3I-CMN-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - communication
---

# Communication — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## ChatRoom

| Field | Notes |
| :---- | :---- |
| Course | FK to `catalogue` Course — set for `Regular`-type courses |
| Batch | FK to `learning-delivery` Batch, nullable — set for `Online Class`/`Mixed` courses instead of (not in addition to) a direct course link. Exactly one of Course or Batch is ever set on a given room |
| Guardian-only | **Derived, not stored** — true whenever the owning course's `minimumAge` \< 13 (FR-CHAT-07). Recomputed from the course's current age tag, never cached, since a stale cached value here would be a safeguarding failure, not just a display bug |
| Status | `open` or `closed`. A closed room is a **read-only archive**, never hidden (FR-CHAT-13) |

**One room per course (Regular) or per batch (Online Class/Mixed)** — §15.1. A learner re-joining a later batch of the same course (FR-BAT-06) enters that batch's own room, never the earlier batch's — rooms are scoped to the specific batch instance, not the course-level teaching relationship.

---

## ChatMessage

| Field | Notes |
| :---- | :---- |
| Room | FK |
| Author account | FK to `identity-and-access` Account. Nullable after account deletion (FR-CHAT-14) |
| Author learner | FK to `identity-and-access` Learner, nullable — set when the message is attributed to a specific profile (either the learner speaking for themselves, 13–17, or a guardian speaking on an under-13 profile's behalf) |
| On behalf of | Boolean — true when Author account ≠ the account that would normally hold Author learner, i.e. a guardian is speaking for a child. Drives the *"Fatima (guardian of Aisha)"* display format (FR-CHAT-06, [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md)) |
| Content | Tombstoned (replaced with a marker, not deleted as a row) on profile deletion ([3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md)). Retained on account deletion (FR-CHAT-14) — see [README.md](README.md#two-deletion-rules-that-look-similar-and-arent) for why these differ |
| Filtered | Boolean — true if the profanity/link filter withheld this message on send (FR-CHAT-11). A filtered message's content is never delivered to the room; only the sender sees it was withheld |
| Sent at | |

**Text only** (FR-CHAT-02) — no attachment or media field exists on this entity, structurally, not as an unenforced convention.

---

## ChatMessageReport

| Field | Notes |
| :---- | :---- |
| Message | FK |
| Reported by | FK to Account |
| Reason | Free text |
| Status | `open` or `resolved` |
| Responded at | Nullable — the field the 24-hour SLA (FR-CHAT-10) measures against |
| Resolved by | FK to Admin Account, nullable |
| Action taken | Free text summary, nullable until resolved |

**Survives message tombstoning and profile deletion** ([3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md)) — a report and its resolution remain fully intact even after the message it was raised against has its content removed.

---

## ModerationAction

| Field | Notes |
| :---- | :---- |
| Room | FK |
| Type | `delete_message`, `mute_participant`, `remove_participant`, or `close_room` (FR-CHAT-09) |
| Target | Message or Account reference, depending on type |
| Performed by | FK to Instructor or Admin Account — both may moderate (FR-CHAT-09, FR-CHAT-12) |
| Performed at | |
| Reason | Free text |

**Every moderation action is logged, full stop** — FR-CHAT-09 makes no exception for routine actions versus consequential ones. This is also what [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md) means by "the moderation record" surviving profile deletion.

---

## NotificationPreference

| Field | Notes |
| :---- | :---- |
| Account | FK |
| Category | `learning_updates`, `billing`, `chat_moderation`, or `instructor` — see [README.md](README.md#notification-categories--confirmed-grouping) for the grouping and why account verification isn't one of these four |
| Push enabled | Boolean, default true |
| Email enabled | Boolean, default true |

**One row per (Account, Category)**, not per individual trigger — FR-NOT-03's opt-out is category-level, and §16.2's fifteen triggers fold into four categories plus one always-on mechanic (account verification), never fifteen individual toggles.

---

## Notification

| Field | Notes |
| :---- | :---- |
| Account | FK — always the account holder (FR-NOT-04), never a learner profile directly |
| Category | Same four values as NotificationPreference, for filtering against it at send time |
| Trigger type | Which of §16.2's events produced this notification |
| Related learner | FK, nullable — set when the notification concerns a specific profile, so the body can name them ("Aisha has completed Level 2 Tajweed", FR-NOT-04) |
| Title, body | Locale-rendered per the account's own locale preference (FR-NOT-05) |
| Read at | Nullable — drives the in-app centre's read/unread state (FR-NOT-02) |
| Sent push, sent email | Booleans — whether each channel was actually attempted for this notification, independent of whether it was *delivered* (see NotificationDeliveryLog) |
| Created at | |

**Checked against NotificationPreference at send time**, not at read time — a category opted out of after a notification was already sent doesn't retroactively hide it from the in-app centre; it only stops future ones in that category.

---

## NotificationDeliveryLog

| Field | Notes |
| :---- | :---- |
| Notification | FK |
| Channel | `push` or `email` |
| Status | `sent`, `bounced`, or `complained` (FR-NOT-08) |
| Timestamp | |

**This is what FR-NOT-08 actually requires** — "delivery, bounce, and complaint events are logged" is a statement about this table, not about the Notification record itself, which only tracks whether sending was *attempted*.

---

## Forward References

None. Every entity this module reads from — Account, Learner, Course, Batch — is already built.

---

## Referenced By

| Module | Reads |
| :---- | :---- |
| `learning-delivery` | ChatRoom — FR-BAT-02's meeting-link distribution posts into the batch's room |
| `reporting` | ChatMessageReport, ModerationAction, Notification, NotificationDeliveryLog — moderation and email-delivery reports (FR-REP-01) |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Account | `identity-and-access` | Every message author, report submitter, moderator, and notification recipient |
| Learner | `identity-and-access` | Message on-behalf-of attribution; notification's "related learner" naming |
| Course | `catalogue` | ChatRoom's age-tag source for the guardian-only derivation; minimum age also drives whether a room exists as guardian-only from creation |
| Batch | `learning-delivery` | ChatRoom scoping for Online Class/Mixed courses |