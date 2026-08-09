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

# Screen: Project Details

**Roles:** Principal · Registration Officer

The detail view of a single project, opened from [Projects](projects.md). The Developer Principal / Director sees a read-only executive view consolidating sales, escrow, documents, and compliance status; the Registration Officer sees an editable operational workspace for preparing, validating, and submitting the project registration.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Projects**
* **Top Bar Title:** Project Details
* **Search Bar:** Search anything...

Both roles reuse the shared Background + HorizontalBorder component, worded slightly differently in each ("The shared Background + HorizontalBorder component is reused" vs "The page uses the shared Background + HorizontalBorder component"), so the exact sentence is kept per role rather than merged. The two layout diagrams are entirely different in shape and content — see [Role Variations](#role-variations).

## Sections

Every section is role-specific — see [Role Variations](#role-variations). The Principal's version is organized around consolidated summary/overview cards (Sales Overview, Escrow Overview, Documents, Compliance); the Registration Officer's is organized around the registration workflow itself (Required Documents, Validation Summary, RERA Queries).

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations).

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Validation

Only the Registration Officer's version has a Validation Summary — the Principal's is read-only and has none. See that role's "Validation Summary" block under [Role Variations](#role-variations).

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

**Title:** Project Details

**Subtitle:** View the complete status and regulatory information for this development project.

**Search Bar:** Search anything...

The shared **Background \+ HorizontalBorder** component is reused.

### Purpose

Provide the Developer Principal / Director with a comprehensive executive view of a single development project, including project information, registration progress, compliance, sales, escrow, and recent activities.

### Layout

Top Bar  
↓  
Project Header  
↓  
Project Summary Cards  
↓  
Project Information  
↓  
Registration Progress  
↓  
Sales Overview          Escrow Overview  
↓  
Documents              Compliance  
↓  
Recent Activity Timeline

### Section 1 — Project Header

Displays key project information.

#### **Left**

* Project Name  
* Project ID  
* Project Status Badge  
* Project Location

#### **Right**

* Registration Date  
* Last Updated  
* View Reports (Button)

### Section 2 — Project Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| Total Units | Number of units in the project |
| Registered Units | Units registered with RERA |
| Units Sold | Sold properties |
| Active Escrow Cases | Ongoing escrow processes |
| Pending Applications | Applications awaiting approval |
| Compliance Issues | Outstanding issues |

### Section 3 — Project Information

Display information in a two-column information card.

#### **General Information**

* Project Name  
* Project ID  
* Development Type  
* Location  
* Land Size  
* Number of Phases  
* Estimated Completion Date

#### **Responsible Personnel**

* Project Registration Officer  
* Sales & Disclosure Officer  
* Escrow Liaison

### Section 4 — Registration Progress

Visual progress tracker showing project registration stages.

#### **Stages**

* Project Submitted  
* Under Review  
* Additional Information Requested  
* Approved  
* Active Development

Completed stages use the existing success indicator.

Current stage is highlighted.

### Section 5 — Sales Overview

Summary card.

Display:

* Total Properties Listed  
* Properties Sold  
* Pending Sales Disclosures  
* Latest Disclosure Date

Button

* View Sales & Disclosures

### Section 6 — Escrow Overview

Summary card.

Display:

* Escrow Institution  
* Active Escrow Account  
* Current Milestone  
* Funds Released  
* Pending Releases

Button

* View Escrow Details

### Section 7 — Documents

Table showing project-related documents.

#### **Columns**

* Document Name  
* Category  
* Uploaded By  
* Upload Date  
* Status  
* Action

Actions

* View

### Section 8 — Compliance

Display compliance status cards.

Examples

* Environmental Clearance  
* Development Permit  
* Building Approval  
* RERA Compliance  
* Sales Disclosure Compliance

Each item shows:

* Status Badge  
* Last Review Date

### Section 9 — Recent Activity

Timeline of project events.

Examples

* Project registered  
* Additional documents uploaded  
* Registration approved  
* Sales disclosure submitted  
* Escrow milestone completed  
* Inspection scheduled

Display the latest 10 activities.

### Empty State

If the project has just been created and has limited information:

**Message**

> This project has been registered, but operational information is not yet available.

Primary Button

* View Applications

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Projects  
↓  
Project Details  
├── View Sales & Disclosures  
├── View Escrow Details  
├── View Applications  
├── View Documents  
└── View Reports

### Notes

* This is a **read-oriented executive screen** designed for the **Developer Principal / Director**.  
* The page consolidates information from multiple modules into a single project view, allowing executives to monitor progress without navigating through operational screens.  
* All editing and submission actions remain with the operational roles (Project Registration Officer, Sales & Disclosure Officer, and Escrow Liaison), while the Principal / Director has oversight and review capabilities.

### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Projects**  
* **Selected Item:** Project Details *(opened from Projects list)*  
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

**Title:** Project Details

**Subtitle:** Complete and manage the development project registration before submission to RERA.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Draft  
* Submit to RERA *(Enabled only when validation passes)*  
* More Actions

### Purpose

Provide the Project Registration Officer with a complete operational workspace to prepare, validate, submit, update, and track a development project throughout the registration lifecycle. Unlike the Developer Principal's read-only project page, this screen is fully interactive and supports editing, document submission, and responding to RERA requests.

### Layout

Top Bar  
↓  
Project Header  
↓  
Registration Progress  
↓  
Project Information  
↓  
Development Information  
↓  
Required Documents  
↓  
Validation Summary  
↓  
RERA Queries (if applicable)  
↓  
Activity Timeline

### Section 1 — Project Header

Displays the project's key information.

#### **Left**

* Project Name  
* Project ID  
* Registration Status Badge  
* Development Type

#### **Right**

* Created Date  
* Last Updated  
* Assigned Officer  
* Save Status

### Section 2 — Registration Progress

A horizontal progress tracker.

#### **Stages**

* Draft  
* Project Information Completed  
* Documents Uploaded  
* Validation Passed  
* Submitted  
* Under Review  
* Approved

Completed stages use the platform's standard success indicator.

The current stage is highlighted.

Clicking completed stages navigates directly to that section.

### Section 3 — Project Information

Editable form.

#### **Basic Information**

* Project Name  
* Development Type  
* Project Description  
* Project Address  
* State  
* Local Government Area  
* Coordinates *(optional)*  
* Expected Start Date  
* Expected Completion Date

#### **Development Information**

* Number of Phases  
* Total Land Area  
* Number of Units  
* Residential Units  
* Commercial Units  
* Mixed Use Details *(if applicable)*

#### **Responsible Contacts**

* Project Manager  
* Registration Officer  
* Contact Email  
* Contact Phone

### Section 4 — Required Documents

Document upload section.

Display required documents with completion status.

#### **Example Documents**

* Land Ownership Documents  
* Development Approval  
* Survey Plan  
* Architectural Drawings  
* Environmental Clearance  
* Building Permit  
* Company Authorization Letter  
* Other Supporting Documents

#### **Columns**

| Document | Status | Uploaded On | Version | Action |
| :---: | :---: | :---: | :---: | :---: |

Actions

* Upload  
* Replace  
* Preview  
* Delete *(Draft only)*

### Section 5 — Validation Summary

See [validation-rules.md](../validation-rules.md) for the shared automatic-validation mechanism and the common field-level checks (required fields, required documents, file verification). This screen's own additional checks: Duplicate project check, Date validation, Location validation.

### Section 6 — RERA Queries

Visible only if RERA requests additional information.

#### **Table**

| Date | Request | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: |

Actions

* Respond  
* Upload Additional Documents  
* View Previous Response

Outstanding queries are highlighted.

### Section 7 — Activity Timeline

Displays every operational event.

Examples

* Project created  
* Information updated  
* Documents uploaded  
* Validation completed  
* Submitted to RERA  
* Returned for correction  
* Additional documents uploaded  
* Resubmitted  
* Approved

Latest activities appear first.

### Empty State

If this is a newly created project:

**Message**

> Start by completing the project information and uploading the required supporting documents before submitting the project for registration.

Primary Button

* Complete Project Information

Secondary Button

* Upload Documents

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Projects  
↓  
Project Details

├── Edit Project Information

├── Upload Documents

├── Save Draft

├── Validate Project

├── Submit to RERA

├── Respond to RERA Query

└── Register Properties

### Notes

* This is the **primary operational screen** for the **Project Registration Officer**.  
* The officer can continuously edit the project until it is submitted.  
* After submission, editable fields become read-only unless RERA returns the application for correction.  
* The **Submit to RERA** button remains disabled until all mandatory validations pass.  
* Once the project reaches the **Approved** status, the officer can proceed to **Property Registrations**, allowing individual units or properties under the project to be registered. This workflow aligns with the Project Registration Officer's responsibility for project registration, document submission, application tracking, and responding to RERA requests.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations).

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
