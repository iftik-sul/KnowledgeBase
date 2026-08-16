---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/fund-release-request.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-10-withdraw-project-profit.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-12-receive-escrow-payment.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - real-estate-developer
  - shared-feature
  - domain-workspace
  - escrow
---

# Feature #5 – Fund Release Request

**Feature Category:** Shared Platform Features – Domain Workspace

## 1. Feature Overview

**Fund Release Request** is the operational workspace for preparing and submitting a milestone-based release request against a project escrow account — reached from Escrow Details (Feature #4), but tracked and processed as its own object with its own detailed progress tracker, engineer/quantity-surveyor verification, and Trustee-then-RERA review chain.

> **Cross-module status vocabulary — corrected 2026-08-16, superseding an earlier same-day resolution.** A first pass mapped this screen's own 9-stage tracker onto `No Request → Pending Approval → Under Review → Approved → Released`, taken from a UI screen's filter values. That was wrong: neither Service #10 nor Service #12's own file uses those terms. Both — verified directly — use `Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → Released`, with additional statuses `Information Requested / Returned / Rejected`, identical to the vocabulary sourced for the other four escrow services (Feature #4). **The screen's own "Under Bank Review" label is also corrected** — the source calls the reviewing party the **Account Trustee**, not a bank; "Bank Review" in the UI screen's own stage names appears to be the screen's own imprecision, not a sourced distinction. See Section 13 for the corrected mapping.

> **Terminology clarified 2026-08-16.** "RERA Escrow Audit" (this feature's second review stage) and financial-trust-institutions' "Compliance & Escrow Auditor" are the **same regulatory role**. Confirmed against `RERAN_service_flows_v2.md`'s master Service Workflows table: this module's six escrow services (rows 8–12, 20–21, including Services #10 and #12 that this feature covers) and financial-trust-institutions' mortgage/lease services (rows 30–39) all carry the identical Regulator/Approver-column value **"Compliance & Escrow Auditor"** — one Group A role, not two departments. See Feature #4's own Feature Overview for the full source citation.

## 2. Purpose

Give any developer user a complete workspace to specify a construction milestone, request the eligible release amount, upload supporting verification documents, respond to Trustee or RERA queries, and monitor the request through to funds released.

## 3. Description

The source documents only one variant of this screen, under the Escrow Liaison heading, with no second variant to reconcile — unlike every other domain workspace in this module. It is reachable and actionable by all four roles regardless. **A UI mismatch is flagged at source**, carried forward honestly rather than resolved by assumption: the screen is shaped as a milestone/construction-draw request (engineer and quantity-surveyor verification, percentage-of-completion tracking), and Service #10 (Project Profit Withdrawal — a margin distribution, not a milestone draw) is documented against it as the closest match, not a confirmed fit.

The request moves through a nine-stage detailed tracker (Draft → Information Completed → Documents Uploaded → Validation Passed → Submitted → Under Bank Review → Under RERA Review → Approved → Funds Released), which is this screen's own UI-layer progress view — see Section 13 for how it maps onto the sourced status vocabulary from Services #10 and #12's own files. The system auto-calculates the maximum eligible release amount against the approved milestone schedule and current escrow balance, flagging any request that exceeds it.

## 4. Used By

Services #10, #12, confirmed via service-10's `derived_from`:

* Project Profit Withdrawal *(flagged UI mismatch — see above)*
* Receive a Payment from the Project's Escrow Account

## 5. Prerequisites

* User is logged into a registered developer company account.
* An active escrow account exists (Feature #4) with an approved milestone schedule.
* Engineer and Quantity Surveyor verification of the cited milestone is available before submission.

## 6. Required Information

* Construction Milestone, Milestone Completion Date
* Requested Release Amount *(system auto-calculates the Eligible Release Amount against the milestone schedule and current balance)*
* Purpose of Release, Contractor/Vendor (optional), Expected Payment Date
* Milestone Verification: percentage completed, work summary, site inspection date, Engineer and Quantity Surveyor verification status and identifying details

## 7. Required Documents

* Engineer Progress Certificate
* Quantity Surveyor Report
* Construction Progress Report
* Site Inspection Report
* Contractor Payment Schedule (if applicable)
* Bank Supporting Documents (if applicable)
* Photographic Evidence

Engineer and Quantity Surveyor supporting documents are mandatory before submission — not optional, per the source screen's own Notes.

## 8. Service Fee

**No RERA service fee, for either service** — confirmed directly against both Service #10 and Service #12's own files. Neither disburses funds via a fee-collecting mechanism; both instead disburse funds *to* the developer.

## 9. Payment Required

**No, for either service.** Not a payment-collecting action — this feature releases funds *from* escrow. Confirmed against both Service #10 and Service #12's own Section 9, not merely inferred.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module) first, escalating to the **Compliance & Escrow Auditor** (RERA's Escrow Account Department) for final audit — the same two-stage chain used across all six escrow services (Feature #4), not a "bank" as the screen's own stage labels suggest, and the identical regulatory role financial-trust-institutions' mortgage/lease services use — see the terminology note under Feature Overview. Any of the developer's four Group B roles may prepare and submit; no role restriction despite the source documenting only the Escrow Liaison's typical workflow.

## 11. Expected Processing Time

Sourced per service, as a waiting-time/service-delivery pair: Service #10 — 29/33 business hours; Service #12 — 29/28 business hours.

## 12. Processing Workflow

Escrow Details
↓
Open Fund Release Request
↓
Select Milestone → Enter Release Information → Capture Milestone Verification
↓
Upload Supporting Documents (Engineer, Quantity Surveyor — mandatory)
↓
Validation Summary (escrow active, milestone eligible, amount within limit, both verifications complete, no duplicate request)
↓
Submit Request
↓
Account Trustee Reviews, Assesses Solvency, Uploads Assessment
↓
Compliance & Escrow Auditor Audits: Approve or Reject
↓
If Approved, Funds Released

## 13. Application Status Flow

**Corrected 2026-08-16.** Sourced directly from Service #10 and Service #12's own files, not from this screen's own UI stage labels:

Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → Released

Additional statuses (both services): Information Requested, Returned, Rejected.

**This screen's own 9-stage detailed tracker maps onto the sourced vocabulary as follows:**

| Detailed tracker stage | Sourced status |
| :---- | :---- |
| Draft, Information Completed, Documents Uploaded, Validation Passed | Draft |
| Submitted | Submitted |
| Under Bank Review | Trustee Review *(the reviewing party is the Account Trustee, not a bank — screen-label correction)* |
| Under RERA Review | RERA Escrow Audit *(performed by the Compliance & Escrow Auditor — see the terminology note under Feature Overview)* |
| Approved | Approved |
| Funds Released | Released |

**Superseded by this correction**: the previous mapping onto `No Request / Pending Approval / Under Review / Approved / Released`, which was itself taken from a different screen's UI filter values and never checked against Service #10 or #12's own files. Approved or Released requests remain read-only except for viewing/downloading — a lifecycle rule applying to every user equally, not a role restriction — unaffected by this correction.

## 14. Possible Outcomes

* Funds Released
* Additional Information Requested (Trustee or RERA)
* Request Returned / Rejected
* Requested Amount Exceeds Eligible Limit *(flagged automatically, not blocking entry but requiring correction before submission)*

## 15. Output

Not specified in source for either service ("no doc" against each row) — each service's own Section 15 proposes an in-system disbursement confirmation record; needs client confirmation.

## 16. Related Features

* Escrow Management *(Feature #4 — where this feature is reached from, via Escrow Details, and whose sourced status vocabulary this feature now shares)*
* Applications *(Feature #1)*
* Financial & Trust Institutions' Escrow Request Queue *(cross-module — the institution's side of this same transaction; **status vocabulary corrected 2026-08-16, and the RERA-side approver confirmed to be the same Compliance & Escrow Auditor role in both modules**, see Feature Overview)*

## 17. UI Screens

* Fund Release Request

## 18. API Requirements

* Retrieve Escrow Account / Milestone Schedule
* Calculate Eligible Release Amount
* Upload Documents
* Validate Release Request (per Section 7's checks)
* Submit to Account Trustee Review, then Compliance & Escrow Auditor's RERA Escrow Audit
* Respond to Queries
* Record Funds Release
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Developer Company, Project, Escrow Account, User
* Fund Release Request, Milestone
* Engineer Verification, Quantity Surveyor Verification
* Document, Query, Communication
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can prepare and submit a fund release request.
* Engineer and Quantity Surveyor verification documents are mandatory before submission.
* The system flags a requested amount exceeding the eligible limit before allowing submission.
* The request passes through Account Trustee review before RERA's escrow audit, in that order.
* Approved or Released requests are read-only for every user.
* The full Activity Timeline is recorded and immutable.
* This feature's detailed tracker maps cleanly onto the sourced status vocabulary at every point.

## 21. Business Rules

1. One fund release request is associated with a single construction milestone.
2. The maximum eligible release amount is auto-calculated against the approved milestone schedule and current escrow balance.
3. Engineer and Quantity Surveyor supporting documents are mandatory before submission.
4. The request must pass Account Trustee review before entering RERA's escrow audit.
5. Approved or Released requests become read-only for every user, not role-dependent.
6. Neither Service #10 nor Service #12 requires payment at any point.
7. All actions and communications are permanently recorded in the Activity Timeline for audit and regulatory compliance.
8. "RERA Escrow Audit" here and financial-trust-institutions' "Compliance & Escrow Auditor" are the same regulatory role, confirmed against the master source table.

## Open Questions

1. **Genuinely unresolved, flagged at source**: is Service #10 (Project Profit Withdrawal) actually the right fit for this screen's milestone/construction-draw shape, or is this a structural mismatch needing its own resolution? Not assumed away.
2. Same adoption question as Feature #1 — needs client confirmation.
