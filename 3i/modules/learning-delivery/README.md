---
project: 3i
module: learning-delivery
type: overview
status: current
updated: 2026-08-23
id: 3I-LDL-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Learning Delivery

The module that turns a purchased seat into an actual enrolled learner, schedules and runs the live sessions a batch-based course depends on, and tracks who showed up.

**Module status: complete.** README, data model, both requirements documents, and the full UI stage are written. This module also **resolved every forward reference `catalogue` and `materials` had open at the time** — both can now read a real Enrolment and Batch record instead of a flagged placeholder. (`catalogue`'s separate dependency on `instructors` was resolved later, by `instructors` itself — not by this module.)

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| BAT | Batches and live sessions | 7 |
| ENR | Enrolment, waitlist and age gating | 7 |

Fourteen baseline requirements. Two existing decisions apply directly — [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) (seat as permanent grant, not per-course) and [3I-DEC-013](/3i/decisions/dec-013-instructor-removal-dismisses-course.md)/[3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md) (course dismissal, sessions-delivered attendance, WWCC scheduling guard). No new decisions were needed to scaffold this module.

## Live Sessions Are Held Outside the Platform

The baseline is explicit (§10 preamble): **the platform schedules sessions, distributes links, and records attendance. It does not host live video.** This keeps `learning-delivery` a scheduling and record-keeping module, not a real-time video infrastructure one — a materially different (and much smaller) engineering surface than `materials`' Bunny Stream integration.

## One Seat, Many Courses

**A seat activates a profile, not a course** ([3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md)). This module's FR-ENR-01 check — "enrolment requires an active subscription with an available seat for that learner" — means the **profile** must be active, not that each new course enrolment consumes a fresh seat. A learner with one active seat can enrol in as many courses as they like, and re-join as many batches of the same course as they like (FR-BAT-06), all against that same seat. This is worth stating plainly here because it's the single most likely place for a future implementer to accidentally build a per-course payment check that doesn't exist in the baseline.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-LDL-DM-001 | current |
| [requirements/bat-batches-and-live-sessions.md](requirements/bat-batches-and-live-sessions.md) | 3I-LDL-REQ-001 | current |
| [requirements/enr-enrolment-waitlist-and-age-gating.md](requirements/enr-enrolment-waitlist-and-age-gating.md) | 3I-LDL-REQ-002 | current |
| [ui/README.md](ui/README.md) | 3I-LDL-UI-000 | current — 4 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| Seat as a per-profile, not per-course, grant | [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) |
| Course dismissal, sessions-delivered attendance, WWCC scheduling guard | [3I-DEC-013](/3i/decisions/dec-013-instructor-removal-dismisses-course.md), [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md) |
| Age gating rules, the enrolment override, and its known chat consequence | [age-and-safeguarding.md](/3i/age-and-safeguarding.md#5-the-enrolment-override) |
| Course age tagging and the six-band system | `catalogue` |

## Delivery

Phase 4, Learning (§21.1) — enrolment, progress, batches, attendance, waitlist.

## Forward References Resolved

What this module resolved for other modules when it was built:

| Consumer | Reference | Resolved by |
| :---- | :---- | :---- |
| `catalogue` | Publish gate's "at least one batch" check | `Batch` |
| `catalogue` | `Review` submission's enrolment check | `Enrolment` |
| `catalogue` | "Has upcoming batch" filter, "most enrolled" sort | `Batch`, `Enrolment` |
| `materials` | Video/offline access gate | `Enrolment` |

See each module's own data-model "Forward References" section for the consumer-side detail; this module doesn't restate it.

**This module's own dependencies — on `instructors`, `assessment`, and `communication` — are resolved too, as of 2026-08-23**, once those three modules were built. See [data-model.md](data-model.md#forward-references).

## Open Against This Module

| Item | Note |
| :---- | :---- |
| Fate of an expired 48-hour waitlist offer (FR-ENR-07) | Baseline says the offer "passes to the next in line" but not what happens to the learner who let it lapse. Modelled as: removed from the waitlist entirely, must re-add to try again — a reasonable default, not confirmed |

## Change Requests Owed to the Client

None directly from this module. [3I-DEC-021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md), which this module implements, was already part of the 2026-08-18 batch listed in [decisions/README.md](/3i/decisions/README.md#scope-changes-against-srd-v20).