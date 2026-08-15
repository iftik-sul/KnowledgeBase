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
---
# Service #1 – Approval / Renewal of Account Trustee & Auditing Company

**Service Category:** Institutional Approval Services

**Source row:** 28 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Approval / Renewal of Account Trustee & Auditing Company** service is how an institution obtains, or renews, RERA's approval to act as an Account Trustee or Auditing Company under RERAN. That approval is the prerequisite for a Group B Account Trustee to manage developer escrow accounts, and for a Group C Auditing Bureau Officer to audit them independently. Without an approved standing, an institution cannot be provisioned into either capacity.

## 2. Purpose

Grant or renew RERA's approval of an institution's standing as a trustee or auditing partner, so that the platform, developers and other institutions can rely on that status wherever it is asserted.

## 3. Description

An institution user applies for new approval or renewal, submitting institution and eligibility information and supporting documents, and pays the applicable fee upfront via the shared platform payment gateway before the application is lodged. RERA's Compliance & Escrow Auditor studies and audits the application. A new approval additionally requires the institution to attend and sign a partner agreement before it takes effect, once RERA has approved; a renewal does not. RERA updates the Trust Account System and the public register of approved trustees and auditors. **Corrected 2026-08-15** — payment previously happened after RERA's decision (and, for a new approval, after the partner agreement was signed); the client has since decided this service now pays upfront instead, merging into the same model as Services #3–#11 (`open-questions.md` B11). The partner agreement itself is unaffected — it remains a post-decision step.

## 4. Who Can Apply

### Applicant

* Any of the institution's four Group C roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail

> **Confirmed 2026-08-15** — previously proposed that the Institution Relationship Manager was the correct owner (an A4 re-derivation against the source, which assigns this application to the Account Trustee). `open-questions.md` A4 now resolves the underlying ownership question altogether: no service is role-specific, so there is no per-role assignment to re-derive. The IRM "maintains registration, renews trustee/auditor approvals" and so is typically who submits this in practice, but any of the four roles may do so.

## 5. Prerequisites

* Registered RERAN institution (Group C) account. *(Registration and onboarding are out of module scope; this service assumes the base institution account already exists.)*  
* At least one user has platform access under the institution's corporate account.  
* For renewal: an existing approved standing that is active or nearing expiry.  
* For new approval: the institution meets RERA's eligibility criteria for trustee/auditor status. *(Proposed — the specific criteria are not enumerated in the source. See Open Questions.)*  
* Payment has been completed via the shared platform payment gateway before the application is lodged. *(Added 2026-08-15 — `open-questions.md` B11.)*

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

> **Proposed** — per `open-questions.md` B8, institutional approval fees are treated as **per approval term, with a two-year validity and a renewal fee at renewal**, since "approval / renewal" is only meaningful if approvals expire. **Confirmed 2026-08-15** — the renewing structure itself is now client-confirmed (B8); the two-year duration remains a proposal. The fee amount is client data not available in source.

## 9. Payment Required

**Yes**

Paid upfront by the institution via the shared platform payment gateway, before the application is lodged — not after RERA's decision. **Corrected 2026-08-15** — previously paid directly by the institution after RERA's approval decision and (for a new approval) after the partner agreement was signed, following the platform's Lodge → Validate → Audit → **Pay** → Issue pipeline and matching source row 28's sequencing. The client has since decided this service now follows the same upfront-checkout pattern as Services #3–#11 (`open-questions.md` B11), retiring the **Institution Fee Payment** model as a distinct category. This is a genuinely new decision, not a re-derivation — row 28's post-decision sequencing was correctly read the first time; the client has decided to build differently from what the source describes.

The partner agreement required for a new approval (sourced, row 28) is unaffected: it remains a post-audit-decision step, independent of when payment happens.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced: RERA "studies and audits application, decides approval or rejection."

> **Proposed** — unlike the mortgage and finance-lease workflows, source row 28 describes no internal institutional certification step for this service; RERA reviews the application directly. If the institution chooses to route preparation and internal sign-off through an internal certify-or-return step before submission — an unrestricted action any of its four Group C users may perform, not a scope — it may do so voluntarily, but this is not described in the source for this specific service and is not assumed here. **Corrected 2026-08-14** — previously described as "internal maker-checker on its corporate account (A1/D2)"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).

