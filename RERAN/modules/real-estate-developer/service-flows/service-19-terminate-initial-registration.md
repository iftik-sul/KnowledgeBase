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
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
---

# Service #19 – Request Termination of Initial Registration

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Request Termination of Initial Registration** service allows a developer to formally end a provisional registration (sale, rent-to-own, or usufruct) before it is completed — for example where a purchaser withdraws or a transaction is cancelled by mutual agreement.

## 2. Purpose

Provide a regulated way to close out a provisional registration that will not proceed to completion, so the unit's status is accurately reflected in the registry.

## 3. Description

The developer opens the provisional registration record, selects termination, provides a reason, and submits. RERA reviews and, on approval, issues a procedure validation document confirming the termination.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Sales & Disclosure Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

> **Corrected 2026-08-15, second pass — the attribution was backwards.** This section previously said "typically filed by the Project Registration Officer," inherited from historical UI-screen sidebar scoping rather than checked against what the work actually is. This service terminates a Sales & Disclosure record (the provisional registration created by #1, #2, or #3) — `roles-and-responsibilities.md`'s Sales & Disclosure Officer worked example is the closer match. The master service table's Responsible Role column agrees: "Sales & Disclosure Officer" for this row. Checked systematically across all eight sale/lease/usufruct-registration services this applies to (#1–#7, #19). This has no access consequence: any of the four Group B roles may file this application regardless of which is "typical."

## 5. Prerequisites

* An existing provisional registration (Service #1, #2, or #3) not yet completed.
* Reason for termination.

## 6. Required Information

* Original Provisional Registration Reference Number
* Reason for Termination

## 7. Required Documents

> **Proposed** — the source names the output but not required inputs beyond a termination request. Needs client confirmation.

* Written Justification / Mutual Termination Agreement (where applicable)
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule. Paid through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Yes — before RERA's decision.** The source workflow places payment at the point of submission, ahead of any review: the developer selects a payment method and sends the application in one step. Paid per transaction through the shared platform payment gateway.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**8 hours 30 minutes**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Provisional Registration Record
↓
Select "Request Termination of Initial Registration"
↓
Provide Reason for Termination
↓
Pay Fees via Payment Gateway
↓
Submit Application Online
↓
RERA Reviews Application
↓
Procedure Validation Document Issued

## 13. Application Status Flow

Draft
↓
Payment Pending
↓
Payment Successful
↓
Submitted
↓
Under Review
↓
Approved
↓
Terminated

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Registration Successfully Terminated
* Additional Information Requested
* Application Returned
* Application Rejected

## 15. Output

* Procedure Validation Document (electronic form)

## 16. Related Services

* Service #1 – Register Initial Sale
* Service #2 – Register Initial Rent-to-Own
* Service #3 – Register Initial Usufruct
* Service #4 – Amend Initial Procedures Data

## 17. UI Screens

* Property Registration Details
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Provisional Registration
* Validate Termination Eligibility
* Submit Termination Application
* Retrieve Application Status
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Generate Procedure Validation Document
* Send Notifications

## 19. Database Entities

* Developer Company
* Provisional Registration
* Termination Record
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request termination of an existing, uncompleted provisional registration.
* System validates the target registration is eligible for termination.
* A reason for termination is required.
* Approved terminations generate a Procedure Validation Document.
* All activities are recorded in the audit log.
* Payment is completed at submission, before the application proceeds for review.

## 21. Business Rules

1. Only a provisional registration not yet completed may be terminated under this service.
2. A reason for termination is required for every submission.
3. Termination closes the provisional registration; it does not itself release any associated mortgage or escrow arrangement, which follow their own services.
4. All submissions, approvals, and notifications must be permanently recorded in the audit trail.
