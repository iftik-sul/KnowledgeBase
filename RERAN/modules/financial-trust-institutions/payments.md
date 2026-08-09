---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
tags:
  - financial-trust-institutions
  - payments
---

# Financial & Trust Institutions — Payments

Every RERAN service is chargeable. Payment is a stage of each service flow, not an optional add-on, and no output document issues until fees are settled.

## Where Payment Sits in the Pipeline

The source defines a six-stage pipeline for every regulated service:

```
Lodge  →  Validate  →  Audit  →  Pay  →  Issue  →  Record & Sync
```

**Payment comes after audit approval, not at submission.** An institution submits a transaction, RERA approves it, and only then are fees settled and the output document released. A rejected application never reaches the payment stage.

This ordering shapes the module's screens: there is no checkout at submission, and an approved-but-unpaid state must exist and be visible.

## Two Payer Models

Group C is unusual in running both models across its 18 services.

| Model | Who pays | Mechanism | Services |
| :---- | :---- | :---- | :---- |
| **Institution account debit** | The institution | Fees deducted directly from the bank's account with RERA | Mortgage registration, amendment, transfer, release; grant property mortgage |
| **Customer payment at counter** | The end customer | Paid at a Real Estate Registration Trustee Centre, e-receipt issued | Finance lease services; fund company registration; heirs' sale; company share sale; title deed services; contract cancellation |
| **Institution fee payment** | The institution | Paid on approval of trustee/auditor standing | Approval / renewal and cancellation of Account Trustee & Auditing company |

> **Proposed** — the model names and this three-way split are not in the source. The underlying facts are: mortgage services state fees are deducted from the bank account, Trustee Centre services state the customer pays and receives a receipt, and the institutional approval services state payment of fees on approval. The categorisation is ours. Needs client confirmation.

**Why it matters:** an institution-debit service needs no payment screen for the officer at all — it needs a balance, a statement, and a reconciliation view. A customer-payment service needs a counter payment flow. Building one pattern for both would be wrong.

## Settlement Mechanisms

The source names three settlement routes across the platform:

* **Payment gateway** — card, bank transfer, and USSD (per the PRD's payment requirements)
* **Escrow deduction** — against a project trust account
* **Institution account debit** — against the bank's standing account with RERA

Group C uses institution account debit and gateway payment. Escrow deduction appears in Group B's developer services, where the Account Trustee acts as an approval step.

## Fee Calculation

Fees and VAT are computed automatically at the audit stage. The platform's fee schedule engine derives the amount from application type, property value, and classification.

> **Proposed** — not in source material for Group C specifically. Rationale: the source states that fees and VAT are computed automatically at stage 4 for every regulated service, and the PRD requires a fee schedule engine driven by application type, property value and classification. No Group C fee table exists in any source document. Needs client confirmation.

### To Confirm

* Is there a published fee schedule for the 18 Group C services, and can it be supplied?
* Do mortgage fees scale with loan value, property value, or are they flat?
* Is VAT applied to all 18 services or only some?
* Are institutional approval and renewal fees annual, or per application?

## Payment Artefacts

The source names these outputs across Group C services:

| Artefact | Appears in |
| :---- | :---- |
| Fee balance (e-deliverable) | Mortgage and finance lease services |
| Payment receipt | Fund company registration, heirs' sale, company share sale |
| E-receipt voucher | Contract cancellation |
| Tax invoice | Platform-wide requirement (PRD) |

> **Proposed** — the source uses "fee balance", "payment receipt" and "e-receipt voucher" inconsistently across rows, likely describing the same artefact. This module treats them as one **payment receipt**, issued electronically on settlement, unless the client distinguishes them. Needs client confirmation.

## Institution Account Management

> **Proposed** — not in source material. Rationale: if fees are deducted from a standing institution account, that account requires a balance, a top-up mechanism, a transaction history and a low-balance warning. None of this is described anywhere in the source, but debit-based settlement cannot function without it. Needs client confirmation.

An institution operating on account debit needs:

* **Account balance** — visible to the Institution Relationship Manager
* **Top-up / funding** — how the institution credits its RERA account
* **Transaction ledger** — every debit tied to its originating service application
* **Low-balance alerting** — before a transaction fails for insufficient funds
* **Periodic statement** — for the institution's own reconciliation

### To Confirm

* Does RERA operate standing accounts for institutions, or is "deducted from bank account" a direct debit against a nominated account?
* Who tops up and how — bank transfer, gateway, or arrangement with RERA finance?
* What happens when an approved transaction cannot be settled for insufficient funds? Does the approval expire?
* Is there a credit arrangement, or is it strictly pre-funded?

## Failed and Reversed Payments

> **Proposed** — not in source material. Rationale: no source document addresses payment failure for any user group, yet an approved-but-unsettled transaction is an unavoidable state in a pay-after-approval pipeline. Needs client confirmation.

* A payment failure must not void the audit approval — the transaction should hold in an approved, unsettled state and be retryable.
* A time limit on that state needs defining, or approvals accumulate indefinitely.
* Refunds exist as a platform service in the public services list (fee refund request, seven business days, subject to Ministry of Finance approval). Whether institutions access refunds through the same route is unstated.

## Additional Statuses

These extend the status vocabulary in [services-overview.md](services-overview.md):

| Status | Meaning |
| :---- | :---- |
| Awaiting Settlement | Approved by RERA, fees not yet settled |
| Payment Failed | Settlement attempted and declined; retryable |
| Settled | Fees received, output document released |
| Refund Requested | A settled fee is under refund review |

## To Confirm — Summary

1. Published fee schedule for the 18 Group C services
2. Mortgage fee basis — loan value, property value, or flat
3. VAT applicability across the 18 services
4. Institutional approval fees — annual or per application
5. Are "fee balance", "payment receipt" and "e-receipt voucher" one artefact or several?
6. Standing account vs direct debit
7. Top-up mechanism and responsibility
8. Behaviour on insufficient funds for an approved transaction
9. Credit arrangement or strictly pre-funded?
10. Time limit on the approved-but-unsettled state
11. Do institutions access fee refunds through the public refund service?
