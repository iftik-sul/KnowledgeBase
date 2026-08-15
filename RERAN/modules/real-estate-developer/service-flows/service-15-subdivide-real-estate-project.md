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

# Service #15 – Real Estate Project Sub-division

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Real Estate Project Sub-division** service allows a developer to divide a registered real estate project into two or more sub-projects, each with its own project reference and unit set.

> **UI note — provisional match.** `ui/screens/project-details.md` does not name a "Sub-divide" action explicitly among its documented Sections; this service is mapped to Project Details on the basis that project-lifecycle actions live there generally, not because the screen names sub-division by name. Flagged as a provisional, not confirmed, mapping.

## 2. Purpose

Allow a project to be split into separately manageable sub-projects — for example where a large master-planned development is phased into distinct registered projects.

## 3. Description

The developer submits a sub-division request identifying the parent project and the proposed sub-project boundaries/unit allocations. RERA's project registration function processes the request, and the Survey Department conducts the underlying survey work to confirm boundaries before the sub-divided projects are approved.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Project Registration Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing registered project (Service #13).
* Proposed sub-division plan with unit allocations.

## 6. Required Information

* Parent Project Reference Number
* Proposed Sub-project Names
* Unit Allocation per Sub-project

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Proposed Sub-division Plan
* Updated Survey Data
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule. Paid through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Yes — after RERA's decision.** The source workflow places the audit/accept-or-reject step *before* the fee is paid; payment is what releases the output, not what admits the application to review. Paid per transaction through the shared platform payment gateway. This is a genuine payment-timing exception, verified against this service's own source row rather than inferred from neighbouring services.

## 10. Processing Authority

**Compliance & Escrow Auditor** (project registration step); **Survey Department** (boundary confirmation).

## 11. Expected Processing Time

**Project registration: 30 minutes; Survey department: 7 business days.**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Project Record
↓
Select "Request Sub-division"
↓
Provide Proposed Sub-division Plan
↓
Submit Application Online
↓
Project Registration Reviews Application
↓
Survey Department Confirms Boundaries
↓
Pay Registration Fee via Payment Gateway
↓
Real Estate Project Approval Certificate Issued for Each Sub-project

## 13. Application Status Flow

Draft
↓
Submitted
↓
Project Registration Review
↓
Survey Department Review
↓
Approved
↓
Payment Pending
↓
Payment Successful
↓
Sub-divided

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Project Successfully Sub-divided
* Additional Information Requested
* Application Rejected

## 15. Output

* Real Estate Project Approval Certificate (per resulting sub-project)

## 16. Related Services

* Service #13 – Registration of Real Estate Project
* Service #17 – Project Re-registration
* Service #26 – Separation or Annexing a Property *(the property-level equivalent of this project-level action — see the near-duplicate note in that service's Section 3)*

## 17. UI Screens

* Project Details *(provisional match — see Section 1)*
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Parent Project
* Submit Sub-division Application
* Notify Survey Department
* Retrieve Survey Confirmation
* Retrieve Application Status
* Calculate Registration Fee
* Initiate Payment
* Verify Payment
* Generate Real Estate Project Approval Certificate (per sub-project)
* Send Notifications

## 19. Database Entities

* Developer Company
* Parent Project
* Sub-project
* Survey Report
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request sub-division of an existing registered project.
* System validates the parent project and proposed unit allocation.
* Survey Department confirms boundaries before approval.
* Approved sub-divisions generate a Real Estate Project Approval Certificate per sub-project.
* All activities are recorded in the audit log.
* Payment is completed after approval and before the sub-project certificates are issued.

## 21. Business Rules

1. Only a registered project may be sub-divided under this service.
2. Survey Department confirmation is required before a sub-division is approved, independent of the project registration review.
3. Each resulting sub-project receives its own project reference number.
4. All submissions, reviews, and notifications must be permanently recorded in the audit trail.
