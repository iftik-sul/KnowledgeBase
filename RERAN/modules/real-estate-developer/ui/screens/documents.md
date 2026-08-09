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

# Screen: Documents

**Roles:** Principal · Registration Officer · Escrow Liaison

A list of documents scoped to the viewing role. The Developer Principal / Director sees a read-only, organization-wide repository; the Registration Officer and Escrow Liaison each see an operational workspace scoped to their own document categories, with the ability to upload, replace, and resubmit documents.

> **Sales & Disclosure Officer:** not documented here. The source material has no top-level Documents screen for this role — see the open question in [../README.md](../README.md). During Batch 2 migration, a `## Screen: Documents` fragment for the Sales & Disclosure Officer was found nested at the wrong heading level inside that role's Application Details section (source lines 9218–9475); it was left untouched there and is not included in this merge, per this issue's instruction not to silently correct the matrix.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Documents**
* **Top Bar Title:** Documents
* **Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

Which sidebar menu items are visible, the subtitle, top-bar page actions, and the layout diagram differ by role — see [Role Variations](#role-variations). The layout diagram is identical for the Registration Officer and Escrow Liaison (Document Summary Cards → Filters & Search → Documents Table → **Pending Verification** → Recent Document Activity → Pagination); the Principal's differs by substituting **Document Analytics** for Pending Verification, reflecting the read-only nature of that role's screen.

## Sections

Every section (Document Summary Cards, Filters, the Documents Table and its Row Actions, Pending Verification / Document Analytics, and Recent Document Activity) is role-specific — see [Role Variations](#role-variations).

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations).

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Documents**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * Sales & Disclosures  
  * Escrow Management  
  * Applications  
  * **Documents (Active)**  
  * Reports  
  * Company Profile  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Documents

**Subtitle:** Access and monitor all organization documents submitted to RERA across projects and regulatory processes.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a centralized repository of all organizational documents. This page enables executives to quickly locate documents, verify their approval status, monitor expirations, review version history, and access files associated with projects, registrations, sales, escrow, and regulatory applications.

### Layout

Top Bar  
↓  
Document Summary Cards  
↓  
Filters & Search  
↓  
Documents Table  
↓  
Document Analytics  
↓  
Recent Document Activity  
↓  
Pagination

### Section 1 — Document Summary Cards

Display eight KPI cards.

| KPI | Description |
| ----- | ----- |
| Total Documents | All documents in the organization |
| Verified Documents | Successfully verified |
| Pending Verification | Awaiting review |
| Rejected Documents | Verification failed |
| Expiring Soon | Documents nearing expiry |
| Expired Documents | Already expired |
| Recently Uploaded | Uploaded in the last 30 days |
| Document Categories | Total document categories |

Selecting a KPI filters the table automatically.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Document Name  
* Category Filter  
* Project Filter  
* Application Type Filter  
* Verification Status Filter  
* Expiry Status Filter  
* Uploaded By Filter  
* Date Range Filter  
* Reset Filters

### Document Categories

* Company Documents  
* Project Documents  
* Property Registration Documents  
* Sales Disclosure Documents  
* Escrow Documents  
* Regulatory Certificates  
* Licenses & Permits  
* Legal Agreements  
* Financial Documents  
* Compliance Documents  
* Other

### Verification Status

See [status-badges.md](../status-badges.md#document-status) for the status vocabulary — the source uses three different, unreconciled vocabularies for document status; see that section for all three.

### Expiry Status

See [status-badges.md](../status-badges.md#document-status) ("Expiry Status" subsection).

### Section 3 — Documents Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Document Name | Name of the document |
| Category | Document classification |
| Linked Record | Related project/application/property |
| Uploaded By | Employee |
| Upload Date | Submission date |
| Expiry Date | If applicable |
| Verification Status | Current verification |
| Action | View Details |

### Row Actions

Each row includes:

* View Details

No editing or uploading is permitted from this screen.

### Section 4 — Document Analytics

Display two analytics cards.

### **Repository Overview**

* Total Storage Used  
* Total Documents  
* Average File Size  
* Most Used Category

### **Compliance Overview**

* Verification Rate  
* Documents Expiring This Month  
* Missing Required Documents  
* Compliance Score

### Section 5 — Recent Document Activity

Timeline widget.

Examples

* Project Plan Uploaded  
* Escrow Agreement Verified  
* Sales Disclosure Returned  
* Building Permit Approved  
* Company License Renewed  
* Compliance Certificate Issued

Each activity displays:

* Document Name  
* Related Record  
* Date & Time  
* Status

Selecting an activity opens the document.

### Empty State

#### **Message**

> No documents are available in the repository.

Primary Button

* View Projects

Secondary Button

* View Applications

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
Documents  
↓  
Search / Filter Documents  
↓  
Select Document  
↓  
Document Details

### Notes

* This is a **centralized document repository** for the **Developer Principal / Director**.  
* It aggregates documents from every operational module into a single searchable interface.  
* Users can monitor document completeness, verification status, and expiry without navigating between multiple modules.  
* Uploading, replacing, or deleting documents is handled by the responsible operational teams according to their permissions.

### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Documents**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * Applications  
  * **Documents (Active)**  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Documents

**Subtitle:** Upload, organize, and manage documents required for project registrations, property registrations, and regulatory applications.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Upload Documents

### Purpose

Provide the Project Registration Officer with an operational document management workspace where all documents required for projects, property registrations, and applications can be uploaded, replaced, tracked, and maintained throughout the registration lifecycle.

Unlike the Developer Principal's version, this page supports full document management.

### Layout

Top Bar  
↓  
Document Summary Cards  
↓  
Filters & Search  
↓  
Documents Table  
↓  
Pending Verification  
↓  
Recent Document Activity  
↓  
Pagination

### Section 1 — Document Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Documents | All uploaded documents |
| Draft Documents | Uploaded but not submitted |
| Pending Verification | Awaiting RERA verification |
| Verified Documents | Successfully verified |
| Returned Documents | Require replacement or correction |
| Rejected Documents | Failed verification |
| Missing Required Documents | Mandatory documents not yet uploaded |
| Expiring Documents | Documents nearing expiry |

Selecting a KPI filters the table.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Document  
* Category Filter  
* Project Filter  
* Property Filter  
* Application Filter  
* Verification Status  
* Upload Date Range  
* Reset Filters

### Document Categories

* Company Documents  
* Project Documents  
* Property Registration Documents  
* Technical Documents  
* Survey Documents  
* Building Approval Documents  
* Environmental Documents  
* Compliance Documents  
* Supporting Documents  
* Other

### Verification Status

See [status-badges.md](../status-badges.md#document-status) for the status vocabulary — the source uses three different, unreconciled vocabularies for document status; see that section for all three.

### Section 3 — Documents Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Document Name | Uploaded document |
| Category | Document category |
| Linked Record | Project / Property / Application |
| Uploaded By | Officer |
| Upload Date | Date uploaded |
| Verification Status | Current status |
| Expiry Date | If applicable |
| Action | Available actions |

### Row Actions

#### **Draft**

* Edit Details  
* Replace  
* Preview  
* Delete

#### **Pending Verification**

* Preview  
* View Details

#### **Information Requested / Returned**

* Replace Document  
* Upload Revised Version  
* Preview  
* Resubmit

#### **Verified**

* View  
* Download

#### **Rejected**

* View Remarks  
* Replace Document

### Section 4 — Pending Verification

Displays documents requiring immediate attention.

#### **Examples**

* Missing mandatory documents  
* Returned verification  
* Expiring approvals  
* Incorrect document format  
* Low-quality scan  
* Signature missing

#### **Columns**

| Document | Issue | Due Date | Priority | Action |
| :---: | :---: | :---: | :---: | :---: |

Actions

* Upload  
* Replace  
* Continue

Items nearing deadline appear first.

### Section 5 — Recent Document Activity

Timeline showing recent document events.

Examples

* Document uploaded  
* Document replaced  
* Verification started  
* Information requested  
* Revised document uploaded  
* Document verified  
* Document rejected

Selecting an activity opens the corresponding document.

### Empty State

**Message**

> No documents have been uploaded yet. Upload the required documents to support your project registrations and regulatory applications.

Primary Button

* Upload Documents

Secondary Button

* View Projects

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
Documents

├── Upload Document

├── Replace Document

├── Preview Document

├── Submit Revised Version

├── Download Verified Document

└── View Document Details

### Notes

* This is the **primary operational document management screen** for the **Project Registration Officer**.  
* Documents can be linked to **Projects, Property Registrations, or Applications**, allowing one repository to support the entire registration workflow.  
* Returned or **Information Requested** documents should automatically appear at the top of the list so officers can respond quickly.  
* Version history should be preserved whenever a document is replaced to maintain a complete audit trail.  
* Mandatory document requirements should be validated automatically before a Project, Property Registration, or Application can be submitted to RERA.

### Next Screen

**Document Details**

This screen will be the Project Registration Officer's operational workspace for a single document, allowing the officer to:

* Preview the document  
* Edit document metadata  
* Replace uploaded files  
* Upload new versions  
* View verification results  
* Respond to RERA document requests  
* Review version history  
* Track document activity and audit history

### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Documents**  
* **Other Menu Items:**  
  * Dashboard  
  * Escrow Management  
  * Applications  
  * **Documents (Active)**  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Documents

**Subtitle:** Upload, organize, and manage escrow documents, milestone verification records, and financial institution submissions.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Upload Documents

### Purpose

Provide the Escrow Liaison with an operational document management workspace where all escrow-related documents can be uploaded, replaced, tracked, and maintained throughout the escrow account and fund release lifecycle.

Unlike the Developer Principal's version, this screen supports complete document management for escrow operations.

### Layout

Top Bar  
↓  
Document Summary Cards  
↓  
Filters & Search  
↓  
Documents Table  
↓  
Pending Verification  
↓  
Recent Document Activity  
↓  
Pagination

### Section 1 — Document Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Documents | All uploaded escrow documents |
| Draft Documents | Saved but not submitted |
| Pending Verification | Awaiting bank or RERA verification |
| Verified Documents | Successfully verified |
| Returned Documents | Require correction or replacement |
| Rejected Documents | Failed verification |
| Missing Required Documents | Mandatory documents not yet uploaded |
| Expiring Documents | Documents nearing expiry |

Selecting a KPI filters the document list.

### Section 2 — Filters

Located above the table.

#### **Components**

* Search Document  
* Category Filter  
* Project Filter  
* Escrow Account Filter  
* Fund Release Filter  
* Financial Institution Filter  
* Verification Status Filter  
* Upload Date Range  
* Reset Filters

#### **Document Categories**

* Escrow Agreement  
* Bank Confirmation Letter  
* Engineer Progress Certificate  
* Quantity Surveyor Report  
* Construction Progress Report  
* Site Inspection Report  
* Fund Release Documents  
* Financial Statements  
* Compliance Documents  
* Supporting Documents  
* Other

#### **Verification Status**

See [status-badges.md](../status-badges.md#document-status) for the status vocabulary — the source uses three different, unreconciled vocabularies for document status; see that section for all three.

### Section 3 — Documents Table

#### **Columns**

| Column | Description |
| ----- | ----- |
| Document Name | Uploaded document |
| Category | Document category |
| Linked Record | Escrow Account / Fund Release / Application |
| Financial Institution | Associated bank |
| Uploaded By | Officer |
| Upload Date | Date uploaded |
| Verification Status | Current status |
| Expiry Date | If applicable |
| Action | Available actions |

### Row Actions

#### **Draft**

* Edit Details  
* Replace  
* Preview  
* Delete

#### **Pending Verification**

* Preview  
* View Details

#### **Information Requested / Returned**

* Replace Document  
* Upload Revised Version  
* Preview  
* Resubmit

#### **Verified**

* View  
* Download

#### **Rejected**

* View Remarks  
* Replace Document

### Section 4 — Pending Verification

Displays documents requiring immediate attention.

#### **Examples**

* Missing Engineer Certificate  
* Quantity Surveyor report requires correction  
* Bank confirmation pending  
* Construction progress report returned  
* Expiring escrow agreement  
* Missing photographic evidence

#### **Columns**

| Document | Issue | Due Date | Priority | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Upload  
* Replace  
* Continue

High-priority items appear first.

### Section 5 — Recent Document Activity

Timeline showing recent document events.

#### **Examples**

* Escrow agreement uploaded  
* Engineer certificate submitted  
* Quantity Surveyor report replaced  
* Verification started  
* Additional information requested  
* Revised document uploaded  
* Document verified  
* Document rejected

Selecting an activity opens the corresponding document.

### Empty State

#### **Message**

> No escrow documents have been uploaded yet. Upload the required documents to support escrow registration and fund release requests.

**Primary Button**

* Upload Documents

**Secondary Button**

* View Escrow Management

### Pagination

Located at the bottom of the table.

#### **Components**

* Rows per page  
* Previous  
* Next  
* Page Number  
* Total Records

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Open Documents  
↓  
Review document summary cards  
↓  
Search or filter escrow documents  
↓  
Upload new documents or replace returned documents  
↓  
Preview documents before submission  
↓  
Resubmit revised documents if requested  
↓  
Monitor verification status  
↓  
Open Document Details when additional action is required

### Notes

* Only escrow-related documents are displayed.  
* Documents are linked to Escrow Accounts, Fund Release Requests, and Applications.  
* Editing and replacement are available only while the document is in an editable status.  
* Verification statuses are synchronized with both Financial Institution and RERA review workflows.  
* Uses the platform's shared document management components and status indicators.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations). The Escrow Liaison's is a single linear arrow diagram rooted at Documents itself rather than the Dashboard-rooted tree diagrams used by the other two roles.

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations). Only the Project Registration Officer's version includes a "Next Screen" preview of Document Details; this is preserved verbatim in its block above.
