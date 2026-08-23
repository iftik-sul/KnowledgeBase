---
project: 3i
module: learning-delivery
type: data-model
status: current
updated: 2026-08-23
id: 3I-LDL-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - learning-delivery
---

# Learning Delivery — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## Batch

| Field | Notes |
| :---- | :---- |
| Course | FK to `catalogue` Course. Only meaningful for `Online Class` or `Mixed` course types — a `Regular` course never has a Batch |
| Instructor | FK to `instructors`' `InstructorProfile` — real reference, resolved 2026-08-23. Mirrors `Course.instructorId` |
| Name | |
| Capacity | Maximum enrolled learners (FR-BAT-01) |
| Number of classes | Session count, set at creation |
| Approximate duration per class | |

**Sessions are a separate entity**, not a field on Batch, because each carries its own date/time and its own attendance records — see **Session** below.

### The WWCC Scheduling Guard

[3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md): **no Session may be created with a date past the owning instructor's WWCC expiry date.** Enforced at batch creation, since every session's date is known up front (FR-BAT-01) — this is a validation on the whole set of sessions being created, not a check that could pass at creation and later fail. Reads `instructors`' `InstructorProfile.wwccExpiryDate` — a real, queryable field, not a forward reference.

---

## Session

| Field | Notes |
| :---- | :---- |
| Batch | FK |
| Scheduled at | Date and time (FR-BAT-01) |
| Status | `scheduled`, `delivered`, `cancelled` — see below |
| Meeting link | Posted by the instructor ahead of the session (FR-BAT-02) |

**"Delivered" is what [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md)'s attendance denominator counts against**, not "scheduled." A session moves to `delivered` once its scheduled time has passed and it wasn't cancelled — not a manual instructor action, since requiring the instructor to remember to mark a routine session as "delivered" is a step that will be forgotten, and the fact of a session having happened is knowable from the clock alone. **Rescheduling** (FR-BAT-04) updates `scheduledAt` on the existing Session record rather than creating a new one, so its identity — and any attendance already recorded against it — is preserved.

