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

# Service #14 – Real Estate Project Cancellation

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Real Estate Project Cancellation** service allows a developer to formally deregister a real estate project — for example where the project is abandoned before any units are sold, or the developer withdraws it for other reasons.

## 2. Purpose

Provide a regulated way to close out a registered project that will not proceed, so its status is accurately reflected in the registry and its reference number is not left open indefinitely.

## 3. Description

The developer opens the project record, selects cancellation, provides a reason, and submits. RERA reviews and, on approval, issues a Real Estate Project Deregistration Certificate.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Project Registration Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing registered project (Service #13).
* No active property-level registrations or escrow accounts outstanding against the project — **proposed**, not stated explicitly in the source; needs client confirmation of whether cancellation is blocked by outstanding sub-records.
* Reason for cancellation.

## 6. Required Information

* Project Reference Number
* Reason for Cancellation

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Written Justification for Cancellation
* Other supporting documents required by RERA

## 8. Service Fee

**No RERA service fee is sourced for this service.** The source workflow contains no payment step.

## 9. Payment Required

**No.** Not required at any point in the sourced workflow. Should the client confirm a fee applies, it would be paid per transaction through the shared platform payment gateway — **proposed**, needs client confirmation.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**15 minutes**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Project Record
↓
Select "Request Project Cancellation"
↓
Provide Reason for Cancellation
↓
Submit Application Online
↓
RERA Reviews Application
↓
Real Estate Project Deregistration Certificate Issued

## 13. Application Status Flow

Draft
↓
Submitted
↓
Under Review
↓
Approved
↓
Deregistered

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Project Successfully Cancelled/Deregistered
* Additional Information Requested
* Application Rejected

## 15. Output

* Real Estate Project Deregistration Certificate (e-certificate)

## 16. Related Services

* Service #13 – Registration of Real Estate Project
* Service #17 – Project Re-registration

## 17. UI Screens

* Project Details
* Application Submitted

## 18. API Requirements

* Retrieve Project
* Validate Cancellation Eligibility
* Submit Cancellation Application
* Retrieve Application Status
* Generate Real Estate Project Deregistration Certificate
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Cancellation Record
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request cancellation of an existing registered project.
* A reason for cancellation is required.
* Approved cancellations generate a Real Estate Project Deregistration Certificate.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a registered project may be cancelled under this service.
2. A reason for cancellation is required for every submission.
3. Cancellation deregisters the project; a subsequent registration under the same details would use Service #13 or #17, not this one.
4. All submissions, approvals, and notifications must be permanently recorded in the audit trail.
