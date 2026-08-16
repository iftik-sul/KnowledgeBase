---
project: RERAN
module: real-estate-service-companies
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-22-real-estate-licensing-application.md"
tags:
  - real-estate-service-companies
  - service-flow
  - licensing
---

# Service #12 – Real Estate Licensing Application

**Service Category:** Real Estate Licensing Services

**Source row:** 59 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Real Estate Licensing Application** service is how a real estate service company obtains the RERA licence required before it can operate any of the module's other services. This is the precondition every other Group D service assumes is already in place — the same relationship Real Estate Developer's Service #22 has to that module's Service #13.

> **Corrected 2026-08-16, by client decision (`open-questions.md` B4).** Row 59 sources payment happening *after* RERA's audit and acceptance ("audit and acceptance; log in, select payment, pay; receive registration notice"). The client has confirmed this normalizes to pay-before-lodging, matching the precedent set for Financial & Trust Institutions' #1, #12, and #18. Sections 9, 12, 13, 20, and 21 reflect the corrected sequence.

## 2. Purpose

Establish a real estate service company's regulatory standing to operate on the platform, before any of its other Group D services become available.

## 3. Description

The company signs up or logs in, fills in company details, attaches supporting documents, and pays the fee via the shared platform gateway before the application is submitted. RERA audits the application; on acceptance, the company receives a registration notice and — for free-zone licences only — a No-Objection Certificate (NOC) e-letter.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Brokerage Principal* — sourced directly (row 59's Responsible Role column), and confirmed reliable per `open-questions.md` A1.

## 5. Prerequisites

* The company is a registered legal entity, not yet RERA-licensed.
* Required company information and supporting documents are available.
* Payment has been completed via the shared platform gateway before the application is lodged.

## 6. Required Information

### Company Information

* Company Legal Name
* Company Registration Number
* Company Address
* Principal Contact Information
* Licence Type (Standard / Free Zone)

> **Proposed** — the source states only that "details" are filled in, without enumerating fields. Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Certificate of Incorporation
* Company Ownership / Directorship Details
* Government-issued Identification (Authorized Representative)
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> Per `payments.md`'s conclusion (adopted from Financial & Trust Institutions' B6), RERA sets this fee directly through the fee-schedule engine, independent of company size or transaction value. The exact fee is a configuration fact, not client data awaiting collection.

## 9. Payment Required

**Yes — upfront, via the shared platform gateway, before the application is lodged.**

**Corrected 2026-08-16, by client decision (`open-questions.md` B4)** — previously paid after audit and acceptance, following the sourced sequence; now paid before submission, matching Financial & Trust Institutions' comparable Service #1. See `payments.md` Model 2.

## 10. Processing Authority

**Licensing & Registration Officer** (Group A) — sourced (approver column, row 59), distinct from Compliance & Escrow Auditor, who approves most other Group D services.

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**5 minutes.** Sourced from row 59.

## 12. Processing Workflow

**Corrected 2026-08-16 — payment moved ahead of audit, by client decision.**

Company User

Sign Up / Log In
↓
Fill Company Details
↓
Attach Supporting Documents
↓
Pay via Shared Platform Gateway *(moved ahead of RERA's review, 2026-08-16)*
↓
Send Application Online

↓

RERA (Licensing & Registration Officer)

Audit Application
↓
Accept or Reject
↓
Send Registration Notice
↓
*(Free-Zone Licences Only)* Send NOC e-Letter

## 13. Application Status Flow

**Corrected 2026-08-16 — `Payment Pending` retired for this service, by client decision.**

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
Information Requested
↓
Returned for Correction
↓
Approved
↓
Completed

### Additional Statuses

* Payment Failed *(retryable, pre-lodging)*
* Rejected
* Withdrawn

**Superseded 2026-08-16.** This service previously carried a distinct "Accepted → Payment Pending → Payment Successful" tail, since payment followed acceptance. With payment now happening before lodging, that sequence collapses into the same Payment Pending / Payment Successful pattern used by every other upfront-paying service in the project.

## 14. Possible Outcomes

* Licence Successfully Issued
* Additional Information Requested
* Application Rejected
* Payment Failed

## 15. Output

* Registration Notice — sourced (row 59)
* NOC e-Letter *(free-zone licences only)* — sourced (row 59)
* Payment Receipt — issued at checkout, before the application was lodged

## 16. Related Services

* Service #13 – Real Estate Permit Application
* Service #19 – Accreditation of Training Entities
* Real Estate Developer Service #22 – Real Estate Licensing Application *(cross-module: the structurally equivalent service for Group B, same pay-after-decision-then-normalized precedent)*

## 17. UI Screens

* Services
* Real Estate Licensing Application
* Company Information
* Document Upload
* Payment
* Payment Successful
* Application Review
* Application Submitted
* Application Details
* Registration Confirmation

## 18. API Requirements

* Submit Licensing Application
* Upload Documents
* Calculate Licensing Fee
* Initiate Payment
* Verify Payment
* Retrieve Application Status
* Issue Registration Notice
* Issue NOC e-Letter *(free-zone only)*
* Send Notifications

## 19. Database Entities

* Company
* Company Licence
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* A company entity can apply for a real estate licence.
* System validates required company information and documents.
* Payment is completed via the shared platform gateway before the application is lodged. *(Corrected 2026-08-16 — previously "after acceptance and before the registration notice.")*
* Free-zone licences additionally receive an NOC e-letter.
* An application cannot be lodged or submitted for audit until payment succeeds.
* All activities are recorded in the audit log.

## 21. Business Rules

1. A company must hold this licence before any other Group D service becomes available to it.
2. Payment is made via the shared platform gateway, upfront, before the application can be lodged. **Corrected 2026-08-16** — previously required after acceptance; `open-questions.md` B4 moves this to upfront, before lodging.
3. A free-zone licence additionally requires an NOC e-letter, issued alongside the registration notice.
4. All submissions, reviews, payments, and notifications must be permanently recorded in the audit trail.

## Open Questions

1. **Eligibility criteria for licensing** are not enumerated in source. Client data.
2. **Exact fee amount.** Client data.
3. **What happens to the fee on a rejected application** (refund, forfeiture, or otherwise). Not addressed by any source document or by the payment-model correction itself — the same genuinely new question Financial & Trust Institutions' equivalent normalized services carry.
