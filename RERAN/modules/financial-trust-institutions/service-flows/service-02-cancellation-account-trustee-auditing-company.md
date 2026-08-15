---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
updated: 2026-08-15
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

An institution user submits a cancellation application. RERA's Compliance & Escrow Auditor studies and audits the request, then issues a cancellation e-certificate by email and updates the Trust Account System and public register to reflect the cancellation.

## 4. Who Can Apply

### Applicant

* Any of the institution's four Group C roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail

> **Confirmed 2026-08-15** — as with Service #1, the source assigns this application to the **Account Trustee** as responsible role. `open-questions.md` A4 no longer re-derives ownership to a different single role (previously the Institution Relationship Manager) — it resolves the underlying question altogether: no service is role-specific, so there is no per-role assignment to re-derive.

## 5. Prerequisites

* Registered RERAN institution (Group C) account.  
* At least one user has platform access under the institution's corporate account.  
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

Sourced from row 29 — identical figures to Service #1. Per `open-questions.md` A6, waiting time is read as the queue/counterparty portion and delivery time as RERA's own processing. **Confirmed 2026-08-15 (client decision)** — this two-number reading is correct; no new SLA figure is needed. *(Corrected 2026-08-15 — previously "needs explicit client confirmation and remains genuinely open"; the client has since confirmed this reading directly, resolving it, the same as Service #1.)*

## 12. Processing Workflow

Institution User

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
* Service #18 — Contract Cancellation

**Corrected 2026-08-15** — the "(also owned by the Institution Relationship Manager)" note previously attached to Service #18 is removed. Per `open-questions.md` A4, no service — including this one or Service #18 — is owned by a particular role.

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

* Any of the institution's four Group C roles can initiate a cancellation application.  
* Required information and documents are validated before submission.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject the application with documented reasoning.  
* Approved cancellations remove the institution from the active Trustee/Auditor register.  
* Institution receives a cancellation e-certificate upon completion.  
* Institution receives notification of the outcome.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Typically the Institution Relationship Manager submits this application, though any of the institution's four Group C roles may act on its behalf — the platform does not gate this by role or a provisioned scope; the acting user and their role are recorded in the audit trail. **Corrected 2026-08-14** — previously required "an authorized representative under a delegated permission scope"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle). **Confirmed 2026-08-15** — previously flagged as a contested A4 re-derivation against the source's Account Trustee assignment; `open-questions.md` A4 now resolves that no service is role-specific, so there is nothing left to re-derive.  
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
