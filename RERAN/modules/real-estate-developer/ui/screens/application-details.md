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

# Screen: Application Details

**Roles:** Principal · Registration Officer · Sales & Disclosure Officer · Escrow Liaison

The detail view of a single application, opened from [Applications](applications.md). The Developer Principal / Director sees a read-only view; the three operational roles (Registration Officer, Sales & Disclosure Officer, Escrow Liaison) see an editable operational workspace scoped to their own application type.

> **Migration note:** in the source material, the Sales & Disclosure Officer's Application Details section (lines 8881–9475) appears far larger than the other three roles' (~275–315 lines each). Once fully read, most of that size is a separate **Documents** (list) screen that is nested under this section at the wrong heading level (`## Screen: Documents` instead of a new `# Screen:` heading) rather than genuine Application Details content. Excluding that misplaced screen, the Sales & Disclosure Officer's actual Application Details content is ~335 lines — comparable to the other three roles. See the report for details; the misplaced Documents content is out of scope for this batch and untouched.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Applications**
* **Selected Item:** Application Details *(opened from Applications list)*
* **Top Bar Title:** Application Details
* **Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

Which sidebar menu items are visible, the subtitle, top-bar page actions, and the layout diagram differ by role — see [Role Variations](#role-variations). The Escrow Liaison's layout is structurally different from the other three: it organizes the body into **tabs** (Overview, Escrow Information, Supporting Documents, Validation Summary, RERA / Bank Queries, Communication History, Activity Timeline) rather than the stacked numbered sections used by the Principal, Registration Officer, and Sales & Disclosure Officer.

## Sections

Every section (Application Header, the information cards, Related Project & Property, role-specific detail blocks, Supporting/Submitted Documents, review or query tables, Communication History, and the Activity Timeline) is role-specific — see [Role Variations](#role-variations).

## Empty State

Differs by role — and not just in wording. For the Principal, Registration Officer, and Sales & Disclosure Officer, the "Empty State" describes an application still in **Draft** that has not yet been submitted. For the Escrow Liaison, it describes a **record-not-found** error state when the application cannot be located — a different concept entirely, not a reworded version of the same one. See [Role Variations](#role-variations).

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Validation

Only the three operational roles (Registration Officer, Sales & Disclosure Officer, Escrow Liaison) have a Validation Summary section — the Principal's version is read-only and has none. See each role's "Validation Summary" block under [Role Variations](#role-variations). Across all three, the pattern is the same in substance (automatic pre-submission checks, displayed as Passed / Warning / Error, with the primary submit button disabled until all mandatory checks pass) but the specific checks listed differ by role and are preserved verbatim per role rather than merged, since the checks are the actual business rule.

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Applications**  
* **Selected Item:** Application Details *(opened from Applications list)*  
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

**Title:** Application Details

**Subtitle:** Review the complete lifecycle, approval progress, and regulatory history of this application.

**Search Bar:** Search anything...

**Page Actions (Right Side):**

* Download Application Summary  
* View Related Project  
* View Related Property

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a comprehensive, read-only view of a regulatory application, including submission details, supporting documents, approval workflow, review history, and related records.

### Layout

Top Bar  
↓  
Application Header  
↓  
Application Summary Cards  
↓  
Application Information  
↓  
Related Project & Property  
↓  
Applicant Information  
↓  
Approval Workflow  
↓  
Submitted Documents  
↓  
RERA Review History  
↓  
Related Records  
↓  
Activity Timeline

### Section 1 — Application Header

Displays high-level application information.

#### **Left**

* Application ID  
* Application Type  
* Current Status Badge

#### **Right**

* Submission Date  
* Last Updated  
* Submitted By

### Section 2 — Application Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| Current Status | Overall application status |
| Approval Progress | Percentage completed |
| Priority | High / Medium / Low |
| Review Cycle | Current review round |
| Days in Process | Number of days since submission |
| Compliance Status | Compliant / Action Required |

### Section 3 — Application Information

Two-column information card.

#### **Basic Details**

* Application ID  
* Application Type  
* Submission Date  
* Submission Channel  
* Current Stage  
* Reference Number

#### **Processing Information**

* Assigned Department  
* Assigned Officer  
* Expected Completion Date  
* Current Processing Queue  
* Last Status Update

### Section 4 — Related Project & Property

Information card.

#### **Project Information**

* Project Name  
* Project ID  
* Development Phase

#### **Property Information *(when applicable)***

* Property Name  
* Unit Number  
* Registration Number

Buttons

* View Project  
* View Property Registration

### Section 5 — Applicant Information

Display the submitting organization's information.

#### **Details**

* Developer Company  
* Submitted By  
* Department  
* Position  
* Contact Information

This section is read-only.

### Section 6 — Approval Workflow

Horizontal workflow timeline.

#### **Stages**

* Draft  
* Submitted  
* Initial Validation  
* Technical Review  
* Compliance Review  
* Final Approval  
* Completed

Each stage displays:

* Stage Name  
* Responsible Department  
* Completion Date  
* Current Status

Completed stages use the standard success indicator.

The active stage is highlighted.

### Section 7 — Submitted Documents

Table.

#### **Columns**

* Document Name  
* Category  
* Uploaded By  
* Upload Date  
* Verification Status  
* Action

#### **Actions**

* View Document

### Section 8 — RERA Review History

Table.

#### **Columns**

* Review Date  
* Reviewing Officer  
* Review Stage  
* Outcome  
* Remarks  
* Status

Examples

* Initial Validation Passed  
* Technical Review Completed  
* Additional Information Requested  
* Compliance Approved  
* Final Approval Granted

### Section 9 — Related Records

Shows every record associated with this application.

Depending on the application type, display:

* Linked Project  
* Property Registration  
* Sales Disclosure  
* Escrow Account  
* Payment Record  
* Approval Certificate

Each record includes:

* Record Type  
* Reference Number  
* Current Status  
* Action (View)

### Section 10 — Activity Timeline

Chronological activity log.

Examples

* Draft created  
* Documents uploaded  
* Application submitted  
* Validation completed  
* Additional documents requested  
* Documents resubmitted  
* Technical review completed  
* Final approval granted  
* Certificate issued

Latest activities appear first.

### Empty State

If the application is still in Draft:

**Message**

> This application is currently being prepared and has not yet been submitted to RERA.

Primary Button

* Return to Applications

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Applications  
↓  
Application Details

├── View Project

├── View Property Registration

├── View Documents

├── View Related Records

└── Download Application Summary

### Notes

* This is the **master detail page** for all application types within the Developer Principal portal.  
* The layout is dynamic. Certain sections (such as Property Information or Escrow Records) appear only when relevant to the selected application type.  
* The page provides executives with complete visibility into the application's lifecycle without allowing edits or submissions.  
* All operational actions remain the responsibility of the relevant functional teams.

### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Applications**  
* **Selected Item:** Application Details *(opened from Applications list)*  
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

**Title:** Application Details

**Subtitle:** Review, update, and manage this regulatory application throughout the approval process.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Draft *(Draft only)*  
* Submit to RERA *(Draft only)*  
* More Actions

### Purpose

Provide the Project Registration Officer with a complete operational workspace for managing a regulatory application from creation through approval. The officer can update application details, upload supporting documents, respond to RERA requests, correct returned submissions, and monitor the approval workflow.

Unlike the Developer Principal's version, this page supports full operational interaction.

### Layout

Top Bar  
↓  
Application Header  
↓  
Approval Progress  
↓  
Application Information  
↓  
Related Project & Property  
↓  
Supporting Documents  
↓  
Validation Summary  
↓  
RERA Queries (If Applicable)  
↓  
Communication History  
↓  
Activity Timeline

### Section 1 — Application Header

Displays application overview.

#### **Left**

* Application ID  
* Application Type  
* Current Status Badge  
* Related Project

#### **Right**

* Created Date  
* Last Updated  
* Submitted By  
* Save Status

### Section 2 — Approval Progress

Display a horizontal workflow.

#### **Stages**

* Draft  
* Submitted  
* Initial Validation  
* Technical Review  
* Compliance Review  
* Final Approval  
* Completed

Completed stages use the existing progress indicator.

Current stage is highlighted.

Selecting a completed stage scrolls to the relevant information.

### Section 3 — Application Information

Editable while the application is in **Draft** or **Returned** status.

### **Basic Information**

* Application Type  
* Related Project  
* Related Property *(when applicable)*  
* Application Reference  
* Submission Category  
* Description

### **Processing Information**

* Responsible Officer  
* Department  
* Submission Date  
* Expected Processing Time

Fields become read-only after submission unless RERA returns the application.

### Section 4 — Related Project & Property

Display linked information.

#### **Project**

* Project Name  
* Project ID  
* Development Status

Button

* View Project Details

#### **Property *(If Applicable)***

* Property Name  
* Registration Number  
* Property Type

Button

* View Property Registration

### Section 5 — Supporting Documents

Upload and manage application documents.

#### **Table**

| Document | Status | Uploaded On | Version | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Upload  
* Replace  
* Preview  
* Download  
* Delete *(Draft only)*

Example documents include:

* Application Form  
* Supporting Certificates  
* Project Documents  
* Property Documents  
* Technical Reports  
* Additional Supporting Files

### Section 6 — Validation Summary

See [validation-rules.md](../validation-rules.md) for the shared automatic-validation mechanism and the common field-level checks (required fields, required documents, file verification). This screen's own additional checks: Related project eligibility, Related property validation, Duplicate submission check.

### Section 7 — RERA Queries

Visible only when RERA requests additional information.

#### **Table**

| Date | Request | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Respond  
* Upload Documents  
* Submit Response  
* View Previous Response

Unresolved requests are highlighted.

### Section 8 — Communication History

Display all communication with RERA.

Each message includes:

* Sender  
* Date & Time  
* Message  
* Attachments  
* Status

Actions

* Reply *(when permitted)*  
* View Attachment

Messages are displayed in chronological conversation format.

### Section 9 — Activity Timeline

Chronological audit trail.

Examples

* Draft created  
* Information updated  
* Documents uploaded  
* Validation completed  
* Submitted to RERA  
* Review started  
* Information requested  
* Response submitted  
* Application resubmitted  
* Approved  
* Certificate issued

Latest activities appear first.

### Empty State

If the application is newly created:

**Message**

> Complete the application information and upload all required supporting documents before submitting it to RERA.

Primary Button

* Complete Application

Secondary Button

* Upload Documents

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Applications  
↓  
Application Details

├── Edit Application

├── Upload Documents

├── Save Draft

├── Validate

├── Submit to RERA

├── Respond to RERA Query

├── Resubmit Application

└── Download Approval Certificate (After Approval)

### Notes

* This is the **primary operational workspace** for the **Project Registration Officer**.  
* Applications remain fully editable while in **Draft** status.  
* After submission, editing is locked unless RERA returns the application or requests additional information.  
* Every submission, document upload, correction, response, and status change is automatically recorded in the activity timeline.  
* The page should prominently display outstanding RERA requests to help officers respond before regulatory deadlines.

### Sales & Disclosure Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Applications**  
* **Selected Item:** Application Details *(opened from Applications list)*  
* **Other Menu Items:**  
  * Dashboard  
  * Sales & Disclosures  
  * **Applications (Active)**  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Application Details

**Subtitle:** Review, update, and manage this sales disclosure application throughout the regulatory approval process.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Draft *(Draft only)*  
* Submit to RERA *(Draft only)*  
* More Actions

### Purpose

Provide the Sales & Disclosure Officer with a complete operational workspace for managing a sales disclosure application from creation through approval. The officer can update application details, manage buyer information, upload supporting documents, respond to RERA requests, correct returned submissions, and monitor the approval workflow.

Unlike the Developer Principal's version, this page supports full operational interaction.

### Layout

Top Bar  
↓  
Application Header  
↓  
Approval Progress  
↓  
Application Information  
↓  
Property & Buyer Information  
↓  
Supporting Documents  
↓  
Validation Summary  
↓  
RERA Queries (If Applicable)  
↓  
Communication History  
↓  
Activity Timeline

### Section 1 — Application Header

Displays application overview.

#### **Left**

* Application ID  
* Application Type  
* Current Status Badge  
* Related Property

#### **Right**

* Created Date  
* Last Updated  
* Submitted By  
* Save Status

### Section 2 — Approval Progress

Display a horizontal workflow.

#### **Stages**

* Draft  
* Submitted  
* Initial Validation  
* Compliance Review  
* Additional Information *(If Required)*  
* Final Approval  
* Completed

Completed stages use the existing progress indicator.

The current stage is highlighted.

Selecting a completed stage scrolls to the relevant section.

### Section 3 — Application Information

Editable while the application is in **Draft**, **Returned**, or **Information Requested** status.

### **Basic Information**

* Application Type  
* Sales Disclosure Reference  
* Related Project  
* Related Property  
* Sale Reference  
* Submission Category  
* Description

### **Processing Information**

* Responsible Officer  
* Department  
* Submission Date  
* Expected Processing Time  
* Current Review Stage

Fields become read-only after submission unless RERA returns the application.

### Section 4 — Property & Buyer Information

### **Property Information**

Display linked property information.

* Project Name  
* Property Name  
* Unit Number  
* Property Registration Number  
* Property Type  
* Current Registration Status

**Button**

* View Property Registration

### **Buyer Information**

Editable while permitted.

#### **Primary Buyer**

* Full Name  
* National ID / Passport Number  
* Nationality  
* Phone Number  
* Email Address  
* Residential Address

#### **Buyer Classification**

* Individual  
* Corporate  
* Joint Purchase  
* Government Institution

#### **Additional Buyers**

Allow multiple buyers where applicable.

Each includes:

* Name  
* Ownership Percentage  
* Contact Information

### Section 5 — Supporting Documents

Upload and manage application documents.

#### **Required Documents**

Examples

* Sales Agreement  
* Buyer Identification  
* Proof of Payment  
* Mortgage Approval *(if applicable)*  
* Corporate Registration Documents *(Corporate Buyer)*  
* Power of Attorney *(if applicable)*  
* Other Supporting Documents

#### **Table**

| Document | Status | Uploaded On | Version | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Upload  
* Replace  
* Preview  
* Download  
* Delete *(Draft only)*

### Section 6 — Validation Summary

See [validation-rules.md](../validation-rules.md) for the shared automatic-validation mechanism and the common field-level checks (required fields, required documents, file verification). This screen's own additional checks: Buyer information completed, Property registration verified, Duplicate application check, Sale amount validation, Buyer identity validation.

### Section 7 — RERA Queries

Visible only when RERA requests additional information.

#### **Table**

| Date | Request | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Respond  
* Upload Documents  
* Update Buyer Information  
* Submit Response  
* View Previous Response

Outstanding requests are highlighted.

### Section 8 — Communication History

Display all communication with RERA.

Each message includes:

* Sender  
* Date & Time  
* Message  
* Attachments  
* Status

#### **Actions**

* Reply *(when permitted)*  
* View Attachment

Messages are displayed in chronological conversation format.

### Section 9 — Activity Timeline

Chronological audit trail.

Examples

* Draft created  
* Buyer information updated  
* Documents uploaded  
* Validation completed  
* Submitted to RERA  
* Compliance review started  
* Additional information requested  
* Buyer information updated  
* Documents replaced  
* Resubmitted  
* Approved  
* Disclosure certificate issued

Latest activities appear first.

### Empty State

If the application is newly created:

**Message**

> Complete the application information, buyer information, and upload all required supporting documents before submitting the application to RERA.

Primary Button

* Complete Application

Secondary Button

* Upload Documents

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Applications  
↓  
Application Details  
├── Edit Application  
├── Manage Buyer Information  
├── Upload Documents  
├── Save Draft  
├── Validate  
├── Submit to RERA  
├── Respond to RERA Query  
├── Resubmit Application  
└── Download Approval Summary (After Approval)

### Notes

* This is the **primary operational workspace** for the **Sales & Disclosure Officer**.  
* Applications remain fully editable while in **Draft**, **Returned**, or **Information Requested** status.  
* After submission, editing is locked unless RERA returns the application or requests additional information.  
* Buyer identity and supporting documents should be validated before submission to reduce regulatory rejection.  
* Every submission, correction, buyer information update, document upload, response, and approval is automatically recorded in the activity timeline for regulatory compliance and audit purposes.

### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Applications**  
* **Selected Item:** Application Details *(opened from Applications list)*  
* **Other Menu Items:**  
  * Dashboard  
  * Escrow Management  
  * **Applications (Active)**  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Application Details

**Subtitle:** Review, update, and manage this escrow-related application throughout the approval process.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Draft *(Draft only)*  
* Submit to RERA / Financial Institution *(Draft only)*  
* More Actions

### Purpose

Provide the Escrow Liaison with a complete operational workspace for managing an escrow-related application from creation through approval. The liaison can update application information, upload supporting documents, respond to requests from RERA or financial institutions, correct returned submissions, and monitor the approval workflow.

Unlike the Developer Principal's version, this page supports full operational interaction.

### Layout

Top Bar  
↓  
Application Header  
↓  
Information Tabs  
    ├─ Overview  
    ├─ Escrow Information  
    ├─ Supporting Documents  
    ├─ Validation Summary  
    ├─ RERA / Bank Queries  
    ├─ Communication History  
    └─ Activity Timeline

### Section 1 — Application Header

Displays the application overview.

#### **Left**

* Application ID  
* Application Type  
* Current Status Badge  
* Related Project

#### **Right**

* Created Date  
* Last Updated  
* Submitted By  
* Save Status

### Tab 1 — Overview

Displays the primary application information.

#### **Basic Information**

* Application ID  
* Application Type  
* Related Project  
* Escrow Account  
* Financial Institution  
* Submission Date  
* Current Status  
* Priority  
* Description

#### **Processing Information**

* Responsible Officer  
* Reviewing Authority  
* Current Review Stage  
* Expected Completion Date

Fields remain editable only while the application is in **Draft**, **Returned**, or **Information Requested** status.

### Tab 2 — Escrow Information

Displays information related to the linked escrow account.

#### **Escrow Details**

* Escrow Account Number  
* Project Name  
* Project Registration Number  
* Financial Institution  
* Current Escrow Balance  
* Current Construction Milestone  
* Fund Release Status

#### **Linked Records**

* View Escrow Details  
* View Fund Release Request

### Tab 3 — Supporting Documents

Manage all documents associated with the application.

#### **Required Documents**

Examples

* Escrow Agreement  
* Bank Confirmation Letter  
* Engineer Progress Certificate  
* Quantity Surveyor Report  
* Construction Progress Report  
* Site Inspection Report  
* Other Supporting Documents

#### **Table**

| Document | Status | Uploaded On | Version | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Upload  
* Replace  
* Preview  
* Download  
* Delete *(Draft only)*

### Tab 4 — Validation Summary

See [validation-rules.md](../validation-rules.md) for the shared automatic-validation mechanism and the common field-level checks (required fields, required documents, file verification). This screen's own additional checks: Escrow account verified, Financial institution selected, Related project eligibility verified, Duplicate application check.

### Tab 5 — RERA / Bank Queries

Visible only when additional information is requested.

#### **Table**

| Date | Request | Requested By | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Respond  
* Upload Documents  
* Update Application  
* Submit Response  
* View Previous Response

Outstanding requests are highlighted.

### Tab 6 — Communication History

Displays all communication between the Developer, Financial Institution, and RERA.

Each message includes:

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

Messages are displayed in chronological order.

### Tab 7 — Activity Timeline

Displays every operational event related to the application.

#### **Examples**

* Application created  
* Draft saved  
* Documents uploaded  
* Validation completed  
* Application submitted  
* Bank review started  
* Additional information requested  
* Response submitted  
* RERA review completed  
* Application approved  
* Application rejected

Each activity displays:

* Date & Time  
* User  
* Description  
* Status

### Empty State

This screen is only accessible after selecting an application. If the record cannot be found, display:

> The requested application could not be found or is no longer available.

**Primary Button**

* Back to Applications

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

1. Open **Applications**.  
2. Select an escrow-related application.  
3. Review the application overview and escrow information.  
4. Upload or replace supporting documents if required.  
5. Review validation results.  
6. Respond to RERA or financial institution queries when requested.  
7. Update the application where permitted.  
8. Resubmit the application if corrections are required.  
9. Track the application until the approval process is completed.

### Notes

* Operational actions are available only while the application is editable.  
* Once approved, the application becomes read-only.  
* Communication history maintains a complete audit trail between the Developer, Financial Institution, and RERA.  
* The tabbed layout follows the standardized Details-page pattern used across the platform.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations). The Escrow Liaison's is written as a numbered procedural walkthrough rather than the arrow/tree diagrams used by the other three roles.

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
