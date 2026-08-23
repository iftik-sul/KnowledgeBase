---
project: 3i
module: learning-delivery
type: requirements
status: current
updated: 2026-08-23
id: 3I-LDL-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - batches
---

# Batches and Live Sessions

Baseline §10. Seven requirements. **Live classes are held outside the platform** — this module schedules them, distributes links, and records attendance; it does not host video.

---

## Creation

| ID | Requirement |
| :---- | :---- |
| **FR-BAT-01** | Batch creation captures name, capacity, number of classes, approximate duration per class, and the date and time of each session |

Every session's date is fixed at creation, which is what makes the WWCC scheduling guard ([3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md)) a validation at creation time rather than an ongoing check — see [data-model.md](../data-model.md#the-wwcc-scheduling-guard).

---

## Meeting Links

| ID | Requirement |
| :---- | :---- |
| **FR-BAT-02** | The instructor posts the meeting link to the batch group chat and, from the platform, by email, ahead of each session |

Both channels, not either — the chat post and the email are both required, since [age-and-safeguarding.md §5](/3i/age-and-safeguarding.md#5-the-enrolment-override)'s known-consequence case (an overridden under-13 learner with no chat access at all) depends on the email channel as the only route that reaches them.

---

## Attendance

| ID | Requirement |
| :---- | :---- |
| **FR-BAT-03** | The instructor marks attendance manually after each session (present / absent / late / excused) |
| **FR-BAT-07** | The instructor sees a batch roster of learner profile names for attendance |

Manual and instructor-only, no self-reporting path. The roster (FR-BAT-07) shows every learner with an `active`-status Enrolment on the batch at the time of the session — a learner who joined mid-batch appears on the roster only from their join date forward, not retroactively on sessions that predate their enrolment.

---

## Changes to a Scheduled Batch

| ID | Requirement |
| :---- | :---- |
| **FR-BAT-04** | Rescheduling a session notifies all enrolled learners automatically by push and email |
| **FR-BAT-05** | Cancelling a batch notifies enrolled learners, who may join a future batch. No refund is triggered, as access is subscription-based |

FR-BAT-05's no-refund logic follows directly from [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md): the learner paid for an active seat, not for this specific batch's sessions, so losing one batch doesn't touch what they paid for — they remain entitled to join whatever batch runs next.

---

## Repeat and Multiple Enrolment

| ID | Requirement |
| :---- | :---- |
| **FR-BAT-06** | A learner may enrol in multiple batches of the same course, including re-joining a later batch |

Each such enrolment is its own [Enrolment](../data-model.md#enrolment) record — a learner's full history of attempts at a course, across however many batches, is preserved rather than overwritten by the most recent one.

---

## Acceptance Criteria

1. A batch cannot be created without at least one scheduled session.
2. A batch creation attempt with any session dated past the instructor's WWCC expiry is refused, naming the expiry date.
3. Rescheduling produces both a push and an email to every enrolled account.
4. Attendance saved for one session does not affect other sessions.
5. Cancelling a batch triggers no refund and no access change — the affected learners' seats remain active.
6. A learner who completed a cancelled batch's course partway can re-enrol in a newly created batch of the same course without any additional payment.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-LDL-DM-001](../data-model.md) |
| Sessions-delivered attendance denominator, WWCC scheduling guard | [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md) |
| Course dismissal on instructor loss | [3I-DEC-013](/3i/decisions/dec-013-instructor-removal-dismisses-course.md) |
| Enrolment, waitlist, age gating | [3I-LDL-REQ-002](enr-enrolment-waitlist-and-age-gating.md) |