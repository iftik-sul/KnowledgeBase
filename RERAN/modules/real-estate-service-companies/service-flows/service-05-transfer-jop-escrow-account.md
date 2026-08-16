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
  - escrow
---

# Service #5 – Transfer JOP Escrow Account

**Service Category:** Jointly Owned Property Services

**Source row:** 50 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Transfer JOP Escrow Account** service moves a jointly-owned property's escrow account from one financial institution or arrangement to another. This is the first of six escrow-adjacent JOP services (Services #5–#10) and the one whose workflow the other five are sourced by direct reference to.

> **Escrow mechanism, resolved 2026-08-16 (`open-questions.md` A3).** This service does **not** route through a Financial & Trust Institutions Account Trustee, unlike Real Estate Developer's escrow services. The sourced workflow goes directly from the company to RERA's Compliance & Escrow Auditor, with no Trustee intermediary named anywhere in row 50. Do not cross-link this service to `financial-trust-institutions/ui/screens/escrow-request-queue.md` — the mechanisms are genuinely different, not the same process under a different name.

## 2. Purpose

Give an owners' association a regulated path to move its jointly-owned property's escrow account, so RERA's own records — and the association's members — can rely on an accurate, approved record of where the account is held.

## 3. Description

The company signs up or logs in to the Owner system, fills in the transfer details, attaches supporting documents, and submits. RERA audits and sends an acceptance or rejection notice, followed by approval via email, with data viewable on the Owner System.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager* (`open-questions.md` A1).

## 5. Prerequisites

* Registered RERAN Group D company account, with JOP administrative supervision registered against the property (Service #1).
* An existing escrow account for the jointly-owned property.
* The receiving institution or arrangement is identified.
* Required supporting documents are available.

## 6. Required Information

### Property & Account Reference

* Jointly-Owned Property Name / Reference
* Current Escrow Account Details

### Transfer Information

* Receiving Institution / Account Details
* Reason for Transfer

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Owners' Association Resolution Approving the Transfer
* Current Escrow Account Statement
* Receiving Institution's Acceptance / Account Confirmation
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 50) — confirmed against `payments.md`'s Model 1, and against A3's finding that this cluster carries no Trustee-mediated fee mechanism either.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 50). No Account Trustee step is described — see the Service Overview note above.

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**1 business day.** Sourced from row 50.

## 12. Processing Workflow

Company User

Sign Up / Log In to Owner System
↓
Select Registered JOP Property
↓
Fill Transfer Details
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
Data Available on Owner System

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

* Escrow Account Successfully Transferred
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

Sourced (row 50): **none as a downloadable document** — output is view-only data via the Owner System, the same pattern as Services #1–#3.

## 16. Related Services

* Service #6 – Request No-Objection Letter to Close Escrow Account
* Service #7 – Accredit Escrow Account Signatories
* Service #1 – Register Company for JOP Administrative Supervision

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

* Services
* Transfer JOP Escrow Account
* Property & Account Reference
* Transfer Information
* Document Upload
* Application Review
* Application Submitted
* Application Details

## 18. API Requirements

* Retrieve JOP Property & Escrow Account Record
* Submit Escrow Transfer Application
* Retrieve Application Status
* Update Escrow Account Record
* Send Notifications

## 19. Database Entities

* Company
* Jointly Owned Property
* JOP Escrow Account
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
* Approved transfers update the official escrow account record.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may submit this application — no role restriction.
2. A JOP supervision registration (Service #1) must exist for the property.
3. This service carries no fee, at any point.
4. No Account Trustee step applies — approval flows directly from company submission to RERA audit, confirmed against source (`open-questions.md` A3).
5. Every application receives a unique application reference number.
6. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
2. **Whether the receiving institution must itself be a RERA-recognized financial institution** (cross-referencing Financial & Trust Institutions' own approval registry, Service #1 of that module) or can be any bank. Not specified in source.
