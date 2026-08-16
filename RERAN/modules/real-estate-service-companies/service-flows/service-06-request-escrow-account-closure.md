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

# Service #6 – Request No-Objection Letter to Close Escrow Account

**Service Category:** Jointly Owned Property Services

**Source row:** 51 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Request No-Objection Letter to Close Escrow Account** service obtains RERA's formal no-objection before a jointly-owned property's project escrow account can be closed. Unlike every other Jointly Owned Property service, this one is sourced as an **email-only** process — the only channel named in row 51.

> **Escrow mechanism** — same finding as Service #5 (`open-questions.md` A3): no Account Trustee step is described. Do not cross-link to `financial-trust-institutions/ui/screens/escrow-request-queue.md`.

## 2. Purpose

Give an owners' association a regulated, documented no-objection from RERA before closing a jointly-owned property's escrow account, so closure doesn't happen without regulatory awareness.

## 3. Description

The company attaches the application form — itself approved by the Land Department — to an email sent to the Jointly Owned Property's official email address. No further steps are described in source beyond this single action; the row does not describe RERA's internal review process, an output document, or a notification back to the applicant.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Owners'-Association Manager* (`open-questions.md` A1).

## 5. Prerequisites

* Registered RERAN Group D company account, with JOP administrative supervision registered against the property (Service #1).
* An existing project escrow account for the jointly-owned property, to be closed.
* The application form itself (approved by the Land Department) is available and completed.

## 6. Required Information

### Property & Account Reference

* Jointly-Owned Property Name / Reference
* Escrow Account Details

### Closure Information

* Reason for Closure

> **Proposed** — the source names only "the application form approved by Land Department" as the artefact, without specifying its field-level contents. Needs client confirmation of the actual form.

## 7. Required Documents

* **The Land-Department-approved application form itself** — sourced (row 51), the one document this row explicitly names.

> **Proposed, beyond the form itself** — not itemized in source.

* Owners' Association Resolution Approving Closure
* Final Escrow Account Statement
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 51) — the workflow's single email-attach step names no payment. Confirmed against `payments.md`'s Model 1.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 51), though the row's own workflow text does not describe an audit step explicitly the way most other Group D rows do. **Proposed**: RERA reviews the emailed form and responds with the no-objection letter or a query, following the same general audit pattern as every other Group D service, since the source's approver column names the same role that reviews every other service in this module.

No internal company-side certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**3 business days.** Sourced from row 51.

## 12. Processing Workflow

Company User

Complete the Land-Department-Approved Application Form
↓
Attach the Form (and Supporting Documents)
↓
Send via Email to the Jointly Owned Property's Official Email

↓

RERA (Compliance & Escrow Auditor)

*(review process not detailed in source — proposed to follow the module's general audit pattern)*
↓
Review Application
↓
Issue No-Objection Letter, or Query the Application

**Channel: Email — the only Group D service documented this way, comparable to Financial & Trust Institutions' Service #23 (Accreditation of Training Entities), also email-only.**

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

> **Proposed** — the source's single-step description does not itself confirm this full status flow. Adopted from the platform-wide core (`open-questions.md` C1) as the reasonable default, since the row's own brevity is a documentation gap, not evidence of a genuinely simpler process.

## 14. Possible Outcomes

* No-Objection Letter Issued
* Additional Information Requested
* Application Rejected

## 15. Output

Sourced (row 51 — blank in the Issued Document column, but the service's own name and purpose imply): **a no-objection letter**, though the source does not explicitly name this as the issued document the way it names outputs for other services. **Proposed**, following the service name directly — needs client confirmation that a formal letter, rather than a simple status update, is actually issued.

## 16. Related Services

* Service #5 – Transfer JOP Escrow Account
* Service #7 – Accredit Escrow Account Signatories

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

Given the email-only channel, this service does not use the standard Submit Application wizard. A minimal portal surface is proposed:

* Services
* Request No-Objection Letter to Close Escrow Account — static instructional screen directing the user to complete and email the Land-Department-approved form, matching the treatment given to Service #19 (Accreditation of Training Entities)

## 18. API Requirements

Not applicable in the same sense as portal-based services — the source specifies an email workflow. **Proposed**: if a portal record of the request and its outcome is desired, a minimal request-tracking record would need: Log Emailed Request, Update Request Status, Retrieve Request History. Needs client confirmation of whether this is in scope.

## 19. Database Entities

* Company
* Jointly Owned Property
* JOP Escrow Account
* Escrow Closure Request
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can submit this request via the email channel.
* RERA reviews the emailed application and responds with a no-objection letter or a query.
* No payment step is presented at any point.
* The request and its outcome are recorded in the audit log, to the extent the email channel allows.

## 21. Business Rules

1. This service is submitted via email — the only channel sourced, no portal path described.
2. This service carries no fee, at any point.
3. A no-objection letter is a precondition for closing the escrow account; the closure itself is not this service's own action.
4. All request and outcome activity should be permanently recorded, to the extent the email channel permits tracking.

## Open Questions

1. **The application form's actual field-level content is not specified in source** — only that it exists and is "approved by Land Department." Client data.
2. **Whether this service should eventually gain an in-app equivalent**, matching the module build playbook's general preference for portal-based flows, or remain email-only. Flagged for client confirmation, not assumed either way.
3. **The specific output document is not explicitly named in source** — proposed as a no-objection letter based on the service's own name; needs confirmation.
