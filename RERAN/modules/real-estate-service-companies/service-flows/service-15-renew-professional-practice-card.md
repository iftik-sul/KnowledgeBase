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
  - "RERAN/modules/real-estate-service-companies/service-flows/service-14-issue-professional-practice-card.md"
tags:
  - real-estate-service-companies
  - service-flow
  - licensing
---

# Service #15 – Renew Professional Practice Card

**Service Category:** Real Estate Licensing Services

**Source row:** 62 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Renew Professional Practice Card** service renews an agent's existing practice card before or after its expiry, with **automatic approval** — the one Group D licensing service sourced as not requiring manual RERA review.

> **Corrected 2026-08-16, by client decision (`open-questions.md` B4).** Same normalization as Services #12–#14 — payment now happens upfront, before submission, not after the automatic approval. With payment moved ahead of the (already-automatic, effectively instantaneous) approval, this service's workflow simplifies more than #12–#14's did: there is no longer a meaningful gap between payment and approval for a status to sit in.

## 2. Purpose

Keep an agent's professional practice card current without requiring the same manual audit the original issuance (Service #14) goes through, since renewal presumes the agent's standing is already established.

## 3. Description

The company signs up or logs in, fills in details, attaches documents, and pays via the shared platform gateway; approval is automatic on submission, and the renewed card becomes printable from the system immediately.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Brokerage Principal* — sourced directly (row 62).

## 5. Prerequisites

* An existing professional practice card (Service #14) to be renewed.
* Required supporting documents are available.
* Payment has been completed via the shared platform gateway before the application is lodged.

## 6. Required Information

### Card Reference

* Existing Card Number
* Agent Name

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Existing Practice Card
* Updated Government-issued Identification (if changed)
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes — upfront, via the shared platform gateway, before the application is lodged and before automatic approval.**

**Corrected 2026-08-16, by client decision (`open-questions.md` B4)** — previously paid after automatic approval, before the renewed card became printable; now paid before submission. See `payments.md` Model 2.

## 10. Processing Authority

**Licensing & Registration Officer** (Group A) — sourced (approver column, row 62), though the approval itself is automatic per the workflow text, not a manual review by this role. **Proposed**: the role is retained as the system-of-record authority even where approval is automated, consistent with how the source attributes an approver to every row regardless of whether review is manual.

## 11. Expected Processing Time

**Automatic approval.** Sourced from row 62 — the only Group D service with this designation rather than a time figure.

## 12. Processing Workflow

**Corrected 2026-08-16 — payment moved ahead of submission, by client decision.**

Company User

Sign Up / Log In
↓
Fill Renewal Details
↓
Attach Supporting Documents
↓
Pay via Shared Platform Gateway *(moved ahead of submission, 2026-08-16)*
↓
Send Application Online
↓
*(Automatic Approval)*
↓
Renewed Card Printable from System

*Channel: Land Department website (Digital system); RERA App.*

## 13. Application Status Flow

**Corrected 2026-08-16 — payment now precedes the automatic approval, by client decision.**

Draft
↓
Payment Pending
↓
Payment Successful
↓
Submitted
↓
Approved *(automatic)*
↓
Completed

### Additional Statuses

* Payment Failed *(retryable, pre-lodging)*
* Withdrawn

**Note:** `Under Review`, `Information Requested`, and `Returned for Correction` are still omitted, consistent with the sourced automatic-approval reading — unaffected by the payment-timing correction. `Rejected` remains omitted for the same reason given previously: an automatically-approved application has no rejection path sourced.

## 14. Possible Outcomes

* Card Successfully Renewed
* Payment Failed

## 15. Output

* **Renewed E-Card** — sourced (row 62)
* Payment Receipt — issued at checkout, before the application was lodged

## 16. Related Services

* Service #14 – Issue Professional Practice Card
* Service #16 – Cancel Professional Practice Card
* Service #17 – Amend Professional Practice Card

## 17. UI Screens

* Services
* Renew Professional Practice Card
* Card Reference
* Payment
* Payment Successful
* Application Submitted
* Renewed Card Confirmation

## 18. API Requirements

* Retrieve Existing Card Record
* Calculate Renewal Fee
* Initiate Payment
* Verify Payment
* Submit Renewal Application
* Auto-Approve Renewal
* Generate Renewed E-Card
* Send Notifications

## 19. Database Entities

* Company
* Agent
* Professional Practice Card
* Card Renewal
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* A company can renew an existing practice card on an agent's behalf.
* Payment is completed via the shared platform gateway before the application is lodged. *(Corrected 2026-08-16.)*
* Renewal is automatically approved on submission, without a manual review step.
* An application cannot be lodged until payment succeeds.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an existing practice card (Service #14) may be renewed under this service.
2. Payment is made via the shared platform gateway, upfront, before the application can be lodged. **Corrected 2026-08-16** — previously required after automatic approval.
3. Renewal approval is automatic — sourced, no manual review step.
4. Every renewal receives a unique application reference number.
5. All submissions, payments, and notifications must be permanently recorded in the audit trail.

## Open Questions

1. **Whether an automatically-approved application can ever be rejected or returned** — the source's silence on this is treated as "no," but this is an inference, not a stated fact. Client data.
2. **Card renewal window** (how far before/after expiry renewal is available) is not specified in source.
3. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
4. **Exact fee amount.** Client data.
