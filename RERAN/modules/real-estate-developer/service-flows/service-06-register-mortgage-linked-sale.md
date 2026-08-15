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
  - "RERAN/modules/real-estate-developer/ui/screens/property-registrations.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
---

# Service #6 – Register Sale Associated with an Initial Mortgage

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Register Sale Associated with an Initial Mortgage** service allows a developer to register the provisional sale of a unit where the purchaser is financing the purchase through a mortgage, coordinating the sale record with the mortgage institution's provisional mortgage registration.

## 2. Purpose

Provide a regulated, provisional record of a mortgage-financed unit sale, linking the developer's sale record to the mortgage institution's provisional mortgage registration under a single project unit.

## 3. Description

The developer selects the property, records the purchaser and mortgage-institution details, attaches supporting documents, selects a payment method, and submits online. RERA reviews and issues a Mortgage Provisional Registration Certificate and an Electronic Map.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Project Registration Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* Registered developer company account.
* Real estate project already registered with RERA.
* Property/unit exists within that project's approved unit list.
* Purchaser and mortgage institution identified.
* Required supporting documents available.

## 6. Required Information

### Property Information

* Project Reference Number
* Unit/Property Identifier

### Purchaser Information

* Full Name
* National Identification Number (NIN)
* Contact Information

### Mortgage Information

* Mortgage Institution
* Mortgage Reference Number
* Mortgage Amount

## 7. Required Documents

> **Proposed** — not itemized in the source beyond "attach documents." Needs client confirmation.

* Provisional Sale Agreement
* Mortgage Offer Letter
* Purchaser Government-issued Identification
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
Select "Register Sale Associated with an Initial Mortgage"
↓
Select Property (Unit)
↓
Enter Purchaser and Mortgage Information
↓
Attach Supporting Documents
↓
Select Payment Method
↓
Submit Application Online
↓
RERA Reviews Application
↓
Mortgage Provisional Registration Certificate Issued
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
Registered

### Additional Statuses

* Information Requested
* Returned
* Rejected
* Cancelled

## 14. Possible Outcomes

* Mortgage-Linked Sale Successfully Registered
* Additional Information Requested
* Application Returned
* Application Rejected
* Payment Failed

## 15. Output

* Mortgage Provisional Registration Certificate
* Electronic Map

## 16. Related Services

* Service #1 – Register Initial Sale
* Service #4 – Amend Initial Procedures Data
* Service #5 – Complete Initial Procedures Data
* Financial & Trust Institutions Service #3 – Mortgage Registration *(cross-module: the mortgage institution's side of this same financing arrangement)*

## 17. UI Screens

* Property Registrations
* Property Registration Details
* Document Upload
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Project Units
* Validate Unit Availability
* Validate Mortgage Institution
* Upload Documents
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Submit Mortgage-Linked Sale Registration
* Retrieve Application Status
* Generate Mortgage Provisional Registration Certificate
* Generate Electronic Map
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Property Unit
* Purchaser
* Mortgage Institution
* Property Sale
* Mortgage
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can initiate a mortgage-linked sale registration for a unit within a registered project.
* System validates the unit belongs to a registered project and is available.
* Mortgage institution details are captured and validated.
* Required documents are uploaded before submission.
* Payment is completed before the application proceeds for review.
* Approved applications generate a Mortgage Provisional Registration Certificate and Electronic Map.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a unit belonging to a registered real estate project may be sold under this service.
2. A mortgage institution must be identified for the application to proceed.
3. Payment must be completed before the application proceeds for regulatory review.
4. Every application receives a unique application reference number.
5. All submissions, approvals, payments, and notifications must be permanently recorded in the audit trail.
