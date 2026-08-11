---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-10
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
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

* Project Registration Officer *(see Service #1 §4 for the source/UI role-assignment note — applies identically here)*

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

Applicable according to the RERAN fee schedule.

## 9. Payment Required

Not specified in the source. **Proposed**: not required, since this is a cancellation rather than a new registration action; needs client confirmation.

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
Submit Application Online
↓
RERA Reviews Application
↓
Procedure Validation Document Issued

## 13. Application Status Flow

Draft
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
* Application Submitted

## 18. API Requirements

* Retrieve Provisional Registration
* Validate Termination Eligibility
* Submit Termination Application
* Retrieve Application Status
* Generate Procedure Validation Document
* Send Notifications

## 19. Database Entities

* Developer Company
* Provisional Registration
* Termination Record
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request termination of an existing, uncompleted provisional registration.
* System validates the target registration is eligible for termination.
* A reason for termination is required.
* Approved terminations generate a Procedure Validation Document.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a provisional registration not yet completed may be terminated under this service.
2. A reason for termination is required for every submission.
3. Termination closes the provisional registration; it does not itself release any associated mortgage or escrow arrangement, which follow their own services.
4. All submissions, approvals, and notifications must be permanently recorded in the audit trail.
