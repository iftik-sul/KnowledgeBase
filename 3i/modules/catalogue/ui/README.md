---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CAT-UI-000
derived_from:
  - requirements/crs-course-catalogue-and-management.md
tags:
  - ui
  - matrix
---

# Catalogue — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Public** | No session, or a session with no learner profile active |
| **Member** | The renamed Account holder role — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md), browsing with a learner profile active |
| **Instructor** | |
| **Admin** | |

---

## Matrix

| Screen | Public | Member | Instructor | Admin |
| :---- | :---: | :---: | :---: | :---: |
| [Catalogue browse](screens/catalogue-browse.md) | ● | ● | | |
| [Course detail](screens/course-detail.md) | ● | ● | | |
| [Course create / edit](screens/course-create-edit.md) | | | ● | |
| [Admin review queue](screens/admin-review-queue.md) | | | | ● |
| [Admin course management](screens/admin-course-management.md) | | | | ● |
| [Rate \& review](screens/rate-and-review.md) | | ● | | |

Six screens.

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
| None against this module's own screens. | |

**Three forward references remain open against modules not yet built** — `instructors`, `materials`, `learning-delivery` — flagged in [data-model.md](../data-model.md#forward-references) and [README.md](../README.md#open-against-this-module) rather than repeated here. They affect what a screen can *show* (e.g. instructor name, upcoming-batch filter) but not this module's own specification.