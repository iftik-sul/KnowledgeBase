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

# Service #5 – Complete Initial Procedures Data

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Complete Initial Procedures Data** service allows a developer to supply the remaining data and documents needed to finalize a provisional registration (sale, rent-to-own, or usufruct) into a full title registration.

## 2. Purpose

Move a provisional registration to completion, issuing the full title records the provisional certificate stood in for.

## 3. Description

The developer opens the provisional registration record, provides any outstanding data and documents, and submits for final review. On approval, RERA issues the completed title documents: an Electronic Certificate of Title / Title Deed and an Electronic Map.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Sales & Disclosure Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

> **Corrected 2026-08-15, second pass — the attribution was backwards.** This section previously said "typically filed by the Project Registration Officer," inherited from historical UI-screen sidebar scoping rather than checked against what the work actually is. This service completes a Sales & Disclosure record (the provisional registration created by #1, #2, or #3) — `roles-and-responsibilities.md`'s Sales & Disclosure Officer worked example is the closer match. The master service table's Responsible Role column agrees: "Sales & Disclosure Officer / Admin Officer" for this row. Checked systematically across all eight sale/lease/usufruct-registration services this applies to (#1–#7, #19). This has no access consequence: any of the four Group B roles may file this application regardless of which is "typical."

## 5. Prerequisites

* An existing provisional registration (Service #1, #2, or #3) eligible for completion.
* Any outstanding required data and documents available.

## 6. Required Information

* Original Provisional Registration Reference Number
* Outstanding Data Fields (as requested by RERA, if any)

## 7. Required Documents

> **Proposed** — not itemized in the source beyond "complete the initial procedures data." Needs client confirmation.

* Any outstanding documents requested during provisional review
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule. Paid through the shared platform payment gateway, per transaction. There is no standing or pre-funded RERA-fee account for developers; each application is paid for on its own.

## 9. Payment Required

**Yes — before RERA's decision.** The source workflow places payment at the point of submission, ahead of any review: the developer selects a payment method and sends the application in one step. Paid per transaction through the shared platform payment gateway.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**6 business days**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Provisional Registration Record
↓
Select "Complete Initial Procedures Data"
↓
Provide Outstanding Data and Documents
↓
Select Payment Method
↓
Submit Completion Application
↓
RERA Reviews Application
↓
Electronic Certificate of Title / Title Deed Issued
↓
Electronic Map Issued

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
Completed

### Additional Statuses

* Information Requested
* Returned
* Rejected
* Cancelled

## 14. Possible Outcomes

* Registration Successfully Completed
* Additional Information Requested
* Application Returned
* Application Rejected
* Payment Failed

## 15. Output

* Electronic Certificate of Title / Title Deed
* Electronic Map

## 16. Related Services

* Service #1 – Register Initial Sale
* Service #2 – Register Initial Rent-to-Own
* Service #3 – Register Initial Usufruct
* Service #4 – Amend Initial Procedures Data

## 17. UI Screens

* Property Registration Details
* Document Upload
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Provisional Registration
* Validate Completion Eligibility
* Upload Documents
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Submit Completion Application
* Retrieve Application Status
* Generate Electronic Certificate of Title
* Generate Electronic Map
* Send Notifications

## 19. Database Entities

* Developer Company
* Provisional Registration
* Title Registration
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can submit a completion request against an eligible provisional registration.
* System validates the target registration is eligible for completion.
* Payment is completed before the completion request proceeds for review.
* Approved completions generate an Electronic Certificate of Title / Title Deed and Electronic Map.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a provisional registration in a completion-eligible status may be completed under this service.
2. Payment must be completed before the request proceeds for regulatory review.
3. Completion converts a provisional record into a full title registration.
4. All submissions, approvals, payments, and notifications must be permanently recorded in the audit trail.
