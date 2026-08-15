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

**Access:** All four roles — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../../navigation.md). Role is audit-trail attribution only.

A list of development projects. The source defines two variants: an executive portfolio view (under the Principal / Director heading) and an operational workspace (under the Registration Officer heading) for creating, editing, submitting and correcting projects. Both variants are reachable and actionable by all four roles — the difference is in what the variant shows, not in who may open it.

## Purpose

Purpose differs between variants — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Projects**
* **Top Bar Title:** Projects
* **Search Bar:** Search anything...

Both roles' Layout diagrams are the same shape (Top Bar → Project Summary Cards → Filters & Search → Projects Table → Pagination), but the subtitle, the top-bar description sentence, and page actions differ by role — see [Role Variations](#role-variations).

## Sections

Every section (Project Summary Cards, Filters, the Projects Table and its Row Actions, Project Status Badges, and, in the Registration Officer variant only, Bulk Actions) differs between variants — see [Role Variations](#role-variations).

## Empty State

Message and actions differ between variants — see [Role Variations](#role-variations).

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
* **Active Menu:** **Projects**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

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

See [status-badges.md](../status-badges.md#project-status) for the status vocabulary — including a conflict between the Principal's and the Registration Officer's lists.

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

See [components.md](../components.md) for definitions of every component used on this screen.

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
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

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

See [status-badges.md](../status-badges.md#project-status) for the status vocabulary — including a conflict between the Principal's and the Registration Officer's lists.

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

See [components.md](../components.md) for definitions of every component used on this screen.

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

Differs between variants — see the "User Flow" heading within each role's block under [Role Variations](#role-variations).

## Notes

Differs between variants — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
