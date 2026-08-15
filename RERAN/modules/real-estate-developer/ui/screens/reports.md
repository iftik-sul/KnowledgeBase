---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-15
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - real-estate-developer
  - ui-spec
---

# Screen: Reports

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described four designs, and was the most divergent screen in the module: **each role had its own entire report catalogue**. The Developer Principal / Director's was executive and organization-wide; the Project Registration Officer's, Sales & Disclosure Officer's and Escrow Liaison's were granular and operational, each covering only its own domain. All four are **retired**; this is one screen carrying the **union of all four catalogues**, organized by subject.
>
> This union is the whole point of the rebuild here. Any approach that picked one catalogue would have deleted three-quarters of the reports available to the organization.

## Purpose

Generate, schedule, save and download reports across every function Group B performs, at both operational and executive grain. Any user may generate any report.

## Layout

```
Top Bar
↓
Report Summary Cards
↓
Report Categories
↓
Report Filters
↓
Saved Reports
↓
Report Templates
↓
Recent Generated Reports
↓
Scheduled Reports
↓
Insights
```

**Top Bar**

* Title: Reports
* Page Actions: **Generate Report** · **Schedule Report** · **Export Report** · **Export Dashboard**

**Absorbed 2026-08-15:** the union of all four variants' page actions. *Export Dashboard* came from the executive variant, *Export Report* from the operational ones; *Generate* and *Schedule* were common.

## Sections

### Section 1 — Report Summary Cards

Reports generated this month, scheduled reports active, saved report definitions, and most-used report — organization-wide.

### Section 2 — Report Categories

**Absorbed 2026-08-15 — the union of all four catalogues.** Reports that existed in only one variant are marked with the grain they were written at, since executive and operational reports on the same subject are genuinely different reports, not duplicates.

**Project Reports**

* Project Progress · Project Completion · Construction Milestones · Development Performance *(executive)*
* Project Registration Status · Project Approval Progress · Returned Projects · Registration Timeline *(operational)*

**Property Reports**

* Property Registrations · Registration Status · Property Inventory · Property Availability *(executive)*
* Property Registration Status · Registration Progress · Approved Properties · Returned Registrations *(operational)*

**Sales & Disclosure Reports**

* Sales Performance · Buyer Statistics · Sales Trends · Disclosure Compliance *(executive)*
* Property Sales Register · Sales Value Analysis · Monthly Sales Summary *(operational)*
* Disclosure Status Report · Submitted Disclosures · Returned Disclosures · Disclosure Approval Timeline
* Buyer Verification Status · Buyer Demographics · Corporate Buyers · Joint Ownership Report · Buyer Identification Report

**Escrow Reports**

* Escrow Balances · Fund Releases · Milestone Progress · Financial Institution Summary *(executive)*
* Escrow Account Summary · Active Escrow Accounts · Escrow Balance Report · Escrow Status Report *(operational)*

**Application & Regulatory Reports**

* Applications · Approval Performance · Processing Time · Compliance Overview *(executive)*
* Submitted Applications · Pending Reviews · Returned Applications · Approval Timeline *(operational)*
* Registration Compliance · Disclosure Compliance Rate · Validation Errors · RERA Query Response Time · Regulatory Performance · Pending Regulatory Actions

**Document Reports**

* Document Verification · Repository Summary *(executive)*
* Missing Documents · Pending Verification · Returned Documents · Expiring Documents *(operational)*

**Financial Reports**

* Revenue · Escrow Funds · Sales Value · Payment Summary *(executive)*
* Property Sales Value · Payment Status Summary · Mortgage Distribution · Sales by Project *(operational)*

**Operational Reports**

* Workload · Due This Week · Outstanding Tasks · Submission History

**Executive Reports**

* Organization Performance · KPI Dashboard · Risk Summary · Executive Summary

> **Reconciliation — "Officer Workload" is renamed "Workload."** Three operational variants each defined an *Officer Workload* report scoped to their own role's queue. With work no longer assigned by role, one report covers organization-wide workload, breakable down by whoever performed the work — attribution, not scope.

### Section 3 — Report Filters

Date range, project, property, application type, status, financial institution, buyer, category and output format. The union of all four variants' filter sets.

### Section 4 — Saved Reports

Saved report definitions, with Run, Edit, Duplicate, Schedule and Delete actions. **Organization-wide, not per user** — a saved report is now visible to everyone. Previously each variant implied its own saved set.

### Section 5 — Report Templates

Predefined templates per category, from all four catalogues.

### Section 6 — Recent Generated Reports

Generated reports with status, generated-by attribution and download links. Status vocabulary — Processing, Completed, Failed, Expired — was **identical across all four variants**, the one legend in this screen with no conflict. See [status-badges.md](../status-badges.md).

### Section 7 — Scheduled Reports

Recurring report schedules with frequency, recipients, next run and Pause/Edit/Delete actions.

**Absorbed 2026-08-15** from the executive variant, the only one to define a Scheduled Reports section — though all four offered a *Schedule Report* action. That gap looks like an omission in the operational variants rather than a deliberate restriction: they could schedule a report but had nowhere to see or manage the schedule.

### Section 8 — Insights

**Absorbed 2026-08-15** by combining the executive variant's *Executive Insights* with the three operational variants' *Pending Operational Insights*. Both are kept and clearly separated — they answer different questions at different grain:

* **Executive Insights** — organization performance, risk summary, trend analysis.
* **Operational Insights** — outstanding tasks, items due this week, validation error patterns, RERA response times.

## Empty State

> No reports generated yet. Generate a report from any category above, or start from a template.

**Primary Button** — Generate Report

## Reused Components

See [components.md](../components.md). **Reconciled naming:** the executive variant's Reused Components list called these "Analytics Cards" while this screen's operational variants called them "Analytics Widgets"; [components.md](../components.md) flagged the divergence. Resolved to **Analytics Cards**, the name used by every other screen in the module.

## Validation

1. No category, report, filter, template or action on this screen is role-gated. Every report is generatable by every user.
2. Saved reports and schedules are organization-wide, not per user.
3. Report figures must match their source screens exactly; this screen computes nothing independently.

## User Flow

```
Dashboard
↓
Reports
├─ Category → report configuration → Generate
├─ Template → prefilled configuration
├─ Saved Report → Run / Edit / Schedule
└─ Recent Generated → Download
```

## Notes

* **This absorbs, rather than references, all four retired variants.**

* **This screen was the strongest evidence that the variants were structural, not visibility.** Four roles meant four separate report catalogues with almost no overlap — the executive catalogue's *Risk Summary* and *KPI Dashboard* existed nowhere else, and the escrow catalogue's *Escrow Balance Report* and *Fund Release* reports existed nowhere else either. This is why the earlier pass flagged the merge for a client decision rather than making it.

* **Executive and operational reports on the same subject are kept as separate reports**, marked by grain. *Project Progress* (executive, portfolio-level) and *Project Registration Status* (operational, per-application) are not the same report under two names, and collapsing them would have lost one of them.

* **Reconciliation — "Officer Workload" → "Workload."** Recorded in Section 2.

* **Reconciliation — component naming.** "Analytics Cards" vs "Analytics Widgets", resolved; `components.md` updated.

* **What was dropped, and why.** Only the per-role scoping of catalogues, saved reports and workload reporting. **No report was removed from any catalogue.**
