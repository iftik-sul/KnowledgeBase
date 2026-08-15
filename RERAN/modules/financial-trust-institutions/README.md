---
project: RERAN
module: financial-trust-institutions
type: overview
status: current
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
| UI Screens | 18 *(13 in `ui/screens/`, 5 in `ui/screens-unified/`)* |

* [roles-and-responsibilities.md](roles-and-responsibilities.md) — Mortgage Officer, Institution Relationship Manager, Account Trustee, Auditing Bureau Officer. All four are attribution-only (2026-08-14 client decision): none gates access, and none owns a specific service (`open-questions.md` A4, 2026-08-15).
* [services-overview.md](services-overview.md) — the 18 services, category breakdown, status vocabulary, and channels.
* [payments.md](payments.md) — the two payer/timing models, payment artefacts, and the corrected pay-upfront, no-standing-account model. *(Corrected 2026-08-15 — previously "three payer/timing models"; B11 folded Service #1 into the upfront model and confirmed Service #2 carries no fee, leaving two models, not three. See `open-questions.md` B11.)*
* [open-questions.md](open-questions.md) — **all 24 questions raised while documenting this module are now confirmed or resolved; 0 need client data.** *(Corrected 2026-08-15 — previously "23 questions... all confirmed or resolved"; B11 was added 2026-08-15 as a genuinely new client decision on Service #1/#2 payment timing, bringing the total to 24. See `open-questions.md`'s own Summary.)*
* [ui/README.md](ui/README.md) — the UI specification package: 18 screens, shared components, validation rules, and status vocabularies. *(Added 2026-08-15 — this bullet previously didn't exist; see "UI Specifications" below for what changed.)*

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

**Written, not pending.** *(Corrected 2026-08-15 — this section previously read "Not yet written. Follows the service flows, per the project's derivation chain," which was accurate when this file was last touched but has been stale since the UI package was actually built; nobody updated this section as that work landed.)*

Eighteen screens across two locations, described in full in [ui/README.md](ui/README.md):

* **`ui/screens/`** (13 files) — Dashboard, Applications, Application Details, Internal Certification Queue, Escrow Request Queue, Escrow Request Details, Trust Accounts, Compliance Reports, Payment History, Institution Profile, Documents, Notifications, and the Group G-operated Assisted Service Terminal.
* **`ui/screens-unified/`** (5 files) — Services Catalog, Service Details, Submit Application (the module's one canonical eighteen-service form, replacing the retired `service-request.md`), Application Review, and this folder's own README documenting how it maps against `ui/screens/`.

Plus three shared reference documents: [ui/components.md](ui/components.md) (component library), [ui/validation-rules.md](ui/validation-rules.md) (validation patterns), and [ui/status-badges.md](ui/status-badges.md) (status vocabularies).

Both the unified-access model and the corrected payment model have been reconciled across the entire UI package — see [ui/README.md](ui/README.md)'s own correction notes for the full history, and issue #50 for how the retire-vs-rewrite questions (Dashboard, Submit Application) were resolved.

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

**All 24 questions raised while documenting this module are now confirmed or resolved** in [open-questions.md](open-questions.md); those positions have been applied throughout the service flows, `services-overview.md`, `payments.md`, and the UI package. *(Corrected 2026-08-15 — previously "23 questions... now confirmed"; B11 added, see the Contents section above.)* Remaining open items — proposals not yet put to the client, as distinct from the closed question set above — are listed in each document's own To Confirm / Open Questions section:

* [roles-and-responsibilities.md](roles-and-responsibilities.md#to-confirm--summary) — 1 item genuinely still open as of 2026-08-15 (6 are resolved and kept for the record). *(Corrected 2026-08-15 — previously "4 genuinely still open"; the Dashboard rework (issue #50) resolved item 7, leaving only item 6 open.)*
* [services-overview.md](services-overview.md#to-confirm) — 5 items.
* [payments.md](payments.md#to-confirm--summary) — 4 items. *(Corrected 2026-08-15 — previously "6 items... not re-verified"; the B11 correction pass did update this section directly, resolving two more and leaving 4. No longer a stale caveat.)*
* Each of the 18 service-flow documents — its own Open Questions section, where something survived the answers doc genuinely unresolved.
* [ui/screens-unified/submit-application.md](ui/screens-unified/submit-application.md#section-3--service-specific-details-dynamic) — the per-service field-layout classification (Pattern A/B/C) for all 18 services, fully resolved as of 2026-08-15; nothing open there either, but worth a direct link since it's a substantial piece of design reasoning that doesn't fit the "To Confirm" framing of the other documents.

When an item is confirmed, remove its `> **Proposed**` block and bump `updated`. When every proposal in a file is resolved, remove `contains_proposals` from its frontmatter.

## Known Source Gaps

* **Account Trustee and Auditing Bureau Officer own no numbered services.** Both have substantial described functions but appear in the service table only as participants in Group B's escrow workflow. Their Group C interface is reconstructed, not sourced.
* **The "bank's internal auditor" in the mortgage workflow is modelled as a checker permission scope, not the Auditing Bureau Officer** (A1) — the Auditing Bureau Officer is an approved external firm auditing developer escrow, a different actor with different properties.
* **The status vocabulary is now platform-wide core plus a Group C extension** (D1), rather than undefined for every user group.
* **No service in Group C is role-specific, for any of the 18 services** (A4, confirmed 2026-08-15, client decision).
* **Row 38 (Service #12) and row 39 (Service #7) are transposed against file order** in the source workbook; the service flows follow the row-to-file mapping, not row sequence.
* **Row 39 (Grant Property Mortgage) names "Payment receipts" as output**, which this document previously flagged as the one exception against every other mortgage row's "Fee balance" wording. Under the corrected payment model (`open-questions.md` B1, B9), there is no standing account and no "fee balance" artefact for any Group C service; row 39's "Payment receipts" is the terminology every service now follows, not an anomaly. See [payments.md](payments.md).
