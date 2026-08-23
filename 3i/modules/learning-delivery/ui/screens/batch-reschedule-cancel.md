---
project: 3i
module: learning-delivery
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-LDL-UI-004
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - batches
  - instructor
---

# Screen: Batch Reschedule / Cancel

Satisfies: FR-BAT-02, FR-BAT-04, FR-BAT-05

---

## Purpose

An instructor reschedules an individual session or cancels the entire batch, and posts meeting links ahead of each session.

## Access Gate

Instructor only, for batches they own.

## Contents

Per-session **Reschedule** action (new date/time, [Session Row](../components.md#session-row)-based) and a batch-level **Cancel Batch** action, styled and confirmed as a harder action than a single reschedule since it affects every remaining session and every enrolled learner at once.

A **meeting link field** per upcoming session, which on save triggers posting to the batch's chat room and by email (FR-BAT-02) — both channels, not a choice between them; see [requirements](../../requirements/bat-batches-and-live-sessions.md#meeting-links) for why both matter.

## Behaviour

**Rescheduling** a session immediately triggers push and email to every enrolled learner (FR-BAT-04) — automatic, not a separate "notify" step the instructor has to remember to trigger.

**Cancelling the batch** notifies every enrolled learner, with copy stating plainly that no refund applies and access continues (FR-BAT-05) — consistent with [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md), since the learner's seat was never tied to this specific batch. The cancellation flow should surface a next step (browse other open batches of the same course) rather than leaving the learner at a dead end.

## Role Variations

Instructor only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the instructor panel supports it (FR-LOC-04).