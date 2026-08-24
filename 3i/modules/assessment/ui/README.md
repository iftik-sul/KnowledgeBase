---
project: 3i
module: assessment
type: ui-spec
status: current
updated: 2026-08-24
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
| **Mobile (Flutter)** | Not a role — a platform column marking which screens are in scope for the native app. See [mobile-scope.md](/3i/mobile-scope.md) |

---

## Matrix

| Screen | Member | Instructor | Admin | Mobile |
| :---- | :---: | :---: | :---: | :---: |
| [Question bank manage](screens/question-bank-manage.md) | | ● | | |
| [Admin question bank](screens/admin-question-bank.md) | | | ● | |
| [Bulk import questions](screens/bulk-import-questions.md) | | ● | ● | |
| [Exam configure](screens/exam-configure.md) | | ● | | |
| [Take exam](screens/take-exam.md) | ● | | | ● |
| [Exam result](screens/exam-result.md) | ● | | | ● |
| [Grade written answers](screens/grade-written-answers.md) | | ● | | |

Seven screens, two in scope for mobile — see [mobile-scope.md](/3i/mobile-scope.md#3-decisions-worth-recording) for why Take Exam is included despite the timed/free-text tradeoffs.

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
