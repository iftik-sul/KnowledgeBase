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
---

# Service #1 – Approval / Renewal of Account Trustee & Auditing Company

**Service Category:** Institutional Approval Services

**Source row:** 28 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Approval / Renewal of Account Trustee & Auditing Company** service is how an institution obtains, or renews, RERA's approval to act as an Account Trustee or Auditing Company under RERAN. That approval is the prerequisite for a Group B Account Trustee to manage developer escrow accounts, and for a Group C Auditing Bureau Officer to audit them independently. Without an approved standing, an institution cannot be provisioned into either capacity.

## 2. Purpose

Grant or renew RERA's approval of an institution's standing as a trustee or auditing partner, so that the platform, developers and other institutions can rely on that status wherever it is asserted.

## 3. Description

The institution's Institution Relationship Manager applies for new approval or renewal, submitting institution and eligibility information and supporting documents. RERA's Compliance & Escrow Auditor studies and audits the application. A new approval additionally requires the institution to attend and sign a partner agreement before it takes effect; a renewal does not. The institution pays the applicable fee, and RERA updates the Trust Account System and the public register of approved trustees and auditors.

## 4. Who Can Apply

### Applicant

* Institution Relationship Manager  
* Any other authorized representative of the institution, acting on its behalf *(no delegated scope required — see Business Rule 1)*

> **Proposed** — the source assigns this application to the **Account Trustee** as responsible role. `open-questions.md` (A4) re-derives ownership: the Institution Relationship Manager "maintains registration, renews trustee/auditor approvals" — exactly what this service does — while the Account Trustee is the *subject* of the approval, not a plausible applicant for its own not-yet-existing (or expiring) status. This document follows the A4 re-derivation. **Confidence: High**, per the answers doc.

## 5. Prerequisites

* Registered RERAN institution (Group C) account. *(Registration and onboarding are out of module scope; this service assumes the base institution account already exists.)*  
* Institution Relationship Manager has platform access under the institution's corporate account.  
* For renewal: an existing approved standing that is active or nearing expiry.  
* For new approval: the institution meets RERA's eligibility criteria for trustee/auditor status. *(Proposed — the specific criteria are not enumerated in the source. See Open Questions.)*

## 6. Required Information

### Institution Information

* Institution Legal Name  
* Institution Type (Account Trustee / Auditing Company)  
* Regulatory Registration / Licence Number  
* Contact Information

### Application Information

* Application Type — New Approval or Renewal  
* Existing Approval Reference Number *(renewal only)*

## 7. Required Documents

> **Proposed** — the source states only that the institution "applies" and documents are audited; it never enumerates them. The list below is proposed by analogy with the individual-user module's document patterns and what an institutional-standing application plainly needs.

* Certificate of Incorporation  
* Regulatory Operating Licence (e.g., Central Bank or applicable regulator)  
* Most Recent Audited Financial Statements  
* Professional Indemnity Insurance Certificate  
* Board Resolution Appointing the Authorized Representative  
* Government-issued Identification (Authorized Representative)  
* Existing Approval Certificate *(renewal only)*  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Proposed** — per `open-questions.md` B8, institutional approval fees are treated as **per approval term, with a two-year validity and a renewal fee at renewal**, since "approval / renewal" is only meaningful if approvals expire. The duration is a proposal; the fee amount is client data not available in source.

## 9. Payment Required

**Yes**

Paid directly by the institution, after RERA's approval decision and (for a new approval) after the partner agreement is signed — not before submission. This follows the platform's Lodge → Validate → Audit → **Pay** → Issue pipeline described in `payments.md`, and matches source row 28's sequencing, where "Payment of fees" is listed after the approval decision.

This service uses the **Institution Fee Payment** model (paid by the institution on approval of its own standing) — sourced, and unaffected by the 2026-08-14 payment-model correction. That correction retired the standing-account **Institution Account Debit** model previously used by the mortgage and finance-lease services (`open-questions.md` B1); it never applied to this service, which was never described as debited from a settlement account.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced: RERA "studies and audits application, decides approval or rejection."

> **Proposed** — unlike the mortgage and finance-lease workflows, source row 28 describes no internal institutional certification step for this service; RERA reviews the application directly. If the institution chooses to route preparation and internal sign-off through an internal certify-or-return step before submission — an unrestricted action any of its four Group C users may perform, not a scope — it may do so voluntarily, but this is not described in the source for this specific service and is not assumed here. **Corrected 2026-08-14** — previously described as "internal maker-checker on its corporate account (A1/D2)"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).

## 11. Expected Processing Time

**Waiting time: 29 business hours; Service delivery: 28 business hours.**

Sourced from row 28. Per `open-questions.md` A6, the waiting-time figure is read as the queue/counterparty portion and the delivery figure as RERA's own processing — a reading the answers doc flags as needing explicit client confirmation, since every Group C SLA carrying two numbers depends on it.

## 12. Processing Workflow

Institution Relationship Manager

Login  
↓  
Open Services  
↓  
Select "Approval / Renewal of Account Trustee & Auditing Company"  
↓  
Select Application Type (New Approval / Renewal)  
↓  
Enter Institution Information  
↓  
Upload Required Documents  
↓  
Submit Application

