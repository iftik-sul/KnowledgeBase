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
  - "RERAN/modules/real-estate-developer/service-flows/service-08-activate-escrow-account.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-09-transfer-escrow-account.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-20-deposit-mortgage-into-escrow.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-21-cancel-bank-guarantee.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
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

> **Cross-module status vocabulary — corrected 2026-08-16, superseding an earlier same-day resolution.** A first pass adopted `No Request → Pending Approval → Under Review → Approved → Released` as canonical, taken from this screen's own UI filter values. That was wrong: it was never checked against the six individual service files (#8, #9, #10, #12, #20, #21), all of which were written independently in an earlier PR and all of which — verified directly, all six — use `Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → [service-specific terminal state]`, with additional statuses `Information Requested / Returned / Rejected`. That vocabulary traces to the master source table; the one adopted in the first pass traced only to a UI screen's filter dropdown, one layer removed from source. **The sourced vocabulary is now canonical**, replacing the incorrect first resolution. See Section 13.

> **Terminology clarified 2026-08-16.** "RERA Escrow Audit" / "Escrow Account Department" and financial-trust-institutions' "Compliance & Escrow Auditor" name the **same regulatory role**, not two different offices. Confirmed directly against `RERAN_service_flows_v2.md`'s master Service Workflows table: rows 8–12, 20–21 (this module's six escrow services) and rows 30–39 (financial-trust-institutions' mortgage/lease services) all carry the identical value **"Compliance & Escrow Auditor"** in the Regulator / Approver column — the same single Group A role defined once in the Groups & Roles table (*"Compliance Directorate — Audits escrow/trust accounts, vets off-plan sales, monitors disclosure, sanctions defaulters"*). "Escrow account department audits by approval or rejection," which this module's own service files' narrative workflow text uses, is the source table's own Workflow-column phrasing for that same role's action — not a second, distinct department. Both phrasings are individually accurate to source; they were just never cross-linked before. Not renamed here, since both trace to source — but readers should treat "RERA Escrow Audit," "Escrow Account Department," and "Compliance & Escrow Auditor" as synonyms throughout this module and financial-trust-institutions alike.

## 2. Purpose

List the organization's project escrow accounts and provide both the oversight view of escrow position and compliance, and the operational controls to register accounts, request fund releases, and coordinate with the Account Trustee.

## 3. Description

Merged from two prior variants — an oversight screen and an operational workspace — that were asymmetric rather than parallel: the oversight variant had rich summary cards, a Fund Release Overview, and Escrow Analytics but almost no filtering; the operational variant had rich search/filter/sort and five row actions but no summary cards or analytics. The merge is mostly additive. The screen's own UI carries a "Fund Release Status" filter with values (`No Request / Pending Approval / Under Review / Approved / Released / Returned / Rejected`) that turned out not to match any of the six sourced service files — retained here as a UI-layer filter set, but no longer treated as the authoritative status vocabulary. See Section 13.

## 4. Used By

Services #8–#9, #20–#21, confirmed via service-08's `derived_from`:

* Escrow Account Activation
* Escrow Account Transfer
* Depositing a Mortgage into an Escrow Account
* Bank Guarantee Cancellation

The module's README flags cardinality mismatches for #9, #20, #21 against this screen — the mapping is directionally right but not field-exact; consult each service's own file for specifics.

