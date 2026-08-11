---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-10
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
  - escrow
---

# Service #11 – Amend the Cap of Administrative, Marketing and VAT Expenses

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Amend the Cap of Administrative, Marketing and VAT Expenses** service allows a developer to request a change to the pre-approved cap on administrative, marketing, and VAT expenses that may be drawn from a project's escrow account.

> **UI gap — flagged, not resolved.** Neither `ui/screens/escrow-management.md` nor `ui/screens/fund-release-request.md` addresses an expense-cap amendment. Nothing in the 19-screen set represents this service. The UI Screens list below is a **proposed** minimum surface, not a documented existing one.

## 2. Purpose

Allow a developer to adjust the pre-approved ceiling on non-construction expenses drawable from escrow, where project circumstances change (for example, a marketing campaign scope increase).

## 3. Description

The developer submits a request naming the current cap, the requested new cap, and justification. The request routes to the Account Trustee for assessment and then to the RERA escrow department for audit. On approval, the escrow account's expense cap is updated.

## 4. Who Can Apply

* Escrow Liaison

## 5. Prerequisites

* An existing active escrow account (Service #8) with a defined expense cap.
* Justification for the requested change.

## 6. Required Information

* Escrow Account Reference Number
* Current Expense Cap
* Requested New Expense Cap
* Justification

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Supporting Budget or Marketing Plan Justifying the New Cap
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

Not specified in the source. **Proposed**: not required; needs client confirmation.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module), escalating to the **RERA Escrow Department** for final audit.

## 11. Expected Processing Time

**Waiting time: 26 business hours; Service delivery: 32 business hours.**

## 12. Processing Workflow

Log in to Real Estate Developers Portal
↓
Select Escrow Account
↓
Select "Amend Expense Cap"
↓
Enter Requested Cap and Justification
↓
Submit Application
↓
Application Sent to Account Trustee
↓
Account Trustee Reviews, Uploads Assessment
↓
Escrow Account Department Audits: Approve or Reject
↓
If Approved, Expense Cap Updated

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
Cap Updated

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Expense Cap Successfully Amended
* Additional Information Requested
* Application Rejected

## 15. Output

Not specified in the source ("no doc" against this row). **Proposed**: an in-system Expense Cap Amendment Confirmation; needs client confirmation.

## 16. Related Services

* Service #8 – Escrow Account Activation
* Service #12 – Receive Payment from Escrow Account

## 17. UI Screens

Not currently represented in the 19-screen UI set. **Proposed** minimum surface: an "Amend Expense Cap" action from Escrow Management, alongside the existing Register Escrow Account and Request Fund Release actions.

## 18. API Requirements

* Retrieve Escrow Account Expense Cap
* Submit Expense Cap Amendment Request
* Notify Account Trustee
* Retrieve Trustee Assessment
* Submit for RERA Escrow Audit
* Retrieve Application Status
* Update Escrow Account Expense Cap
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Escrow Account
* Account Trustee
* Expense Cap
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request an amendment to an active escrow account's expense cap.
* Trustee assessment and RERA escrow audit both precede approval.
* Approved amendments update the escrow account's expense cap.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an active escrow account's expense cap may be amended under this service.
2. Justification is required for every submission.
3. The Account Trustee's assessment must precede RERA's escrow audit.
4. All submissions, assessments, audits, and notifications must be permanently recorded in the audit trail.
5. **No UI screen currently exists for this service** — flagged for the client rather than force-fit to an existing screen.
