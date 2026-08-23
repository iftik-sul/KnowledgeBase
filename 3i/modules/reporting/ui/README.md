---
project: 3i
module: reporting
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-RPT-UI-000
derived_from:
  - requirements/rep-reports-and-exports.md
tags:
  - ui
  - matrix
---

# Reporting — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Admin** | The only role with any access to this module, throughout — see [README.md](../README.md#admin-only-not-a-member-facing-module) |

---

## Matrix

| Screen | Admin |
| :---- | :---: |
| [Admin report generator](screens/admin-report-generator.md) | ● |
| [Admin scheduled reports](screens/admin-scheduled-reports.md) | ● |

Two screens.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | Report Type Selector, Export Job Status Badge |
| [validation-rules.md](validation-rules.md) | Filter requirements per report type, schedule recipient validation |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| None. | |