---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - real-estate-developer
  - ui-spec
---

# Screen: Sales & Disclosures

**Roles:** Principal · Sales & Disclosure Officer

A list of property sales and their disclosure status. The Developer Principal / Director has read-only, organization-wide oversight; the Sales & Disclosure Officer has an operational workspace for recording sales, preparing disclosures, and progressing them through RERA review.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Sales & Disclosures**
* **Top Bar Title:** Sales & Disclosures
* **Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

Both roles' Layout diagrams share the same core shape (Top Bar → Sales Summary Cards → Filters & Search → Sales & Disclosures Table → Pagination); the Sales & Disclosure Officer's inserts an extra **Bulk Actions** step before Pagination, and the Principal's inserts a **Sales Analytics** step instead. The subtitle and page actions differ by role — see [Role Variations](#role-variations).

## Sections

Every section (Sales Summary Cards, Filters, the Sales & Disclosures Table and its Row Actions, Sales/Disclosure Status Badges, Bulk Actions — Sales & Disclosure Officer only — and the closing analytics/performance section) is role-specific — see [Role Variations](#role-variations).

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations).

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Sales & Disclosures**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * **Sales & Disclosures (Active)**  
  * Escrow Management  
  * Applications  
  * Documents  
  * Reports  
  * Company Profile  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Sales & Disclosures

**Subtitle:** Monitor all property sales, buyer disclosures, and regulatory compliance across your developments.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with an executive view of all property sales and disclosure activities, ensuring every completed sale complies with RERA disclosure requirements and allowing management to monitor the sales pipeline across all projects.

### Layout

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

### Section 1 — Sales Summary Cards

Display eight KPI cards.

| KPI | Description |
| ----- | ----- |
| Total Sales | Total recorded property sales |
| Active Listings | Properties currently available for sale |
| Pending Disclosures | Awaiting disclosure submission |
| Submitted Disclosures | Submitted to RERA |
| Approved Disclosures | Successfully accepted |
| Returned Disclosures | Returned for correction |
| Total Sales Value | Combined value of completed sales |
| This Month's Sales | Sales completed during the current month |

Selecting a KPI filters the table.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Property / Buyer  
* Project Filter  
* Sales Status Filter  
* Disclosure Status Filter  
* Property Type Filter  
* Date Range Filter  
* Reset Filters

### Section 3 — Sales & Disclosures Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Sale Reference | Unique sale reference |
| Property | Property Name / Unit |
| Project | Development Project |
| Buyer | Buyer Name |
| Sale Date | Date of sale |
| Sale Value | Transaction value |
| Disclosure Status | Current disclosure status |
| Current Status | Overall sale status |
| Action | View Details |

### Row Actions

Each row includes:

* View Details

The Developer Principal has oversight access only.

### Sales Status Badges

