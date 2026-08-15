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

# Service #20 – Depositing a Mortgage into an Escrow Account

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Depositing a Mortgage into an Escrow Account** service allows a developer to route mortgage-financed proceeds for a project into that project's escrow account, so that mortgage-sourced funds are subject to the same trustee-controlled disbursement as other project funds.

> **UI cardinality mismatch — flagged, not resolved.** As with Services #9, #10, #11, and #21, `ui/screens/escrow-management.md` exposes no dedicated action for this transaction; it is documented against the same generic Escrow Management surface described in Service #8. See the PR description for the consolidated cardinality-mismatch note.

## 2. Purpose

Ensure mortgage proceeds financing a project flow through the same regulated, Trustee-controlled escrow account as other project funds, rather than bypassing escrow controls.

## 3. Description

The developer submits a request identifying the mortgage, the financing institution, and the destination escrow account. The request routes to the Account Trustee, who assesses and uploads supporting documentation, and forwards it to the RERA escrow department for audit. On approval, the mortgage proceeds are recorded as deposited into the escrow account.

## 4. Who Can Apply

Any user of a registered developer account, whatever role they hold — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, or Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../navigation.md).

*Typically filed in practice by the Escrow Liaison* — a documented judgment call, not an uncontested fact. **Corrected 2026-08-15 (issue #37).** The master service table's own Responsible Role column for this row reads **"Sales & Disclosure Officer,"** not Escrow Liaison — a disagreement checked systematically across all seven escrow services (#8–#12, #20, #21). All seven rows are attributed to Sales & Disclosure Officer (with or without "/ Admin Officer") in the source table; none is attributed to Escrow Liaison. `roles-and-responsibilities.md`'s Escrow Liaison description — "coordinates trustee/auditor, files escrow statements and milestone-release requests" — is a near-verbatim match to what these seven services actually do, and reads as the more considered source: the source table's role column looks like a coarse, category-level default applied across nearly the whole Real Estate Development Services section, not a genuine per-service judgment — the same shape Group C's A4 finding identified in its own source table's role column. This document follows that precedent and treats Escrow Liaison as the better-reasoned typical attribution, not the source table's — but this is a stated judgment call, not a sourced fact either way. **It has no access consequence**: any of the four Group B roles may file this application regardless of which is "typical."

That is a description of customary practice, not a restriction — the role recorded against the submission is audit-trail attribution only.

## 5. Prerequisites

* An existing active escrow account (Service #8).
* An identified mortgage financing the project (see Service #6).

## 6. Required Information

* Escrow Account Reference Number
* Mortgage Reference Number
* Mortgage Institution
* Deposit Amount

## 7. Required Documents

> **Proposed** — not itemized in the source. Needs client confirmation.

* Mortgage Offer/Disbursement Letter
* Other supporting documents required by RERA

## 8. Service Fee

**No RERA service fee is sourced for this service.** The source workflow runs from submission through Account Trustee assessment to the escrow department's approval or rejection, with no payment step at any point.

> This is separate from the project escrow account itself, which this service acts upon. That account is a regulated holding account for sale proceeds and construction-milestone releases — not a pre-funded RERA-fee account, and not affected by the move to per-transaction fee payment.

## 9. Payment Required

**No.** Not required at any point in the sourced workflow. Should the client confirm that a processing fee does apply, it would be paid per transaction through the shared platform payment gateway like every other Group B fee — **proposed**, needs client confirmation.

## 10. Processing Authority

**Account Trustee** (Financial & Trust Institutions module), escalating to the **RERA Escrow Department** for final audit.

## 11. Expected Processing Time

**Waiting time: 26 working hours; Service delivery: 32 working hours.**

## 12. Processing Workflow

Log in to Real Estate Developers Portal
↓
Select Escrow Account
↓
Select "Deposit Mortgage into Escrow Account"
↓
Identify Mortgage and Deposit Amount
↓
Submit Application
↓
Application Sent to Account Trustee
↓
Account Trustee Reviews, Uploads Assessment
↓
Escrow Account Department Audits: Approve or Reject
↓
If Approved, Deposit Recorded

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
Deposited

### Additional Statuses

* Information Requested
* Returned
* Rejected

## 14. Possible Outcomes

* Mortgage Deposit Successfully Recorded
* Additional Information Requested
* Application Rejected

## 15. Output

Not specified in the source ("no doc" against this row). **Proposed**: an in-system Mortgage Deposit Confirmation; needs client confirmation.

## 16. Related Services

* Service #6 – Register Sale Associated with an Initial Mortgage
* Service #8 – Escrow Account Activation
* Financial & Trust Institutions: [ui/screens/escrow-request-queue.md](../../financial-trust-institutions/ui/screens/escrow-request-queue.md) and [ui/screens/escrow-request-details.md](../../financial-trust-institutions/ui/screens/escrow-request-details.md) *(cross-module: the Account Trustee's side of this transaction)*

## 17. UI Screens

Documented against the same generic surface as Service #8 — see the cardinality-mismatch note in Section 1.

## 18. API Requirements

* Validate Escrow Account Status
* Validate Mortgage Reference
* Submit Mortgage Deposit Request
* Notify Account Trustee
* Retrieve Trustee Assessment
* Submit for RERA Escrow Audit
* Retrieve Application Status
* Record Escrow Deposit
* Send Notifications

## 19. Database Entities

* Developer Company
* Project
* Escrow Account
* Mortgage
* Account Trustee
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can request deposit of mortgage proceeds into an active project escrow account.
* System validates the mortgage reference and escrow account status.
* Trustee assessment and RERA escrow audit both precede approval.
* Approved deposits update the escrow account balance.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an active escrow account may receive a mortgage deposit under this service.
2. The mortgage must be a valid, identified mortgage financing the same project.
3. The Account Trustee's assessment must precede RERA's escrow audit.
4. All submissions, assessments, audits, and deposits must be permanently recorded in the audit trail.
5. **No dedicated UI action exists for this service** — flagged for the client rather than force-fit to a distinct screen.
