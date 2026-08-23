---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Assessment — Validation Rules

Field-level and flow-level validation shared across two or more assessment screens.

---

## CSV Import Row Validation

On [Bulk Import Questions](screens/bulk-import-questions.md): every row is checked before any row is written (see [requirements](../requirements/qb-question-bank.md#bulk-import) for the full column spec) — `type` is one of the five valid values; `correct_answer` letters actually correspond to non-blank `option_*` columns for `mcq`/`multi_select`; `marks` and `negative_marks` are valid non-negative integers; `negative_marks` does not exceed `marks`. Every failure is reported with its row number, the offending column, and a specific message — never a generic "row 14 invalid."

## Negative Marks Cap

On [Question Bank Manage](screens/question-bank-manage.md), [Admin Question Bank](screens/admin-question-bank.md), and CSV import: `negative_marks` cannot exceed `marks` (see [data-model.md](../data-model.md#question)) — not baseline-stated, a reasonable default preventing a single question from being able to produce a larger score deduction than it could ever have awarded.

## One Final Exam Per Course

On [Exam Configure](screens/exam-configure.md): selecting `type = final` is refused with a specific message if the course already has one (FR-EX-01) — the instructor sees why, and is pointed toward editing the existing final exam instead of guessing.