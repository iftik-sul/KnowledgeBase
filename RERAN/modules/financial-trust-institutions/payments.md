---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-15
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

Every RERAN service is chargeable, except Service #2 (Cancellation of Account Trustee & Auditing Company), which carries no fee at all (`open-questions.md` B11, confirmed 2026-08-15). For every other Group C service, payment is the first stage of the service flow — there is no post-approval payment step left anywhere in the module.

**Corrected 2026-08-14 (client decision, via discussion — not a written source document).** This document previously described a standing pre-funded settlement account, debited after RERA approval, for the mortgage and finance-lease lifecycle (#3–#11). That model is retired. See `open-questions.md` B1 for the full correction and why the earlier reasoning is preserved there rather than deleted.

**Corrected 2026-08-15 (client decision — `open-questions.md` B11).** This document previously described a third payer/timing model, **Institution Fee Payment**, in which Services #1–#2 paid after RERA's decision — sourced directly from row 28's sequencing. The client has since decided that Service #1 now pays upfront, merging into the same model as Services #3–#11, and confirmed that Service #2 carries no fee at all. The Institution Fee Payment model is retired as a distinct category. **Group C now runs two payment models, not three:** Upfront Gateway Payment (#1, #3–#11) and Customer Payment at Counter (#12–#18). Everything below reflects this.

## Where Payment Sits in the Pipeline

**Two different timings, by service group:**

| Group | Timing | Basis |
| :---- | :---- | :---- |
| Institutional approval/renewal, and mortgage/finance-lease lifecycle (#1, #3–#11) | **Upfront**, before Lodge/Validate/Audit | #3–#11 corrected 2026-08-14 (client decision); #1 corrected 2026-08-15 (client decision, B11) — previously sourced as post-decision (row 28), the client has since decided to build this differently |
| Title and ownership transactions (#12–#18) | **At the point of service** — the customer pays at the Trustee Centre counter (or online, per C2) as part of the transaction | Sourced directly per row (e.g. row 38: "Customer pays fees and obtains e-receipt"). Unaffected by either correction; already point-of-sale |
| Cancellation, institutional and contract (#2, #18) | **No fee** (#2) or **customer pays at point of service** (#18, see above) | #2 confirmed 2026-08-15 (client decision, B11) — row 29's workflow lists no payment step, and the client has now confirmed this is not an omission: cancellation is genuinely free |

For #1 and #3–#11, the sequence is:

```
Draft  →  Pay  →  Lodge  →  Validate  →  Audit  →  Issue  →  Record & Sync
```

An institution user drafts the application, pays via the shared platform-wide payment gateway, and only then is the application lodged — for internal certification where sourced (Services #3–#11 only; #1 has no internal certification step in source) and RERA's audit. A rejected application has already paid — this document does not resolve what happens to that fee, since no source or client decision addresses it; see To Confirm — Summary.

**For Service #1 specifically:** the partner agreement signing required for a *new* approval (sourced, row 28) is unaffected by the payment-timing change. It remains a post-audit-decision step: payment funds the application at lodging; the agreement is signed once RERA has approved, before completion. The corrected workflow is Draft → Pay → Lodge → Audit → *(new approval only:* Sign Partner Agreement*)* → Issue.

**For Service #2:** there is no Pay step in the sequence at all. Draft → Lodge → Audit → Issue.

For #12–#18, payment and lodging happen together, at the counter or online checkout, unchanged by either correction.

**This also corrects a broader claim, for #3–#11 specifically.** `module-roadmap.md` previously stated, as a platform-wide cross-cutting observation, that "every fee-bearing service pays after audit approval, not at submission" — sourced from this document's old, now-retired pipeline description for #3–#11. Checking that claim against the individual-user and Real Estate Developer modules' actual service flows (both pay upfront: individual-user Service #8's `Payment must be completed before the application proceeds for regulatory review`, real-estate-developer Service #1's identical pattern) shows the platform-wide claim was never true even before this correction. With Service #1 now also paying upfront (B11), Group C has no post-approval-payment service left at all — see `module-roadmap.md`'s own note on this.

## Who Pays

Two payer/timing combinations, not three:

| Model | Who pays | Timing | Services |
| :---- | :---- | :---- | :---- |
| **Upfront gateway payment** *(#3–#11 corrected 2026-08-14; #1 added 2026-08-15, B11)* | The institution | Upfront, via the shared platform payment gateway, before lodging | Institutional approval/renewal, mortgage and finance-lease lifecycle (#1, #3–#11) |
| **Customer payment at counter** *(unaffected — sourced)* | The end customer | At the point of service (Trustee Centre counter or online, per C2) | Title and ownership transactions (#12–#18) |

**Service #2 pays nothing.** It is not a third model — it is the absence of a payment step, confirmed 2026-08-15 (B11).

**Why it matters:** #1 now needs a checkout step before the application can be lodged, where it previously needed a post-approval payment prompt after the partner agreement (new approvals) or after audit (renewals). #2's payment screens, if any were ever built against the old "pays after decision" assumption, should be removed rather than reworked — there is nothing to charge. #12–#18 are unchanged by either correction.

## Settlement Mechanisms

The source names three settlement routes across the platform:

* **Payment gateway** — card, bank transfer, and USSD (per the PRD's payment requirements)
* **Escrow deduction** — against a project trust account
* **Institution account debit** — against a bank's standing account with RERA

**Group C now uses payment gateway only, for every service that charges a fee.** Institution account debit is retired for this module — there is no standing account left to debit against (`open-questions.md` B1). Escrow deduction remains Group B's developer-services mechanism, where the Account Trustee acts as an approval step; unaffected by either correction and not a Group C payment route either before or after them.

## Fee Calculation

**RERA sets the fee for each service directly.** The amount is configuration, held in the platform's fee schedule engine (FR-16) and populated by RERA — not derived from loan value, property value, or any other figure belonging to the financial institution's relationship with its own customer (`open-questions.md` B6). This fee-setting principle applies module-wide, but *when* the fee is computed and charged now follows the two-way split above: at checkout before lodging for #1 and #3–#11 (both corrected — #3–#11 on 2026-08-14, #1 on 2026-08-15); at the point of service for #12–#18 (unaffected); and never, for #2 (confirmed 2026-08-15 — no fee applies).

> **Corrected 2026-08-14.** This section previously derived mortgage-service fees ad valorem from "application type, property value, and classification," treating RERA's fee as scaling with the secured loan amount. That conflated two things B6 now separates: the FI's own lending economics with its customer (never RERA's concern, never documented here) and RERA's own per-service fee (a flat, RERA-set figure per service code). FR-16's "application type... classification" language may still describe RERA varying its fee by service *type* — compatible with the corrected model — but a per-loan ad valorem calculation is specifically ruled out.

### To Confirm

* Is VAT applied to all 18 services or only some? *(Resolved — B7, confirmed 2026-08-15: VAT applies to all 18 services, no exemptions. Removed from this list.)*
* Are institutional approval and renewal fees annual, or per application? *(Resolved — B8, confirmed 2026-08-15: per-approval-term, renewing. The two-year duration specifically remains a proposal, not a sourced or separately confirmed figure.)*
* Does cancellation carry a fee? *(Resolved — B11, confirmed 2026-08-15: no. Removed from this list.)*

## Payment Artefacts

**Corrected 2026-08-14 — collapses to one artefact.** `open-questions.md` B9 (which previously distinguished a "fee balance" standing-account statement line from a "payment receipt") is superseded, not reworked: with no standing account, there is no fee balance to distinguish from anything. Every payment is a single, per-transaction event.

| Artefact | What it is | Appears in |
| :---- | :---- | :---- |
| Payment Receipt (e-receipt) | Proof that a single transaction settled, issued at checkout before the application is lodged (or at point of service, for #12–#18) | Every fee-bearing Group C service (#1, #3–#18) |
| Tax Invoice | Platform-wide requirement (PRD) | All fee-bearing services |

**Service #2 issues no payment artefact**, having no fee to settle (B11, confirmed 2026-08-15).

"E-receipt voucher," used by name in source row 45 (#18), and "Payment Receipts," used by name in source row 39 (#7), are both the same artefact as Payment Receipt above under different names — row 39 in particular is now the naming pattern every other mortgage-service row should be read as matching, not the exception it was treated as under the old fee-balance framing.

**Confidence:** Confirmed on the collapse to one artefact (client decision via B1/B9). The exact receipt field set is not specified in source.

## Failed and Reversed Payments

**Corrected 2026-08-14.** The old model's failure handling (`open-questions.md` B3, B4, B10) assumed a standing account: an approved-but-unsettled transaction held for 30 days before expiring, and a failed settlement retried against a balance that could run low. None of that applies once payment happens before an application is even lodged.

* **Payment failure at checkout** is not an application-lifecycle event — the application hasn't been lodged yet. The user retries payment; nothing is submitted, certified, or audited until it succeeds. No audit approval is ever at stake, since none has happened yet. This now applies to Service #1 as well as #3–#11 (B11, corrected 2026-08-15).
* **A rejected application has already paid.** What happens to that fee — refund, forfeiture, or something else — is not addressed by any source document or by the client decision behind either correction. Left genuinely open; see To Confirm — Summary.
* **A settled payment needing reversal** (overpayment, a voided transaction) has no institution-specific route documented under the corrected model. `open-questions.md` B10's old argument for bypassing the platform's public refund route rested entirely on protecting a standing account's same-day reconciliation, which no longer exists — that argument doesn't carry over. Whether Group C should still get an expedited refund path on some other basis is not decided here.
* **Service #2 has no payment to fail or reverse.** Not applicable, having no fee at all.

**What this replaces.** The old section here described `Approved — Awaiting Payment` as a real, visible state, a 30-calendar-day expiry to `Expired` (B3), and same-day automatic credit-back to a settlement account (B10). None of that is preserved as a weakened version — see below for what happens to those statuses.

## Additional Statuses

The platform core status vocabulary in [services-overview.md](services-overview.md) (D1) still includes `Approved — Awaiting Payment` and `Expired` as proposed core statuses. **Neither applies to any Group C service under the corrected model.**

* **`Approved — Awaiting Payment` does not occur anywhere in Group C.** It previously applied to Services #1–#2 only, since #3–#11 already paid upfront and #12–#18 paid at the counter. With Service #1 now also paying upfront (B11, confirmed 2026-08-15) and Service #2 confirmed to carry no fee, there is no Group C service left where an approval can occur while payment is still pending. This status is a genuine module-wide non-use of a platform-core status, not a Group C extension needing its own row. *(Corrected 2026-08-15 — previously scoped to "#1–#2 only"; B11 closes that last remaining case.)*
* **`Expired`, as previously defined for Group C, does not occur either.** Its only sourced meaning here was `open-questions.md` B3's "approved but unsettled for 30 calendar days" — a scenario upfront payment makes impossible, now for every fee-bearing Group C service. **B3 itself was not in scope for either correction and remains as written in `open-questions.md`** — flagging the resulting tension rather than resolving it: B3 answers a question ("what happens when an approved transaction cannot be settled?") that no longer has a live scenario to answer anywhere in Group C, under the corrected payment model. Whether B3 needs its own follow-up correction is left for review.

| Status | Meaning | Still applies to Group C? |
| :---- | :---- | :---- |
| Payment Failed | Checkout attempted and declined; retryable, nothing submitted yet | Yes, for #1 and #3–#11 — reframed as pre-lodging, not post-approval |
| Refund Requested | A settled fee is under refund review | Open — see Failed and Reversed Payments above; not resolved which route applies |

## To Confirm — Summary

**Corrected 2026-08-15.** B1, B2, B4, B5, B6, B7, B8, B9, B10, and B11 are now resolved (B9 and B10 by supersession, not by independent rework — see `open-questions.md`). What remains:

1. **What happens to the fee on a rejected application** (refund, forfeiture, or otherwise) — not addressed by any source document or by either payment-model correction. Genuinely open, applies now to Service #1 as well as #3–#11.
2. **Whether Group C should use the platform's public refund route, or some other route, for a settled payment needing reversal** — B10's old argument for a special route no longer holds; no replacement decision has been made.
3. **The B3/`Expired` tension** flagged above under Additional Statuses — B3 wasn't in scope for either correction, but its sourced scenario can no longer occur anywhere in Group C.
4. **Whether the shared payment gateway is genuinely the same build artefact as individual-user's wallet primitive (P-22), or a separate integration** — P-22 is documented as balance-based, which doesn't cleanly match Group C's no-standing-account model (`open-questions.md` B2).
