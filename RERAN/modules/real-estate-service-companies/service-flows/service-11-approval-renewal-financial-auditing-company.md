---
project: RERAN
module: real-estate-service-companies
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
  - "RERAN/modules/real-estate-service-companies/service-flows/service-06-request-escrow-account-closure.md"
  - "RERAN/modules/real-estate-service-companies/service-flows/service-19-accreditation-training-entities.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-01-approval-renewal-account-trustee-auditing-company.md"
tags:
  - real-estate-service-companies
  - service-flow
  - jointly-owned-property
  - audit
---

# Service #11 – Approval / Renewal of Financial Auditing Company

**Service Category:** Jointly Owned Property Services

**Source row:** 56 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as transferring escrow account steps" (Service #5) — for the general audit/approval shape, but names its own distinct channel (see below).

## 1. Service Overview

The **Approval / Renewal of Financial Auditing Company** service is how a financial auditing company obtains, or renews, RERA's approval to act as an auditor for jointly-owned-property matters within Group D — the institutional-standing counterpart, within this module, to Financial & Trust Institutions' Service #1 (Approval/Renewal of Account Trustee & Auditing Company).

> **Corrected 2026-08-16 — Section 12 rewritten to match the sourced email-only channel.** Row 56's own Channel column names only "Official email of the Jointly Owned Property" — the same email-only pattern Services #6 and #19 use, not the portal-based pattern most of the "same as transferring escrow account steps" cluster (#7–#10) follows. This file previously carried a portal-style "Sign Up / Log In" workflow inherited uncorrected from the Service #5 cross-reference it was originally derived from — found during the 2026-08-16 Phase 6 audit, and corrected here. The row's underlying audit/approval shape (submit, RERA reviews, accepts or rejects, sends notice) is still "same as Service #5" in substance; only the *channel* differs, and that channel difference is now reflected throughout this file.

> **Note on the parallel to Financial & Trust Institutions' Service #1.** That service pays *upfront*, following a 2026-08-15 client normalization from its originally-sourced post-decision timing. This row's own workflow sources **no payment step at all**, unlike that service — the two are structurally similar in purpose (institutional approval/renewal) but genuinely different in their sourced payment treatment. Do not assume this service should be normalized to match Financial & Trust Institutions' #1 without a separate client decision; it is not part of Open Question B4, which concerns Group D's own Licensing services #12–15.

## 2. Purpose

Grant or renew RERA's approval of a financial auditing company's standing to conduct audits of jointly-owned-property accounts and budgets, the credential that Services #9 and #10 rely on when a company names an audit office as its appointee.

## 3. Description

The auditing company completes its institutional details, attaches supporting documents, and sends the application via email to the Jointly Owned Property's official address. RERA audits the application and sends an acceptance or rejection notice, followed by approval via email once accepted.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager*, though this is the one JOP service where the applicant is plausibly the auditing company itself rather than the property's own supervising company — the source does not clearly distinguish which entity type files this application. See Open Questions.

## 5. Prerequisites

* Registered RERAN Group D company account.
* For renewal: an existing approved standing that is active or nearing expiry.
* For new approval: the applicant meets RERA's eligibility criteria for financial-auditing standing. *(Proposed — the specific criteria are not enumerated in the source.)*
* The application form itself is completed and ready to send. *(Proposed, matching the pattern sourced for Service #6, which also names a form as the artefact submitted — needs client confirmation whether an equivalent standard form exists for this service.)*

## 6. Required Information

### Company Information

* Company Legal Name
* Company Registration / Licence Reference
* Application Type — New Approval or Renewal

> **Proposed** — not itemized in source beyond the cross-reference to Service #5's general steps. Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Certificate of Incorporation
* Professional Registration / Licence Evidence
* Existing Approval Certificate *(renewal only)*
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 56) — no payment step appears anywhere in the sourced workflow. Confirmed against `payments.md`'s Model 1.

## 9. Payment Required

**No.**

Genuinely sourced as free — unlike Financial & Trust Institutions' structurally similar Service #1, which does charge (upfront, post-normalization). See the Service Overview note above; this difference is sourced, not an inconsistency to reconcile.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 56), though the row's own workflow text does not describe an audit step explicitly the way most portal-based Group D rows do. **Proposed**: RERA reviews the emailed application and responds with acceptance, rejection, or a query, following the same general audit pattern inferred for Service #6, since the source's approver column names the same role that reviews every other service in this module.

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**8 business days.** Sourced from row 56 — the longest processing time of any Jointly Owned Property service, consistent with an institutional-approval decision rather than a routine filing.

