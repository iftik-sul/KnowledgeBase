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

**No Storage Usage Bar exists in this module** — [3I-DEC-029](/3i/decisions/dec-029-no-instructor-storage-quota.md) removed the per-instructor storage quota this component would have displayed.