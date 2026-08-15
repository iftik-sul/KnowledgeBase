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
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-queue.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
  - escrow
---

# Service #9 – Escrow Account Transfer

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Escrow Account Transfer** service allows a developer to request moving a project's active escrow account from its current Account Trustee to a different one.

> **UI cardinality mismatch — flagged, not resolved.** `ui/screens/escrow-management.md` exposes exactly two generic actions — "Register Escrow Account" and "Request Fund Release" — for the entire escrow surface. There is no dedicated "Transfer Escrow Account" action distinct from account activation. This service is documented against the same generic Escrow Management screen as Service #8, not a screen of its own. See the PR description for the full cardinality-mismatch note covering rows 8, 9, 10, 12, 20, and 21.

## 2. Purpose

Allow a developer to change the institution holding a project's escrow account — for example where the current Account Trustee's approval lapses, or the developer wants a different institution — without dissolving and re-activating the account from scratch.

## 3. Description

The developer submits a transfer request naming the current and destination Account Trustee. The request routes through the current Trustee (or the Account Trustee capability generally, per the shared escrow workflow pattern), is audited by the RERA escrow department, and on approval the account of record changes to the new Trustee.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Escrow Liaison* — a documented judgment call, not an uncontested fact. **Corrected 2026-08-15 (issue #37).** The master service table's own Responsible Role column for this row reads **"Sales & Disclosure Officer / Admin Officer,"** not Escrow Liaison — a disagreement checked systematically across all seven escrow services (#8–#12, #20, #21). All seven rows are attributed to Sales & Disclosure Officer (with or without "/ Admin Officer") in the source table; none is attributed to Escrow Liaison. `roles-and-responsibilities.md`'s Escrow Liaison description — "coordinates trustee/auditor, files escrow statements and milestone-release requests" — is a near-verbatim match to what these seven services actually do, and reads as the more considered source: the source table's role column looks like a coarse, category-level default applied across nearly the whole Real Estate Development Services section, not a genuine per-service judgment — the same shape Group C's A4 finding identified in its own source table's role column. This document follows that precedent and treats Escrow Liaison as the better-reasoned typical attribution, not the source table's — but this is a stated judgment call, not a sourced fact either way. **It has no access consequence**: any of the four Group B roles may file this application regardless of which is "typical."

That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing active escrow account (Service #8).
* Destination Account Trustee identified and approved to act as trustee.

## 6. Required Information

* Current Escrow Account Reference Number
* Destination Account Trustee
* Reason for Transfer

## 7. Required Documents

> **Proposed** — not itemized in the source. Following the same pattern as Service #8's Trustee-assessment documents. Needs client confirmation.

* Reason / Justification for Transfer
* Destination Trustee's Acceptance
* Other supporting documents required by RERA

## 8. Service Fee

**No RERA service fee is sourced for this service.** The source workflow runs from submission through Account Trustee assessment to the escrow department's approval or rejection, with no payment step at any point.

> This is separate from the project escrow account itself, which this service acts upon. That account is a regulated holding account for sale proceeds and construction-milestone releases — not a pre-funded RERA-fee account, and not affected by the move to per-transaction fee payment.

## 9. Payment Required

**No.** Not required at any point in the sourced workflow. Should the client confirm that a processing fee does apply, it would be paid per transaction through the shared platform payment gateway like every other Group B fee — **proposed**, needs client confirmation.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module), escalating to the **RERA Escrow Department** for final audit.

## 11. Expected Processing Time

**Waiting time: 24 working hours; Service delivery: 45 working hours.**

## 12. Processing Workflow

Log in to Real Estate Developers Portal
↓
Select Escrow Account Link
↓
Select "Apply for Escrow Account Transfer"
↓
Identify Destination Account Trustee
↓
Submit Application
↓
Application Sent to Account Trustee
↓
Account Trustee Studies Request, Uploads Assessment
↓
Escrow Account Department Audits: Approve or Reject
↓
If Approved, System Updated — Escrow Account Transferred

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
Transferred

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Escrow Account Successfully Transferred
* Additional Information Requested
* Application Rejected

## 15. Output

Not specified in the source ("no doc" against this row). **Proposed**: an in-system Escrow Account Transfer Confirmation; needs client confirmation.

## 16. Related Services

* Service #8 – Escrow Account Activation
* Financial & Trust Institutions: [ui/screens/escrow-request-queue.md](../../financial-trust-institutions/ui/screens/escrow-request-queue.md) and [ui/screens/escrow-request-details.md](../../financial-trust-institutions/ui/screens/escrow-request-details.md) *(cross-module: the Account Trustee's side of this transaction)*

## 17. UI Screens

Documented against the same generic surface as Service #8 — see the cardinality-mismatch note in Section 1. No screen names an "Escrow Account Transfer" action distinctly.

## 18. API Requirements

* Validate Escrow Account Status
* Validate Destination Trustee Eligibility
* Submit Escrow Transfer Request
* Notify Current and Destination Trustee
* Submit for RERA Escrow Audit
* Retrieve Application Status
* Update Escrow Account Trustee of Record
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

* Developer can request a transfer of an existing active escrow account to a new Account Trustee.
* System validates the escrow account is active and the destination Trustee is eligible.
* RERA escrow department audits before the transfer completes.
* Approved transfers update the escrow account's Trustee of record.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an active escrow account may be transferred.
2. The destination Account Trustee must be an approved trustee under Financial & Trust Institutions' trust-account approval process.
3. All submissions, Trustee assessments, audits, and notifications must be permanently recorded in the audit trail.
4. **No dedicated UI action exists for this service** — flagged for the client rather than force-fit to a distinct screen.
