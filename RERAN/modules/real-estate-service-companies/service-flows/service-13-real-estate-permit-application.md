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
  - "RERAN/modules/real-estate-service-companies/service-flows/service-12-real-estate-licensing-application.md"
tags:
  - real-estate-service-companies
  - service-flow
  - licensing
---

# Service #13 – Real Estate Permit Application

**Service Category:** Real Estate Licensing Services

**Source row:** 60 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Real Estate Permit Application** service issues advertisement permits to a licensed company — covering electronic, classified, billboard, and SMS advertisement types under one service, selected by a Permit Type field (`open-questions.md` A4), rather than four separate services.

> **Payment timing — flagged, building against source (`open-questions.md` B4).** Same pay-after-acceptance shape as Service #12; see that file's note for the full reasoning.

## 2. Purpose

Give a licensed company a regulated path to obtain permits for its advertising activity, with RERA reviewing and approving each permit type before it can be used.

## 3. Description

The company signs up or logs in, selects the permit type, fills in details, attaches supporting documents, and sends the application. RERA audits and sends notice of acceptance; the company then pays, and receives the permit e-certificate through the Digital system.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Brokerage Principal* — sourced directly (row 60).

## 5. Prerequisites

* The company holds a valid real estate licence (Service #12).
* Required permit details and supporting documents are available.

## 6. Required Information

### Company Information

* Company Licence Reference

### Permit Information

* Permit Type — Electronic / Classified / Billboard / SMS / Other
* Advertisement Content / Details
* Proposed Duration or Campaign Period

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation. Per `open-questions.md` A4, this is proposed as one service with a Permit Type field, not four separate services.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Sample / Proof of Advertisement Content
* Company Licence Certificate
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule. RERA sets this fee directly through configuration, per the same conclusion applied to Service #12.

## 9. Payment Required

**Yes — after audit and acceptance, before the permit e-certificate is issued.**

Sourced (row 60): "audit and acceptance; log in, select payment, pay; receive permit certificate via Digital system." Same Model 2 timing as Service #12. See Open Question B4.

## 10. Processing Authority

**Licensing & Registration Officer** (Group A) — sourced (approver column, row 60).

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**7 minutes.** Sourced from row 60.

## 12. Processing Workflow

Company User

Sign Up / Log In
↓
Select Permit Type
↓
Fill Advertisement Details
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
Receive Permit e-Certificate via Digital System

*Channel: All permit types — Land Department website (Digital system). Electronic, classified, billboard, and SMS advertisement permits specifically — also reachable via RERA App.*

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

* Payment Failed *(retryable)*
* Rejected
* Withdrawn

## 14. Possible Outcomes

* Permit Successfully Issued
* Additional Information Requested
* Application Rejected
* Payment Failed

## 15. Output

* **Permit e-Certificate** — sourced (row 60)
* Payment Receipt

## 16. Related Services

* Service #12 – Real Estate Licensing Application
* Service #14 – Issue Professional Practice Card

## 17. UI Screens

Not yet built — Phase 4.

## 18. API Requirements

* Validate Company Licence
* Submit Permit Application
* Upload Documents
* Retrieve Application Status
* Calculate Permit Fee
* Initiate Payment
* Verify Payment
* Generate Permit e-Certificate
* Send Notifications

## 19. Database Entities

* Company
* Company Licence
* Permit
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* A licensed company can apply for any of the sourced permit types through one service.
* System validates the company holds a valid licence before allowing the application.
* Payment is completed after acceptance and before the certificate is issued — unless Open Question B4 is resolved toward normalization.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a licensed company (Service #12) may apply for a permit.
2. All advertisement permit types are handled by this one service, differentiated by a Permit Type field — a design judgement (`open-questions.md` A4), not a sourced certainty.
3. Payment is required after acceptance and before the certificate is issued.
4. Every application receives a unique application reference number.
5. All submissions, reviews, payments, and notifications must be permanently recorded in the audit trail.

## Open Questions

1. **Should this service's payment timing be normalized to pay-before-lodging?** See `open-questions.md` B4.
2. **Whether the four advertisement permit types genuinely share one service or need splitting** — see `open-questions.md` A4. Medium confidence, reversible if wrong.
3. **Exact fee amount, and whether it varies by permit type.** Client data.
