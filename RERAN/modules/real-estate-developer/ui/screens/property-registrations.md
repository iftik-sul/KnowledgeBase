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

**Access:** All four roles — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../../navigation.md). Role is audit-trail attribution only.

A list of property registrations. The Developer Principal / Director has read-only, organization-wide visibility; the Registration Officer has an operational workspace for creating, editing, submitting, and correcting registrations under approved projects.

## Purpose

Purpose differs between variants — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Property Registrations**
* **Top Bar Title:** Property Registrations
* **Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

Both roles' Layout diagrams share the same core shape (Top Bar → Registration Summary Cards → Filters & Search → Property Registrations Table → Pagination); the Registration Officer's inserts an extra **Bulk Actions** step before Pagination that the Principal's lacks. The subtitle and page actions differ by role — see [Role Variations](#role-variations).

## Sections

Every section (Registration Summary Cards, Filters, the Property Registrations Table and its Row Actions, Registration Status Badges, Bulk Actions, in the Registration Officer variant only, and the closing insights section) differs between variants — see [Role Variations](#role-variations).

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
* **Active Menu:** **Property Registrations**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

### Top Bar Status

**Title:** Property Registrations

**Subtitle:** Monitor all property registrations submitted under your development projects.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with complete visibility into all property registrations across the organization, allowing them to monitor approval progress, registration status, and regulatory compliance without performing operational registration activities.

### Layout

Top Bar  
↓  
Registration Summary Cards  
↓  
Filters & Search  
↓  
Property Registrations Table  
↓  
Pagination

### Section 1 — Registration Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| Total Registrations | All property registrations |
| Pending Review | Awaiting RERA review |
| Approved | Successfully registered |
| Returned for Correction | Requires additional information |
| Rejected | Registration rejected |
| Registered This Month | New registrations during the current month |

Selecting a KPI automatically filters the table.

### Section 2 — Filters

Located directly above the table.

#### **Components**

* Search Property  
* Project Filter  
* Registration Status Filter  
* Property Type Filter  
* Date Range Filter  
* Reset Filters

### Section 3 — Property Registrations Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Registration No. | Unique registration reference |
| Property ID | Internal property identifier |
| Property Name / Unit | Registered property |
| Project Name | Associated development project |
| Property Type | Apartment, Villa, Commercial, etc. |
| Submitted Date | Registration submission date |
| Current Status | Registration status |
| Last Updated | Latest activity |
| Action | View Details |

### Row Actions

Each row includes:

* View Details

The Developer Principal has read access only. Registration activities are performed by the Project Registration Officer.

### Registration Status Badges

See [status-badges.md](../status-badges.md#property-registration-status) for the status vocabulary — including a conflict between the Principal's and the Registration Officer's lists. (This role's version of the source additionally noted "Badge colors follow the existing RERA design system" — see the note at the top of status-badges.md on why no actual colours survived migration.)

### Section 4 — Registration Insights

Below the table, display two summary cards.

#### **Registration Performance**

* Approval Rate  
* Average Approval Time  
* Registrations This Quarter  
* Pending Reviews

#### **Registration Distribution**

Breakdown by property type.

Example

* Residential  
* Commercial  
* Mixed Use  
* Industrial

This can use the platform's standard chart component.

### Empty State

#### **Message**

> No property registrations have been submitted yet.

Primary Button

* View Projects

Secondary Button

* Learn About Property Registration

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
Property Registrations  
↓  
Search / Filter Registrations  
↓  
Select Registration  
↓  
Property Registration Details

### Next Screen

**Property Registration Details**

This screen presents the complete registration record for a single property, including:

* Property information  
* Linked development project  
* Registration timeline  
* Submitted documents  
* RERA review history  
* Comments and queries  
* Approval status  
* Audit trail

It serves as the primary read-only review page for the Developer Principal / Director.

### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Property Registrations**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

### Top Bar Status

**Title:** Property Registrations

**Subtitle:** Register and manage properties under approved development projects.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Register New Property

### Purpose

Provide the Project Registration Officer with an operational workspace to create, edit, submit, and monitor individual property registrations within approved development projects. This screen serves as the primary interface for managing property registration activities before and during RERA review.

### Layout

Top Bar  
↓  
Registration Summary Cards  
↓  
Filters & Search  
↓  
Property Registrations Table  
↓  
Bulk Actions  
↓  
Pagination

### Section 1 — Registration Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Properties | All registered and draft properties |
| Draft Registrations | Registrations being prepared |
| Submitted | Submitted to RERA |
| Under Review | Currently under regulatory review |
| Information Requested | Awaiting developer response |
| Approved | Successfully registered |
| Returned | Returned for correction |
| Registered This Month | Completed registrations this month |

Selecting a KPI filters the table.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Property  
* Project Filter  
* Property Type Filter  
* Registration Status Filter  
* Assigned Officer Filter *(if applicable)*  
* Date Range Filter  
* Reset Filters

### Section 3 — Property Registrations Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Registration No. | Registration reference |
| Property Name / Unit | Property or unit |
| Project | Parent development project |
| Property Type | Apartment, Villa, Commercial, etc. |
| Current Status | Registration stage |
| Submitted Date | Date submitted |
| Last Updated | Latest activity |
| Action | Available actions |

### Row Actions

Actions depend on registration status.

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

* View Registration Certificate  
* Download Registration Summary

### Registration Status Badges

See [status-badges.md](../status-badges.md#property-registration-status) for the status vocabulary — including a conflict between the Principal's and the Registration Officer's lists.

### Bulk Actions

Allow bulk operations where applicable.

Available actions:

* Export Selected  
* Download Registration Summary  
* Delete Drafts  
* Print Registration List

Bulk submission is available only if permitted by business rules.

### Section 4 — Registration Progress Overview

Display two operational summary cards.

#### **Registration Performance**

* Approval Rate  
* Average Processing Time  
* Registrations Submitted This Month  
* Pending Responses

#### **Project Distribution**

Breakdown of registrations by project.

Example:

* Project A  
* Project B  
* Project C  
* Others

Selecting a project filters the table.

### Empty State

#### **Message**

> No property registrations have been created yet. Register your first property under an approved development project.

Primary Button

* Register New Property

Secondary Button

* View Projects

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
Property Registrations

├── Register New Property

├── Continue Registration

├── Edit Registration

├── Submit Registration

├── Respond to RERA Query

├── Download Registration Summary

└── View Property Registration Details

### Notes

* This is the **primary operational screen** for the **Project Registration Officer**.  
* Only **approved development projects** are available when creating a new property registration.  
* Registrations returned by RERA should be visually highlighted and appear at the top of the default list.  
* Officers can manage the complete lifecycle of a property registration, from draft creation through approval, while maintaining full traceability of submissions and responses.

## User Flow

Differs between variants — see the "User Flow" heading within each role's block under [Role Variations](#role-variations).

## Notes

Only the variant under the Registration Officer heading has an explicit Notes section — see that role's block under [Role Variations](#role-variations). The Principal's version has no Notes section; it closes instead with a "Next Screen" preview of Property Registration Details, preserved verbatim in its block above.
