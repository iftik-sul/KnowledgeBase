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
  - "RERAN/modules/real-estate-developer/ui/screens/escrow-management.md"
  - "RERAN/modules/real-estate-developer/ui/screens/escrow-details.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-queue.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
  - escrow
---

# Service #8 – Escrow Account Activation

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Escrow Account Activation** service allows a developer to request activation of a project trust (escrow) account with a Group C Account Trustee, the first step in bringing a real estate project's escrow arrangements under RERA-regulated management.

## 2. Purpose

Establish a regulated escrow account for a project, with a designated Account Trustee, before any project funds can be routed through it.

## 3. Description

The developer logs in, selects the escrow account activation service, and submits the application. The request routes to the Group C Account Trustee, who assesses the developer/project's capability, uploads a supporting assessment, and forwards it to the RERA escrow department, which audits and approves or rejects the request. On approval, the escrow account is activated and reflected in the developer's Escrow Management screen.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Escrow Liaison.* That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* Registered developer company account.
* Real estate project already registered with RERA (see Service #13).
* No existing active escrow account for the same project.

## 6. Required Information

* Project Reference Number
* Requested Account Trustee (bank/institution)
* Project Solvency / Capability Summary

## 7. Required Documents

> **Proposed** — the source specifies only that the Trustee "uploads & sends docs" as part of its own assessment step, not what the developer must submit at request time. Needs client confirmation.

* Project Financial Summary
* Company Registration Documents
* Other supporting documents required by the Account Trustee or RERA

## 8. Service Fee

**No RERA service fee is sourced for this service.** The source workflow runs from submission through Account Trustee assessment to the escrow department's approval or rejection, with no payment step at any point.

> This is separate from the project escrow account itself, which this service acts upon. That account is a regulated holding account for sale proceeds and construction-milestone releases — not a pre-funded RERA-fee account, and not affected by the move to per-transaction fee payment.

## 9. Payment Required

**No.** Not required at any point in the sourced workflow. Should the client confirm that a processing fee does apply, it would be paid per transaction through the shared platform payment gateway like every other Group B fee — **proposed**, needs client confirmation.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module), escalating to the **RERA Escrow Department** for final audit.

## 11. Expected Processing Time

**Waiting time: 20 business hours** (queue time before the Trustee acts); **Service delivery: 13 business hours** (from Trustee action to completion). The split follows the same waiting-time/service-delivery reading Financial & Trust Institutions' `roles-and-responsibilities.md` (answer A6) proposes for these paired SLA figures across all escrow rows — proposed, not confirmed by the client.

## 12. Processing Workflow

Log in to Real Estate Developers Portal
↓
Select Escrow Account Link
↓
Select "Activate Escrow Account"
↓
Submit Application
↓
Application Sent to Account Trustee
↓
Account Trustee Studies Capability, Uploads Assessment
↓
Escrow Account Department Audits: Approve or Reject
↓
If Approved, System Updated — Escrow Account Activated

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
Active

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Escrow Account Successfully Activated
* Additional Information Requested
* Application Rejected

## 15. Output

Not specified in the source ("no doc" against this row). **Proposed**: an in-system Escrow Account Activation Confirmation, following the pattern of other completed applications in this module; needs client confirmation.

## 16. Related Services

* Service #9 – Escrow Account Transfer
* Service #12 – Receive Payment from Escrow Account
* Service #13 – Register Real Estate Project
* Financial & Trust Institutions Service — Account Trustee escrow request handling: [ui/screens/escrow-request-queue.md](../../financial-trust-institutions/ui/screens/escrow-request-queue.md) and [ui/screens/escrow-request-details.md](../../financial-trust-institutions/ui/screens/escrow-request-details.md) *(cross-module: this is the Account Trustee's side of this exact transaction)*

## 17. UI Screens

* Escrow Management
* Escrow Details
* Application Submitted

## 18. API Requirements

* Validate Project Eligibility
* Submit Escrow Activation Request
* Notify Account Trustee
* Retrieve Trustee Assessment
* Submit for RERA Escrow Audit
* Retrieve Application Status
* Activate Escrow Account
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Escrow Account
* Account Trustee
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request escrow account activation for a registered project with no existing active account.
* Request routes to the designated Account Trustee for assessment.
* Trustee assessment is forwarded to the RERA escrow department for final audit.
* Approved requests activate the escrow account and update the developer's Escrow Management view.
* All activities are recorded in the audit log.

## 21. Business Rules

1. A project may have only one active escrow account at a time.
2. The Account Trustee's assessment must precede RERA's escrow audit; RERA does not act on an activation request directly from the developer.
3. All submissions, Trustee assessments, audits, and notifications must be permanently recorded in the audit trail.
4. **Output document not specified in source** — flagged for client confirmation rather than invented outright.
