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

# Service #17 – Amend Professional Practice Card

**Service Category:** Real Estate Licensing Services

**Source row:** 64 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Amend Professional Practice Card** service updates details recorded on an agent's existing practice card, with **automatic approval** — the second Group D licensing service (alongside Service #15) sourced as not requiring manual RERA review.

## 2. Purpose

Keep a practice card's recorded details accurate — a name change, updated contact information, or a corrected error — without requiring the same manual audit the original issuance goes through.

## 3. Description

The company signs up or logs in to the Digital system, adds the details and documents to be updated, and sends the application online; approval is automatic via the system.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Brokerage Principal* — sourced directly (row 64).

## 5. Prerequisites

* An existing, active professional practice card (Service #14) to be amended.
* The requested update is supported by evidence, where applicable.

## 6. Required Information

### Card Reference

* Existing Card Number
* Agent Name

### Update Information

* Field(s) to be Updated
* Requested New Value(s)

> **Proposed** — not itemized in source beyond "add details and documents to be updated." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source beyond "documents to be updated."

* Evidence Supporting the Update (e.g., name-change certificate)
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 64) — the workflow contains no payment step, unlike Service #15 (Renewal), which does charge despite also being automatically approved. This is a genuine, sourced difference between the two automatic-approval services, not an inconsistency.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Licensing & Registration Officer** (Group A) — sourced (approver column, row 64), though approval is automatic per the workflow text.

## 11. Expected Processing Time

**Automatic approval.** Sourced from row 64.

## 12. Processing Workflow

Company User

Sign Up / Log In to Digital System
↓
Add Details and Documents to be Updated
↓
Send Application Online
↓
*(Automatic Approval)*
↓
Card Updated in System

## 13. Application Status Flow

Draft
↓
Submitted
↓
Approved *(automatic)*
↓
Completed

### Additional Statuses

* Withdrawn

**Note:** matching Service #15's reasoning, manual-review and rejection statuses are omitted, since automatic approval is sourced with no described review step.

## 14. Possible Outcomes

* Card Details Successfully Updated

## 15. Output

Sourced (row 64): **not specified beyond "card updated"** — unlike Service #15, this row names no specific output artefact (no e-card reprint, no notice). **Proposed**: an updated e-card, matching Service #15's pattern; needs client confirmation whether a new card is issued or the existing one is simply updated in the system record.

## 16. Related Services

* Service #14 – Issue Professional Practice Card
* Service #15 – Renew Professional Practice Card
* Service #16 – Cancel Professional Practice Card

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

* Services
* Amend Professional Practice Card
* Card Reference
* Field Selection & Updated Values (conditional field selector — Pattern C, checking a field reveals a Current Value / Requested New Value pair for that field only)
* Document Upload
* Application Submitted
* Application Details

## 18. API Requirements

* Retrieve Existing Card Record
* Submit Amendment Application
* Upload Documents
* Auto-Approve Amendment
* Update Card Record
* Send Notifications

## 19. Database Entities

* Company
* Agent
* Professional Practice Card
* Card Amendment Record
* Application
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* A company can request an amendment to an existing practice card's recorded details.
* Amendment is automatically approved on submission.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only an existing, active practice card (Service #14) may be amended under this service.
2. Amendment approval is automatic — sourced, no manual review step.
3. This service carries no fee, at any point.
4. Every amendment receives a unique application reference number.
5. All submissions and updates must be permanently recorded in the audit trail.

## Open Questions

1. **What output, if any, is generated on completion** — not specified beyond "card updated." Client data.
2. **Which fields may be amended through this service** versus requiring cancellation and reissue is not specified in source.
3. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
