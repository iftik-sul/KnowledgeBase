---
project: 3i
module: reporting
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-RPT-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Reporting — Validation Rules

Field-level validation shared across two or more reporting screens.

---

## Filter Requirements Per Report Type

On [Admin Report Generator](screens/admin-report-generator.md) and [Admin Scheduled Reports](screens/admin-scheduled-reports.md): every report type requires a date range at minimum — an unbounded "all time" export is not the default for any type, since the platform's own capacity baseline (§20.2, up to 5,000 accounts and 400 hours of video by month 12) means an unbounded learner-activity or attendance export could reasonably be enormous. Type-specific filters (a single course, a single instructor) are optional narrowing, not required.

## Schedule Recipient Validation

On [Admin Scheduled Reports](screens/admin-scheduled-reports.md): each recipient is validated as a well-formed email address only — **not** checked against `identity-and-access`'s Account table, since a valid recipient (FR-REP-03's "nominated recipients") may deliberately be someone with no platform Account at all. At least one recipient is required to save a schedule; an admin cannot schedule a report that goes nowhere.