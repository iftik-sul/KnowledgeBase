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
  - "RERAN/modules/individual-user/service-flows/service-26-submit-tenancy-dispute.md"
tags:
  - real-estate-service-companies
  - service-flow
  - dispute
---

# Service #25 – Primary Suit (Joint Property)

**Service Category:** Real Estate Dispute Services

**Source row:** 57 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Primary Suit (Joint Property)** service files a first-instance dispute suit concerning a jointly-owned property, with RERA's Dispute Adjudication Officer processing the matter through to judgment.

> **Payment model — Model 4, channel-dependent, same shape as Individual User's Submit Tenancy Dispute (#26).** Service Center: payment follows audit. Online: payment sits essentially at submission, with no separate audit step named before it. See `payments.md` Model 4.

## 2. Purpose

Give a company a regulated path to file a primary dispute suit on behalf of a jointly-owned property's owners' association, with RERA's tribunal processing the matter to a first-instance judgment.

## 3. Description

**Service Center channel:** the company moves to a service center, submits documents, the application is entered into the system and audited, fees are paid, and the company attends sessions via the remote litigation system, receiving judgment from the website.

**Online channel:** the company signs up or logs in, uploads documents, pays electronically, attends the session, and receives judgment.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Company Dispute Filing Officer* — sourced directly (row 57), confirmed reliable per `open-questions.md` A1.

## 5. Prerequisites

* Registered RERAN Group D company account.
* The jointly-owned property has a registered JOP administrative supervision relationship with the company (Service #1), or the company is otherwise a party with standing to file.
* Required supporting documents are available.

## 6. Required Information

### Property & Dispute Information

* Jointly-Owned Property Name / Reference
* Subject of Dispute
* Description of the Dispute
* Requested Resolution

> **Proposed** — not itemized in source beyond "submit docs." Needs client confirmation.

## 7. Required Documents

> **Proposed** — not itemized in source.

* Owners' Association Resolution Authorizing the Suit
* Evidence Supporting the Dispute
* Government-issued Identification (Company Representative)
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Payment timing differs by channel — see Processing Workflow.

**Service Center:** documents are submitted and the application is entered and audited first; payment is completed at that point, before the company attends the remote litigation session.

**Online:** payment is completed shortly after document upload, with no separate audit step named before it — effectively upfront.

*(Same channel-dependent shape sourced for Individual User's Submit Tenancy Dispute service — see that file's own Section 9 for the analogous reasoning.)*

## 10. Processing Authority

**Dispute Adjudication Officer** (Group A) — sourced (approver column, row 57), distinct from Compliance & Escrow Auditor, who approves most other Group D services.

## 11. Expected Processing Time

Registration completion: **10 minutes**
Service completion: **8 business days**

Sourced from row 57.

## 12. Processing Workflow

Option 1 – Service Center

Move to Service Center
↓
Submit Documents
↓
Application Entered into System
↓
Application Audited
↓
Pay Fees
↓
Attend Sessions via Remote Litigation System
↓
Receive Judgment from Website

────────────────────────

Option 2 – Online

Sign Up / Log In
↓
Upload Documents
↓
Pay Fees (e-Pay)
↓
Attend Session
↓
Receive Judgment

## 13. Application Status Flow

Draft
↓
Payment Pending
↓
Payment Successful
↓
Submitted
↓
Assigned
↓
Under Review
↓
Hearing
↓
Information Requested
↓
Decision Issued
↓
Completed

### Additional Statuses

* Returned
* Rejected
* Withdrawn
* Audited — Awaiting Payment *(Service Center channel only — the application is audited before payment is collected, unlike the online channel's near-upfront timing shown in the main flow above; see Section 9)*

## 14. Possible Outcomes

* First Instance Judgment Issued
* Additional Information Requested
* Application Rejected
* Payment Failed

## 15. Output

* **First Instance Judgement** — sourced (row 57)

## 16. Related Services

* Service #26 – Execution Case (Joint Ownership)
* Service #1 – Register Company for JOP Administrative Supervision
* Individual User Service #26 – Submit Tenancy Dispute *(cross-module: the structurally comparable channel-dependent dispute pattern)*

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."** Online channel only — the Service Center channel is out of scope pending resolution of whether Group D has any assisted-mode surface at all (`navigation.md`).

* Services
* Primary Suit (Joint Property)
* Property & Dispute Information
* Document Upload
* Payment
* Payment Successful
* Application Review
* Application Submitted
* Application Details
* Hearing Schedule
* Judgment

## 18. API Requirements

* Retrieve JOP Property Record
* Validate Company Standing to File
* Upload Supporting Documents
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Submit Dispute Application
* Assign Dispute Case
* Retrieve Application Status
* Retrieve Hearing Information
* Generate Judgment Document
* Send Notifications

## 19. Database Entities

* Company
* Jointly Owned Property
* Dispute Case
* Hearing
* Judgment
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can file a primary suit on behalf of a jointly-owned property.
* Payment is completed at the point required by the selected channel.
* Application receives a unique reference number.
* Hearing sessions are scheduled where required.
* A first-instance judgment is issued upon completion.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may file this suit — no role restriction.
2. Payment must be completed at the point required by the selected channel — before the remote litigation session at the Service Center, or shortly after upload online.
3. Every dispute application receives a unique reference number.
4. All applications, hearings, judgments, payments, and communications must be permanently recorded in the audit trail.

## Open Questions

1. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
2. **What standing is required to file this suit** — whether any Group D company with a JOP relationship to the property can file, or whether specific authorization from the owners' association is required. Not specified in source.
3. **Exact fee amount.** Client data.
4. **The Service Center channel has no designed screen**, pending `navigation.md`'s open question about whether Group D has any assisted-mode surface at all.
