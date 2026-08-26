---
project: 3i
module: materials
type: ui-spec
status: current
updated: 2026-08-26
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

**Audio playback UI is deferred, not designed at this pass** — a direct sequencing call, 2026-08-26, not a requirements change. Audio remains a valid material type per FR-MAT-01 and the data model is unaffected; only the Figma design work for the audio-specific layout is currently out of scope. Document viewing is the only variant being actively designed right now.

## Access Gate

Member with a qualifying enrolment, checked directly against `learning-delivery`'s `Enrolment` record.

## Contents

**Document:** rendered directly in an in-page viewer (FR-MAT-07) — no separate download, no "open in new tab to the raw file" link, since either would defeat the no-download rule this screen exists to enforce.

**Document layout, 2026-08-26:** the document fills the entire left region of the screen edge-to-edge — not a smaller card inset within a dark surround. The elaborate top status bar used on [Video Player](video-player.md) (course title, course-progress bar, edit/bookmark/fullscreen icons) is **not** carried over here — those are video-specific affordances (fullscreen in particular makes no sense for a panel that already fills its container). In its place, a minimal top bar with a **back button only**, top-left. The right-hand course-content sidebar is unchanged from [Video Player](video-player.md) — same component, same states. Below the document region, the lesson title/breadcrumb, the Overview/Notes tabs, and the Previous Lesson / Next Lesson buttons all remain exactly as on [Video Player](video-player.md) — only the content-viewport region and its header differ.

**Audio (deferred):** standard playback controls, [Progress Indicator](../components.md#progress-indicator) reflecting cumulative percentage played, same accumulation principle as video — retained here as a written spec for whenever this variant is picked back up, not currently being designed.

## Behaviour

**Document completion timing is continuous, not cumulative** — per [data-model.md](../../data-model.md#materialprogress), the viewer must remain open for 30 continuous seconds in one sitting; closing at 29 seconds and reopening later does not carry a partial count forward. This is a judgement call on an ambiguous requirement, flagged as such in the data model — not a hard baseline guarantee.

**Audio, like video, accumulates progress across sessions** and never regresses once a percentage is earned.

## Role Variations

**Member:** full viewing/listening with progress tracking.
**Instructor:** preview access to their own course's materials, no progress tracked.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): document viewer chrome mirrors; document content itself follows its own authored direction, not the UI's.
