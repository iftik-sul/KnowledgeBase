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

# Screen: Property Registrations

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described two designs — a monitoring view (Developer Principal / Director) and an operational workspace (Project Registration Officer) — with different KPI sets, table columns, row actions and status lists. Both are **retired**; this is one screen absorbing the load-bearing content of each, including the Registration Insights analytics that only the monitoring view carried.

## Purpose

List the organization's property registrations and provide both the monitoring view and the operational controls to prepare, submit, correct and track them. Any user may do either.

## Layout

```
Top Bar
↓
Registration Summary Cards
↓
Filters & Search
↓
Property Registrations Table
↓
Registration Insights
↓
Pagination
```

**Top Bar**

* Title: Property Registrations
* Subtitle: Register properties and units, and track their regulatory status.
* Search Bar: Search anything...
* Page Actions: **Register New Property**

The page uses the shared **Background + HorizontalBorder** component.

## Sections

### Section 1 — Registration Summary Cards

| KPI | Description | Absorbed from |
| :---- | :---- | :---- |
| Total Registrations | All registrations and drafts, organization-wide | Both *(reconciled — see Notes)* |
| Draft Registrations | Being prepared, not submitted | Registration Officer |
| Submitted | Submitted to RERA | Registration Officer |
| Under Review | Currently under regulatory review | Both *(reconciled)* |
| Information Requested | Awaiting developer response | Both |
| Returned | Returned for correction | Registration Officer |
| Approved | Successfully registered | Both |
| Rejected | Registration rejected | Principal |
| Registered This Month | Completed registrations this month | Both |

Selecting a card filters the table.

**Reconciled 2026-08-15:** the monitoring variant's *Pending Review* and the operational variant's *Under Review* counted the same population under different labels; kept as **Under Review**. The monitoring variant's *Returned for Correction* and the operational variant's *Returned* likewise; kept as **Returned**.

### Section 2 — Filters

* Search Property
* Project Filter
* Property Type Filter
* Registration Status Filter
* Date Range Filter
* Reset Filters

**Removed 2026-08-15:** the operational variant's **Assigned Officer Filter** *(marked "if applicable" in the source)* — per-user scoping, retired with the access model, same as on [projects.md](projects.md).

### Section 3 — Property Registrations Table

| Column | Description |
| :---- | :---- |
| Registration No. | Unique registration reference |
| Property ID | Internal property identifier |
| Property Name / Unit | Registered property or unit |
| Project | Parent development project |
| Property Type | Apartment, Villa, Commercial, etc. |
| Submitted Date | Registration submission date |
| Current Status | Registration status |
| Last Updated | Latest activity |
| Action | Available actions |

**Absorbed 2026-08-15:** the union of both variants' columns. *Property ID* appeared only in the monitoring view; both variants' remaining columns were the same set under slightly different names (*Project Name* / *Project*, *Property Name / Unit* in both).

### Row Actions

Available actions depend on **registration status**, not on who is looking.

| Status | Actions |
| :---- | :---- |
| Draft | Continue Registration · Edit · Delete |
| Submitted / Under Review | View Details |
| Information Requested / Returned | Respond to Query · Upload Documents · Resubmit |
| Approved | View Registration Certificate · Download Registration Summary |
| Rejected | View Details · View Remarks |

**Reconciled 2026-08-15:** the monitoring variant offered only *View Details* on every row — an access restriction expressed as a row-action list, now retired. Status still governs what is possible for everyone.

### Bulk Actions

* Export Selected
* Download Registration Summary
* Delete Drafts

Previously operational-variant only; now available to every user.

### Section 4 — Registration Insights

**Absorbed 2026-08-15** from the monitoring view, the only variant to carry analytics. Retained in full.

**Registration Performance**

* Approval Rate
* Average Approval Time
* Registrations This Quarter
* Pending Reviews

**Registration Distribution**

* Residential
* Commercial
* Mixed Use
* Industrial

### Registration Status Badges

See [status-badges.md](../status-badges.md#property-registration-status). The two variants' lists were reconciled on 2026-08-15 — see [Notes](#notes).

## Empty State

**Message**

> No property registrations yet. Register a property against an existing project to begin.

**Primary Button** — Register New Property
**Secondary Button** — View Projects

**Reconciled 2026-08-15:** the monitoring variant's empty state offered *View Projects* and *Learn About Property Registration* with no create action; the operational variant offered creation. Both create and navigate actions survive.

## Pagination

Rows per page · Previous · Next · Page Number · Total Records

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

1. No card, column, filter, row action or section on this screen is role-gated. What a user can do to a record depends on the record's status, never on who they are.
2. Summary card figures must match the table's own filtered counts exactly.
3. Status vocabulary comes from [status-badges.md](../status-badges.md#property-registration-status) and is not redefined here.

## User Flow

```
Dashboard
↓
Property Registrations
├─ Register New Property → property registration flow
├─ Summary Card → filtered table
├─ Row → Property Registration Details
└─ Registration Insights → Reports
```

## Next Screen

**[Property Registration Details](property-registration-details.md)** — the single-registration view, covering property information, linked development project, registration timeline, submitted documents, RERA review history, comments and queries, approval status and audit trail.

## Notes

* **This absorbs, rather than references, both retired variants.** Their KPI sets, filters, columns, status-driven row actions, bulk actions and analytics are now one screen.

* **Reconciliation — the status lists differed by one state.** [status-badges.md](../status-badges.md#property-registration-status) recorded the monitoring variant with 6 states (Draft, Submitted, Under Review, Information Requested, Approved, Rejected) and the operational variant with 7 (adding **Returned**). Unlike the project-status conflict on [projects.md](projects.md), this one *is* a clean subset: resolved to the **7-state union**, keeping Returned. `status-badges.md` is updated to record the resolution.

* **Reconciliation — "Total Registrations" vs "Total Properties."** The monitoring variant counted "all property registrations"; the operational variant counted "all registered and draft properties" under the name *Total Properties*. Same population once drafts are included in both. Kept as **Total Registrations**, since the screen lists registrations rather than properties, and a property can carry more than one registration over its life.

* **What was dropped, and why.** Only the Assigned Officer filter (per-user scoping), the duplicate *Pending Review* / *Returned for Correction* labels, and the view-only row-action list. Nothing representing distinct work was discarded — the monitoring variant's Registration Insights, its Property ID column and its Rejected KPI are all carried forward.