## 11. Expected Processing Time

**Waiting time: 29 business hours; Service delivery: 28 business hours.**

Sourced from row 28. Per `open-questions.md` A6, the waiting-time figure is read as the queue/counterparty portion and the delivery figure as RERA's own processing. **Confirmed 2026-08-15 (client decision)** — this two-number reading is correct; no new SLA figure is needed.

## 12. Processing Workflow

Institution User

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
Pay via Shared Platform Gateway  
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

Institution User *(new approval only)*

Coordinate Attendance  
↓  
Sign Partner Agreement

↓

RERA

Update Trust Account System  
↓  
Update Public Register of Approved Trustees & Auditors  
↓  
Notify Institution

**Corrected 2026-08-15** — the payment step ("Pay via Shared Platform Gateway") previously sat after RERA's approval decision and the partner agreement, as "Complete Payment." It now sits before "Submit Application," matching Services #3–#11's checkout-before-lodging pattern (`open-questions.md` B11). The partner agreement step for new approvals is otherwise unchanged in sequence — it still follows RERA's decision.

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
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

* Payment Failed *(retryable, pre-lodging — see [payments.md](../payments.md))*  
* Rejected  
* Withdrawn

**Corrected 2026-08-15 — `Approved — Awaiting Payment` and `Expired` removed; `Payment Pending` / `Payment Successful` added before `Submitted`.** This service previously carried `Approved — Awaiting Payment` and an `Expired` status for approvals left unpaid for 30 calendar days (B3), matching the old post-decision payment model. With payment now happening before lodging (`open-questions.md` B11), nothing is ever approved while still awaiting payment, and B3's unsettled-after-approval scenario can no longer occur — the same reasoning already applied to Services #3–#11 when their payment model was corrected on 2026-08-14. B3 itself was not revisited by either correction and remains as written in `open-questions.md`.

> **Proposed** — this service still does not carry the Group C `Pending Internal Certification` / `Returned by Certifier` extension (D1), because source row 28 describes no internal institutional certification step; this is unaffected by the payment-timing correction. If the institution enables an internal certify-or-return step on this workflow voluntarily, those two statuses would precede `Submitted`, per the platform-wide pattern in `services-overview.md`.

## 14. Possible Outcomes

* Institution Approved as Account Trustee / Auditing Company (new)  
* Institution's Approval Renewed  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

**Corrected 2026-08-15** — "Approval Expired" is removed as a possible outcome, for the same reason the `Expired` status is removed from Section 13: there is no longer a scenario where an approval can lapse unpaid, since payment happens before lodging.

## 15. Output

Upon successful completion, the system generates:

* Approved Strategic Partner Status, recorded online in the Trust Account System and RERA's public register of approved trustees and auditors — sourced phrasing from row 28: *"Approving a strategic partner – online."*  
* Updated Approval Expiry Date *(renewal)*  
* Payment Receipt — proof the fee settled, issued at checkout before the application was lodged. **Corrected 2026-08-15** — previously issued at completion, following the post-decision payment model; now issued at checkout, matching Services #3–#11.

> **Corrected 2026-08-14.** This note previously cited `open-questions.md` B9 for the conclusion that a payment receipt, not a "fee balance," is the correct artefact here. B9 is now superseded (see `open-questions.md`), and "fee balance" no longer describes any Group C artefact — there is no standing account left to produce one, for the mortgage and finance-lease services either. The conclusion for this service doesn't change: it was never account-debited and always issues a receipt. What's removed is the citation to a comparison ("not a fee balance, used by the account-debit services") that no longer describes anything real.

## 16. Related Services

