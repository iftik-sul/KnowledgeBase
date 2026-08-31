---
project: 3i
module: learning-delivery
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-LDL-UI-000
derived_from:
  - requirements/bat-batches-and-live-sessions.md
  - requirements/enr-enrolment-waitlist-and-age-gating.md
tags:
  - ui
  - matrix
---

# Learning Delivery — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

**All screens in this module are Instructor- or Member-role self-service — none are paused.** Confirmed explicitly by [3I-DEC-039](/3i/decisions/dec-039-instructor-self-service-unpaused.md); this module was never covered by [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md)'s original scope, and DEC-039 removes any ambiguity rather than leaving it unstated.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Member** | The renamed Account holder role — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md), enrolling on behalf of a profile or themselves |
| **Instructor** | The owning instructor of the batch/course |
| **Mobile (Flutter)** | Not a role — a platform column marking which screens are in scope for the native app. See [mobile-scope.md](/3i/mobile-scope.md) |

---

## Matrix

| Screen | Member | Instructor | Mobile |
| :---- | :---: | :---: | :---: |
| [Enrol \& waitlist](screens/enrol-and-waitlist.md) | ● | | ● |
| [Batch schedule / manage](screens/batch-schedule-manage.md) | | ● | |
| [Batch roster \& attendance](screens/batch-roster-attendance.md) | | ● | ● |
| [Batch reschedule / cancel](screens/batch-reschedule-cancel.md) | | ● | |

Four screens, two in scope for mobile — see [mobile-scope.md](/3i/mobile-scope.md#2-scope-by-module).

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | Session Row, Waitlist Position Badge |
| [validation-rules.md](validation-rules.md) | Age-gate check and override, waitlist promotion window |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| None. | |

**Both forward references this module's screens originally carried are resolved** (2026-08-23) — `instructorId`/WWCC expiry (`instructors`) and meeting-link chat distribution (`communication`) are both real, built modules now. See [data-model.md](../data-model.md#forward-references--resolved-2026-08-23).
