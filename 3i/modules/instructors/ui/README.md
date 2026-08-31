---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-INS-UI-000
derived_from:
  - requirements/inst-instructor-onboarding.md
tags:
  - ui
  - matrix
---

# Instructors — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

**[Instructor Application](screens/instructor-application.md) is paused for visual design — see [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md), extended to this module by [3I-DEC-038](/3i/decisions/dec-038-instructor-registration-account-works-normally.md).** Its behaviour and data flow are settled and current; only Figma work is deferred.

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
| [Instructor application](screens/instructor-application.md) ⚠ paused | ● | | | ● |
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
| [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md) | Figma design work on Instructor Application |