## 12. Processing Workflow

**Corrected 2026-08-16 — rewritten to an email-based workflow, matching Services #6 and #19's sourced channel, replacing the previously-inherited portal-style sequence.**

Auditing Company User

Complete Institutional Details (Application Type, Company Information)
↓
Attach Supporting Documents
↓
Send via Email to the Jointly Owned Property's Official Email

↓

RERA (Compliance & Escrow Auditor)

*(review process not detailed in source — proposed to follow the module's general audit pattern, matching Service #6)*
↓
Review Application
↓
Accept or Reject
↓
Send Acceptance / Rejection Notice
↓
*(if accepted)* Send Approval Notice via Email

*Channel: Email — sourced (row 56), the third of three email-only Group D services alongside Services #6 and #19.*

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

**Corrected 2026-08-16** — unchanged in substance from the previous version; this status flow was already a reasonable default adopted from the platform-wide core rather than tied to the (now-corrected) portal workflow text, so no further change was needed here beyond the workflow correction above.

## 14. Possible Outcomes

* Company Approved as Financial Auditor (new)
* Company's Approval Renewed
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

Sourced (row 56): **none as a downloadable document** — the row names no issued document, unlike Financial & Trust Institutions' equivalent service, which issues recorded approval status. **Proposed**: an in-system approval status update, comparable to that service; needs client confirmation.

## 16. Related Services

* Service #6 – Request No-Objection Letter to Close Escrow Account *(cross-reference corrected 2026-08-16 — the actual channel match, replacing the previous Service #5 cross-reference, which shares this service's audit shape but not its channel)*
* Service #8 – Appoint Financial Auditor
* Service #9 – Appoint Audit Office for JOP Financial Accounts
* Service #10 – Appoint Audit Office for JOP Budget Audit
* Financial & Trust Institutions Service #1 – Approval/Renewal of Account Trustee & Auditing Company *(cross-module: structurally comparable institutional-approval service, different fee treatment — see Service Overview note)*

## 17. UI Screens

**Corrected 2026-08-16 — firmed up now that Section 12's channel inconsistency is resolved.** Given the sourced email-only channel, this service does not use a portal wizard, matching Services #6 and #19's treatment:

* Services
* Approval / Renewal of Financial Auditing Company — static instructional screen directing the user to complete and email the application to the Jointly Owned Property's official address

## 18. API Requirements

Not applicable in the same sense as portal-based services — the source specifies an email workflow, matching Service #6. **Proposed**: if a portal record of the request and its outcome is desired, a minimal request-tracking record would need: Log Emailed Request, Update Request Status, Retrieve Request History. Needs client confirmation of whether this is in scope.

## 19. Database Entities

* Company
* Financial Auditing Company Approval
* Application
* Service Request
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the applicant company's four Group D roles can submit a new-approval or renewal application via the email channel.
* RERA reviews the emailed application and responds with acceptance, rejection, or a query.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log, to the extent the email channel allows.

## 21. Business Rules

1. Any of the applicant company's four Group D roles may submit this application — no role restriction.
2. This service is submitted via email — the only channel sourced, no portal path described. **Corrected 2026-08-16** — previously implied a portal path inherited from Service #5's workflow; that implication is retired.
3. This service carries no fee, at any point — genuinely sourced, not to be normalized to match Financial & Trust Institutions' comparable service without a separate client decision.
4. Approved standing is the credential Services #9 and #10 rely on when naming an audit office.
5. Every application receives a unique application reference number.
6. All submissions, approvals, and notifications are permanently recorded in the audit trail, to the extent the email channel allows.

## Open Questions

1. ~~Section 12's workflow describes portal "Sign Up / Log In" language that contradicts row 56's own sourced email-only channel.~~ **Resolved 2026-08-16** — Section 12 rewritten to an email-based workflow, matching Services #6 and #19.
2. **Who the applicant actually is — the JOP-supervising company, or the auditing company itself seeking Group D standing — is not clearly distinguished in source.** This affects Section 4 (Who Can Apply) directly. Needs client confirmation.
3. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
4. **Whether an approval/renewal validity period applies** (comparable to Financial & Trust Institutions' proposed two-year term for its own Service #1) is not addressed in source.
5. **The absence of any output document is notable and may be a source gap rather than a genuine "nothing is issued" design** — flagged, not assumed either way.
6. **Whether a standard application form exists for this service**, comparable to Service #6's "Land-Department-approved application form," is not addressed in source — proposed by analogy in Section 5, not confirmed.
