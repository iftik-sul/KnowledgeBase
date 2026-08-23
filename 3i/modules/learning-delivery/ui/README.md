---
project: 3i
module: learning-delivery
type: ui-spec
status: current
updated: 2026-08-23
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

---

## Roles

| Column | Who |
| :---- | :---- |
| **Member** | The renamed Account holder role — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md), enrolling on behalf of a profile or themselves |
| **Instructor** | The owning instructor of the batch/course |

---

## Matrix

| Screen | Member | Instructor |
| :---- | :---: | :---: |
| [Enrol \& waitlist](screens/enrol-and-waitlist.md) | ● | |
| [Batch schedule / manage](screens/batch-schedule-manage.md) | | ● |
| [Batch roster \& attendance](screens/batch-roster-attendance.md) | | ● |
| [Batch reschedule / cancel](screens/batch-reschedule-cancel.md) | | ● |

Four screens.

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
| None against this module's own screens. | |

**Two forward references remain open** against modules not yet built — `instructorId`/WWCC expiry (`instructors`) and meeting-link chat distribution (`communication`). Neither blocks this module's own screens; see [data-model.md](../data-model.md#forward-references).