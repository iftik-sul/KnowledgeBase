---
project: 3i
module: materials
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-MTL-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - materials
---

# Screen: Course Materials List

Satisfies: FR-MAT-01

---

## Purpose

The ordered list of every material in a course — a learner's entry point into course content.

## Access Gate

Member, with a learner profile active and a qualifying enrolment on the course, checked directly against `learning-delivery`'s `Enrolment` record. Instructor sees the same list, view-only, for courses they own (management happens on [Material Upload / Manage](material-upload-manage.md) instead).

## Contents

Ordered [Material List Item](../components.md#material-list-item)s, one per material, in the course's defined order. Selecting a video or audio item opens [Video Player](video-player.md) or [Document / Audio Viewer](document-audio-viewer.md) respectively; selecting an external link opens it in a new tab (no in-platform tracking of external-link "completion," since there's no meaningful way to measure consumption of a link the platform doesn't control).

## Role Variations

**Member:** entry point into content, with per-item progress shown.
**Instructor:** identical list, view-only, no progress indicators (an instructor's own consumption isn't tracked — [data-model.md](../../data-model.md#materialprogress) is learner-scoped).

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): list order and the drag-to-reorder affordance (instructor variant) both mirror.