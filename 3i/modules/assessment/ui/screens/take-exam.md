---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-005
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - exams
  - safeguarding
---

# Screen: Take Exam

Satisfies: FR-EX-02, FR-EX-04, FR-EX-08

---

## Purpose

A learner (via their Member) attempts an exam — timed, autosaved, with no proctoring of any kind.

## Access Gate

Member, for a profile with a qualifying enrolment on the exam's course, within the attempt limit and past any cooldown. Not reachable before `Exam.openDate` or after `Exam.closeDate` where set.

## Contents

Questions in order (randomised per FR-EX-02 if the exam has that flag set; options randomised per-question the same way), the [Attempt Timer](../components.md#attempt-timer), and a submit action.

**No webcam prompt, no tab-switch warning, no IP or location check** (FR-EX-08) — this screen has none of the chrome a proctored exam tool would have, deliberately.

## Behaviour

Answers autosave periodically as the learner works — this is what makes auto-submission-at-expiry meaningful (see [data-model.md](/3i/modules/assessment/data-model.md#the-timer-and-disconnect-detection)); an answer typed and never saved before a disconnect is lost, same as it would be in any autosaved form. **The timer is server-authoritative** — closing and reopening the browser tab doesn't reset or pause it.

On manual submission before time expires, the attempt moves straight to `submitted`. On timer expiry, auto-submission happens using the last autosaved state, and the learner sees this occur rather than being silently redirected. On detected disconnection before either, the attempt is later marked `forfeited` — the learner returning to a forfeited attempt sees that state plainly, not an error.

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12) — the timer especially must stay legible, since a learner glancing at it under time pressure is exactly the wrong moment for a contrast failure. Full RTL mirroring (FR-LOC-04).