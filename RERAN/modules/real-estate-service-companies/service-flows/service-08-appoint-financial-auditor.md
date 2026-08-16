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
  - "RERAN/modules/real-estate-service-companies/service-flows/service-05-transfer-jop-escrow-account.md"
tags:
  - real-estate-service-companies
  - service-flow
  - jointly-owned-property
  - audit
---

# Service #8 – Appoint Financial Auditor

**Service Category:** Jointly Owned Property Services

**Source row:** 53 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as transferring escrow account steps" (Service #5) — expanded in full below.

## 1. Service Overview

The **Appoint Financial Auditor** service obtains RERA's approval to appoint a financial auditor with specific responsibilities over a jointly-owned property's finances — distinct from Services #9 and #10, which appoint an *audit office* for a defined scope of work (financial accounts, or budget) rather than an individual auditor with open-ended responsibilities.

## 2. Purpose

Give an owners' association a regulated path to appoint a financial auditor whose responsibilities are specifically defined, so RERA has a record of who holds financial oversight authority over the property's accounts.

## 3. Description

The company signs up or logs in, fills in the proposed auditor's details and defined responsibilities, attaches supporting documents, and submits. RERA audits and sends an acceptance or rejection notice, followed by approval via email once accepted.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager* (`open-questions.md` A1).

## 5. Prerequisites

* Registered RERAN Group D company account, with JOP administrative supervision registered against the property (Service #1).
* The proposed financial auditor is identified.
* Required supporting documents are available.

## 6. Required Information

### Property Reference

* Jointly-Owned Property Name / Reference

### Auditor Information

* Auditor Name / Firm
* Professional Registration / Licence Reference
* Defined Scope of Responsibilities
* Term of Appointment

> **Proposed** — not itemized in source beyond "same as transferring escrow account steps." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Owners' Association Resolution Approving the Appointment
* Auditor's Professional Registration Evidence
* Proposed Terms of Engagement
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 53) — confirmed against `payments.md`'s Model 1.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 53).

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**1 business day.** Sourced from row 53.

## 12. Processing Workflow

Company User

Sign Up / Log In to Owner System
↓
Select Registered JOP Property
↓
Fill Auditor Details and Defined Responsibilities
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

* Financial Auditor Successfully Appointed
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

Sourced (row 53): **none as a downloadable document** — output is data available via the Owner system.

## 16. Related Services

* Service #9 – Appoint Audit Office for JOP Financial Accounts
* Service #10 – Appoint Audit Office for JOP Budget Audit
* Service #11 – Approval / Renewal of Financial Auditing Company

## 17. UI Screens

Not yet built — Phase 4.

## 18. API Requirements

* Retrieve JOP Property Record
* Submit Auditor Appointment Application
* Retrieve Application Status
* Update Appointed Auditor Register
* Send Notifications

## 19. Database Entities

* Company
* Jointly Owned Property
* Appointed Financial Auditor
* Application
* Service Request
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can submit this application, against a property with an existing JOP supervision registration.
* Required information and documents are validated before submission.
* Application receives a unique application reference number.
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.
* Approved appointments update the property's appointed-auditor register.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may submit this application — no role restriction.
2. A JOP supervision registration (Service #1) must exist for the property.
3. This service carries no fee, at any point.
4. The appointed auditor's responsibilities must be specifically defined as part of the application — a general or open-ended appointment is not what this service sources.
5. Every application receives a unique application reference number.
6. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
2. **The functional distinction between this service and Services #9/#10** (an individual auditor with defined responsibilities, vs. an audit office for a specific accounts or budget audit) is inferred from the rows' differing titles rather than an explicit source statement distinguishing them. Needs client confirmation that this reading is correct.
