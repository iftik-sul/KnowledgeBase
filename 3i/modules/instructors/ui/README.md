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

**Only the two Admin-facing screens below remain paused for visual design** — [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md), narrowed by [3I-DEC-039](/3i/decisions/dec-039-instructor-self-service-unpaused.md) to Admin-role screens specifically. Instructor Application, WWCC Renewal, and the new Instructor Dashboard are all unpaused, designable now using the standard system.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Member** | Applying to become an instructor — the same Account, before the role is granted |
| **Instructor** | Managing their own WWCC, storage status, courses, and batches once approved |
| **Admin** | |
| **Mobile (Flutter)** | Not a role — a platform column marking which screens are in scope for the native app. See [mobile-scope.md](/3i/mobile-scope.md) |

---

## Matrix

| Screen | Member | Instructor | Admin | Mobile |
| :---- | :---: | :---: | :---: | :---: |
| [Instructor application](screens/instructor-application.md) | ● | | | ● |
| [Instructor dashboard](screens/instructor-dashboard.md) | | ● | | ● |
| [Admin application review](screens/admin-application-review.md) ⚠ paused | | | ● | |
| [Admin instructor management](screens/admin-instructor-management.md) ⚠ paused | | | ● | |
| [WWCC renewal](screens/wwcc-renewal.md) | | ● | | ● |

Five screens, three in scope for mobile — see [mobile-scope.md](/3i/mobile-scope.md#3-decisions-worth-recording) for why the document-capture screens (application and renewal) are included; Instructor Dashboard added to mobile scope 2026-08-26 as a general browsing/overview screen, consistent with Guardian and Learner Dashboard both being mobile-in-scope.

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
| [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md), narrowed by [3I-DEC-039](/3i/decisions/dec-039-instructor-self-service-unpaused.md) | Figma design work on the 2 ⚠-marked Admin screens above only |
