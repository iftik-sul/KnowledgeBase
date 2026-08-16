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
  - "RERAN/modules/real-estate-service-companies/service-flows/service-01-register-company-jop-supervision.md"
tags:
  - real-estate-service-companies
  - service-flow
  - jointly-owned-property
---

# Service #3 – Register JOP-Competent Employees

**Service Category:** Jointly Owned Property Services

**Source row:** 48 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as registering real estate company" — expanded in full below.

## 1. Service Overview

The **Register JOP-Competent Employees** service records the company's staff who hold professional competence in the management of jointly-owned properties, giving RERA a registry of who is qualified to act on the company's behalf for JOP administration.

## 2. Purpose

Establish which of the company's employees are recognized by RERA as professionally competent to manage jointly-owned property matters, so the company's staffing meets whatever competence standard RERA sets for this work.

## 3. Description

The company follows the same registration pattern as Service #1: sign up or log in to the Owner's system, fill in the employee's details, attach supporting documents evidencing competence, and submit online. RERA audits and, on acceptance, issues data viewable via the Owner's system and an online login card.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager* (`open-questions.md` A1).

## 5. Prerequisites

* Registered RERAN Group D company account.
* The employee to be registered holds evidence of professional competence in JOP management.
* Required supporting documents are available.

## 6. Required Information

### Employee Information

* Full Name
* National Identification Number (NIN)
* Contact Information
* Position / Role at the Company

### Competence Information

* Qualification / Certification Held
* Issuing Body
* Date of Qualification

> **Proposed** — not itemized in source beyond "same as registering real estate company." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Evidence of Professional Qualification
* Government-issued Identification (Employee)
* Employment Confirmation Letter
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 48) — confirmed against `payments.md`'s Model 1.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 48).

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**5 minutes.** Sourced from row 48.

## 12. Processing Workflow

Company User

Sign Up / Log In to Owner's System
↓
Fill Employee & Competence Details
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
*(if accepted)* Employee Data Available via Owner's System and Online Login Card

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

* Employee Successfully Registered as JOP-Competent
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

Sourced (row 48): **an online login card**, plus data viewable via the Owner's system — unlike Services #1 and #2, this row explicitly names a card as an artefact, not purely view-only data.

## 16. Related Services

* Service #1 – Register Company for JOP Administrative Supervision
* Service #14 – Issue Professional Practice Card *(a comparable card-issuance service, different domain)*

## 17. UI Screens

Not yet built — Phase 4.

## 18. API Requirements

* Validate Company Account
* Submit Employee Competence Registration
* Retrieve Application Status
* Generate Online Login Card
* Update JOP Competent-Employee Register
* Send Notifications

## 19. Database Entities

* Company
* Employee
* JOP Competence Record
* Application
* Service Request
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can register an employee's JOP competence.
* Required information and documents are validated before submission.
* Application receives a unique application reference number.
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.
* Approved registrations issue an online login card and update the register.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may submit this registration — no role restriction.
2. This service carries no fee, at any point.
3. An approved registration issues the employee an online login card, distinct from a downloadable certificate.
4. Every application receives a unique application reference number.
5. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information, document lists, and the specific competence standard RERA applies are proposed, not sourced.** Needs client confirmation.
2. **Whether this registration expires or requires renewal**, comparable to a professional practice card (Service #15). Not specified in source.
