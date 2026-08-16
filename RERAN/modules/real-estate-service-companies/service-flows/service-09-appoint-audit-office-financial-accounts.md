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
tags:
  - real-estate-service-companies
  - service-flow
  - jointly-owned-property
  - audit
---

# Service #9 – Appoint Audit Office for JOP Financial Accounts

**Service Category:** Jointly Owned Property Services

**Source row:** 54 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as transferring escrow account steps" (Service #5) — expanded in full below.

## 1. Service Overview

The **Appoint Audit Office for JOP Financial Accounts** service obtains RERA's approval to appoint an audit office specifically to audit a jointly-owned property's financial accounts — a scoped appointment, distinct from Service #8's individually-defined-responsibilities auditor and Service #10's budget-specific audit appointment.

## 2. Purpose

Give an owners' association a regulated path to appoint an audit office for the specific purpose of auditing the property's financial accounts, ensuring RERA has a record of which firm is conducting that audit.

## 3. Description

The company signs up or logs in, fills in the proposed audit office's details, attaches supporting documents, and submits. RERA audits and sends an acceptance or rejection notice, followed by approval via email once accepted.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager* (`open-questions.md` A1).

## 5. Prerequisites

* Registered RERAN Group D company account, with JOP administrative supervision registered against the property (Service #1).
* The proposed audit office is identified.
* Required supporting documents are available.

## 6. Required Information

### Property Reference

* Jointly-Owned Property Name / Reference

### Audit Office Information

* Audit Office Name / Firm
* Professional Registration / Licence Reference
* Scope: Financial Accounts Audit
* Audit Period

> **Proposed** — not itemized in source beyond "same as transferring escrow account steps." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Owners' Association Resolution Approving the Appointment
* Audit Office's Professional Registration Evidence
* Proposed Terms of Engagement
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 54) — confirmed against `payments.md`'s Model 1.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 54).

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**1 business day.** Sourced from row 54.

## 12. Processing Workflow

Company User

Sign Up / Log In to Owner System
↓
Select Registered JOP Property
↓
Fill Audit Office Details and Scope
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

* Audit Office Successfully Appointed
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

Sourced (row 54): **none as a downloadable document** — output is data available via the Owner system.

## 16. Related Services

* Service #8 – Appoint Financial Auditor
* Service #10 – Appoint Audit Office for JOP Budget Audit
* Service #11 – Approval / Renewal of Financial Auditing Company

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

* Services
* Appoint Audit Office for JOP Financial Accounts
* Property Reference
* Audit Office Information
* Document Upload
* Application Review
* Application Submitted
* Application Details

## 18. API Requirements

* Retrieve JOP Property Record
* Submit Audit Office Appointment Application
* Retrieve Application Status
* Update Appointed Audit Office Register
* Send Notifications

## 19. Database Entities

* Company
* Jointly Owned Property
* Appointed Audit Office
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
* Approved appointments update the property's appointed-audit-office register.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may submit this application — no role restriction.
2. A JOP supervision registration (Service #1) must exist for the property.
3. This service carries no fee, at any point.
4. The appointment's scope is specifically the financial accounts audit — distinct from Service #10's budget-audit scope.
5. Every application receives a unique application reference number.
6. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
2. **Whether this appointment recurs annually or is a one-time appointment per audit cycle** is not specified in source.
