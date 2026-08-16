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

> **Payment timing — flagged, building against source, not pre-emptively normalized (`open-questions.md` B4).** This service's sourced sequence pays *after* audit and acceptance, the same shape Financial & Trust Institutions' Service #1 had before its 2026-08-15 client normalization to pay-before-lodging. Whether the client wants the same normalization applied here is an open question, not assumed either way in this document.

## 2. Purpose

Establish a real estate service company's regulatory standing to operate on the platform, before any of its other Group D services become available.

## 3. Description

The company signs up or logs in, fills in company details, attaches supporting documents, and sends the application. RERA audits and sends notice of acceptance. The company then logs in, selects payment, and pays; on payment, the company receives a registration notice and — for free-zone licences only — a No-Objection Certificate (NOC) e-letter.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Brokerage Principal* — sourced directly (row 59's Responsible Role column), and confirmed reliable per `open-questions.md` A1: Group D's Responsible Role column holds up cleanly, unlike Group B's or Group C's.

## 5. Prerequisites

* The company is a registered legal entity, not yet RERA-licensed.
* Required company information and supporting documents are available.

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

> Per `payments.md`'s B2-equivalent conclusion (adopted from Financial & Trust Institutions' B6), RERA sets this fee directly through the fee-schedule engine, independent of company size or transaction value. The exact fee is a configuration fact, not client data awaiting collection.

## 9. Payment Required

**Yes — after audit and acceptance, before the registration notice is issued.**

Sourced (row 59): "audit and acceptance; log in, select payment, pay; receive registration notice." Payment is the step immediately before output delivery, not the first step of submission. See `payments.md` Model 2 and Open Question B4 for the normalization question this timing raises.

## 10. Processing Authority

**Licensing & Registration Officer** (Group A) — sourced (approver column, row 59), distinct from Compliance & Escrow Auditor, who approves most other Group D services.

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**5 minutes.** Sourced from row 59.

## 12. Processing Workflow

Company User

Sign Up / Log In
↓
Fill Company Details
↓
Attach Supporting Documents
↓
Send Application Online

↓

RERA (Licensing & Registration Officer)

Audit Application
↓
Accept or Reject
↓
Send Notice of Acceptance

↓

Company User

Log In
↓
Select Payment
↓
Pay Fees
↓
Receive Registration Notice
↓
*(Free-Zone Licences Only)* Receive NOC e-Letter

## 13. Application Status Flow

Draft
↓
Submitted
↓
Under Review
↓
Information Requested
↓
Returned for Correction
↓
Accepted
↓
Payment Pending
↓
Payment Successful
↓
Completed

### Additional Statuses

* Payment Failed *(retryable — the application itself has already been accepted at this point; only the payment step needs retrying)*
* Rejected
* Withdrawn

## 14. Possible Outcomes

* Licence Successfully Issued
* Additional Information Requested
* Application Rejected
* Payment Failed

## 15. Output

* Registration Notice — sourced (row 59)
* NOC e-Letter *(free-zone licences only)* — sourced (row 59)
* Payment Receipt — issued once payment succeeds, matching every other fee-bearing service in the project

## 16. Related Services

* Service #13 – Real Estate Permit Application
* Service #19 – Accreditation of Training Entities
* Real Estate Developer Service #22 – Real Estate Licensing Application *(cross-module: the structurally equivalent service for Group B, same pay-after-decision-then-normalized precedent)*

## 17. UI Screens

Not yet built — Phase 4.

## 18. API Requirements

* Submit Licensing Application
* Upload Documents
* Retrieve Application Status
* Calculate Licensing Fee
* Initiate Payment
* Verify Payment
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
* Payment is completed after acceptance and before the registration notice is issued — unless Open Question B4 is resolved toward normalization, in which case this criterion updates to match.
* Free-zone licences additionally receive an NOC e-letter.
* All activities are recorded in the audit log.

## 21. Business Rules

1. A company must hold this licence before any other Group D service becomes available to it.
2. Payment is required after acceptance and before the registration notice is issued — sourced sequencing, flagged as a normalization candidate (B4), not pre-emptively changed.
3. A free-zone licence additionally requires an NOC e-letter, issued alongside the registration notice.
4. All submissions, reviews, payments, and notifications must be permanently recorded in the audit trail.

## Open Questions

1. **Should this service's payment timing be normalized to pay-before-lodging**, matching Financial & Trust Institutions' #1/#12/#18 precedent? See `open-questions.md` B4 — the central open question this service and #13–#15 share.
2. **Eligibility criteria for licensing** are not enumerated in source. Client data.
3. **Exact fee amount.** Client data.
