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

---

## A. Roles & Service Structure

### A1. Does the source's Responsible Role column hold up service-by-service?

**Yes, cleanly — unlike Group B and Group C.** Both of those modules' Responsible Role columns turned out to be coarse category defaults that didn't survive contact with individual rows (Group C's column named "Mortgage Officer" for 15 of 18 rows, including transactions with no lending component at all). Group D's column is different: every JOP row (46–56) names Owners'-Association Manager, every Licensing row (59–66) names Brokerage Principal, every Rental row (67–69) names Property Management Officer, every Transaction row (70–71) names Brokerage Principal, and every Dispute row (57–58) names Company Dispute Filing Officer — a clean 1:1 mapping to category, with no cross-contamination anywhere.

This doesn't change anything about access — per the unified-access decision, any of the four roles may act on any service regardless. It does mean the "typically handled by" framing in `roles-and-responsibilities.md` can be trusted as accurate description, not treated with the same skepticism Group B/C's column needed.

**Confidence:** Sourced.

### A2. Does row 65 (Real Estate Evaluation Details Certificate) genuinely belong to Group D?

**Provisionally kept in Group D, flagged for client confirmation, not moved unilaterally.**

Row 65's own workflow text reads differently from every other Group D row: "sign up and login via evaluation company option... accept or reject application... make real estate evaluation... add evaluation details, value and notes." The actor accepting or rejecting is the evaluation company itself, processing a customer's request for a valuation — not RERA reviewing a company's own regulatory filing, which is the shape every other Group D row has. This reads as a Group G (Allied Professionals — Valuer role) service that the source table happened to file under Group D's row range.

Against moving it: the source table explicitly assigns this row to Group D in its own Group column, and Group G's roles and services are not yet documented in this project — reassigning it now would mean building Group D content for a service that might belong to an undocumented module. Kept here, provenance flagged in `services-overview.md`, service-flow file (once written) to carry the same flag rather than presenting Group D ownership as settled.

**Confidence:** Medium. **If wrong:** the module's count drops from 26 to 25, and Real Estate Licensing Services from 8 to 7 — both are cleanly reversible if the client confirms reassignment.

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

**Proposed: keep the sourced pay-after-decision timing as the default, flagged explicitly as a normalization candidate for the same reason Financial & Trust Institutions' #1, #12, and #18 were normalized.**

The parallel is close: Financial & Trust Institutions' Service #1 (Approval/Renewal) originally paid after RERA's decision, exactly like Group D's #12–15 do now, and the client chose to move it upfront on 2026-08-15, then extended the same normalization to #12/#18 on 2026-08-16 once their post-decision timing was found. Group D's four services are structurally the closest analogue anywhere in the project to what Financial & Trust Institutions' #1 looked like *before* that normalization.

Proposing "keep as sourced" rather than "normalize pre-emptively" because the earlier normalizations were client decisions, not something inferred from source alone — this document doesn't get to decide the client wants Group D built the same way without being asked. But flagging it this explicitly, rather than leaving it as a routine payment-timing note, means the question is visible early rather than discovered mid-build the way it was for Group C.

**Confidence:** Medium on "keep as sourced" being the right default to build against; High on "this is a real candidate the client should be asked about directly," given the close precedent.

**If the client says normalize:** Model 2 folds into Model 3 (pay-then-output), and #12–15's service-flow files, `payments.md`, and any UI built in Phase 4 all need the same kind of multi-file correction Financial & Trust Institutions needed on 2026-08-16 — worth getting this answer *before* Phase 3 rather than after, unlike how it happened for Group C.

### B5. Exact fee amounts

**Client data.** No fee amount is given in source for any of the 26 services. Same conclusion as every other module's equivalent question (Financial & Trust Institutions B5, Individual User's equivalent) — treated as RERA-configured, not missing data to chase, per B5's reasoning above.

**Confidence:** Confirmed as client data — the one question in this document with no proposed number, matching the pattern every other module's payments analysis has had exactly one of.

---

## C. Platform-Wide

### C1. Status vocabulary

**Adopt D1 as-is** — the platform-core lifecycle (Draft → Submitted → Under Review → Information Requested → Returned for Correction → Approved → Rejected → Completed → Withdrawn → Expired) that Financial & Trust Institutions' D1 already established, with no Group D extension needed.

Financial & Trust Institutions added a Group C extension (`Pending Internal Certification`, `Returned by Certifier`) because its mortgage/lease services source an internal certification gate. Per A5 above, Group D has no such gate anywhere — so Group D needs the platform core only, unextended. This is the first module in the project confirmed to need no module-specific extension at all.

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

**One item flagged for direct client confirmation, distinct from B5's fee-amount question, which is expected to remain unanswerable from source alone:**

* **B4** — whether Group D's Licensing services (#12–15) should be normalized to pay-before-lodging, matching the precedent set by Financial & Trust Institutions' #1/#12/#18. Proposed answer is to build against the sourced timing and ask directly, rather than normalize pre-emptively or leave the question implicit until Phase 4 the way it happened for Group C.

**Also flagged, lower priority:**

* **A2** — row 65's Group D vs. Group G provenance.
* **A4** — row 60's single-service-with-a-type-field treatment.

Neither A2 nor A4 blocks Phase 3 — both have a proposed answer this document is building against, and both are cleanly reversible if the client says otherwise.
