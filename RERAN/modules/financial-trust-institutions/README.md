---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - financial-trust-institutions
  - index
---

# Financial & Trust Institutions Module

RERAN user Group C — banks, mortgage institutions, account trustees and auditing bureaux that finance, secure and audit real-estate transactions.

**Scope:** post-login functionality only. Registration and onboarding are out of scope for this project.

## Contents

| Section | Count |
| :---- | :---: |
| Roles | 4 |
| Business Services | 18 |
| Shared Platform Features | 17 |

* [roles-and-responsibilities.md](roles-and-responsibilities.md) — Mortgage Officer, Institution Relationship Manager, Account Trustee, Auditing Bureau Officer. All four are attribution-only (2026-08-14 client decision): none gates access, and none owns a specific service (`open-questions.md` A4, 2026-08-15).
* [services-overview.md](services-overview.md) — the 18 services, category breakdown, status vocabulary, and channels.
* [payments.md](payments.md) — the three payer/timing models, payment artefacts, and the 2026-08-14 correction to a pay-upfront, no-standing-account model for the mortgage and finance-lease lifecycle. *(Corrected 2026-08-14 — previously "the three payer models, settlement account, and payment artefacts"; there is no standing account any more, see `open-questions.md` B1.)*
* [open-questions.md](open-questions.md) — **all 23 questions raised while documenting this module are now confirmed or resolved; 0 need client data.** *(Corrected 2026-08-15 — previously "22 of 23... 1 (the fee schedule) is client data"; B5 was resolved 2026-08-14, and A4/A6, the two items that had been put directly in front of the client, were confirmed 2026-08-15. Nothing remains on that list — see `open-questions.md`'s own Summary.)*

## Service Flows

18 of 18 service-flow documents are written, at template depth, in [service-flows/](service-flows/):

| # | Service | Category |
| :---: | :---- | :---- |
| 1 | [Approval / Renewal of Account Trustee & Auditing Company](service-flows/service-01-approval-renewal-account-trustee-auditing-company.md) | Institutional Approval |
| 2 | [Cancellation of Account Trustee & Auditing Company](service-flows/service-02-cancellation-account-trustee-auditing-company.md) | Institutional Approval |
| 3 | [Mortgage Registration](service-flows/service-03-mortgage-registration.md) | Mortgage |
| 4 | [Mortgage Amendment](service-flows/service-04-mortgage-amendment.md) | Mortgage |
| 5 | [Mortgage Transfer](service-flows/service-05-mortgage-transfer.md) | Mortgage |
| 6 | [Mortgage Release](service-flows/service-06-mortgage-release.md) | Mortgage |
| 7 | [Grant Property Mortgage](service-flows/service-07-grant-property-mortgage.md) | Mortgage |
| 8 | [Finance Lease Registration](service-flows/service-08-finance-lease-registration.md) | Finance Lease |
| 9 | [Finance Lease Amendment](service-flows/service-09-finance-lease-amendment.md) | Finance Lease |
| 10 | [Finance Lease Transfer](service-flows/service-10-finance-lease-transfer.md) | Finance Lease |
| 11 | [Finance Lease Release](service-flows/service-11-finance-lease-release.md) | Finance Lease |
| 12 | [Registration of Real Estate Fund Companies](service-flows/service-12-register-real-estate-fund-company.md) | Title & Ownership |
| 13 | [Sale Procedure (Heirs)](service-flows/service-13-sale-procedure-heirs.md) | Title & Ownership |
| 14 | [Company Shares Sale](service-flows/service-14-company-shares-sale.md) | Title & Ownership |
| 15 | [Updating Title Deed Information](service-flows/service-15-update-title-deed-information.md) | Title & Ownership |
| 16 | [Split Ownership](service-flows/service-16-split-ownership.md) | Title & Ownership |
| 17 | [Issuance of Title Deed](service-flows/service-17-issue-title-deed.md) | Title & Ownership |
| 18 | [Contract Cancellation](service-flows/service-18-contract-cancellation.md) | Contract |

All 18 carry `status: draft` and `contains_proposals: true` — each has genuinely sourced sections (workflow, channel, output, SLA, all traceable to `RERAN_service_flows_v2.md` rows 28–45) alongside proposed sections (required documents, and per-service business-rule inferences) marked inline. See each file's Open Questions section for what remains genuinely unresolved.

## UI Specifications

> Not yet written. Follows the service flows, per the project's derivation chain.

## The Defining Pattern: Two Gates

**Corrected 2026-08-15 — this section previously opened with an unconditional claim that contradicted its own second sentence.** It read "Every Group C action passes through an internal certification gate... No Group C role completes a regulated action unilaterally," then immediately qualified that the gate is sourced only for part of the module. The two statements can't both be true as written; the qualified version below is the accurate one.

The internal certification gate is sourced for the mortgage and finance-lease lifecycle (Services #3–#11): every one of those actions passes through internal certification inside the institution, then external audit at RERA. Services #1, #2, and #12–#18 do not carry the same gate in their Application Status Flow — no internal institutional certification step is described in source for those rows, so those services go straight to RERA audit. The two-gate pattern is the module's working design intent for services where the institution enables it, not a sourced fact for all eighteen — see [roles-and-responsibilities.md](roles-and-responsibilities.md#how-they-work-together) for the fuller statement of this.

Where the gate does apply, it is an unrestricted action, not a scope or a fifth role: any of the institution's four Group C users may certify or return a filing, including the person who filed it, with the acting user and their role recorded in the audit trail. **Corrected 2026-08-14** — earlier versions of this document modelled certification as a "maker-checker permission scope" on the corporate account (A1/D2); permission scopes are retired module-wide per the client's unified-access decision. See [navigation.md#audit-trail-principle](navigation.md#audit-trail-principle) for the current model.

## Platform Sub-systems

The source names three for this group:

* Online Mortgage System
* Trust-Account Approval & Renewal
* Transaction Audit Queue

## Proposed Content

This module contains proposed content marked with `contains_proposals: true` in frontmatter and inline `> **Proposed**` blocks. The source material is incomplete for this group — in particular, two of the four roles have no documented post-login behaviour at all.

**All 23 questions raised while documenting this module are now confirmed or resolved** in [open-questions.md](open-questions.md); those positions have been applied throughout the service flows, `services-overview.md`, and `payments.md`. *(Corrected 2026-08-15 — previously "22 of 23... now carry a proposed working position"; see the Contents section above for what changed.)* Remaining open items — proposals not yet put to the client, as distinct from the closed question set above — are listed in each document's own To Confirm / Open Questions section:

* [roles-and-responsibilities.md](roles-and-responsibilities.md#to-confirm--summary) — 7 items listed, 4 genuinely still open as of 2026-08-15 (3 are resolved and kept for the record)
* [services-overview.md](services-overview.md#to-confirm) — 5 items *(corrected 2026-08-15 — previously 7; the A4 and B5 items were resolved and removed, not repeated)*
* [payments.md](payments.md#to-confirm--summary) — 6 items *(not re-verified as part of this correction — flagged, not fixed, if stale)*
* Each of the 18 service-flow documents — its own Open Questions section, where something survived the answers doc genuinely unresolved

When an item is confirmed, remove its `> **Proposed**` block and bump `updated`. When every proposal in a file is resolved, remove `contains_proposals` from its frontmatter.

## Known Source Gaps

* **Account Trustee and Auditing Bureau Officer own no numbered services.** Both have substantial described functions but appear in the service table only as participants in Group B's escrow workflow. Their Group C interface is reconstructed, not sourced.
* **The "bank's internal auditor" in the mortgage workflow is modelled as a checker permission scope, not the Auditing Bureau Officer** (A1) — the Auditing Bureau Officer is an approved external firm auditing developer escrow, a different actor with different properties.
* **The status vocabulary is now platform-wide core plus a Group C extension** (D1), rather than undefined for every user group.
* **No service in Group C is role-specific, for any of the 18 services** (A4, confirmed 2026-08-15, client decision). *(Corrected 2026-08-15 — this bullet previously read "Services #1 and #2's role-assignment inconsistency is resolved — both now sit with the Institution Relationship Manager," which was the answer's superseded re-derivation, not the current one. The client has since confirmed Group C does not assign services to roles at all; that superseded position is kept in `open-questions.md` A4 for the record but is no longer accurate as a statement of the current model.)*
* **Row 38 (Service #12) and row 39 (Service #7) are transposed against file order** in the source workbook; the service flows follow the row-to-file mapping, not row sequence.
* **Row 39 (Grant Property Mortgage) names "Payment receipts" as output**, which this document previously flagged as the one exception against every other mortgage row's "Fee balance" wording. **Corrected 2026-08-14** — under the corrected payment model (`open-questions.md` B1, B9), there is no standing account and no "fee balance" artefact for any Group C service; row 39's "Payment receipts" is the terminology every mortgage-service row now follows, not an anomaly. See [payments.md](payments.md).
