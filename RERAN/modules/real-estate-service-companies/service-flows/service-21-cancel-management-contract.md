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
  - "RERAN/modules/real-estate-service-companies/service-flows/service-20-register-renew-management-contract.md"
tags:
  - real-estate-service-companies
  - service-flow
  - rental
---

# Service #21 – Cancel Management Contract

**Service Category:** Real Estate Rental Services

**Source row:** 68 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Cancel Management Contract** service ends a registered real estate management contract, formally closing out the management relationship on RERA's registry.

## 2. Purpose

Give a company a regulated way to end its management contract for a property — for example when the arrangement is terminated by mutual agreement — so RERA's registry accurately reflects the current management relationship.

## 3. Description

The company signs up or logs in to the tenancy system, fills in details, attaches documents, and sends the application online. An email is sent confirming cancellation of the contract.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Property Management Officer* — sourced directly (row 68).

## 5. Prerequisites

* An existing, registered management contract (Service #20) to be cancelled.
* Reason for cancellation.

## 6. Required Information

### Contract Reference

* Existing Management Contract Number
* Property Reference
* Reason for Cancellation

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Mutual Termination Agreement, where applicable
* Existing Management Contract
* Other supporting documents, where relevant

## 8. Service Fee

**None. This service is free.**

Sourced (row 68) — no payment step appears anywhere in the workflow.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 68).

## 11. Expected Processing Time

**Immediate.** Sourced from row 68.

## 12. Processing Workflow

Company User

Sign Up / Log In to Tenancy System
↓
Fill Cancellation Details
↓
Attach Documents
↓
Submit Application Online

↓

RERA

*(review process not detailed further in source beyond delivery of the outcome)*
↓
Send Email Confirming Contract Cancellation

## 13. Application Status Flow

Draft
↓
Submitted
↓
Under Review
↓
Approved
↓
Completed

### Additional Statuses

* Rejected
* Withdrawn

> **Proposed** — row 68's own workflow text is terse ("send application online" → "email sent to cancel the contract"), without describing an explicit audit step the way most other Group D rows do. Adopted from the platform-wide core as the reasonable default rather than assuming an unsourced simpler process, consistent with how Service #6's similarly terse workflow was handled.

## 14. Possible Outcomes

* Management Contract Successfully Cancelled
* Application Rejected

## 15. Output

* **Email confirming contract cancellation** — sourced (row 68), though no downloadable document is named.

## 16. Related Services

* Service #20 – Register/Renew Management Contract
* Service #22 – Register Tenancy System User

## 17. UI Screens

Not yet built — Phase 4.

## 18. API Requirements

* Retrieve Existing Management Contract
* Submit Cancellation Application
* Upload Documents
* Retrieve Application Status
* Update Contract Status
* Send Notifications

## 19. Database Entities

* Company
* Property
* Management Contract
* Contract Cancellation Record
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can request cancellation of an existing management contract.
* Required information and documents are validated before submission.
* No payment step is presented at any point in the flow.
* Approved cancellations are confirmed by email.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an existing, registered management contract (Service #20) may be cancelled under this service.
2. This service carries no fee, at any point.
3. Every cancellation application receives a unique application reference number.
4. All submissions and outcomes must be permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
2. **What happens to tenancy-system users registered under the cancelled contract (Service #22)** — whether they are also deregistered, or persist independently — is not addressed in source.
