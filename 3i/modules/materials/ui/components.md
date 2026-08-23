---
project: 3i
module: materials
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-MTL-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Materials — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## Material List Item

Used on: [Course materials list](screens/course-materials-list.md), [Material upload / manage](screens/material-upload-manage.md).

One row per material: type icon (video/document/audio/link), title, duration (video/audio) or estimated read time (document, if available), and a [Progress Indicator](#progress-indicator) reflecting the current learner's `MaterialProgress`. On the instructor-facing management variant, adds a drag handle for reordering (FR-MAT-01, "ordered within a course") and an edit/delete affordance in place of the progress indicator, since an instructor's own consumption isn't the point of that view.

## Progress Indicator

Used on: [Material List Item](#material-list-item), [Video Player](screens/video-player.md), [Document / Audio Viewer](screens/document-audio-viewer.md).

Three visual states: not started, in progress (shows percentage for video/audio, or a simple "viewing" state for document since document completion is binary-ish at 30 seconds rather than a meaningful percentage), and complete (a check mark, once `MaterialProgress.completedAt` is set — permanent once reached, per [data-model.md](../data-model.md#materialprogress), so this indicator never regresses backward even if the learner re-engages with already-completed content).

## Caption Toggle

Used on: [Video Player](screens/video-player.md).

On/off toggle for the required English caption track (FR-MAT-06). Defaults to **on** — not a baseline requirement, but consistent with NFR-12's accessibility posture; a learner who doesn't want captions can turn them off, but the platform doesn't make accessibility opt-in by default.