---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/payment-history.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - payments
---

# Feature #7 – Payment History

**Feature Category:** Shared Platform Features – Institution-Specific

## 1. Feature Overview

**Payment History** is a per-transaction reporting view of every payment the institution has made or is owed: receipts, amounts, service references, and status. It replaced a retired "Settlement Account" screen entirely — not corrected in place, but a different screen for a different model, since there is no standing pre-funded account left to display.

## 2. Purpose

Let any institution user see what has been paid, when, for which application, and whether a payment succeeded, failed, or is under refund review — a reporting view over completed and pending transactions, not an account to manage.

## 3. Description

Every payment record is tied to a specific application. No balance figure appears anywhere — there is nothing to fund and no low-balance state. The screen accounts for three distinct payment timings, not one: **upfront, before lodging** (Services #1, #3–#11), **at counter, before RERA's decision** (Services #13–#17), and **at counter, after RERA's decision** (Services #12, #18) — the last requiring an `Awaiting Payment` row that exists with no payment record at all until the counter payment clears. Service #2 carries no fee at all and produces no row.

## 4. Used By

All 18 Group C services, except Service #2 (no fee, no row):

* Mortgage Registration, Amendment, Transfer, Release (upfront)
* Grant Property Mortgage, Finance Lease Registration (upfront)
* Updating Title Deed Information, Split Ownership, Issuance of Title Deed (at counter, before decision)
* Registration of Real Estate Fund Companies, Contract Cancellation (at counter, after decision)

## 5. Prerequisites

* User is logged into a verified institution account.
* At least one payment has been made, or (for #12/#18) at least one application has reached Approved and is awaiting counter payment.

## 6. Required Information

Search/filter by: Application reference · Receipt reference · Service · Status (Successful / Failed / Refund Requested / Refunded / Awaiting Payment) · Payer (Institution / Customer) · Payment Timing (Upfront before lodging / At counter before decision / At counter after decision) · Date range · Amount range.

## 7. Required Documents

None to view. Payment Receipt (PDF, including VAT per answer B7) is downloadable per row once paid — not available for a row still Awaiting Payment.

## 8. Service Fee

No separate fee for using this feature. Fee amounts shown are configuration facts (`open-questions.md` B5), not fixed figures — the feature displays whatever the fee-schedule engine actually charged for a given transaction.

## 9. Payment Required

**No** — this is a read-only reporting screen. No action here initiates, retries, or reverses a payment; a failed upfront/at-counter-before-decision payment is retried from the originating service request itself, not from here. **What happens when a #12/#18 counter payment attempt fails, or the customer never returns, is not specified anywhere in the module** — flagged as an open gap, not resolved.

## 10. Processing Authority

**Any of the institution's four Group C roles** — no role or scope restriction; every user sees the same institution-wide history.

## 11. Expected Processing Time

Retrieval is immediate. Payment settlement timing follows the originating service's own model.

## 12. Processing Workflow

Dashboard
↓
Open Payment History
↓
Search / Filter (Service, Status, Payer, Payment Timing, Date, Amount)
↓
View Receipt (where paid) **or** View Application

## 13. Application Status Flow

Successful · Failed · Refund Requested · Refunded · **Awaiting Payment** *(Services #12/#18 only — populated on RERA approval, with Receipt Reference/Method/Paid left blank until the counter payment clears, then updated in place rather than creating a new row)*

## 14. Possible Outcomes

* Payment Successful / Failed
* Refund Requested / Refunded
* Approved, Awaiting Counter Payment *(#12/#18 only)*

## 15. Output

* Payment History table row per transaction
* Payment Receipt (PDF), where paid — institution/customer details, service, amount, VAT, method, gateway reference, timestamp

## 16. Related Features

* Service Requests *(where payment is initiated, per the originating service's own timing)*
* Applications *(the underlying application a payment is tied to)*

## 17. UI Screens

* Payment History
* Receipt Detail

## 18. API Requirements

* Retrieve Institution Payment History
* Retrieve Receipt Detail
* Retrieve Application Link
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Institution, Institution Staff, User
* Payment Transaction, Payment Receipt
* Application *(cross-referenced)*
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can view the full institution-wide payment history.
* No balance figure or account-management action appears anywhere on this feature.
* An Awaiting Payment row exists for approved #12/#18 applications with no payment yet, updating in place once payment clears rather than creating a new row.
* Service #2 never produces a row.
* Receipt download is unavailable for rows still Awaiting Payment.
* All access is recorded in the audit log.

## 21. Business Rules

1. This is a reporting feature, not an account — there is nothing to fund, no balance to project, and no low-balance state.
2. Three payment timings exist, not two: upfront before lodging, at counter before decision, at counter after decision (Services #12/#18 only).
3. Service #2 carries no fee and produces no payment record.
4. No action on this feature initiates, retries, or reverses a payment.
5. Refund status is display-only; the refund mechanism itself is unresolved and not asserted here.
6. What happens to a rejected application's already-paid fee is unresolved and not asserted here.
7. All payment records and access are permanently recorded in the audit trail.

## Open Questions

1. What happens when a #12/#18 counter payment attempt fails or the customer never returns? Not specified anywhere in the module.
2. What happens to the fee on a rejected application, for services where payment precedes the decision? Unresolved (`payments.md`'s To Confirm — Summary).
3. Which refund mechanism applies — the platform's public refund service or an institution-specific process? Unresolved (`open-questions.md` B10, superseded).
4. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
