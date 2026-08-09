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

# Screen: Fund Release Request Details

**Roles:** Escrow Liaison

The detail view of a single, already-submitted fund release request, opened from Escrow Details' Fund Releases tab or directly from Escrow Management. Documented for the Escrow Liaison only — no other role has a version of this screen in the source material.

## Purpose

Provide the Escrow Liaison with a complete operational workspace to review and manage an existing fund release request throughout its approval lifecycle. The liaison can monitor review progress, update eligible information when permitted, upload revised documents, respond to queries from the Financial Institution or RERA, review communication history, and track every activity related to the request.

## Layout

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Escrow Management**  
* **Selected Item:** Fund Release Request Details *(opened from Escrow Details → Fund Releases or Escrow Management)*  
* **Other Menu Items:**  
  * Dashboard  
  * **Escrow Management (Active)**  
  * Applications  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Fund Release Request Details

**Subtitle:** Review, update, and manage this milestone-based fund release request throughout the approval process.

**Search Bar:** Search within fund release requests...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Changes *(Enabled when edits are made and request is editable)*  
* Submit Response *(Visible when additional information is requested)*  
* More Actions

Top Bar  
↓  
Fund Release Header  
↓  
Information Tabs  
    ├─ Overview  
    ├─ Milestone Verification  
    ├─ Financial Information  
    ├─ Supporting Documents  
    ├─ RERA / Bank Queries  
    ├─ Communication History  
    └─ Activity Timeline

## Sections

### Section 1 — Fund Release Header

Displays the overall request summary.

#### **Left**

* Release Request ID  
* Escrow ID  
* Project Name  
* Release Status Badge

#### **Right**

* Submitted Date  
* Last Updated  
* Requested By  
* Current Review Stage

#### **Quick Actions**

* Download Request Summary  
* Print Request  
* View Escrow Account

### Tab 1 — Overview

Displays the complete release request information.

#### **Escrow Information**

* Escrow Account Number  
* Financial Institution  
* Project Name  
* Project Registration Number  
* Current Escrow Balance

#### **Release Request Details**

* Construction Milestone  
* Milestone Completion Date  
* Requested Release Amount  
* Eligible Release Amount  
* Purpose of Release  
* Contractor / Vendor  
* Expected Payment Date  
* Remarks

#### **Approval Status**

* Submission Status  
* Bank Review Status  
* RERA Review Status  
* Final Approval Status

### Tab 2 — Milestone Verification

Displays milestone completion and verification details.

#### **Construction Progress**

* Milestone Name  
* Milestone Description  
* Percentage Completed  
* Site Inspection Date  
* Completion Evidence

#### **Professional Verification**

* Engineer Name  
* Engineer Registration Number  
* Engineer Verification Status  
* Quantity Surveyor Name  
* Quantity Surveyor Registration Number  
* Quantity Surveyor Verification Status  
* Verification Date

#### **Inspection Summary**

* Site Inspection Result  
* Reviewer Remarks  
* Compliance Status

### Tab 3 — Financial Information

Displays financial calculations associated with the request.

#### **Escrow Summary**

* Initial Escrow Deposit  
* Total Deposited  
* Total Released  
* Current Available Balance

#### **Release Calculation**

* Requested Amount  
* Eligible Release Amount  
* Approved Amount *(when available)*  
* Remaining Balance After Release

#### **Payment Information**

* Payment Status  
* Payment Reference *(when released)*  
* Funds Release Date *(if completed)*

### Tab 4 — Supporting Documents

Displays every document submitted with the release request.

#### **Categories**

* Engineer Progress Certificate  
* Quantity Surveyor Report  
* Construction Progress Report  
* Site Inspection Report  
* Contractor Payment Schedule  
* Bank Supporting Documents  
* Photographic Evidence  
* Other Supporting Documents

#### **Table Columns**

| Column | Description |
| ----- | ----- |
| Document | Document name |
| Category | Document type |
| Uploaded By | User |
| Uploaded On | Date |
| Version | Current version |
| Status | Verification status |
| Action | View |

#### **Actions**

* View  
* Download  
* Upload Revised Version *(when permitted)*

### Tab 5 — RERA / Bank Queries

Visible only when additional information has been requested.

#### **Table**

| Column | Description |
| ----- | ----- |
| Date | Request date |
| Requested By | RERA / Financial Institution |
| Query | Requested clarification |
| Due Date | Response deadline |
| Status | Current status |
| Action | Respond |

#### **Actions**

* Respond  
* Upload Additional Documents  
* Update Request Information  
* Submit Response  
* View Previous Responses

Outstanding requests are highlighted.

### Tab 6 — Communication History

Displays all communication related to the request.

Each message includes:

* Sender  
* Organization  
* Date & Time  
* Message  
* Attachments  
* Status

#### **Actions**

* Reply *(when permitted)*  
* View Attachment

Messages are displayed in chronological conversation format.

### Tab 7 — Activity Timeline

Displays a complete audit trail for the fund release request.

#### **Timeline Examples**

* Draft created  
* Request submitted  
* Validation completed  
* Bank review started  
* Additional information requested  
* Documents uploaded  
* Response submitted  
* Bank approved request  
* RERA review started  
* RERA approved request  
* Funds released  
* Request completed

Each activity displays:

* Date & Time  
* User / Organization  
* Activity Description  
* Status

## Empty State

If no additional queries, communications, or activities exist:

**Message**

> No additional records are available for this fund release request yet.

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

The source material has no explicit Validation Summary section for this screen, unlike [fund-release-request.md](fund-release-request.md) (the creation form). Edits remain governed by status: "The Escrow Liaison may update request information and upload revised documents only while the request is in an editable status (such as Draft, Returned, or Information Requested). Once the request reaches Approved or Funds Released, it becomes read-only." — see Notes below.

## User Flow

Open Escrow Management  
↓  
Locate the required escrow account  
↓  
Click View Details  
↓  
Open the Fund Releases tab  
↓  
Select the required fund release request  
↓  
Review fund release details  
↓  
Review approval progress and current status  
↓  
Respond to RERA or Financial Institution queries (if requested)  
↓  
Upload revised supporting documents or update request information (when permitted)  
↓  
Resubmit the response (if required)  
↓  
Track the approval workflow until the funds are released

## Notes

* This screen serves as the **operational detail page** for a single fund release request and is accessed from the **Fund Releases** tab within **Escrow Details** or directly from **Escrow Management**.  
* The Escrow Liaison may update request information and upload revised documents **only while the request is in an editable status** (such as **Draft**, **Returned**, or **Information Requested**). Once the request reaches **Approved** or **Funds Released**, it becomes **read-only**.  
* All approval decisions by the **Financial Institution** and **RERA** are displayed as status updates and cannot be modified by the developer.  
* Every response to queries, document upload, status change, and review action is automatically recorded in the **Activity Timeline** to maintain a complete audit trail for regulatory compliance.  
* The system validates that any revised request continues to comply with the approved milestone, eligible release amount, and supporting document requirements before allowing a response or resubmission.  
* The page follows the same **Details Screen** design pattern used throughout the Real Estate Developer Portal, ensuring a consistent user experience across operational modules.