**Distinct from Fund Release Request (Feature #5)**, which covers Services #10 and #12 — milestone-based withdrawal and receipt, reached from this screen's Escrow Details but tracked as a separate object, now using the same sourced status vocabulary as this feature.

## 5. Prerequisites

* User is logged into a registered developer company account.
* The relevant project is already registered (Feature #2).

## 6. Required Information

Varies by selected service — see each service's own Section 6. Search/filter on this screen: Escrow ID, project name, project registration number, financial institution, account number, escrow status, fund release status.

## 7. Required Documents

Varies by service — see each service's own Section 7.

## 8. Service Fee

Set by the selected service (RERA fee, per transaction, via the shared platform gateway) — not to be confused with the escrow account's own balance, which is not a fee at all. All six services checked directly (#8, #9, #10, #12, #20, #21) carry **no RERA service fee at all** — the source workflow for every one of them runs from submission through Trustee assessment to RERA's audit with no payment step anywhere.

## 9. Payment Required

**No, for any of the six services** — confirmed directly against all six individual service files, not just Service #8 as previously stated. None sources a payment step at any point in its workflow.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module) first, escalating to **RERA's Escrow Account Department** for final audit — a fixed two-stage chain, sourced identically across all six services. This second-stage authority is the **Compliance & Escrow Auditor** (Group A) — the identical role and Regulator/Approver-column value used across financial-trust-institutions' mortgage/lease services (rows 30–39) — not a separate department, see the terminology note under Feature Overview.

## 11. Expected Processing Time

Set by the selected service, as a waiting-time/service-delivery pair (e.g. Service #8: 20/13 business hours; Service #9: 24/45 working hours; Service #20: 26/32 working hours; Service #21: 26/32 business hours) — see each service's own Section 11. Not uniform across the four services this feature covers.

## 12. Processing Workflow

Dashboard
↓
Open Escrow Management
↓
Register Escrow Account *(or select an existing account)*
↓
Complete Service-Specific Form (activation / transfer / mortgage deposit / bank guarantee cancellation)
↓
Submit Application
↓
Account Trustee Reviews, Uploads Assessment
↓
Compliance & Escrow Auditor Audits (Escrow Account Department): Approve or Reject
↓
If Approved, Escrow Account Status Updated (per selected service's terminal state)

## 13. Application Status Flow

**Corrected 2026-08-16.** Sourced directly from all six individual service files (#8, #9, #10, #12, #20, #21), not from this screen's own UI filter values:

Draft
↓
Submitted
↓
Trustee Review
↓
RERA Escrow Audit *(performed by the Compliance & Escrow Auditor — see the terminology note under Feature Overview)*
↓
Approved
↓
*Service-specific terminal state:*

| Service | Terminal state |
| :---- | :---- |
| #8 — Escrow Account Activation | Active |
| #9 — Escrow Account Transfer | Transferred |
| #20 — Depositing a Mortgage into an Escrow Account | Deposited |
| #21 — Bank Guarantee Cancellation | Cancelled |

Additional statuses (all six services): Information Requested, Returned, Rejected.

**Superseded by this correction**: the screen's own UI filter set (`No Request / Pending Approval / Under Review / Approved / Released / Returned / Rejected`) and the "Escrow Status" (`Pending Registration → Active → Suspended → Closed`) / "Fund Release Status" split previously described here. Neither matches the sourced vocabulary above. The UI filter values may still be worth surfacing as filter options in an eventual build, but they are not this feature's status flow.

## 14. Possible Outcomes

* Escrow Account Activated / Transferred
* Mortgage Deposited into Escrow
* Bank Guarantee Cancelled
* Additional Information Requested
* Application Returned or Rejected

## 15. Output

Not specified in source for any of the four services ("no doc" against each row) — each service's own Section 15 proposes an in-system confirmation record; needs client confirmation.

## 16. Related Features

* Fund Release Request *(Feature #5 — the milestone-based withdrawal/receipt flow reached from Escrow Details, Services #10/#12, using the same sourced status vocabulary)*
* Applications *(Feature #1)*
* Financial & Trust Institutions' Escrow Request Queue and Trust Accounts *(cross-module — the Account Trustee's side of the same accounts; **status vocabulary corrected 2026-08-16, and the RERA-side approver confirmed to be the same Compliance & Escrow Auditor role in both modules**, see Feature Overview)*

## 17. UI Screens

* Escrow Management
* Escrow Details

## 18. API Requirements

* Retrieve Organization Escrow Accounts / Search / Filter
* Retrieve Escrow Details, Fund Release Overview, Escrow Analytics
* Submit Escrow Registration / Transfer / Deposit / Cancellation (per selected service)
* Notify Account Trustee
* Retrieve Trustee Assessment
* Submit for RERA Escrow Audit
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Developer Company, Project, User
* Escrow Account, Application
* Account Trustee, Bank Guarantee, Mortgage *(where relevant per service)*
* Document, Notification, Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can view, register, and act on any escrow account.
* Every request routes through Account Trustee review before RERA's escrow audit — never directly to RERA.
* No payment step is required for any of the four services this feature covers.
* Row actions are governed by the account's own state, never by who is viewing.
* All escrow activity is recorded in the audit log, including the acting user's role.
* Status vocabulary matches the sourced individual service files, not the screen's own UI filter values.

## 21. Business Rules

1. Any of the developer's four Group B roles may register or act on any escrow account — no per-user assignment scoping.
2. Every request passes through Account Trustee review, then RERA's escrow audit, in that order — sourced identically across all six escrow services.
3. None of the four services this feature covers (#8, #9, #20, #21) requires payment at any point.
4. Row actions depend on the account's own state — a closed or already-actioned request takes no duplicate action, regardless of who asks.
5. All escrow activity is permanently recorded in the audit trail, including the acting user's role.
6. The status vocabulary (`Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → [service-specific terminal state]`, plus `Information Requested / Returned / Rejected`) is sourced from the individual service files and is authoritative — the screen's own UI filter values are not.
7. "RERA Escrow Audit," "Escrow Account Department," and financial-trust-institutions' "Compliance & Escrow Auditor" are the same regulatory role, confirmed against the master source table — not three different names for three different things.

## Open Questions

1. Whether "Escrow Balance" should mean gross balance or balance net of committed pending releases is flagged but unresolved — the source screen glosses both the same way; if the client intends the net reading, a second column would be needed.
2. Cardinality mismatches for Services #9, #20, #21 against this screen are flagged in the module README but not resolved here — consult each service's own file.
3. Whether the screen's own UI filter values (`No Request / Pending Approval / Under Review / Approved / Released`) should be retained as user-facing filter labels even though they don't match the sourced status names, or whether the UI should be updated to use the sourced names directly — a design decision, not resolved here.
4. Same adoption question as Feature #1 — needs client confirmation.
