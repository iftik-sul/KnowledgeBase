---
project: 3i
module: instructors
type: requirements
status: current
updated: 2026-08-23
id: 3I-INS-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - instructors
---

# Instructor Onboarding

Baseline §7. Seven requirements, none amended by decision — [3I-DEC-013](/3i/decisions/dec-013-instructor-removal-dismisses-course.md) and [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md) specify consequences of losing an instructor without changing what any FR-INST requirement itself says.

---

## Application

| ID | Requirement |
| :---- | :---- |
| **FR-INST-01** | Instructor applications capture bio, area of expertise, and CV upload |
| **FR-INST-02** | Applications require **admin approval**. Approved instructors gain the instructor role; rejected applicants are notified with a reason and **may re-apply** |

Re-application produces a new [InstructorApplication](../data-model.md#instructorapplication) row — the full history of an Account's attempts stays visible, never overwritten. Approval is a role-assignment consequence ([3I-DEC-007](/3i/decisions/dec-007-rbac-without-hardcoded-roles.md)'s data-not-code principle), not a special code path.

---

## WWCC

| ID | Requirement |
| :---- | :---- |
| **FR-INST-03** | The instructor record captures **WWCC number, issuing state, and expiry date**, with an admin alert **60 days before expiry** |
| **FR-INST-04** | An instructor whose WWCC has expired **cannot be assigned to, or continue teaching**, any course tagged under 18 |

Full mechanism — including the two distinct enforcement moments (creation-time check, and automatic suspension the instant expiry passes) — in [data-model.md](../data-model.md#fr-inst-04-enforcement--what-cannot-continue-teaching-actually-does). Not restated here. See also [age-and-safeguarding.md §7](/3i/age-and-safeguarding.md#7-instructors) for the safeguarding reasoning, and [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md) for how the 60-day alert becomes an actionable scheduling guard rather than a passive notice.

---

## Storage

| ID | Requirement |
| :---- | :---- |
| **FR-INST-05** | Each instructor has a **50 GB storage quota**, adjustable by admin |

The quota field lives on `InstructorProfile` (this module); **enforcing it at upload time is `materials`' responsibility** — see [README.md](../README.md#open-against-this-module) for the cross-module note. This module owns the number, not the enforcement point.

---

## Course Ownership

| ID | Requirement |
| :---- | :---- |
| **FR-INST-06** | **One instructor per course.** Course ownership belongs to the assigned instructor |

Already the shape `catalogue`'s `Course.instructorId` assumed as a single scalar FK, not a list — this requirement is satisfied by that field's cardinality, nothing further to add here.

---

## Suspension

| ID | Requirement |
| :---- | :---- |
| **FR-INST-07** | Admin may **suspend** an instructor. Their published courses become suspended; enrolled learners retain access to completed materials and may join a future batch |

Uses the exact same course-suspension mechanism FR-INST-04's automatic enforcement uses — one status transition in `catalogue`, two different triggers (admin discretion here, WWCC expiry there), distinguished in the audit trail. "Enrolled learners retain access to completed materials" is `materials`' and `learning-delivery`'s existing behaviour for a suspended course, not something this module implements separately.

---

## Acceptance Criteria

1. A rejected applicant receives a reason and can submit a new application, with the prior rejected application remaining visible in their history.
2. An expired WWCC produces an admin alert at the 60-day mark and blocks assignment to (creation of) any under-18-tagged course from that point.
3. The instant a WWCC actually expires without renewal, every currently-published under-18 course owned by that instructor moves to suspended automatically — no admin action required to trigger it.
4. Suspending an instructor (admin-initiated) does not delete learner progress or issued certificates.
5. A course-creation attempt for an under-18-tagged course by an instructor with an already-expired WWCC is refused, naming the expiry date.
6. Renewing a WWCC clears the pending 60-day alert state and does not, on its own, automatically republish any course suspended by the earlier expiry — each requires its own admin review.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-INS-DM-001](../data-model.md) |
| Safeguarding reasoning | [age-and-safeguarding.md §7](/3i/age-and-safeguarding.md#7-instructors) |
| Course dismissal, WWCC scheduling guard | [3I-DEC-013](/3i/decisions/dec-013-instructor-removal-dismisses-course.md), [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md) |
| Course ownership field | `catalogue` |