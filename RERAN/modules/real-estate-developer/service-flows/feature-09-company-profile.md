---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/company-profile.md"
tags:
  - real-estate-developer
  - shared-feature
  - company-profile
---

# Feature #9 – Company Profile

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

**Company Profile** is the organization's master profile: corporate information, RERA registration and license status, corporate structure, authorized representatives, office locations, banking/escrow information, company-level documents, and organization settings.

## 2. Purpose

Give any developer user a centralized, editable view of the organization's regulatory standing and corporate information — the authoritative source of organization-level information used throughout the module.

## 3. Description

Unlike every other domain and general-platform screen in this module, this screen had **only one design in source** — no role variant to merge, and so it was missed by the earlier access-model correction pass that touched the other fifteen. A second pass on 2026-08-15 found and removed a leftover permission-scope statement ("Only users with appropriate permissions can modify these settings") and Principal-only framing in the Purpose and Notes sections, bringing this screen in line with its own Access line, which already said "all four roles." Masked banking details (account number, last four digits visible) are a display convention protecting the data itself, not a permission distinction between users — corrected from language that implied otherwise.

## 4. Used By

Not tied to any single numbered service — the organization's standing document, referenced across the module (e.g. escrow figures cross-reference Escrow Management; RERA license status feeds the Dashboard's Compliance & Standing Focus Area).

## 5. Prerequisites

* User is logged into a registered developer company account.

## 6. Required Information

None to view. To edit: whichever section's fields are being updated (organization details, contact information, RERA registration, corporate information, representatives, office locations, banking information, settings).

## 7. Required Documents

Company-level documents: Certificate of Incorporation, RERA License, Tax Certificate, Memorandum & Articles, Board Resolution, Insurance Certificates, Compliance Certificates.

## 8. Service Fee

No fee for viewing or editing the profile itself.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the developer's four Group B roles**, unrestricted — confirmed both by this screen's own Access line and by the 2026-08-15 second-pass correction removing the leftover permission gate.

## 11. Expected Processing Time

Edits are immediate. **Confirmed 2026-08-16 — no Validation Summary is needed here, by client decision.** The absence noted in the previous version of this document is not a gap: this is a profile-editing screen, not a submission-based service, and the module's Validation Summary pattern exists specifically for pre-submission checks (required fields, required documents, cross-service consistency) that don't apply to editing a standing record.

## 12. Processing Workflow

Dashboard
↓
Open Company Profile
↓
View Company Header, Summary Cards, and any section
↓
Edit Company Profile *(any section, any user)* **or** Download Company Profile **or** View Audit Log
↓
*(on Edit)* Changes Saved, Recorded in Audit Trail with Acting User and Role

## 13. Application Status Flow

Not a submission-based feature — no application status flow. RERA License Status itself carries its own vocabulary (Active / Suspended / Expired), tracked as a field on this screen rather than a workflow this feature drives.

## 14. Possible Outcomes

* Profile Section Updated
* Company Profile Downloaded
* Audit History Viewed

## 15. Output

* Updated profile record
* Downloadable Company Profile document
* Audit trail entry per change, with acting user and role

## 16. Related Features

* Escrow Management *(Section 8's Banking & Escrow Information links out to it)*
* Dashboard *(Compliance & Standing Focus Area references RERA License Status and organization standing from here)*

## 17. UI Screens

* Company Profile

## 18. API Requirements

* Retrieve Company Profile (all sections)
* Update Company Profile (per section)
* Retrieve Authorized Representatives, Office Locations, Company Documents
* Retrieve Audit History
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Developer Company, User
* Authorized Representative, Office Location
* Banking Information, Escrow Summary *(cross-referenced from Escrow Management)*
* Company Document
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can view and edit every section of this feature.
* Masked banking information is masked identically for every user — a display convention, not a permission tier.
* All profile changes are recorded in the audit log with acting user and role.
* Escrow figures shown here match Escrow Management's own figures exactly.
* No pre-submission Validation Summary panel is required for this screen.

## 21. Business Rules

1. Any of the developer's four Group B roles may view or edit any section of this feature — no permission gate on any section, including Organization Settings.
2. Sensitive financial data (bank account numbers) is masked identically for every user, protecting the data itself rather than distinguishing between users.
3. All changes are permanently recorded in the audit trail, including the acting user's role.
4. This feature is the authoritative source of organization-level information used elsewhere in the module.
5. **Decided 2026-08-16.** This is a profile-editing screen, not a submission service — no Validation Summary panel is needed, unlike the module's form screens.

## Open Questions

1. ~~Is the absence of a Validation Summary a gap?~~ **Decided 2026-08-16 — no, not applicable to a profile page.**
2. Same adoption question as Feature #1 — needs client confirmation.
