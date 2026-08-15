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

# Service #3 – Register Initial Usufruct

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Register Initial Usufruct** service allows a developer to register a provisional usufruct right — the right to use and benefit from a unit without owning it outright — granted over a unit within a registered project.

## 2. Purpose

Provide a regulated, provisional record of usufruct grants at the point of initial agreement, ahead of the usufruct holder's registration being finalized.

## 3. Description

The developer selects the property, records the usufructuary's details and the scope/duration of the right, attaches supporting documents, selects a payment method, and submits online. RERA reviews and issues a Usufruct Registration e-Certificate.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Sales & Disclosure Officer.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

> **Corrected 2026-08-15, second pass — the attribution was backwards.** This section previously said "typically filed by the Project Registration Officer," inherited from `property-registrations.md`'s old role-gated sidebar scoping rather than checked against what the work actually is. `roles-and-responsibilities.md`'s Sales & Disclosure Officer worked example describes exactly this kind of transaction — recording a grant/arrangement against a specific unit and beneficiary, uploading the agreement, submitting the disclosure — while the Project Registration Officer's own example describes creating a new project, an unrelated activity. The master service table's Responsible Role column agrees: "Sales & Disclosure Officer / Admin Officer" for this row. Checked systematically across all eight sale/lease/usufruct-registration services this applies to (#1–#7, #19). This has no access consequence: any of the four Group B roles may file this application regardless of which is "typical."

## 5. Prerequisites

* Registered developer company account.
* Real estate project already registered with RERA.
* Property/unit exists within that project's approved unit list.
* Usufructuary identified.
* Required supporting documents available.

## 6. Required Information

### Property Information

* Project Reference Number
* Unit/Property Identifier

### Usufructuary Information

* Full Name
* National Identification Number (NIN)
* Contact Information

### Usufruct Terms

* Scope of Right
* Effective Date
* Duration / Expiry (if applicable)

## 7. Required Documents

> **Proposed** — not itemized in the source beyond "attach documents." Needs client confirmation.

* Usufruct Grant Agreement
* Usufructuary Government-issued Identification
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
Select "Register Initial Usufruct"
↓
Select Property (Unit)
↓
Enter Usufructuary Information and Terms
↓
Attach Supporting Documents
↓
Select Payment Method
↓
Submit Application Online
↓
RERA Reviews Application
↓
Usufruct Registration e-Certificate Issued
↓
Output Sent by E-mail

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

* Usufruct Successfully Registered
* Additional Information Requested
* Application Returned
* Application Rejected
* Payment Failed

## 15. Output

* Usufruct Registration e-Certificate

## 16. Related Services

* Service #4 – Amend Initial Procedures Data
* Service #5 – Complete Initial Procedures Data
* Service #13 – Register Real Estate Project
* Individual User Service #14 – Register Usufruct Right *(cross-module: the usufructuary-side counterpart)*

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
* Submit Usufruct Registration Application
* Retrieve Application Status
* Generate Usufruct Registration e-Certificate
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Property Unit
* Usufructuary
* Usufruct Grant
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can initiate a provisional usufruct registration for a unit within a registered project.
* System validates the unit belongs to a registered project.
* Required documents are uploaded before submission.
* Payment is completed before the application proceeds for review.
* Application receives a unique reference number.
* Approved applications generate a Usufruct Registration e-Certificate.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a unit belonging to a registered real estate project may be subject to this service.
2. Payment must be completed before the application proceeds for regulatory review.
3. Every application receives a unique application reference number.
4. All submissions, approvals, payments, and notifications must be permanently recorded in the audit trail.
