---
project: 3i
module: materials
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-MTL-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - materials
---

# Screen: Document / Audio Viewer

Satisfies: FR-MAT-07, FR-MAT-08

---

## Purpose

In-browser rendering of a document, or playback of an audio material, with no download offered on web.

## Access Gate

Member with a qualifying enrolment, checked directly against `learning-delivery`'s `Enrolment` record.

## Contents

**Document:** rendered directly in an in-page viewer (FR-MAT-07) — no separate download, no "open in new tab to the raw file" link, since either would defeat the no-download rule this screen exists to enforce.

**Audio:** standard playback controls, [Progress Indicator](../components.md#progress-indicator) reflecting cumulative percentage played, same accumulation principle as video.

## Behaviour

**Document completion timing is continuous, not cumulative** — per [data-model.md](../data-model.md#materialprogress), the viewer must remain open for 30 continuous seconds in one sitting; closing at 29 seconds and reopening later does not carry a partial count forward. This is a judgement call on an ambiguous requirement, flagged as such in the data model — not a hard baseline guarantee.

**Audio, like video, accumulates progress across sessions** and never regresses once a percentage is earned.

## Role Variations

**Member:** full viewing/listening with progress tracking.
**Instructor:** preview access to their own course's materials, no progress tracked.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): document viewer chrome and audio player controls mirror; document content itself follows its own authored direction, not the UI's.