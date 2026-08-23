---
project: 3i
module: reporting
type: requirements
status: current
updated: 2026-08-23
id: 3I-RPT-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - reporting
---

# Reports and Exports

Baseline §18. Five requirements, none amended by decision.

---

## Report Types

| ID | Requirement |
| :---- | :---- |
| **FR-REP-01** | Reports: learner activity, course performance, enrolment, attendance, exam results, certificates issued, revenue (gross), subscription and churn, waivers granted, moderation and reports handled, instructor activity |

Eleven fixed types, full source mapping in [data-model.md](../data-model.md#report-type--source-mapping) — not restated here. Every source module already exists; nothing in this list is blocked.

---

## Export and Delivery

| ID | Requirement |
| :---- | :---- |
| **FR-REP-02** | Export formats: **Excel, CSV, PDF** |
| **FR-REP-03** | **Scheduled reports** delivered by email on a recurring schedule to nominated recipients |

FR-REP-03's "nominated recipients" are plain email addresses, not necessarily platform Accounts — see [data-model.md](../data-model.md#scheduledreport) and [README.md](../README.md#on-demand-exports-and-scheduled-reports-are-different-delivery-paths) for why this bypasses `communication`'s category-preference system entirely rather than trying to force an external recipient through an opt-out model that doesn't apply to them.

---

## Background Processing

| ID | Requirement |
| :---- | :---- |
| **FR-REP-04** | Report generation runs as a **background job**; large exports do not block the UI |

Every export — on-demand or scheduled, regardless of report type or expected size — runs through the same `ReportExportJob` background-job path (see [data-model.md](../data-model.md#reportexportjob)). There is no separate "small report, generate synchronously" shortcut; consistency of behaviour matters more here than optimising the common case.

---

## Revenue Reporting

| ID | Requirement |
| :---- | :---- |
| **FR-REP-05** | Revenue reporting is **gross platform revenue, GST separated** |

Reads directly from the GST breakout `commerce` already records on every invoice specifically to satisfy this requirement (FR-BILL-08) — this module doesn't recompute or re-derive GST, it reads what's already stored for exactly this purpose.

---

## Acceptance Criteria

1. A scheduled weekly report arrives by email with the correct attachment format, to every nominated recipient, including one who holds no platform Account.
2. A 50,000-row export completes without timing out the request — the admin's UI remains responsive throughout, showing job status rather than blocking.
3. The revenue report's gross figure and GST breakout match the sum of `commerce`'s own invoice-level GST fields exactly.
4. Every one of the eleven report types produces a non-empty export against seeded test data covering its full source-module reach.
5. Pausing a `ScheduledReport` (setting `active = false`) stops future scheduled runs without deleting the schedule's configuration.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-RPT-DM-001](../data-model.md) |
| GST breakout this module reads | `commerce` (FR-BILL-08) |
| Email delivery infrastructure reused for scheduled reports | `communication` (FR-NOT-07) |