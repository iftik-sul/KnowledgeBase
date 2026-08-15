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

# Screen: Applications

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described four designs: an organization-wide monitoring view (Developer Principal / Director) and three near-identical operational workspaces (Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison), each scoped to its own application types. All four are **retired**. This is one screen covering every application type, absorbing the monitoring view's analytics and the operational views' work controls.

## Purpose

List every regulatory application the organization has submitted to RERA — registration, sales disclosure, escrow, licensing and title-deed alike — with the controls to continue drafts, respond to queries, correct returns and resubmit, plus the analytics to monitor approval performance. Any user may do any of it.

## Layout

```
Top Bar
↓
Application Summary Cards
↓
Filters & Search
↓
Applications Table
↓
Pending Actions
↓
Application Analytics
↓
Recent Regulatory Activities
↓
Pagination
```

**Top Bar**

* Title: Applications
* Subtitle: Track, manage and respond to every regulatory application your organization has submitted to RERA.
* Search Bar: Search anything...
* Page Actions: **Submit New Application**

## Sections

### Section 1 — Application Summary Cards

| KPI | Description | Absorbed from |
| :---- | :---- | :---- |
| Total Applications | All applications, every type, organization-wide | All four *(reconciled — see Notes)* |
| Draft Applications | Not yet submitted | All four |
| Submitted | Successfully submitted, awaiting review | All four |
| Under Review | Currently being processed | All four |
| Information Requested | Awaiting developer response | All four *(reconciled — label)* |
| Returned | Returned for correction | The three operational variants |
| Approved | Successfully approved | All four |
| Rejected | Rejected applications | Principal |
| Due This Week | Applications requiring action this week | The three operational variants |
| Average Approval Time | Average processing duration | Principal |

Selecting a card filters the table.

### Section 2 — Filters

* Search Application
* **Application Type Filter** — registration · property · sales disclosure · escrow · licensing · title deed
* Project Filter
* Property Filter
* Status Filter
* Assigned RERA Unit Filter
* Date Range Filter
* Reset Filters

**Absorbed 2026-08-15:** the union of all four variants' filters. The **Application Type Filter** now does the work that the three operational variants did by having three separate screens — a user narrowing to escrow applications selects the type rather than switching screens.

### Section 3 — Applications Table

| Column | Description |
| :---- | :---- |
| Application ID | Unique application reference |
| Application Type | Service submitted |
| Related Project | Associated development project |
| Related Property | Associated property or unit *(where applicable)* |
| Buyer | Buyer name *(sales disclosure applications only)* |
| Submitted By | Employee who submitted, and their role at the time |
| Submitted Date | Date submitted |
| Current Status | Processing stage |
| Assigned RERA Unit | Reviewing department |
| Last Updated | Latest activity |
| Action | Available actions |

**Absorbed 2026-08-15:** the union of all four variants' columns. Domain-specific columns that appeared in only one operational variant — *Buyer* (sales disclosure), *Related Property* (registration) — are retained and render only where meaningful for that application type, rather than forcing three separate tables.

**Submitted By** was the Principal's column alone. Kept and extended: it now records the role held at the time of submission, matching the audit-trail model ([navigation.md](../../navigation.md#audit-trail-principle)). This is the screen where role-as-attribution is most visible, and it is the one place role still legitimately appears.

### Row Actions

Available actions depend on **application status**, not on who is looking.

| Status | Actions |
| :---- | :---- |
| Draft | Continue · Edit · Delete |
| Submitted / Under Review | View Details |
| Information Requested | Respond · Upload Documents · Resubmit |
| Returned | Edit · Correct Issues · Resubmit |
| Approved | View Details · Download Approval |
| Rejected | View Details |

**Reconciled 2026-08-15:** the monitoring variant offered only *View Details* on every row. Retired as an access restriction. The three operational variants defined the identical status-to-action mapping above, so no reconciliation was needed between them.

### Section 4 — Pending Actions

A prioritized table of applications where something is waiting on a developer user.

| Application | Required Action | Due Date | Priority | Action |
| :---: | :---: | :---: | :---: | :---: |

Applications with **Information Requested** or **Returned** status appear at the top. Items nearing their deadline sort first.

**Absorbed 2026-08-15** from the three operational variants, which each defined this section identically over their own application subset. Now one table across all types.

### Section 5 — Application Analytics

**Absorbed 2026-08-15** from the monitoring variant, the only one to carry analytics. Retained in full — approval rates, average processing duration by application type, volume by status and by RERA unit.

> **This is the section the merge most easily could have lost.** The three operational variants explicitly framed themselves as emphasizing "actionable work rather than analytics." Picking any of them as the base would have discarded this section entirely.

### Section 6 — Recent Regulatory Activities

Activity feed of submissions, RERA decisions, information requests and resubmissions across the organization, most recent first. Present in all four variants with the same definition.

## Empty State

**Message**

> No applications yet. Submit an application to RERA to begin, or continue a draft.

**Primary Button** — Submit New Application

**Reconciled 2026-08-15:** the four variants each had an empty state addressed to their own scope ("No escrow applications yet", "No sales disclosure applications yet", and so on). One organization-wide message replaces them, since the screen is no longer scoped to a domain or a role.

## Pagination

Rows per page · Previous · Next · Page Number · Total Records

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

1. No card, column, filter, row action or section on this screen is role-gated. What a user can do depends on the application's status, never on who they are.
2. Summary card figures must match the table's own filtered counts exactly.
3. Domain-specific columns render only for application types where they carry a value; they are never role-conditional.
4. Status vocabulary comes from [status-badges.md](../status-badges.md) and is not redefined here.

## User Flow

```
Dashboard
↓
Applications
├─ Submit New Application → the relevant service flow
├─ Summary Card / Type Filter → filtered table
├─ Row → Application Details
├─ Pending Actions row → the response flow
└─ Application Analytics → Reports
```

## Notes

* **This absorbs, rather than references, all four retired variants.**

* **The three operational variants were the same design three times.** Project Registration Officer, Sales & Disclosure Officer and Escrow Liaison each defined the same KPI set (including the same *Due This Week* card), the same six-status row-action mapping, the same Pending Actions table and the same activity feed — differing only in which application types they listed and one or two domain columns. Merging them cost nothing; what were three screens is now one screen plus an **Application Type Filter**.

* **Reconciliation — "Additional Information Requested" vs "Information Requested."** The monitoring variant used the longer label; all three operational variants used the shorter. Same status. Kept as **Information Requested**, matching [status-badges.md](../status-badges.md) and the service flows.

* **Reconciliation — "Total Applications" was scoped four ways.** The monitoring variant counted all submitted applications organization-wide; each operational variant counted only its own domain ("all escrow-related applications", "all sales disclosure applications"). Resolved to organization-wide across every type, consistent with the removal of domain and per-user scoping.

* **Reconciliation — the monitoring variant had no *Returned* or *Due This Week* card; the operational variants had no *Rejected* or *Average Approval Time*.** All four are kept. Each was absent from a variant because that variant either could not act on the state or did not report on it — neither is a reason to drop a real metric.

* **What was dropped, and why.** Only the view-only row-action list, the per-domain scoping of the KPI and empty-state text, and the operational variants' Notes paragraphs naming themselves "the primary operational application management screen for the {role}". Nothing representing distinct work was discarded — the monitoring variant's Application Analytics, Rejected and Average Approval Time survive, as do the operational variants' Pending Actions, Due This Week, Returned and full row-action mapping.
