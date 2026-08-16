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
  - transaction
  - auction
---

# Service #23 – Permit to Sell by Public Auction

**Service Category:** Real Estate Transaction Services

**Source row:** 70 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Permit to Sell by Public Auction** service obtains RERA's permission for a company to sell real estate by public auction, the precondition for Service #24 (Registration of a Property Sold by Auction).

## 2. Purpose

Give a company a regulated path to obtain permission to conduct property sales by public auction, before any individual auction sale can be registered.

## 3. Description

The company signs up or logs in, selects the user type, selects the service, fills in details, and attaches documents. An application completion notice is received; no payment step or further explicit review is described in source beyond that notice.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Brokerage Principal* — sourced directly (row 70).

## 5. Prerequisites

* Registered RERAN Group D company account.
* The company holds a valid real estate licence (Service #12).

## 6. Required Information

### Company Information

* Company Legal Name and Licence Reference
* User Type

### Auction Information

* Proposed Scope of Auction Activity

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Company Licence Certificate
* Proposed Auction Terms / Procedures
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 70) — no payment step appears anywhere in the workflow.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 70), though the row's own workflow text describes only "application completion notice received" without an explicit audit step named. **Proposed**: RERA review happens between submission and the completion notice, following the module's general pattern, even though not spelled out in this particular row.

## 11. Expected Processing Time

**Within two business days.** Sourced from row 70.

## 12. Processing Workflow

Company User

Sign Up / Log In
↓
Select User Type
↓
Select Service
↓
Fill Details
↓
Attach Documents
↓
Submit Application Online

↓

RERA (Compliance & Escrow Auditor)

*(review process not detailed further in source)*
↓
Application Completion Notice Received

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

> **Proposed** — adopted from the platform-wide core, since row 70's own text names only a completion notice without describing the intermediate statuses explicitly.

## 14. Possible Outcomes

* Permit Successfully Granted
* Application Rejected

## 15. Output

Sourced (row 70): **not specified beyond "application completion notice received."** No specific document is named in the Issued Document column. **Proposed**: a Public Auction Permit, matching the service's own name; needs client confirmation.

## 16. Related Services

* Service #24 – Register Property Sold by Auction
* Service #12 – Real Estate Licensing Application

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

* Services
* Permit to Sell by Public Auction
* Company Information
* Auction Information
* Document Upload
* Application Review
* Application Submitted
* Application Details

## 18. API Requirements

* Validate Company Licence
* Submit Auction Permit Application
* Upload Documents
* Retrieve Application Status
* Generate Application Completion Notice
* Send Notifications

## 19. Database Entities

* Company
* Company Licence
* Auction Permit
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* A licensed company can apply for a permit to sell by public auction.
* System validates the company holds a valid licence before allowing the application.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a licensed company (Service #12) may apply for this permit.
2. This service carries no fee, at any point.
3. This permit is the precondition for Service #24 (registering an auction sale).
4. Every application receives a unique application reference number.
5. All submissions and notifications must be permanently recorded in the audit trail.

## Open Questions

1. **The output document is not explicitly named in source** — proposed as a Public Auction Permit based on the service's own name. Needs confirmation.
2. **Whether this permit is time-limited or per-auction**, versus a standing permission once granted, is not specified in source.
3. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