**Meeting link distribution** (FR-BAT-02: posted to the batch's chat room, and by email) is a `communication`-module action triggered by this record, not something this module implements itself — `learning-delivery` owns the Session and its scheduled time; `communication` owns actually sending the link out.

---

## AttendanceRecord

| Field | Notes |
| :---- | :---- |
| Session | FK |
| Learner | FK |
| Status | `present`, `absent`, `late`, or `excused` (FR-BAT-03) |
| Marked at | |
| Marked by | The instructor — attendance is always instructor-marked, never self-reported |

**One row per (Session, Learner).** Marking attendance for one session never touches another session's records — each Session's roster and attendance are independent, even within the same Batch.

---

## Enrolment

| Field | Notes |
| :---- | :---- |
| Learner | FK |
| Course | FK to `catalogue` Course — real reference |
| Batch | FK, **nullable**. Set only for `Online Class`/`Mixed` courses; null for `Regular` |
| Enrolled by | FK to `identity-and-access` Account — the guardian or the learner themselves, per enrolment authority (FR-ENR-02) |
| Status | `active`, `waitlisted`, `offered`, `cancelled`, `expired` — see below |
| Age override | Boolean, plus approving Account and timestamp when true (FR-ENR-04) |
| Waitlist position | Nullable, set only while `status = waitlisted` |
| Offer expires at | Nullable, set only while `status = offered` — 48-hour window (FR-ENR-07) |
| Enrolled at | |

**Re-joining a later batch of the same course is a new Enrolment row**, not an update to an old one (FR-BAT-06) — a learner's history of separate attempts at the same course, each against its own batch, is preserved rather than overwritten.

**Does not consume a seat on its own.** FR-ENR-01's "available seat for that learner" check reads the Learner's own activation state in `identity-and-access`/`commerce` — real reference, already built — confirming the *profile* is active. Enrolling in a second, third, or tenth course does not require a second, third, or tenth seat. See [README.md](README.md#one-seat-many-courses).

### Status Lifecycle

| From | Event | To | Notes |
| :---- | :---- | :---- | :---- |
| — | Enrol, capacity available | `active` | Immediate |
| — | Enrol, batch at capacity | `waitlisted` | Position assigned (FR-ENR-06) |
| `waitlisted` | A seat frees up (cancellation elsewhere in the batch) | `offered` | First-in-line only; `offerExpiresAt` set to +48h (FR-ENR-07) |
| `offered` | Learner accepts within 48h | `active` | |
| `offered` | 48h elapses, no action | `expired` | Offer passes to next waitlisted learner. See [README.md](README.md#open-against-this-module) on the open question of what happens to this Enrolment afterward |
| `active` | Learner or guardian cancels | `cancelled` | |

### Age Gating

**FR-ENR-03**: refused if `Learner.age < Course.minimumAge` — both real references now (`identity-and-access`, `catalogue`).

**FR-ENR-04, the override**: a guardian may push the enrolment through **up to 2 years** past the learner's actual age relative to `Course.minimumAge`, with explicit confirmation. Sets `ageOverride = true` plus the approving Account and a timestamp — a permanent audit fact on the Enrolment row, never cleared.

**FR-ENR-05**: the override has a hard ceiling — **no override reaches a course tagged `18+`**, regardless of how close the learner's age is. This is checked independently of the 2-year math, not as a special case of it, since "2 years past 16 reaches 18" would otherwise accidentally satisfy both rules and let an override into 18+ content.

**Known consequence, confirmed intended**: an overridden under-13 learner enrolled into a 13+-tagged course has no chat access at all — see [age-and-safeguarding.md §5](/3i/age-and-safeguarding.md#5-the-enrolment-override) for the full explanation. This module doesn't work around that; it's `communication`'s room-mode logic reading the course's own age tag, unaffected by any individual Enrolment's override flag.

---

## Course-Level Progress — Computed, Not Stored

"This learner is 60% through this course" is **not a stored field anywhere** — it's computed by aggregating `materials`' `MaterialProgress` records and `assessment`'s exam-attempt completion across every Material and exam belonging to the Enrolment's Course. Same principle as `catalogue`'s derived age band and `materials`' derived completion flags: a value with multiple contributing sources is computed at read time, never duplicated into a field that could drift out of sync with what actually happened.

---

## Forward References — Resolved (2026-08-23)

This module was originally scaffolded before `instructors`, `assessment`, and `communication` existed. All three are now real:

| Reference | Resolved by |
| :---- | :---- |
| `Batch.instructorId`, WWCC expiry for the scheduling guard | `instructors`' `InstructorProfile` |
| Course-level progress's exam-completion component | `assessment`'s `ExamAttempt` |
| Meeting-link distribution (FR-BAT-02) | `communication` |

---

## Referenced By

| Module | Reads |
| :---- | :---- |
| `catalogue` | Batch — publish gate, "has upcoming batch" filter, "most enrolled" sort. Enrolment — Review submission's enrolment check |
| `materials` | Enrolment — video/offline access gate |
| `assessment` | Enrolment — exams are scoped to an enrolled learner on a course |
| `certification` | AttendanceRecord, Session — attendance-certificate eligibility (FR-CERT-02, sessions-delivered denominator per [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md)) |
| `communication` | Session — meeting-link distribution; Batch — chat room scoping (one room per batch for Online Class/Mixed courses, per §15.1) |
| `reporting` | Enrolment, AttendanceRecord — enrolment and attendance reports (FR-REP-01) |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Course | `catalogue` | Owner of Batch; `minimumAge`/`maximumAge` for the age gate |
| Learner | `identity-and-access` | Age for the gate; subject of Enrolment and AttendanceRecord |
| Account | `identity-and-access` | Enrolment authority (who enrolled, who approved an override) |
| Subscription | `commerce` | FR-ENR-01's seat-availability check |
| InstructorProfile | `instructors` | `Batch.instructorId`, WWCC scheduling guard |
| ExamAttempt | `assessment` | Course-level progress's exam-completion component |