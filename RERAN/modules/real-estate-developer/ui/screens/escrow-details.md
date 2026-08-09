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

# Screen: Escrow Details

**Roles:** Principal · Escrow Liaison

The detail view of a single escrow account, opened from [Escrow Management](escrow-management.md). The Developer Principal / Director sees a read-only view; the Escrow Liaison sees an operational workspace for requesting fund releases and managing milestones and documents.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Escrow Management**
* **Top Bar Title:** Escrow Details
* **Search Bar:** (differs by role — see below)

The page uses the shared **Background \+ HorizontalBorder** component.

The two Layout diagrams are structurally different: the Principal's is a stacked, numbered-section layout; the Escrow Liaison's uses **Information Tabs** (Overview, Fund Releases, Milestones, Documents, Activity Log) under a single summary card, the same tab pattern seen on that role's Application Details and Document Details screens. The subtitle and search-bar placeholder text also differ by role — see [Role Variations](#role-variations).

## Sections

Every section is role-specific — see [Role Variations](#role-variations). Only the Escrow Liaison's version has a **Right Sidebar — Alerts & Reminders** section; the Principal's has no equivalent.

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations).

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Escrow Management**  
* **Selected Item:** Escrow Details *(opened from Escrow Management list)*  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * Sales & Disclosures  
  * **Escrow Management (Active)**  
  * Applications  
  * Documents  
  * Reports  
  * Company Profile  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Escrow Details

**Subtitle:** Review the complete escrow account, milestone progress, and fund release history.

**Search Bar:** Search anything...

**Page Actions (Right Side):**

* Download Escrow Summary  
* View Linked Project  
* View Sales Record

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a complete, read-only view of an escrow account, including financial institution details, construction milestones, fund releases, supporting documents, and compliance history.

### Layout

Top Bar  
↓  
Escrow Header  
↓  
Escrow Summary Cards  
↓  
Escrow Account Information  
↓  
Project Information  
↓  
Financial Institution Information  
↓  
Milestone & Fund Release Timeline  
↓  
Fund Release History  
↓  
Escrow Documents  
↓  
RERA Review History  
↓  
Activity Timeline

### Section 1 — Escrow Header

Displays high-level escrow information.

#### **Left**

* Escrow Account Number  
* Project Name  
* Escrow Status Badge

#### **Right**

* Financial Institution  
* Last Updated  
* Managed By (Escrow Liaison)

### Section 2 — Escrow Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| Escrow Status | Current account status |
| Escrow Balance | Current funds held |
| Total Funds Released | Cumulative released funds |
| Current Milestone | Active construction milestone |
| Next Release Amount | Amount pending approval |
| Compliance Status | Compliant / Pending |

### Section 3 — Escrow Account Information

Two-column information card.

#### **Account Details**

* Escrow Account Number  
* Escrow Reference  
* Account Opening Date  
* Escrow Type  
* Current Balance  
* Currency

#### **Responsible Parties**

* Developer Company  
* Escrow Liaison  
* Financial Institution  
* RERA Reference

### Section 4 — Project Information

Information card.

Display:

* Project Name  
* Project ID  
* Project Location  
* Development Phase  
* Overall Progress  
* Linked Property Registrations

Button

* View Project Details

### Section 5 — Financial Institution Information

Information card.

Display:

* Institution Name  
* Branch  
* Relationship Manager  
* Contact Information  
* Escrow Agreement Reference

Button

* View Institution Details

### Section 6 — Milestone & Fund Release Timeline

Horizontal progress tracker.

#### **Stages**

* Escrow Account Created  
* Initial Deposit  
* Milestone 1 Completed  
* Fund Release 1  
* Milestone 2 Completed  
* Fund Release 2  
* Final Completion  
* Escrow Closed

Completed stages use the platform's standard success indicator.

The current stage is highlighted.

### Section 7 — Fund Release History

Table showing all release requests.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Release No. | Sequential release number |
| Milestone | Construction milestone |
| Requested Amount | Requested release amount |
| Approved Amount | Approved release amount |
| Approval Date | Date approved |
| Status | Release status |
| Action | View Details |

### Section 8 — Escrow Documents

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

### Section 9 — RERA Review History

Table.

#### **Columns**

* Review Date  
* Reviewing Officer  
* Activity  
* Outcome  
* Status

Examples

* Escrow Agreement Approved  
* Milestone Verified  
* Fund Release Approved  
* Compliance Review Completed

### Section 10 — Activity Timeline

Chronological history.

Examples

* Escrow account opened  
* Initial deposit received  
* Milestone inspection completed  
* Fund release requested  
* RERA approval granted  
* Funds released  
* Escrow account updated

Latest activities appear first.

### Empty State

If the escrow account has been created but no fund releases have occurred:

**Message**

> The escrow account has been established. Fund releases will appear once construction milestones are completed and approved.

Primary Button

* View Project

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Escrow Management  
↓  
Escrow Details

├── View Project Details

├── View Sales Record

├── View Escrow Documents

├── View Financial Institution

└── Download Escrow Summary

### Notes

