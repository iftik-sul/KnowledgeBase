---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-14
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - payments
---

# Financial & Trust Institutions — Payments

Every RERAN service is chargeable. For most Group C services, payment is now the first stage of the service flow — but not all: institutional approval and renewal (#1–#2) remain paid **after** RERA's decision, on genuinely sourced grounds unrelated to this correction. See below.

**Corrected 2026-08-14 (client decision, via discussion — not a written source document).** This document previously described a standing pre-funded settlement account, debited after RERA approval, for the mortgage and finance-lease lifecycle (#3–#11). That model is retired. See `open-questions.md` B1 for the full correction and why the earlier reasoning is preserved there rather than deleted. **This correction is narrower than "everyone pays upfront now"** — it retires the *Institution Account Debit* mechanism specifically. It does not touch the *Institution Fee Payment* model (#1–#2) or the *Customer Payment at Counter* model (#12–#18), both of which have their own, independent sourcing untouched by B1. Collapsing all three into one uniform "pay upfront" model would have been wrong; corrected below.

## Where Payment Sits in the Pipeline

**Three different timings, by service group — not one pipeline:**

| Group | Timing | Basis |
| :---- | :---- | :---- |
| Mortgage and finance-lease lifecycle (#3–#11) | **Upfront**, before Lodge/Validate/Audit | Corrected 2026-08-14 (client decision) — was previously inferred as post-approval from the now-retired B1 standing-account reading; no independent source ever placed it after approval |
| Institutional approval / renewal, cancellation (#1–#2) | **After RERA's decision** (and, for a new approval, after the partner agreement is signed) | Sourced directly — row 28 sequences "Payment of fees" after the approval decision. Unaffected by this correction; B1 never applied to these two services in the first place |
| Title and ownership transactions (#12–#18) | **At the point of service** — the customer pays at the Trustee Centre counter (or online, per C2) as part of the transaction | Sourced directly per row (e.g. row 38: "Customer pays fees and obtains e-receipt"). Unaffected by this correction; already point-of-sale, never dependent on B1's standing-account reading |

For #3–#11, the corrected sequence is:

```
Draft  →  Pay  →  Lodge  →  Validate  →  Audit  →  Issue  →  Record & Sync
```

An institution user drafts the application, pays via the shared platform-wide payment gateway, and only then is the application lodged for internal certification (where sourced, Services #3–#11) and RERA's audit. A rejected application has already paid — this document does not resolve what happens to that fee, since no source or client decision addresses it; see To Confirm — Summary.

For #1–#2, the sequence is unchanged from before this correction: **Lodge → Validate → Audit → Pay → Issue**. For #12–#18, payment and lodging happen together, at the counter or online checkout, which this correction doesn't reorder.

**This also corrects a broader claim, for #3–#11 specifically.** `module-roadmap.md` previously stated, as a platform-wide cross-cutting observation, that "every fee-bearing service pays after audit approval, not at submission" — sourced from this document's old, now-retired pipeline description for #3–#11. Checking that claim against the individual-user and Real Estate Developer modules' actual service flows (both pay upfront: individual-user Service #8's `Payment must be completed before the application proceeds for regulatory review`, real-estate-developer Service #1's identical pattern) shows the platform-wide claim was never true even before this correction — Group C's old #3–#11 model was the outlier, not the rule, and #1–#2's genuinely-sourced post-approval timing was never representative of "every fee-bearing service" either. See `module-roadmap.md`'s own note on this.

## Who Pays

Three payer/timing combinations, not a single uniform model — mechanism corrected only where B1 applied:

| Model | Who pays | Timing | Services |
| :---- | :---- | :---- | :---- |
| **Upfront gateway payment** *(corrected 2026-08-14)* | The institution | Upfront, via the shared platform payment gateway, before lodging | Mortgage and finance-lease lifecycle (#3–#11) |
| **Institution fee payment** *(unaffected — sourced)* | The institution | After RERA's approval decision | Institutional approval / renewal, cancellation (#1–#2) |
| **Customer payment at counter** *(unaffected — sourced)* | The end customer | At the point of service (Trustee Centre counter or online, per C2) | Title and ownership transactions (#12–#18) |

**Why it matters:** #3–#11 now need a checkout step before the application can be lodged, where they previously needed a post-approval balance display. #1–#2 and #12–#18 are unchanged by this correction — their payment screens are whatever they already were.

## Settlement Mechanisms

The source names three settlement routes across the platform:

* **Payment gateway** — card, bank transfer, and USSD (per the PRD's payment requirements)
* **Escrow deduction** — against a project trust account
* **Institution account debit** — against a bank's standing account with RERA

**Group C now uses payment gateway only.** Institution account debit is retired for this module — there is no standing account left to debit against (`open-questions.md` B1). Escrow deduction remains Group B's developer-services mechanism, where the Account Trustee acts as an approval step; unaffected by this correction and not a Group C payment route either before or after it.

## Fee Calculation

**RERA sets the fee for each service directly.** The amount is configuration, held in the platform's fee schedule engine (FR-16) and populated by RERA — not derived from loan value, property value, or any other figure belonging to the financial institution's relationship with its own customer (`open-questions.md` B6). This fee-setting principle applies module-wide, but *when* the fee is computed and charged still follows the three-way split above: at checkout before lodging for #3–#11 (corrected); at the point of service for #12–#18 (unaffected); and at the audit stage, ahead of the (unchanged) post-approval payment step, for #1–#2 (unaffected).

> **Corrected 2026-08-14.** This section previously derived mortgage-service fees ad valorem from "application type, property value, and classification," treating RERA's fee as scaling with the secured loan amount. That conflated two things B6 now separates: the FI's own lending economics with its customer (never RERA's concern, never documented here) and RERA's own per-service fee (a flat, RERA-set figure per service code). FR-16's "application type... classification" language may still describe RERA varying its fee by service *type* — compatible with the corrected model — but a per-loan ad valorem calculation is specifically ruled out.

### To Confirm

* Is there a published fee schedule for the 18 Group C services, and can it be supplied? *(Resolved by B5 — there is no separate document; RERA populates the fee-schedule engine's configuration directly. Removed from this list; see below.)*
* Is VAT applied to all 18 services or only some? *(Unaffected by this correction — B7's default-applies, configurable-per-service answer stands.)*
* Are institutional approval and renewal fees annual, or per application? *(Unaffected by this correction — B8's per-approval-term, two-year-validity proposal stands.)*

## Payment Artefacts

**Corrected 2026-08-14 — collapses to one artefact.** `open-questions.md` B9 (which previously distinguished a "fee balance" standing-account statement line from a "payment receipt") is superseded, not reworked: with no standing account, there is no fee balance to distinguish from anything. Every payment is a single, per-transaction event.

| Artefact | What it is | Appears in |
| :---- | :---- | :---- |
| Payment Receipt (e-receipt) | Proof that a single transaction settled, issued at checkout before the application is lodged | Every fee-bearing Group C service (#1–#18) |
| Tax Invoice | Platform-wide requirement (PRD) | All fee-bearing services |

"E-receipt voucher," used by name in source row 45 (#18), and "Payment Receipts," used by name in source row 39 (#7), are both the same artefact as Payment Receipt above under different names — row 39 in particular is now the naming pattern every other mortgage-service row should be read as matching, not the exception it was treated as under the old fee-balance framing.

**Confidence:** Confirmed on the collapse to one artefact (client decision via B1/B9). The exact receipt field set is not specified in source.

## Failed and Reversed Payments

**Corrected 2026-08-14.** The old model's failure handling (`open-questions.md` B3, B4, B10) assumed a standing account: an approved-but-unsettled transaction held for 30 days before expiring, and a failed settlement retried against a balance that could run low. None of that applies once payment happens before an application is even lodged.

* **Payment failure at checkout** is not an application-lifecycle event — the application hasn't been lodged yet. The user retries payment; nothing is submitted, certified, or audited until it succeeds. No audit approval is ever at stake, since none has happened yet.
* **A rejected application has already paid.** What happens to that fee — refund, forfeiture, or something else — is not addressed by any source document or by the client decision behind this correction. Left genuinely open; see To Confirm — Summary.
* **A settled payment needing reversal** (overpayment, a voided transaction) has no institution-specific route documented under the corrected model. `open-questions.md` B10's old argument for bypassing the platform's public refund route rested entirely on protecting a standing account's same-day reconciliation, which no longer exists — that argument doesn't carry over. Whether Group C should still get an expedited refund path on some other basis is not decided here.

**What this replaces.** The old section here described `Approved — Awaiting Payment` as a real, visible state, a 30-calendar-day expiry to `Expired` (B3), and same-day automatic credit-back to a settlement account (B10). None of that is preserved as a weakened version — see below for what happens to those statuses.

## Additional Statuses

The platform core status vocabulary in [services-overview.md](services-overview.md) (D1) still includes `Approved — Awaiting Payment` and `Expired` as proposed core statuses. **Neither applies to Group C under the corrected model:**

* **`Approved — Awaiting Payment` does not occur for Group C.** Payment happens before lodging, so nothing is ever approved while still awaiting payment. This is a genuine module-level non-use of a platform-core status, not a Group C extension needing its own row.
* **`Expired`, as previously defined for Group C, does not occur either.** Its only sourced meaning here was `open-questions.md` B3's "approved but unsettled for 30 calendar days" — a scenario upfront payment makes impossible. **B3 itself was not in this correction's scope and remains as written in `open-questions.md`** — flagging the resulting tension rather than resolving it: B3 answers a question ("what happens when an approved transaction cannot be settled?") that no longer has a live scenario to answer, for Group C specifically, under the corrected payment model. Whether B3 needs its own follow-up correction is left for review.

| Status | Meaning | Still applies to Group C? |
| :---- | :---- | :---- |
| Payment Failed | Checkout attempted and declined; retryable, nothing submitted yet | Yes — reframed as pre-lodging, not post-approval |
| Refund Requested | A settled fee is under refund review | Open — see Failed and Reversed Payments above; not resolved which route applies |

## To Confirm — Summary

**Corrected 2026-08-14.** B1, B2, B4, B5, B6, B9, and B10 are now resolved (B9 and B10 by supersession, not by independent rework — see `open-questions.md`). What remains:

1. VAT applicability across the 18 services — applied by default per B7, but service-code-level exemptions, if any, are unconfirmed. *(Unaffected by this correction.)*
2. Institutional approval fees — proposed as per-approval-term with a two-year validity (B8), but the duration and amount are proposals, not sourced figures. *(Unaffected by this correction.)*
3. **What happens to the fee on a rejected application** (refund, forfeiture, or otherwise) — not addressed by any source document or by the payment-model correction itself. Genuinely new and open, not carried over from the pre-correction list.
4. **Whether Group C should use the platform's public refund route, or some other route, for a settled payment needing reversal** — B10's old argument for a special route no longer holds; no replacement decision has been made.
5. **The B3/`Expired` tension** flagged above under Additional Statuses — B3 wasn't in this correction's scope, but its sourced scenario can no longer occur for Group C.
6. **Whether the shared payment gateway is genuinely the same build artefact as individual-user's wallet primitive (P-22), or a separate integration** — P-22 is documented as balance-based, which doesn't cleanly match Group C's no-standing-account model (`open-questions.md` B2).
