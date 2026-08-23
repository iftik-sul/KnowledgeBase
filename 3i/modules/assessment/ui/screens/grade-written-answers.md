---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-007
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - exams
  - instructor
---

# Screen: Grade Written Answers

Satisfies: FR-EX-05

---

## Purpose

An instructor manually grades short-answer and essay responses from submitted attempts on their own courses.

## Access Gate

Instructor only, for exams on courses they own.

## Contents

A queue of every `submitted` attempt with `awaitingManualGrading = true` for this instructor's exams, each showing the learner's written answer, the question's optional model answer (for `short_answer`, shown as reference only — see [data-model.md](/3i/modules/assessment/data-model.md#question)), and a marks-awarded field per ungraded question in that attempt.

## Behaviour

**No service-level grading turnaround is enforced or displayed** (FR-EX-05) — unlike [chat's moderation queue](/3i/modules/communication/README.md), there's no SLA countdown here; the baseline is explicit that none is promised. Once every written question in an attempt is graded, `awaitingManualGrading` flips to false and the attempt's overall `score`/`passed` compute and the learner's [Exam Result](exam-result.md) updates.

**Grading one attempt does not affect any other** — same independence principle already established for batch attendance ([learning-delivery](/3i/modules/learning-delivery/ui/screens/batch-roster-attendance.md)).

## Role Variations

Instructor only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the instructor panel supports it (FR-LOC-04).