*Channel: Land Department website (Real Estate Developers Portal – Title Deed), Trust Account System, or email — all three are named in the source (row 28).*

↓

RERA

Study Application  
↓  
Audit Application  
↓  
Approve, Return, or Reject

↓

Institution Relationship Manager *(new approval only)*

Coordinate Attendance  
↓  
Sign Partner Agreement

↓

Institution Relationship Manager

Complete Payment

↓

RERA

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
Approved — Awaiting Payment  
↓  
Completed

### Additional Statuses

* Rejected  
* Withdrawn  
* Expired *(approved but unpaid for 30 calendar days — B3)*

> **Proposed** — this service does not carry the Group C `Pending Internal Certification` / `Returned by Certifier` extension (D1), because source row 28 describes no internal institutional certification step. If the institution enables an internal certify-or-return step on this workflow voluntarily, those two statuses would precede `Submitted`, per the platform-wide pattern in `services-overview.md`. **Corrected 2026-08-14** — previously described as enabling "maker-checker... voluntarily (A1/D2)"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).

## 14. Possible Outcomes

* Institution Approved as Account Trustee / Auditing Company (new)  
* Institution's Approval Renewed  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Approval Expired  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Approved Strategic Partner Status, recorded online in the Trust Account System and RERA's public register of approved trustees and auditors — sourced phrasing from row 28: *"Approving a strategic partner – online."*  
* Updated Approval Expiry Date *(renewal)*  
* Payment Receipt

> **Corrected 2026-08-14.** This note previously cited `open-questions.md` B9 for the conclusion that a payment receipt, not a "fee balance," is the correct artefact here. B9 is now superseded (see `open-questions.md`), and "fee balance" no longer describes any Group C artefact — there is no standing account left to produce one, for the mortgage and finance-lease services either. The conclusion for this service doesn't change: it was never account-debited and always issues a receipt. What's removed is the citation to a comparison ("not a fee balance, used by the account-debit services") that no longer describes anything real.

## 16. Related Services

* Service #2 — Cancellation of Account Trustee & Auditing Company  
* Service #18 — Contract Cancellation *(also owned by the Institution Relationship Manager)*
* Group B — Escrow services the Account Trustee performs once approved *(Proposed cross-module note; the Account Trustee's escrow queue is documented in `open-questions.md` A2 and the Group B module, not in this module)*

## 17. UI Screens

* Services  
* Approval / Renewal of Account Trustee & Auditing Company  
* Application Type Selection  
* Institution Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Agreement Signing *(new approval only)*  
* Approval / Renewal Confirmation

## 18. API Requirements

* Retrieve Institution Profile  
* Validate Institution Eligibility  
* Retrieve Existing Approval Status *(renewal)*  
* Upload Documents  
* Calculate Service Fee  
* Submit Approval / Renewal Application  
* Retrieve Application Status  
* Record Partner Agreement Signing *(new approval)*  
* Initiate Payment  
* Verify Payment  
* Update Approved Trustee / Auditor Register  
* Generate Approval Confirmation  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff *(no scope field — every staff member has identical system access; role is recorded per-action, not per-account, see Audit Log below)*  
* Application  
* Service Request  
* Document  
* Approval Record  
* Approval Expiry  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log *(captures the acting user and their role at time of action for every logged event, per [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle))*

## 20. Acceptance Criteria

* Institution Relationship Manager can initiate a new-approval or renewal application.  
* System distinguishes the new-approval flow (agreement signing) from the renewal flow.  
* Required information and documents are validated before submission.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject the application with documented reasoning.  
* Payment is required before the approval or renewal is finalized.  
* Approved Trustee/Auditor register and expiry date are updated upon completion.  
* Institution receives a payment receipt distinct from any settlement-account balance.  
* Institution receives notification of the outcome.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Typically the Institution Relationship Manager submits this application, though any authorized representative of the institution may act on its behalf — the platform does not gate this by a provisioned scope; the acting user and their role are recorded in the audit trail. **Corrected 2026-08-14** — previously required "an authorized representative under a delegated permission scope"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle). *(Proposed — A4 re-derivation; the source assigns this to the Account Trustee.)*
2. The institution must hold, or be seeking, approved standing as an Account Trustee or Auditing Company.  
3. A new-approval application requires attendance and execution of a partner agreement before completion; a renewal does not.  
4. Payment is required before the approval or renewal is finalized, paid directly by the institution rather than deducted from a standing settlement account.  
5. Approval, return, and rejection decisions must carry documented reasoning.  
6. Approved status and its expiry date are recorded in RERA's public register of approved trustees and auditors.  
7. An approval lapses to Expired if approved but left unpaid for 30 calendar days. *(B3, proposed duration.)*  
8. Every application receives a unique application reference number.  
9. All applications, approvals, renewals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

The following could not be closed by rows 28–45 or by the answers doc, and are carried forward rather than dropped:

1. **Eligibility criteria for new approval.** The source states RERA "studies and audits" the application but never lists what makes an institution eligible to become an approved trustee or auditor. Client data.  
2. **Specific approval/rejection criteria.** Beyond the platform-wide requirement for documented reasoning (FR-04, cited in `open-questions.md` A3), no service-specific decision criteria are sourced.  
3. **Exact fee amount.** Client data — see `open-questions.md` B5, the one question of 23 with no proposed answer.
