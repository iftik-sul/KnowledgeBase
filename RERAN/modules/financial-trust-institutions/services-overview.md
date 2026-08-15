---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-16
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - financial-trust-institutions
  - services-overview
---

# Financial & Trust Institutions — Services Overview

18 business services, verified against the master service table (rows 28–45). This total reconciles with the source workbook's own summary: Development 2 + Transaction 15 + Title-Deed Data 1 = 18.

All 18 are approved by the **Compliance & Escrow Auditor**, a Group A role. No Group C service is self-approving.

## Business Services

### 1. Institutional Approval Services (2)

Approval and cancellation of the institution's standing as an approved trustee or auditor.

* Service #1 — Approval / renewal of Account Trustee & Auditing company
* Service #2 — Cancellation of Account Trustee & Auditing company

### 2. Mortgage Services (5)

The core lending lifecycle against registered titles.

* Service #3 — Mortgage registration
* Service #4 — Mortgage amendment
* Service #5 — Mortgage transfer
* Service #6 — Mortgage release
* Service #7 — Grant property mortgage

### 3. Finance Lease Services (4)

The finance lease lifecycle, mirroring the mortgage services.

* Service #8 — Finance lease registration
* Service #9 — Finance lease amendment
* Service #10 — Finance lease transfer
* Service #11 — Finance lease release

### 4. Title & Ownership Transaction Services (6)

Title-deed transactions executed through the institution rather than by the owner directly.

* Service #12 — Registration of real estate fund companies in the register of privileges
* Service #13 — Sale procedure (heirs)
* Service #14 — Company shares sale
* Service #15 — Updating title deed information
* Service #16 — Split ownership
* Service #17 — Issuance of title deed

### 5. Contract Services (1)

* Service #18 — Contract cancellation

> **Proposed** — the five category names above are not in the source material. The source groups these 18 services under three internal admin categories (Development 2, Transaction 15, Title-Deed Data 1), which describe RERA's filing structure rather than what an institution user does. The regrouping is by user-facing task, matching the approach taken in the individual-user module. The underlying 18 services and their count are unchanged and fully sourced. Needs client confirmation.

## Business Services Summary

| Category | Services |
| :---- | :---: |
| Institutional Approval Services | 2 |
| Mortgage Services | 5 |
| Finance Lease Services | 4 |
| Title & Ownership Transaction Services | 6 |
| Contract Services | 1 |
| **Total Business Services** | **18** |

### Reconciliation to Source Categories

| Source category | Count | Maps to |
| :---- | :---: | :---- |
| Development | 2 | Institutional Approval Services |
| Transaction | 15 | Mortgage (5) + Finance Lease (4) + Title & Ownership (6) |
| Title-Deed Data | 1 | Contract Services |
| **Total** | **18** | |

## Service Ownership

**Confirmed 2026-08-15 (client decision) — no service is role-specific.** Any of the institution's four Group C roles — Mortgage Officer, Institution Relationship Manager, Account Trustee, Auditing Bureau Officer — may act on any of the 18 services. There is no per-service or per-role assignment table; role is retained solely for audit-trail attribution (who performed which action), consistent with the access-model correction — see [navigation.md#audit-trail-principle](navigation.md#audit-trail-principle).

The source's responsible-role column (naming the Mortgage Officer for 15 of the 18 rows, including several Trustee Centre counter transactions with no lending component) remains unreliable as a per-service assignment, which is why an earlier version of this section attempted to re-derive ownership per service rather than accept the column at face value. That re-derivation is superseded, not extended: the client has confirmed Group C does not assign services to roles at all, so no corrected table is needed — see `open-questions.md` A4 for the full reasoning and the retired per-service table, kept there for the record.

**Trustee Centre Operator (Group G) is a channel/assisted-mode role, not a Group C role**, and was never a correct entry in a Group C ownership table — see C2 for the assisted-mode channel model, which is unaffected by this correction.

## Shared Platform Features

> **Proposed** — not in source material. Rationale: the source defines a standard six-stage pipeline (lodge → validate → audit → pay → issue → record) that every regulated service follows, and the individual-user module documents four shared application-management features serving that pipeline. Group C services run the same pipeline and therefore require the same capabilities. Needs client confirmation.

### Application Management (4)

**Written 2026-08-16** — all four now exist as standalone documents in [service-flows/](service-flows/), following the same 21-section template as this module's numbered services and cross-checked against this module's own two-gate certification pattern and two-way payment-timing split, rather than copied uniformly from individual-user's version of the same features. Each remains `status: draft` / `contains_proposals: true` pending client confirmation of To Confirm item 2 below.

