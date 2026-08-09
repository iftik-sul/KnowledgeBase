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

# Screen: Property Registration Details

**Roles:** Registration Officer

The detail view of a single property registration, opened from [Property Registrations](property-registrations.md). Documented for the Registration Officer only — no other role has a version of this screen in the source material.

## Purpose

Provide the Project Registration Officer with a complete operational workspace to register an individual property under an approved development project. The officer can create and edit property information, upload supporting documents, validate required information, submit the registration to RERA, respond to regulatory queries, and track approval progress.

## Layout

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Property Registrations**  
* **Selected Item:** Property Registration Details *(opened from Property Registrations list)*  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * **Property Registrations (Active)**  
  * Applications  
  * Documents  
  * Reports  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Property Registration Details

**Subtitle:** Complete, validate, and submit this property registration for regulatory approval.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Save Draft  
* Submit to RERA *(Enabled only after validation passes)*  
* More Actions

Top Bar  
↓  
Property Header  
↓  
Registration Progress  
↓  
Property Information  
↓  
Ownership & Project Information  
↓  
Required Documents  
↓  
Validation Summary  
↓  
RERA Queries (if applicable)  
↓  
Activity Timeline

## Sections

### Section 1 — Property Header

Displays the registration summary.

#### **Left**

* Registration Number *(Draft until submitted)*  
* Property Name / Unit  
* Registration Status Badge  
* Linked Project

#### **Right**

* Created Date  
* Last Updated  
* Assigned Officer  
* Save Status

### Section 2 — Registration Progress

Display a horizontal workflow tracker.

#### **Stages**

* Draft  
* Property Information Completed  
* Documents Uploaded  
* Validation Passed  
* Submitted  
* Under Review  
* Approved

Completed stages use the platform's standard success indicator.

The current stage is highlighted.

Completed stages are clickable for quick navigation.

### Section 3 — Property Information

Editable registration form.

### **Basic Information**

* Property Name  
* Unit Number  
* Property Type  
* Development Project *(Read-only once selected)*  
* Block / Tower  
* Floor  
* Property Size  
* Number of Bedrooms *(if applicable)*  
* Number of Bathrooms *(if applicable)*  
* Parking Spaces  
* Property Description

### **Location Information**

* State  
* Local Government Area  
* Site Address  
* GPS Coordinates *(optional)*

### **Property Classification**

* Residential  
* Commercial  
* Mixed Use  
* Industrial  
* Other

### **Registration Information**

* Registration Category  
* Intended Use  
* Occupancy Status  
* Construction Status

### Section 4 — Ownership & Project Information

Display linked information.

### **Developer Information *(Read-only)***

* Developer Company  
* Developer Registration Number

### **Linked Project *(Read-only)***

* Project Name  
* Project ID  
* Project Status  
* Development Phase

Button

* View Project Details

### Section 5 — Required Documents

Document upload section.

Display all required documents with completion status.

#### **Example Documents**

* Approved Building Plan  
* Unit Layout / Floor Plan  
* Survey Plan  
* Inspection Report  
* Completion Certificate *(if applicable)*  
* Property Photographs  
* Utility Clearance *(if applicable)*  
* Other Supporting Documents

#### **Table**

| Document | Status | Uploaded On | Version | Action |
| :---: | :---: | :---: | :---: | :---: |

Actions

* Upload  
* Replace  
* Preview  
* Delete *(Draft only)*

### Section 6 — Validation Summary

See [validation-rules.md](../validation-rules.md) for the shared automatic-validation mechanism and the common field-level checks (required fields, required documents, file verification). This screen's own additional checks: Approved project selected, Duplicate property registration check, Unit number uniqueness, Address validation.

### Section 7 — RERA Queries

Visible only after RERA requests additional information.

#### **Table**

| Date | Request | Due Date | Status | Action |
| :---: | :---: | :---: | :---: | :---: |

Actions

* Respond  
* Upload Additional Documents  
* View Previous Response

Outstanding requests are visually highlighted.

### Section 8 — Activity Timeline

Display every activity performed on the registration.

Examples

* Registration created  
* Property information updated  
* Documents uploaded  
* Validation completed  
* Submitted to RERA  
* Information requested  
* Additional documents uploaded  
* Resubmitted  
* Registration approved  
* Registration certificate issued

Latest activities appear first.

## Empty State

If this is a newly created registration:

**Message**

> Complete the property information and upload all required supporting documents before submitting this registration to RERA.

Primary Button

* Complete Property Information

Secondary Button

* Upload Documents

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

See "Section 6 — Validation Summary" above.

## User Flow

Dashboard  
↓  
Property Registrations  
↓  
Property Registration Details

├── Edit Property Information

├── Upload Documents

├── Save Draft

├── Validate Registration

├── Submit to RERA

├── Respond to RERA Query

└── Download Registration Certificate (After Approval)

## Notes

* This is the **primary operational screen** for the **Project Registration Officer**.  
* A property can only be registered under an **approved development project**.  
* The officer can edit the registration freely while it remains in **Draft**.  
* Once submitted, the registration becomes read-only unless RERA returns it for correction or requests additional information.  
* After approval, the system should display the registration certificate and allow it to be downloaded.  
* Every modification, submission, document upload, and regulatory response should be recorded in the activity timeline to maintain a complete audit trail.

