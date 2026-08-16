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

Every payment record is tied to a specific application. No balance figure appears anywhere — there is nothing to fund and no low-balance state. The screen accounts for two payment timings: **upfront, before lodging** (Services #1, #3–#11) and **at counter, before RERA's decision** (Services #12–#18). Service #2 carries no fee at all and produces no row.

**Corrected 2026-08-16.** This feature previously distinguished a third timing — "at counter, after RERA's decision," for Services #12 and #18 — and built a dedicated `Awaiting Payment` row status around it, populated on RERA approval with the receipt fields left blank until the counter payment cleared. The client has since reviewed that #12/#18 exception directly, confirmed it was an artefact of the source's original physical-counter process rather than intentional design, and normalized both services to pay before RERA's decision, the same as #13–#17. That row status, and the payment-failure-and-non-return scenario it created, are both retired below — every payment record in this module now follows the same shape: it exists because a payment happened, not because an approval is waiting on one.

## 4. Used By

All 18 Group C services, except Service #2 (no fee, no row):

* Mortgage Registration, Amendment, Transfer, Release (upfront)
* Grant Property Mortgage, Finance Lease Registration (upfront)
* Registration of Real Estate Fund Companies, Updating Title Deed Information, Split Ownership, Issuance of Title Deed, Contract Cancellation (at counter, before decision)

## 5. Prerequisites

* User is logged into a verified institution account.
* At least one payment has been made.

## 6. Required Information

Search/filter by: Application reference · Receipt reference · Service · Status (Successful / Failed / Refund Requested / Refunded) · Payer (Institution / Customer) · Payment Timing (Upfront before lodging / At counter before decision) · Date range · Amount range.

## 7. Required Documents

None to view. Payment Receipt (PDF, including VAT per answer B7) is downloadable per row once paid.

## 8. Service Fee

No separate fee for using this feature. Fee amounts shown are configuration facts (`open-questions.md` B5), not fixed figures — the feature displays whatever the fee-schedule engine actually charged for a given transaction.

## 9. Payment Required

**No** — this is a read-only reporting screen. No action here initiates, retries, or reverses a payment; a failed payment is retried from the originating service request itself, not from here.

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

Successful · Failed · Refund Requested · Refunded

**Corrected 2026-08-16 — `Awaiting Payment` removed.** This status previously existed for Services #12/#18, populated on RERA approval with a payment record left partially blank until the counter payment cleared. With both services normalized to pay before RERA's decision, every payment record is created only once a payment has actually happened, the same as every other Group C service — there is no longer an intermediate "approved but unpaid" state for a row to represent.

## 14. Possible Outcomes

* Payment Successful / Failed
* Refund Requested / Refunded

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
* Every row corresponds to an actual payment event — there is no row representing an approved-but-unpaid state.
* Service #2 never produces a row.
* All access is recorded in the audit log.

## 21. Business Rules

1. This is a reporting feature, not an account — there is nothing to fund, no balance to project, and no low-balance state.
2. Two payment timings exist: upfront before lodging (#1, #3–#11), and at counter before RERA's decision (#12–#18). Service #2 carries no fee and produces no payment record.
3. No action on this feature initiates, retries, or reverses a payment.
4. Refund status is display-only; the refund mechanism itself is unresolved and not asserted here.
5. What happens to a rejected application's already-paid fee is unresolved and not asserted here.
6. All payment records and access are permanently recorded in the audit trail.

## Open Questions

1. What happens to the fee on a rejected application, for services where payment precedes the decision? Unresolved (`payments.md`'s To Confirm — Summary).
2. Which refund mechanism applies — the platform's public refund service or an institution-specific process? Unresolved (`open-questions.md` B10, superseded).
3. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