* This is an **executive oversight screen** for the **Developer Principal /Director**.  
* It consolidates all financial and regulatory information related to a single escrow account.  
* No financial transactions or approvals can be performed from this page.  
* All operational escrow activities remain the responsibility of the **Escrow Liaison**, while approvals by financial institutions and RERA are reflected as read-only status updates.

### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Escrow Management**  
* **Other Menu Items:**  
  * Dashboard  
  * **Escrow Management (Active)**  
  * Applications  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support  
* **Selected Record:** Escrow Details

### Top Bar Status

**Title:** Escrow Details

**Subtitle:** View escrow account information, milestones, fund releases, and compliance activities

**Search Bar:** Search within escrow records...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Request Fund Release  
* Download Escrow Summary

### Purpose

Provide a complete view of a single escrow account, allowing the Escrow Liaison to monitor the account lifecycle, review milestones, track fund releases, upload supporting documents, and respond to regulatory or financial institution requirements.

### Layout

Top Bar  
↓  
Escrow Summary Card  
↓  
Information Tabs  
    ├─ Overview  
    ├─ Fund Releases  
    ├─ Milestones  
    ├─ Documents  
    └─ Activity Log

### Section 1 — Escrow Summary Card

Displays key information at the top of the page.

#### **Information**

* Escrow ID  
* Project Name  
* Project Registration Number  
* Financial Institution  
* Escrow Account Number  
* Current Balance  
* Total Deposits  
* Total Released  
* Current Milestone  
* Escrow Status  
* Registration Date

#### **Quick Actions**

* Request Fund Release  
* Upload Documents  
* Download Summary

### Tab 1 — Overview

Displays the general escrow account information.

#### **Project Information**

* Project Name  
* Development Type  
* Developer Name  
* Project Registration Number  
* Project Location

#### **Escrow Information**

* Financial Institution  
* Escrow Account Number  
* Account Opening Date  
* Current Status

#### **Financial Summary**

* Initial Deposit  
* Total Deposited  
* Total Released  
* Remaining Balance

### Tab 2 — Fund Releases

Displays every release request associated with the escrow account.

#### **Table Columns**

| Column | Description |
| ----- | ----- |
| Release ID | Unique request number |
| Milestone | Construction milestone |
| Requested Amount | Amount requested |
| Approved Amount | Amount approved |
| Request Date | Submission date |
| Status | Current status |
| Action | View Details |

#### **Status**

See [status-badges.md](../status-badges.md#fund-release-status) for the status vocabulary — including a conflict between this list, the Principal's escrow-management.md list, and the Escrow Liaison's own escrow-management.md list.

#### **Actions**

* View Details

If the request is still editable:

* Continue Draft

### Tab 3 — Milestones

Displays all construction milestones linked to this escrow account.

#### **Columns**

* Milestone Name  
* Planned Completion  
* Actual Completion  
* Verification Status  
* Eligible Release Amount  
* Status

#### **Status**

See [status-badges.md](../status-badges.md#milestone-verification-status-additional-vocabulary-found-during-consolidation) for the status vocabulary.

### Tab 4 — Documents

Displays all escrow-related documents.

#### **Categories**

* Escrow Agreement  
* Bank Confirmation Letter  
* Construction Progress Report  
* Engineer Certificate  
* Quantity Surveyor Report  
* Fund Release Documents  
* Supporting Documents

#### **Columns**

* Document Name  
* Category  
* Uploaded By  
* Upload Date  
* Version  
* Status  
* Action

#### **Actions**

* View  
* Download

### Tab 5 — Activity Log

Displays every activity performed on the escrow account.

#### **Timeline**

Examples

* Escrow account registered  
* Initial deposit received  
* Construction milestone submitted  
* Milestone verified  
* Fund release requested  
* Bank confirmed request  
* RERA approved release  
* Funds transferred  
* Additional documents requested  
* Escrow account closed

Each activity displays

* Date & Time  
* User  
* Description  
* Status

### Right Sidebar — Alerts & Reminders

Displays important notifications related to this escrow account.

Examples

* Milestone awaiting verification  
* Bank confirmation pending  
* Additional documents required  
* Fund release returned  
* Compliance review scheduled  
* Upcoming submission deadline

### Empty State

If no milestones or releases exist yet:

**Message**

> This escrow account has been registered successfully. No fund release requests or construction milestones have been recorded yet.

**Primary Button**

* Request Fund Release

**Secondary Button**

* Upload Documents

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Escrow Details

├── Request Fund Release

│      ↓

│  Fund Release Request

│

├── View Fund Release

│      ↓

│  Fund Release Details

│

├── Upload Documents

│      ↓

│  Documents

│

├── Download Summary

│

└── Back

       ↓

   Escrow Management

### Notes

* This screen acts as the central workspace for managing an individual escrow account.  
* All fund release requests, construction milestones, supporting documents, and activity history should be linked to the selected escrow account.  
* Users cannot modify approved or released fund requests; those records are read-only.  
* Every action performed on the escrow account should be recorded in the **Activity Log** for audit and regulatory compliance.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations). The Escrow Liaison's is rooted at Escrow Details itself rather than at Dashboard.

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
