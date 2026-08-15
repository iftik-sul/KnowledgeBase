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
  - "RERAN/modules/financial-trust-institutions/ui/README.md"
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
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

> **Rebuilt 2026-08-16, bottom-up, from the module's actual built screens** — `ui/screens/` (13 files) and `ui/screens-unified/` (4 files, plus README), cross-checked against `roles-and-responsibilities.md`'s documented per-role responsibilities. This replaces the previous 17-feature list (4 Application Management + 5 Institution-Specific + 8 General Platform), which was proposed by analogy to individual-user's feature count rather than checked against what this module actually has built. The count is now **12**, not because features were arbitrarily cut, but because several of the original 17 turned out to be the same screen described twice (Track Application Status and Applications; Services Catalog and Submit Application), while two others that genuinely have their own built screens — Trust Accounts, Compliance Reports — were missing from the original 17 entirely. Still `> **Proposed**` overall: the *existence* of this shared layer is not itself sourced (no such concept appears in `RERAN_service_flows_v2.md`), only its content is now checked against what's actually built. Needs client confirmation.

### Application Lifecycle (2)

**Restructured 2026-08-16** from a four-feature split (Submit Application / Track Application Status / Respond to Information Request / Resubmit Returned Application) that mirrored individual-user's framing rather than this module's own screens. `ui/screens-unified/` groups Services Catalog + Service Details + Submit Application as one flow; `ui/screens/` has exactly one pair of screens (`applications.md` + `application-details.md`, plus `application-review.md`) covering tracking, responding, and resubmitting — there was never a dedicated screen for any of those three as a separate thing.

