---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-10
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

> **Proposed — re-derived, not the source's responsible-role column.** `open-questions.md` A4 finds that column unreliable as a per-service assignment: it names the Mortgage Officer for 15 of the 18 rows (30–44), including heirs' sale, company share sale, split ownership, and title-deed issuance — Trustee Centre counter transactions with no lending component that a bank's mortgage desk does not run. The table below re-derives ownership per service instead. **Confidence:** High for Services #1–#2; Medium for the #12–#17 re-derivation, since it contradicts the source column and that should be visible to the client.

| Role | Services | Basis |
| :---- | :---: | :---- |
| Institution Relationship Manager | 3 (#1, #2, #18) | #1–#2: A4 re-derivation (source names Account Trustee; IRM is described as maintaining registration and renewing trustee/auditor approvals). #18: sourced directly — row 45 already names the IRM. |
| Mortgage Officer | 9 (#3–#11), plus #12–#17 where bank-originated | Sourced for #3–#11 — the only rows whose workflow text shows bank-originated entry ("bank employee enters ... via online mortgage system"). A4's rule for #12–#17 is conditional, not absolute — "Mortgage Officer where bank-originated; otherwise executed by a Trustee Centre operator" — but no row among 38, 40–44 sources a bank-originated variant for those six, so this branch is carried as unconfirmed rather than counted. |
| Trustee Centre Operator (Group G, assisted mode) | 6 (#12–#17) | A4's *otherwise* branch — title & ownership transaction rows show customer walk-in entry with no bank involvement, despite the source column naming the Mortgage Officer. This is the only branch of A4's conditional that rows 38, 40–44 actually source; see each service flow's Open Questions for the unconfirmed Mortgage Officer branch. |
| Account Trustee | 0 | Acts within Group B escrow services (A2); owns no numbered Group C service. |
| Auditing Bureau Officer | 0 | Acts as the internal certification gate on Mortgage Officer transactions (A1/D2), modelled as a permission scope rather than service ownership. |

The #12–#17 count reflects only the sourced (Trustee Centre) branch of A4's conditional — it is not a claim that these six services can *only* ever be bank-originated-excluded. This replaces the previous count (Mortgage Officer 17 / Institution Relationship Manager 1), which took the source's responsible-role column at face value.

## Shared Platform Features

> **Proposed** — not in source material. Rationale: the source defines a standard six-stage pipeline (lodge → validate → audit → pay → issue → record) that every regulated service follows, and the individual-user module documents four shared application-management features serving that pipeline. Group C services run the same pipeline and therefore require the same capabilities. Needs client confirmation.

### Application Management (4)

* Feature #1 — Submit Application
* Feature #2 — Track Application Status
* Feature #3 — Respond to Information Request
* Feature #4 — Resubmit Returned Application

### Institution-Specific Features (5)

> **Proposed** — C4 finds the original three correct but incomplete. Two more are load-bearing consequences of B1 and A1/A5 and are added here.

* Feature #5 — Internal Certification Queue — transactions awaiting the checker permission scope's certification before routing to RERA (A1/D2: a maker-checker permission scope on the corporate account, not a fifth role)
* Feature #6 — Escrow Request Queue — developer-originated requests awaiting Account Trustee action, confirmed as a queue inside the platform (A2)
* Feature #7 — Approval Expiry Tracking — trustee and auditor approval renewal windows, now driven by the two-year validity period proposed in B8
* Feature #8 — Settlement Account — balance, top-up, transaction ledger, low-balance alerting, and periodic statements for the institution's standing pre-funded account (B1)
* Feature #9 — Staff & Permission Scopes — roster, scope assignment, and revocation for delegated institution staff (A1, A5)

### General Platform Features (8)

* Dashboard
* Services Catalog
* Applications
* Documents
* Payments — note: Group C runs three payer models rather than one (see `payments.md`): Institution Account Debit for Services #3–#11 (deducted from the institution's standing settlement account after approval, B1), Customer Payment at Counter for Services #12–#18 (paid by the customer, with a receipt or e-receipt voucher issued, B9), and Institution Fee Payment for Services #1–#2 (paid by the institution on approval of its own standing)
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
| Draft | Started, not submitted | Mortgage Officer / Institution Relationship Manager / Trustee Centre Operator |
| Pending Internal Certification *(Group C extension — services with an internal maker-checker gate only, see A1/D2)* | Awaiting the institution's own checker permission scope | Mortgage Officer |
| Returned by Certifier *(Group C extension)* | Sent back internally for correction | Internal Certifier (checker permission scope) |
| Submitted | In RERA's Transaction Audit queue | Internal Certifier, or the applicant directly where no internal gate applies |
| Under Review | With the regulator | Compliance & Escrow Auditor |
| Information Requested | RERA has raised a query | Compliance & Escrow Auditor |
| Returned for Correction | Sent back to the applicant | Compliance & Escrow Auditor |
| Approved — Awaiting Payment | Passed audit; fee not yet settled | Compliance & Escrow Auditor |
| Rejected | Refused with documented reason | Compliance & Escrow Auditor |
| Completed | Settled and output document issued | Platform |
| Withdrawn | Abandoned by the applicant | Applicant |
| Expired | Approved but left unpaid for 30 calendar days (B3) | Platform |

`Pending Internal Certification` and `Returned by Certifier` apply only to services with a sourced two-gate pattern (Services #3–#11, the mortgage and finance-lease lifecycle). Services #1, #2, and #12–#18 do not carry them, since no internal institutional certification step is described in source for those rows — see each service flow's Application Status Flow section.

## Channels

> **Resolved by `open-questions.md` C2.** Every Group C service is documented as **online-capable**. The Trustee Centre is an assisted mode of the same online service, not a separate paper channel — Registration Flow 7 provisions Trustee Centre operators with individual NIMC-verified accounts and per-operator transaction scopes, under audit. This reverses the earlier assumption that counter-only services should be preserved as documented, and is the only reading compatible with the PRD (US-14's diaspora requirement, Business Goal 2's processing-time target, and the platform's stated purpose of removing in-person visits). **Confidence:** High.

* **Online Mortgage System** — the institution's own portal access, the primary channel for the mortgage lifecycle (Services #3–#7)
* **Real Estate Registration Trustee Centres** — the assisted mode of the same online service, used for finance lease services (#8–#11) and several title & ownership transactions (#12–#17), operated by a Trustee Centre operator (Group G) on the customer's or institution's behalf
* **Land Department** — the assisted-mode channel named directly in source for Services #15–#17

Whether direct customer/institution access to a given service is *enabled at launch*, versus assisted-mode-only, is a configuration decision, not an architecture one.

## To Confirm

Fourteen items remain open across this module's two documents, one fewer than before this rewrite — C2 (online path) and the Service Ownership questions for #1/#2 are now resolved per the answers doc and are not repeated here.

1. Are the five proposed service categories acceptable, or should the source's Development / Transaction / Title-Deed Data grouping be retained? (C1 — proposed answer: adopt them, keep the reconciliation table.)
2. Is the #12–#17 re-derivation to Trustee Centre Operator acceptable, given it contradicts the source's responsible-role column? (A4 — Medium confidence, flagged for the client explicitly.)
3. Do the four Application Management features apply to Group C as they do to individual users? (C3 — proposed answer: yes, unchanged.)
4. Are the five institution-specific features (including the two added by C4 — Settlement Account, Staff & Permission Scopes) correct, and is anything still missing?
5. Is the proposed status vocabulary (platform core + Group C extension, D1) acceptable, and is the specific status list correct?
6. Fee settlement: is the three-way payer-model split (Institution Account Debit / Customer Payment at Counter / Institution Fee Payment) correct for all 18 services, and is it right that finance lease services (#8–#11) sit in the account-debit group on "Fee balance" evidence alone, given their workflow text reads as a counter payment? (B1, flagged in Services #8–#11's Open Questions.)
7. Published fee schedule for the 18 services — the one question of 23 with no proposed answer (B5, client data).
