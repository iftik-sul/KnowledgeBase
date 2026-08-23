---
project: 3i
module: learning-delivery
type: requirements
status: current
updated: 2026-08-23
id: 3I-LDL-REQ-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - enrolment
---

# Enrolment, Waitlist and Age Gating

Baseline §11. Seven requirements, one amended by decision — [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) (seat as a per-profile grant, clarifying what FR-ENR-01's "available seat" check actually means).

---

## The Seat Check

| ID | Requirement |
| :---- | :---- |
| **FR-ENR-01** | Enrolment requires an active subscription with an available seat for that learner |

**"Available seat for that learner" means the learner's own profile is active** ([3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md)) — not that this specific course-enrolment event needs a seat allocated to it. See [README.md](../README.md#one-seat-many-courses) for why this distinction matters and is easy to get wrong when implementing.

---

## Enrolment Authority

| ID | Requirement |
| :---- | :---- |
| **FR-ENR-02** | Enrolment authority: guardian enrols under-13 profiles; 13–17 profiles default to guardian approval, with a guardian toggle to allow self-enrolment; standalone accounts self-enrol |

**"Standalone accounts" no longer exist** ([3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md)) — every account holder is 18+ by construction, so the third branch of this requirement (standalone self-enrolment) now only ever applies to the account holder enrolling *themselves* as a learner, not to any minor. The under-13 and 13–17 branches are unaffected, since those were always about profiles, not standalone accounts.

---

## Age Gating

| ID | Requirement |
| :---- | :---- |
| **FR-ENR-03** | A learner cannot enrol in a course whose minimum age exceeds their age |
| **FR-ENR-04** | A guardian may override the age gate **upward by up to 2 years**, with explicit confirmation. Overrides are logged with the approving account and timestamp |
| **FR-ENR-05** | **No override is possible into a course tagged 18+** |

Full detail, including the override's known chat-access consequence, is in [age-and-safeguarding.md §5](/3i/age-and-safeguarding.md#5-the-enrolment-override) — not restated here. This document covers the enrolment-flow mechanics; that one covers the safeguarding reasoning.

---

## Waitlist

| ID | Requirement |
| :---- | :---- |
| **FR-ENR-06** | When a batch is at capacity, learners join a **waitlist** with a visible position |
| **FR-ENR-07** | On a cancellation, the first waitlisted learner is notified and auto-promoted. The offer expires after 48 hours and passes to the next in line |

**Waitlisting only applies to batch-based enrolment** (`Online Class`/`Mixed` courses) — a `Regular` self-paced course has no capacity concept and therefore no waitlist; FR-ENR-06's "batch at capacity" precondition doesn't arise for it.

**The 48-hour offer window is per learner, not per seat** — if the first-in-line learner's offer expires, the freed seat is offered fresh to the next learner with their own full 48 hours, not a shortened remainder of the first learner's window.

---

## Acceptance Criteria

1. An 11-year-old can be enrolled into a 13+ course with guardian confirmation; the same learner cannot be enrolled into an 18+ course by any route, including the override.
2. A waitlisted learner is promoted and notified within one minute of a cancellation freeing a seat.
3. Enrolment fails cleanly when no seat is available (the learner's profile isn't active), with an upgrade path shown — not a generic error.
4. A learner with an active seat can enrol in a second, unrelated course without any additional payment or seat check beyond confirming the profile is still active.
5. An enrolment override is permanently recorded with the approving guardian account and timestamp, and remains on the Enrolment record even after the course is completed or the batch ends.
6. A promoted waitlist offer that isn't accepted within 48 hours passes automatically to the next-in-line learner, with a fresh 48-hour window for them.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-LDL-DM-001](../data-model.md) |
| Seat as per-profile grant | [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) |
| No standalone accounts | [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) |
| Age-gating reasoning and known consequences | [age-and-safeguarding.md §5](/3i/age-and-safeguarding.md#5-the-enrolment-override) |
| Batches and live sessions | [3I-LDL-REQ-001](bat-batches-and-live-sessions.md) |