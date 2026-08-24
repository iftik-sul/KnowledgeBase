---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-24
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
| **Mobile (Flutter)** | Not a role — a platform column marking which screens are in scope for the native app. See [mobile-scope.md](/3i/mobile-scope.md) |

---

## Matrix

| Screen | Member | Instructor | Admin | Mobile |
| :---- | :---: | :---: | :---: | :---: |
| [Instructor application](screens/instructor-application.md) | ● | | | ● |
| [Admin application review](screens/admin-application-review.md) | | | ● | |
| [Admin instructor management](screens/admin-instructor-management.md) | | | ● | |
| [WWCC renewal](screens/wwcc-renewal.md) | | ● | | ● |

Four screens, two in scope for mobile — see [mobile-scope.md](/3i/mobile-scope.md#3-decisions-worth-recording) for why both document-capture screens (application and renewal) are included together.

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
