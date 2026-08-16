---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: extrapolated
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/service-flows/service-10-withdraw-project-profit.md"
  - "RERAN/modules/real-estate-developer/service-flows/feature-05-fund-release-request.md"
  - "RERAN/modules/real-estate-developer/ui/screens/fund-release-request.md"
tags:
  - real-estate-developer
  - shared-feature
  - domain-workspace
  - escrow
---

# Feature #13 – Profit Withdrawal Request

**Feature Category:** Shared Platform Features – Domain Workspace

> **Built 2026-08-16, by client decision.** Service #10 (Project Profit Withdrawal) was previously documented against Fund Release Request (Feature #5), the module's only escrow-disbursement screen — flagged from the start as a mismatch, since that screen's fields (Engineer Progress Certificate, Quantity Surveyor Report, milestone percentage complete, site inspection date) describe a construction-milestone draw, not a profit distribution. The client has confirmed the mismatch is real: Service #10 needs its own flow. **No source screen exists for this feature** — it is proposed here, structured as a sibling to Fund Release Request rather than a variant of it, reusing what genuinely is sourced (the Account Trustee → RERA Escrow Audit approval chain, the canonical escrow status vocabulary) and replacing what was borrowed from the wrong screen (the construction-verification fields) with fields that actually describe entitlement to profit.

## 1. Feature Overview

**Profit Withdrawal Request** is the workspace for a developer to draw down accumulated profit from a project's escrow account — a margin distribution once entitled, not a milestone-based construction draw. It shares Fund Release Request's approval chain and status vocabulary, since both are escrow-disbursement requests reviewed by the same parties, but replaces that feature's construction-verification fields with ones that actually describe profit entitlement.

## 2. Purpose

Give a developer a workspace shaped for what Service #10 actually is — proving entitlement to accumulated profit — rather than force-fitting it into a form built for proving physical construction progress.

## 3. Description

The developer selects the escrow account, states the basis for entitlement (project completion percentage or a specific contractual trigger), enters the requested amount, and attaches supporting financial documentation. The request routes to the Account Trustee for a solvency assessment, then to RERA's Escrow Audit for final approval — the same two-stage chain Fund Release Request and Escrow Management (Feature #4) use, since all three are ultimately reviewed by the same Account Trustee and Compliance & Escrow Auditor. On approval, funds are released.

**What this feature deliberately does not carry over from Fund Release Request:** Engineer Progress Certificate, Quantity Surveyor Report, percentage-of-construction-complete, and site inspection date. None of these describe a profit distribution, and requiring them would have been the mismatch this feature exists to fix.

## 4. Used By

Service #10 only, moved here from Feature #5 by this correction:

* Project Profit Withdrawal

## 5. Prerequisites

* User is logged into a registered developer company account.
* An active escrow account exists (Feature #4) with an available profit balance.
* A stated basis for entitlement to withdraw (e.g. project completion percentage, contractual milestone reached).

## 6. Required Information

* Escrow Account Reference Number
* Requested Withdrawal Amount
* Basis for Entitlement (completion percentage, or the specific contractual trigger relied upon)
* Purpose of Withdrawal (optional free text)

## 7. Required Documents

> **Proposed** — not itemized in source; built by client decision, reasoned from what a profit-entitlement claim actually needs to demonstrate, not from Fund Release Request's construction-verification list.

* Project Financial Statement Supporting the Withdrawal
* Account Trustee Assessment *(uploaded by the Trustee during review, not by the developer at submission)*
* Evidence of the Stated Entitlement Basis (e.g. sales register showing completion percentage, or the specific contract clause relied upon)
* Other supporting documents required by RERA

## 8. Service Fee

**No RERA service fee** — confirmed directly against Service #10's own file. This service disburses funds *to* the developer; it does not collect a fee.

## 9. Payment Required

**No.** This feature releases funds from escrow rather than collecting a fee.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module) first, escalating to the **Compliance & Escrow Auditor** for final audit — the same two-stage chain sourced across all six escrow services (Feature #4) and used by Fund Release Request (Feature #5) for Service #12.

## 11. Expected Processing Time

**Waiting time: 29 business hours; Service delivery: 33 business hours.** Sourced from Service #10's own file (row 10 of the master table).

## 12. Processing Workflow

Escrow Details *(Feature #4)*
↓
Open Profit Withdrawal Request
↓
Select Escrow Account → State Basis for Entitlement → Enter Requested Amount
↓
Upload Supporting Financial Documentation
↓
Submit Request
↓
Account Trustee Assesses Solvency and Entitlement Basis, Uploads Assessment
↓
Compliance & Escrow Auditor Audits: Approve or Reject
↓
If Approved, Funds Released

## 13. Application Status Flow

Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → Released

Additional statuses: Information Requested, Returned, Rejected.

**Same canonical vocabulary as Feature #4 and Feature #5** — sourced from Service #10's own file, unchanged by this restructure. Only the *form fields* leading up to submission changed; the review chain and status vocabulary did not need correcting, since they were never the source of the mismatch.

## 14. Possible Outcomes

* Profit Withdrawal Approved and Released
* Additional Information Requested
* Request Returned / Rejected

## 15. Output

Not specified in source ("no doc" against Service #10's row). **Proposed**: an in-system Profit Withdrawal Confirmation and disbursement record, consistent with the module's other escrow-disbursement outputs.

## 16. Related Features

* Escrow Management *(Feature #4 — where this feature is reached from, via Escrow Details)*
* Fund Release Request *(Feature #5 — the sibling feature for Service #12's milestone-based release; shares the same approval chain and status vocabulary, but a genuinely different form)*
* Applications *(Feature #1)*

## 17. UI Screens

**No screen currently exists.** Proposed screen name: **Profit Withdrawal Request**, structured as Fund Release Request's screen is, minus its construction-verification sections, plus the entitlement-basis fields above.

## 18. API Requirements

* Retrieve Escrow Account / Available Profit Balance
* Validate Requested Amount Against Available Balance
* Upload Documents
* Submit Profit Withdrawal Request
* Notify Account Trustee
* Retrieve Trustee Assessment
* Submit for RERA Escrow Audit
* Disburse Funds
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Developer Company, Project, Escrow Account, User
* Profit Withdrawal Request
* Document
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can prepare and submit a profit withdrawal request.
* The system validates the requested amount against the escrow account's available balance.
* No construction-milestone fields (Engineer Certificate, Quantity Surveyor Report, site inspection) are required — this feature does not ask for evidence of physical construction progress.
* The request passes through Account Trustee review before RERA's escrow audit, in that order.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an active escrow account with an available profit balance may be drawn against under this feature.
2. The Account Trustee's assessment must precede RERA's escrow audit.
3. **Decided 2026-08-16.** This feature exists specifically because Service #10 is a margin distribution, not a milestone-based construction draw — Fund Release Request (Feature #5) narrows to Service #12 only as a consequence.
4. No RERA service fee applies to this feature.
5. All submissions, Trustee assessments, audits, and disbursements must be permanently recorded in the audit trail.

## Open Questions

1. **No screen currently exists for this feature** — the field list and layout above are proposed, not sourced or designed against an existing UI. Needs client/design review before being built.
2. What documentation genuinely constitutes sufficient "evidence of entitlement basis"? Proposed examples given (sales register, contract clause) are illustrative, not a confirmed requirements list.
3. Same adoption question as Feature #1 — needs client confirmation.
