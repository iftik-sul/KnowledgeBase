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

# Screen: Company Profile

**Access:** All four roles — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../../navigation.md). Role is audit-trail attribution only.

The organization's master profile: corporate information, RERA registration, authorized representatives, office locations, banking/escrow information, company documents, and settings. Only one design of this screen exists in the source material — unlike the fifteen multi-variant screens elsewhere in this module, there was never a second version to merge, so this file needed no rebuild.

> **Corrected 2026-08-15, second pass.** This file's own Access line already said "all four roles," but its Purpose, Notes, and Section 10 still described the screen as though it belonged to the Developer Principal / Director specifically, including a literal leftover permission gate ("Only users with appropriate permissions can modify these settings") that the earlier access-model correction pass evidently missed — likely because this screen had no role variant to merge, and so wasn't touched by the same pass that removed gating language from the fifteen screens that did. Fixed throughout below.

## Purpose

Give any developer user a centralized view of the organization's corporate information, regulatory registrations, licenses, office locations, authorized representatives, banking information, and company documents. This page is the master profile for the developer organization, and any user may view or edit it.

## Layout

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Company Profile**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

### Top Bar Status

**Title:** Company Profile

**Subtitle:** Manage your organization's registration details, licenses, authorized representatives, and corporate information.

**Search Bar:** Search anything...

**Page Actions (Right Side):**

* Edit Company Profile  
* Download Company Profile  
* View Audit Log

The page uses the shared **Background \+ HorizontalBorder** component.

Top Bar  
↓  
Company Header  
↓  
Company Summary Cards  
↓  
Basic Company Information  
↓  
RERA Registration  
↓  
Corporate Information  
↓  
Authorized Representatives  
↓  
Office Locations  
↓  
Banking & Escrow Information  
↓  
Company Documents  
↓  
Organization Settings  
↓  
Audit Information

## Sections

### Section 1 — Company Header

Displays key organization information.

#### **Left**

* Company Logo  
* Company Name  
* Developer Registration Number  
* Company Status Badge

#### **Right**

* Organization Type  
* Member Since  
* Last Profile Updated

### Section 2 — Company Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| RERA License Status | Active / Suspended / Expired |
| Active Projects | Number of ongoing projects |
| Registered Properties | Total registered properties |
| Active Escrow Accounts | Linked escrow accounts |
| Authorized Representatives | Total approved representatives |
| Compliance Score | Overall organizational compliance |

### Section 3 — Basic Company Information

Two-column information card.

#### **Organization Details**

* Company Name  
* Registration Number  
* Company Type  
* Tax Identification Number  
* Date of Incorporation  
* Country of Registration

#### **Contact Information**

* Official Email  
* Phone Number  
* Website  
* Customer Support Contact

### Section 4 — RERA Registration

Displays regulatory registration details.

#### **Information**

* Developer Registration Number  
* Registration Date  
* License Number  
* License Status  
* Expiry Date  
* Renewal Status  
* Assigned RERA Office

See [status-badges.md](../status-badges.md#company--rera-license-status) for the status vocabulary.

### Section 5 — Corporate Information

Displays legal and corporate structure.

#### **Information**

* Legal Entity Name  
* Parent Company *(if applicable)*  
* Business Category  
* Share Capital  
* Number of Employees  
* Primary Business Activity

### Section 6 — Authorized Representatives

Table listing individuals authorized to act on behalf of the company.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Name | Representative name |
| Position | Job title |
| Role | System role |
| Authorization Status | Active / Inactive |
| Appointment Date | Date assigned |
| Action | View Details |

### Section 7 — Office Locations

Displays all registered offices.

#### **Information**

Each office card displays:

* Office Name  
* Office Type  
* Address  
* City  
* State  
* Contact Number  
* Office Manager

Office Types

* Head Office  
* Regional Office  
* Project Office  
* Sales Office

### Section 8 — Banking & Escrow Information

Displays financial information.

#### **Banking Information**

* Primary Bank  
* Account Name  
* Account Number *(masked except last four digits)*  
* SWIFT Code *(if applicable)*

#### **Escrow Information**

* Linked Financial Institutions  
* Active Escrow Accounts  
* Total Escrow Value  
* Latest Escrow Activity

Button

* View Escrow Management

### Section 9 — Company Documents

Displays organization-level documents.

#### **Categories**

* Certificate of Incorporation  
* RERA License  
* Tax Certificate  
* Memorandum & Articles  
* Board Resolution  
* Insurance Certificates  
* Compliance Certificates  
* Other Corporate Documents

#### **Table Columns**

| Column | Description |
| ----- | ----- |
| Document | Document name |
| Category | Document category |
| Verification Status | Current status |
| Expiry Date | If applicable |
| Action | View |

### Section 10 — Organization Settings

Displays organization configuration.

#### **Settings**

* Organization Time Zone  
* Default Language  
* Notification Preferences  
* Preferred Communication Method  
* Report Delivery Preference  
* Default Currency

Any of the four roles may modify these settings — there is no permission gate on this section, the same as every other section on this screen.

**Corrected 2026-08-15, second pass** — previously read "Only users with appropriate permissions can modify these settings," a leftover permission-scope statement inconsistent with this screen's own Access line and with the module's unified-access model. Removed rather than reworded, since there is no permission concept left for it to refer to.

### Section 11 — Audit Information

Displays administrative information.

#### **Information**

* Profile Created On  
* Created By  
* Last Updated  
* Last Updated By  
* Recent Profile Changes

Button

* View Complete Audit History

## Empty State

If the organization profile is incomplete:

**Message**

> Complete your company profile to maintain regulatory compliance and enable all RERA services.

Primary Button

* Complete Company Profile

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

The source material has no explicit Validation Summary section for this screen — no automated pre-submission validation panel is described, unlike the form screens elsewhere in this module.

## User Flow

Dashboard  
↓  
Company Profile

├── View Representatives

├── View Office Locations

├── View Company Documents

├── View Escrow Information

├── Edit Company Profile

└── View Audit History

## Notes

* This is the organization's **master profile page**, reachable and editable by any developer user — not a Principal-only screen. **Corrected 2026-08-15, second pass** — previously described as "the administrative profile page for the Developer Principal / Director," which contradicted this file's own Access line.
* It consolidates all corporate, regulatory, financial, and organizational information into a single interface.
* Sensitive financial information (such as bank account numbers) is partially masked for every user — this is a display convention protecting the data itself, not a permission distinction between users. **Corrected 2026-08-15, second pass** — previously "displayed only to authorized users," language that implied a permission tier that doesn't exist in this module.
* Changes to company information are captured in the audit trail, recording the acting user and the role they held at the time, to maintain regulatory accountability.
* This page serves as the authoritative source of organization-level information used throughout the RERA platform.
