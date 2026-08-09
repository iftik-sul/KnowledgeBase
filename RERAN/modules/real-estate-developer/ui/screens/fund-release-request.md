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

# Screen: Fund Release Request

**Roles:** Escrow Liaison

The form used to prepare and submit a milestone-based fund release request, reached from [Escrow Details](escrow-details.md). Documented for the Escrow Liaison only — no other role has a version of this screen in the source material.

## Purpose

Provide the Escrow Liaison with a complete operational workspace to prepare, validate, and submit a milestone-based fund release request. The liaison can specify the construction milestone, request the eligible release amount, upload supporting documents, respond to bank or RERA queries, and monitor the approval process until funds are released.

## Layout

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Escrow Management**  
* **Selected Record:** Fund Release Request

### Top Bar Status

**Title:** Fund Release Request

**Subtitle:** Prepare and submit a milestone-based fund release request for escrow approval.

**Search Bar:** Search within fund release requests...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Draft  
* Submit Request *(Enabled only after validation passes)*  
* More Actions

Top Bar  
↓  
Fund Release Header  
↓  
Release Progress  
↓  
Release Information  
↓  
Milestone Verification  
↓  
Financial Information  
↓  
Supporting Documents  
↓  
Validation Summary  
↓  
RERA / Bank Queries (If Applicable)  
↓  
Communication History  
↓  
Activity Timeline

## Sections

### Section 1 — Fund Release Header

Displays the release request overview.

#### **Left**

* Release Request ID *(Draft until submitted)*  
* Escrow ID  
* Project Name  
* Release Status Badge

#### **Right**

* Created Date  
* Last Updated  
* Requested By  
* Save Status

### Section 2 — Release Progress

Display a horizontal workflow tracker.

#### **Stages**

* Draft  
* Information Completed  
* Documents Uploaded  
* Validation Passed  
* Submitted  
* Under Bank Review  
* Under RERA Review  
* Approved  
* Funds Released

Completed stages use the platform's standard success indicator.

The current stage is highlighted.

Completed stages are clickable for quick navigation.

### Section 3 — Release Information

Editable while the request is in **Draft**, **Returned**, or **Information Requested** status.

#### **Escrow Information *(Read-only)***

* Escrow Account  
* Project Name  
* Project Registration Number  
* Financial Institution  
* Current Escrow Balance

#### **Release Request Details**

* Construction Milestone  
* Milestone Completion Date  
* Requested Release Amount  
* Eligible Release Amount *(Auto-calculated)*  
* Purpose of Release  
* Contractor / Vendor *(Optional)*  
* Expected Payment Date  
* Remarks

### Section 4 — Milestone Verification

Capture details supporting milestone completion.

#### **Construction Progress**

* Milestone Description  
* Percentage of Project Completed  
* Work Completed Summary  
* Site Inspection Date  
* Engineer Verification Status  
* Quantity Surveyor Verification Status

#### **Verification Information**

* Engineer Name  
* Engineer Registration Number  
* Quantity Surveyor Name  
* Verification Date

### Section 5 — Financial Information

Display escrow and release financial details.

#### **Escrow Summary *(Read-only)***

* Initial Escrow Deposit  
* Total Deposited  
* Total Funds Released  
* Current Available Balance

#### **Release Calculation**

* Requested Amount  
* Approved Milestone Percentage  
* Maximum Eligible Release  
* Remaining Balance After Release

System automatically highlights if the requested amount exceeds the eligible limit.

### Section 6 — Supporting Documents

Upload documents required for fund release.

#### **Required Documents**

* Engineer Progress Certificate  
* Quantity Surveyor Report  
* Construction Progress Report  
* Site Inspection Report  
* Contractor Payment Schedule *(if applicable)*  
* Bank Supporting Documents *(if applicable)*  
* Photographic Evidence  
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

See [validation-rules.md](../validation-rules.md) for the shared automatic-validation mechanism and the common field-level checks (required fields, required documents, file verification). This screen's own additional checks: Escrow account is active, Milestone eligible for release, Requested amount within approved limit, Engineer verification completed, Quantity Surveyor verification completed, Duplicate release request check.

### Section 8 — RERA / Bank Queries

Visible only when additional information is requested.

#### **Table**

| Date | Request | Requested By | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: | :---: |

#### **Actions**

* Respond  
* Upload Additional Documents  
* Update Request  
* Submit Response  
* View Previous Response

Outstanding requests are highlighted.

### Section 9 — Communication History

Displays communication between the Developer, Financial Institution, and RERA.

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

### Section 10 — Activity Timeline

Displays every event related to this fund release request.

#### **Examples**

* Fund release request created  
* Milestone selected  
* Release amount updated  
* Supporting documents uploaded  
* Validation completed  
* Submitted to bank  
* Bank review started  
* Additional information requested  
* Response submitted  
* Bank approved request  
* Submitted to RERA  
* RERA approved release  
* Funds transferred  
* Request completed

Each activity displays:

* Date & Time  
* User  
* Description  
* Status

## Empty State

If this is a newly created request:

**Message**

> Start by selecting the completed construction milestone and providing the required financial and supporting information to request the release of escrow funds.

**Primary Button**

* Select Milestone

**Secondary Button**

* Upload Supporting Documents

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

See "Section 7 — Validation Summary" above.

## User Flow

Escrow Details

        ↓

Fund Release Request

        │

        ├── Save Draft

        │

        ├── Upload Supporting Documents

        │

        ├── Submit Request

        │        ↓

        │   Bank Review

        │        ↓

        │   RERA Review

        │        ↓

        │  Funds Released

        │

        └── Back

              ↓

       Escrow Details

## Notes

* One fund release request should be associated with a single construction milestone.  
* The system should automatically calculate the **maximum eligible release amount** based on the approved milestone schedule and escrow balance.  
* Supporting documents from engineers and quantity surveyors are mandatory before submission.  
* Once submitted, all actions and communications should be recorded in the **Activity Timeline** for audit and regulatory compliance.  
* Requests that are **Approved** or **Funds Released** become read-only, except for viewing and downloading supporting information.
