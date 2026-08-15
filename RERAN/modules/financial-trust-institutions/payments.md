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

Every RERAN service is chargeable, except Service #2 (Cancellation of Account Trustee & Auditing Company), which carries no fee at all (`open-questions.md` B11, confirmed 2026-08-15). For most Group C services, payment is the first stage of the service flow. **Two services — #12 and #18 — are a genuine, sourced exception: payment happens after RERA's decision, not before.** See "Where Payment Sits in the Pipeline" below.

**Corrected 2026-08-14 (client decision, via discussion — not a written source document).** This document previously described a standing pre-funded settlement account, debited after RERA approval, for the mortgage and finance-lease lifecycle (#3–#11). That model is retired. See `open-questions.md` B1 for the full correction and why the earlier reasoning is preserved there rather than deleted.

**Corrected 2026-08-15 (client decision — `open-questions.md` B11).** This document previously described a third payer/timing model, **Institution Fee Payment**, in which Services #1–#2 paid after RERA's decision — sourced directly from row 28's sequencing. The client has since decided that Service #1 now pays upfront, merging into the same model as Services #3–#11, and confirmed that Service #2 carries no fee at all. The Institution Fee Payment model is retired as a distinct category. **Group C now runs two payer/timing models, not three:** Upfront Gateway Payment (#1, #3–#11) and Customer Payment at Counter (#12–#18). Everything below reflects this.

**Corrected again, same day, after a fuller per-service audit.** The Customer Payment at Counter model is not internally uniform on *timing relative to RERA's decision*, even though every one of #12–#18 shares the same payer (the customer) and channel (the counter). Checking each service's own sourced workflow found: **Services #13–#17 have the customer pay before RERA reviews the application. Services #12 and #18 have RERA decide first, and the customer pays after.** This wasn't previously distinguished anywhere in this document — see the pipeline table below.

## Where Payment Sits in the Pipeline

**Three sequences, not two, once #12/#18's exception is accounted for:**

| Group | Timing | Basis |
| :---- | :---- | :---- |
| Institutional approval/renewal, and mortgage/finance-lease lifecycle (#1, #3–#11) | **Upfront**, before Lodge/Validate/Audit | #3–#11 corrected 2026-08-14 (client decision); #1 corrected 2026-08-15 (client decision, B11) — previously sourced as post-decision (row 28), the client has since decided to build this differently |
| Most title and ownership transactions (#13–#17) | **At the point of service, before RERA's decision** — the customer pays at the Trustee Centre counter (or Land Department, per C2) as part of lodging the transaction | Sourced directly per row (e.g. row 40: heir pays before RERA's audit). Unaffected by either B1/B11 correction; already point-of-sale, and already pre-decision |
| **Registration of Real Estate Fund Companies (#12) and Contract Cancellation (#18)** | **At the point of service, after RERA's decision** — the customer pays at the counter once approved, return, or rejected is known | Sourced directly (row 38, row 45) — a genuinely different sequence from #13–#17, not previously distinguished in this document. See those two files' own Section 9/13 for the full sourced sequence. |
| Cancellation, institutional (#2) | **No fee** | Confirmed 2026-08-15 (client decision, B11) — row 29's workflow lists no payment step, and the client has confirmed this is not an omission |

For #1 and #3–#11, the sequence is:

```
Draft  →  Pay  →  Lodge  →  Validate  →  Audit  →  Issue  →  Record & Sync
```

An institution user drafts the application, pays via the shared platform-wide payment gateway, and only then is the application lodged — for internal certification where sourced (Services #3–#11 only; #1 has no internal certification step in source) and RERA's audit. A rejected application has already paid — this document does not resolve what happens to that fee, since no source or client decision addresses it; see To Confirm — Summary.

**For Service #1 specifically:** the partner agreement signing required for a *new* approval (sourced, row 28) is unaffected by the payment-timing change. It remains a post-audit-decision step: payment funds the application at lodging; the agreement is signed once RERA has approved, before completion. The corrected workflow is Draft → Pay → Lodge → Audit → *(new approval only:* Sign Partner Agreement*)* → Issue.

**For Service #2:** there is no Pay step in the sequence at all. Draft → Lodge → Audit → Issue.

**For #13–#17:** payment and lodging happen together, at the counter or online checkout, before RERA's review — unchanged by either the B1 or B11 correction, since those corrections were scoped to #1–#11.

**For #12 and #18:** Lodge → Audit (RERA decides) → Pay at counter → Issue. This is the one sequence anywhere in the corrected Group C model where an application can sit approved while payment is still outstanding — see Additional Statuses below.

**This also corrects a broader claim, for #3–#11 specifically.** `module-roadmap.md` previously stated, as a platform-wide cross-cutting observation, that "every fee-bearing service pays after audit approval, not at submission" — sourced from this document's old, now-retired pipeline description for #3–#11. Checking that claim against the individual-user and Real Estate Developer modules' actual service flows (both pay upfront: individual-user Service #8's `Payment must be completed before the application proceeds for regulatory review`, real-estate-developer Service #1's identical pattern) shows the platform-wide claim was never true even before this correction. **Group C itself is not fully upfront either, once #12/#18 are accounted for** — see `module-roadmap.md`'s own cross-cutting note, which needs the same correction this document just received.

## Who Pays

Two payer/timing *models*, but the second has an internal timing split (above) that this table doesn't fully capture on its own — see "Where Payment Sits in the Pipeline" for the complete picture:

| Model | Who pays | Timing | Services |
| :---- | :---- | :---- | :---- |
| **Upfront gateway payment** *(#3–#11 corrected 2026-08-14; #1 added 2026-08-15, B11)* | The institution | Upfront, via the shared platform payment gateway, before lodging | Institutional approval/renewal, mortgage and finance-lease lifecycle (#1, #3–#11) |
| **Customer payment at counter** *(unaffected by B1/B11 — sourced; internal timing split found 2026-08-15)* | The end customer | At the point of service (Trustee Centre counter, Land Department, or online, per C2) — **before** RERA's decision for #13–#17, **after** it for #12 and #18 | Title and ownership transactions, contract cancellation (#12–#18) |

**Service #2 pays nothing.** It is not a third model — it is the absence of a payment step, confirmed 2026-08-15 (B11).

**Why it matters:** #1 now needs a checkout step before the application can be lodged, where it previously needed a post-approval payment prompt after the partner agreement (new approvals) or after audit (renewals). #2's payment screens, if any were ever built against the old "pays after decision" assumption, should be removed rather than reworked — there is nothing to charge. #13–#17 need a checkout step at lodging, same as the upfront model in spirit though sourced independently. **#12 and #18 need the opposite of #13–#17: a payment step that only appears once RERA's decision is known**, not at lodging — building all six title/ownership/contract services (#12–#18 minus #2, which has none) against a single "pay at lodging" assumption would be wrong for two of them.

## Settlement Mechanisms

The source names three settlement routes across the platform:

* **Payment gateway** — card, bank transfer, and USSD (per the PRD's payment requirements)
* **Escrow deduction** — against a project trust account
* **Institution account debit** — against a bank's standing account with RERA

**Group C now uses payment gateway only, for every service that charges a fee.** Institution account debit is retired for this module — there is no standing account left to debit against (`open-questions.md` B1). Escrow deduction remains Group B's developer-services mechanism, where the Account Trustee acts as an approval step; unaffected by either correction and not a Group C payment route either before or after them.

## Fee Calculation

**RERA sets the fee for each service directly.** The amount is configuration, held in the platform's fee schedule engine (FR-16) and populated by RERA — not derived from loan value, property value, or any other figure belonging to the financial institution's relationship with its own customer (`open-questions.md` B6). This fee-setting principle applies module-wide, but *when* the fee is computed and charged now follows the split above: at checkout before lodging for #1 and #3–#17; at checkout after RERA's decision for #12 and #18; and never, for #2 (confirmed 2026-08-15 — no fee applies).

> **Corrected 2026-08-14.** This section previously derived mortgage-service fees ad valorem from "application type, property value, and classification," treating RERA's fee as scaling with the secured loan amount. That conflated two things B6 now separates: the FI's own lending economics with its customer (never RERA's concern, never documented here) and RERA's own per-service fee (a flat, RERA-set figure per service code). FR-16's "application type... classification" language may still describe RERA varying its fee by service *type* — compatible with the corrected model — but a per-loan ad valorem calculation is specifically ruled out.

### To Confirm

* Is VAT applied to all 18 services or only some? *(Resolved — B7, confirmed 2026-08-15: VAT applies to all 18 services, no exemptions. Removed from this list.)*
* Are institutional approval and renewal fees annual, or per application? *(Resolved — B8, confirmed 2026-08-15: per-approval-term, renewing. The two-year duration specifically remains a proposal, not a sourced or separately confirmed figure.)*
* Does cancellation carry a fee? *(Resolved — B11, confirmed 2026-08-15: no. Removed from this list.)*
* **Added 2026-08-15.** Is #12/#18's post-decision payment timing intentional, or should it be normalized to the pre-decision pattern #13–#17 already use, once the process is digitized rather than run at a physical counter? Not addressed by source or by any client decision — see `services-overview.md`'s To Confirm list, item 5.

## Payment Artefacts

**Corrected 2026-08-14 — collapses to one artefact.** `open-questions.md` B9 (which previously distinguished a "fee balance" standing-account statement line from a "payment receipt") is superseded, not reworked: with no standing account, there is no fee balance to distinguish from anything. Every payment is a single, per-transaction event.

| Artefact | What it is | Appears in |
| :---- | :---- | :---- |
| Payment Receipt (e-receipt) | Proof that a single transaction settled, issued at checkout — before lodging (#1, #3–#17) or after RERA's decision, before completion (#12, #18) | Every fee-bearing Group C service (#1, #3–#18) |
| Tax Invoice | Platform-wide requirement (PRD) | All fee-bearing services |

**Service #2 issues no payment artefact**, having no fee to settle (B11, confirmed 2026-08-15).

"E-receipt voucher," used by name in source row 45 (#18), and "Payment Receipts," used by name in source row 39 (#7), are both the same artefact as Payment Receipt above under different names — row 39 in particular is now the naming pattern every other mortgage-service row should be read as matching, not the exception it was treated as under the old fee-balance framing.

**Confidence:** Confirmed on the collapse to one artefact (client decision via B1/B9). The exact receipt field set is not specified in source.

## Failed and Reversed Payments

**Corrected 2026-08-14.** The old model's failure handling (`open-questions.md` B3, B4, B10) assumed a standing account: an approved-but-unsettled transaction held for 30 days before expiring, and a failed settlement retried against a balance that could run low. None of that applies once payment happens before an application is even lodged — though see the note below on #12/#18, where a different kind of approved-but-unpaid state genuinely does exist.

* **Payment failure at checkout** is not an application-lifecycle event for #1 and #3–#17 — the application hasn't been lodged yet (or, for #13–#17, hasn't cleared the counter step). The user retries payment; nothing is submitted, certified, or audited until it succeeds.
* **For #12 and #18, a payment failure after approval is a different situation**, not addressed anywhere in this document until this correction: the application has already been audited and approved by RERA; only the customer's counter payment remains. What happens if that payment fails or the customer doesn't return to pay is not specified in source and is not resolved here — see To Confirm — Summary.
* **A rejected application has already paid**, for #1 and #3–#17. What happens to that fee — refund, forfeiture, or something else — is not addressed by any source document or by either payment-model correction. Left genuinely open; see To Confirm — Summary. **This doesn't apply to #12/#18**, where a rejection happens before payment was ever collected.
* **A settled payment needing reversal** (overpayment, a voided transaction) has no institution-specific route documented under the corrected model. `open-questions.md` B10's old argument for bypassing the platform's public refund route rested entirely on protecting a standing account's same-day reconciliation, which no longer exists — that argument doesn't carry over. Whether Group C should still get an expedited refund path on some other basis is not decided here.
* **Service #2 has no payment to fail or reverse.** Not applicable, having no fee at all.

**What this replaces.** The old section here described `Approved — Awaiting Payment` as a real, visible state, a 30-calendar-day expiry to `Expired` (B3), and same-day automatic credit-back to a settlement account (B10). Neither status is preserved as a weakened version for #1 or #3–#17 — see Additional Statuses below for what happens to them, and for the genuine #12/#18 exception.

## Additional Statuses

The platform core status vocabulary in [services-overview.md](services-overview.md) (D1) still includes `Approved — Awaiting Payment` and `Expired` as proposed core statuses.

* **`Approved — Awaiting Payment` occurs for exactly two Group C services: #12 and #18.** An earlier correction pass this same day claimed the status applied to no Group C service at all, reasoning that #1 now pays upfront (B11) and #2 carries no fee, closing what looked like the last remaining case. That reasoning checked #1–#11 but never re-verified #12–#18 individually — doing so found that #12 and #18 genuinely source RERA's decision *before* the customer's counter payment (row 38, row 45), which is exactly the scenario this status describes. It remains correctly absent for #1, #3–#11 (all pay upfront) and #13–#17 (all pay before RERA's decision). *(Corrected 2026-08-15, twice in the same day — see `services-overview.md`'s Application Status Vocabulary section for the same correction.)*
* **`Expired`, as previously defined for Group C, still does not occur anywhere.** Its only sourced meaning here was `open-questions.md` B3's "approved but unsettled for 30 calendar days" — a scenario written for a registered-title, standing-account context. #12/#18's approved-but-unpaid window is a short, same-visit counter wait (both services carry a 25–30 and 15 minute SLA respectively), not a multi-day lapse risk; B3's 30-day figure has no natural application to either. **B3 itself was not in scope for any of today's corrections and remains as written in `open-questions.md`.**

| Status | Meaning | Still applies to Group C? |
| :---- | :---- | :---- |
| Payment Failed | Checkout attempted and declined; retryable, nothing submitted/lodged yet | Yes, for #1, #3–#11 (pre-lodging) and #13–#17 (pre-decision) |
| Refund Requested | A settled fee is under refund review | Open — see Failed and Reversed Payments above; not resolved which route applies |

## To Confirm — Summary

**Corrected 2026-08-15, twice.** B1, B2, B4, B5, B6, B7, B8, B9, B10, and B11 are resolved (B9 and B10 by supersession, not by independent rework — see `open-questions.md`). What remains, after the fuller #12–#18 audit:

1. **What happens to the fee on a rejected application** (refund, forfeiture, or otherwise) — not addressed by any source document or by either payment-model correction. Applies to Service #1 and #3–#17; does not apply to #12/#18, where rejection precedes payment collection.
2. **Whether Group C should use the platform's public refund route, or some other route, for a settled payment needing reversal** — B10's old argument for a special route no longer holds; no replacement decision has been made.
3. **The B3/`Expired` tension** flagged above under Additional Statuses — B3 wasn't in scope for any correction, and its sourced scenario doesn't map cleanly onto #12/#18's short counter-payment window either.
4. **Whether the shared payment gateway is genuinely the same build artefact as individual-user's wallet primitive (P-22), or a separate integration** — P-22 is documented as balance-based, which doesn't cleanly match Group C's no-standing-account model (`open-questions.md` B2).
5. **Added 2026-08-15.** What happens if a customer approved under #12 or #18 never returns to pay at the counter — no expiry, forfeiture, or escalation rule is sourced or proposed for this scenario, which is structurally different from #1–#11's pre-lodging payment failures.
