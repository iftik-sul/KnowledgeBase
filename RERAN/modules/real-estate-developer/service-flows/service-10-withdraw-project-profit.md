---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/service-flows/feature-13-profit-withdrawal-request.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
  - escrow
---

# Service #10 – Project Profit Withdrawal

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Project Profit Withdrawal** service allows a developer to request withdrawal of the developer's profit margin from a project's escrow account, distinct from a milestone-based construction fund release.

> **Resolved 2026-08-16, by client decision.** The UI mismatch flagged since this document was first written — this service was documented against `ui/screens/fund-release-request.md`, a screen shaped for milestone/construction-draw requests (engineer certification, Quantity Surveyor report, milestone percentage complete) — is now resolved. The client has confirmed profit withdrawal genuinely needs its own flow, distinct from milestone-based fund release. See [Feature #13 — Profit Withdrawal Request](feature-13-profit-withdrawal-request.md), a new feature built to this service's actual shape rather than borrowed from Service #12's screen.

## 2. Purpose

Allow a developer to draw down accumulated profit from a project's escrow account once entitled to do so, under Account Trustee and RERA oversight.

## 3. Description

The developer submits a profit withdrawal request against the project's escrow account, stating the basis for entitlement. The request routes to the Account Trustee, who assesses project solvency and the basis for the withdrawal, uploads supporting assessment, and forwards to RERA's Escrow Audit. On approval, the withdrawal is released.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Escrow Liaison* — a documented judgment call, not an uncontested fact. **Corrected 2026-08-15 (issue #37).** The master service table's own Responsible Role column for this row reads **"Sales & Disclosure Officer / Admin Officer,"** not Escrow Liaison — a disagreement checked systematically across all seven escrow services (#8–#12, #20, #21). All seven rows are attributed to Sales & Disclosure Officer (with or without "/ Admin Officer") in the source table; none is attributed to Escrow Liaison. `roles-and-responsibilities.md`'s Escrow Liaison description — "coordinates trustee/auditor, files escrow statements and milestone-release requests" — is a near-verbatim match to what these seven services actually do, and reads as the more considered source: the source table's role column looks like a coarse, category-level default applied across nearly the whole Real Estate Development Services section, not a genuine per-service judgment — the same shape Group C's A4 finding identified in its own source table's role column. This document follows that precedent and treats Escrow Liaison as the better-reasoned typical attribution, not the source table's — but this is a stated judgment call, not a sourced fact either way. **It has no access consequence**: any of the four Group B roles may file this application regardless of which is "typical."

That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing active escrow account (Service #8) with available profit balance.
* Basis for entitlement to withdraw (e.g. project completion percentage, contractual milestone).

## 6. Required Information

* Escrow Account Reference Number
* Requested Withdrawal Amount
* Basis for Entitlement

## 7. Required Documents

> **Proposed** — not itemized in the source. See Feature #13 for the full proposed list, reasoned from what a profit-entitlement claim needs to demonstrate.

* Project Financial Statement Supporting the Withdrawal
* Account Trustee Assessment (uploaded by the Trustee)
* Other supporting documents required by RERA

## 8. Service Fee

**Not a fee-collecting service.** This service disburses funds *to* the developer from the project escrow account; RERA is not collecting a service fee here, and the source workflow contains no payment step.

> The escrow account this draws on is a regulated holding account for sale proceeds and construction-milestone releases. It is not a pre-funded RERA-fee account, and the move to per-transaction fee payment does not apply to it.

## 9. Payment Required

**No.** This service disburses funds to the developer rather than collecting a fee from them.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module), escalating to the **Compliance & Escrow Auditor** (RERA's Escrow Account Department) for final audit.

## 11. Expected Processing Time

**Waiting time: 29 business hours; Service delivery: 33 business hours.**

## 12. Processing Workflow

Login to Real Estate Developers Portal
↓
Open Profit Withdrawal Request *(Feature #13)*
↓
Select Escrow Account, State Basis for Entitlement, Enter Requested Amount
↓
Upload Supporting Documents
↓
Submit Application
↓
Application Sent to Account Trustee
↓
Account Trustee Assesses Solvency, Uploads Assessment
↓
Compliance & Escrow Auditor Audits: Approve or Reject
↓
If Approved, Funds Released

## 13. Application Status Flow

Draft
↓
Submitted
↓
Trustee Review
↓
RERA Escrow Audit
↓
Approved
↓
Released

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Profit Withdrawal Approved and Released
* Additional Information Requested
* Application Rejected

## 15. Output

Not specified in the source ("no doc" against this row). **Proposed**: an in-system Profit Withdrawal Confirmation and disbursement record; needs client confirmation.

## 16. Related Services

* Service #8 – Escrow Account Activation
* Service #12 – Receive Payment from Escrow Account *(sibling service, now on a separate feature — Fund Release Request, Feature #5 — since its milestone-verification shape genuinely fits that screen where this service's doesn't)*
* Financial & Trust Institutions: [ui/screens/escrow-request-queue.md](../../financial-trust-institutions/ui/screens/escrow-request-queue.md) and [ui/screens/escrow-request-details.md](../../financial-trust-institutions/ui/screens/escrow-request-details.md) *(cross-module: the Account Trustee's side of this transaction)*

## 17. UI Screens

**No screen currently exists.** Previously documented against Fund Release Request as the closest available match; now assigned to Feature #13 — Profit Withdrawal Request, itself unbuilt, proposed to this service's actual shape. See that feature's own Section 17.

## 18. API Requirements

* Validate Escrow Account Status and Balance
* Submit Profit Withdrawal Request
* Notify Account Trustee
* Retrieve Trustee Assessment
* Submit for RERA Escrow Audit
* Retrieve Application Status
* Disburse Funds
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Escrow Account
* Account Trustee
* Profit Withdrawal
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request a profit withdrawal against an active escrow account with available balance.
* System validates requested amount against available balance.
* Trustee assessment and RERA escrow audit both precede release.
* Approved withdrawals disburse funds and update the escrow account balance.
* No construction-milestone verification (Engineer Certificate, Quantity Surveyor Report) is required — resolved 2026-08-16, this service is not a construction draw.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an active escrow account with an available profit balance may be drawn against under this service.
2. The Account Trustee's assessment must precede RERA's escrow audit.
3. All submissions, Trustee assessments, audits, and disbursements must be permanently recorded in the audit trail.
4. **Resolved 2026-08-16.** This service is documented against its own feature (#13), not force-fit to Fund Release Request's construction-draw shape.

## Open Questions

1. ~~Is this service's screen a genuine fit?~~ **Resolved 2026-08-16 — no; see Feature #13, a new proposed feature, not yet built.**
2. What documentation genuinely constitutes sufficient "evidence of entitlement basis"? See Feature #13's own Open Questions.
