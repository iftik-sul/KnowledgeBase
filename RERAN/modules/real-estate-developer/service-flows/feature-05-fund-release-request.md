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

> **Narrowed 2026-08-16, by client decision.** This feature previously covered both Service #10 (Project Profit Withdrawal) and Service #12 (Receive Payment from Escrow Account) — flagged from the start as a mismatch for #10, since this screen's fields (engineer/quantity-surveyor verification, milestone percentage complete) describe a construction-milestone draw, not a profit distribution. The client has confirmed the mismatch and Service #10 now has its own feature — see [Feature #13 — Profit Withdrawal Request](feature-13-profit-withdrawal-request.md). **This feature now covers Service #12 only**, the one service its construction-verification shape genuinely fits.

## 2. Purpose

Give any developer user a complete workspace to specify a construction milestone, request the eligible release amount, upload supporting verification documents, respond to Trustee or RERA queries, and monitor the request through to funds released.

## 3. Description

The source documents only one variant of this screen, under the Escrow Liaison heading, with no second variant to reconcile — unlike every other domain workspace in this module. It is reachable and actionable by all four roles regardless.

The request moves through a nine-stage detailed tracker (Draft → Information Completed → Documents Uploaded → Validation Passed → Submitted → Under Bank Review → Under RERA Review → Approved → Funds Released), which is this screen's own UI-layer progress view — see Section 13 for how it maps onto Service #12's sourced status vocabulary. The system auto-calculates the maximum eligible release amount against the approved milestone schedule and current escrow balance, flagging any request that exceeds it.

## 4. Used By

Service #12 only, following the 2026-08-16 narrowing:

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

**No RERA service fee** — confirmed directly against Service #12's own file. This service disburses funds *to* the developer.

## 9. Payment Required

**No.** Not a payment-collecting action — this feature releases funds *from* escrow. Confirmed against Service #12's own Section 9.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module) first, escalating to the **Compliance & Escrow Auditor** (RERA's Escrow Account Department) for final audit — the same two-stage chain used across all six escrow services (Feature #4), not a "bank" as the screen's own stage labels suggest, and the identical regulatory role financial-trust-institutions' mortgage/lease services use — see Feature #4's own Feature Overview for the terminology note. Any of the developer's four Group B roles may prepare and submit; no role restriction despite the source documenting only the Escrow Liaison's typical workflow.

## 11. Expected Processing Time

**Waiting time: 29 business hours; Service delivery: 28 business hours.** Sourced from Service #12's own file.

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

Sourced directly from Service #12's own file, not from this screen's own UI stage labels:

Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → Released

Additional statuses: Information Requested, Returned, Rejected.

**This screen's own 9-stage detailed tracker maps onto the sourced vocabulary as follows:**

| Detailed tracker stage | Sourced status |
| :---- | :---- |
| Draft, Information Completed, Documents Uploaded, Validation Passed | Draft |
| Submitted | Submitted |
| Under Bank Review | Trustee Review *(the reviewing party is the Account Trustee, not a bank — screen-label correction)* |
| Under RERA Review | RERA Escrow Audit *(performed by the Compliance & Escrow Auditor — see Feature #4's terminology note)* |
| Approved | Approved |
| Funds Released | Released |

Approved or Released requests remain read-only except for viewing/downloading — a lifecycle rule applying to every user equally, not a role restriction.

## 14. Possible Outcomes

* Funds Released
* Additional Information Requested (Trustee or RERA)
* Request Returned / Rejected
* Requested Amount Exceeds Eligible Limit *(flagged automatically, not blocking entry but requiring correction before submission)*

## 15. Output

Not specified in source for Service #12 ("no doc" against the row) — its own Section 15 proposes an in-system disbursement confirmation record; needs client confirmation.

## 16. Related Features

* Escrow Management *(Feature #4 — where this feature is reached from, via Escrow Details, and whose sourced status vocabulary this feature shares)*
* Profit Withdrawal Request *(Feature #13 — the sibling feature for Service #10, split out 2026-08-16; shares the same approval chain and status vocabulary, but a genuinely different form)*
* Applications *(Feature #1)*
* Financial & Trust Institutions' Escrow Request Queue *(cross-module — the institution's side of this same transaction; status vocabulary and RERA-side approver confirmed identical across both modules)*

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

* Any of the developer's four Group B roles can prepare and submit a fund release request for Service #12.
* Engineer and Quantity Surveyor verification documents are mandatory before submission.
* The system flags a requested amount exceeding the eligible limit before allowing submission.
* The request passes through Account Trustee review before RERA's escrow audit, in that order.
* Approved or Released requests are read-only for every user.
* The full Activity Timeline is recorded and immutable.

## 21. Business Rules

1. One fund release request is associated with a single construction milestone.
2. The maximum eligible release amount is auto-calculated against the approved milestone schedule and current escrow balance.
3. Engineer and Quantity Surveyor supporting documents are mandatory before submission.
4. The request must pass Account Trustee review before entering RERA's escrow audit.
5. Approved or Released requests become read-only for every user, not role-dependent.
6. Service #12 does not require payment at any point.
7. All actions and communications are permanently recorded in the Activity Timeline for audit and regulatory compliance.
8. **Decided 2026-08-16.** This feature is scoped to Service #12 only — Service #10 has its own feature (#13), since its underlying transaction (a profit distribution) doesn't match this screen's construction-milestone shape.

## Open Questions

1. ~~Is Service #10 the right fit for this screen?~~ **Resolved 2026-08-16 — no, split into Feature #13.**
2. Same adoption question as Feature #1 — needs client confirmation.