* [Feature #1 — Service Requests](service-flows/feature-01-service-requests.md) — browse the catalog, view a service's requirements, complete and submit the canonical application form. Absorbs what was separately proposed as "Services Catalog" (General Platform) and "Submit Application" (Application Management).
* [Feature #2 — Applications](service-flows/feature-02-applications.md) — the single workspace for everything after submission: tracking, responding to RERA information requests, resubmitting after a RERA return, downloading outputs. Absorbs what were separately proposed as "Track Application Status," "Respond to Information Request," and "Resubmit Returned Application."

### Institution-Specific (5)

**Two genuinely new entries found 2026-08-16** by checking role responsibilities against built screens, not present in the original 17-feature list at all:

* **Feature #3 — Internal Certification Queue** — transactions awaiting certify-or-return by any of the institution's four Group C users before routing to RERA. Sourced screen: `internal-certification-queue.md`. **Corrected 2026-08-14**: previously gated by a "checker permission scope"; scopes are retired module-wide, this is now an unrestricted action attributed by role — see [navigation.md#audit-trail-principle](navigation.md#audit-trail-principle). *(Standalone document not yet written.)*
* **Feature #4 — Escrow Request Queue** — developer-originated requests awaiting Account Trustee (or, under unified access, any Group C role's) assessment, certification, or return. Sourced screens: `escrow-request-queue.md`, `escrow-request-details.md` (A2). *(Standalone document not yet written.)*
* **Feature #5 — Trust Accounts** *(new)* — the institution's register of trust accounts under management, distinct from the intake queue above. Sourced directly from the Account Trustee's documented responsibility: *"Maintain the register of trust accounts under management"* (`roles-and-responsibilities.md`). Sourced screen: `trust-accounts.md`. Missing from the original 17-feature list entirely. *(Standalone document not yet written.)*
* **Feature #6 — Compliance Reports** *(new)* — the Auditing Bureau Officer's independent audit and reporting function: raising findings against trust accounts, opening/closing audit engagements, submitting RERA-defined compliance reports. Sourced directly from documented responsibilities: *"Prepare and submit independent compliance reports to RERA... Raise findings against trust accounts... Open and close audit engagements."* Sourced screen: `compliance-reports.md`. Previously buried as a single "Reporting / compliance alerts" bullet under Dashboard/Notifications examples, not its own feature. *(Standalone document not yet written.)*
* **Feature #7 — Payment History** — per-transaction payment records: receipts, amounts, service references, status. Sourced screen: `payment-history.md`. **Corrected 2026-08-14** — previously "Settlement Account" (balance, top-up, ledger, low-balance alerting); that standing account is retired (`open-questions.md` B1) — see [payments.md](payments.md). *(Standalone document not yet written.)*

**Dropped from the previous list, with reasons:**
* *Approval Expiry Tracking* — no dedicated screen exists. Expiry display already lives on `institution-profile.md`; folded into Feature #10 (Institution Profile) below rather than kept as a separate feature with no screen behind it.
* *Staff Records / Staff & Permission Scopes* — see **Open Gap** below. Not folded into anything, because folding it in would misrepresent an actual documentation hole as resolved.

### General Platform (5)

* **Feature #8 — Dashboard** — the same content for every user (2026-08-15 unification, [navigation.md](navigation.md#landing-after-login)); not role-specific. Sourced screen: `dashboard.md`.
* **Feature #9 — Documents** — centralized repository across applications, escrow requests, compliance records. Sourced screen: `documents.md`.
* **Feature #10 — Institution Profile** — the institution's registered identity and regulatory standing, including current approval status and expiry (absorbing the display-only part of the dropped Approval Expiry Tracking above — renewal itself is *initiated* through Service #1, not a separate action here). Sourced screen: `institution-profile.md`.
* **Feature #11 — Notifications** — centralized alerts across applications, approvals, escrow, certification, compliance. Sourced screen: `notifications.md`.
* **Feature #12 — Help & Support** — help content, FAQ, support contact. Named in [navigation.md](navigation.md)'s sidebar; no screen file built yet, content largely `TBD`.

## Open Gap: Staff Management

**Found 2026-08-16, not resolved.** `roles-and-responsibilities.md` documents the Institution Relationship Manager's responsibility to *"Add and remove staff records within the institution"* — and `open-questions.md` A1/A5 both assume delegated staff exist under a corporate account. But no screen in `ui/screens/` or `ui/screens-unified/`, and no item in [navigation.md](navigation.md)'s sidebar, represents staff management at all. This is a genuine hole between a documented role responsibility and the built UI — not silently folded into Institution Profile (which has no staff-roster content in its own spec) and not invented as a new feature without a screen behind it, the same standard applied to Approval Expiry Tracking above. Needs a client decision: build a dedicated screen, or confirm this responsibility is out of scope for the current UI package.

## Platform Features Summary

| Category | Features |
| :---- | :---: |
| Application Lifecycle | 2 |
| Institution-Specific | 5 |
| General Platform | 5 |
| **Total Shared Platform Features** | **12** |

Open gap (not counted above): Staff Management — documented responsibility, no screen, no feature.

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

1. Are the five proposed service categories acceptable, or should the source's Development / Transaction / Title-Deed Data grouping be retained? (C1 — proposed answer: adopt them, keep the reconciliation table.)
2. Does the restructured 12-feature Shared Platform Features layer (rebuilt 2026-08-16 from actual screens, replacing the earlier 17-feature list) correctly represent what this module needs? In particular: is the Service Requests / Applications split (2 features instead of the earlier 4) right, and are Trust Accounts / Compliance Reports correctly identified as missing pieces rather than over-documentation?
3. Staff Management open gap (new 2026-08-16): should a dedicated screen/feature be built, or is this responsibility out of scope for the current UI package?
4. Is the proposed status vocabulary (platform core + Group C extension, D1) acceptable, and is the specific status list correct?
5. Fee settlement: is the corrected two-way payer/timing split (Upfront Gateway Payment / Customer Payment at Counter, with Service #2 fee-free — see `payments.md`) correct for all 18 services? **Also worth confirming with the client:** whether #12 and #18's post-approval payment timing is intentional design, or an artefact of the source's counter-based process that should be normalized to match #13–#17's pay-first pattern once digitized.
