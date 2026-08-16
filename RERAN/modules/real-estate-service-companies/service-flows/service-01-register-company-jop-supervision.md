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
  - jointly-owned-property
---

# Service #1 – Register Company for JOP Administrative Supervision

**Service Category:** Jointly Owned Property Services

**Source row:** 46 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Register Company for JOP Administrative Supervision** service records a real estate service company's role as the administrative supervisor of a jointly-owned (strata / JOP) property, giving RERA a regulated record of which company oversees which joint property before any of the module's other JOP services can be filed against it.

## 2. Purpose

Establish, on RERA's own registry, which company holds administrative supervision responsibility for a given jointly-owned property — the foundational record every other JOP service in this module depends on.

## 3. Description

A company user signs up or logs in to the Owner's system, fills in the required details, attaches supporting documents, and sends the application online. RERA audits the application and sends an acceptance or rejection notice, followed by an approval notice via email once accepted. The registered data becomes viewable on the Owner's system and the Land Department website.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager.* That is a description of customary practice, not a restriction. Unlike Group B and Group C, Group D's source Responsible Role column holds up cleanly service-by-service (`open-questions.md` A1) — every Jointly Owned Property row, including this one, names Owners'-Association Manager without exception.

## 5. Prerequisites

* Registered RERAN Group D company account.
* The jointly-owned property to be supervised exists and is identifiable (e.g., by development/project reference).
* Required supporting documents are available.

## 6. Required Information

### Company Information

* Company Legal Name
* Company Registration / Licence Reference

### Property Information

* Jointly-Owned Property Name / Reference
* Property Address
* Number of Units

> **Proposed** — the source states only that "details" are filled in, without enumerating fields. The list above is proposed by analogy with how other RERAN modules capture the company-to-property relationship; needs client confirmation.

## 7. Required Documents

> **Proposed** — the source states only that documents are "attached," without enumerating them.

* Company Registration Certificate
* Board Resolution Authorizing JOP Supervision
* Evidence of Appointment by the Property's Owners (where applicable)
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 46) — the workflow contains no payment step anywhere, confirmed against `payments.md`'s Model 1 (No Fee) finding, which applies to all 11 Jointly Owned Property services without exception.

## 9. Payment Required

**No.**

No payment step exists at any point in the sourced workflow. See `payments.md`'s Model 1.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 46).

No internal company-side certification gate exists for this service — sourced directly, confirmed against `open-questions.md` A5, which found no Group D row describes an internal maker-checker step comparable to Financial & Trust Institutions' mortgage services.

## 11. Expected Processing Time

**5 minutes.** Sourced from row 46.

## 12. Processing Workflow

Company User

Sign Up / Log In to Owner's System
↓
Fill Company & Property Details
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

Per `open-questions.md` C1, Group D adopts the platform-core status vocabulary unextended — no internal-certification statuses apply anywhere in this module.

## 14. Possible Outcomes

* Company Successfully Registered for JOP Administrative Supervision
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

Sourced (row 46): **none as a downloadable document** — the row explicitly states the output is "view data via online Owner's system and Department's website," not an issued certificate. The registration itself, once approved, is the record; nothing is generated for the company to download.

## 16. Related Services

* Service #4 – Register Owners Association
* Service #5 – Transfer JOP Escrow Account
* Service #11 – Approval / Renewal of Financial Auditing Company

## 17. UI Screens

Not yet built — Phase 4 of the module build sequence. **Proposed** minimum surface: a company-to-property registration form within a JOP module workspace.

## 18. API Requirements

* Validate Company Account
* Submit JOP Supervision Registration
* Retrieve Application Status
* Update JOP Property Register
* Send Notifications

## 19. Database Entities

* Company
* Company Staff
* Jointly Owned Property
* JOP Supervision Record
* Application
* Service Request
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can submit this registration.
* Required information and documents are validated before submission.
* Application receives a unique application reference number.
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.
* Approved registrations update the official JOP supervision register.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may submit this registration — no role restriction, per the unified-access model.
2. This service carries no fee, at any point (`payments.md` Model 1).
3. Approval establishes the company's supervisory relationship to the named jointly-owned property, which subsequent JOP services (Services #2–#11) act against.
4. Every application receives a unique application reference number.
5. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced beyond "fill details" / "attach documents."** Needs client confirmation.
2. **Whether a jointly-owned property must itself be pre-registered elsewhere** (e.g., via a Group B or Group E service) before this service can reference it, or whether this service can register the property implicitly. Not specified in source.
