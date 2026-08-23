---
project: 3i
module: communication
type: requirements
status: current
updated: 2026-08-23
id: 3I-CMN-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - chat
---

# Group Chat and Moderation

Baseline §15. Fifteen requirements. [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md) and [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md) apply directly; neither changes what any FR-CHAT requirement itself says, both specify how it's implemented.

---

## Structure

| ID | Requirement |
| :---- | :---- |
| **FR-CHAT-01** | Real-time delivery over WebSocket. Messages persist to PostgreSQL |
| **FR-CHAT-02** | **Text only.** No image, file, or media sharing |
| **FR-CHAT-03** | **Group only.** No direct or 1:1 messaging anywhere in the platform |
| **FR-CHAT-04** | Flat structure — no announcement-only mode |

FR-CHAT-02 and FR-CHAT-03 are child-safety design decisions (§23 items 10–11), not deferred features — [age-and-safeguarding.md §6](/3i/age-and-safeguarding.md#6-chat) is explicit that they are not candidates for later addition without a safeguarding review. FR-CHAT-03's acceptance criterion is structural: no API route exists that creates a two-participant private room, not a UI convention that happens not to expose one.

---

## History

| ID | Requirement |
| :---- | :---- |
| **FR-CHAT-05** | Message history is retained indefinitely and is searchable |

Subject to the tombstoning behaviour on profile deletion ([3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md)) — "retained indefinitely" describes the message record, not necessarily its content forever.

---

## Age-Derived Access

| ID | Requirement |
| :---- | :---- |
| **FR-CHAT-06** | **Under-13 learners have no chat access.** The guardian participates on the child's behalf, displayed as *"Fatima (guardian of Aisha)"* |
| **FR-CHAT-07** | Where a course's minimum age is under 13, the room is automatically set to guardian-only mode. This is derived from the age tag, not configured by the instructor |
| **FR-CHAT-08** | 13–17 learners participate directly, subject to the guardian toggle |

Full safeguarding reasoning in [age-and-safeguarding.md §6](/3i/age-and-safeguarding.md#6-chat) and [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md) — not restated here. The requirement-level summary: guardian-only mode is computed from `Course.minimumAge` every time it's checked ([data-model.md](../data-model.md#chatroom)), never cached as a static flag on the room.

---

## Moderation

| ID | Requirement |
| :---- | :---- |
| **FR-CHAT-09** | Instructor and admin may delete messages, mute participants, and remove participants. All moderation actions are logged |
| **FR-CHAT-10** | Any participant may report a message. Reports enter an admin moderation queue with a **24-hour response target**, tracked and reportable |
| **FR-CHAT-11** | A server-side **profanity and content filter** runs on send, across all five languages, including link scanning. Filtered messages are withheld and flagged |
| **FR-CHAT-12** | Chat logs are auditable by admin **across all rooms**, not only by the owning instructor |

§22.3 risk 2 names multilingual profanity filtering as expected to produce false positives on religious vocabulary — tuning time is budgeted and an admin override on filtered messages exists (FR-CHAT-11's own "flagged" state is what an admin overrides). FR-CHAT-10's exempt string set (the report flow's own copy) is listed in [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md).

---

## Room Lifecycle

| ID | Requirement |
| :---- | :---- |
| **FR-CHAT-13** | Instructor or admin may close a room. Closed rooms become **read-only archives, never hidden** |

A closed room's messages remain fully readable by anyone who could read them before closure — closing changes who can *write*, not who can *see*.

---

## Deletion and Safety

| ID | Requirement |
| :---- | :---- |
| **FR-CHAT-14** | On account deletion, message authorship is anonymised to "Deleted user". Messages are retained |
| **FR-CHAT-15** | A **safety contact** is published in-app and on the website |

FR-CHAT-14 is the account-deletion rule; it is not the same as profile-deletion tombstoning — see [README.md](../README.md#two-deletion-rules-that-look-similar-and-arent) for the distinction stated precisely, since the two are easy to conflate. FR-CHAT-15's safety-contact copy is in the exempt safeguarding-string set ([3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md)).

---

## Acceptance Criteria

1. No API route exists that creates a two-participant private room.
2. A course tagged minimum age 8 produces a guardian-only room without instructor action.
3. A reported message appears in the admin queue with an SLA countdown.
4. An overdue-reports figure is visible on the admin dashboard.
5. Deleting a profile tombstones that profile's messages (content gone, "Deleted learner", moderation record intact); deleting an account anonymises authorship only, content intact — the two produce visibly different results in the same room.
6. A rejoined batch's room is empty of the earlier batch's messages — they remain in the original batch's own (possibly closed) room.
7. A closed room's messages remain fully visible to prior participants; no new message can be posted to it by anyone.