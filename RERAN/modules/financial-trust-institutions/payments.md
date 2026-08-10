---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-10
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

> **Superseded by `open-questions.md` B1.** Finance lease services (#8–#11) now sit in the **Institution Account Debit** group, not Customer Payment at Counter as this document previously stated. B1's evidence is that "Fee balance" — a standing-account statement line, not a receipt — is listed among the issued deliverables for nearly every Group C mortgage **and finance-lease** row, and a balance is only meaningful where a running account exists to report. Rows 34–37 (finance lease) carry that same "Fee balance" artefact, so B1's reasoning applies to them by the same logic as the mortgage rows, even though their workflow text reads like a counter transaction ("submit docs, enter system, pay, receive output via email"). That tension is not resolved by source and is flagged in each finance-lease service flow's Open Questions.

| Model | Who pays | Mechanism | Services |
| :---- | :---- | :---- | :---- |
| **Institution account debit** | The institution | Deducted from the institution's standing, pre-funded settlement account with RERA, after RERA approval (B1) | Mortgage registration, amendment, transfer, release; grant property mortgage (#3–#7); finance lease registration, amendment, transfer, release (#8–#11) |
| **Customer payment at counter** | The end customer | Paid at a Real Estate Registration Trustee Centre or Land Department counter, a payment receipt or e-receipt voucher issued (B9) | Fund company registration; heirs' sale; company share sale; title deed update; split ownership; title deed issuance; contract cancellation (#12–#18) |
| **Institution fee payment** | The institution | Paid directly by the institution on approval of its own trustee/auditor standing, not deducted from the settlement account | Approval / renewal and cancellation of Account Trustee & Auditing company (#1–#2) |

> **Proposed** — the model names and this three-way split are not themselves in the source; B1 supplies the mechanism (standing account vs. per-transaction payment), and the service-by-service assignment above follows each row's output artefact (Fee Balance vs. Payment Receipt / e-Receipt Voucher, per B9). **Confidence:** High on the account-debit mechanism (B1); Medium-high on the specific 9/7/2 split, since the finance-lease placement rests on inference rather than an explicit "deducted from bank account" statement like the mortgage rows carry. Needs client confirmation.

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

> **Superseded by `open-questions.md` B9.** This document previously treated "fee balance," "payment receipt," and "e-receipt voucher" as one artefact. That assumption was wrong: they are **two different things**. A payment receipt (or e-receipt voucher — the same artefact under a different name) is proof that a single transaction settled. A fee balance is the standing settlement-account position *after* that deduction — a statement line, not a receipt. This follows directly from B1: only a running account produces a balance worth issuing as an output document; a one-off gateway or counter payment produces a receipt.

| Artefact | What it is | Appears in |
| :---- | :---- | :---- |
| Fee balance (e-deliverable) | Settlement-account statement line, not proof of a single transaction | Mortgage services (#3–#7) and finance lease services (#8–#11) — the Institution Account Debit group |
| Payment receipt | Proof that a single transaction settled | Fund company registration, heirs' sale, company share sale (#12–#14), and the other Customer Payment at Counter services (#15–#17) |
| E-receipt voucher | Same artefact as a payment receipt, different name | Contract cancellation (#18) |
| Tax invoice | Platform-wide requirement (PRD) | All fee-bearing services |

**Confidence:** Medium-high, contingent on B1's account-debit mechanism holding for the services it's applied to.

## Institution Account Management

> **Resolved (mechanism) by `open-questions.md` B1, B2, B4.** The account is a **standing pre-funded account**, not a direct debit against a nominated bank account (B1, High confidence on the mechanism). The Institution Relationship Manager authorises top-ups over two rails — bank transfer against a unique institution reference for large amounts, payment gateway for smaller ones — proposed to reuse the same wallet primitive as the individual-user module's proposed P-22 rather than a second build (B2, Medium confidence). There is no credit arrangement: submission is blocked when the projected balance after fees would go negative, with a configurable warning threshold before that point (B4, High confidence). **The scope consequence is not yet estimated:** balance display, top-up, transaction ledger, low-balance alerting and periodic statements are all real build work that appears in no source document and no estimate — this is the item to raise with the client, not the mechanism itself.

An institution operating on account debit needs:

* **Account balance** — visible to the Institution Relationship Manager
* **Top-up / funding** — bank transfer (large amounts) or payment gateway (smaller amounts), authorised by the Institution Relationship Manager (B2)
* **Transaction ledger** — every debit tied to its originating service application
* **Low-balance alerting** — before a transaction fails for insufficient funds, at a configurable threshold (B4)
* **Periodic statement** — for the institution's own reconciliation

### To Confirm

* Sign-off on the standing pre-funded account mechanism and, separately, the unscoped Settlement Account subsystem it requires to build (B1).
* Confirmation that the wallet primitive can be shared with individual-user P-22 rather than built twice (B2).

## Failed and Reversed Payments

> **Resolved by `open-questions.md` B3, B4, B10.** A payment failure does not void the audit approval — the transaction holds in **Approved — Awaiting Payment** and is retryable. The approval lapses to **Expired** after **30 calendar days** unsettled (B3, Medium confidence on the specific duration; the principle that approvals must expire is the part to defend — an indefinite hold accumulates a register of approved-but-unregistered interests, invisible to a searcher, which is the fraud surface the platform exists to close). Resubmission is required on expiry; re-audit is not, unless the underlying title changed in the interim, in which case it is. Institutions do **not** use the public refund service (B10, Medium confidence): overpayment or a voided transaction credits back to the settlement account automatically, same-day; cash-out to a commercial account happens only on account closure and can reuse the public refund workflow's Ministry of Finance approval for that step alone. Applying the public route's seven-business-day, bank-attachment-based turnaround to a bank whose fee failed to settle on a 20-minute service would be disproportionate.

* A payment failure must not void the audit approval — the transaction holds in an approved, unsettled state and is retryable.
* An approved but unsettled transaction expires after 30 calendar days (B3).
* Overpayment or a voided transaction credits back to the institution's settlement account automatically, same-day (B10).
* Cash-out to a commercial account happens only on account closure, reusing the public refund workflow's Ministry of Finance approval step (B10).

## Additional Statuses

These extend the platform core status vocabulary in [services-overview.md](services-overview.md), which now carries `Approved — Awaiting Payment` and `Expired` directly (D1). The Group C-specific refinements below still apply:

| Status | Meaning |
| :---- | :---- |
| Approved — Awaiting Payment | Approved by RERA, fees not yet settled (platform core, D1) |
| Payment Failed | Settlement attempted and declined; retryable without losing the approval |
| Completed | Fees received, output document released (platform core, D1) |
| Expired | Approved but unsettled for 30 calendar days; resubmission required (B3) |
| Refund Requested | A settled fee is under refund review (institution-initiated only for account-closure cash-out, B10) |

## To Confirm — Summary

Six of the original eleven items are resolved by the answers doc and are not repeated here (B1's mechanism, B2's top-up rails, B3's expiry principle, B4's no-credit rule, B9's artefact split, B10's refund route). What remains:

1. Published fee schedule for the 18 Group C services (B5 — client data; the one question of 23 with no proposed answer).
2. Mortgage fee basis — the ad valorem/banded/floor/cap structure is proposed (B6), but the specific bands are not.
3. VAT applicability across the 18 services — applied by default per B7, but service-code-level exemptions, if any, are unconfirmed.
4. Institutional approval fees — proposed as per-approval-term with a two-year validity (B8), but the duration and amount are proposals, not sourced figures.
5. **Sign-off that the Settlement Account subsystem is real, unscoped build work** (B1's scope consequence) — this is a cost question for the client, not a design question for us.
6. The exact 30-calendar-day figure in B3 — the principle that approvals expire is defended; the specific number is a proposal.
