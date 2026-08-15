---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/ui/screens/project-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
---

# Service #16 – Changing the Name of a Real Estate Project

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Changing the Name of a Real Estate Project** service allows a developer to rename a registered project — for example following a rebrand — without affecting its underlying registration or unit set.

> **Confirmed overlap with Service #24 — client-confirmed 2026-08-15, issue #37.** A name change may also be submitted as one of the fields on Service #24 (Register/Amend Project Details). Neither service is the exclusive path — this one is the narrow, no-fee, name-only route; #24 is the broader route when a name change accompanies other project detail changes. Whichever the developer selects is what's recorded.

## 2. Purpose

Keep a project's registered name current, so RERA's public-facing project records and the developer's marketing remain consistent.

## 3. Description

The developer opens the project record, provides the new name and a reason, and submits. RERA reviews and, on approval, issues an updated Real Estate Project Approval Certificate reflecting the new name.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Project Registration Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing registered project (Service #13).
* Proposed new project name.

## 6. Required Information

* Project Reference Number
* Current Project Name
* Proposed New Project Name
* Reason for Name Change

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Board Resolution or Equivalent Authorization for the Name Change (where applicable)
* Other supporting documents required by RERA

## 8. Service Fee

**No RERA service fee is sourced for this service.** The source workflow contains no payment step.

## 9. Payment Required

**No.** Not required at any point in the sourced workflow. Should the client confirm a fee applies, it would be paid per transaction through the shared platform payment gateway — **proposed**, needs client confirmation.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**30 minutes**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Project Record
↓
Select "Change Project Name"
↓
Enter New Name and Reason
↓
Submit Application Online
↓
RERA Reviews Application
↓
Updated Real Estate Project Approval Certificate Issued

## 13. Application Status Flow

Draft
↓
Submitted
↓
Under Review
↓
Approved
↓
Renamed

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Project Name Successfully Changed
* Additional Information Requested
* Application Rejected

## 15. Output

* Updated Real Estate Project Approval Certificate

## 16. Related Services

* Service #13 – Registration of Real Estate Project
* Service #17 – Project Re-registration
* Service #24 – Register/Amend Real Estate Project Details *(confirmed overlap — either route may be used for a name change; see Section 1)*

## 17. UI Screens

* Project Details
* Application Submitted

## 18. API Requirements

* Retrieve Project
* Submit Name Change Application
* Retrieve Application Status
* Generate Updated Real Estate Project Approval Certificate
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Name Change Record
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request a name change for an existing registered project.
* A reason for the change is required.
* Approved name changes generate an updated Real Estate Project Approval Certificate.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a registered project's name may be changed under this service.
2. A reason for the name change is required for every submission.
3. The project's reference number and unit set are unaffected by a name change.
4. **A name change may also be submitted through Service #24 — client-confirmed 2026-08-15, issue #37.** Neither is the exclusive path.
5. All submissions, approvals, and notifications must be permanently recorded in the audit trail.
