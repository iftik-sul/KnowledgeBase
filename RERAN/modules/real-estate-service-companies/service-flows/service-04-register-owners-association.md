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

# Service #4 – Register Owners Association

**Service Category:** Jointly Owned Property Services

**Source row:** 49 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Register Owners Association** service formally registers an owners' association for a jointly-owned property with RERA, issuing an owner committee registration certificate on approval. Unlike Services #1–#3, this service is explicitly reachable by two different applicant types through two different channels.

## 2. Purpose

Give a jointly-owned property's owners' association formal, regulated standing with RERA, so the association can subsequently act (appoint auditors, approve fees, manage the escrow account) with recognized authority.

## 3. Description

The applicant signs up or logs in, fills in the association's details, attaches supporting documents, and sends the application online. RERA audits and sends an acceptance or rejection notice, followed by an approval notice via email once accepted, and the data becomes viewable on the Land Department website.

## 4. Who Can Apply

**Sourced as two distinct channels, not one applicant type:**

* **Real estate companies** — via the Land Department website (Owner system). Any of the company's four Group D roles may act; typically the Owners'-Association Manager in practice.
* **Owners** (individual unit owners, outside Group D) — via the RERA App.

This is the one Group D service the source explicitly opens to a non-company applicant type as well, sourced directly from row 49's Channel column ("For real estate companies: Land Department website (Owner system). For owners: RERA App").

## 5. Prerequisites

* For company applicants: registered RERAN Group D company account.
* For owner applicants: registered RERAN Individual User account (cross-module — see Related Services).
* The jointly-owned property to be represented exists and is identifiable.
* Required supporting documents are available.

## 6. Required Information

### Association Information

* Proposed Association Name
* Jointly-Owned Property Name / Reference
* Number of Units Represented

### Applicant Information

* Applicant Name and Contact Details
* Applicant Type (Company / Owner)

> **Proposed** — not itemized in source beyond "fill details." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Minutes of the Meeting Establishing the Association
* List of Unit Owners / Members
* Proposed Association Constitution / Bylaws
* Other supporting documents required by RERAN

## 8. Service Fee

**None. This service is free.**

Sourced (row 49) — confirmed against `payments.md`'s Model 1.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 49).

No internal certification gate exists for this service (`open-questions.md` A5).

## 11. Expected Processing Time

**25 minutes.** Sourced from row 49.

## 12. Processing Workflow

Applicant (Company or Owner)

Sign Up / Log In *(Owner System for companies; RERA App for owners)*
↓
Fill Association Details
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
Data Available on Land Department Website

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

* Owners Association Successfully Registered
* Additional Information Requested
* Application Rejected
* Application Withdrawn

## 15. Output

* **Owner Committee Registration Certificate** — sourced (row 49), the only Service #1–#4 to issue a named certificate rather than view-only data.

## 16. Related Services

* Service #1 – Register Company for JOP Administrative Supervision
* Service #2 – Approve Service Fees & Utilization Fees
* Individual User (cross-module) — the owner-applicant channel for this service belongs to that module's user base, though the service itself is documented here since it is filed under Group D in source

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."**

* Services
* Register Owners Association
* Association Information
* Applicant Information
* Document Upload
* Application Review
* Application Submitted
* Application Details
* Owner Committee Registration Certificate

**Proposed**: given the two sourced applicant channels (company vs. owner), this service likely needs two distinct entry points sharing the same underlying form, rather than one shared form indistinguishable by applicant type — needs client confirmation before final design.

## 18. API Requirements

* Validate Applicant (Company or Owner)
* Retrieve JOP Property Reference
* Submit Owners Association Registration
* Retrieve Application Status
* Generate Owner Committee Registration Certificate
* Send Notifications

## 19. Database Entities

* Company *(where company-filed)*
* Individual User *(where owner-filed, cross-module)*
* Jointly Owned Property
* Owners Association
* Application
* Service Request
* Document
* Notification
* Audit Log

## 20. Acceptance Criteria

* Either a company (any of its four Group D roles) or an individual owner can submit this registration, through their respective channel.
* Required information and documents are validated before submission.
* Application receives a unique application reference number.
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.
* Approved registrations issue an Owner Committee Registration Certificate.
* No payment step is presented at any point in the flow.
* All activities are recorded in the audit log.

## 21. Business Rules

1. This service is reachable by both company and individual-owner applicants, through different channels — sourced directly, not proposed.
2. Where filed by a company, any of its four Group D roles may act — no role restriction.
3. This service carries no fee, at any point.
4. Approved registrations issue an Owner Committee Registration Certificate — the association's formal evidence of standing.
5. Every application receives a unique application reference number.
6. All submissions, approvals, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
2. **Whether the company-side and owner-side applications for the same property must be reconciled** (e.g., does an owner-filed registration require company acknowledgment, or vice versa) is not addressed in source.
3. **Cross-module ownership**: since owners may file this service via the RERA App, should this service also be documented (or cross-linked) from the Individual User module? Flagged, not resolved — this document treats it as a Group D service per its source-table filing, consistent with the instruction not to add or remove services from either module's count.
