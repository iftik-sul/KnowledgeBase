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

# Service #2 – Register Initial Rent-to-Own

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Register Initial Rent-to-Own** service allows a developer to register the provisional lease-to-own arrangement of a unit within a registered project, giving RERA a regulatory record of the arrangement before the tenant-purchaser completes ownership.

## 2. Purpose

Provide a regulated, provisional record of lease-to-own (rent-to-own) arrangements at the point of initial agreement, protecting both the developer's and the tenant-purchaser's positions ahead of full transfer.

## 3. Description

The developer selects the property, records the tenant-purchaser and lease-to-own terms, attaches supporting documents, selects a payment method, and submits online. RERA reviews and issues a Provisional Lease-To-Own e-contract, delivered by e-mail to the tenant-purchaser.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Sales & Disclosure Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

> **Corrected 2026-08-15, second pass — the attribution was backwards.** This section previously said "typically filed by the Project Registration Officer," inherited from `property-registrations.md`'s old role-gated sidebar scoping rather than checked against what the work actually is. `roles-and-responsibilities.md`'s Sales & Disclosure Officer worked example describes exactly this kind of transaction — recording a sale/arrangement against a specific unit and buyer/lessee, uploading the agreement, submitting the disclosure — while the Project Registration Officer's own example describes creating a new project, an unrelated activity. The master service table's Responsible Role column agrees: "Sales & Disclosure Officer / Admin Officer" for this row. Checked systematically across all eight sale/lease/usufruct-registration services this applies to (#1–#7, #19). This has no access consequence: any of the four Group B roles may file this application regardless of which is "typical."

## 5. Prerequisites

* Registered developer company account.
* Real estate project already registered with RERA.
* Property/unit exists within that project's approved unit list.
* Tenant-purchaser identified.
* Required supporting documents available.

## 6. Required Information

### Property Information

* Project Reference Number
* Unit/Property Identifier

### Tenant-Purchaser Information

* Full Name
* National Identification Number (NIN)
* Contact Information

### Lease-to-Own Terms

* Total Contract Value
* Payment Schedule
* Lease Duration Before Ownership Transfer
* Agreed Start Date

## 7. Required Documents

> **Proposed** — not itemized in the source beyond "attach documents." Needs client confirmation.

* Provisional Lease-to-Own Agreement
* Tenant-Purchaser Government-issued Identification
* Proof of Initial Payment
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
Select "Register Initial Rent-to-Own"
↓
Select Property (Unit)
↓
Enter Tenant-Purchaser and Lease-to-Own Terms
↓
Attach Supporting Documents
↓
Select Payment Method
↓
Submit Application Online
↓
RERA Reviews Application
↓
Provisional Lease-To-Own e-Contract Issued
↓
Output Sent by E-mail to Tenant-Purchaser

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

* Provisional Lease-to-Own Successfully Registered
* Additional Information Requested
* Application Returned
* Application Rejected
* Payment Failed

## 15. Output

* Provisional Lease-To-Own e-Contract (e-mailed to tenant-purchaser)

## 16. Related Services

* Service #4 – Amend Initial Procedures Data
* Service #5 – Complete Initial Procedures Data
* Service #13 – Register Real Estate Project
* Individual User Service #10 – Register Lease-to-Own *(cross-module: the tenant-purchaser-side counterpart)*

## 17. UI Screens

* Property Registrations
* Property Registration Details
* Document Upload
* Payment
* Application Submitted

## 18. API Requirements

* Retrieve Project Units
* Validate Unit Availability
* Upload Documents
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Submit Lease-to-Own Registration Application
* Retrieve Application Status
* Generate Provisional Lease-To-Own e-Contract
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Property Unit
* Tenant-Purchaser
* Lease-to-Own Agreement
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can initiate a provisional lease-to-own registration for a unit within a registered project.
* System validates the unit belongs to a registered project and is available.
* Required documents are uploaded before submission.
* Payment is completed before the application proceeds for review.
* Application receives a unique reference number.
* Approved applications generate a Provisional Lease-To-Own e-Contract.
* Tenant-purchaser receives the output by e-mail.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a unit belonging to a registered real estate project may be offered under this service.
2. Payment must be completed before the application proceeds for regulatory review.
3. The provisional e-contract is evidence of a regulated lease-to-own arrangement pending eventual ownership transfer.
4. Every application receives a unique application reference number.
5. All submissions, approvals, payments, and notifications must be permanently recorded in the audit trail.
