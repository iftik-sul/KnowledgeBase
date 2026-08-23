---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-004
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - exams
  - instructor
---

# Screen: Exam Configure

Satisfies: FR-EX-01, FR-EX-02, FR-EX-03, FR-EX-06

---

## Purpose

An instructor assembles an exam — practice or final — from their own bank and the admin bank, and sets its timing, attempt, and reveal rules.

## Access Gate

Instructor only, for courses they own.

## Fields

Title, type (practice/final — see [validation-rules.md](../validation-rules.md#one-final-exam-per-course) for the one-final cap), duration, pass mark, max attempts (default 3), cooldown (**default differs by type** — pre-filled at 24h for practice, 168h for final, editable), open/close dates (optional), randomise questions/options toggles, and the reveal-answers policy selector (`standard` / `always` / `never`, defaulting to `standard`).

**Question picker**: [Question Card](../components.md#question-card)s from the instructor's own bank and the admin bank, each selectable with a per-exam marks override. Total marks displayed live as a running sum, computed from current selections — never a field the instructor types in directly.

## Behaviour

Questions from either bank can sit in the same exam — there's no rule limiting an exam to one source, since FR-QB-02's whole point is letting an instructor draw on the shared admin set alongside their own.

## Role Variations

Instructor only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring (FR-LOC-04).