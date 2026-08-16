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
  - "RERAN/modules/real-estate-service-companies/service-flows/service-23-permit-sell-by-public-auction.md"
tags:
  - real-estate-service-companies
  - service-flow
  - transaction
  - auction
---

# Service #24 – Register Property Sold by Auction

**Service Category:** Real Estate Transaction Services

**Source row:** 71 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Register Property Sold by Auction** service records the outcome of a public auction sale conducted under a valid permit (Service #23), issuing the resulting title documents once the sale is registered.

> **Payment model — Model 3, Upfront / Pay-Then-Output (`payments.md`).** This is the one Group D service where payment sits at the end of submission, immediately before output delivery, with no separate audit step named between them — structurally distinct from both Model 1 (no fee) and Model 2 (pay after decision) elsewhere in this module.

## 2. Purpose

Give RERA a regulated record of a property sold by public auction, issuing the buyer's title documents once the transaction is registered and paid for.

## 3. Description

The company signs up or logs in, selects the user type, selects the service, fills in details, attaches documents, pays the service fee, and receives the service outputs online.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Brokerage Principal* — sourced directly (row 71).

## 5. Prerequisites

* Registered RERAN Group D company account, holding a valid Permit to Sell by Public Auction (Service #23).
* The auction sale has taken place and its outcome is known.
* Required supporting documents are available.

## 6. Required Information

### Auction Sale Information

* Permit Reference (Service #23)
* Property Reference / Address
* Winning Bidder Information
* Sale Value
* Auction Date

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Auction Sale Record / Minutes
* Winning Bidder's Government-issued Identification
* Proof of Payment by the Bidder
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule. RERA sets this fee directly through configuration, per the same conclusion applied elsewhere in this module.

## 9. Payment Required

**Yes — sourced sequence is "attach docs → pay service fees → receive service outputs online."**

No separate audit step is named between payment and output delivery — payment is effectively the last user-facing action before the system delivers results. See `payments.md` Model 3.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 71).

## 11. Expected Processing Time

**25–30 minutes.** Sourced from row 71.

## 12. Processing Workflow

Company User

Sign Up / Log In
↓
Select User Type
↓
Select Service
↓
Fill Auction Sale Details
↓
Attach Documents
↓
Pay Service Fees
↓
Receive Service Outputs Online

## 13. Application Status Flow

Draft
↓
Payment Pending
↓
Payment Successful
↓
Submitted
↓
Completed

### Additional Statuses

* Payment Failed *(retryable, pre-lodging)*
* Rejected
* Withdrawn

> **Proposed** — sourced sequence places payment before output with no separate audit step named, so this status flow treats payment as effectively concluding the user-facing part of submission, with review (if any) happening automatically or between payment and output delivery. Flagged, not asserted with full confidence, since the source's brevity here could also represent an omitted audit step rather than a genuinely automatic process.

## 14. Possible Outcomes

* Auction Sale Successfully Registered
* Payment Failed

## 15. Output

* Certificate of Title / Title Deed — sourced (row 71)
* Map — sourced (row 71)
* Payment Receipts — sourced (row 71)

## 16. Related Services

* Service #23 – Permit to Sell by Public Auction

## 17. UI Screens

Not yet built — Phase 4.

## 18. API Requirements

* Validate Auction Permit
* Submit Auction Sale Registration
* Upload Documents
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Generate Certificate of Title / Title Deed
* Generate Map
* Send Notifications

## 19. Database Entities

* Company
* Auction Permit
* Property
* Auction Sale
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* A company holding a valid auction permit (Service #23) can register a completed auction sale.
* Required information and documents are validated before submission.
* Payment is completed before outputs are delivered.
* Approved registrations generate a Certificate of Title / Title Deed and Map.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a company holding a valid Permit to Sell by Public Auction (Service #23) may register a sale under this service.
2. Payment must be completed before outputs are delivered — sourced sequencing, no separate audit step described between payment and delivery.
3. Every registration receives a unique application reference number.
4. All submissions, payments, and notifications must be permanently recorded in the audit trail.

## Open Questions

1. **Whether a review/audit step genuinely happens between payment and output delivery**, or the process is truly as automatic as the source's brevity suggests. Client data.
2. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
3. **Exact fee amount.** Client data.
