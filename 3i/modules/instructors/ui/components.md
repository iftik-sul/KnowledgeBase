---
project: 3i
module: instructors
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-INS-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Instructors — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## WWCC Status Badge

Used on: [Admin Instructor Management](screens/admin-instructor-management.md), [WWCC Renewal](screens/wwcc-renewal.md).

Three states: **Current** (expiry more than 60 days out), **Expiring Soon** (within the 60-day alert window, FR-INST-03 — matches the moment the admin alert fires), **Expired** (FR-INST-04's teaching block is active). Each state is visually distinct, not a single badge with different text colours, since this is the same field the scheduling guard and course-creation block both read — an admin or instructor glancing at it should immediately know which enforcement regime currently applies.

## Storage Usage Bar

Used on: [Admin Instructor Management](screens/admin-instructor-management.md).

A simple used-versus-quota bar (FR-INST-05), computed live from `materials` rather than a stored running total — see [data-model.md](/3i/modules/instructors/data-model.md#instructorprofile). Shows the actual byte figures, not just a percentage, since "73%" means little without knowing the quota it's 73% of — same "show the formula, not just the number" principle already used for the seat-linked device allowance and the offline-item cap elsewhere in this project.