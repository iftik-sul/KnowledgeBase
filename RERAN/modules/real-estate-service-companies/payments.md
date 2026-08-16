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
tags:
  - real-estate-service-companies
  - payments
---

# Real Estate Service Companies — Payments

**Checked service by service, not assumed as one model.** Financial & Trust Institutions started from a single-model assumption and needed two later corrections once individual rows were checked; this document checks every one of Group D's 26 rows directly before proposing a model, following the build playbook's Phase 2 instruction.

## The Headline Finding

**19 of Group D's 26 services carry no fee at all.** This is a materially higher no-fee proportion than any other module documented so far — Financial & Trust Institutions has 1 free service out of 18, Individual User has 5 out of 43. Do not build a "most services are chargeable" default anywhere in this module's UI or validation layer the way other modules reasonably could; here, **free is the norm and a fee is the exception**, concentrated almost entirely in the Licensing and Transaction categories.

## Payment Models

Four distinct patterns, not one:

### Model 1 — No Fee

**19 services.** All 11 Jointly Owned Property services (#1–11), all 3 Rental services (#20–22), and 4 of the 8 Licensing services (#16 Cancel Card, #17 Amend Card, #18 Evaluation Certificate, #19 Training Accreditation), plus 1 Transaction service (#23 Auction Permit).

Sourced directly — none of these rows' workflow text mentions a payment step at any point, from submission through output delivery.

### Model 2 — Institution Fee Payment (pay after decision)

**4 services: #12–15** (Real Estate Licensing Application, Real Estate Permit Application, Issue Professional Practice Card, Renew Professional Practice Card).

Sourced sequence, all four rows: submit → audit/acceptance → **pay** → receive output. Payment is the last step before delivery, not the first step of submission.

> **This is the same shape Financial & Trust Institutions' Service #1 had before its 2026-08-15 client-directed normalization to pay-before-lodging.** Flagged here as a genuine candidate for the same normalization, not applied unilaterally — see Open Question B4 below. The source is unambiguous about the *current* sequence; whether the client wants it changed the way Group C's #1 was changed is a separate decision.

### Model 3 — Upfront / Pay-Then-Output

**1 service: #24** (Registration of a Property Sold by Auction).

Sourced sequence: submit docs → **pay service fees** → receive service outputs (Certificate of Title, Map, Payment Receipts). No separate audit step is named between payment and output — payment is effectively the last user-facing action before the system delivers.

### Model 4 — Customer Payment at Counter, Channel-Dependent

**2 services: #25, #26** (Primary Suit and Execution Case, both Joint Property disputes).

Both rows describe two channels with different timing, the same shape Individual User's Submit Tenancy Dispute (#26) uses:

* **Service Center:** submit docs → enter system and audit → **pay fees** → attend session/hearing. Payment follows audit.
* **Online:** upload docs → **e-pay** → attend session. No separate audit step is named between upload and payment — payment sits essentially at submission.

## Who Pays

The company (through whichever of its four Group D roles is acting) pays in every fee-bearing service — there is no service where a third party (a unit owner, a tenant, a customer) is described as the payer. This differs from Financial & Trust Institutions, where several services (#12–18) name the *customer* as payer rather than the institution. Worth confirming this reading holds — see Open Question B1.

## Fee Calculation

No fee amounts are given in source for any of the 26 services. Per the precedent set in Financial & Trust Institutions (`open-questions.md` B5), treat this as RERA-configured, populated through the fee-schedule engine (FR-16), not as missing client data to chase — the same conclusion, reached the same way, applies here without needing independent re-derivation.

## Additional Statuses

No service in Group D sources an `Approved — Awaiting Payment`-shaped state the way Financial & Trust Institutions' Services #12/#18 briefly did (see that module's own corrected history). Model 2's four services (#12–15) pay *after* audit but *before* output — the closest analogue — but because payment is the terminal step before delivery, not an intermediate wait state a user returns to later, this reads as a normal "Approved, pending payment" step within the same session rather than a distinct status requiring its own badge. Revisit this if Model 2 is normalized per Open Question B4 — an upfront-payment model would remove the question entirely, the same way Group C's normalization retired the status for #12/#18.

## To Confirm — Summary

1. **Should Model 2's pay-after-decision timing (#12–15) be normalized to pay-before-lodging**, matching the pattern the client chose for Financial & Trust Institutions' #1, #12, and #18? See Open Question B4.
2. **Does the JOP category's absence of an Account Trustee step mean it genuinely does not share Group B/C's escrow mechanism**, or does the source simply omit an intermediary that should still be modeled? See Open Question A3.
3. **Fee amounts** — client data, same as every other module (B5-equivalent).
