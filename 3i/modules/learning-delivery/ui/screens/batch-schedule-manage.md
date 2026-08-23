---
project: 3i
module: learning-delivery
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-LDL-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - batches
  - instructor
---

# Screen: Batch Schedule / Manage

Satisfies: FR-BAT-01

---

## Purpose

An instructor creates a batch for their `Online Class`/`Mixed` course — name, capacity, session count, duration, and every session's date and time.

## Access Gate

Instructor only, for courses they own.

## Contents

Name, capacity, number of classes, approximate duration per class, and a [Session Row](../components.md#session-row) per scheduled session with a date/time picker.

## Behaviour

**Every session date is validated against the WWCC scheduling guard** (see [validation-rules.md](../validation-rules.md#wwcc-scheduling-guard)) before the batch can be saved — a single offending session refuses the whole creation, naming which session and the instructor's expiry date, rather than silently dropping just that one session from an otherwise-created batch.

Once created, this screen also serves as the read-only view of a batch's schedule for reference — editing capacity or session count after learners have enrolled is a judgement call left to the instructor, with a warning shown if the change would put an already-`active` Enrolment over the new capacity.

## Role Variations

Instructor only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring (FR-LOC-04).