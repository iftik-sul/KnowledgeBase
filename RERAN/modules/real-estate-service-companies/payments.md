---
project: RERAN
module: real-estate-service-companies
type: payments
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
tags:
  - real-estate-service-companies
  - payments
---

# Real Estate Service Companies — Payments

**Checked service by service, not assumed as one model.** Financial & Trust Institutions started from a single-model assumption and needed two later corrections once individual rows were checked; this document checks every one of Group D's 26 rows directly before proposing a model, following the build playbook's Phase 2 instruction.

> **Corrected 2026-08-16 (client decision, `open-questions.md` B4).** Services #12–15 (Real Estate Licensing Application, Permit Application, Issue Practice Card, Renew Practice Card) originally sourced payment happening *after* RERA's audit and acceptance — "audit and acceptance; log in, select payment, pay." The client has confirmed this should be normalized to pay-before-lodging, matching the precedent set for Financial & Trust Institutions' #1, #12, and #18. **"Model 2 — Institution Fee Payment (pay after decision)" is retired.** Group D now has three payment models, not four.

## The Headline Finding

**19 of Group D's 26 services carry no fee at all.** This is a materially higher no-fee proportion than any other module documented so far — Financial & Trust Institutions has 1 free service out of 18, Individual User has 5 out of 43. Do not build a "most services are chargeable" default anywhere in this module's UI or validation layer the way other modules reasonably could; here, **free is the norm and a fee is the exception**, concentrated almost entirely in the Licensing and Transaction categories. This finding is unaffected by the 2026-08-16 normalization — it changes *when* the 7 fee-bearing services pay, not how many of the 26 charge anything at all.

## Payment Models

Three distinct patterns, following the 2026-08-16 normalization:

### Model 1 — No Fee

**19 services.** All 11 Jointly Owned Property services (#1–11), all 3 Rental services (#20–22), and 4 of the 8 Licensing services (#16 Cancel Card, #17 Amend Card, #18 Evaluation Certificate, #19 Training Accreditation), plus 1 Transaction service (#23 Auction Permit).

Sourced directly — none of these rows' workflow text mentions a payment step at any point, from submission through output delivery.

### Model 2 — Upfront Gateway Payment (pay before lodging)

**4 services: #12–15** (Real Estate Licensing Application, Real Estate Permit Application, Issue Professional Practice Card, Renew Professional Practice Card).

**Corrected 2026-08-16 (client decision).** Payment is completed via the shared platform gateway as part of submission, before the application is lodged for RERA's review — the same pattern the majority of fee-bearing services across the project use, and the same normalization Financial & Trust Institutions applied to its own comparable Service #1.

> **Superseded sourced sequence.** All four rows originally described "submit → audit/acceptance → pay → receive output" — payment as the last step before delivery, not the first step of submission. That sourced sequence is preserved here for the record, the same way Financial & Trust Institutions kept its own superseded reasoning rather than deleting it: row 59–62's post-decision sequencing was correctly read the first time; the client has since decided to build differently from what the source describes, distinguishing this from a re-derivation.

### Model 3 — Pay-Then-Output

**1 service: #24** (Registration of a Property Sold by Auction).

Sourced sequence: submit docs → **pay service fees** → receive service outputs (Certificate of Title, Map, Payment Receipts). No separate audit step is named between payment and output — payment is effectively the last user-facing action before the system delivers. **Distinct from Model 2**, even though both now pay "before completion" in a loose sense: Model 2 pays before RERA ever reviews the application; Model 3 pays as the final step of a process RERA has (implicitly) already reviewed.

### Model 4 — Customer Payment at Counter, Channel-Dependent

**2 services: #25, #26** (Primary Suit and Execution Case, both Joint Property disputes).

Both rows describe two channels with different timing, the same shape Individual User's Submit Tenancy Dispute (#26) uses:

* **Service Center:** submit docs → enter system and audit → **pay fees** → attend session/hearing. Payment follows audit.
* **Online:** upload docs → **e-pay** → attend session. No separate audit step is named between upload and payment — payment sits essentially at submission.

## Who Pays

The company (through whichever of its four Group D roles is acting) pays in every fee-bearing service — there is no service where a third party (a unit owner, a tenant, a customer) is described as the payer. This differs from Financial & Trust Institutions, where several services (#12–18) name the *customer* rather than the institution as payer.

## Fee Calculation

No fee amounts are given in source for any of the 26 services. Per the precedent set in Financial & Trust Institutions (`open-questions.md` B5), treat this as RERA-configured, populated through the fee-schedule engine (FR-16), not as missing client data to chase — the same conclusion, reached the same way, applies here without needing independent re-derivation.

## Additional Statuses

**Corrected 2026-08-16.** With Model 2's normalization, no service in Group D sources an `Approved — Awaiting Payment` or `Payment Pending`-shaped state anywhere in the module — the scenario this status would represent (an approved application still owing a fee) no longer exists. This module never carried the status as a genuinely built feature outside a brief Phase 4 addition for #12–15 specifically; see `ui/status-badges.md`'s own correction note for that removal.

## To Confirm — Summary

1. ~~**Should Model 2's pay-after-decision timing (#12–15) be normalized to pay-before-lodging?**~~ **Resolved 2026-08-16** — yes, per client decision (`open-questions.md` B4).
2. **Does the JOP category's absence of an Account Trustee step mean it genuinely does not share Group B/C's escrow mechanism**, or does the source simply omit an intermediary that should still be modeled? See `open-questions.md` A3 — unaffected by this correction.
3. **Fee amounts** — client data, same as every other module (B5-equivalent).
