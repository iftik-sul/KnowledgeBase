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
  - "RERAN/modules/real-estate-service-companies/service-flows/service-08-appoint-financial-auditor.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-01-approval-renewal-account-trustee-auditing-company.md"
tags:
  - real-estate-service-companies
  - service-flow
  - jointly-owned-property
  - audit
---

# Service #11 – Approval / Renewal of Financial Auditing Company

**Service Category:** Jointly Owned Property Services

**Source row:** 56 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as transferring escrow account steps" (Service #5) — expanded in full below.

## 1. Service Overview

The **Approval / Renewal of Financial Auditing Company** service is how a financial auditing company obtains, or renews, RERA's approval to act as an auditor for jointly-owned-property matters within Group D — the institutional-standing counterpart, within this module, to Financial & Trust Institutions' Service #1 (Approval/Renewal of Account Trustee & Auditing Company).

> **Note on the parallel to Financial & Trust Institutions' Service #1.** That service pays *upfront*, following a 2026-08-15 client normalization from its originally-sourced post-decision timing. This row's own workflow ('same as transferring escrow account steps') sources **no payment step at all**, unlike that service — the two are structurally similar in purpose (institutional approval/renewal) but genuinely different in their sourced payment treatment. Do not assume this service should be normalized to match Financial & Trust Institutions' #1 without a separate client decision; it is not part of Open Question B4, which concerns Group D's own Licensing services #12–15.

## 2. Purpose

Grant or renew RERA's approval of a financial auditing company's standing to conduct audits of jointly-owned-property accounts and budgets, the credential that Services #9 and #10 rely on when a company names an audit office as its appointee.

## 3. Description

The auditing company signs up or logs in, fills in its institutional details, attaches supporting documents, and submits. RERA audits and sends an acceptance or rejection notice, followed by approval via email once accepted.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager*, though this is the one JOP service where the applicant is plausibly the auditing company itself rather than the property's own supervising company — the source does not clearly distinguish which entity type files this application. See Open Questions.

## 5. Prerequisites

* Registered RERAN Group D company account.
* For renewal: an existing approved standing that is active or nearing expiry.
* For new approval: the applicant meets RERA's eligibility criteria for financial-auditing standing. *(Proposed — the specific criteria are not enumerated in the source.)*

## 6. Required Information

### Company Information

* Company Legal Name
* Company Registration / Licence Reference
* Application Type — New Approval or Renewal

> **Proposed** — not itemized in source beyond "same as transferring escrow account steps." Needs client confirmation.

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

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 56).

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**8 business days.** Sourced from row 56 — the longest processing time of any Jointly Owned Property service, consistent with an institutional-approval decision rather than a routine filing.

## 12. Processing Workflow

Auditing Company User

Sign Up / Log In
↓
Select Application Type (New Approval / Renewal)
↓
Fill Company Information
↓
Attach Supporting Documents
↓
Submit Application Online

↓

RERA (Compliance & Escrow Auditor)

Audit Application
↓
Accept or Reject
↓
Send Acceptance / Rejection Notice
↓
*(if accepted)* Send Approval Notice via Email

*Channel: Official email of the Jointly Owned Property — sourced (row 56), unusual among Group D's institutional-standing pattern for using an email-based channel where most services use a portal.*

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

## 14. Possible Outcomes

* Company Approved as Financial Auditor (new)
* Company's Approval Renewed
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

Sourced (row 56): **none as a downloadable document** — the row names no issued document, unlike Financial & Trust Institutions' equivalent service, which issues recorded approval status. **Proposed**: an in-system approval status update, comparable to that service; needs client confirmation.

## 16. Related Services

* Service #8 – Appoint Financial Auditor
* Service #9 – Appoint Audit Office for JOP Financial Accounts
* Service #10 – Appoint Audit Office for JOP Budget Audit
* Financial & Trust Institutions Service #1 – Approval/Renewal of Account Trustee & Auditing Company *(cross-module: structurally comparable institutional-approval service, different fee treatment — see Service Overview note)*

## 17. UI Screens

Not yet built — Phase 4.

## 18. API Requirements

* Validate Applicant Eligibility
* Submit Approval / Renewal Application
* Retrieve Application Status
* Update Approved Auditing Company Register
* Send Notifications

## 19. Database Entities

* Company
* Financial Auditing Company Approval
* Application
* Service Request
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the four Group D roles at the applicant company can submit a new-approval or renewal application.
* Required information and documents are validated before submission.
* Application receives a unique application reference number.
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the applicant company's four Group D roles may submit this application — no role restriction.
2. This service carries no fee, at any point — genuinely sourced, not to be normalized to match Financial & Trust Institutions' comparable service without a separate client decision.
3. Approved standing is the credential Services #9 and #10 rely on when naming an audit office.
4. Every application receives a unique application reference number.
5. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Who the applicant actually is — the JOP-supervising company, or the auditing company itself seeking Group D standing — is not clearly distinguished in source.** This affects Section 4 (Who Can Apply) directly. Needs client confirmation.
2. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
3. **Whether an approval/renewal validity period applies** (comparable to Financial & Trust Institutions' proposed two-year term for its own Service #1) is not addressed in source.
4. **The absence of any output document is notable and may be a source gap rather than a genuine "nothing is issued" design** — flagged, not assumed either way.
