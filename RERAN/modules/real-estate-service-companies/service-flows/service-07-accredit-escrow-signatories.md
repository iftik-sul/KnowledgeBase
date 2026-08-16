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
  - escrow
---

# Service #7 – Accredit Escrow Account Signatories

**Service Category:** Jointly Owned Property Services

**Source row:** 52 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as transferring escrow account steps" (Service #5) — expanded in full below.

## 1. Service Overview

The **Accredit Escrow Account Signatories** service obtains RERA's approval for the individuals authorized to sign on a jointly-owned property's escrow account, giving the account's banking relationship a regulated list of who may authorize transactions against it.

> **Escrow mechanism** — same finding as Service #5 (`open-questions.md` A3): no Account Trustee step is described.

## 2. Purpose

Ensure that only RERA-accredited individuals can sign on a jointly-owned property's escrow account, closing off a fraud surface where unaccredited signatories could authorize improper withdrawals.

## 3. Description

The company signs up or logs in to the Regulations Department system, fills in the proposed signatories' details, attaches supporting documents, and submits. RERA audits and sends an acceptance or rejection notice, followed by approval via email once accepted.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager* (`open-questions.md` A1).

## 5. Prerequisites

* Registered RERAN Group D company account, with JOP administrative supervision registered against the property (Service #1).
* An existing escrow account for the jointly-owned property.
* The proposed signatories are identified and available to be registered.

## 6. Required Information

### Property & Account Reference

* Jointly-Owned Property Name / Reference
* Escrow Account Details

### Signatory Information (per proposed signatory)

* Full Name
* National Identification Number (NIN)
* Position / Authority Basis
* Signature Specimen

> **Proposed** — not itemized in source beyond "same as transferring escrow account steps." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Owners' Association Resolution Naming the Signatories
* Government-issued Identification (Each Signatory)
* Signature Specimen Cards
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 52) — confirmed against `payments.md`'s Model 1.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 52). No Account Trustee step is described.

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**1 business day.** Sourced from row 52.

## 12. Processing Workflow

Company User

Sign Up / Log In *(Regulations Department, Owner's system)*
↓
Select Registered JOP Property
↓
Fill Signatory Details
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

* Signatories Successfully Accredited
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

Sourced (row 52): **none as a downloadable document** — output is data available via the Regulations Department system, matching the same pattern as Service #5.

## 16. Related Services

* Service #5 – Transfer JOP Escrow Account
* Service #6 – Request No-Objection Letter to Close Escrow Account
* Service #8 – Appoint Financial Auditor

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

* Services
* Accredit Escrow Account Signatories
* Property & Account Reference
* Signatory Information (repeatable group — Pattern B, one entry per proposed signatory)
* Document Upload
* Application Review
* Application Submitted
* Application Details

## 18. API Requirements

* Retrieve JOP Property & Escrow Account Record
* Submit Signatory Accreditation Application
* Retrieve Application Status
* Update Accredited Signatory Register
* Send Notifications

## 19. Database Entities

* Company
* Jointly Owned Property
* JOP Escrow Account
* Accredited Signatory
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
* Approved applications update the accredited signatory register for the escrow account.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may submit this application — no role restriction.
2. A JOP supervision registration (Service #1) must exist for the property.
3. This service carries no fee, at any point.
4. Only accredited signatories may authorize transactions against the escrow account — enforced by whatever banking relationship holds the account, not by this service itself.
5. Every application receives a unique application reference number.
6. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
2. **Maximum or minimum number of accredited signatories, and whether joint-signature rules apply**, is not specified in source.
