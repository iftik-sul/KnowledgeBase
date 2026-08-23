---
project: 3i
module: instructors
type: overview
status: current
updated: 2026-08-23
id: 3I-INS-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Instructors

The module that turns an applicant into an approved instructor, keeps their Working With Children Check current and enforced, and is the thing every other module has been forward-referencing as `instructorId` since `catalogue` was first written.

**Module status: complete.** README, data model, requirements, and the full UI stage are written. This module **resolves the last standing forward reference** in the project — `Course.instructorId`, `Batch.instructorId`, and the WWCC scheduling guard are all real now.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| INST | Instructor onboarding | 7 |

Two existing decisions apply directly: [3I-DEC-013](/3i/decisions/dec-013-instructor-removal-dismisses-course.md) (losing an instructor mid-course dismisses the course) and [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md) (the WWCC scheduling guard this module's data now makes real). No new decisions were needed to scaffold this module.

## Instructor Is a Role Held By an Account, Not a Separate Identity

**Deliberate modelling choice, stated plainly because it's easy to get wrong by analogy with Learner:** a `Learner` is a distinct person a Member manages, with its own identity separate from the account holder. An **instructor is not that** — it's the account holder *themselves*, holding the Instructor role (FR-RBAC-02). The person who applies, gets approved, and teaches is the same Account that logs in.

So the `InstructorProfile` this module owns is a **1:1 extension of `identity-and-access`'s Account, keyed by the same id** — not a new independent entity with its own primary key. This is exactly the shape `Course.instructorId` and `Batch.instructorId` already assumed when `catalogue` and `learning-delivery` forward-referenced them: a plain Account id. Modelling `InstructorProfile` any other way would mean every existing `instructorId` field in two already-specified modules would need to change meaning. It doesn't, because this table is purely additive.

## What This Fixes

Three requirements depend on a real, queryable WWCC expiry date — not just data captured once at application time and left inert:

- **FR-INST-03** — the 60-day admin alert needs something to check on a schedule.
- **FR-INST-04** — blocking an expired-WWCC instructor from under-18 courses needs a live field to check at course-creation and at the moment expiry actually passes.
- **The WWCC scheduling guard** ([3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md), already documented in `learning-delivery` as reading from this module) needs the same field.

See [data-model.md](data-model.md#instructorprofile) for the field itself.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-INS-DM-001 | current |
| [requirements/inst-instructor-onboarding.md](requirements/inst-instructor-onboarding.md) | 3I-INS-REQ-001 | current |
| [ui/README.md](ui/README.md) | 3I-INS-UI-000 | current — 4 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| WWCC capture, the 60-day alert, and the expired-WWCC teaching block | [age-and-safeguarding.md §7](/3i/age-and-safeguarding.md#7-instructors) |
| Course dismissal on instructor loss | [3I-DEC-013](/3i/decisions/dec-013-instructor-removal-dismisses-course.md) |
| WWCC scheduling guard, sessions-delivered attendance | [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md) |
| One instructor per course, course ownership | `catalogue` (`Course.instructorId`, now resolved) |

## Delivery

Phase 1, Foundation (§21.1) in the baseline's own sequencing — though this project built it much later than that, once every module that reads `instructorId` already existed and could be checked against a real reference rather than an assumed one.

## Forward References Resolved

| Consumer | Reference | Now resolved by |
| :---- | :---- | :---- |
| `catalogue` | `Course.instructorId` | `InstructorProfile` (keyed by the same Account id) |
| `catalogue` | FR-CRS-07's instructor-name search | `InstructorProfile` |
| `learning-delivery` | `Batch.instructorId`, WWCC expiry for the scheduling guard | `InstructorProfile.wwccExpiryDate` |

## Open Against This Module

| Item | Note |
| :---- | :---- |
| WWCC legal position | **Outstanding client dependency, §22.2 item 4**, from the institute's lawyer. This module is fully specified without it — the data model and enforcement logic don't depend on the legal analysis — but it may inform exactly what "WWCC" means for interstate or overseas instructors, which this spec doesn't attempt to resolve |
| Storage-quota enforcement lives partly outside this module | FR-INST-05's 50GB quota is a field this module owns (`InstructorProfile.storageQuotaBytes`), but **enforcing it at upload time is `materials`' responsibility**, not something this module's own screens do. `materials`' existing upload validation ([3I-MTL-UI-VAL](/3i/modules/materials/ui/validation-rules.md)) does not yet reference it — flagged here as an addition that module will need, not a change to anything already decided there |
| Who updates WWCC on renewal | Not specified in the baseline. Modelled as instructor-initiated (their own credential to keep current), landing directly on `InstructorProfile` without requiring a fresh application — reasonable default, not confirmed |

## Change Requests Owed to the Client

None. Nothing in this module amends or reverses the baseline.