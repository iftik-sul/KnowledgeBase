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

# Service #14 – Issue Professional Practice Card

**Service Category:** Real Estate Licensing Services

**Source row:** 61 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Issue Professional Practice Card** service issues an official e-card to an agent working for a licensed real estate company, evidencing their professional standing to practice.

> **Corrected 2026-08-16, by client decision (`open-questions.md` B4).** Same normalization as Services #12/#13 — payment now happens upfront, before lodging, not after acceptance.

## 2. Purpose

Give individual agents at a licensed company a regulated, verifiable credential — the practice card — evidencing RERA's recognition of their standing to practice.

## 3. Description

The company signs up or logs in, fills in the agent's details, attaches supporting documents, pays via the shared platform gateway, and sends the application. RERA audits and, on acceptance, the card becomes printable from the system.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Brokerage Principal* — sourced directly (row 61).

## 5. Prerequisites

* The company holds a valid real estate licence (Service #12).
* The agent to be issued a card is identified and employed by the company.
* Required supporting documents are available.
* Payment has been completed via the shared platform gateway before the application is lodged.

## 6. Required Information

### Agent Information

* Full Name
* National Identification Number (NIN)
* Contact Information
* Position / Role at the Company

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Government-issued Identification (Agent)
* Evidence of Employment with the Company
* Passport Photograph
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes — upfront, via the shared platform gateway, before the application is lodged.**

**Corrected 2026-08-16, by client decision (`open-questions.md` B4)** — previously paid after audit and acceptance, before the card became printable; now paid before submission. See `payments.md` Model 2.

## 10. Processing Authority

**Licensing & Registration Officer** (Group A) — sourced (approver column, row 61).

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**5 minutes.** Sourced from row 61.

## 12. Processing Workflow

**Corrected 2026-08-16 — payment moved ahead of audit, by client decision.**

Company User

Sign Up / Log In
↓
Fill Agent Details
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
Card Printable from System

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

## 14. Possible Outcomes

* Card Successfully Issued
* Additional Information Requested
* Application Rejected
* Payment Failed

## 15. Output

* **E-Card** — sourced (row 61), printable from the system rather than emailed
* Payment Receipt — issued at checkout, before the application was lodged

## 16. Related Services

* Service #12 – Real Estate Licensing Application
* Service #15 – Renew Professional Practice Card
* Service #16 – Cancel Professional Practice Card
* Service #17 – Amend Professional Practice Card

## 17. UI Screens

* Services
* Issue Professional Practice Card
* Agent Information
* Document Upload
* Payment
* Payment Successful
* Application Review
* Application Submitted
* Application Details
* Card Issued

## 18. API Requirements

* Validate Company Licence
* Submit Card Issuance Application
* Upload Documents
* Calculate Card Fee
* Initiate Payment
* Verify Payment
* Retrieve Application Status
* Generate E-Card
* Send Notifications

## 19. Database Entities

* Company
* Agent
* Professional Practice Card
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* A licensed company can apply for a practice card on an agent's behalf.
* System validates the company holds a valid licence before allowing the application.
* Payment is completed via the shared platform gateway before the application is lodged. *(Corrected 2026-08-16.)*
* An application cannot be lodged or submitted for audit until payment succeeds.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a licensed company (Service #12) may apply for a practice card on an agent's behalf.
2. Payment is made via the shared platform gateway, upfront, before the application can be lodged. **Corrected 2026-08-16** — previously required after acceptance.
3. Every application receives a unique application reference number.
4. All submissions, reviews, payments, and notifications must be permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
2. **Card validity period** is not specified for issuance — Service #15 (Renewal) implies one exists, but the term itself is not sourced. Client data.
3. **Exact fee amount.** Client data.
