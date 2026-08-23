---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Assessment — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## Question Card

Used on: [Question Bank Manage](screens/question-bank-manage.md), [Admin Question Bank](screens/admin-question-bank.md), [Exam Configure](screens/exam-configure.md) (question picker).

Shows question text (truncated), type badge, marks, difficulty. On the two bank-management screens, adds edit/delete/copy affordances as appropriate to context (copy only appears when browsing the *admin* bank from an instructor's view — see [Question Bank Manage](screens/question-bank-manage.md)). On the exam-assembly picker, adds a checkbox and a per-exam marks-override field.

## Attempt Timer

Used on: [Take Exam](screens/take-exam.md).

A visible countdown to the attempt's `expiresAt`, computed from the **server's** clock and duration, never the client's — a learner's device clock being wrong, or being deliberately paused, must not extend or shorten the real deadline. Reaching zero triggers auto-submission of whatever is currently saved (FR-EX-04); the learner sees this happen, not a silent redirect.

## Reveal Gate

Used on: [Exam Result](screens/exam-result.md).

Shows or withholds correct answers and explanations based on the exam's [reveal-answers policy](/3i/modules/assessment/data-model.md#reveal-answers-policy-fr-ex-06) and the learner's own attempt history — under `standard`, this means checking whether *this* attempt passed or whether *all* attempts are now exhausted, not just whether an answer key technically exists. When withheld, the component shows the learner's score and pass/fail state without revealing which specific answers were wrong, since partial disclosure (score visible, answers not) is the whole point of the gate.