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

**Access:** All four roles — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../../navigation.md). Role is audit-trail attribution only.

A list of escrow accounts. The source defines two variants: an organization-wide oversight variant (under the Principal / Director heading) and an operational workspace (under the Escrow Liaison heading) for registering escrow accounts and initiating fund release requests. Both variants are reachable and actionable by all four roles — the difference is in what the variant shows, not in who may open it.

> **The escrow balances on this screen are not a RERA-fee account.** The balance, milestone and fund-release figures shown here belong to the developer's **project escrow account** — the regulated holding account for sale proceeds, deposits and construction-milestone releases that is the subject matter of Services [#8](../../service-flows/service-08-activate-escrow-account.md)–[#12](../../service-flows/service-12-receive-escrow-payment.md) and [#20](../../service-flows/service-20-deposit-mortgage-into-escrow.md)–[#21](../../service-flows/service-21-cancel-bank-guarantee.md). It is a product feature, entirely separate from how RERA's *service fees* are paid.
>
> RERA service fees moved to per-transaction payment through the shared platform payment gateway on 2026-08-15 (issue #58); there is no standing or pre-funded RERA-fee account for developers. That change does not touch anything on this screen. A balance, a top-up, or a debit shown here is escrow, not fees — do not read it as a retired fee-account artifact and remove it.

## Purpose

Purpose differs between variants — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Escrow Management**
* **Top Bar Title:** Escrow Management
* **Search Bar:** (differs by role — see below)

The page uses the shared **Background \+ HorizontalBorder** component.

The two Layout diagrams differ substantially: the Principal's is a 6-step flow including Escrow Summary Cards and Escrow Analytics; the Escrow Liaison's is a simpler 3-step flow (Filter & Search → Escrow Accounts Table → Pagination) with no KPI summary cards at all. The subtitle and search-bar placeholder text also differ by role — see [Role Variations](#role-variations).

## Sections

Every section differs between variants — see [Role Variations](#role-variations). The Escrow Liaison's version has no KPI/summary-card section, and organizes filters and status badges differently from the Principal's.

## Empty State

Message and actions differ between variants — see [Role Variations](#role-variations). Only the Escrow Liaison's version specifies an illustration (Escrow Account), consistent with the pattern seen on that role's other screens.

## Reused Components

Differs between variants — see [Role Variations](#role-variations).

## Role Variations

> **Reframed 2026-08-15 — these are content variants, not access restrictions.** Every variant
> below is reachable and actionable by all four roles; none of them is withheld from anyone. What
> the blocks record is that the source material defined this screen more than once, with different
> KPI sets, filters, columns, actions or empty states each time — differences of *content*, not of
> permission. Those are preserved verbatim rather than merged, because collapsing them into one
> screen is a design decision about which variant (or which union of them) is correct, and that is
> the client's call, not a documentation cleanup. **Flagged for review — see
> [../README.md](../README.md#per-role-content-variants-flagged-for-review).**
>
> The role headings below should now be read as *"the variant the source defined under this role's
> heading"*, not *"what this role is allowed to see"*.

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Escrow Management**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

### Top Bar Status

**Title:** Escrow Management

**Subtitle:** Monitor escrow accounts, fund release milestones, and financial institution coordination.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with an executive overview of all escrow activities across development projects, ensuring funds are released according to approved milestones and all escrow obligations remain compliant with RERA requirements.

### Layout

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

### Section 1 — Escrow Summary Cards

Display eight KPI cards.

| KPI | Description |
| ----- | ----- |
| Active Escrow Accounts | Currently active escrow accounts |
| Total Escrow Balance | Total funds held in escrow |
| Pending Fund Releases | Awaiting milestone approval |
| Released Funds | Funds successfully released |
| Pending Milestones | Milestones awaiting completion |
| Completed Milestones | Successfully completed milestones |
| Escrow Compliance | Overall compliance rate |
| Financial Institutions | Partner financial institutions |

Selecting a KPI filters the table.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Escrow Account  
* Project Filter  
* Financial Institution Filter  
* Escrow Status Filter  
* Fund Release Status Filter  
* Date Range Filter  
* Reset Filters

### Section 3 — Escrow Accounts Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Escrow ID | Unique escrow reference |
| Project | Development project |
| Financial Institution | Escrow bank |
| Escrow Balance | Current balance |
| Current Milestone | Latest construction milestone |
| Release Status | Fund release status |
| Last Updated | Most recent activity |
| Action | View Details |

### Row Actions

Each row includes:

* View Details

This variant provides no editing controls; the operational variant below does, and any role may use either.

### Escrow Status Badges

See [status-badges.md](../status-badges.md#escrow-status) for the status vocabulary — including a conflict between the Principal's and the Escrow Liaison's lists.

### Fund Release Status Badges

See [status-badges.md](../status-badges.md#fund-release-status) for the status vocabulary — including a conflict between the Principal's and the Escrow Liaison's lists.

### Section 4 — Fund Release Overview

Display a milestone progress table.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Milestone | Construction milestone |
| Planned Date | Expected completion |
| Actual Date | Completion date |
| Release Amount | Funds associated with milestone |
| Status | Current milestone status |

### Section 5 — Escrow Analytics

Display two summary cards.

#### **Financial Summary**

* Total Escrow Value  
* Released This Month  
* Pending Release Value  
* Average Release Time

#### **Compliance Summary**

* Milestones On Schedule  
* Delayed Milestones  
* Pending Reviews  
* Compliance Score

### Empty State

#### **Message**

> No escrow accounts have been created for your development projects.

Primary Button

* View Projects

Secondary Button

* View Sales & Disclosures

### Pagination

Bottom of the table.

Components

* Rows per page  
* Previous  
* Next  
* Page Number  
* Total Records

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Escrow Management  
↓  
Search / Filter Escrow Accounts  
↓  
Select Escrow Account  
↓  
Escrow Details

### Notes

* This is an **executive oversight screen** for the **Developer Principal / Director**.  
* It consolidates escrow information from all projects into a single portfolio view.  
* The Principal monitors financial progress and regulatory compliance without performing escrow operations.  
* Escrow coordination and document submission remain the responsibility of the **Escrow Liaison**.

### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Escrow Management**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

### Top Bar Status

**Title:** Escrow Management

**Subtitle:** Manage escrow accounts and monitor fund release progress

**Search Bar:** Search escrow accounts, projects, banks...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Register Escrow Account  
* Request Fund Release

### Purpose

Allow the Escrow Liaison to manage all escrow accounts associated with the developer's projects, monitor account status, track construction milestones, and initiate milestone-based fund release requests.

### Layout

Top Bar  
↓  
Filter & Search  
↓  
Escrow Accounts Table  
↓  
Pagination

### Section 1 — Filter & Search

#### **Search**

Search by:

* Escrow ID  
* Project Name  
* Project Registration Number  
* Financial Institution  
* Account Number

#### **Filters**

**Escrow Status**

* All  
* Pending Registration  
* Active  
* Suspended  
* Closed

**Fund Release Status**

* All  
* No Request  
* Pending Approval  
* Under Review  
* Approved  
* Released  
* Returned  
* Rejected

**Financial Institution**

Dropdown list

**Project**

Dropdown list

**Registration Date**

Date Range

**Sort By**

* Recently Updated  
* Registration Date  
* Project Name  
* Escrow Status

### Section 2 — Escrow Accounts Table

Display all escrow accounts assigned to the developer.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Escrow ID | Unique escrow reference |
| Project | Registered development project |
| Financial Institution | Linked bank |
| Escrow Account Number | Registered escrow account |
| Current Milestone | Latest construction milestone |
| Available Balance | Current escrow balance |
| Last Fund Release | Most recent approved release |
| Escrow Status | Current account status |
| Last Updated | Latest activity |
| Action | View Details |

### Status Badges

#### **Escrow Status**

See [status-badges.md](../status-badges.md#escrow-status) for the status vocabulary — including a conflict between the Principal's and the Escrow Liaison's lists.

#### **Fund Release Status**

See [status-badges.md](../status-badges.md#fund-release-status) for the status vocabulary — including a conflict between the Principal's and the Escrow Liaison's lists.

### Row Actions

Each row contains:

* View Details

Overflow Menu

* Request Fund Release  
* View Applications  
* View Documents  
* Download Escrow Summary

### Bulk Actions

Available after selecting multiple escrow accounts.

* Export Selected  
* Generate Summary Report

### Empty State

**Illustration**

Escrow Account

**Message**

> No escrow accounts have been registered yet.

**Primary Button**

* Register Escrow Account

**Secondary Button**

* Learn About Escrow Registration

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Escrow Management

├── Register Escrow Account  
│      ↓  
│  Register Escrow Account  
│  
├── View Details  
│      ↓  
│  Escrow Details  
│  
├── Request Fund Release  
│      ↓  
│  Fund Release Request  
│  
├── View Applications  
│      ↓  
│  Applications  
│  
└── View Documents  
       ↓  
    Documents

### Notes

* Only escrow accounts linked to the logged-in developer should be displayed.  
* Escrow accounts should always be associated with a registered development project.  
* Escrow status and fund release status should be visually distinct using the platform's standard status badges.  
* Users can only initiate fund release requests from **Active** escrow accounts.  
* Selecting **View Details** opens the complete escrow account record, including project information, account history, milestones, fund releases, uploaded documents, and regulatory actions.

## User Flow

Differs between variants — see the "User Flow" heading within each role's block under [Role Variations](#role-variations).

## Notes

Differs between variants — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
