---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - question-bank
  - instructor
---

# Screen: Question Bank Manage

Satisfies: FR-QB-01, FR-QB-02, FR-QB-05, FR-QB-06

---

## Purpose

An instructor's own question bank — create, edit, delete manually, and browse-and-copy from the admin bank.

## Access Gate

Instructor only. Shows exclusively this instructor's own `instructor`-scope questions — [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md) applies at the query itself, not as a client-side filter.

## Contents

**My Questions tab:** [Question Card](../components.md#question-card) grid/list of every question this instructor owns, with **Add Question** opening a type-first form (select type, then the form adapts — option fields for MCQ variants, none for essay) and per-card edit/delete.

**Browse Admin Bank tab:** read-only [Question Card](../components.md#question-card)s from the `admin`-scope bank, each with a **Copy to My Bank** action (FR-QB-02). Copying immediately creates an independent row in "My Questions" — the instructor is taken there (or shown a confirmation) rather than left wondering whether it worked.

## Behaviour

Saving a manually created or edited question requires: type, question text, marks. Type-conditional requirements (options + correct answer for MCQ variants) are enforced only for those types — an essay question is valid with just text and marks.

## Role Variations

Instructor only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring (FR-LOC-04).