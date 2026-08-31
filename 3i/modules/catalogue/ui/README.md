---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-CAT-UI-000
derived_from:
  - requirements/crs-course-catalogue-and-management.md
tags:
  - ui
  - matrix
---

# Catalogue — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

**Only the two Admin-facing screens below remain paused for visual design** — [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md), narrowed by [3I-DEC-039](/3i/decisions/dec-039-instructor-self-service-unpaused.md) to Admin-role screens specifically. [Course Create/Edit](screens/course-create-edit.md) is Instructor-role self-service and is now unpaused, designable using the standard system.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Public** | No session, or a session with no learner profile active |
| **Member** | The renamed Account holder role — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md), browsing with a learner profile active |
| **Instructor** | |
| **Admin** | |
| **Mobile (Flutter)** | Not a role — a platform column marking which screens are in scope for the native app. See [mobile-scope.md](/3i/mobile-scope.md) |

---

## Matrix

| Screen | Public | Member | Instructor | Admin | Mobile |
| :---- | :---: | :---: | :---: | :---: | :---: |
| [Catalogue browse](screens/catalogue-browse.md) | ● | ● | | | ● |
| [Course detail](screens/course-detail.md) | ● | ● | | | ● |
| [Course create / edit](screens/course-create-edit.md) | | | ● | | |
| [Admin review queue](screens/admin-review-queue.md) ⚠ paused | | | | ● | |
| [Admin course management](screens/admin-course-management.md) ⚠ paused | | | | ● | |
| [Rate \& review](screens/rate-and-review.md) | | ● | | | ● |

Six screens, three in scope for mobile — see [mobile-scope.md](/3i/mobile-scope.md#2-scope-by-module).

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | Course Card, Filter Panel |
| [validation-rules.md](validation-rules.md) | Age field, publish gate, category requirement |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md), narrowed by [3I-DEC-039](/3i/decisions/dec-039-instructor-self-service-unpaused.md) | Figma design work on the 2 ⚠-marked Admin screens above only |

**All forward references this module originally carried are resolved** (2026-08-23) — `instructors`, `materials`, and `learning-delivery` are all real, built modules now. See [data-model.md](../data-model.md#forward-references--all-resolved-2026-08-23).
