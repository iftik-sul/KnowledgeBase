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

# Service #2 – Approve Service Fees & Utilization Fees

**Service Category:** Jointly Owned Property Services

**Source row:** 47 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as registering real estate company (steps above)" — expanded in full below, per house style (see Service #1, and the pattern established across Group C's mortgage-lifecycle services).

## 1. Service Overview

The **Approve Service Fees & Utilization Fees** service obtains RERA's approval for the service charges and utilization fees an owners' association intends to levy against unit owners of a jointly-owned property. This is a regulatory approval of fees the *association charges its own members* — it is not a RERA service fee, and should not be confused with Section 8/9 below, which cover what (if anything) RERA itself charges for this application.

## 2. Purpose

Give owners' associations a regulated path to have their proposed service and utilization fee schedules approved before levying them against unit owners, so RERA can confirm charges are reasonable and properly disclosed.

## 3. Description

The company follows the same registration pattern as Service #1: sign up or log in to the Owner's system, fill in the proposed fee details, attach supporting documents, and submit online. RERA audits the application and sends an acceptance or rejection notice, followed by an approval notice via email once accepted.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager* (`open-questions.md` A1).

## 5. Prerequisites

* Registered RERAN Group D company account, with JOP administrative supervision already registered against the property (Service #1).
* Proposed service and utilization fee schedule available.
* Required supporting documents are available.

## 6. Required Information

### Property Reference

* Jointly-Owned Property Name / Reference

### Fee Schedule

* Proposed Service Fee Amount
* Proposed Utilization Fee Amount
* Basis of Calculation (e.g., per unit, per square metre)
* Effective Period

> **Proposed** — not itemized in source beyond "same as registering real estate company." The fields above are proposed by analogy with what a fee-approval application plainly needs; needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Proposed Fee Schedule Document
* Basis / Justification for the Proposed Fees
* Owners' Association Resolution Approving the Proposed Fees
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 47, by reference to row 46's pattern) — confirmed against `payments.md`'s Model 1, which applies to all 11 Jointly Owned Property services.

## 9. Payment Required

**No.**

No payment step exists at any point in the sourced workflow.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 47).

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**25 minutes.** Sourced from row 47.

## 12. Processing Workflow

Company User

Sign Up / Log In to Owner's System
↓
Select Registered JOP Property
↓
Fill Proposed Fee Details
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
↓
Data Available on Owner's System and Land Department Website

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

* Fee Schedule Approved
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

Sourced (row 47): **none as a downloadable document** — same pattern as Service #1, output is view-only data on the Owner's system and Land Department website, not an issued certificate.

## 16. Related Services

* Service #1 – Register Company for JOP Administrative Supervision
* Service #4 – Register Owners Association

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

* Services
* Approve Service Fees & Utilization Fees
* Property Reference
* Fee Schedule Details
* Document Upload
* Application Review
* Application Submitted
* Application Details

## 18. API Requirements

* Retrieve JOP Supervision Record
* Submit Fee Approval Application
* Retrieve Application Status
* Update Approved Fee Schedule
* Send Notifications

## 19. Database Entities

* Company
* Jointly Owned Property
* JOP Fee Schedule
* Application
* Service Request
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can submit this application, against a property with an existing JOP supervision registration (Service #1).
* Required information and documents are validated before submission.
* Application receives a unique application reference number.
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.
* Approved fee schedules are recorded against the JOP property.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may submit this application — no role restriction.
2. A JOP supervision registration (Service #1) must exist for the property before this service can be filed against it.
3. This service carries no fee, at any point.
4. Approval of a fee schedule is distinct from, and does not itself constitute, a RERA service fee for using the platform.
5. Every application receives a unique application reference number.
6. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced beyond the cross-reference to row 46's steps.** Needs client confirmation.
2. **Whether approved fee schedules require periodic re-approval** (e.g., annually) or remain valid indefinitely once approved. Not specified in source.
