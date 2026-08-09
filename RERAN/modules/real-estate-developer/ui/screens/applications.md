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

# Screen: Applications

**Roles:** Principal · Registration Officer · Sales & Disclosure Officer · Escrow Liaison

A list of every regulatory application relevant to the viewing role. The Developer Principal / Director sees an organization-wide, read-only monitoring view; the three operational roles (Registration Officer, Sales & Disclosure Officer, Escrow Liaison) each see an operational workspace scoped to their own application types, with the ability to continue, edit, respond to, and resubmit applications.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Applications**
* **Top Bar Title:** Applications
* **Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

Which sidebar menu items are visible, the subtitle, top-bar page actions, and the layout diagram differ by role — see [Role Variations](#role-variations). The layout diagram is identical for the Registration Officer, Sales & Disclosure Officer, and Escrow Liaison (Application Summary Cards → Filters & Search → Applications Table → **Pending Actions** → Recent Regulatory Activities → Pagination); the Principal's differs by substituting **Application Analytics** for Pending Actions, reflecting the read-only nature of that role's screen.

## Sections

Every numbered section (Application Summary Cards, Filters, the Applications Table and its Row Actions, Pending Actions / Application Analytics, and Recent Regulatory Activities) is role-specific — see [Role Variations](#role-variations).

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations).

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Applications**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * Sales & Disclosures  
  * Escrow Management  
  * **Applications (Active)**  
  * Documents  
  * Reports  
  * Company Profile  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Applications

**Subtitle:** Monitor all regulatory applications submitted by your organization to RERA.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a centralized, organization-wide view of every application submitted to RERA. This screen enables executives to monitor processing status, approval progress, pending actions, and regulatory turnaround times without participating in operational processing.

### Layout

Top Bar  
↓  
Application Summary Cards  
↓  
Filters & Search  
↓  
Applications Table  
↓  
Application Analytics  
↓  
Recent Regulatory Activities  
↓  
Pagination

### Section 1 — Application Summary Cards

Display eight KPI cards.

| KPI | Description |
| ----- | ----- |
| Total Applications | All submitted applications |
| Draft Applications | Not yet submitted |
| Submitted | Awaiting review |
| Under Review | Currently being processed |
| Additional Information Requested | Waiting for developer response |
| Approved | Successfully approved |
| Rejected | Rejected applications |
| Average Approval Time | Average processing duration |

Selecting any KPI automatically filters the table.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Application ID  
* Application Type Filter  
* Project Filter  
* Status Filter  
* Submitted By Filter  
* Date Range Filter  
* Priority Filter  
* Reset Filters

### Application Types

* Project Registration  
* Property Registration  
* Sales Disclosure  
* Escrow Application  
* Project Amendment  
* License Application  
* Compliance Submission  
* Other Regulatory Service

### Status Badges

See [status-badges.md](../status-badges.md#application-status) for the status vocabulary — including a conflict between the Principal's and the operational roles' lists.

### Priority Indicators

* High  
* Medium  
* Low

### Section 3 — Applications Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Application ID | Unique application number |
| Application Type | Type of submission |
| Project | Related project |
| Submitted By | Responsible employee |
| Submission Date | Date submitted |
| Current Status | Processing stage |
| Last Updated | Latest activity |
| Action | View Details |

### Row Actions

Each row includes:

* View Details

The Developer Principal cannot modify or resubmit applications from this page.

### Section 4 — Application Analytics

Display two analytics cards.

### **Processing Performance**

* Submitted This Month  
* Approved This Month  
* Rejected This Month  
* Average Processing Time

### **Regulatory Compliance**

* Approval Rate  
* Pending Responses  
* Overdue Applications  
* Compliance Score

### Section 5 — Recent Regulatory Activities

Timeline widget displaying the latest organization-wide activities.

Examples

* Project Registration Approved  
* Property Registration Submitted  
* Additional Documents Requested  
* Sales Disclosure Approved  
* Escrow Application Reviewed  
* Compliance Certificate Issued

Each item displays:

* Activity  
* Application ID  
* Date & Time  
* Current Status

Selecting an activity opens the related application.

### Empty State

#### **Message**

> No regulatory applications have been submitted yet.

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
Applications  
↓  
Search / Filter Applications  
↓  
Select Application  
↓  
Application Details

### Notes

* This is an **executive monitoring screen** for the **Developer Principal / Director**.  
* It serves as the single source of truth for every regulatory application submitted by the organization.  
* Executives can quickly identify bottlenecks, delayed approvals, rejected submissions, and applications requiring additional information.  
* All submission, editing, and response activities remain the responsibility of the relevant operational roles (Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison, etc.).

### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Applications**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * **Applications (Active)**  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Applications

**Subtitle:** Track, manage, and respond to all regulatory applications submitted to RERA.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Submit New Application *(Available when applicable)*

### Purpose

Provide the Project Registration Officer with an operational workspace to monitor every application submitted to RERA, respond to information requests, manage returned applications, track approval progress, and maintain full visibility over the registration lifecycle.

Unlike the Developer Principal's version, this screen supports operational follow-up and corrective actions.

### Layout

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
Recent Regulatory Activities  
↓  
Pagination

### Section 1 — Application Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Applications | All submitted applications |
| Draft Applications | Not yet submitted |
| Submitted | Successfully submitted |
| Under Review | Currently being processed |
| Information Requested | Awaiting developer response |
| Returned | Returned for correction |
| Approved | Successfully approved |
| Due This Week | Applications requiring action this week |

Selecting a KPI filters the application list.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Application  
* Application Type  
* Project Filter  
* Property Filter  
* Status Filter  
* Priority Filter  
* Date Range  
* Reset Filters

### Application Types

* Project Registration  
* Property Registration  
* Project Amendment  
* Compliance Submission  
* Additional Information Submission  
* Other RERA Services

### Status Badges

See [status-badges.md](../status-badges.md#application-status) for the status vocabulary — including a conflict between the Principal's and the operational roles' lists.

### Priority

* High  
* Medium  
* Low

### Section 3 — Applications Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Application ID | Unique reference |
| Application Type | Service submitted |
| Related Project | Associated project |
| Related Property | Associated property (if applicable) |
| Submitted Date | Date submitted |
| Current Status | Processing stage |
| Assigned RERA Unit | Reviewing department |
| Last Updated | Latest activity |
| Action | Available actions |

### Row Actions

#### **Draft**

* Continue  
* Edit  
* Delete

#### **Submitted / Under Review**

* View Details

#### **Information Requested**

* Respond  
* Upload Documents  
* Resubmit

#### **Returned**

* Edit  
* Correct Issues  
* Resubmit

#### **Approved**

* View Details  
* Download Approval

#### **Rejected**

* View Details

### Section 4 — Pending Actions

Highlight applications requiring immediate attention.

#### **Examples**

* Additional information requested  
* Missing documents  
* Application returned  
* Submission deadline approaching  
* Supporting documents rejected

#### **Columns**

| Application | Required Action | Due Date | Priority | Action |
| :---: | :---: | :---: | :---: | :---: |

Actions

* Respond  
* Upload  
* Continue

High-priority items appear first.

### Section 5 — Recent Regulatory Activities

Display a timeline.

Examples

* Application submitted  
* Validation completed  
* RERA review started  
* Additional information requested  
* Documents uploaded  
* Application resubmitted  
* Technical review completed  
* Approval granted

Selecting an activity opens the related application.

### Empty State

#### **Message**

> No applications have been submitted yet.

Primary Button

* View Projects

Secondary Button

* Register Property

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
Applications

├── Continue Draft

├── Edit Application

├── Submit Application

├── Respond to RERA

├── Upload Documents

├── Resubmit

└── View Application Details

### Notes

* This is the **primary operational application management screen** for the **Project Registration Officer**.  
* Returned and **Information Requested** applications should automatically appear at the top of the list to ensure timely action.  
* Users should be able to continue unfinished draft applications directly from this screen.  
* All operational actions are recorded in the application's audit trail.  
* The page should emphasize actionable work rather than analytics, helping officers quickly identify what requires attention.

### Next Screen

**Application Details**

This will be the operational workspace where the Project Registration Officer can:

* Review complete application information  
* Edit draft applications  
* Upload or replace supporting documents  
* Respond to RERA information requests  
* Submit corrections  
* Resubmit returned applications  
* Track the approval workflow  
* View the complete communication history with RERA

### Sales & Disclosure Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Applications**  
* **Other Menu Items:**  
  * Dashboard  
  * Sales & Disclosures  
  * **Applications (Active)**  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Applications

**Subtitle:** Track, manage, and respond to all sales disclosure applications submitted to RERA.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Submit New Application *(Available when applicable)*

### Purpose

Provide the Sales & Disclosure Officer with an operational workspace to monitor all sales disclosure applications submitted to RERA, respond to regulatory requests, manage returned disclosures, track approval progress, and maintain full visibility over the disclosure lifecycle.

Unlike the Developer Principal's version, this screen supports operational follow-up, corrections, and resubmissions.

### Layout

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
Recent Regulatory Activities  
↓  
Pagination

### Section 1 — Application Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Applications | All sales disclosure applications |
| Draft Applications | Applications not yet submitted |
| Submitted | Successfully submitted to RERA |
| Under Review | Currently being reviewed |
| Information Requested | Awaiting additional information |
| Returned | Returned for correction |
| Approved | Successfully approved |
| Due This Week | Applications requiring action this week |

Selecting a KPI filters the application list.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Application  
* Application Type  
* Project Filter  
* Property Filter  
* Buyer Filter  
* Status Filter  
* Priority Filter  
* Date Range  
* Reset Filters

#### **Application Types**

* Sales Disclosure  
* Disclosure Amendment  
* Additional Buyer Information  
* Compliance Submission  
* Supporting Document Submission  
* Other RERA Sales Services

#### **Status Badges**

See [status-badges.md](../status-badges.md#application-status) for the status vocabulary — including a conflict between the Principal's and the operational roles' lists.

#### **Priority**

* High  
* Medium  
* Low

### Section 3 — Applications Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Application ID | Unique application reference |
| Application Type | Type of submission |
| Property | Property / Unit |
| Buyer | Buyer Name |
| Submitted Date | Submission date |
| Current Status | Processing stage |
| Assigned RERA Unit | Reviewing department |
| Last Updated | Latest activity |
| Action | Available actions |

### Row Actions

#### **Draft**

* Continue  
* Edit  
* Delete

#### **Submitted / Under Review**

* View Details

#### **Information Requested**

* Respond  
* Update Buyer Information  
* Upload Documents  
* Resubmit

#### **Returned**

* Correct Disclosure  
* Upload Documents  
* Resubmit

#### **Approved**

* View Details  
* Download Approval Summary

#### **Rejected**

* View Details

### Section 4 — Pending Actions

Highlight applications requiring immediate attention.

#### **Examples**

* Buyer information requested  
* Missing supporting documents  
* Returned disclosure  
* Submission deadline approaching  
* Identity verification pending  
* Proof of payment missing

#### **Columns**

| Application | Required Action | Due Date | Priority | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Respond  
* Upload  
* Continue

Critical items appear first.

### Section 5 — Recent Regulatory Activities

Display a timeline of the latest regulatory events.

Examples

* Sales disclosure submitted  
* Validation completed  
* RERA review started  
* Additional buyer information requested  
* Buyer documents uploaded  
* Disclosure resubmitted  
* Compliance review completed  
* Disclosure approved

Selecting an activity opens the related application.

### Empty State

**Message**

> No sales disclosure applications have been submitted yet.

Primary Button

* Record Property Sale

Secondary Button

* Create Sales Disclosure

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
Applications  
├── Continue Draft  
├── Edit Application  
├── Submit Application  
├── Respond to RERA  
├── Update Buyer Information  
├── Upload Documents  
├── Resubmit  
└── View Application Details

### Notes

* This is the **primary operational application management screen** for the **Sales & Disclosure Officer**.  
* Applications with **Information Requested** or **Returned** status should automatically appear at the top of the list to ensure timely regulatory responses.  
* Users should be able to continue unfinished draft applications directly from this screen.  
* Every submission, buyer information update, document upload, correction, and regulatory response must be recorded in the application's audit trail.  
* The page emphasizes actionable work rather than analytics, enabling officers to quickly identify pending disclosure tasks and compliance deadlines.

### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Applications**  
* **Other Menu Items:**  
  * Dashboard  
  * Escrow Management  
  * **Applications (Active)**  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Applications

**Subtitle:** Track, manage, and respond to all escrow-related applications submitted to RERA and financial institutions.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Submit New Application *(Available when applicable)*

### Purpose

Provide the Escrow Liaison with an operational workspace to manage all escrow-related applications, including escrow account registrations, fund release submissions, compliance updates, and responses to requests from RERA or financial institutions. The screen supports operational follow-up, corrections, document resubmission, and approval tracking.

### Layout

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
Recent Regulatory Activities  
↓  
Pagination

### Section 1 — Application Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Applications | All escrow-related applications |
| Draft Applications | Applications not yet submitted |
| Submitted | Successfully submitted |
| Under Review | Currently under review |
| Information Requested | Awaiting additional information |
| Returned | Returned for correction |
| Approved | Successfully approved |
| Due This Week | Applications requiring action this week |

Selecting a KPI filters the application list.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Application  
* Application Type Filter  
* Project Filter  
* Escrow Account Filter  
* Financial Institution Filter  
* Status Filter  
* Priority Filter  
* Date Range Filter  
* Reset Filters

#### **Application Types**

* Escrow Account Registration  
* Fund Release Request  
* Escrow Amendment  
* Additional Information Submission  
* Compliance Submission  
* Other Escrow Services

#### **Status Badges**

See [status-badges.md](../status-badges.md#application-status) for the status vocabulary — including a conflict between the Principal's and the operational roles' lists.

#### **Priority**

* High  
* Medium  
* Low

### Section 3 — Applications Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Application ID | Unique application reference |
| Application Type | Type of escrow service |
| Project | Related development project |
| Escrow Account | Escrow reference |
| Financial Institution | Associated bank |
| Submitted Date | Submission date |
| Current Status | Processing stage |
| Last Updated | Latest activity |
| Action | Available actions |

### Row Actions

#### **Draft**

* Continue  
* Edit  
* Delete

#### **Submitted / Under Review**

* View Details

#### **Information Requested**

* Respond  
* Upload Documents  
* Update Application  
* Resubmit

#### **Returned**

* Correct Application  
* Upload Revised Documents  
* Resubmit

#### **Approved**

* View Details  
* Download Approval

#### **Rejected**

* View Details

### Section 4 — Pending Actions

Highlight applications requiring immediate attention.

#### **Examples**

* Additional documents requested  
* Fund release application returned  
* Escrow registration pending correction  
* Bank clarification required  
* Compliance submission due  
* Milestone verification pending

#### **Columns**

| Application | Required Action | Due Date | Priority | Action |
| ----- | ----- | ----- | ----- | ----- |
| Fund Release Request | Upload Engineer Certificate | 05 Aug 2026 | High | Continue |
| Escrow Registration | Respond to Bank Query | 06 Aug 2026 | Medium | Respond |

#### **Actions**

* Respond  
* Upload  
* Continue

Critical items appear first.

### Section 5 — Recent Regulatory Activities

Display a timeline of the latest escrow-related activities.

#### **Examples**

* Escrow account registered  
* Fund release request submitted  
* Bank review started  
* Additional information requested  
* Supporting documents uploaded  
* Application resubmitted  
* RERA approval granted  
* Funds released

Selecting an activity opens the related application.

### Empty State

#### **Message**

> No escrow-related applications have been submitted yet.

**Primary Button**

* Register Escrow Account

**Secondary Button**

* Open Escrow Management

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

Open Applications  
↓  
Review application summary cards  
↓  
Search or filter escrow-related applications  
↓  
Select an application from the list  
↓  
Review the current status and required actions  
↓  
Respond to RERA or Financial Institution requests (if needed)  
↓  
Upload revised documents or update the application (when permitted)  
↓  
Resubmit the application (if required)  
↓  
Track the approval process until the application is completed

### Notes

* This screen includes only **escrow-related applications**.  
* Applications are grouped by project and escrow account for easier tracking.  
* Operational actions are available only while the application is editable.  
* Status badges and workflow behavior follow the platform's shared design system.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations).

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations). Only the Project Registration Officer's version includes a "Next Screen" preview of the Application Details screen; this is preserved verbatim in its block above.