See [status-badges.md](../status-badges.md#sales-status) for the status vocabulary — including a conflict between the Principal's and the Officer's lists.

### Disclosure Status Badges

See [status-badges.md](../status-badges.md#disclosure-status) for the status vocabulary — including a conflict between the Principal's and the Officer's lists.

### Section 4 — Sales Analytics

Display two summary cards.

#### **Sales Performance**

* Sales This Month  
* Sales This Quarter  
* Average Sale Value  
* Total Revenue

#### **Disclosure Compliance**

* Compliance Rate  
* Pending Disclosures  
* Average Approval Time  
* Returned Cases

Both cards use the platform's standard analytics component.

### Empty State

#### **Message**

> No property sales have been recorded yet.

Primary Button

* View Projects

Secondary Button

* View Property Registrations

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
Sales & Disclosures  
↓  
Search / Filter Sales  
↓  
Select Sale  
↓  
Sales & Disclosure Details

### Notes

* This is an **executive monitoring screen** for the **Developer Principal / Director**.  
* It provides complete visibility into sales activities and regulatory disclosure compliance without allowing operational edits.  
* Creation and submission of sales disclosures remain the responsibility of the **Sales & Disclosure Officer**.

### Sales & Disclosure Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Sales & Disclosures**  
* **Other Menu Items:**  
  * Dashboard  
  * **Sales & Disclosures (Active)**  
  * Applications  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Sales & Disclosures

**Subtitle:** Record property sales, prepare disclosures, and manage regulatory compliance for completed transactions.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Record Property Sale  
* Create Sales Disclosure

### Purpose

Provide the Sales & Disclosure Officer with the primary operational workspace for managing the complete lifecycle of property sales and disclosure submissions. The officer can record sales, prepare buyer disclosures, submit disclosure packages to RERA, respond to regulatory queries, and monitor approval progress.

Unlike the Developer Principal's read-only oversight page, this screen supports full operational activities.

### Layout

Top Bar  
↓  
Sales Summary Cards  
↓  
Filters & Search  
↓  
Sales & Disclosures Table  
↓  
Bulk Actions  
↓  
Pagination

### Section 1 — Sales Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Sales | All recorded sales |
| Draft Sales | Sales not yet finalized |
| Sales Awaiting Disclosure | Sales requiring disclosure preparation |
| Draft Disclosures | Disclosures being prepared |
| Submitted Disclosures | Submitted to RERA |
| Under Review | Currently under regulatory review |
| Returned Disclosures | Require correction |
| Approved Disclosures | Successfully approved |

Selecting a KPI filters the table.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Property / Buyer  
* Project Filter  
* Property Type Filter  
* Sales Status Filter  
* Disclosure Status Filter  
* Date Range Filter  
* Assigned Officer Filter *(if applicable)*  
* Reset Filters

### Section 3 — Sales & Disclosures Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Sale Reference | Unique sales reference |
| Property | Property / Unit |
| Project | Development project |
| Buyer | Buyer name |
| Sale Date | Date of transaction |
| Sale Value | Sale amount |
| Disclosure Status | Regulatory disclosure status |
| Current Stage | Operational stage |
| Last Updated | Latest activity |
| Action | Available actions |

### Row Actions

Available actions depend on the current status.

#### **Draft Sale**

* Continue Sale Entry  
* Edit  
* Delete

#### **Disclosure Pending**

* Create Disclosure  
* Upload Buyer Documents

#### **Draft Disclosure**

* Continue Disclosure  
* Edit  
* Validate  
* Submit to RERA

#### **Under Review**

* View Details

#### **Information Requested / Returned**

* Respond to Query  
* Upload Additional Documents  
* Correct Disclosure  
* Resubmit

#### **Approved**

* View Details  
* Download Disclosure Summary

### Sales Status Badges

See [status-badges.md](../status-badges.md#sales-status) for the status vocabulary — including a conflict between the Principal's and the Officer's lists.

### Disclosure Status Badges

See [status-badges.md](../status-badges.md#disclosure-status) for the status vocabulary — including a conflict between the Principal's and the Officer's lists.

### Bulk Actions

Allow bulk operations where applicable.

Available actions:

* Export Selected  
* Download Sales Summary  
* Print Sales Register  
* Bulk Assign *(if supported)*  
* Bulk Generate Reports

Bulk submission is available only where business rules permit.

### Section 4 — Sales Performance Overview

Display two operational summary cards.

#### **Sales Performance**

* Total Sales Value  
* Sales This Month  
* Average Sale Value  
* Pending Sales

#### **Disclosure Performance**

* Disclosure Completion Rate  
* Average Approval Time  
* Returned Cases  
* Buyer Documents Pending

Selecting any metric filters the table.

### Empty State

#### **Message**

> No property sales have been recorded yet. Record your first property sale to begin the disclosure process.

Primary Button

* Record Property Sale

Secondary Button

* View Approved Projects

### Pagination

Bottom of the table.

#### **Components**

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
Sales & Disclosures  
├── Record Property Sale  
├── Continue Sale Entry  
├── Create Sales Disclosure  
├── Upload Buyer Documents  
├── Submit Disclosure  
├── Respond to RERA Query  
├── Resubmit Disclosure  
└── View Sales & Disclosure Details

### Notes

* This is the **primary operational screen** for the **Sales & Disclosure Officer**.  
* Sales can only be recorded against **approved and registered properties**.  
* Returned disclosures and **Information Requested** cases should automatically appear at the top of the list.  
* The workflow progresses from **Property Sale → Buyer Information → Sales Disclosure → RERA Review → Approval**, with each stage fully traceable.  
* Every edit, submission, buyer document upload, regulatory response, and approval should be recorded in the audit trail to maintain compliance.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations).

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
