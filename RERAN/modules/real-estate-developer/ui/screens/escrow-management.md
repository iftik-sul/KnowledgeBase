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

# Screen: Escrow Management

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described two designs — an executive oversight screen (Developer Principal / Director) and an operational workspace (Escrow Liaison) — with different KPI sets, filter structures, table columns and row actions. Both are **retired**; this is one screen absorbing the load-bearing content of each, including the Escrow Analytics and Fund Release Overview that only the oversight view carried.

> **The balances on this screen are not a RERA-fee account.** The balance, milestone and fund-release figures here belong to the developer's **project escrow account** — the regulated holding account for sale proceeds, deposits and construction-milestone releases that is the subject matter of Services [#8](../../service-flows/service-08-activate-escrow-account.md)–[#12](../../service-flows/service-12-receive-escrow-payment.md) and [#20](../../service-flows/service-20-deposit-mortgage-into-escrow.md)–[#21](../../service-flows/service-21-cancel-bank-guarantee.md). It is a product feature, entirely separate from how RERA's *service fees* are paid.
>
> RERA service fees moved to per-transaction payment through the shared platform payment gateway on 2026-08-15 (issue #58); there is no standing or pre-funded RERA-fee account for developers. That change does not touch anything on this screen. A balance, a top-up, or a debit shown here is escrow, not fees — do not read it as a retired fee-account artifact and remove it.

## Purpose

List the organization's project escrow accounts and provide both the oversight view of escrow position and compliance, and the operational controls to register accounts, request fund releases and coordinate with the Account Trustee. Any user may do either.

## Layout

```
Top Bar
↓
Escrow Summary Cards
↓
Filters & Search
↓
Escrow Accounts Table
↓
Fund Release Overview
↓
Escrow Analytics
↓
Pagination
```

**Top Bar**

* Title: Escrow Management
* Subtitle: Monitor project escrow accounts and manage milestone-based fund releases.
* Search Bar: Search anything...
* Page Actions: **Register Escrow Account** · **Request Fund Release**

The page uses the shared **Background + HorizontalBorder** component.

## Sections

### Section 1 — Escrow Summary Cards

| KPI | Description | Absorbed from |
| :---- | :---- | :---- |
| Active Escrow Accounts | Currently active escrow accounts | Principal |
| Total Escrow Balance | Total funds held in escrow | Principal |
| Pending Fund Releases | Awaiting milestone approval | Principal |
| Released Funds | Funds successfully released | Principal |
| Pending Milestones | Milestones awaiting completion | Principal |
| Completed Milestones | Successfully completed milestones | Principal |
| Escrow Compliance | Overall compliance rate | Principal |
| Financial Institutions | Partner financial institutions | Principal |

**Note:** the operational variant defined no summary cards at all — it opened directly on Filter & Search. The oversight variant's card set is therefore carried forward whole, and is now shown to every user. This is an addition to the operational surface, not a loss from it.

Selecting a card filters the table.

### Section 2 — Filters & Search

**Search by:** Escrow ID · Project Name · Project Registration Number · Financial Institution · Account Number

**Filters**

* Escrow Status — All · Pending Registration · Active · Suspended · Closed
* Fund Release Status — All · No Request · Pending Approval · Under Review · Approved · Released · Returned · Rejected
* Project Filter
* Financial Institution Filter
* Date Range Filter
* Reset Filters

**Sort by:** Recently Updated · Registration Date · Project Name · Escrow Status

**Absorbed 2026-08-15:** the operational variant's detailed search-field list, explicit status filter values and sort options — none of which the oversight variant defined — combined with the oversight variant's Project, Financial Institution and Date Range filters.

### Section 3 — Escrow Accounts Table

| Column | Description |
| :---- | :---- |
| Escrow ID | Unique escrow reference |
| Project | Registered development project |
| Financial Institution | Escrow bank |
| Escrow Account Number | Registered escrow account |
| Escrow Balance | Current balance |
| Current Milestone | Latest construction milestone |
| Last Fund Release | Most recent approved release |
| Escrow Status | Current account status |
| Release Status | Fund release status |
| Last Updated | Most recent activity |
| Action | Available actions |

**Absorbed 2026-08-15:** the union of both variants' columns. *Escrow Account Number* and *Last Fund Release* came only from the operational view; *Release Status* only from the oversight view. **Reconciled:** the oversight view called the balance column *Escrow Balance* and the operational view called it *Available Balance*; kept as **Escrow Balance** — see [Notes](#notes).

### Row Actions

* View Details
* Request Fund Release
* View Applications
* View Documents
* Download Escrow Summary

**Reconciled 2026-08-15:** the oversight variant offered only *View Details*, with a note that "this screen is read-only for the Developer Principal." That was an access restriction, not a lifecycle rule, and is retired. The operational action set now applies to every user. Where an action is genuinely unavailable it is because of the account's own state — a closed account takes no new release request — not because of who is asking.

### Bulk Actions

* Export Selected
* Generate Summary Report

Previously operational-variant only; now available to every user.

### Section 4 — Fund Release Overview

**Absorbed 2026-08-15** from the oversight view, the only variant to carry it.

| Column | Description |
| :---- | :---- |
| Milestone | Construction milestone |
| Planned Date | Expected completion |
| Actual Date | Completion date |
| Release Amount | Funds associated with milestone |
| Status | Current milestone status |

### Section 5 — Escrow Analytics

**Absorbed 2026-08-15** from the oversight view. Retained in full.

**Financial Summary**

* Total Escrow Value
* Released This Month
* Pending Release Value
* Average Release Time

**Compliance Summary**

* Milestones On Schedule
* Delayed Milestones
* Pending Reviews
* Compliance Score

### Status Badges

Two vocabularies apply — **Escrow Status** and **Fund Release Status**. See [status-badges.md](../status-badges.md); this screen defines neither.

## Empty State

**Message**

> No escrow accounts registered yet. Register a project escrow account to begin tracking milestone-based fund releases.

**Primary Button** — Register Escrow Account
**Secondary Button** — View Projects

**Reconciled 2026-08-15:** the oversight variant's empty state offered only navigation (*View Projects*, *View Sales & Disclosures*); the operational variant offered *Register Escrow Account*. Both survive, with the create action primary.

## Pagination

Rows per page · Previous · Next · Page Number · Total Records

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

1. No card, column, filter, row action or section on this screen is role-gated. What a user can do to an escrow account depends on the account's state, never on who they are.
2. Summary card figures must match the table's own filtered counts exactly.
3. The escrow account's status and the fund release's status are separate values and must not be conflated in filters, badges or counts.
4. Balances shown here are the project escrow account's, sourced from the escrow system of record — never a RERA-fee figure.

## User Flow

```
Dashboard
↓
Escrow Management
├─ Register Escrow Account → escrow registration flow
├─ Request Fund Release → Fund Release Request
├─ Summary Card → filtered table
├─ Row → Escrow Details
└─ Escrow Analytics → Reports
```

## Notes

* **This absorbs, rather than references, both retired variants.** The oversight screen and the operational workspace are gone as separate designs; their summary cards, search and filter structures, columns, row actions, fund release overview and analytics are now one screen.

* **Reconciliation — "Escrow Balance" vs "Available Balance."** The oversight variant's column was *Escrow Balance* ("current balance"); the operational variant's was *Available Balance* ("current escrow balance"). The definitions are identical, but the names are not interchangeable in an escrow context, where *available* can imply funds net of committed releases. Since neither variant defined a committed-funds concept, and both glossed the column the same way, kept as **Escrow Balance** — the neutral reading, matching the Total Escrow Balance KPI. **If the client intends "available" to mean net of pending releases, that is a real distinction and would need a second column; flagged rather than assumed.**

* **The two variants were asymmetric, not parallel.** The oversight variant had eight summary cards, a Fund Release Overview and an Analytics section but almost no filtering and one row action. The operational variant had rich search, explicit filter values and sorting, five row actions and bulk actions, but no summary cards and no analytics. Each was close to the complement of the other, so this merge is mostly additive — very little overlapped enough to need choosing between.

* **What was dropped, and why.** Only the "this screen is read-only for the Developer Principal" note and the view-only row-action list — both access restrictions. Nothing representing distinct work was discarded.
