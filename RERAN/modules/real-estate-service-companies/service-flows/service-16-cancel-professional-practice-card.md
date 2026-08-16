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
  - "RERAN/modules/real-estate-service-companies/service-flows/service-14-issue-professional-practice-card.md"
tags:
  - real-estate-service-companies
  - service-flow
  - licensing
---

# Service #16 – Cancel Professional Practice Card

**Service Category:** Real Estate Licensing Services

**Source row:** 63 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Cancel Professional Practice Card** service revokes an agent's existing practice card, ending their RERA-recognized standing to practice on the company's behalf.

## 2. Purpose

Give a company a regulated way to revoke an agent's practice card — for example when the agent leaves the company — so the card no longer represents valid standing once the relationship ends.

## 3. Description

The company logs in to the Licensing System, selects the service, fills in details and attaches documents if any, and sends the application. RERA audits the application and, on approval, sends notice of card revocation via email.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Brokerage Principal* — sourced directly (row 63).

## 5. Prerequisites

* An existing, active professional practice card (Service #14) to be cancelled.

## 6. Required Information

### Card Reference

* Existing Card Number
* Agent Name
* Reason for Cancellation

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation.

## 7. Required Documents

Sourced (row 63): documents are attached **"if any"** — unlike every other licensing service, this row explicitly allows a document-free submission. **Proposed**, where documents are provided:

* Evidence of the Reason for Cancellation (e.g., termination letter)
* Other supporting documents, where relevant

## 8. Service Fee

**None. This service is free.**

Sourced (row 63) — the workflow contains no payment step, matching the pattern that cancellation services across the project (Financial & Trust Institutions' Service #2, Individual User's various cancellation services) tend to be free.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Licensing & Registration Officer** (Group A) — sourced (approver column, row 63).

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**2 minutes.** Sourced from row 63 — the fastest processing time in the module.

## 12. Processing Workflow

Company User

Log In to Licensing System
↓
Select "Cancel Professional Practice Card"
↓
Fill Details
↓
Attach Documents *(if any)*
↓
Send Application Online

↓

RERA (Licensing & Registration Officer)

Audit Application
↓
Approve
↓
Send Notice of Card Revocation via Email

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

## 14. Possible Outcomes

* Card Successfully Cancelled
* Application Rejected

## 15. Output

* **Notice of Card Revocation** (via email) — sourced (row 63)

## 16. Related Services

* Service #14 – Issue Professional Practice Card
* Service #15 – Renew Professional Practice Card
* Service #17 – Amend Professional Practice Card

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

* Services
* Cancel Professional Practice Card
* Card Reference
* Document Upload *(optional — sourced as "if any")*
* Application Review
* Application Submitted
* Application Details

## 18. API Requirements

* Retrieve Existing Card Record
* Submit Cancellation Application
* Upload Documents *(optional)*
* Retrieve Application Status
* Revoke Card
* Send Notifications

## 19. Database Entities

* Company
* Agent
* Professional Practice Card
* Card Cancellation Record
* Application
* Document *(optional)*
* Notification
* Audit Log

## 20. Acceptance Criteria

* A company can request cancellation of an existing practice card.
* Documents may be attached, but are not mandatory.
* No payment step is presented at any point in the flow.
* Approved cancellations revoke the card and notify by email.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an existing, active practice card (Service #14) may be cancelled under this service.
2. This service carries no fee, at any point.
3. Supporting documents are optional, not mandatory — sourced directly.
4. Every cancellation application receives a unique application reference number.
5. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information fields are proposed, not sourced.** Needs client confirmation.
2. **Whether a cancelled card can be reinstated**, or whether a new issuance (Service #14) is the only path back, is not specified in source.
