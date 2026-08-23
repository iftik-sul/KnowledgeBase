---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-006
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - exams
---

# Screen: Exam Result

Satisfies: FR-EX-03, FR-EX-05, FR-EX-06, FR-EX-07

---

## Purpose

Shows a learner's result for an exam — score, pass/fail, and correct-answer reveal, gated by the exam's reveal policy.

## Access Gate

Member, for their own profile's attempts only.

## Contents

Score and pass/fail state (once fully graded — see below for the awaiting-grading case), attempt number out of the max, and the [Reveal Gate](../components.md#reveal-gate) showing or withholding correct answers and explanations per the exam's policy.

**"Highest score retained" (FR-EX-03)** is what's shown as the headline result whenever more than one attempt has been submitted — not the most recent attempt, the best one. Individual past attempts remain viewable underneath, so a learner can still see what happened on an earlier, lower-scoring try.

**If the attempt contains ungraded written answers** (FR-EX-05), this screen shows a clear "awaiting grading" state instead of a score — no partial or provisional score is shown for the auto-graded portion alone, since a partial number could be mistaken for the final result.

**A failed final exam** (FR-EX-07) shows a plain retry action if attempts remain, or a clear "no attempts remaining" state if not — no special messaging beyond what any exhausted-attempts case already shows.

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).