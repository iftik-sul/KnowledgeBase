---
project: RERAN
module: real-estate-service-companies
type: overview
status: current
updated: 2026-08-16
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - real-estate-service-companies
  - index
---

# Real Estate Service Companies Module

RERAN user Group D — licensed brokerages, jointly-owned-property (JOP) administrators, and property management firms that operate under a single verified company account.

**Scope:** post-login functionality only. Registration and onboarding are out of scope for this project.

**Built from scratch, 2026-08-16, in a single session.** The prior version of this module (roles-and-responsibilities.md, services-overview.md, README.md — three files, no service flows, no UI) was deleted at the client's explicit request, and this module was rebuilt following all six phases of [module-build-playbook.md](../../module-build-playbook.md) in strict dependency order — the first module in the project to do so without a later out-of-order correction.

## Contents

| Section | Count |
| :---- | :---: |
| Roles | 4 |
| Business Services | 26 |
| Shared Platform Features | 8 |
| UI Screens | 12 |

* [roles-and-responsibilities.md](roles-and-responsibilities.md) — Brokerage Principal, Owners'-Association Manager, Property Management Officer, Company Dispute Filing Officer. Unified access from the start (never went through a role-permission-matrix phase, unlike Groups B and C): none of the four roles gates access; each description is customary practice, not restriction.
* [services-overview.md](services-overview.md) — the 26 services, category breakdown, full row-to-service mapping (a clean 1:1 reconciliation, no consolidation or splitting needed), and the 8-feature shared-platform layer.
* [payments.md](payments.md) — three payment models, following the 2026-08-16 normalization of Services #12–15 (`open-questions.md` B4). **19 of the 26 services carry no fee at all** — a materially higher no-fee proportion than any other module in the project.
* [open-questions.md](open-questions.md) — 12 questions, 11 answered with a proposed or confirmed position, 1 genuine client-data exception (exact fee amounts). Two items — A2 (Service #18's module ownership) and B4 (payment normalization) — were put to the client directly and resolved 2026-08-16; both carry a "Files needing a follow-up pass" checklist recording exactly what was propagated where.
* [navigation.md](navigation.md) — sidebar structure, unified-access rules, and the module's own flagged finding that it may have no assisted-mode (Trustee Centre) channel at all — the first module in the project to raise this possibility.
* [role-workflows.md](role-workflows.md) — the shared post-login journey across all four roles.
* [shared-platform-features.md](shared-platform-features.md) — 8 features derived bottom-up from the actual built screens, fewer than Financial & Trust Institutions' 12 or Real Estate Developer's 13 because Group D's own source material lacks the mechanisms (internal certification, Trustee-mediated escrow, recurring compliance reporting) those modules' extra features exist to model.

## Service Flows

26 of 26 service-flow documents are written, at template depth, in [service-flows/](service-flows/):

| # | Service | Category |
| :---: | :---- | :---- |
| 1 | [Register Company for JOP Administrative Supervision](service-flows/service-01-register-company-jop-supervision.md) | Jointly Owned Property |
| 2 | [Approve Service Fees & Utilization Fees](service-flows/service-02-approve-service-utilization-fees.md) | Jointly Owned Property |
| 3 | [Register JOP-Competent Employees](service-flows/service-03-register-jop-competent-employees.md) | Jointly Owned Property |
| 4 | [Register Owners Association](service-flows/service-04-register-owners-association.md) | Jointly Owned Property |
| 5 | [Transfer JOP Escrow Account](service-flows/service-05-transfer-jop-escrow-account.md) | Jointly Owned Property |
| 6 | [Request No-Objection Letter to Close Escrow Account](service-flows/service-06-request-escrow-account-closure.md) | Jointly Owned Property *(email-only channel)* |
| 7 | [Accredit Escrow Account Signatories](service-flows/service-07-accredit-escrow-signatories.md) | Jointly Owned Property *(Pattern B — repeatable signatory group)* |
| 8 | [Appoint Financial Auditor](service-flows/service-08-appoint-financial-auditor.md) | Jointly Owned Property |
| 9 | [Appoint Audit Office for JOP Financial Accounts](service-flows/service-09-appoint-audit-office-financial-accounts.md) | Jointly Owned Property |
| 10 | [Appoint Audit Office for JOP Budget Audit](service-flows/service-10-appoint-audit-office-budget-audit.md) | Jointly Owned Property |
| 11 | [Approval / Renewal of Financial Auditing Company](service-flows/service-11-approval-renewal-financial-auditing-company.md) | Jointly Owned Property *(channel inconsistency flagged — see Known Source Gaps)* |
| 12 | [Real Estate Licensing Application](service-flows/service-12-real-estate-licensing-application.md) | Real Estate Licensing *(payment normalized 2026-08-16 — now pays upfront, before lodging)* |
| 13 | [Real Estate Permit Application](service-flows/service-13-real-estate-permit-application.md) | Real Estate Licensing *(payment normalized 2026-08-16)* |
| 14 | [Issue Professional Practice Card](service-flows/service-14-issue-professional-practice-card.md) | Real Estate Licensing *(payment normalized 2026-08-16)* |
| 15 | [Renew Professional Practice Card](service-flows/service-15-renew-professional-practice-card.md) | Real Estate Licensing *(payment normalized 2026-08-16; automatic approval)* |
| 16 | [Cancel Professional Practice Card](service-flows/service-16-cancel-professional-practice-card.md) | Real Estate Licensing |
| 17 | [Amend Professional Practice Card](service-flows/service-17-amend-professional-practice-card.md) | Real Estate Licensing *(Pattern C — conditional field selector; automatic approval)* |
| 18 | [Register Real Estate Evaluation Details Certificate](service-flows/service-18-register-evaluation-details-certificate.md) | Real Estate Licensing *(module ownership confirmed 2026-08-16; own atypical shape still has no designed screen — see Known Source Gaps)* |
| 19 | [Accreditation of Training Entities](service-flows/service-19-accreditation-training-entities.md) | Real Estate Licensing *(email-only channel)* |
| 20 | [Register/Renew Management Contract](service-flows/service-20-register-renew-management-contract.md) | Real Estate Rental |
| 21 | [Cancel Management Contract](service-flows/service-21-cancel-management-contract.md) | Real Estate Rental |
| 22 | [Register Tenancy System User](service-flows/service-22-register-tenancy-system-user.md) | Real Estate Rental |
| 23 | [Permit to Sell by Public Auction](service-flows/service-23-permit-sell-by-public-auction.md) | Real Estate Transaction |
| 24 | [Register Property Sold by Auction](service-flows/service-24-register-property-sold-by-auction.md) | Real Estate Transaction |
| 25 | [Primary Suit (Joint Property)](service-flows/service-25-primary-suit-joint-property.md) | Real Estate Dispute |
| 26 | [Execution Case (Joint Ownership)](service-flows/service-26-execution-case-joint-ownership.md) | Real Estate Dispute |

All 26 carry `status: draft` and `contains_proposals: true`. This module reconciles cleanly against source: 26 rows (46–71), no consolidation, no splitting — the cleanest reconciliation of any module in the project.

## UI Specifications

12 screens under [ui/screens/](ui/screens/): Dashboard, Services Catalog, Service Details, Submit Application, Application Review, Applications, Application Details, Jointly Owned Property (a dedicated register, matching Financial & Trust Institutions' Trust Accounts precedent), Documents, Notifications, Company Profile, and Help & Support.

Plus three shared reference documents: [ui/components.md](ui/components.md), [ui/validation-rules.md](ui/validation-rules.md), and [ui/status-badges.md](ui/status-badges.md) — all derived from what the 12 screens actually contain, not templated in advance.

**Field-layout patterns, checked service-by-service rather than assumed:** 21 of 25 wizard-eligible services use Pattern A (flat fields) — the highest single-pattern concentration of any module — with one Pattern B (Service #7) and one Pattern C (Service #17) exception. Two services (#6, #19) are email-only with no wizard at all — the highest email-only count of any module.

**Service #18 has no designed screen.** Its module ownership is confirmed (`open-questions.md` A2), but its own sourced workflow — an evaluation company deciding on a customer's request, not RERA reviewing a company's filing — doesn't fit the shared Submit Application wizard every other service uses. It's listed in the catalogue with a placeholder, per `ui/screens/services-catalog.md`'s own Notes.

## Payment Models

**Corrected 2026-08-16, by client decision (`open-questions.md` B4).** Three models, not four:

* **No fee** — 19 services (#1–11, #16, #17, #20–23).
* **Upfront gateway payment, before lodging** — 4 services (#12–15), normalized from their originally-sourced post-decision timing.
* **Pay-then-output** (#24) and **channel-dependent, possibly two-stage** (#25, #26) — the two remaining, genuinely distinct timing shapes.

No Group D service is ever approved while payment is still pending — the same uniform state Financial & Trust Institutions reached the same day, for a structurally comparable reason (both modules had a small cluster of services normalized away from post-decision payment on 2026-08-16).

## Cross-Module Findings

* **JOP's escrow-adjacent services (#5–#10) do not share Group B/C's Trustee-mediated escrow mechanism**, despite the "escrow account" terminology in several service names — checked directly against source (`open-questions.md` A3): every JOP service routes directly from company to RERA's Compliance & Escrow Auditor, with no Account Trustee intermediary sourced anywhere. Do not cross-link these services to `financial-trust-institutions/ui/screens/escrow-request-queue.md`.
* **Group D may have no Trustee Centre / assisted-mode channel at all** — none of its 26 sourced rows name one, unlike Financial & Trust Institutions or Individual User, both of which have several. Flagged in `navigation.md`, not yet confirmed with the client.
* **Service #19 (Accreditation of Training Entities) is near-identical to Real Estate Developer's own Service #23** — same five-step email process, same SLA, same output. Treated as a genuinely distinct accreditation track (Group D vs. Group B), not a source duplication, but flagged for client confirmation.

## Proposed Content

This module contains proposed content marked with `contains_proposals: true` in frontmatter and inline `> **Proposed**` blocks. Most Group D service-flow files mark their entire Required Documents section as Proposed — the source table rarely itemizes documents beyond "attach documents," a materially higher proportion of under-specification than Financial & Trust Institutions or Real Estate Developer.

Remaining open items are listed in each document's own Open Questions / To Confirm section:

* [open-questions.md](open-questions.md#summary) — 1 item genuinely still open (A4, row 60's permit-bundling treatment), lower priority, reversible if wrong.
* [payments.md](payments.md#to-confirm--summary) — exact fee amounts, client data, the one item every module's payments analysis has had exactly one of.
* Each of the 26 service-flow documents — its own Open Questions section.
* [shared-platform-features.md](shared-platform-features.md#open-questions) — whether Service #18 needs its own dedicated feature once its screen is eventually designed.

## Known Source Gaps

* **Service #18's own workflow doesn't fit any other Group D service's shape.** Its acting party (an "evaluation company") accepts or rejects a customer's request directly, with no RERA review step described — the clearest structural anomaly in the module, and the reason it has no designed screen despite confirmed module ownership.
* **Service #11's Section 12 workflow contradicts its own sourced email-only channel** (row 56 names only "Official email of the Jointly Owned Property," but the file's workflow text still describes portal-style sign-up) — found during the Phase 6 audit, 2026-08-16, not yet corrected. See that file's own Open Questions.
* **Row 65 (Service #18) and Row 60 (Service #13) both carry genuine ambiguity** the source table doesn't resolve: whether row 65 belongs to Group D or Group G (resolved by client decision to stay in Group D, `open-questions.md` A2), and whether row 60's four advertisement permit types are one service or several (proposed as one, `open-questions.md` A4, not yet put to the client).
* **Whether Service #12 covers renewal at all** is unresolved — unlike Financial & Trust Institutions' comparably-shaped Service #1, row 59's own source text describes only a first-time application shape. Flagged in `ui/screens/company-profile.md`.
* **This module's build history is unusually compressed** — every phase, plus a full Phase 6 audit correcting 21 files' stale Section 17 references, happened in a single session on 2026-08-16. Treat any cross-reference to "the module as originally built" with the understanding that the entire module was built and audited the same day; there is no earlier, differently-shaped version to reconcile against the way other modules occasionally need to.
