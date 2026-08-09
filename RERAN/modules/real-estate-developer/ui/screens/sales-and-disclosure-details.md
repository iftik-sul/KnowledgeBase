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

# Screen: Sales & Disclosure Details

**Roles:** Principal · Sales & Disclosure Officer

The detail view of a single property sale, opened from [Sales & Disclosures](sales-and-disclosures.md). The Developer Principal / Director sees a read-only view; the Sales & Disclosure Officer sees an editable operational workspace covering the sale from recording through disclosure approval.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Sales & Disclosures**
* **Top Bar Title:** Sales & Disclosure Details
* **Search Bar:** Search anything...

Both roles reuse the shared Background + HorizontalBorder component, worded slightly differently in each ("The page continues using the shared..." vs "The page uses the shared..."), so the exact sentence is kept per role rather than merged. The two Layout diagrams differ in both content and length — see [Role Variations](#role-variations).

## Sections

Every section is role-specific — see [Role Variations](#role-variations). The Principal's version is organized around read-only summary cards and history tables; the Sales & Disclosure Officer's is organized around the disclosure workflow itself (editable Sale/Buyer Information, Validation Summary, RERA Queries, Communication History).

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations).

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Validation

Only the Sales & Disclosure Officer's version has a Validation Summary — the Principal's is read-only and has none. See that role's "Validation Summary" block under [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Sales & Disclosures**  
* **Selected Item:** Sales & Disclosure Details *(opened from Sales & Disclosures list)*  
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

**Title:** Sales & Disclosure Details

**Subtitle:** Review the complete sales transaction and disclosure record for this property.

**Search Bar:** Search anything...

**Page Actions (Right Side):**

* Download Disclosure Report  
* View Property Registration  
* View Project

The page continues using the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a comprehensive, read-only view of a completed property sale, including buyer information, disclosure status, supporting documents, RERA review history, and compliance progress.

### Layout

Top Bar  
↓  
Sales Header  
↓  
Sales Summary Cards  
↓  
Property Information  
↓  
Buyer Information  
↓  
Sales Information  
↓  
Disclosure Progress  
↓  
Submitted Documents  
↓  
RERA Review History  
↓  
Activity Timeline

### Section 1 — Sales Header

Display key transaction information.

#### **Left**

* Sale Reference Number  
* Property Name / Unit  
* Sale Status Badge

#### **Right**

* Sale Date  
* Last Updated  
* Managed By (Sales & Disclosure Officer)

### Section 2 — Sales Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| Sale Status | Current transaction status |
| Disclosure Status | Current RERA disclosure stage |
| Sale Value | Total sale amount |
| Buyer Verification | Verified / Pending |
| Escrow Status | Linked escrow progress |
| Compliance Status | Compliant / Pending |

### Section 3 — Property Information

Information card.

#### **Property Details**

* Property Name  
* Unit Number  
* Property Type  
* Project Name  
* Registration Number  
* Property Address

Button

* View Property Registration

### Section 4 — Buyer Information

Information card.

#### **Buyer Details**

* Buyer Name  
* Buyer Type (Individual / Business)  
* Identification Number  
* Contact Information  
* Verification Status

This information is displayed according to the user's access permissions and applicable privacy controls.

### Section 5 — Sales Information

Display transaction details.

#### **Details**

* Sale Reference  
* Sale Date  
* Sale Price  
* Payment Method  
* Sales Officer  
* Transaction Status

### Section 6 — Disclosure Progress

Horizontal progress tracker.

#### **Stages**

* Sale Recorded  
* Disclosure Prepared  
* Submitted to RERA  
* Under Review  
* Approved  
* Disclosure Completed

Current stage is highlighted.

Completed stages display the standard success indicator.

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
* Action Taken  
* Remarks  
* Status

Examples

* Disclosure Submitted  
* Additional Information Requested  
* Compliance Verified  
* Disclosure Approved

### Section 9 — Activity Timeline

Chronological history.

Examples

* Property reserved  
* Buyer verified  
* Sale completed  
* Disclosure submitted  
* Documents uploaded  
* RERA review completed  
* Disclosure approved

Latest activities appear first.

### Empty State

If the disclosure has not yet been submitted:

**Message**

> The sales transaction has been recorded, but the disclosure has not yet been submitted to RERA.

Primary Button

* View Sales & Disclosures

### Reused Components

* Left Sidebar  
* Top Bar  
* Information Cards  
* KPI Cards  
* Progress Tracker  
* Data Tables  
* Status Badges  
* Activity Timeline  
* Document Viewer  
* Empty State  
* Buttons

### User Flow

Dashboard  
↓  
Sales & Disclosures  
↓  
Sales & Disclosure Details

├── View Property Registration

├── View Project

├── View Submitted Documents

└── Download Disclosure Report

### Sales & Disclosure Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Sales & Disclosures**  
* **Selected Item:** Sales & Disclosure Details *(opened from Sales & Disclosures list)*  
* **Other Menu Items:**  
  * Dashboard  
  * **Sales & Disclosures (Active)**  
  * Applications  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Sales & Disclosure Details

**Subtitle:** Record, validate, and manage this property sale and its regulatory disclosure.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Draft  
* Submit to RERA *(Enabled only after validation passes)*  
* More Actions

### Purpose

Provide the Sales & Disclosure Officer with a complete operational workspace to manage a property sale from initial recording through regulatory disclosure approval. The officer can enter sale details, manage buyer information, upload supporting documents, prepare disclosure information, respond to RERA requests, and monitor the approval lifecycle.

Unlike the Developer Principal's version, this page is fully interactive and supports editing, validation, submission, and resubmission.

### Layout

Top Bar  
↓  
Sale Header  
↓  
Disclosure Progress  
↓  
Sale Information  
↓  
Buyer Information  
↓  
Property Information  
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

### Section 1 — Sale Header

Displays the overall sale information.

#### **Left**

* Sale Reference Number  
* Property / Unit Name  
* Disclosure Status Badge  
* Linked Project

#### **Right**

* Sale Date  
* Last Updated  
* Sales Officer  
* Save Status

### Section 2 — Disclosure Progress

Display a horizontal workflow tracker.

#### **Stages**

* Sale Recorded  
* Buyer Information Completed  
* Supporting Documents Uploaded  
* Validation Passed  
* Disclosure Submitted  
* Under Review  
* Approved

Completed stages use the platform's standard success indicator.

The current stage is highlighted.

Completed stages are clickable for quick navigation.

### Section 3 — Sale Information

Editable while the disclosure is in **Draft**, **Returned**, or **Information Requested** status.

#### **Sale Details**

* Sale Reference  
* Sale Date  
* Property  
* Project  
* Sale Type  
* Sale Value  
* Payment Method  
* Payment Status  
* Reservation Date *(if applicable)*  
* Completion Date *(if applicable)*

#### **Transaction Details**

* Sales Agreement Number  
* Sales Agent *(if applicable)*  
* Financing Type  
* Mortgage Provider *(if applicable)*  
* Remarks

### Section 4 — Buyer Information

Capture buyer details required for regulatory disclosure.

#### **Primary Buyer**

* Full Name  
* National ID / Passport Number  
* Date of Birth  
* Nationality  
* Phone Number  
* Email Address  
* Residential Address

#### **Buyer Classification**

* Individual  
* Corporate Entity  
* Joint Purchase  
* Government Institution

#### **Additional Purchasers *(When Applicable)***

Allow multiple buyers to be added.

Each additional buyer includes:

* Name  
* Ownership Percentage  
* Contact Information

### Section 5 — Property Information

Display linked property information.

#### **Property Details *(Read-only)***

* Property Name  
* Unit Number  
* Property Registration Number  
* Project Name  
* Property Type  
* Floor  
* Size  
* Current Registration Status

Button

* View Property Registration

### Section 6 — Supporting Documents

Document management section.

#### **Required Documents**

Examples

* Sales Agreement  
* Buyer Identification  
* Proof of Payment  
* Mortgage Approval *(if applicable)*  
* Power of Attorney *(if applicable)*  
* Corporate Resolution *(Corporate Buyers)*  
* Other Supporting Documents

#### **Table**

| Document | Status | Uploaded On | Version | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Upload  
* Replace  
* Preview  
* Delete *(Draft only)*

### Section 7 — Validation Summary

Automatic validation before submission.

Validation checks include:

* Mandatory fields completed  
* Buyer information completed  
* Property eligibility verified  
* Required documents uploaded  
* Duplicate disclosure check  
* Sale value validation  
* Buyer identity validation  
* File verification

Display results using:

* ✅ Passed  
* ⚠ Warning  
* ❌ Error

Selecting an issue scrolls directly to the affected field.

The **Submit to RERA** button remains disabled until all mandatory validations pass.

### Section 8 — RERA Queries

Visible only when RERA requests additional information.

#### **Table**

| Date | Request | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Respond  
* Upload Additional Documents  
* Update Buyer Information  
* Submit Response  
* View Previous Response

Outstanding requests are visually highlighted.

### Section 9 — Communication History

Conversation thread with RERA.

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

Displays every activity performed on this disclosure.

Examples

* Sale recorded  
* Buyer information updated  
* Documents uploaded  
* Validation completed  
* Disclosure submitted  
* RERA review started  
* Additional information requested  
* Documents replaced  
* Resubmitted  
* Disclosure approved

Latest activities appear first.

### Empty State

If the disclosure has just been created:

**Message**

> Complete the sale information, buyer information, and upload all required documents before submitting the disclosure to RERA.

Primary Button

* Complete Sale Information

Secondary Button

* Upload Documents

### Reused Components

* Left Sidebar  
* Top Bar (Background \+ HorizontalBorder)  
* Progress Tracker  
* Information Cards  
* Editable Form Components  
* File Upload Component  
* Validation Panel  
* Status Badges  
* Communication Thread  
* Timeline  
* Buttons

### User Flow

Dashboard  
↓  
Sales & Disclosures  
↓  
Sales & Disclosure Details  
├── Edit Sale Information  
├── Manage Buyer Information  
├── Upload Documents  
├── Save Draft  
├── Validate Disclosure  
├── Submit to RERA  
├── Respond to RERA Query  
└── Download Disclosure Summary (After Approval)

### Notes

* This is the **primary operational workspace** for the **Sales & Disclosure Officer**.  
* The page supports the complete lifecycle of a property sale and regulatory disclosure, from initial sale recording to final RERA approval.  
* Buyer information should be validated before submission to reduce regulatory rejection.  
* The disclosure becomes read-only after submission unless RERA returns it or requests additional information.  
* Every modification, document upload, buyer update, regulatory response, and approval must be recorded in the activity timeline to maintain a complete audit trail and regulatory compliance.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations).

## Notes

Only the Sales & Disclosure Officer's version has a Notes section — see that role's block under [Role Variations](#role-variations). The Principal's version has no Notes section; its content ends at User Flow.
