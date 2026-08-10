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
  - "RERAN/modules/real-estate-developer/ui/screens/escrow-management.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-queue.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
  - escrow
---

# Service #21 – Bank Guarantee Cancellation

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Bank Guarantee Cancellation** service allows a developer to request cancellation of a bank guarantee held in connection with a project's escrow arrangements — for example once the guaranteed obligation has been fulfilled and the guarantee is no longer needed.

> **UI cardinality mismatch — flagged, not resolved.** As with Services #9, #10, #11, and #20, `ui/screens/escrow-management.md` exposes no dedicated action for this transaction; it is documented against the same generic Escrow Management surface described in Service #8. See the PR description for the consolidated cardinality-mismatch note.

## 2. Purpose

Allow a developer to formally release a bank guarantee once its underlying obligation is discharged, under Account Trustee and RERA oversight.

## 3. Description

The developer submits a cancellation request identifying the bank guarantee and the basis for cancellation. The request routes to the Account Trustee, who assesses and uploads supporting documentation, and forwards it to the RERA escrow department for audit. On approval, the guarantee is cancelled.

## 4. Who Can Apply

* Escrow Liaison

## 5. Prerequisites

* An existing bank guarantee associated with the project's escrow arrangements.
* Basis for cancellation (e.g. obligation fulfilled, guarantee superseded).

## 6. Required Information

* Bank Guarantee Reference Number
* Issuing Institution
* Reason for Cancellation

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Evidence the Underlying Obligation Is Fulfilled
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
Select "Request Bank Guarantee Cancellation"
↓
Identify Guarantee and Reason
↓
Submit Application
↓
Application Sent to Account Trustee
↓
Account Trustee Reviews, Uploads Assessment
↓
Escrow Account Department Audits: Approve or Reject
↓
If Approved, Guarantee Cancelled

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
Cancelled

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Bank Guarantee Successfully Cancelled
* Additional Information Requested
* Application Rejected

## 15. Output

Not specified in the source ("no doc" against this row). **Proposed**: an in-system Bank Guarantee Cancellation Confirmation; needs client confirmation.

## 16. Related Services

* Service #8 – Escrow Account Activation
* Financial & Trust Institutions: [ui/screens/escrow-request-queue.md](../../financial-trust-institutions/ui/screens/escrow-request-queue.md) and [ui/screens/escrow-request-details.md](../../financial-trust-institutions/ui/screens/escrow-request-details.md) *(cross-module: the Account Trustee's side of this transaction)*

## 17. UI Screens

Documented against the same generic surface as Service #8 — see the cardinality-mismatch note in Section 1.

## 18. API Requirements

* Validate Bank Guarantee Status
* Submit Guarantee Cancellation Request
* Notify Account Trustee
* Retrieve Trustee Assessment
* Submit for RERA Escrow Audit
* Retrieve Application Status
* Cancel Bank Guarantee
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Escrow Account
* Bank Guarantee
* Account Trustee
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request cancellation of an existing bank guarantee tied to the project's escrow arrangements.
* System validates the guarantee reference and current status.
* Trustee assessment and RERA escrow audit both precede approval.
* Approved requests cancel the guarantee.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an existing, active bank guarantee may be cancelled under this service.
2. A reason for cancellation is required for every submission.
3. The Account Trustee's assessment must precede RERA's escrow audit.
4. All submissions, assessments, audits, and cancellations must be permanently recorded in the audit trail.
5. **No dedicated UI action exists for this service** — flagged for the client rather than force-fit to a distinct screen.
