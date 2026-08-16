---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-16
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

Every RERAN service is chargeable, except Service #2 (Cancellation of Account Trustee & Auditing Company), which carries no fee at all (`open-questions.md` B11, confirmed 2026-08-15). **As of 2026-08-16, by client decision, every fee-bearing Group C service pays before RERA's decision.** There is no longer any service where payment happens after approval.

**Corrected 2026-08-14 (client decision, via discussion — not a written source document).** This document previously described a standing pre-funded settlement account, debited after RERA approval, for the mortgage and finance-lease lifecycle (#3–#11). That model is retired. See `open-questions.md` B1 for the full correction and why the earlier reasoning is preserved there rather than deleted.

**Corrected 2026-08-15 (client decision — `open-questions.md` B11).** This document previously described a third payer/timing model, **Institution Fee Payment**, in which Services #1–#2 paid after RERA's decision — sourced directly from row 28's sequencing. The client has since decided that Service #1 now pays upfront, merging into the same model as Services #3–#11, and confirmed that Service #2 carries no fee at all. The Institution Fee Payment model is retired as a distinct category.

**Corrected 2026-08-16, by client decision — the #12/#18 exception is retired, not merely documented.** Source rows 38 and 45 describe Services #12 and #18 paying *after* RERA's decision, at the physical counter — a genuine artefact of the process being originally designed around a walk-in transaction, confirmed by client decision on 2026-08-16 to be exactly that: an artefact of the old counter-based process, not intentional design. **Normalized to pay-before-decision**, matching Services #13–#17's pattern, once the process is digitized onto the shared platform gateway. **Group C now runs a single payer/timing pattern**: every fee-bearing service pays before RERA reviews the application — either upfront via the shared gateway (institution-paid) or at the point of service before lodging (customer-paid, at the counter or online). Everything below reflects this.

## Where Payment Sits in the Pipeline

**One pattern, not several, once the 2026-08-16 normalization is applied:**

| Group | Timing | Basis |
| :---- | :---- | :---- |
| Institutional approval/renewal, and mortgage/finance-lease lifecycle (#1, #3–#11) | **Upfront**, before Lodge/Validate/Audit | #3–#11 corrected 2026-08-14 (client decision); #1 corrected 2026-08-15 (client decision, B11) |
| All title, ownership, and contract transactions (#12–#18 except #2) | **At the point of service, before RERA's decision** — the customer pays at the Trustee Centre counter (or Land Department, or online, per C2) as part of lodging the transaction | #13–#17 sourced directly per row (unaffected by any correction — already pre-decision). **#12 and #18 corrected 2026-08-16**: previously sourced as post-decision (row 38, row 45), the client has confirmed this was an artefact of the original counter-based process and normalized it to match #13–#17 |
| Cancellation, institutional (#2) | **No fee** | Confirmed 2026-08-15 (client decision, B11) — row 29's workflow lists no payment step, and the client has confirmed this is not an omission |

For #1 and #3–#11, the sequence is:

```
Draft  →  Pay  →  Lodge  →  Validate  →  Audit  →  Issue  →  Record & Sync
```

An institution user drafts the application, pays via the shared platform-wide payment gateway, and only then is the application lodged — for internal certification where sourced (Services #3–#11 only; #1 has no internal certification step in source) and RERA's audit. A rejected application has already paid — this document does not resolve what happens to that fee, since no source or client decision addresses it; see To Confirm — Summary.

**For Service #1 specifically:** the partner agreement signing required for a *new* approval (sourced, row 28) is unaffected by the payment-timing change. It remains a post-audit-decision step: payment funds the application at lodging; the agreement is signed once RERA has approved, before completion. The corrected workflow is Draft → Pay → Lodge → Audit → *(new approval only:* Sign Partner Agreement*)* → Issue.

**For Service #2:** there is no Pay step in the sequence at all. Draft → Lodge → Audit → Issue.

**For #13–#18 (all six, following the 2026-08-16 normalization):** payment and lodging happen together, at the counter or online checkout, before RERA's review. #12 and #18 previously ran Lodge → Audit → Pay → Issue; **now run the same Pay → Lodge → Audit → Issue sequence as #13–#17.** This is a documented product decision extending beyond source, not itself sourced — see each service's own file for the corrected workflow.

**This also corrects a broader claim, for #3–#11 specifically.** `module-roadmap.md` previously stated, as a platform-wide cross-cutting observation, that "every fee-bearing service pays after audit approval, not at submission" — sourced from this document's old, now-retired pipeline description for #3–#11. Checking that claim against the individual-user and Real Estate Developer modules' actual service flows (both pay upfront: individual-user Service #8's `Payment must be completed before the application proceeds for regulatory review`, real-estate-developer Service #1's identical pattern) shows the platform-wide claim was never true even before this correction. **As of 2026-08-16, Group C is now fully upfront/pre-decision as well** — the module-roadmap.md claim, ironically, is now accurate for Group C in outcome, even though its original reasoning (drawn from the old #3–#11-only pipeline) was never correct. `module-roadmap.md` still needs its own correction pass to fix the reasoning, even if the conclusion now happens to hold.

## Who Pays

**One payer/timing pattern**, following the 2026-08-16 normalization:

| Model | Who pays | Timing | Services |
| :---- | :---- | :---- | :---- |
| **Upfront gateway payment** *(#3–#11 corrected 2026-08-14; #1 added 2026-08-15, B11)* | The institution | Upfront, via the shared platform payment gateway, before lodging | Institutional approval/renewal, mortgage and finance-lease lifecycle (#1, #3–#11) |
| **Customer payment at counter/online, before decision** *(#13–#17 always sourced this way; #12 and #18 normalized 2026-08-16)* | The end customer | At the point of service (Trustee Centre counter, Land Department, or online, per C2) — **before** RERA's decision, for all six | Title, ownership, and contract transactions (#12–#18 except #2) |

**Service #2 pays nothing.** It is not a third model — it is the absence of a payment step, confirmed 2026-08-15 (B11).

**Why it matters:** #1 needs a checkout step before the application can be lodged, where it previously needed a post-approval payment prompt. #2's payment screens, if any were ever built against the old "pays after decision" assumption, should be removed rather than reworked — there is nothing to charge. **#12 and #18 now need a checkout step at lodging, the same as #13–#17** — where they previously needed a payment prompt gated on RERA's decision, that gate is retired. Any screen or workflow step built against the old post-decision assumption for #12/#18 should be reworked to match #13–#17, not treated as a distinct case anymore.

## Settlement Mechanisms

The source names three settlement routes across the platform:

* **Payment gateway** — card, bank transfer, and USSD (per the PRD's payment requirements)
* **Escrow deduction** — against a project trust account
* **Institution account debit** — against a bank's standing account with RERA

**Group C now uses payment gateway only, for every service that charges a fee.** Institution account debit is retired for this module — there is no standing account left to debit against (`open-questions.md` B1). Escrow deduction remains Group B's developer-services mechanism, where the Account Trustee acts as an approval step; unaffected by either correction and not a Group C payment route either before or after them.

## Fee Calculation

**RERA sets the fee for each service directly.** The amount is configuration, held in the platform's fee schedule engine (FR-16) and populated by RERA — not derived from loan value, property value, or any other figure belonging to the financial institution's relationship with its own customer (`open-questions.md` B6). This fee-setting principle applies module-wide. **As of 2026-08-16, the fee is computed and charged at the same point for every fee-bearing service: at checkout, before lodging** — never after RERA's decision, and never, for #2 (confirmed 2026-08-15 — no fee applies).

> **Corrected 2026-08-14.** This section previously derived mortgage-service fees ad valorem from "application type, property value, and classification," treating RERA's fee as scaling with the secured loan amount. That conflated two things B6 now separates: the FI's own lending economics with its customer (never RERA's concern, never documented here) and RERA's own per-service fee (a flat, RERA-set figure per service code). FR-16's "application type... classification" language may still describe RERA varying its fee by service *type* — compatible with the corrected model — but a per-loan ad valorem calculation is specifically ruled out.

### To Confirm

* Is VAT applied to all 18 services or only some? *(Resolved — B7, confirmed 2026-08-15: VAT applies to all 18 services, no exemptions. Removed from this list.)*
* Are institutional approval and renewal fees annual, or per application? *(Resolved — B8, confirmed 2026-08-15: per-approval-term, renewing. The two-year duration specifically remains a proposal, not a sourced or separately confirmed figure.)*
* Does cancellation carry a fee? *(Resolved — B11, confirmed 2026-08-15: no. Removed from this list.)*
* ~~Is #12/#18's post-decision payment timing intentional, or an artefact of the counter-based process?~~ **Resolved 2026-08-16 — artefact of the old process, normalized. Removed from this list.**

## Payment Artefacts

**Corrected 2026-08-14 — collapses to one artefact.** `open-questions.md` B9 (which previously distinguished a "fee balance" standing-account statement line from a "payment receipt") is superseded, not reworked: with no standing account, there is no fee balance to distinguish from anything. Every payment is a single, per-transaction event.

| Artefact | What it is | Appears in |
| :---- | :---- | :---- |
| Payment Receipt (e-receipt) | Proof that a single transaction settled, issued at checkout before lodging — **for every fee-bearing service, following the 2026-08-16 normalization** | Every fee-bearing Group C service (#1, #3–#18) |
| Tax Invoice | Platform-wide requirement (PRD) | All fee-bearing services |

**Service #2 issues no payment artefact**, having no fee to settle (B11, confirmed 2026-08-15).

"E-receipt voucher," used by name in source row 45 (#18), and "Payment Receipts," used by name in source row 39 (#7), are both the same artefact as Payment Receipt above under different names — row 39 in particular is the naming pattern every other mortgage-service row should be read as matching, not the exception it was treated as under the old fee-balance framing.

**Confidence:** Confirmed on the collapse to one artefact (client decision via B1/B9). The exact receipt field set is not specified in source.

## Failed and Reversed Payments

**Corrected 2026-08-14, then again 2026-08-16.** The old model's failure handling (`open-questions.md` B3, B4, B10) assumed a standing account: an approved-but-unsettled transaction held for 30 days before expiring, and a failed settlement retried against a balance that could run low. None of that applies once payment happens before an application is even lodged. **The 2026-08-16 normalization removes the one remaining case (#12/#18) where a different failure mode — payment failing after approval — genuinely existed.**

* **Payment failure at checkout is not an application-lifecycle event, for any of the 17 fee-bearing services.** The application hasn't been lodged yet. The user retries payment; nothing is submitted, certified, or audited until it succeeds.
* **A rejected application has already paid, for every fee-bearing service.** What happens to that fee — refund, forfeiture, or something else — is not addressed by any source document or by any payment-model correction. Left genuinely open; see To Confirm — Summary.
* **A settled payment needing reversal** (overpayment, a voided transaction) has no institution-specific route documented under the corrected model. `open-questions.md` B10's old argument for bypassing the platform's public refund route rested entirely on protecting a standing account's same-day reconciliation, which no longer exists — that argument doesn't carry over. Whether Group C should still get an expedited refund path on some other basis is not decided here.
* **Service #2 has no payment to fail or reverse.** Not applicable, having no fee at all.

**What this replaces.** The old section here described `Approved — Awaiting Payment` as a real, visible state for #12/#18, a 30-calendar-day expiry to `Expired` (B3), and same-day automatic credit-back to a settlement account (B10). None of these apply any longer — see Additional Statuses below.

## Additional Statuses

**Corrected 2026-08-16 — `Approved — Awaiting Payment` no longer occurs for any Group C service.** The 2026-08-15 correction found and preserved #12/#18 as a genuine exception where this status applied; the 2026-08-16 payment-timing normalization retires that exception by design rather than by documentation. See [services-overview.md](services-overview.md)'s Application Status Vocabulary section for the same correction, applied there.

* **`Expired`, as previously defined for Group C, does not occur anywhere.** Its only sourced meaning here was `open-questions.md` B3's "approved but unsettled for 30 calendar days" — a scenario written for a registered-title, standing-account context that never described any Group C service cleanly, including #12/#18's now-retired exception. **B3 itself was not in scope for this correction and remains as written in `open-questions.md`.**

| Status | Meaning | Still applies to Group C? |
| :---- | :---- | :---- |
| Payment Failed | Checkout attempted and declined; retryable, nothing submitted/lodged yet | Yes, for all 17 fee-bearing services (pre-lodging, following the 2026-08-16 normalization) |
| Refund Requested | A settled fee is under refund review | Open — see Failed and Reversed Payments above; not resolved which route applies |

## To Confirm — Summary

**Corrected 2026-08-16.** B1, B2, B4, B5, B6, B7, B8, B9, B10, and B11 are resolved. What remains, after the 2026-08-16 payment normalization:

1. **What happens to the fee on a rejected application** (refund, forfeiture, or otherwise) — not addressed by any source document or by any payment-model correction. Applies to all 17 fee-bearing services now, following the normalization — this question is no longer split between #1–#17 and #12/#18, since every service now pays before the decision.
2. **Whether Group C should use the platform's public refund route, or some other route, for a settled payment needing reversal** — B10's old argument for a special route no longer holds; no replacement decision has been made.
3. **The B3/`Expired` tension** flagged above under Additional Statuses — B3 wasn't in scope for this correction, and its sourced scenario doesn't cleanly describe any current Group C service.
4. **Whether the shared payment gateway is genuinely the same build artefact as individual-user's wallet primitive (P-22), or a separate integration** — P-22 is documented as balance-based, which doesn't cleanly match Group C's no-standing-account model (`open-questions.md` B2).
5. ~~What happens if a customer approved under #12 or #18 never returns to pay at the counter?~~ **Moot as of 2026-08-16** — payment now happens before RERA's decision, before there is anything to "not return" for.
