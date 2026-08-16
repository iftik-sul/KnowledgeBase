---
project: RERAN
module: real-estate-service-companies
type: decision
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/roles-and-responsibilities.md"
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/payments.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - real-estate-service-companies
  - open-questions
  - decisions
---

# Group D — Questions and Proposed Answers

Every question below carries a **proposed answer**, following the standing instruction not to leave things for the client that can be reasoned to from the source material. Confidence levels match Financial & Trust Institutions' convention:

| Level | Meaning |
| :---- | :---- |
| **Sourced** | The source material answers this directly |
| **High** | A strong inference from the source |
| **Medium** | A reasonable design judgement; a different answer would also be defensible |
| **Client data** | Cannot be reasoned to. Only RERA holds the answer |

**Scope note:** post-login functionality only. Registration and onboarding are excluded.

**2026-08-16 update, post-Phase-5.** Both items flagged for direct client confirmation are now resolved: **A2** — Service #18 stays in Group D, to be wired into the UI. **B4** — Services #12–15 are normalized to pay-before-lodging, matching the precedent set for Financial & Trust Institutions' #1/#12/#18. Both are client decisions, not re-derivations — see each answer below for what changes as a result, and the propagation checklist each carries.

---

## A. Roles & Service Structure

### A1. Does the source's Responsible Role column hold up service-by-service?

