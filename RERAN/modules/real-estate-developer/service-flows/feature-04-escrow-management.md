---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/escrow-management.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - shared-feature
  - domain-workspace
  - escrow
---

# Feature #4 – Escrow Management

**Feature Category:** Shared Platform Features – Domain Workspace

## 1. Feature Overview

**Escrow Management** is the domain workspace for the developer's project escrow accounts — the regulated holding accounts for sale proceeds, deposits, and construction-milestone releases. Registering an account, monitoring its balance and milestone progress, and initiating fund-release requests (which continue into the separate Fund Release Request feature) all happen here.

**Important distinction, stated explicitly in the source screen itself:** the balances shown here are the project escrow account's own balances — entirely separate from how RERA's service fees are paid (per-transaction, via the shared platform gateway, since 2026-08-15). A balance or debit on this screen is escrow, not fees.

> **Cross-module status vocabulary — resolved 2026-08-16.** This feature's own Fund Release Status vocabulary — `No Request → Pending Approval → Under Review → Approved → Released` — is now the canonical cross-module vocabulary for all six developer escrow request types (Services #8/9/10/12/20/21), adopted by client decision. Financial & Trust Institutions' [Escrow Request Queue](../../financial-trust-institutions/service-flows/feature-04-escrow-request-queue.md) is updated to use these same terms — `Awaiting Assessment`/`Under Assessment` renamed to `Pending Approval`/`Under Review`, and `Under Review` now explicitly spans both the institution's own assessment and RERA's subsequent audit, closing the gap where that feature previously had no status for RERA's post-certification review. Fund Release Request (Feature #5)'s more granular 9-stage tracker maps onto this vocabulary rather than replacing it — see that feature's own Section 13.

## 2. Purpose

List the organization's project escrow accounts and provide both the oversight view of escrow position and compliance, and the operational controls to register accounts, request fund releases, and coordinate with the Account Trustee.

## 3. Description

Merged from two prior variants — an oversight screen and an operational workspace — that were asymmetric rather than parallel: the oversight variant had rich summary cards, a Fund Release Overview, and Escrow Analytics but almost no filtering; the operational variant had rich search/filter/sort and five row actions but no summary cards or analytics. The merge is mostly additive. Two separate status vocabularies apply — Escrow Status and Fund Release Status — kept distinct rather than conflated, the same pattern as Sales & Disclosures' two-lifecycle design.

## 4. Used By

Services #8–#9, #20–#21, confirmed via service-08's `derived_from`:

* Escrow Account Activation
* Escrow Account Transfer
* Depositing a Mortgage into an Escrow Account
* Bank Guarantee Cancellation

The module's README flags cardinality mismatches for #9, #20, #21 against this screen — the mapping is directionally right but not field-exact; consult each service's own file for specifics.

