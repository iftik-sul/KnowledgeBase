---
project: 3i
module: reporting
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-RPT-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Reporting — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## Report Type Selector

Used on: [Admin Report Generator](screens/admin-report-generator.md), [Admin Scheduled Reports](screens/admin-scheduled-reports.md).

The eleven fixed types (FR-REP-01), grouped loosely by the module cluster they read from (Learning — activity/course performance/enrolment/attendance/exam results/certificates; Commerce — revenue/subscription \& churn/waivers; Community — moderation; Instructors — instructor activity) purely for the admin's own scanability — not a baseline-defined grouping, and not a second-level category system the way `communication`'s notification categories are; just a visual grouping of an otherwise flat list of eleven.

## Export Job Status Badge

Used on: [Admin Report Generator](screens/admin-report-generator.md).

Four states matching `ReportExportJob.status`: **Queued**, **Running**, **Completed** (with a download action), **Failed** (with a retry action). A running job's badge updates live — polling or a push update, not requiring a manual page refresh to see a large export finish — which is the concrete UI expression of FR-REP-04's "does not block the UI": the admin can navigate away and come back rather than needing to watch a spinner.