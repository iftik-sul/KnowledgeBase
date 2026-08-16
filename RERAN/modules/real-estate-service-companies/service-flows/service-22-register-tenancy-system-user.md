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

# Service #22 – Register Tenancy System User

**Service Category:** Real Estate Rental Services

**Source row:** 69 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Register Tenancy System User** service registers a user — by category — within the tenancy system on the company's behalf, giving the company's staff or agents the access they need to operate tenancy-related services for properties under its management.

## 2. Purpose

Let a real estate management company register the individual users who need to operate within the tenancy system on its behalf, categorized by their role or function.

## 3. Description

The company signs up or logs in to the tenancy system and selects the user category, fills in details, attaches documents, and sends the application online. A notice is delivered to the registered user's email.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Property Management Officer* — sourced directly (row 69).

## 5. Prerequisites

* Registered RERAN Group D company account.
* The user to be registered is identified, along with their intended category.

## 6. Required Information

### User Information

* Full Name
* National Identification Number (NIN)
* Contact Information
* User Category

> **Proposed** — the source names "category" as a selection field but does not enumerate the categories themselves. Needs client confirmation of what categories exist.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Government-issued Identification (User)
* Evidence of Role / Employment at the Company
* Other supporting documents, where relevant

## 8. Service Fee

**None. This service is free.**

Sourced (row 69) — no payment step appears anywhere in the workflow.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 69).

## 11. Expected Processing Time

**Immediate.** Sourced from row 69.

## 12. Processing Workflow

Company User

Sign Up / Log In to Tenancy System
↓
Select User Category
↓
Fill User Details
↓
Attach Documents
↓
Submit Application Online

↓

System

Register User
↓
Deliver Notice to Registered User's Email

## 13. Application Status Flow

Draft
↓
Submitted
↓
Approved
↓
Completed

### Additional Statuses

* Rejected
* Withdrawn

> **Proposed**, given row 69's terse workflow text ("send application online" → "notice delivered") does not itself describe an explicit audit step. The "Immediate" processing time suggests this may be closer to automatic registration than a manually reviewed one — flagged, not asserted.

## 14. Possible Outcomes

* User Successfully Registered in the Tenancy System

## 15. Output

* **Notice delivered to the registered user's email** — sourced (row 69), no downloadable document named.

## 16. Related Services

* Service #20 – Register/Renew Management Contract
* Service #21 – Cancel Management Contract

## 17. UI Screens

Not yet built — Phase 4.

## 18. API Requirements

* Validate Company Account
* Submit Tenancy System User Registration
* Upload Documents
* Register User
* Send Notifications

## 19. Database Entities

* Company
* Tenancy System User
* User Category
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can register a tenancy-system user by category.
* Required information and documents are validated before submission.
* No payment step is presented at any point in the flow.
* The registered user is notified by email.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may submit this registration — no role restriction.
2. This service carries no fee, at any point.
3. Every registration is categorized by user type — sourced, categories themselves not enumerated.
4. Every registration receives a unique application reference number.
5. All submissions and notifications must be permanently recorded in the audit trail.

## Open Questions

1. **What the sourced "categories" actually are** — not enumerated anywhere in source. Client data.
2. **Whether registration requires an active management contract (Service #20)** to be in place, or is independent of one. Not specified in source.
3. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
