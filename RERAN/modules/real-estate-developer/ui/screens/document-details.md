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

# Screen: Document Details

**Roles:** Principal · Registration Officer · Sales & Disclosure Officer · Escrow Liaison

The detail view of a single document, opened from the Documents list. The Developer Principal / Director sees a read-only master viewer; the three operational roles (Registration Officer, Sales & Disclosure Officer, Escrow Liaison) see an editable operational workspace for managing that document through its verification lifecycle.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Documents**
* **Selected Item:** Document Details *(opened from Documents list)*
* **Top Bar Title:** Document Details
* **Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

Which sidebar menu items are visible, the subtitle, top-bar page actions, and the layout diagram differ by role — see [Role Variations](#role-variations). As with Application Details, the Escrow Liaison's layout is structurally different from the other three: it organizes the body into **tabs** (Preview, Information, Linked Records, Verification Summary, Version History, RERA / Bank Queries, Communication History, Activity Timeline) rather than stacked numbered sections.

## Sections

Every section (Document Header, Document Preview, Document Information, Linked Records, verification/review content, Version History, query and communication tables, and the Activity Timeline) is role-specific — see [Role Variations](#role-variations).

## Empty State

Differs by role — and not just in wording. For the Principal, Registration Officer, and Sales & Disclosure Officer, the "Empty State" describes a document that has just been uploaded or created and is awaiting verification. For the Escrow Liaison, it describes a **record-not-found** error state, the same pattern seen on that role's Application Details screen — a different concept entirely, not a reworded version of the same one. See [Role Variations](#role-variations).

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Documents**  
* **Selected Item:** Document Details *(opened from Documents list)*  
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

**Title:** Document Details

**Subtitle:** Review document information, verification status, version history, and linked regulatory records.

**Search Bar:** Search anything...

**Page Actions (Right Side):**

* Download Document  
* View Linked Record  
* Share Link *(Internal Only)*

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a complete, read-only view of an individual document, including its metadata, verification status, approval history, related records, and version history.

### Layout

Top Bar  
↓  
Document Header  
↓  
Document Summary Cards  
↓  
Document Preview  
↓  
Document Information  
↓  
Linked Records  
↓  
Verification Details  
↓  
Version History  
↓  
Review History  
↓  
Activity Timeline

### Section 1 — Document Header

Displays key document information.

#### **Left**

* Document Name  
* Category  
* Verification Status Badge

#### **Right**

* Uploaded Date  
* Uploaded By  
* Latest Version

### Section 2 — Document Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| Verification Status | Current review status |
| Document Version | Latest version number |
| Expiry Status | Valid / Expiring / Expired |
| Linked Records | Number of associated records |
| Last Reviewed | Most recent verification date |
| Compliance Status | Compliant / Action Required |

### Section 3 — Document Preview

The primary content area of the page.

#### **Features**

* Embedded document viewer  
* Zoom In / Zoom Out  
* Fit to Width  
* Rotate  
* Page Navigation  
* Full Screen  
* Download

Supported document formats include:

* PDF  
* Images  
* Office Documents  
* CAD drawings (where supported)  
* Other supported regulatory attachments

### Section 4 — Document Information

Two-column information card.

#### **Basic Information**

* Document Name  
* Document ID  
* Category  
* File Type  
* File Size  
* Upload Date  
* Uploaded By

#### **Administrative Information**

* Verification Status  
* Expiry Date  
* Required By Regulation  
* Current Version  
* Storage Location  
* Document Owner

### Section 5 — Linked Records

Shows where this document is being used.

Possible linked records include:

* Project  
* Property Registration  
* Sales Disclosure  
* Escrow Account  
* Regulatory Application  
* Company Profile  
* License  
* Compliance Submission

#### **Table Columns**

| Column | Description |
| ----- | ----- |
| Record Type | Type of record |
| Reference Number | Record ID |
| Current Status | Record status |
| Action | View Record |

### Section 6 — Verification Details

Displays verification information.

#### **Information**

* Verification Status  
* Verified By  
* Verification Date  
* Verification Method  
* Compliance Outcome  
* Remarks

If verification is pending, display:

> Waiting for regulatory verification.

### Section 7 — Version History

Table showing all versions.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Version | Version number |
| Uploaded By | User |
| Upload Date | Date |
| Change Summary | Description of update |
| Status | Active / Archived |
| Action | View Version |

The latest version is clearly identified.

### Section 8 — Review History

Displays every regulatory review performed.

#### **Columns**

* Review Date  
* Reviewer  
* Review Type  
* Outcome  
* Remarks

Examples

* Initial Verification  
* Compliance Review  
* Updated Version Accepted  
* Final Verification

### Section 9 — Activity Timeline

Chronological activity log.

Examples

* Document uploaded  
* Version 2 uploaded  
* Verification requested  
* Verification completed  
* Linked to Project Registration  
* Used in Escrow Application  
* Downloaded by authorized user

Latest activities appear first.

### Empty State

If the document has not yet been reviewed:

**Message**

> This document has been uploaded successfully and is awaiting verification.

Primary Button

* Return to Documents

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Documents  
↓  
Document Details

├── Preview Document

├── View Linked Record

├── View Previous Versions

├── Review Verification Details

└── Download Document

### Notes

* This is the **master document viewer** for the **Developer Principal / Director**.  
* The page supports every document type stored in the RERA platform.  
* All information is presented in **read-only mode**.  
* The embedded document viewer allows executives to inspect documents without downloading them, while maintaining secure access controls and a complete audit trail.

### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Documents**  
* **Selected Item:** Document Details *(opened from Documents list)*  
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

**Title:** Document Details

**Subtitle:** Review, update, and manage this document throughout the regulatory verification process.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Changes *(Enabled when edits are made)*  
* Upload New Version  
* More Actions

### Purpose

Provide the Project Registration Officer with a complete operational workspace for managing an individual document. The officer can preview the document, update metadata, replace uploaded files, submit revised versions, respond to RERA verification requests, review version history, and track all document-related activities.

Unlike the Developer Principal's version, this page is fully interactive and supports document lifecycle management.

### Layout

Top Bar  
↓  
Document Header  
↓  
Verification Progress  
↓  
Document Preview  
↓  
Document Information  
↓  
Linked Records  
↓  
Verification Summary  
↓  
Version History  
↓  
RERA Queries (If Applicable)  
↓  
Activity Timeline

### Section 1 — Document Header

Displays high-level document information.

#### **Left**

* Document Name  
* Document Category  
* Verification Status Badge  
* Linked Record Reference

#### **Right**

* Uploaded Date  
* Last Updated  
* Uploaded By  
* Save Status

### Section 2 — Verification Progress

Display a horizontal workflow tracker.

#### **Stages**

* Draft  
* Uploaded  
* Submitted for Verification  
* Under Review  
* Information Requested *(If Applicable)*  
* Verified  
* Completed

Completed stages use the platform's standard success indicator.

The current stage is highlighted.

Completed stages are clickable for quick navigation.

### Section 3 — Document Preview

Primary viewing area.

#### **Features**

* Embedded document viewer  
* Zoom In / Zoom Out  
* Fit to Width  
* Rotate  
* Page Navigation  
* Full Screen  
* Download

Supported formats

* PDF  
* Images  
* Microsoft Office Documents  
* CAD Drawings *(where supported)*  
* Other approved attachment formats

The preview updates immediately after a replacement or new version is uploaded.

### Section 4 — Document Information

Editable while the document is in **Draft**, **Returned**, or **Information Requested** status.

### **Basic Information**

* Document Name  
* Category  
* Document Type  
* Description  
* Related Project  
* Related Property *(if applicable)*  
* Related Application *(if applicable)*

### **File Information *(Read-only)***

* File Name  
* File Type  
* File Size  
* Upload Date  
* Uploaded By  
* Current Version

### **Administrative Information**

* Expiry Date *(if applicable)*  
* Mandatory Document  
* Verification Status  
* Submission Status

### Section 5 — Linked Records

Displays every record associated with the document.

Possible linked records include:

* Development Project  
* Property Registration  
* Regulatory Application  
* Supporting Submission

#### **Table**

| Record Type | Reference | Status | Action |
| ----- | ----- | ----- | ----- |
| Project | PRJ-001245 | Approved | View |
| Property Registration | PROP-00987 | Under Review | View |
| Application | APP-00452 | Submitted | View |

Selecting **View** opens the related record.

### Section 6 — Verification Summary

Displays automated and regulatory verification results.

#### **Automatic Validation**

See [validation-rules.md](../validation-rules.md#document-upload-rules) for the file-integrity check list — including a conflict between this role's version and the other two operational roles'.

#### **Regulatory Verification**

See [status-badges.md](../status-badges.md#document-status) ("Document Details screen — Regulatory Verification" subsection) for the status vocabulary — the source uses three different, unreconciled vocabularies for document status; see that section for all three.

Display results using:

* ✅ Passed  
* ⚠ Warning  
* ❌ Failed

If validation fails, selecting the issue scrolls directly to the affected field or upload section.

### Section 7 — Version History

Maintain a complete history of every uploaded version.

#### **Table**

| Version | Uploaded By | Upload Date | Change Summary | Status | Action |
| :---: | :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* View Version  
* Compare Versions  
* Download Version

The latest version is clearly marked as **Current**.

### Section 8 — RERA Queries

Visible only when RERA requests clarification or replacement.

#### **Table**

| Date | Request | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Replace Document  
* Upload Additional File  
* Submit Response  
* View Previous Response

Outstanding requests appear with high-priority highlighting.

### Section 9 — Activity Timeline

Displays every document-related event.

Examples

* Document created  
* Metadata updated  
* File uploaded  
* New version uploaded  
* Submitted for verification  
* Verification started  
* Information requested  
* Replacement uploaded  
* Verified  
* Linked to application

Latest activities appear first.

### Empty State

If the document has just been created:

**Message**

> Upload the required document and complete its information before submitting it for verification.

Primary Button

* Upload Document

Secondary Button

* Complete Document Information

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Documents  
↓  
Document Details

├── Edit Document Information

├── Upload / Replace File

├── Save Changes

├── Upload New Version

├── Submit for Verification

├── Respond to RERA Query

└── View Version History

### Notes

* This is the **primary operational document management screen** for the **Project Registration Officer**.  
* Document metadata can be edited while the document is in **Draft**, **Returned**, or **Information Requested** status.  
* Every replacement creates a new version while preserving previous versions for audit purposes.  
* The embedded viewer allows officers to verify uploaded content before submission without downloading the file.  
* All uploads, replacements, verification requests, responses, and approvals are automatically recorded in the activity timeline.  
* A document cannot be marked as ready for submission if mandatory validation checks fail or required metadata is incomplete.

### Next Screen

**Reports**

This will be the Project Registration Officer's reporting workspace, allowing officers to generate and export operational reports related to:

* Project Registrations  
* Property Registrations  
* Regulatory Applications  
* Document Status  
* Registration Performance  
* Pending Tasks  
* Approval Progress  
* Submission History

### Sales & Disclosure Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Documents**  
* **Selected Item:** Document Details *(opened from Documents list)*  
* **Other Menu Items:**  
  * Dashboard  
  * Sales & Disclosures  
  * Applications  
  * **Documents (Active)**  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Document Details

**Subtitle:** Review, update, and manage this document throughout the sales disclosure verification process.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Changes *(Enabled when edits are made)*  
* Upload New Version  
* More Actions

### Purpose

Provide the Sales & Disclosure Officer with a complete operational workspace for managing an individual sales-related document. The officer can preview documents, update metadata, replace uploaded files, upload revised versions, respond to RERA verification requests, review version history, and track all document activities throughout the disclosure lifecycle. This screen is fully interactive and supports document lifecycle management for sales disclosures.

### Layout

Top Bar  
↓  
Document Header  
↓  
Verification Progress  
↓  
Document Preview  
↓  
Document Information  
↓  
Linked Records  
↓  
Verification Summary  
↓  
Version History  
↓  
RERA Queries (If Applicable)  
↓  
Communication History  
↓  
Activity Timeline

### Section 1 — Document Header

Displays the document overview.

#### **Left**

* Document Name  
* Document Category  
* Verification Status Badge  
* Linked Sales Reference

#### **Right**

* Uploaded Date  
* Last Updated  
* Uploaded By  
* Save Status

### Section 2 — Verification Progress

Display a horizontal workflow tracker.

#### **Stages**

* Draft  
* Uploaded  
* Submitted for Verification  
* Under Review  
* Information Requested *(If Applicable)*  
* Verified  
* Completed

Completed stages use the platform's standard success indicator.

The current stage is highlighted.

Completed stages are clickable for quick navigation.

### Section 3 — Document Preview

Primary document viewing area.

#### **Features**

* Embedded Document Viewer  
* Zoom In / Zoom Out  
* Fit to Width  
* Rotate  
* Page Navigation  
* Full Screen  
* Download

#### **Supported Formats**

* PDF  
* Images  
* Microsoft Office Documents  
* Scanned Identification Documents  
* Other approved attachment formats

The preview refreshes automatically after a replacement or new version is uploaded.

### Section 4 — Document Information

Editable while the document is in **Draft**, **Returned**, or **Information Requested** status.

### **Basic Information**

* Document Name  
* Category  
* Document Type  
* Description  
* Related Project  
* Related Property  
* Related Buyer  
* Related Sales Disclosure  
* Related Application *(if applicable)*

### **File Information *(Read-only)***

* File Name  
* File Type  
* File Size  
* Upload Date  
* Uploaded By  
* Current Version

### **Administrative Information**

* Expiry Date *(if applicable)*  
* Mandatory Document  
* Verification Status  
* Submission Status

### Section 5 — Linked Records

Displays every record associated with this document.

Possible linked records include:

* Property Sale  
* Buyer  
* Sales Disclosure  
* Sales Disclosure Application  
* Property Registration  
* Development Project

#### **Table**

| Record Type | Reference | Status | Action |
| ----- | ----- | ----- | ----- |
| Property Sale | SALE-001245 | Completed | View |
| Buyer | BUY-00451 | Verified | View |
| Sales Disclosure | DISC-00087 | Under Review | View |
| Application | APP-00354 | Submitted | View |

Selecting **View** opens the related record.

### Section 6 — Verification Summary

Displays both automatic and regulatory verification results.

#### **Automatic Validation**

See [validation-rules.md](../validation-rules.md#document-upload-rules) for the file-integrity check list — including a conflict with the Registration Officer's shorter version of this same check list.

#### **Regulatory Verification**

See [status-badges.md](../status-badges.md#document-status) ("Document Details screen — Regulatory Verification" subsection) for the status vocabulary — the source uses three different, unreconciled vocabularies for document status; see that section for all three.

Display results using:

* ✅ Passed  
* ⚠ Warning  
* ❌ Failed

Selecting a validation issue scrolls directly to the affected field or upload section.

### Section 7 — Version History

Maintain a complete history of uploaded versions.

#### **Table**

| Version | Uploaded By | Upload Date | Change Summary | Status | Action |
| :---: | :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* View Version  
* Compare Versions  
* Download Version

The latest version is clearly marked as **Current Version**.

### Section 8 — RERA Queries

Visible only when RERA requests clarification or replacement.

#### **Table**

| Date | Request | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Replace Document  
* Upload Additional File  
* Update Buyer Information *(if applicable)*  
* Submit Response  
* View Previous Response

Outstanding requests appear with high-priority highlighting.

### Section 9 — Communication History

Conversation thread between the Sales & Disclosure Officer and RERA.

Each message displays:

* Sender  
* Date & Time  
* Message  
* Attachments  
* Status

#### **Actions**

* Reply *(when permitted)*  
* View Attachment

Messages are displayed chronologically.

### Section 10 — Activity Timeline

Displays every document-related activity.

Examples

* Document created  
* Metadata updated  
* File uploaded  
* New version uploaded  
* Submitted for verification  
* Verification started  
* Information requested  
* Replacement uploaded  
* Buyer information updated  
* Document verified  
* Linked to disclosure application

Latest activities appear first.

### Empty State

If the document has just been created:

**Message**

> Upload the required buyer or transaction document and complete its information before submitting it for verification.

**Primary Button**

* Upload Document

**Secondary Button**

* Complete Document Information

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Documents  
↓  
Document Details

├── Edit Document Information

├── Upload / Replace File

├── Save Changes

├── Upload New Version

├── Submit for Verification

├── Respond to RERA Query

├── Update Buyer Information

└── View Version History

### Notes

* This is the **primary operational document management screen** for the **Sales & Disclosure Officer**.  
* The page supports the complete lifecycle of buyer and transaction documents, including upload, replacement, verification, and resubmission.  
* Documents can be linked to **Property Sales, Buyers, Sales Disclosures, and Sales Disclosure Applications**, ensuring complete traceability throughout the disclosure process.  
* Version history must be preserved for every replacement to provide a full regulatory audit trail.  
* The **Submit for Verification** action remains disabled until all mandatory validations pass.  
* Personally identifiable buyer information should be protected according to the platform's security and privacy requirements.

### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Documents**  
* **Selected Item:** **Document Details** *(opened from Documents list)*  
* **Other Menu Items:**  
  * Dashboard  
  * Escrow Management  
  * Applications  
  * **Documents (Active)**  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Document Details

**Subtitle:** Review, update, and manage escrow documents throughout the verification and approval process.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Changes *(Enabled when edits are made)*  
* Upload New Version  
* More Actions

### Purpose

Provide the Escrow Liaison with a complete operational workspace for managing an individual escrow-related document. The liaison can preview documents, upload revised versions, review verification results, respond to RERA or Financial Institution requests, track version history, and monitor every document-related activity throughout the escrow lifecycle.

### Layout

Top Bar  
↓  
Document Header  
↓  
Information Tabs

    ├─ Preview

    ├─ Information

    ├─ Linked Records

    ├─ Verification Summary

    ├─ Version History

    ├─ RERA / Bank Queries

    ├─ Communication History

    └─ Activity Timeline

### Section 1 — Document Header

Displays the document overview.

#### **Left**

* Document Name  
* Document Category  
* Verification Status Badge  
* Linked Escrow Reference

#### **Right**

* Uploaded Date  
* Last Updated  
* Uploaded By  
* Save Status

### Tab 1 — Preview

Primary document viewing area.

#### **Features**

* Embedded Document Viewer  
* Zoom In / Zoom Out  
* Fit to Width  
* Rotate  
* Page Navigation  
* Full Screen  
* Download

#### **Supported Formats**

* PDF  
* Images  
* Microsoft Office Documents  
* CAD Drawings *(where supported)*  
* Other approved attachment formats

The preview refreshes automatically whenever a revised version is uploaded.

### Tab 2 — Information

Editable while the document is in **Draft**, **Returned**, or **Information Requested** status.

#### **Basic Information**

* Document Name  
* Category  
* Document Type  
* Description  
* Related Project  
* Related Escrow Account  
* Related Fund Release Request  
* Related Application *(if applicable)*

#### **File Information *(Read-only)***

* File Name  
* File Type  
* File Size  
* Upload Date  
* Uploaded By  
* Current Version

#### **Administrative Information**

* Expiry Date *(if applicable)*  
* Mandatory Document  
* Verification Status  
* Submission Status

### Tab 3 — Linked Records

Displays every record associated with this document.

Possible linked records include:

* Escrow Account  
* Fund Release Request  
* Escrow Application  
* Development Project  
* Financial Institution Submission

#### **Table**

| Record Type | Reference | Status | Action |
| ----- | ----- | ----- | ----- |
| Escrow Account | ESC-000254 | Active | View |
| Fund Release | FR-000078 | Under Review | View |
| Application | APP-001246 | Submitted | View |

#### **Actions**

* View Record

### Tab 4 — Verification Summary

Displays automatic and regulatory verification results.

#### **Automatic Validation**

See [validation-rules.md](../validation-rules.md#document-upload-rules) for the file-integrity check list — including a conflict with the Registration Officer's shorter version of this same check list.

#### **Regulatory Verification**

See [status-badges.md](../status-badges.md#document-status) ("Document Details screen — Regulatory Verification" subsection) for the status vocabulary — the source uses three different, unreconciled vocabularies for document status; see that section for all three.

Display results using:

* ✅ Passed  
* ⚠ Warning  
* ❌ Failed

Selecting a validation issue scrolls directly to the relevant section.

### Tab 5 — Version History

Maintain a complete history of uploaded versions.

#### **Table**

| Version | Uploaded By | Upload Date | Change Summary | Status | Action |
| :---: | :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* View Version  
* Compare Versions  
* Download Version

The latest version is clearly identified as **Current Version**.

### Tab 6 — RERA / Bank Queries

Visible only when additional information has been requested.

#### **Table**

| Date | Request | Requested By | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Respond  
* Upload Revised Document  
* Submit Response  
* View Previous Response

Outstanding requests are highlighted until resolved.

### Tab 7 — Communication History

Displays the complete communication log.

Each conversation includes:

* Sender  
* Organization  
* Date & Time  
* Message  
* Attachments  
* Status

#### **Actions**

* Reply *(when permitted)*  
* View Attachments  
* Download Attachments

### Tab 8 — Activity Timeline

Displays every activity performed on the document.

Examples

* Document uploaded  
* Metadata updated  
* Submitted for verification  
* Financial institution review started  
* RERA review started  
* Information requested  
* Revised version uploaded  
* Verification completed  
* Document approved  
* Document rejected

Each activity displays:

* Date & Time  
* User  
* Description  
* Status

### Empty State

#### **Message**

> The requested document could not be found or is no longer available.

**Primary Button**

* Back to Documents

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Documents  
    ↓  
Search / Filter Documents  
    ↓  
Select Document  
    ↓  
Review Document Preview  
    ↓  
Review Document Information  
    ↓  
Check Verification Summary  
    ↓  
Review Version History  
    ↓  
Respond to RERA / Bank Queries (If Required)  
    ↓  
Upload Revised Version (If Required)  
    ↓  
Save Changes / Submit Response

### Notes

* Editing is permitted only while the document is in an editable status (Draft, Returned, or Information Requested).  
* Every uploaded revision creates a new document version while preserving the complete audit trail.  
* All communications with RERA and Financial Institutions are recorded in the Communication History.  
* The screen follows the standardized **Information Tabs** pattern used across all operational detail pages in the platform.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations). The Escrow Liaison's is a single linear arrow diagram describing the review procedure rather than the Dashboard-rooted tree diagrams used by the other three roles.

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations). Only the Project Registration Officer's version includes a "Next Screen" preview of the Reports screen; this is preserved verbatim in its block above.
