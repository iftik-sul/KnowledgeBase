---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - question-bank
---

# Screen: Bulk Import Questions

Satisfies: FR-QB-07

---

## Purpose

Upload a CSV or Excel file of questions, see validation results, and commit the valid rows into the uploader's own bank.

## Access Gate

Instructor or Admin. Imported questions land in the uploader's own scope — `instructor` or `admin` — identical to a manually created question from the same account.

## Contents

- **Download template** — the exact column spec from [requirements](../requirements/qb-question-bank.md#bulk-import), pre-filled with one or two example rows per question type.
- Optional **course** selector, applied to the whole batch (not per-row).
- File upload (CSV or Excel only — **no docx**, see [README.md](/3i/modules/assessment/README.md#two-ways-questions-get-in)).
- **Preview \& Validate** step: a table of every row with a pass/fail indicator, and a full error list (row, column, message) for anything that failed (see [validation-rules.md](../validation-rules.md#csv-import-row-validation)).
- **Commit** — enabled once validation has run, imports only the passing rows. Failed rows are never written; the uploader can fix the source file and re-upload rather than hunting for what silently didn't make it in.

## Behaviour

Nothing is written to the database until **Commit** is explicitly pressed — validation alone never creates a question, however clean the file.

## Role Variations

Identical for Instructor and Admin, differing only in which scope the import lands in.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04): the row-by-row validation table mirrors as a whole, including error-column ordering.