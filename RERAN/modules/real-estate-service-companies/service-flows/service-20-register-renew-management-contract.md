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
tags:
  - real-estate-service-companies
  - service-flow
  - rental
---

# Service #20 – Register/Renew Management Contract

**Service Category:** Real Estate Rental Services

**Source row:** 67 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Register/Renew Management Contract** service records a real estate management firm's contract to manage a property, giving RERA a regulated record of the management relationship before the firm can act on the property within the tenancy system.

## 2. Purpose

Establish, on RERA's own registry, which firm holds the management contract for a given property, and keep that record current as contracts are renewed.

## 3. Description

The company signs up or logs in to the system, fills in the required details, attaches required documents, and sends the application online. On completion, an email is sent with the registered management contract.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Property Management Officer* — sourced directly (row 67), confirmed reliable per `open-questions.md` A1.

## 5. Prerequisites

* Registered RERAN Group D company account.
* The property to be managed is identified.
* A management agreement between the company and the property owner (or owners' association) has been executed.
* Required supporting documents are available.

## 6. Required Information

### Company Information

* Company Legal Name and Registration Reference

### Property Information

* Property Reference / Address
* Owner or Owners' Association Details

### Contract Information

* Contract Type — New Registration or Renewal
* Contract Term
* Scope of Management Services

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation.

## 7. Required Documents

* **Required documents (unspecified beyond "required documents")** — sourced (row 67) as a requirement, though not itemized.

> **Proposed**, by analogy with what a management-contract registration plainly needs:

* Signed Management Agreement
* Company Registration / Licence Evidence
* Property Ownership / Owners' Association Authorization
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 67) — the workflow contains no payment step, confirmed against `payments.md`'s finding that all three Rental services are free.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 67).

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**1 hour and 35 minutes.** Sourced from row 67.

## 12. Processing Workflow

Company User

Sign Up / Log In to the System
↓
Select Contract Type (New / Renewal)
↓
Fill Property and Contract Details
↓
Attach Required Documents
↓
Submit Application Online

↓

RERA (Compliance & Escrow Auditor)

Review Application
↓
Approve
↓
Send Registered Management Contract via Email

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

* Management Contract Successfully Registered or Renewed
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

* **Registered Management Contract** (via email) — sourced (row 67)

## 16. Related Services

* Service #21 – Cancel Management Contract
* Service #22 – Register Tenancy System User

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

* Services
* Register/Renew Management Contract
* Company Information
* Property & Contract Information
* Document Upload
* Application Review
* Application Submitted
* Application Details
* Registered Management Contract

## 18. API Requirements

* Validate Company Account
* Submit Management Contract Registration / Renewal
* Upload Documents
* Retrieve Application Status
* Generate Registered Management Contract
* Send Notifications

## 19. Database Entities

* Company
* Property
* Management Contract
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can register or renew a management contract.
* Required information and documents are validated before submission.
* Application receives a unique application reference number.
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.
* Approved contracts are delivered by email.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may submit this application — no role restriction.
2. This service carries no fee, at any point.
3. Both new registration and renewal are handled through this one service, distinguished by a Contract Type field.
4. Every application receives a unique application reference number.
5. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced beyond the general reference to "required documents."** Needs client confirmation.
2. **Standard contract term length, and how far before expiry renewal can be initiated**, is not specified in source.
