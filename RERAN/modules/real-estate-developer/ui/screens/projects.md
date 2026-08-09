---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/real-estate-developer/ui-design/RERAN_real_estate_developer_ui.md"
tags:
  - real-estate-developer
  - ui-spec
---

# Screen: Projects

**Roles:** Principal · Registration Officer

A list of development projects. The Developer Principal / Director sees a read-only executive portfolio view; the Registration Officer sees an operational workspace for creating, editing, submitting, and correcting projects.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Projects**
* **Top Bar Title:** Projects
* **Search Bar:** Search anything...

Both roles' Layout diagrams are the same shape (Top Bar → Project Summary Cards → Filters & Search → Projects Table → Pagination), but the subtitle, the top-bar description sentence, and page actions differ by role — see [Role Variations](#role-variations).

## Sections

Every section (Project Summary Cards, Filters, the Projects Table and its Row Actions, Project Status Badges, and — Registration Officer only — Bulk Actions) is role-specific — see [Role Variations](#role-variations).

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations).

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Projects**  
* **Other Menu Items:**  
  * Dashboard  
  * **Projects (Active)**  
  * Property Registrations  
  * Sales & Disclosures  
  * Escrow Management  
  * Applications  
  * Documents  
  * Reports  
  * Company Profile  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Projects

**Subtitle:** Monitor and oversee all development projects across your organization.

**Search Bar:** Search anything...

No additional controls are displayed in the top bar. It reuses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a centralized view of all development projects, allowing executive monitoring of project progress, approvals, compliance status, and overall portfolio performance.

### Layout

Top Bar  
↓  
Project Summary Cards  
↓  
Filters & Search  
↓  
Projects Table  
↓  
Pagination

### Section 1 — Project Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| Total Projects | All registered projects |
| Active Projects | Projects currently under development |
| Pending Approval | Awaiting RERA review |
| Approved Projects | Successfully approved |
| Completed Projects | Development completed |
| Suspended Projects | Projects on hold or suspended |

Each card acts as a quick filter.

### Section 2 — Filters

Located directly above the table.

#### **Components**

* Search Project  
* Status Filter  
* Location Filter  
* Registration Stage Filter  
* Date Range Filter  
* Reset Filters

### Section 3 — Projects Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Project ID | Unique reference |
| Project Name | Registered project name |
| Location | State / City |
| Registration Status | Draft / Pending / Approved / Rejected |
| Development Stage | Planning / Construction / Completed |
| Progress | Percentage completion |
| Last Updated | Latest activity |
| Action | View Details |

### Row Actions

Each row contains:

* View Details

The Principal / Director has oversight responsibilities, so this screen focuses on reviewing project information rather than operational editing.

### Project Status Badges

Use existing platform badge styles.

* Draft  
* Pending Review  
* Approved  
* Rejected  
* Suspended  
* Completed

### Empty State

#### **Message**

> No development projects have been registered yet.

Primary Button

* Learn About Project Registration

### Pagination

Bottom of the table.

Components:

* Rows per page  
* Previous  
* Next  
* Page Number  
* Total Results

### Reused Components

* Left Sidebar  
* Top Bar  
* KPI Cards  
* Search Bar  
* Filter Bar  
* Data Table  
* Status Badges  
* Pagination  
* Empty State  
* Buttons

### User Flow

Dashboard  
↓  
Projects  
↓  
Search / Filter Projects  
↓  
Select Project  
↓  
Project Details

### Notes

* This is an **executive portfolio view**, optimized for monitoring rather than project administration.  
* All project creation, document submission, and registration activities are handled by the **Project Registration Officer**, while the Principal / Director uses this screen to review progress and organizational performance.  
* The table should support sorting by Project Name, Status, Progress, and Last Updated.


### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Projects**  
* **Other Menu Items:**  
  * Dashboard  
  * **Projects (Active)**  
  * Property Registrations  
  * Applications  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Projects

**Subtitle:** Create, manage, and submit development projects for regulatory approval.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Register New Project

### Purpose

Provide the Project Registration Officer with a centralized workspace to create, edit, submit, and track development projects throughout their registration lifecycle. Unlike the Developer Principal's read-only portfolio view, this screen is operational and supports day-to-day project registration activities.

### Layout

Top Bar  
↓  
Project Summary Cards  
↓  
Filters & Search  
↓  
Projects Table  
↓  
Pagination

### Section 1 — Project Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Projects | All assigned projects |
| Draft Projects | Projects still being prepared |
| Submitted Projects | Submitted to RERA |
| Under Review | Currently under regulatory review |
| Information Requested | Waiting for additional information |
| Approved Projects | Successfully approved |
| Returned Projects | Returned for correction |
| Completed Projects | Fully registered projects |

Selecting a KPI filters the project list.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Project  
* Project Status Filter  
* Development Type Filter  
* Location Filter  
* Assigned Officer Filter *(if applicable)*  
* Date Range Filter  
* Reset Filters

### Section 3 — Projects Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Project ID | Unique project reference |
| Project Name | Development project name |
| Development Type | Residential, Commercial, Mixed Use, etc. |
| Location | State / City |
| Current Status | Registration status |
| Last Updated | Latest activity |
| Assigned To | Responsible officer |
| Action | Available actions |

### Row Actions

Available actions depend on project status.

#### **Draft**

* Continue Registration  
* Edit  
* Delete

#### **Submitted / Under Review**

* View Details

#### **Information Requested / Returned**

* Respond to Query  
* Upload Documents  
* Resubmit

#### **Approved**

* View Details  
* Register Properties

### Project Status Badges

Use the shared status component.

* Draft  
* Submitted  
* Under Review  
* Information Requested  
* Returned  
* Approved  
* Rejected  
* Completed

### Bulk Actions

Allow bulk operations for eligible records.

* Export Selected  
* Download Summary  
* Submit Multiple Drafts *(if supported)*  
* Delete Drafts

### Empty State

#### **Message**

> You haven't created any development projects yet.

Primary Button

* Register New Project

Secondary Button

* Learn About Project Registration

### Pagination

Bottom of the table.

Components:

* Rows per page  
* Previous  
* Next  
* Page Number  
* Total Records

### Reused Components

* Left Sidebar  
* Top Bar (Background \+ HorizontalBorder)  
* KPI Cards  
* Search Bar  
* Filter Bar  
* Data Table  
* Status Badges  
* Pagination  
* Buttons  
* Empty State

### User Flow

Dashboard  
↓  
Projects  
├── Register New Project  
├── Continue Registration  
├── Edit Project  
├── Submit Project  
├── Respond to RERA Query  
├── Register Properties  
└── View Project Details

### Notes

* This is the **primary operational screen** for the **Project Registration Officer**.  
* Unlike the Developer Principal's version, this page supports **creating, editing, submitting, correcting, and resubmitting** projects.  
* Projects returned by RERA should be clearly highlighted with high-visibility status badges and surfaced near the top of the list.  
* "Register Properties" becomes available only after the development project reaches the appropriate approved status, following the defined registration workflow.


## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations).

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
