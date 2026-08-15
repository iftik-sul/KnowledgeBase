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

# Screen: Sales & Disclosures

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described two designs — an executive monitoring screen (Developer Principal / Director) and an operational workspace (Sales & Disclosure Officer) — with different KPI sets, table columns, row actions and analytics. Both are **retired**; this is one screen absorbing the load-bearing content of each, including the Sales Analytics that only the monitoring view carried.

## Purpose

List the organization's recorded property sales alongside their regulatory disclosure status, and provide both the monitoring view of sales performance and disclosure compliance, and the operational controls to record sales, prepare disclosures, upload buyer documents and submit to RERA. Any user may do either.

## Layout

```
Top Bar
↓
Sales Summary Cards
↓
Filters & Search
↓
Sales & Disclosures Table
↓
Sales Analytics
↓
Pagination
```

**Top Bar**

* Title: Sales & Disclosures
* Subtitle: Record property sales and file the disclosures RERA requires for each.
* Search Bar: Search anything...
* Page Actions: **Record Property Sale** · **Create Sales Disclosure**

The page uses the shared **Background + HorizontalBorder** component.

## Sections

### Section 1 — Sales Summary Cards

| KPI | Description | Absorbed from |
| :---- | :---- | :---- |
| Total Sales | All recorded property sales, organization-wide | Both |
| Draft Sales | Sales not yet finalized | Sales & Disclosure Officer |
| Active Listings | Properties currently available for sale | Principal |
| Sales Awaiting Disclosure | Sales requiring disclosure preparation | Both *(reconciled — see Notes)* |
| Draft Disclosures | Disclosures being prepared | Sales & Disclosure Officer |
| Submitted Disclosures | Submitted to RERA | Both |
| Under Review | Currently under regulatory review | Sales & Disclosure Officer |
| Returned Disclosures | Returned for correction | Both |
| Approved Disclosures | Successfully approved | Both |
| Total Sales Value | Combined value of completed sales | Principal |
| This Month's Sales | Sales completed during the current month | Principal |

Selecting a card filters the table.

### Section 2 — Filters

* Search Property / Buyer
* Project Filter
* Property Type Filter
* Sales Status Filter
* Disclosure Status Filter
* Date Range Filter
* Reset Filters

**Removed 2026-08-15:** the operational variant's **Assigned Officer Filter** *(marked "if applicable" in the source)* — per-user scoping, retired with the access model, consistent with [projects.md](projects.md) and [property-registrations.md](property-registrations.md).

### Section 3 — Sales & Disclosures Table

| Column | Description |
| :---- | :---- |
| Sale Reference | Unique sale reference |
| Property | Property name / unit |
| Project | Development project |
| Buyer | Buyer name |
| Sale Date | Date of transaction |
| Sale Value | Transaction value |
| Current Status | Overall sale status |
| Current Stage | Operational stage |
| Disclosure Status | Regulatory disclosure status |
| Last Updated | Latest activity |
| Action | Available actions |

**Absorbed 2026-08-15:** the union of both variants' columns. *Last Updated* and *Current Stage* came only from the operational view; *Current Status* only from the monitoring view. **Two distinct statuses are tracked per sale** — the sale's own lifecycle and the disclosure's lifecycle — and the source keeps them separate, so both columns are retained rather than collapsed. See [status-badges.md](../status-badges.md#sales--disclosure-status).

### Row Actions

Available actions depend on **sale and disclosure status**, not on who is looking.

| Status | Actions |
| :---- | :---- |
| Draft Sale | Continue Sale Entry · Edit · Delete |
| Disclosure Pending | Create Disclosure · Upload Buyer Documents |
| Draft Disclosure | Continue Disclosure · Edit · Validate · Submit to RERA |
| Submitted / Under Review | View Details |
| Information Requested / Returned | Respond to Query · Upload Additional Documents · Resubmit |
| Approved | View Details · Download Disclosure Record |

**Reconciled 2026-08-15:** the monitoring variant offered only *View Details* on every row — an access restriction expressed as a row-action list, now retired. Status still governs what is possible for everyone.

### Bulk Actions

* Export Selected
* Download Summary

Previously operational-variant only; now available to every user.

### Section 4 — Sales Analytics

**Absorbed 2026-08-15** from the monitoring view, the only variant to carry analytics. Retained in full.

**Sales Performance**

* Sales This Month
* Sales This Quarter
* Average Sale Value
* Total Revenue

**Disclosure Compliance**

* Compliance Rate
* Pending Disclosures
* Average Approval Time
* Returned Cases

### Status Badges

Two separate vocabularies apply on this screen — **Sales Status** and **Disclosure Status**. See [status-badges.md](../status-badges.md#sales--disclosure-status); this screen defines neither.

## Empty State

**Message**

> No property sales recorded yet. Record a sale to begin, then file its disclosure with RERA.

**Primary Button** — Record Property Sale
**Secondary Button** — View Property Registrations

**Reconciled 2026-08-15:** the monitoring variant's empty state offered only navigation (*View Projects*, *View Property Registrations*); the operational variant offered creation. Both survive, with the create action primary.

## Pagination

Rows per page · Previous · Next · Page Number · Total Records

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

1. No card, column, filter, row action or section on this screen is role-gated. What a user can do to a record depends on the record's status, never on who they are.
2. Summary card figures must match the table's own filtered counts exactly.
3. The sale's status and the disclosure's status are separate values and must not be conflated in filters, badges or counts.
4. Status vocabulary comes from [status-badges.md](../status-badges.md#sales--disclosure-status) and is not redefined here.

## User Flow

```
Dashboard
↓
Sales & Disclosures
├─ Record Property Sale → sale entry flow
├─ Create Sales Disclosure → disclosure flow
├─ Summary Card → filtered table
├─ Row → Sales & Disclosure Details
└─ Sales Analytics → Reports
```

## Notes

* **This absorbs, rather than references, both retired variants.** Their KPI sets, filters, columns, status-driven row actions and analytics are now one screen.

* **Reconciliation — "Pending Disclosures" vs "Sales Awaiting Disclosure."** The monitoring variant's card was named *Pending Disclosures* and defined as "awaiting disclosure submission"; the operational variant's was *Sales Awaiting Disclosure*, "sales requiring disclosure preparation." Same population — a sale recorded with no disclosure filed. Kept as **Sales Awaiting Disclosure**, the more precise name, since "pending" is ambiguous between "not yet started" and "submitted, awaiting RERA." The monitoring variant's *Pending Disclosures* label survives inside Section 4's Disclosure Compliance card, where it is a performance metric rather than a work queue.

* **The two-status design is preserved deliberately.** A sale and its disclosure have separate lifecycles, and the source documents them separately. Merging the screens did not merge the statuses; both columns, both filters and both badge vocabularies remain.

* **What was dropped, and why.** Only the Assigned Officer filter (per-user scoping), the view-only row-action list, and the monitoring variant's Notes paragraph stating the screen provides visibility "without allowing operational edits" and that "creation and submission of sales disclosures remain the responsibility of the Sales & Disclosure Officer" — both permission claims that are no longer true. Nothing representing distinct work was discarded; the monitoring variant's Total Sales Value, This Month's Sales, Active Listings and full Sales Analytics section are all carried forward.
