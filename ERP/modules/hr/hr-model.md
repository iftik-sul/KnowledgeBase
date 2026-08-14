---
project: ERP
module: hr
type: data-model
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# HR Model

- Employee Master with `pay_type`: Monthly Salary or Daily Wage.
- Daily Attendance.
- Leave Management (sick/casual).
- Payroll: single global tax formula, with a per-employee toggle to apply it.
- Global "Work Hours per Day" setting, used to convert logged hours into day-equivalents.
- Shift Master with per-employee assignment.

## Out of scope

Recruitment, Onboarding, Performance Management, Training.