**Distinct from Fund Release Request (Feature #5)**, which covers Services #10 and #12 — milestone-based withdrawal and receipt, reached from this screen's Escrow Details but tracked as a separate object, now mapped onto the same canonical status vocabulary as this feature.

## 5. Prerequisites

* User is logged into a registered developer company account.
* The relevant project is already registered (Feature #2).

## 6. Required Information

Varies by selected service — see each service's own Section 6. Search/filter on this screen: Escrow ID, project name, project registration number, financial institution, account number, escrow status, fund release status.

## 7. Required Documents

Varies by service — see each service's own Section 7.

## 8. Service Fee

Set by the selected service (RERA fee, per transaction, via the shared platform gateway) — not to be confused with the escrow account's own balance, which is not a fee at all.

## 9. Payment Required

**Depends on the selected service.** Service #8 (Escrow Account Activation) is confirmed to carry **no RERA fee at all** — checked directly during the earlier planning phase of this rebuild. Do not assume uniformity across #8–#9, #20–#21; consult each service's own Section 9.

## 10. Processing Authority

**Compliance & Escrow Auditor**, with cross-module coordination to Financial & Trust Institutions' Account Trustee for the escrow account's own management (see Related Features).

## 11. Expected Processing Time

Set by the selected service — see its own Section 11.

## 12. Processing Workflow

Dashboard
↓
Open Escrow Management
↓
Register Escrow Account *(or select an existing account)*
↓
Complete Service-Specific Form (activation / transfer / mortgage deposit / bank guarantee cancellation)
↓
Upload Required Documents
↓
Submit
↓
RERA Reviews, Coordinating with Account Trustee Where Applicable
↓
Escrow Account Status Updated

## 13. Application Status Flow

**Escrow Status:** Pending Registration → Active → Suspended → Closed

**Fund Release Status** *(tracked separately, surfaced here but acted on via Feature #5)* — **the canonical cross-module vocabulary as of 2026-08-16**: No Request → Pending Approval → Under Review → Approved → Released, or → Returned / Rejected

These two vocabularies are never conflated in filters, badges, or counts.

**Cross-module reconciliation, resolved 2026-08-16**: financial-trust-institutions' Escrow Request Queue now uses this same vocabulary for its assessment phase, with `Under Review` spanning both the institution's assessment and RERA's subsequent audit — see that feature's own Section 13.

## 14. Possible Outcomes

* Escrow Account Activated / Transferred
* Mortgage Deposited into Escrow
* Bank Guarantee Cancelled
* Account Suspended / Closed

## 15. Output

Varies by service — typically an account registration or transfer confirmation. See each service's own Section 15.

## 16. Related Features

* Fund Release Request *(Feature #5 — the milestone-based withdrawal/receipt flow reached from Escrow Details, Services #10/#12, mapped onto this feature's status vocabulary)*
* Applications *(Feature #1)*
* Financial & Trust Institutions' Escrow Request Queue and Trust Accounts *(cross-module — the Account Trustee's side of the same accounts; **status vocabulary reconciled 2026-08-16**, see Feature Overview)*

## 17. UI Screens

* Escrow Management
* Escrow Details

## 18. API Requirements

* Retrieve Organization Escrow Accounts / Search / Filter
* Retrieve Escrow Details, Fund Release Overview, Escrow Analytics
* Submit Escrow Registration / Transfer / Deposit / Cancellation (per selected service)
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Developer Company, Project, User
* Escrow Account, Escrow Status, Fund Release *(cross-referenced with Feature #5)*
* Financial Institution
* Document, Application
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can view, register, and act on any escrow account.
* Escrow Status and Fund Release Status are never conflated in filters, badges, or counts.
* Balances shown are always the escrow account's own, never a RERA-fee figure.
* Row actions are governed by the account's own state, never by who is viewing.
* All escrow activity is recorded in the audit log, including the acting user's role.
* Fund Release Status uses the same terms as financial-trust-institutions' Escrow Request Queue for the same transaction types.

## 21. Business Rules

1. Any of the developer's four Group B roles may register or act on any escrow account — no per-user assignment scoping.
2. Escrow Status and Fund Release Status are separate values with separate lifecycles.
3. Balances on this screen are the project escrow account's own — never conflated with RERA service-fee payment, which moved to per-transaction gateway payment on 2026-08-15 and is unrelated.
4. Row actions depend on the account's own state — a closed account takes no new release request, regardless of who asks.
5. All escrow activity is permanently recorded in the audit trail, including the acting user's role.
6. Fund Release Status (`No Request → Pending Approval → Under Review → Approved → Released`, or `Returned`/`Rejected`) is the canonical cross-module vocabulary for Services #8/9/10/12/20/21, adopted 2026-08-16 — any future screen or document describing these transactions should use these terms.

## Open Questions

1. Whether "Escrow Balance" should mean gross balance or balance net of committed pending releases is flagged but unresolved — the source screen glosses both the same way; if the client intends the net reading, a second column would be needed.
2. Cardinality mismatches for Services #9, #20, #21 against this screen are flagged in the module README but not resolved here — consult each service's own file.
3. Same adoption question as Feature #1 — needs client confirmation.
