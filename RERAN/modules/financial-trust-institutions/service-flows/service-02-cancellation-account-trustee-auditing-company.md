---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
updated: 2026-08-14
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
tags:
  - financial-trust-institutions
  - service-flow
  - institutional-approval
  - account-trustee
  - auditing-company
  - cancellation
---

# Service #2 – Cancellation of Account Trustee & Auditing Company

**Service Category:** Institutional Approval Services

**Source row:** 29 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Cancellation of Account Trustee & Auditing Company** service lets an institution give up its approved standing as an Account Trustee or Auditing Company. RERA reviews the request, issues a cancellation certificate, and removes the institution from the active register of approved trustees and auditors.

## 2. Purpose

Formally terminate an institution's approved trustee or auditor standing at its own request, so the platform, developers and other institutions no longer rely on a status the institution no longer holds.

## 3. Description

The Institution Relationship Manager submits a cancellation application. RERA's Compliance & Escrow Auditor studies and audits the request, then issues a cancellation e-certificate by email and updates the Trust Account System and public register to reflect the cancellation.

## 4. Who Can Apply

### Applicant

* Institution Relationship Manager  
* Authorized Representative acting under a delegated permission scope

> **Proposed** — as with Service #1, the source assigns this application to the **Account Trustee** as responsible role. `open-questions.md` A4 re-derives ownership to the Institution Relationship Manager, on the same reasoning: giving up institutional standing is a company-level act, not a transaction the trustee performs on itself. **Confidence: High**, per the answers doc.

## 5. Prerequisites

* Registered RERAN institution (Group C) account.  
* Institution Relationship Manager has platform access under the institution's corporate account.  
* An existing approved standing as Account Trustee or Auditing Company to cancel.  
* No unresolved obligations under the standing being cancelled. *(Proposed — not stated in source; see Open Questions.)*

## 6. Required Information

### Institution Information

* Institution Legal Name  
* Existing Approval Reference Number  
* Reason for Cancellation

## 7. Required Documents

> **Proposed** — the source states only that the institution "submits application" and that RERA "studies and audits" it, without enumerating documents. The list below is proposed by analogy with the individual-user module and what a standing-cancellation request plainly needs.

* Existing Approval Certificate  
* Board Resolution Authorizing Cancellation  
* Confirmation of No Outstanding Trust Account Obligations *(where the institution has acted as Account Trustee)*  
* Government-issued Identification (Authorized Representative)  
* Other supporting documents required by RERAN

## 8. Service Fee

Not specified in source. Row 29's workflow lists no payment step, unlike row 28 (Approval/Renewal), which explicitly includes "Payment of fees." See Section 9 and Open Questions.

## 9. Payment Required

**Not specified in source.**

> **Proposed** — no payment step appears anywhere in row 29's workflow. The working assumption is that cancellation carries no fee, consistent with the source's silence, but this is an inference rather than a sourced position and should be confirmed with the client before it is treated as final. See Open Questions.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced: RERA "studies and audits the application."

## 11. Expected Processing Time

**Waiting time: 29 business hours; Service delivery: 28 business hours.**

Sourced from row 29 — identical figures to Service #1. Per `open-questions.md` A6, waiting time is read as the queue/counterparty portion and delivery time as RERA's own processing; this reading needs explicit client confirmation.

## 12. Processing Workflow

Institution Relationship Manager

Login  
↓  
Open Services  
↓  
Select "Cancellation of Account Trustee & Auditing Company"  
↓  
Enter Institution Information  
↓  
Upload Required Documents  
↓  
Submit Application

*Channel: Land Department website (Real Estate Developers Portal – Title Deed), Trust Account System, or email — all three are named in the source (row 29).*

↓

RERA

Study Application  
↓  
Audit Application  
↓  
Approve, Return, or Reject  
↓  
Issue Cancellation e-Certificate  
↓  
Send Cancellation e-Certificate via Email  
↓  
Update Trust Account System  
↓  
Update Public Register of Approved Trustees & Auditors  
↓  
Notify Institution

## 13. Application Status Flow

Draft  
↓  
Submitted  
↓  
Under Review  
↓  
Information Requested  
↓  
Returned for Correction  
↓  
Approved  
↓  
Completed

### Additional Statuses

* Rejected  
* Withdrawn

> **Proposed** — this service carries no `Approved — Awaiting Payment` state and no `Expired` state, because Section 9 finds no sourced payment step to make conditional. If a fee is later confirmed, both should be reinstated per the core vocabulary in `services-overview.md`. This service also does not carry the Group C `Pending Internal Certification` / `Returned by Certifier` extension, for the same reason given in Service #1: no internal institutional certification step is described in source.

## 14. Possible Outcomes

* Approval / Renewal Standing Cancelled  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Cancellation e-Certificate — sourced (row 29)  
* Updated Public Register Entry (institution removed from active trustee/auditor register)

## 16. Related Services

* Service #1 — Approval / Renewal of Account Trustee & Auditing Company  
* Service #18 — Contract Cancellation *(also owned by the Institution Relationship Manager)*

## 17. UI Screens

* Services  
* Cancellation of Account Trustee & Auditing Company  
* Institution Information  
* Document Upload  
* Application Review  
* Application Submitted  
* Application Details  
* Cancellation Confirmation

## 18. API Requirements

* Retrieve Institution Profile  
* Retrieve Existing Approval Status  
* Upload Documents  
* Submit Cancellation Application  
* Retrieve Application Status  
* Update Approved Trustee / Auditor Register  
* Generate Cancellation e-Certificate  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff *(no scope field — every staff member has identical system access; role is recorded per-action, not per-account, see Audit Log below)*  
* Application  
* Service Request  
* Document  
* Approval Record  
* Notification  
* Audit Log *(captures the acting user and their role at time of action for every logged event, per [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle))*

## 20. Acceptance Criteria

* Institution Relationship Manager can initiate a cancellation application.  
* Required information and documents are validated before submission.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject the application with documented reasoning.  
* Approved cancellations remove the institution from the active Trustee/Auditor register.  
* Institution receives a cancellation e-certificate upon completion.  
* Institution receives notification of the outcome.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only the Institution Relationship Manager, or an authorized representative under a delegated permission scope, may submit this application. *(Proposed — A4 re-derivation; the source assigns this to the Account Trustee.)*
2. The institution must hold an existing approved standing as Account Trustee or Auditing Company to cancel it.  
3. Cancellation, return, and rejection decisions must carry documented reasoning.  
4. The public register of approved trustees and auditors is updated on completion to remove the institution's active standing.  
5. Every application receives a unique application reference number.  
6. All applications, approvals, cancellations, and notifications are permanently recorded in the audit trail.

## Open Questions

The following could not be closed by row 29 or by the answers doc, and are carried forward rather than dropped:

1. **Does cancellation carry a fee?** Row 29's workflow lists no payment step, unlike Service #1. Not clearly resolved either way by source or by the answers doc, which addresses fee *mechanism* (B1–B9) but not whether this specific service is chargeable at all.  
2. **What happens to obligations under an active Account Trustee standing at the point of cancellation** (e.g., trust accounts still under the institution's management)? Not addressed in source.  
3. **Exact fee amount, if one applies.** Client data — see `open-questions.md` B5.
