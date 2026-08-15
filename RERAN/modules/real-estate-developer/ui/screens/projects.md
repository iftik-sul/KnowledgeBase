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

# Screen: Projects

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described two structurally different designs: an executive portfolio view (Developer Principal / Director) and an operational workspace (Project Registration Officer), with different KPI sets, filters, table columns, row actions and status vocabularies. Both are **retired**; this is one screen absorbing the load-bearing content of each. The monitoring content that only the portfolio view carried is preserved as Portfolio Insights rather than discarded.

## Purpose

List the organization's development projects and provide both the monitoring view of the portfolio and the operational controls to create, edit, submit and correct project registrations. Any user may do either.

## Layout

```
Top Bar
↓
Project Summary Cards
↓
Filters & Search
↓
Projects Table
↓
Portfolio Insights
↓
Pagination
```

**Top Bar**

* Title: Projects
* Subtitle: Register, track and monitor the organization's development projects.
* Search Bar: Search anything...
* Page Actions: **Register New Project**

The page uses the shared **Background + HorizontalBorder** component.

## Sections

### Section 1 — Project Summary Cards

| KPI | Description | Absorbed from |
| :---- | :---- | :---- |
| Total Projects | All projects, organization-wide | Both *(reconciled — see Notes)* |
| Draft Projects | Still being prepared, not submitted | Registration Officer |
| Submitted Projects | Submitted to RERA | Registration Officer |
| Under Review | Currently under regulatory review | Both *(reconciled)* |
| Information Requested | Waiting for additional information | Registration Officer |
| Returned Projects | Returned for correction | Registration Officer |
| Approved Projects | Successfully approved | Both |
| Active Projects | Currently under development | Principal |
| Suspended Projects | On hold or suspended | Principal |
| Completed Projects | Development completed | Both |

Selecting a card filters the table.

### Section 2 — Filters

* Search Project
* Project Status Filter
* Development Type Filter
* Location Filter
* Registration Stage Filter
* Date Range Filter
* Reset Filters

**Removed 2026-08-15:** the Registration Officer variant's **Assigned Officer Filter** *(marked "if applicable" even in the source)*. It filtered by which officer a project was assigned to — a scoping concept that does not survive unified access, where no project belongs to one user's view. The **Uploaded/Created By** attribution remains visible on the record itself and in the audit trail; it is simply no longer a filter dimension for narrowing "my" work.

### Section 3 — Projects Table

| Column | Description |
| :---- | :---- |
| Project ID | Unique project reference |
| Project Name | Development project name |
| Development Type | Residential, Commercial, Mixed Use, etc. |
| Location | State / City |
| Current Status | Registration status |
| Development Stage | Planning / Construction / Completed |
| Progress | Percentage completion |
| Last Updated | Latest activity |
| Action | Available actions |

**Absorbed 2026-08-15:** the union of both variants' columns. *Development Stage* and *Progress* came only from the portfolio view; *Development Type* only from the operational view. Both are real project attributes and both are kept. The Registration Officer variant's **Assigned To** column is dropped for the same reason as the Assigned Officer filter.

The table supports sorting by Project Name, Status, Progress and Last Updated.

### Row Actions

Available actions depend on **project status**, not on who is looking.

| Status | Actions |
| :---- | :---- |
| Draft | Continue Registration · Edit · Delete |
| Submitted / Under Review | View Details |
| Information Requested / Returned | Respond to Query · Upload Documents · Resubmit |
| Approved | View Details · Register Properties |
| Suspended / Completed | View Details |

**Reconciled 2026-08-15:** the portfolio view offered only *View Details* on every row. That was an access restriction expressed as a row-action list, not a lifecycle rule, so it is retired — the status-driven actions above now apply for every user. Status still governs what is possible: a submitted project cannot be edited by anyone.

### Bulk Actions

* Export Selected
* Download Summary
* Submit Multiple Drafts *(if supported)*
* Delete Drafts

Previously available only in the Registration Officer variant; now available to every user, since bulk operations were gated by role rather than by record state.

### Section 4 — Portfolio Insights

**Absorbed 2026-08-15** from the executive portfolio view, which was the only variant to carry monitoring analytics. Retained in full — it is real distinct content, not a role's framing of shared content.

* Project distribution by development stage and by type.
* Progress summary across active projects.
* Organizational performance over the current quarter.

Links to [reports.md](reports.md) for the full report set.

### Project Status Badges

See [status-badges.md](../status-badges.md#project-status). **The two variants' conflicting status lists were reconciled on 2026-08-15** — see [Notes](#notes).

## Empty State

**Message**

> No development projects yet. Register a project to begin, or learn how project registration works.

**Primary Button** — Register New Project
**Secondary Button** — Learn About Project Registration

**Reconciled 2026-08-15:** the portfolio view's empty state offered only *Learn About Project Registration*, with no create action; the operational view's read "You haven't created any development projects yet" and offered creation. The organization-level phrasing plus both actions is what survives — the screen is no longer addressed to a role, and "you haven't created any" is wrong on a shared, organization-wide list.

## Pagination

Rows per page · Previous · Next · Page Number · Total Results

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

1. No card, column, filter, row action or section on this screen is role-gated. What a user can do to a record depends on the record's status, never on who they are.
2. Summary card figures must match the table's own filtered counts exactly.
3. Status vocabulary comes from [status-badges.md](../status-badges.md#project-status) and is not redefined here.

## User Flow

```
Dashboard
↓
Projects
├─ Register New Project → project registration flow
├─ Summary Card → filtered table
├─ Row → Project Details
└─ Portfolio Insights → Reports
```

## Notes

* **This absorbs, rather than references, both retired variants.** The executive portfolio view and the operational workspace are gone as separate designs; their load-bearing content — KPI sets, filters, columns, status-driven row actions, bulk actions and portfolio analytics — is now one screen.

* **Reconciliation — the two status vocabularies genuinely conflicted and are now merged.** [status-badges.md](../status-badges.md#project-status) recorded the conflict as unresolvable-by-subsetting: the Principal's list had *Pending Review* and *Suspended*, which the Registration Officer's lacked entirely; the Registration Officer's had *Submitted*, *Under Review*, *Information Requested* and *Returned*, which the Principal's lacked. Resolved as follows, since one screen cannot carry two vocabularies:
  * **Union of both**, giving nine states: Draft, Submitted, Under Review, Information Requested, Returned, Approved, Rejected, Suspended, Completed.
  * **"Pending Review" is dropped as a duplicate label**, not as a state — it and "Under Review" describe the same regulatory position, and "Under Review" is the label used everywhere else in the module and in the service flows.
  * **"Suspended" is kept.** It was the harder case: it describes a project put on hold, a state genuinely unrepresentable in the operational vocabulary. Dropping it because only one variant listed it would have lost a real state.
  * `status-badges.md` is updated to record this resolution in place of the flagged conflict.

* **Reconciliation — "Total Projects" meant two things.** The portfolio view counted "all registered projects"; the operational view counted "all *assigned* projects." Resolved to organization-wide, consistent with the removal of per-user assignment scoping across the module.

* **What was dropped, and why.** Only the Assigned Officer filter and Assigned To column (per-user scoping, retired with the access model), the "Pending Review" duplicate label, the view-only row-action list (an access restriction in disguise), and the portfolio view's Notes paragraph stating that "all project creation, document submission and registration activities are handled by the Project Registration Officer" — a permission claim that is no longer true. Nothing representing distinct work was discarded.
