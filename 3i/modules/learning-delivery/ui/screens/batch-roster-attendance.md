---
project: 3i
module: learning-delivery
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-LDL-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - batches
  - instructor
---

# Screen: Batch Roster & Attendance

Satisfies: FR-BAT-03, FR-BAT-07

---

## Purpose

An instructor views the roster of enrolled learners for a batch and marks attendance after each session.

## Access Gate

Instructor only, for batches they own.

## Contents

A [Session Row](../components.md#session-row) selector, and for the selected session, a roster of every learner profile with an `active`-status Enrolment on the batch **as of that session's date** (FR-BAT-07) — a learner who joined after a given session's date does not appear on that earlier session's roster. Each roster row has a present / absent / late / excused selector (FR-BAT-03).

## Behaviour

Attendance is **saved per session independently** — marking session 3 does not touch or require session 1 or 2's records, and the instructor can mark sessions in any order, not strictly sequentially. Once a session's status is `delivered` (past its scheduled time, per [data-model.md](../data-model.md#session)), its roster remains editable — the baseline doesn't specify a lock-after-N-days rule, so attendance can be corrected retroactively without a time limit, a reasonable default rather than a confirmed one.

## Role Variations

Instructor only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the instructor panel supports it (FR-LOC-04).