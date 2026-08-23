---
project: 3i
module: materials
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-MTL-UI-000
derived_from:
  - requirements/mat-course-materials-and-video-delivery.md
tags:
  - ui
  - matrix
---

# Materials — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Member** | The renamed Account holder role — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md), with a learner profile active and a qualifying enrolment |
| **Instructor** | The owning instructor of the course a material belongs to |
| **Mobile (Flutter)** | Not a role — a platform column, since offline management exists only there |

---

## Matrix

| Screen | Member | Instructor | Mobile |
| :---- | :---: | :---: | :---: |
| [Course materials list](screens/course-materials-list.md) | ● | ● (view) | ● |
| [Video player](screens/video-player.md) | ● | ● (preview) | ● |
| [Document / audio viewer](screens/document-audio-viewer.md) | ● | ● (preview) | ● |
| [Material upload / manage](screens/material-upload-manage.md) | | ● | |
| [Mobile offline manager](screens/mobile-offline-manager.md) | | | ● |

Five screens. **No admin-specific screen** — per FR-MAT-09, materials aren't independently admin-moderated; admin's only lever over a course's content is the course-level approval/suspend/take-down actions already specified in `catalogue`.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | Material list item, progress indicator, caption toggle |
| [validation-rules.md](validation-rules.md) | Upload limits and type validation, caption requirement |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| None. | |

**The enrolment/entitlement check gating access to [Video Player](screens/video-player.md), [Document / Audio Viewer](screens/document-audio-viewer.md), and [Mobile Offline Manager](screens/mobile-offline-manager.md) was originally forward-referenced pending `learning-delivery`.** That module is real and built now — see [data-model.md](../data-model.md#forward-references--resolved-2026-08-23).