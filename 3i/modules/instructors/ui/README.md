---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-INS-UI-000
derived_from:
  - requirements/inst-instructor-onboarding.md
tags:
  - ui
  - matrix
---

# Instructors — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Member** | Applying to become an instructor — the same Account, before the role is granted |
| **Instructor** | Managing their own WWCC and storage status once approved |
| **Admin** | |

---

## Matrix

| Screen | Member | Instructor | Admin |
| :---- | :---: | :---: | :---: |
| [Instructor application](screens/instructor-application.md) | ● | | |
| [Admin application review](screens/admin-application-review.md) | | | ● |
| [Admin instructor management](screens/admin-instructor-management.md) | | | ● |
| [WWCC renewal](screens/wwcc-renewal.md) | | ● | |

Four screens.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | WWCC Status Badge, Storage Usage Bar |
| [validation-rules.md](validation-rules.md) | WWCC field validation, rejection-reason requirement |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| None. | |