**Yes, cleanly — unlike Group B and Group C.** Both of those modules' Responsible Role columns turned out to be coarse category defaults that didn't survive contact with individual rows (Group C's column named "Mortgage Officer" for 15 of 18 rows, including transactions with no lending component at all). Group D's column is different: every JOP row (46–56) names Owners'-Association Manager, every Licensing row (59–66) names Brokerage Principal, every Rental row (67–69) names Property Management Officer, every Transaction row (70–71) names Brokerage Principal, and every Dispute row (57–58) names Company Dispute Filing Officer — a clean 1:1 mapping to category, with no cross-contamination anywhere.

This doesn't change anything about access — per the unified-access decision, any of the four roles may act on any service regardless. It does mean the "typically handled by" framing in `roles-and-responsibilities.md` can be trusted as accurate description, not treated with the same skepticism Group B/C's column needed.

**Confidence:** Sourced.

### A2. Does row 65 (Real Estate Evaluation Details Certificate) genuinely belong to Group D?

**Confirmed 2026-08-16 (client decision) — kept in Group D, to be wired into the UI.**

Row 65's own workflow text still reads differently from every other Group D row: "sign up and login via evaluation company option... accept or reject application... make real estate evaluation... add evaluation details, value and notes." The actor accepting or rejecting is the evaluation company itself, processing a customer's request for a valuation — not RERA reviewing a company's own regulatory filing, the shape every other Group D row has. That structural oddity is unchanged by this decision; **what's resolved is ownership, not the service's own atypical shape.** The client has confirmed this stays a Group D service on the source table's own terms, rather than being reassigned to an undocumented Group G module.

**What this changes:** Service #18 was excluded from the module's Phase 4 UI build entirely (no catalogue entry, no wizard path, no dashboard reference) pending this decision. It now needs a Phase 4 follow-up pass — see the propagation checklist below. Its own atypical workflow (evaluation company decides, not RERA) still doesn't fit the standard company-to-RERA submission pattern every other service uses, so it needs its own screen treatment, not a forced fit into `submit-application.md`'s Pattern A/B/C shell.

> **Superseded framing (pre-2026-08-16).** Previously: "provisionally kept in Group D, flagged for client confirmation, not moved unilaterally... kept here, provenance flagged... rather than presenting Group D ownership as settled." Ownership is now settled; the underlying structural-oddity observation this answer was built on is preserved above rather than deleted, since it still explains why this service needs different UI treatment from the other 24 selectable services.

**Confidence:** Confirmed (client decision, 2026-08-16).

**Files needing a follow-up pass, not yet done as of this entry:**

* `service-flows/service-18-register-evaluation-details-certificate.md` — remove the "not resolved" provenance framing at the top; update to reflect confirmed status.
* `services-overview.md` — remove the "provisionally kept... excluded from UI" language in the Row-to-Service Mapping section.
* `navigation.md` — remove the section excluding Service #18 from the sidebar/catalogue.
* `role-workflows.md` — add Service #18 to the Licensing cluster's shared journey.
* `ui/screens/services-catalog.md` — remove the 7-of-8-selectable exclusion note; Licensing becomes 8 of 8 selectable.
* `ui/screens/service-details.md` and a new atypical-flow screen (not yet designed) for Service #18's evaluation-company-decides shape.
* `ui/screens/dashboard.md` — remove the Notes-section exclusion.
* `roles-and-responsibilities.md` — update its own Open Questions item 1, which still describes this as unresolved.

### A3. Does the JOP category share Group B/C's escrow-Trustee mechanism?

**No — checked directly against the workflow text, not assumed either way.**

Rows 50–56 (the escrow-adjacent JOP services: transfer, close, accredit signatories, appoint auditors) each describe the same five-step shape: "sign up/log in to Owner system, fill details, attach docs, submit; audit and acceptance/rejection; receive approval via email." No row names an Account Trustee, or any intermediary actor between the Owners'-Association Manager and RERA's Compliance & Escrow Auditor. This is structurally different from Real Estate Developer's escrow services (#8–12, #20–21), which explicitly route through "Trustee Account studies capability, uploads & sends docs" before RERA's audit, and from Financial & Trust Institutions' Escrow Request Queue, which exists specifically to model that Trustee step.

The "escrow account" terminology in several JOP row titles ("transferring the escrow account," "close the project escrow account," "accredit authorized signatories on the escrow account") is about a jointly-owned property's own escrow account as a *subject matter* — the same way Financial & Trust Institutions' Trust Accounts feature is about accounts as subject matter — not evidence of a shared processing mechanism. The mechanism itself (direct company-to-regulator, no Trustee) is genuinely different from Group B/C's.

**Recommendation:** do not cross-link JOP's escrow-adjacent services to `financial-trust-institutions/ui/screens/escrow-request-queue.md` the way the original issue #34 considered. Model them as a direct two-step company-to-regulator flow, matching what's actually sourced.

**Confidence:** High. **If wrong:** JOP's escrow services would need a Trustee-facing queue added later, the same shape as Financial & Trust Institutions' Escrow Request Queue — a real but bounded rework, not a full redesign, since the company-facing side of the flow wouldn't change.

### A4. Does row 60 (Real Estate Permit Application) bundle multiple permit types into one service?

**No — one service with a Permit Type field, not four separate services.**

Row 60's channel column lists "Electronic, classified, billboard, and SMS advertisement permits" as sub-types reachable through the RERA App specifically, while "all types" also go through the Land Department website. The workflow steps (sign up, fill details, attach docs, audit, pay, receive certificate) are identical regardless of type — nothing in the row describes type-specific steps, fields, or outputs the way Individual User's lease-registration row (which split into #23/#24) had genuinely distinct downstream services. This reads as one service with a type-selection field, not several services sharing a row.

**Confidence:** Medium. **If wrong:** this splits into two services (a general permit type, and an "RERA App" advertisement-permit type, or four if each advertisement channel is genuinely distinct) — a design judgement, not a sourced fact either way, so flagged rather than treated as settled.

### A5. Is there an internal company-side certification gate anywhere in Group D, the way Financial & Trust Institutions' mortgage services (#3–11) have?

**No — not sourced anywhere in Group D's 26 rows.**

Every Group D workflow goes directly from company submission to RERA audit (Compliance & Escrow Auditor or Dispute Adjudication Officer, depending on category) — no row describes an internal "company auditor" or maker-checker step comparable to Financial & Trust Institutions' "audited by bank auditor" language. This means Group D's Application Status Flow (D1, adopted below) does not need the Group C extension statuses (`Pending Internal Certification`, `Returned by Certifier`) anywhere — every service goes straight to `Submitted`.

**Confidence:** Sourced.

---

## B. Payments

### B1. Does the company always pay, or does a third party ever pay instead?

**The company always pays, in every fee-bearing service.** No Group D row names a unit owner, tenant, or other customer as payer — contrast Financial & Trust Institutions, where Services #12–18 name the *customer* rather than the institution as payer. Every fee-bearing Group D row (#12–15, #24, #25, #26) describes the company itself (through whichever of its four roles is filing) completing payment.

**Confidence:** Sourced.

### B2. Fee basis — flat, or does it vary by transaction value?

**RERA sets a flat, configured fee per service, the same conclusion Financial & Trust Institutions reached (B6).** No Group D row ties a fee to a transaction value, property value, or any other company-side figure the way an ad valorem model would require. Adopt Financial & Trust Institutions' B6 answer directly rather than re-deriving it: RERA's fee-schedule engine (FR-16) sets a fee per service code.

**Confidence:** High, adopted from Financial & Trust Institutions B6.

### B3. VAT applicability

**Adopt Financial & Trust Institutions' B7 answer directly: VAT applies to all fee-bearing services, no exemptions.** Nothing in Group D's source rows contradicts this, and no module-specific reason exists to treat Group D's 7 fee-bearing services differently from Financial & Trust Institutions' 17.

**Confidence:** High, adopted from Financial & Trust Institutions B7. Genuinely Medium on its own — Group D has no source row that mentions VAT explicitly the way Financial & Trust Institutions' off-plan workflow does — but there's no basis to treat it differently either, so the platform-wide default carries over.

### B4. Should Model 2's pay-after-decision timing (#12–15) be normalized to pay-before-lodging?

**Confirmed 2026-08-16 (client decision) — normalized to pay-before-lodging, matching Financial & Trust Institutions' #1/#12/#18 precedent.**

Payment for Services #12, #13, #14, and #15 now happens as part of submission, via the shared platform gateway, before RERA reviews the application — the same pattern used by the majority of fee-bearing services elsewhere in the project. This retires "Model 2 — Institution Fee Payment (pay after decision)" as a category in `payments.md`: no Group D service pays after RERA's decision any more.

**This is a genuinely new decision, not a re-derivation** — row 59–62's own sourced sequence ("audit and acceptance; log in, select payment, pay") was correctly read the first time; the client has decided to build differently from what the source describes, the same framing Financial & Trust Institutions' equivalent corrections used for their own #1/#12/#18.

> **Superseded framing (pre-2026-08-16).** Previously proposed: "keep the sourced pay-after-decision timing as the default... flagged explicitly as a normalization candidate." That was the right way to build *before* the client weighed in — a proposed default, not an assumption the answer was already known. The client has since confirmed the normalization directly.

**Confidence:** Confirmed (client decision, 2026-08-16).

**Files needing a follow-up pass, not yet done as of this entry:**

* `payments.md` — retire Model 2, fold #12–15 into an upfront-payment model (distinct from #24's pay-then-output Model 3, since #12–15 now pay *before* RERA review rather than as the last step before output).
* `service-flows/service-12` through `service-15` — Sections 9, 12, 13, 20, 21 each need the same kind of correction Financial & Trust Institutions' #1/#12/#18 needed.
* `role-workflows.md` — the Licensing cluster's shared-journey description still says "audit/acceptance → pay → receive output."
* `ui/screens/submit-application.md` — Section 5's branching for #12–15 (payment skipped during submission, collected later) needs removing; these four services fold into the same submission-time payment step as #24.
* `ui/screens/application-review.md` — Section 5 (Payment Confirmation) now applies to #12–15 as well as #24/#25/#26 online.
* `ui/screens/application-details.md` — remove the "Currently with... payment due," the Payment Pending progress step, and the Complete Payment action, all built specifically for #12–15's old timing.
* `ui/screens/applications.md` — remove or update the Awaiting Payment status card's #12–15-specific framing.
* `ui/screens/notifications.md` — remove the Payment Due Priority Alert category, built specifically for this now-retired timing.
* `ui/status-badges.md` — remove the Payment Pending application status.
* `ui/validation-rules.md` — simplify the Payments section's four-model description; the submission-blocking rule no longer needs to carve out an exception for #12–15.
* `shared-platform-features.md` — the "Features Considered and Not Built" Payment History note cites #12–15's payment-due tracking as a reason it might be needed; re-evaluate now that the scenario no longer exists.

### B5. Exact fee amounts

**Client data.** No fee amount is given in source for any of the 26 services. Same conclusion as every other module's equivalent question (Financial & Trust Institutions B5, Individual User's equivalent) — treated as RERA-configured, not missing data to chase, per B5's reasoning above.

**Confidence:** Confirmed as client data — the one question in this document with no proposed number, matching the pattern every other module's payments analysis has had exactly one of.

---

## C. Platform-Wide

### C1. Status vocabulary

**Adopt D1 as-is** — the platform-core lifecycle (Draft → Submitted → Under Review → Information Requested → Returned for Correction → Approved → Rejected → Completed → Withdrawn → Expired) that Financial & Trust Institutions' D1 already established, with no Group D extension needed.

Financial & Trust Institutions added a Group C extension (`Pending Internal Certification`, `Returned by Certifier`) because its mortgage/lease services source an internal certification gate. Per A5 above, Group D has no such gate anywhere — so Group D needs the platform core only, unextended. **With B4's normalization, this is now true without exception** — the platform core needs no Group D extension at all, not even the narrower `Payment Pending` addition this module briefly carried for #12–15 during Phase 4.

**Confidence:** High, adopted from D1 directly.

### C2. Is the unified-access model (no per-role gating) appropriate for Group D from the start?

**Yes — already adopted in `roles-and-responsibilities.md` and `services-overview.md`, per explicit build instruction rather than derived here.** Both Group B and Group C reached this same model after a role-permission-matrix phase that later needed retracting. Group D skips that phase entirely. This isn't a new derivation — it's a build decision already made and applied in Phase 1, recorded here for completeness since Financial & Trust Institutions' equivalent question (implicit in its own navigation.md history) belongs in this document's category.

**Confidence:** Confirmed (build instruction, not inferred).

---

## Summary

| Area | Questions | Answered | Needs client data |
| :---- | :---: | :---: | :---: |
| A. Roles & Service Structure | 5 | 5 | 0 |
| B. Payments | 5 | 5 | 1 (B5 only) |
| C. Platform-Wide | 2 | 2 | 0 |
| **Total** | **12** | **12** | **1** |

**Both items previously flagged for direct client confirmation are now resolved (2026-08-16):**

* ~~**B4**~~ — confirmed: Services #12–15 normalized to pay-before-lodging, matching Financial & Trust Institutions' #1/#12/#18 precedent.
* ~~**A2**~~ — confirmed: Service #18 stays in Group D, to be wired into the UI in a Phase 4 follow-up pass.

**A4** remains flagged, lower priority, with a proposed answer this document is building against — the row-60 permit-bundling question is still reversible if the client says otherwise, and hasn't been raised directly the way A2 and B4 were.

**Propagation is not yet complete for either resolved item** — both entries above carry a "Files needing a follow-up pass" checklist. Per the module's own established discipline (see Financial & Trust Institutions' three-pass `Approved — Awaiting Payment` history for what happens when this step is skipped), a decision recorded here is not the same as a decision executed everywhere it's referenced. Treat this document's Confirmed status as the record of the decision, not evidence the rest of the module already reflects it.
