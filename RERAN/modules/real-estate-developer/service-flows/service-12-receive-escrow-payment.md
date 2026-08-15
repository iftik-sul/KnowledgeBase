---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/ui/screens/fund-release-request.md"
  - "RERAN/modules/real-estate-developer/ui/screens/fund-release-request-details.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-queue.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
  - escrow
---

# Service #12 – Receive a Payment from the Project's Escrow Account

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Receive a Payment from the Project's Escrow Account** service allows a developer to request release of funds from a project's escrow account against a completed construction milestone — the milestone-based fund release the module's `fund-release-request.md` screen is built around.

## 2. Purpose

Allow a developer to draw down escrow funds as construction milestones are certified complete, under Account Trustee certification and RERA oversight, so that project financing tracks physical progress.

## 3. Description

The developer submits a fund release request against a project's escrow account, citing the completed milestone and attaching engineer/Quantity Surveyor certification. The request routes to the Account Trustee, who certifies the milestone and project solvency, uploads supporting assessment, and forwards it to the RERA escrow department for audit. On approval, funds are released.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Escrow Liaison.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing active escrow account (Service #8).
* A completed construction milestone with supporting certification.

## 6. Required Information

* Escrow Account Reference Number
* Milestone Reached
* Requested Payment Amount

## 7. Required Documents

> **Proposed** — not itemized in the source beyond the general escrow-request pattern; the UI screen (`fund-release-request.md`) independently documents an Engineer Certificate and Quantity Surveyor report as part of this workflow, which this list follows. Needs client confirmation against the source.

* Engineer Certificate of Milestone Completion
* Quantity Surveyor Report
* Other supporting documents required by RERA

## 8. Service Fee

**Not a fee-collecting service.** This service disburses funds *to* the developer from the project escrow account; RERA is not collecting a service fee here, and the source workflow contains no payment step.

> The escrow account this draws on is a regulated holding account for sale proceeds and construction-milestone releases. It is not a pre-funded RERA-fee account, and the move to per-transaction fee payment does not apply to it.

## 9. Payment Required

Not applicable — this service disburses funds to the developer rather than collecting a fee from them. **Proposed**: a processing fee may still apply per the standard fee schedule, in which case it would be charged per transaction through the shared platform payment gateway; needs client confirmation.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module), escalating to the **RERA Escrow Department** for final audit.

## 11. Expected Processing Time

**Waiting time: 29 business hours; Service delivery: 28 business hours.**

## 12. Processing Workflow

Log in to Real Estate Developers Portal
↓
Select Escrow Account
↓
Select "Request Fund Release"
↓
Enter Milestone and Requested Amount
↓
Attach Milestone Certification
↓
Submit Application
↓
Application Sent to Account Trustee
↓
Account Trustee Certifies Milestone, Assesses Solvency, Uploads Assessment
↓
Escrow Account Department Audits: Approve or Reject
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

* Payment Successfully Released
* Additional Information Requested
* Application Rejected

## 15. Output

Not specified in the source ("no doc" against this row). **Proposed**: an in-system Fund Release Confirmation and disbursement record, consistent with `fund-release-request-details.md`; needs client confirmation.

## 16. Related Services

* Service #8 – Escrow Account Activation
* Service #10 – Project Profit Withdrawal
* Financial & Trust Institutions: [ui/screens/escrow-request-queue.md](../../financial-trust-institutions/ui/screens/escrow-request-queue.md) and [ui/screens/escrow-request-details.md](../../financial-trust-institutions/ui/screens/escrow-request-details.md) *(cross-module: the Account Trustee's side of this transaction)*

## 17. UI Screens

* Fund Release Request
* Fund Release Request Details

## 18. API Requirements

* Validate Escrow Account Status
* Validate Milestone Certification
* Submit Fund Release Request
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
* Construction Milestone
* Fund Release Request
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request fund release against an active escrow account for a certified milestone.
* System validates the escrow account is active and milestone certification is attached.
* Trustee certification and RERA escrow audit both precede release.
* Approved requests disburse funds and update the escrow account balance.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an active escrow account may be drawn against under this service.
2. A certified construction milestone is required for every request.
3. The Account Trustee's certification must precede RERA's escrow audit.
4. All submissions, certifications, audits, and disbursements must be permanently recorded in the audit trail.