* Service #2 — Cancellation of Account Trustee & Auditing Company  
* Service #18 — Contract Cancellation
* Group B — Escrow services the Account Trustee performs once approved *(Proposed cross-module note; the Account Trustee's escrow queue is documented in `open-questions.md` A2 and the Group B module, not in this module)*

**Corrected 2026-08-15** — the "(also owned by the Institution Relationship Manager)" note previously attached to Service #18 is removed. Per `open-questions.md` A4, no service — including this one or Service #18 — is owned by a particular role.

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
* Initiate Payment  
* Verify Payment  
* Submit Approval / Renewal Application  
* Retrieve Application Status  
* Record Partner Agreement Signing *(new approval)*  
* Update Approved Trustee / Auditor Register  
* Generate Approval Confirmation  
* Send Notifications

**Corrected 2026-08-15** — "Initiate Payment" and "Verify Payment" moved earlier in this list, ahead of "Submit Approval / Renewal Application," to match the corrected upfront-payment sequence. No API was added or removed, only reordered to reflect Section 12.

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

* Any of the institution's four Group C roles can initiate a new-approval or renewal application.  
* System distinguishes the new-approval flow (agreement signing) from the renewal flow.  
* Required information and documents are validated before submission.  
* Fee is paid via the shared platform payment gateway before the application is lodged. *(Corrected 2026-08-15 — previously "before the approval or renewal is finalized," i.e. post-decision; see `open-questions.md` B11.)*  
* An application cannot be lodged or submitted for audit until payment succeeds. *(Added 2026-08-15, matching Services #3–#11's equivalent criterion.)*  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject the application with documented reasoning.  
* Approved Trustee/Auditor register and expiry date are updated upon completion.  
* Institution receives a payment receipt at checkout, before lodging.  
* Institution receives notification of the outcome.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Typically the Institution Relationship Manager submits this application, though any of the institution's four Group C roles may act on its behalf — the platform does not gate this by role or a provisioned scope; the acting user and their role are recorded in the audit trail. **Corrected 2026-08-14** — previously required "an authorized representative under a delegated permission scope"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle). **Confirmed 2026-08-15** — previously flagged as a contested A4 re-derivation against the source's Account Trustee assignment; `open-questions.md` A4 now resolves that no service is role-specific, so there is nothing left to re-derive.  
2. The institution must hold, or be seeking, approved standing as an Account Trustee or Auditing Company.  
3. A new-approval application requires attendance and execution of a partner agreement before completion; a renewal does not.  
4. Payment is made via the shared platform payment gateway, upfront, before the application can be lodged — not deducted from a standing settlement account, and not collected after approval. **Corrected 2026-08-15** — previously "required before the approval or renewal is finalized, paid directly by the institution rather than deducted from a standing settlement account," matching the post-decision model; `open-questions.md` B11 moves this to upfront, before lodging, the same as Services #3–#11.  
5. Approval, return, and rejection decisions must carry documented reasoning.  
6. Approved status and its expiry date are recorded in RERA's public register of approved trustees and auditors.  
7. Every application receives a unique application reference number.  
8. All applications, approvals, renewals, payments, and notifications are permanently recorded in the audit trail.

**Corrected 2026-08-15** — the previous rule 7 ("An approval lapses to Expired if approved but left unpaid for 30 calendar days," B3, proposed duration) is removed. With payment happening before lodging, there is no post-approval unpaid state to lapse from — the same reasoning already applied when Services #3–#11's business rules were corrected on 2026-08-14. B3 itself was not revisited by this correction and remains as written in `open-questions.md`. Rules renumbered accordingly.

## Open Questions

The following could not be closed by rows 28–45 or by the answers doc, and are carried forward rather than dropped:

1. **Eligibility criteria for new approval.** The source states RERA "studies and audits" the application but never lists what makes an institution eligible to become an approved trustee or auditor. Client data.  
2. **Specific approval/rejection criteria.** Beyond the platform-wide requirement for documented reasoning (FR-04, cited in `open-questions.md` A3), no service-specific decision criteria are sourced.  
3. **Exact fee amount.** Client data — see `open-questions.md` B5.  
4. **What happens to the fee on a rejected application** (refund, forfeiture, or otherwise). Not addressed by any source document or by the payment-model correction itself; genuinely new as of the 2026-08-15 upfront-payment decision, applying here the same way it already applies to Services #3–#11 — see `payments.md`'s To Confirm — Summary.
