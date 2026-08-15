---
project: RERAN
module: real-estate-developer
type: overview
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - index
---

# Real Estate Developer Module

Documentation for RERAN user Group B — licensed development companies that register projects and off-plan sales, operate escrow accounts, and file construction progress. The most heavily regulated external group.

The module enables registered real estate development companies to participate in the RERA ecosystem by registering development projects, submitting property registrations, managing property sales disclosures, coordinating escrow activities, and interacting with RERA throughout the development lifecycle. Each registered developer is treated as a single organization; users within the organization are assigned one of four predefined business roles, with the Developer Principal / Director serving as the primary organizational representative.

**Access is not gated by role (confirmed 2026-08-15).** All four roles share identical access to every screen and action in the module. Role is retained only as an audit-trail attribution field — every action records who performed it and what role they held at the time. See [navigation.md](navigation.md).

## Roles (4)

* [roles-and-responsibilities.md](roles-and-responsibilities.md) — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison. Descriptions and typical practice; not access definitions.
* [role-workflows.md](role-workflows.md) — the shared path through the system, plus per-role typical-practice notes.

## Navigation & Access

* [navigation.md](navigation.md) — sidebar structure, unified access rules, and the audit-trail principle.

## Service Flows

27 of 27 service-flow documents are written, at template depth, in [service-flows/](service-flows/) — see [issue #33](https://github.com/iftik-sul/KnowledgeBase/issues/33), closed by PR #36 (merged 2026-08-11), for the full row-to-service-to-screen mapping, mismatch list, and report-back. **This module's derivation chain ran backwards**: the UI (19 screens) existed first with no service flows underneath it; these flows were written second and cross-checked against the existing screens rather than the other way around. Every mismatch found between a screen and its source row is called out inline in the relevant service and listed in the PR description — screens were **not** edited to resolve them.

| # | Service | Category |
| :---: | :---- | :---- |
| 1 | [Register Initial Sale](service-flows/service-01-register-initial-sale.md) | Real Estate Development |
| 2 | [Register Initial Rent-to-Own](service-flows/service-02-register-initial-rent-to-own.md) | Real Estate Development |
| 3 | [Register Initial Usufruct](service-flows/service-03-register-initial-usufruct.md) | Real Estate Development |
| 4 | [Amend Initial Procedures Data](service-flows/service-04-amend-initial-procedures-data.md) | Real Estate Development |
| 5 | [Complete Initial Procedures Data](service-flows/service-05-complete-initial-procedures-data.md) | Real Estate Development |
| 6 | [Register Sale Associated with an Initial Mortgage](service-flows/service-06-register-mortgage-linked-sale.md) | Real Estate Development |
| 7 | [Transfer Registration Fees Between Properties](service-flows/service-07-transfer-registration-fees.md) | Real Estate Development *(no matching UI screen — flagged)* |
| 8 | [Escrow Account Activation](service-flows/service-08-activate-escrow-account.md) | Real Estate Development |
| 9 | [Escrow Account Transfer](service-flows/service-09-transfer-escrow-account.md) | Real Estate Development *(cardinality mismatch — flagged)* |
| 10 | [Project Profit Withdrawal](service-flows/service-10-withdraw-project-profit.md) | Real Estate Development *(UI mismatch — flagged)* |
| 11 | [Amend the Cap of Administrative, Marketing and VAT Expenses](service-flows/service-11-amend-expense-cap.md) | Real Estate Development *(no matching UI screen — flagged)* |
| 12 | [Receive a Payment from the Project's Escrow Account](service-flows/service-12-receive-escrow-payment.md) | Real Estate Development |
| 13 | [Registration of Real Estate Project](service-flows/service-13-register-real-estate-project.md) | Real Estate Development |
| 14 | [Real Estate Project Cancellation](service-flows/service-14-cancel-real-estate-project.md) | Real Estate Development |
| 15 | [Real Estate Project Sub-division](service-flows/service-15-subdivide-real-estate-project.md) | Real Estate Development |
| 16 | [Changing the Name of a Real Estate Project](service-flows/service-16-rename-real-estate-project.md) | Real Estate Development |
| 17 | [Project Re-registration](service-flows/service-17-re-register-real-estate-project.md) | Real Estate Development |
| 18 | [Settlements Application](service-flows/service-18-settlements-application.md) | Real Estate Development *(UI framing mismatch — flagged)* |
| 19 | [Request Termination of Initial Registration](service-flows/service-19-terminate-initial-registration.md) | Real Estate Development |
| 20 | [Depositing a Mortgage into an Escrow Account](service-flows/service-20-deposit-mortgage-into-escrow.md) | Real Estate Development *(cardinality mismatch — flagged)* |
| 21 | [Bank Guarantee Cancellation](service-flows/service-21-cancel-bank-guarantee.md) | Real Estate Development *(cardinality mismatch — flagged)* |
| 22 | [Real Estate Licensing Application](service-flows/service-22-real-estate-licensing-application.md) | Real Estate Licensing *(no matching UI screen — flagged)* |
| 23 | [Accreditation of Training Entities](service-flows/service-23-accredit-training-entities.md) | Real Estate Licensing *(email-only; no UI screen — flagged)* |
| 24 | [Registration/Amendment of Real Estate Project Details](service-flows/service-24-register-amend-project-details.md) | Title Deed Data *(ambiguous screen + near-duplicate — flagged)* |
| 25 | [Issuing Map Application](service-flows/service-25-issue-map.md) | Title Deed Data *(ambiguous screen — flagged)* |
| 26 | [Separation or Annexing a Property](service-flows/service-26-separate-or-annex-property.md) | Title Deed Data |
| 27 | [Requesting a Technical Report for the Project](service-flows/service-27-request-technical-report.md) | Title Deed Data *(UI mismatch — flagged)* |

All 27 carry `status: draft` and `contains_proposals: true` — each has genuinely sourced sections (workflow, channel, output, SLA, all traceable to `RERAN_service_flows_v2.md` rows 1–27) alongside proposed sections (required documents, in particular — the source never itemizes these for Group B any more than it did for Group C) marked inline. Escrow services (#8–#12, #20–#21) cross-link to Financial & Trust Institutions' `escrow-request-queue.md` and `escrow-request-details.md` — the Account Trustee's side of the same transaction.

## UI Specifications

* [ui/README.md](ui/README.md) — screen index (19 distinct screens), all reachable by all four roles.

## Open Questions

* **Resolved 2026-08-15 by the unified-access decision.** This previously read as a role-permission mismatch: the Role Permission Matrix granted the Sales & Disclosure Officer full access to Documents, but no Documents *list* screen existed for that role in [ui/screens/documents.md](ui/screens/documents.md) — only Document Details — while every other role with Document Details also had a list. It was held open as a client question because resolving it would have meant silently editing the permission matrix.

  That is no longer the case: the matrix is retired, and Documents is fully accessible to all four roles. The misplaced source fragment (found at the wrong heading level inside that role's Application Details section, source lines 9218–9475) has now been **checked against `documents.md` and merged in**, because it carries content the screen did not otherwise have — a **Buyer Filter** and **Disclosure Filter**, a sales-specific document category set (Sales Agreements, Buyer Identification, Proof of Payment, Mortgage Documents, Corporate Buyer Documents, Power of Attorney, Disclosure Forms), a `Sale / Disclosure / Buyer` value for the table's Linked Record column, and its own empty state. Dropping it would have lost real sales-disclosure detail. With access unified, including it is a merge rather than a matrix correction, so it no longer needs a client decision.
* **Resolved** — service flows now exist in [service-flows/](service-flows/), written against the already-existing UI per issue #33. Every UI file's `derived_from` still points at `reference/source-of-truth/RERAN_service_flows_v2.md` and `RERAN_user_group_structure_v2.md` rather than the new service-flow documents; updating those pointers was out of scope for issue #33, which was service-flows only and explicitly did not touch `ui/`. Left as a follow-up.

## Known Gap from Source Retirement

The original combined UI document (`ui-design/RERAN_real_estate_developer_ui.md`) has been migrated into this module's structured files and deleted. One piece of its content was never migrated and has since been restored from git history; one piece was correctly left out as genuine duplication:

* **Restored:** a per-role reporting responsibility ("Generate registration/sales/escrow reports" for the three operational roles; "Review organizational reports" and "Monitor company performance" for the Principal) was present in a second, shorter Roles & Responsibilities section in the source but absent from every role's Main Responsibilities in [roles-and-responsibilities.md](roles-and-responsibilities.md). Added back above. The module overview paragraph from the same source section is now included at the top of this file.
* **Correctly left out:** that same shorter section's per-role "Purpose" paragraphs restated the existing "Who are they?" text, and its Organization Structure tree duplicates the one already in [navigation.md](navigation.md).

The misplaced Sales & Disclosure Officer Documents-screen fragment (see Open Questions above) has since been merged into [ui/screens/documents.md](ui/screens/documents.md) and is no longer an open item.
