---
project: 3i
module: assessment
type: requirements
status: current
updated: 2026-08-23
id: 3I-ASM-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - question-bank
---

# Question Bank

Baseline §12.1. Seven requirements, none amending the baseline — [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md) specifies *how* FR-QB-03/04's isolation is enforced, without changing what either requirement says.

---

## Two Scopes

| ID | Requirement |
| :---- | :---- |
| **FR-QB-01** | Two bank scopes: **admin** and **instructor** |
| **FR-QB-02** | Instructors may view and **copy** admin questions into their own bank. The copy is independent and editable |

Copying creates a genuinely new `Question` row, owned by the copying instructor, with `copiedFromQuestionId` set purely for provenance (see [data-model.md](../data-model.md#question)). Editing the copy afterward never touches the original admin question, and editing the original admin question afterward never touches any copy already made from it — the two are fully decoupled the instant the copy exists.

---

## Isolation

| ID | Requirement |
| :---- | :---- |
| **FR-QB-03** | Instructor questions are **private to their owner**. They are invisible to other instructors **and to admins** |
| **FR-QB-04** | Isolation is enforced **at the query layer**. A request for another instructor's bank returns **404, not 403** |

Full mechanism and reasoning in [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md) — not restated here. The requirement-level summary: every read path (bank listing, single-question fetch, exam assembly, bulk import row lookups, reporting, exports) carries the scope filter as a hard requirement, and admin has no bypass.

---

## Question Content

| ID | Requirement |
| :---- | :---- |
| **FR-QB-05** | Question types: single-answer MCQ, multi-select MCQ, true/false, short answer, essay |
| **FR-QB-06** | Each question carries marks, optional negative marks, optional partial credit, difficulty, and an explanation |

See [data-model.md](../data-model.md#question) for the correct-answer shape per type. Negative marks and partial credit are both optional and both most meaningful for the two MCQ variants — a `short_answer` or `essay` question carrying negative marks is legal but has no practical effect, since those types are never auto-scored against a stored correct answer.

---

## Bulk Import

| ID | Requirement |
| :---- | :---- |
| **FR-QB-07** | Bulk import via CSV/Excel with a downloadable template, row-level validation, and an error report |

**CSV and Excel only — not docx.** See [README.md](../README.md#two-ways-questions-get-in) for why: a spreadsheet is naturally tabular in a way a word-processing document isn't, and that's what makes row-level validation possible at all.

**Template columns**, one row per question:

| Column | Required | Notes |
| :---- | :---- | :---- |
| `type` | Yes | `mcq` \| `multi_select` \| `true_false` \| `short_answer` \| `essay` |
| `question_text` | Yes | |
| `option_1`–`option_6` | Conditional | `mcq`/`multi_select` only. Blank columns ignored |
| `correct_answer` | Conditional | `mcq`: one option letter. `multi_select`: pipe-separated letters (e.g. `A\|C`). `true_false`: `True`/`False`. `short_answer`: optional model answer, non-authoritative. `essay`: ignored |
| `marks` | Yes | Positive integer |
| `negative_marks` | No | Integer, default 0, capped at `marks` |
| `partial_credit` | No | Yes/No, meaningful only for `multi_select` |
| `difficulty` | No | `easy`/`medium`/`hard`, default `medium` |
| `explanation` | No | |

**Course tagging applies to the whole batch**, chosen once before upload, not as a per-row column — a batch of imported questions for one course is the common case, and per-row course assignment would add complexity the baseline doesn't ask for.

**Preview-then-commit, not partial silent import.** Every row is validated first — valid type, `correct_answer` letters actually matching non-blank option columns, numeric fields parsing, negative marks not exceeding marks — producing a full row-level error report (row number, column, message) **before anything is written**. The uploader sees exactly what will and won't import, and commits the valid rows in one explicit action. This is a reasonable-default choice, not baseline-mandated; the alternative (write valid rows immediately, report errors after) leaves the uploader unsure what already landed.

**Imported questions inherit the uploader's own scope** — an instructor's import lands in their `instructor`-scope bank, an admin's import lands in `admin`-scope, under the same isolation rules as any manually created question (FR-QB-04). Import is a second write path into the same model, not an exception to it.

---

## Acceptance Criteria

1. An instructor querying another instructor's bank receives 404, indistinguishable from querying a bank that doesn't exist.
2. An admin querying any instructor's individual question by ID also receives 404 — admin has no bypass.
3. Copying an admin question, then editing the copy, does not alter the original admin question.
4. A CSV import of 200 rows, several deliberately malformed, reports every error by row and column without writing any row until the uploader commits.
5. A committed import's questions appear only in the uploader's own scoped bank, subject to the same isolation as manually created questions.
6. A `multi_select` question's `partial_credit` flag has no effect when set on a `short_answer` or `essay` question — it's simply inert, not an error.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-ASM-DM-001](../data-model.md) |
| Isolation mechanism | [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md) |
| Examinations | [3I-ASM-REQ-002](ex-examinations.md) |