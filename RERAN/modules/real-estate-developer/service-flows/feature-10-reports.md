---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/reports.md"
tags:
  - real-estate-developer
  - shared-feature
  - reports
---

# Feature #10 – Reports

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

**Reports** generates, schedules, saves, and downloads reports across every function the module performs, at both executive and operational grain — the union of what were four entirely separate, near-non-overlapping report catalogues.

## 2. Purpose

Let any developer user generate any report on any subject, at any grain, rather than being limited to whichever catalogue a prior role-based design happened to expose.

## 3. Description

This was the most structurally divergent screen in the module to rebuild: each of the four prior role-based designs had its own **entire** report catalogue, with the executive catalogue (Risk Summary, KPI Dashboard) and the escrow catalogue (Escrow Balance Report, Fund Release reports) sharing almost nothing. Executive and operational reports on the same subject — e.g. *Project Progress* (portfolio-level) and *Project Registration Status* (per-application) — are kept as separate reports, not collapsed into one, since collapsing would have lost one of them. No report was removed from any catalogue in the merge; only per-role scoping of catalogues, saved reports, and workload reporting was dropped.

## 4. Used By

Not tied to any single numbered service — spans every domain workspace and the Applications feature.

## 5. Prerequisites

* User is logged into a registered developer company account.

## 6. Required Information

Report filters: date range, project, property, application type, status, financial institution, buyer, category, output format.

## 7. Required Documents

None — reports are generated from existing data, not document uploads.

## 8. Service Fee

No fee.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the developer's four Group B roles** — every report is generatable by every user, following the 2026-08-15 merge of four separate catalogues into one.

## 11. Expected Processing Time

Not given a single sourced figure — generation time presumably varies by report complexity and data volume; not addressed in source.

## 12. Processing Workflow

Dashboard
↓
Open Reports
↓
Select Category → Report → Configure Filters, **or** select a Template, **or** open a Saved Report
↓
Generate Report *(or Schedule Report for recurring generation)*
↓
Recent Generated Reports (Processing → Completed / Failed / Expired)
↓
Download

## 13. Application Status Flow

Generated report status: Processing → Completed / Failed / Expired — the one status vocabulary on this screen that was already identical across all four prior variants, with no conflict to reconcile.

## 14. Possible Outcomes

* Report Generated and Available for Download
* Report Scheduled for Recurring Generation
* Report Generation Failed

## 15. Output

* Generated report file, in the selected output format
* Saved report definition, organization-wide (not per-user)
* Report schedule, with frequency, recipients, and next-run date

## 16. Related Features

* Projects, Property Registrations, Sales & Disclosures, Escrow Management, Fund Release Request, Applications, Documents — every report subject area corresponds to one of these features' own data.
* Dashboard *(Portfolio Insights, Registration Insights, Escrow Analytics, and Sales Analytics all link out to the full report set here)*

## 17. UI Screens

* Reports

## 18. API Requirements

* Retrieve Report Categories / Templates / Saved Reports
* Generate Report / Schedule Report / Export Report / Export Dashboard
* Retrieve Recent Generated Reports
* Retrieve Executive Insights, Operational Insights
* Send Notifications *(on scheduled report completion)*
* Create Audit Log

## 19. Database Entities

* Developer Company, User
* Report Definition, Report Category, Report Template
* Generated Report, Report Schedule
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can generate any report from any category.
* Executive-grain and operational-grain reports on the same subject remain available as distinct reports.
* Saved reports and schedules are organization-wide, visible to every user, not per-user.
* Report figures match their source features exactly — this feature computes nothing independently.
* All generation, scheduling, and download activity is recorded in the audit log.

## 21. Business Rules

1. Any of the developer's four Group B roles may generate, schedule, save, or download any report — no catalogue is role-restricted.
2. Executive and operational reports on the same subject are distinct reports, not duplicates — neither is dropped in favor of the other.
3. Saved reports and schedules are organization-wide.
4. Report figures must match their source features exactly; no independent computation.
5. All report activity is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. Expected generation time is not sourced — needs client confirmation if an SLA is desired.
2. Same adoption question as Feature #1 — needs client confirmation.