* [Feature #1 — Submit Application](service-flows/feature-01-submit-application.md)
* [Feature #2 — Track Application Status](service-flows/feature-02-track-application-status.md)
* [Feature #3 — Respond to Information Request](service-flows/feature-03-respond-to-information-request.md)
* [Feature #4 — Resubmit Returned Application](service-flows/feature-04-resubmit-returned-application.md)

### Institution-Specific Features (5)

> **Proposed** — C4 finds the original three correct but incomplete. Two more are load-bearing consequences of B1 and A1/A5 and are added here.

* Feature #5 — Internal Certification Queue — transactions awaiting certify-or-return by any of the institution's four Group C users before routing to RERA. **Corrected 2026-08-14**: previously described as gated by a "checker permission scope"; permission scopes are retired module-wide, and this is now an unrestricted action attributed by role in the audit trail, not a scope or a fifth role — see [navigation.md#audit-trail-principle](navigation.md#audit-trail-principle). *(Not yet written as a standalone document — out of scope for the 2026-08-16 Application Management pass; the four docs above reference it but do not duplicate it.)*
* Feature #6 — Escrow Request Queue — developer-originated requests awaiting Account Trustee action, confirmed as a queue inside the platform (A2)
* Feature #7 — Approval Expiry Tracking — trustee and auditor approval renewal windows, now driven by the two-year validity period proposed in B8
* Feature #8 — Payment History — per-transaction payment records for the institution: receipts, amounts, service references, and status (successful / failed / refund-requested). **Corrected 2026-08-14** — previously "Settlement Account" (balance, top-up, transaction ledger, low-balance alerting, periodic statements) for a standing pre-funded account; that account is retired (`open-questions.md` B1). This feature is a per-transaction history/reporting view, not an account-management subsystem — see [payments.md](payments.md).
* Feature #9 — Staff Records — roster and staff-record management for the institution's delegated staff (A1, A5). **Corrected 2026-08-14** — previously "Staff & Permission Scopes," with scope assignment and revocation; permission scopes are retired module-wide, and every staff member has identical system access from the moment they're added, so this feature is now purely about who is on the institution's staff list for audit-trail attribution — see [navigation.md#audit-trail-principle](navigation.md#audit-trail-principle).

### General Platform Features (8)

* Dashboard
* Services Catalog
* Applications
* Documents
* Payments — note: Group C runs two payer/timing models, not one (see `payments.md`, corrected 2026-08-15): **Upfront gateway payment** for Services #1 and #3–#11 (paid by the institution via the shared platform gateway, before the application is lodged — #3–#11 corrected 2026-08-14, #1 corrected 2026-08-15, both retiring earlier post-approval models) and **Customer Payment at Counter** for Services #12–#18 (paid by the customer at the point of service, sourced, unaffected by either correction). **Service #2 carries no fee at all** (confirmed 2026-08-15, `open-questions.md` B11) — it is not a third model, simply the absence of a payment step. *(Corrected 2026-08-15 — previously listed three models, including "Institution Fee Payment" for Services #1–#2, paid after RERA's decision; that model is retired, see `payments.md`.)*
* Notifications
* Institution Profile
* Help & Support

## Platform Features Summary

| Category | Features |
| :---- | :---: |
| Application Management | 4 |
| Institution-Specific | 5 |
| General Platform | 8 |
| **Total Shared Platform Features** | **17** |

## Application Status Vocabulary

> **Proposed — superseded by `open-questions.md` D1.** The status vocabulary is now platform-wide core, with a Group C extension, rather than a status set defined from scratch for this module alone. Needs client confirmation of the specific list, though the platform-wide-core-plus-module-extension principle carries **High** confidence (FR-18/FR-19 require a live dashboard and configurable reports across all regulatory service areas, neither buildable over per-module vocabularies).

| Status | Meaning | Set by |
| :---- | :---- | :---- |
| Draft | Started, not submitted | Any of the institution's four Group C roles |
| Pending Internal Certification *(Group C extension — services with an internal certification gate only)* | Awaiting certify-or-return by any of the institution's four Group C users *(corrected 2026-08-14 — not a "checker permission scope"; scopes are retired, see [navigation.md](navigation.md))* | Any Group C role, attributed in the audit trail |
| Returned by Certifier *(Group C extension)* | Sent back internally for correction | Any Group C role, attributed in the audit trail *(corrected 2026-08-14 — not "Internal Certifier (checker permission scope)")* |
| Submitted | In RERA's Transaction Audit queue | Internal Certifier, or the applicant directly where no internal gate applies |
| Under Review | With the regulator | Compliance & Escrow Auditor |
| Information Requested | RERA has raised a query | Compliance & Escrow Auditor |
| Returned for Correction | Sent back to the applicant | Compliance & Escrow Auditor |
| Approved — Awaiting Payment *(Services #12 and #18 only — see note below)* | Passed audit; fee not yet settled | Compliance & Escrow Auditor |
| Rejected | Refused with documented reason | Compliance & Escrow Auditor |
| Completed | Settled and output document issued | Platform |
| Withdrawn | Abandoned by the applicant | Applicant |
| Expired *(does not occur for any Group C service — see note below)* | Approved but left unpaid for 30 calendar days (B3) | Platform |

**Corrected 2026-08-15** — the "Set by" column for `Draft` previously read "Mortgage Officer / Institution Relationship Manager / Trustee Centre Operator," naming specific roles as if only they could start an application. Per the corrected A4, any of the institution's four Group C roles may do this; Trustee Centre Operator remains correct as the assisted-mode channel actor, unrelated to this correction.

`Pending Internal Certification` and `Returned by Certifier` apply only to services with a sourced two-gate pattern (Services #3–#11, the mortgage and finance-lease lifecycle). Services #1, #2, and #12–#18 do not carry them, since no internal institutional certification step is described in source for those rows — see each service flow's Application Status Flow section.

**Corrected 2026-08-15, revised again same day after a fuller per-service audit — `Approved — Awaiting Payment` is not universally absent.** An earlier pass this same day claimed the status "no longer applies to any Group C service, including #1–#2," reasoning that #1 now pays upfront (B11) and #2 carries no fee, closing the last case where payment could follow approval. That reasoning is correct as far as it goes, but incomplete: it never checked Services #12–#18 individually against their own sourced workflow order. Doing so found that **Services #12 and #18 genuinely source payment *after* RERA's decision** (row 38 and row 45 respectively), while Services #13–#17 source payment *before* RERA's decision. So the status is accurate for exactly two of the eighteen services, not zero — see each of those two files' own Section 13 for the sourced sequence. `Expired` remains correctly absent everywhere: its only sourced basis, B3's "approved but unregistered" reasoning, was written for a registered-title, post-approval-payment context that doesn't describe #12/#18's short counter-payment window either.

## Channels

> **Resolved by `open-questions.md` C2.** Every Group C service is documented as **online-capable**. The Trustee Centre is an assisted mode of the same online service, not a separate paper channel — Registration Flow 7 provisions Trustee Centre operators with individual NIMC-verified accounts and per-operator transaction scopes, under audit. This reverses the earlier assumption that counter-only services should be preserved as documented, and is the only reading compatible with the PRD (US-14's diaspora requirement, Business Goal 2's processing-time target, and the platform's stated purpose of removing in-person visits). **Confidence:** High.

* **Online Mortgage System** — the institution's own portal access, the primary channel for the mortgage lifecycle (Services #3–#7)
* **Real Estate Registration Trustee Centres** — the assisted mode of the same online service, used for finance lease services (#8–#11) and several title & ownership transactions (#12–#17), operated by a Trustee Centre operator (Group G) on the customer's or institution's behalf
* **Land Department** — the assisted-mode channel named directly in source for Services #15–#17

Whether direct customer/institution access to a given service is *enabled at launch*, versus assisted-mode-only, is a configuration decision, not an architecture one.

## To Confirm

Five items remain open in this section, down from seven — A4 (service ownership) is now confirmed by client decision (2026-08-15) and B5 (fee schedule) is resolved as a configuration fact rather than client data (2026-08-14); neither is repeated below. C2 (online path) and the original Service Ownership questions for #1/#2 were already excluded before this rewrite.

1. Are the five proposed service categories acceptable, or should the source's Development / Transaction / Title-Deed Data grouping be retained? (C1 — proposed answer: adopt them, keep the reconciliation table.)
2. Do the four Application Management features apply to Group C as they do to individual users? (C3 — proposed answer: yes, unchanged.) **Written 2026-08-16, still open**: the four documents now exist (linked above) and are cross-checked against this module's own two-gate and two-payment-model patterns rather than copied uniformly — but the underlying question (should Group C carry this layer at all, and does the write-up correctly capture it) is unchanged and still needs client confirmation.
3. Are the five institution-specific features (including the two added by C4 — Payment History, Staff Records) correct, and is anything still missing?
4. Is the proposed status vocabulary (platform core + Group C extension, D1) acceptable, and is the specific status list correct?
5. Fee settlement: is the corrected two-way payer/timing split (Upfront Gateway Payment / Customer Payment at Counter, with Service #2 fee-free — see `payments.md`) correct for all 18 services? **Corrected 2026-08-15** — this item previously described a three-way split, including Institution Fee Payment for Services #1–#2; that model is retired per `open-questions.md` B11. **Also worth confirming with the client:** whether #12 and #18's post-approval payment timing is intentional design, or an artefact of the source's counter-based process that should be normalized to match #13–#17's pay-first pattern once digitized.
