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

# Service #17 – Project Re-registration

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Project Re-registration** service allows a developer to re-register a project whose registration has lapsed or been cancelled, or that otherwise needs to be brought back into active registered status.

> **UI note.** This service, Service #14 (Cancellation), and Service #16 (Rename) are all documented against the same `project-details.md` screen, distinguished by which action within it is invoked. The screen does not name "Re-registration" separately from initial registration in the material read; this mapping is the closest reasonable fit, flagged rather than asserted with full confidence.

## 2. Purpose

Provide a path back to active registration for a project that has lapsed or been cancelled, without requiring the developer to originate a wholly new project record where the underlying project still exists.

## 3. Description

The developer submits a re-registration application referencing the prior project record, with updated survey confirmation where required. Project registration reviews the application; the Survey Department confirms current boundary and unit data before re-approval.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Project Registration Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* A prior project registration (active, lapsed, or cancelled) to re-register against.
* Updated survey data, where the prior survey is no longer current.

## 6. Required Information

* Prior Project Reference Number
* Reason for Re-registration
* Updated Unit/Survey Data (where applicable)

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Updated Survey Report
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule. Paid through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Yes — after RERA's decision.** The source workflow places the audit/accept-or-reject step *before* the fee is paid; payment is what releases the output, not what admits the application to review. Paid per transaction through the shared platform payment gateway. This is a genuine payment-timing exception, verified against this service's own source row rather than inferred from neighbouring services.

## 10. Processing Authority

**Compliance & Escrow Auditor** (project registration step); **Survey Department** (boundary/unit confirmation).

## 11. Expected Processing Time

**Project registration: 40 minutes; Survey department: 7 business days.**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Prior Project Record
↓
Select "Project Re-registration"
↓
Provide Updated Data and Reason
↓
Submit Application Online
↓
Project Registration Reviews Application
↓
Survey Department Confirms Current Data
↓
Pay Registration Fee via Payment Gateway
↓
Real Estate Project Approval Certificate Re-issued

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
Re-registered

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Project Successfully Re-registered
* Additional Information Requested
* Application Rejected

## 15. Output

* Real Estate Project Approval Certificate

## 16. Related Services

* Service #13 – Registration of Real Estate Project
* Service #14 – Real Estate Project Cancellation
* Service #16 – Changing the Name of a Real Estate Project

## 17. UI Screens

* Project Details *(shared with Services #14 and #16 — see the note in Section 1)*
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Prior Project Record
* Submit Re-registration Application
* Notify Survey Department
* Retrieve Survey Confirmation
* Retrieve Application Status
* Calculate Registration Fee
* Initiate Payment
* Verify Payment
* Generate Real Estate Project Approval Certificate
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Survey Report
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can submit a re-registration application referencing a prior project record.
* Survey Department confirms current data before re-approval.
* Approved re-registrations generate a Real Estate Project Approval Certificate.
* All activities are recorded in the audit log.
* Payment is completed after approval and before the certificate is re-issued.

## 21. Business Rules

1. A re-registration application must reference an existing prior project record.
2. Survey Department confirmation is required before re-registration is approved, independent of the project registration review.
3. All submissions, reviews, and notifications must be permanently recorded in the audit trail.
