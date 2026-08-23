---
project: 3i
module: assessment
type: overview
status: current
updated: 2026-08-23
id: 3I-ASM-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Assessment

The module that lets an instructor build a private (or admin, a shared) bank of questions, assemble exams from them, and run the attempt-taking, timing, grading, and reveal logic a learner actually experiences.

**Module status: complete.** README, data model, both requirements documents, and the full UI stage are written.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| QB | Question bank | 7 |
| EX | Examinations | 8 |

Fifteen baseline requirements. One existing decision applies directly and is load-bearing for this whole module: [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md) (question bank isolation enforced at the query layer, 404 not 403, admin included). No new decisions were needed to scaffold this module.

## Two Banks, One Question Model

Every `Question` carries a `scope` — `admin` or `instructor` (FR-QB-01). An instructor's questions are invisible to every other instructor **and to admin** (FR-QB-03) — [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md) is explicit that this holds across admin tooling, reporting, and exports, not just the obvious question-list screen. An instructor may copy an admin question into their own bank; the copy is a genuinely independent, editable row from that point on, not a reference back to the original (FR-QB-02).

## Two Ways Questions Get In

Manual creation (a form, one question at a time — the everyday path) and bulk import via CSV/Excel (FR-QB-07, for someone bringing in a set already typed up elsewhere). Both land in the same bank under the same isolation rules; import is a second write path into the same model, not a separate one. See [requirements/qb-question-bank.md](requirements/qb-question-bank.md#bulk-import) for the full column spec, and note explicitly: **docx is not a supported import format.** CSV/Excel are naturally tabular, which is what makes row-level validation and a clean error report possible; a docx is free-flowing text and would need either a rigid dictated format (no real advantage over a spreadsheet) or free-form interpretation (a fundamentally different, AI-assisted feature, not bulk import). Confirmed out of scope for this module.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-ASM-DM-001 | current |
| [requirements/qb-question-bank.md](requirements/qb-question-bank.md) | 3I-ASM-REQ-001 | current |
| [requirements/ex-examinations.md](requirements/ex-examinations.md) | 3I-ASM-REQ-002 | current |
| [ui/README.md](ui/README.md) | 3I-ASM-UI-000 | current — 7 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| Question bank isolation, 404 not 403, admin included | [3I-DEC-006](/3i/decisions/dec-006-question-bank-isolation.md) |
| The course an exam or question is scoped to | `catalogue` |

## Delivery

Phase 5, Assessment (§21.1) — question bank, exams, grading, certificates. This module covers the question-bank/exam half; `certification` covers the certificate half.

## Forward References — Resolved (2026-08-23)

This module was originally scaffolded before `certification` existed:

| Reference | Resolved by |
| :---- | :---- |
| Certificate eligibility reading exam completion | `certification`'s `Certificate` reads `ExamAttempt` from this module |

Same relationship `materials`' `MaterialProgress` has with `certification` — this module exposes the fact (an attempt submitted, its pass/fail state), and the certificate-issuing module reads it.

## Open Against This Module

| Item | Note |
| :---- | :---- |
| Exam-attempt disconnect detection mechanism | The baseline states the outcome (disconnection forfeits the attempt) but not the detection mechanics. Modelled with a heartbeat/autosave + grace-window scheme — see [data-model.md](data-model.md#the-timer-and-disconnect-detection). Reasonable default, not confirmed |
| Negative marks capped at the question's own marks value | Not stated in the baseline. Reasonable default preventing a question from producing a net-negative score contribution larger than it could ever award |

## Change Requests Owed to the Client

None. Nothing in this module amends or reverses the baseline.