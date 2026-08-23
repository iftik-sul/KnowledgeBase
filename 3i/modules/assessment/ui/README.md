---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-ASM-UI-000
derived_from:
  - requirements/qb-question-bank.md
  - requirements/ex-examinations.md
tags:
  - ui
  - matrix
---

# Assessment — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Member** | The renamed Account holder role — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md), taking an exam on behalf of an enrolled profile |
| **Instructor** | |
| **Admin** | |

---

## Matrix

| Screen | Member | Instructor | Admin |
| :---- | :---: | :---: | :---: |
| [Question bank manage](screens/question-bank-manage.md) | | ● | |
| [Admin question bank](screens/admin-question-bank.md) | | | ● |
| [Bulk import questions](screens/bulk-import-questions.md) | | ● | ● |
| [Exam configure](screens/exam-configure.md) | | ● | |
| [Take exam](screens/take-exam.md) | ● | | |
| [Exam result](screens/exam-result.md) | ● | | |
| [Grade written answers](screens/grade-written-answers.md) | | ● | |

Seven screens.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | Question Card, Attempt Timer, Reveal Gate |
| [validation-rules.md](validation-rules.md) | CSV import row validation, negative-marks cap, one-final-exam-per-course |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| None. | |