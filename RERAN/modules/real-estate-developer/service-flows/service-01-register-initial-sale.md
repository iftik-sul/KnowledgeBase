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
  - "RERAN/modules/real-estate-developer/ui/screens/property-registrations.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
---

# Service #1 – Register Initial Sale

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Register Initial Sale** service allows a developer to register the provisional sale of a unit within a registered real estate project — the first regulatory record that a specific unit has been sold to a purchaser, ahead of full title transfer. It is the developer-side counterpart to the property-registration record a purchaser later relies on.

## 2. Purpose

Give RERA a timely, regulated record of provisional unit sales as they happen, so that project sales activity, purchaser protections, and eventual title transfer can all be tracked against a single source of truth.

## 3. Description

The developer selects the property (unit) within a registered project, fills in the sale and purchaser details, attaches supporting documents, selects a payment method, and submits the application online through the Real Estate Developers Portal. RERA issues a provisional registration e-certificate, delivered by e-mail to the purchaser.

> **Proposed** — the source describes the output as sent to the purchaser but does not say whether the developer also receives a copy in-app. Documenting an in-app copy to the submitting Registration Officer as the reasonable default; needs client confirmation.

## 4. Who Can Apply

* Project Registration Officer *(submits via the Property Registrations screen — see Section 16 note on role assignment)*

> **Source/UI role note.** The master table names "Sales & Disclosure Officer / Admin Officer" as the responsible role for this service. The matching UI screen, `property-registrations.md`, is scoped to the **Project Registration Officer's** sidebar in this module's UI documentation — Sales & Disclosure Officer's sidebar has no Property Registrations entry. Documenting both facts rather than resolving the discrepancy; flagged in the PR description as a source/UI role mismatch that applies to rows 1–7 and 19 alike.

## 5. Prerequisites

* Registered developer company account.
* Real estate project already registered with RERA (see Service #13).
* Property/unit exists within that project's approved unit list.
* Purchaser identified.
* Required supporting documents available.

## 6. Required Information

### Property Information

* Project Reference Number
* Unit/Property Identifier
* Unit Type and Specifications

### Purchaser Information

* Full Name
* National Identification Number (NIN)
* Contact Information

### Sale Information

* Sale Value
* Payment Plan / Terms
* Agreed Sale Date

## 7. Required Documents

> **Proposed** — not itemized in the source beyond "attach documents." List below follows the pattern used for equivalent Individual User sale-registration services; needs client confirmation.

* Provisional Sale Agreement
* Purchaser Government-issued Identification
* Proof of Initial Payment
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes** — the workflow selects a payment method before submission.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**6 business days**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Select "Register Initial Sale"
↓
Select Property (Unit)
↓
Fill Sale and Purchaser Details
↓
Attach Supporting Documents
↓
Select Payment Method
↓
Submit Application Online
↓
RERA Reviews Application
↓
Provisional Registration e-Certificate Issued
↓
Output Sent by E-mail to Purchaser

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

* Provisional Sale Successfully Registered
* Additional Information Requested
* Application Returned
* Application Rejected
* Payment Failed

## 15. Output

* Provisional Registration e-Certificate (e-mailed to purchaser)

## 16. Related Services

* Service #4 – Amend Initial Procedures Data
* Service #5 – Complete Initial Procedures Data
* Service #13 – Register Real Estate Project
* Individual User Service #6 – Register Property Sale *(cross-module: the purchaser-side counterpart once the sale is complete)*

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
* Submit Sale Registration Application
* Retrieve Application Status
* Generate Provisional Registration e-Certificate
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Property Unit
* Purchaser
* Property Sale
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can initiate a provisional sale registration for a unit within a registered project.
* System validates the unit belongs to a registered project and is available for sale.
* Required documents are uploaded before submission.
* Payment is completed before the application proceeds for review.
* Application receives a unique reference number.
* Approved applications generate a Provisional Registration e-Certificate.
* Purchaser receives the output by e-mail.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a unit belonging to a registered real estate project may be sold under this service.
2. Payment must be completed before the application proceeds for regulatory review.
3. The provisional registration e-certificate is the developer's evidence of a regulated sale record pending full title transfer.
4. Every application receives a unique application reference number.
5. All submissions, approvals, payments, and notifications must be permanently recorded in the audit trail.
