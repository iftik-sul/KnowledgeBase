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
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - shared-feature
  - domain-workspace
  - escrow
---

# Feature #5 – Fund Release Request

**Feature Category:** Shared Platform Features – Domain Workspace

## 1. Feature Overview

**Fund Release Request** is the operational workspace for preparing and submitting a milestone-based release request against a project escrow account — reached from Escrow Details (Feature #4), but tracked and processed as its own object with its own detailed progress tracker, engineer/quantity-surveyor verification, and bank-then-RERA review chain.

> **Cross-module status vocabulary — resolved 2026-08-16.** `No Request → Pending Approval → Under Review → Approved → Released` (Feature #4's Fund Release Status) is now the canonical cross-module status for Services #10/#12, matching financial-trust-institutions' Escrow Request Queue. This feature's own 9-stage tracker (Section 13) remains as the detailed progress view for this specific screen — it doesn't disappear — but now explicitly maps onto the canonical vocabulary: pre-submission stages (`Draft` through `Validation Passed`) fall under canonical `No Request`; `Submitted` marks the transition to `Pending Approval`; `Under Bank Review` and `Under RERA Review` are both sub-stages of canonical `Under Review` (the institution's assessment and RERA's subsequent audit, respectively — the same reconciliation applied on the institution's side); `Approved` and `Funds Released` map directly to their canonical counterparts.

## 2. Purpose

Give any developer user a complete workspace to specify a construction milestone, request the eligible release amount, upload supporting verification documents, respond to bank or RERA queries, and monitor the request through to funds released.

## 3. Description

The source documents only one variant of this screen, under the Escrow Liaison heading, with no second variant to reconcile — unlike every other domain workspace in this module. It is reachable and actionable by all four roles regardless. **A UI mismatch is flagged at source**, carried forward honestly rather than resolved by assumption: the screen is shaped as a milestone/construction-draw request (engineer and quantity-surveyor verification, percentage-of-completion tracking), and Service #10 (Project Profit Withdrawal — a margin distribution, not a milestone draw) is documented against it as the closest match, not a confirmed fit.

The request moves through a nine-stage detailed tracker (Draft → Information Completed → Documents Uploaded → Validation Passed → Submitted → Under Bank Review → Under RERA Review → Approved → Funds Released), which now maps onto the canonical five-stage cross-module vocabulary — see Feature Overview. The system auto-calculates the maximum eligible release amount against the approved milestone schedule and current escrow balance, flagging any request that exceeds it.

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

Set by the underlying service (#10 or #12) — see each service's own Section 8.

## 9. Payment Required

Not a payment-collecting action itself — this feature releases funds *from* escrow rather than collecting a fee. Consult Service #10/#12's own Section 9 for whether either carries a separate RERA fee alongside the release.

## 10. Processing Authority

**Bank review, then RERA review, in sequence** — distinct from most of this module's services, which go directly to RERA. Both are sub-stages of the canonical `Under Review` status (see Feature Overview). Any of the developer's four Group B roles may prepare and submit; no role restriction despite the source documenting only the Escrow Liaison's typical workflow.

## 11. Expected Processing Time

Not given a single figure in source — spans two sequential review stages (bank, then RERA); see Service #10/#12's own Section 11 for whatever timing is sourced there.

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
Under Bank Review → Under RERA Review
↓
Approved → Funds Released

## 13. Application Status Flow

**Detailed tracker (this screen's own progress view):**
Draft → Information Completed → Documents Uploaded → Validation Passed → Submitted → Under Bank Review → Under RERA Review → Approved → Funds Released

**Mapped onto the canonical cross-module vocabulary (resolved 2026-08-16):**

| Detailed stage | Canonical status |
| :---- | :---- |
| Draft, Information Completed, Documents Uploaded, Validation Passed | No Request |
| Submitted | Pending Approval |
| Under Bank Review | Under Review *(institution's assessment)* |
| Under RERA Review | Under Review *(RERA's audit, same canonical status)* |
| Approved | Approved |
| Funds Released | Released |

Additional: Information Requested (from bank or RERA, via the Queries table) → Response Submitted → review resumes, staying within canonical `Under Review` throughout. **Approved or Funds Released requests become read-only** except for viewing/downloading — a lifecycle rule applying to every user equally, not a role restriction.

## 14. Possible Outcomes

* Funds Released
* Additional Information Requested (bank or RERA)
* Request Returned / Rejected
* Requested Amount Exceeds Eligible Limit *(flagged automatically, not blocking entry but requiring correction before submission)*

## 15. Output

* Funds released to the developer, recorded against the escrow account's balance
* Full Activity Timeline of the request, from creation through funds transferred

## 16. Related Features

* Escrow Management *(Feature #4 — where this feature is reached from, via Escrow Details, and whose canonical status vocabulary this feature's detailed tracker now maps onto)*
* Applications *(Feature #1)*
* Financial & Trust Institutions' Escrow Request Queue *(cross-module — the institution's side of this same transaction; **status vocabulary reconciled 2026-08-16**, see Feature Overview)*

## 17. UI Screens

* Fund Release Request

## 18. API Requirements

* Retrieve Escrow Account / Milestone Schedule
* Calculate Eligible Release Amount
* Upload Documents
* Validate Release Request (per Section 7's checks)
* Submit to Bank Review, then RERA Review
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
* The request passes through Bank Review before RERA Review, in that order, both within canonical `Under Review`.
* Approved or Funds Released requests are read-only for every user.
* The full Activity Timeline is recorded and immutable.
* This feature's detailed tracker maps cleanly onto the canonical cross-module vocabulary at every point.

## 21. Business Rules

1. One fund release request is associated with a single construction milestone.
2. The maximum eligible release amount is auto-calculated against the approved milestone schedule and current escrow balance.
3. Engineer and Quantity Surveyor supporting documents are mandatory before submission.
4. The request must pass Bank Review before entering RERA Review; both are sub-stages of canonical `Under Review`.
5. Approved or Funds Released requests become read-only for every user, not role-dependent.
6. All actions and communications are permanently recorded in the Activity Timeline for audit and regulatory compliance.

## Open Questions

1. **Genuinely unresolved, flagged at source**: is Service #10 (Project Profit Withdrawal) actually the right fit for this screen's milestone/construction-draw shape, or is this a structural mismatch needing its own resolution? Not assumed away.
2. Expected processing time is not given a single sourced figure spanning both review stages — needs client confirmation.
3. Same adoption question as Feature #1 — needs client confirmation.
