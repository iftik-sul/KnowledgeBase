---
project: 3i
module: learning-delivery
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-LDL-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Learning Delivery — Validation Rules

Field-level and flow-level validation shared across two or more learning-delivery screens.

---

## Age Gate and Override

On [Enrol \& Waitlist](screens/enrol-and-waitlist.md): enrolment is refused outright when `Learner.age < Course.minimumAge` (FR-ENR-03), **unless** the gap is 2 years or less and a guardian explicitly confirms an override (FR-ENR-04) — the confirmation is a distinct, deliberate step, not a checkbox bundled into the ordinary enrolment action, since this is a safeguarding-adjacent decision the guardian should not be able to trigger by accident.

**The override option itself is absent, not disabled, once the gap exceeds 2 years or the course is tagged 18+** (FR-ENR-05) — same absent-not-disabled convention used throughout `identity-and-access` and `catalogue`. A guardian should never see an override button that would fail if pressed.

## Waitlist Promotion Window

On [Enrol \& Waitlist](screens/enrol-and-waitlist.md): an `offered`-status Enrolment shows a live countdown against its 48-hour `offerExpiresAt` (FR-ENR-07). Accepting past expiry is refused — the offer has already passed to the next learner in line by then, and the UI should reflect that rather than accepting a stale action.

## WWCC Scheduling Guard

On [Batch Schedule / Manage](screens/batch-schedule-manage.md): no session date may fall past the instructor's WWCC expiry ([3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md)), checked live against `instructors`' `InstructorProfile.wwccExpiryDate`. A single offending session refuses the whole batch, not just that session.