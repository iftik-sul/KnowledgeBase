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

**All 12 are now written as standalone documents (2026-08-16).**

### Application Lifecycle (2)

**Restructured 2026-08-16** from a four-feature split (Submit Application / Track Application Status / Respond to Information Request / Resubmit Returned Application) that mirrored individual-user's framing rather than this module's own screens. `ui/screens-unified/` groups Services Catalog + Service Details + Submit Application as one flow; `ui/screens/` has exactly one pair of screens (`applications.md` + `application-details.md`, plus `application-review.md`) covering tracking, responding, and resubmitting — there was never a dedicated screen for any of those three as a separate thing.

* [Feature #1 — Service Requests](service-flows/feature-01-service-requests.md) — browse the catalog, view a service's requirements, complete and submit the canonical application form. Absorbs what was separately proposed as "Services Catalog" (General Platform) and "Submit Application" (Application Management).
* [Feature #2 — Applications](service-flows/feature-02-applications.md) — the single workspace for everything after submission: tracking, responding to RERA information requests, resubmitting after a RERA return, downloading outputs. Absorbs what were separately proposed as "Track Application Status," "Respond to Information Request," and "Resubmit Returned Application."

### Institution-Specific (5)

**Two genuinely new entries found 2026-08-16** by checking role responsibilities against built screens, not present in the original 17-feature list at all: Trust Accounts and Compliance Reports.

* [Feature #3 — Internal Certification Queue](service-flows/feature-03-internal-certification-queue.md) — transactions awaiting certify-or-return by any of the institution's four Group C users before routing to RERA, Services #3–#11 only. Sourced screen: `internal-certification-queue.md`. **Corrected 2026-08-14**: previously gated by a "checker permission scope"; scopes are retired module-wide, this is now an unrestricted action attributed by role — see [navigation.md#audit-trail-principle](navigation.md#audit-trail-principle).
* [Feature #4 — Escrow Request Queue](service-flows/feature-04-escrow-request-queue.md) — developer-originated requests (Real Estate Developer's escrow services, not one of Group C's own 18) awaiting assessment, certification, or return by any of the institution's four Group C roles. Sourced screens: `escrow-request-queue.md`, `escrow-request-details.md` (A2). SLA sourced via A6. **Status vocabulary corrected 2026-08-16, twice, plus terminology clarification** — see Cross-Module Correction and Cross-Module Clarification below.
* [Feature #5 — Trust Accounts](service-flows/feature-05-trust-accounts.md) *(new)* — the institution's register of trust accounts under management, distinct from the intake queue above. Sourced directly from the Account Trustee's documented responsibility: *"Maintain the register of trust accounts under management"* (`roles-and-responsibilities.md`). Sourced screen: `trust-accounts.md`.
* [Feature #6 — Compliance Reports](service-flows/feature-06-compliance-reports.md) *(new)* — the Auditing Bureau Officer's independent audit and reporting function: raising findings against trust accounts, opening/closing audit engagements, submitting RERA-defined compliance reports. Sourced directly from documented responsibilities: *"Prepare and submit independent compliance reports to RERA... Raise findings against trust accounts... Open and close audit engagements."* Sourced screen: `compliance-reports.md`.
* [Feature #7 — Payment History](service-flows/feature-07-payment-history.md) — per-transaction payment records: receipts, amounts, service references, status. Sourced screen: `payment-history.md`. **Corrected 2026-08-14** — previously "Settlement Account" (balance, top-up, ledger, low-balance alerting); that standing account is retired (`open-questions.md` B1) — see [payments.md](payments.md). **Payment model normalized 2026-08-16** — see Payments below; the "three payment timings" this feature previously described are now two.

**Dropped from the previous list, with reasons:**
* *Approval Expiry Tracking* — no dedicated screen exists. Expiry display already lives on `institution-profile.md`; folded into Feature #10 (Institution Profile) below rather than kept as a separate feature with no screen behind it.
* *Staff Records / Staff & Permission Scopes* — **decided 2026-08-16, no longer dropped — a dedicated screen and feature is being built.** See Staff Management below, superseding the previous Open Gap treatment.

### General Platform (5)

* [Feature #8 — Dashboard](service-flows/feature-08-dashboard.md) — the same content for every user (2026-08-15 unification, [navigation.md](navigation.md#landing-after-login)); not role-specific. Aggregates Features #1–#7's own figures without independent data of its own. Sourced screen: `dashboard.md`.
* [Feature #9 — Documents](service-flows/feature-09-documents.md) — centralized repository across applications, escrow requests, compliance records; upload happens only from within an originating feature, never standalone. Sourced screen: `documents.md`.
* [Feature #10 — Institution Profile](service-flows/feature-10-institution-profile.md) — the institution's registered identity and regulatory standing, including current approval status and expiry (absorbing the display-only part of the dropped Approval Expiry Tracking above — renewal itself is *initiated* through Service #1, not a separate action here). Sourced screen: `institution-profile.md`.
* [Feature #11 — Notifications](service-flows/feature-11-notifications.md) — centralized alerts across applications, approvals, escrow, certification, compliance. **Corrected 2026-08-16** — the #12/#18 awaiting-counter-payment category found 2026-08-15 is retired along with the payment model that produced it; see Payments below. Sourced screen: `notifications.md`.
* [Feature #12 — Help & Support](service-flows/feature-12-help-and-support.md) — **built 2026-08-16, by client decision — see below**, superseding the prior `TBD` treatment.

## Staff Management — Built 2026-08-16, by Client Decision

**Feature #13 — Staff Records**, a new dedicated screen and feature, closing the gap found the same day between `roles-and-responsibilities.md`'s documented Institution Relationship Manager responsibility (*"Add and remove staff records within the institution"*) and the absence of any screen representing it. See `service-flows/feature-13-staff-records.md` for the full specification.

## Help & Support — Built 2026-08-16, by Client Decision

**Feature #12** is no longer `TBD`. Built at Claude's discretion, by explicit client instruction, since no source material existed to derive it from. See `service-flows/feature-12-help-and-support.md` for the full specification — content is clearly marked as a proposed build, not sourced, throughout.

## Payments — Normalized 2026-08-16, by Client Decision

**Services #12 and #18's post-approval payment timing is confirmed to be an artefact of the source's counter-based process, not intentional design, and is normalized to pay-before-decision** — matching Services #13–#17's pattern, once digitized onto the shared platform gateway.

This retires the two-way-model-with-an-exception structure documented since 2026-08-15: **all fee-bearing Group C services now pay before RERA's decision** — either upfront via the shared platform gateway (Services #1, #3–#11) or at the point of service, before RERA reviews, at the counter or online (Services #12–#18). Service #2 remains fee-free (confirmed 2026-08-15, `open-questions.md` B11) — unaffected by this normalization, since there was never a payment step to reorder.

**Consequence for the status vocabulary below:** `Approved — Awaiting Payment` no longer occurs for any Group C service, including #12 and #18. The exception documented on 2026-08-15 (found via a per-service audit that specifically checked #12 and #18 against their own sourced workflow order) is now closed by this normalization rather than left standing. See [payments.md](payments.md) for the full corrected model and Services #12 and #18's own files for the corrected per-service timing.

## Cross-Module Correction: Escrow Status Vocabulary

**Corrected 2026-08-16, twice.** First pass renamed this feature's statuses to `Pending Approval → Under Review → Approved → Released`, matching real-estate-developer's Escrow Management — but that vocabulary itself was wrong, taken from a UI screen's filter values rather than the sourced service files it was meant to describe.

**Checked directly against all six escrow service files on the developer side (#8, #9, #10, #12, #20, #21) — all six independently use the same sourced vocabulary**, not either module's earlier guess:

`Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → [service-specific terminal state]`, plus additional statuses `Information Requested / Returned / Rejected`.

This feature's vocabulary is corrected to match: the institution's own assessment stage is `Trustee Review` (not `Pending Approval` or `Under Assessment`), and a Certify action advances a request from `Trustee Review` into the explicit, separately-named `RERA Escrow Audit` stage — closing the original gap (no status for RERA's post-certification review) more precisely than the first correction did, since `RERA Escrow Audit` is now its own named stage rather than an ambiguous continuation of a shared "Under Review." See `feature-04-escrow-request-queue.md`'s own Feature Overview and Section 13 for the full corrected flow, and the mirrored correction in real-estate-developer's `shared-platform-features.md`.

## Cross-Module Clarification: "RERA Escrow Audit" and "Compliance & Escrow Auditor" Are the Same Role

**Clarified 2026-08-16.** While correcting the status vocabulary above, a further terminology gap was checked directly against `RERAN_service_flows_v2.md`'s master Service Workflows table: real-estate-developer's six escrow rows (8–12, 20–21) and this module's mortgage/lease rows (30–39) carry the identical **"Compliance & Escrow Auditor"** value in the Regulator/Approver column. There is only one such role in the source's Groups & Roles table (Group A, Compliance Directorate — *"Audits escrow/trust accounts, vets off-plan sales, monitors disclosure, sanctions defaulters"*). This feature's own "RERA's Escrow Department" — inherited from real-estate-developer's service files, which in turn carried the source table's own narrative Workflow-column phrasing — names the same role this module already calls the Compliance & Escrow Auditor everywhere else (e.g. Service #3, Mortgage Registration). Both phrasings trace to source; neither was wrong, they were simply never cross-linked before. Feature #4 now names the role explicitly rather than leaving "escrow department" as an unlabeled synonym.

## Platform Features Summary

| Category | Features | Status |
| :---- | :---: | :---- |
| Application Lifecycle | 2 | Written |
| Institution-Specific | 5 | Written |
| Staff Management | 1 | Written 2026-08-16 |
| General Platform | 5 | Written |
| **Total Shared Platform Features** | **13** | **13 of 13 written** |

## Application Status Vocabulary

> **Confirmed 2026-08-16, by client decision.** The platform-wide-core-plus-Group-C-extension vocabulary below is accepted as correct, superseding `open-questions.md` D1's open status.

| Status | Meaning | Set by |
| :---- | :---- | :---- |
| Draft | Started, not submitted | Any of the institution's four Group C roles |
| Pending Internal Certification *(Group C extension — services with an internal certification gate only)* | Awaiting certify-or-return by any of the institution's four Group C users | Any Group C role, attributed in the audit trail |
| Returned by Certifier *(Group C extension)* | Sent back internally for correction | Any Group C role, attributed in the audit trail |
| Submitted | In RERA's Transaction Audit queue | Internal Certifier, or the applicant directly where no internal gate applies |
| Under Review | With the regulator | Compliance & Escrow Auditor |
| Information Requested | RERA has raised a query | Compliance & Escrow Auditor |
| Returned for Correction | Sent back to the applicant | Compliance & Escrow Auditor |
| Approved | Passed audit | Compliance & Escrow Auditor |
| Rejected | Refused with documented reason | Compliance & Escrow Auditor |
| Completed | Settled and output document issued | Platform |
| Withdrawn | Abandoned by the applicant | Applicant |

**Corrected 2026-08-16 — `Approved — Awaiting Payment` and `Expired` are removed, this time for all 18 services without exception.** Both existed only because Services #12 and #18 sourced payment after RERA's decision; that timing is now normalized to pay-before-decision (see Payments above), so nothing is ever approved while still awaiting payment, for any Group C service. This supersedes the 2026-08-15 correction, which found and preserved #12/#18 as a genuine exception — that exception is now closed by design decision rather than merely documented.

`Pending Internal Certification` and `Returned by Certifier` apply only to services with a sourced two-gate pattern (Services #3–#11, the mortgage and finance-lease lifecycle). Services #1, #2, and #12–#18 do not carry them, since no internal institutional certification step is described in source for those rows — see each service flow's Application Status Flow section.

## Channels

> **Resolved by `open-questions.md` C2.** Every Group C service is documented as **online-capable**. The Trustee Centre is an assisted mode of the same online service, not a separate paper channel — Registration Flow 7 provisions Trustee Centre operators with individual NIMC-verified accounts and per-operator transaction scopes, under audit. This reverses the earlier assumption that counter-only services should be preserved as documented, and is the only reading compatible with the PRD (US-14's diaspora requirement, Business Goal 2's processing-time target, and the platform's stated purpose of removing in-person visits). **Confidence:** High.

* **Online Mortgage System** — the institution's own portal access, the primary channel for the mortgage lifecycle (Services #3–#7)
* **Real Estate Registration Trustee Centres** — the assisted mode of the same online service, used for finance lease services (#8–#11) and several title & ownership transactions (#12–#17), operated by a Trustee Centre operator (Group G) on the customer's or institution's behalf
* **Land Department** — the assisted-mode channel named directly in source for Services #15–#17

Whether direct customer/institution access to a given service is *enabled at launch*, versus assisted-mode-only, is a configuration decision, not an architecture one.

## To Confirm

1. Are the five proposed service categories acceptable, or should the source's Development / Transaction / Title-Deed Data grouping be retained? (C1 — proposed answer: adopt them, keep the reconciliation table.)
2. Does the restructured 13-feature Shared Platform Features layer correctly represent what this module needs? **All 13 are now written.**
3. ~~Staff Management open gap~~ **Decided 2026-08-16 — build one. Done, see Feature #13.**
4. ~~Help & Support content~~ **Decided 2026-08-16 — build one, full discretion given. Done, see Feature #12.**
5. ~~Is the proposed status vocabulary acceptable?~~ **Confirmed 2026-08-16.**
6. ~~Fee settlement: is the two-way payer/timing split correct, and is #12/#18's post-approval timing intentional?~~ **Decided 2026-08-16 — artefact of the old process, normalized to pay-before-decision. Done, see Payments above.**
