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
  - "RERAN/modules/real-estate-service-companies/service-flows/service-25-primary-suit-joint-property.md"
tags:
  - real-estate-service-companies
  - service-flow
  - dispute
---

# Service #26 – Execution Case (Joint Ownership)

**Service Category:** Real Estate Dispute Services

**Source row:** 58 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Execution Case (Joint Ownership)** service enforces a judgment already awarded by the judicial committees (typically the outcome of Service #25's primary suit), against a defaulting party in a jointly-owned property matter.

> **Payment model — Model 4, channel-dependent, same shape as Service #25.**

## 2. Purpose

Give a company a regulated path to enforce a judgment already awarded in a jointly-owned property dispute, closing the loop Service #25 opens.

## 3. Description

**Service Center channel:** the company moves to a service center, submits documents, the application is entered into the system and audited, and fees are paid.

**Online channel:** the company signs up or logs in, obtains the judgment annotated with execution, submits documents, pays electronically, submits e-applications if necessary 15 days after notice, pays any e-application fees, and receives the judge's resolution.

## 4. Who Can Apply

Any of the company's four Group D roles — the platform does not gate this by role; the acting user and their role are recorded in the audit trail.

*Typically filed in practice by the Company Dispute Filing Officer* — sourced directly (row 58).

## 5. Prerequisites

* Registered RERAN Group D company account.
* An existing judgment awarded by the judicial committees (typically via Service #25) requiring enforcement.
* Required supporting documents are available.

## 6. Required Information

### Judgment Reference

* Original Judgment / Case Reference
* Defaulting Party Details

### Execution Information

* Requested Enforcement Action

> **Proposed** — not itemized in source beyond "submit docs." Needs client confirmation.

## 7. Required Documents

* **Judgment Annotated with Execution** — sourced (row 58), the one document this row explicitly names as required for the online path.

> **Proposed, beyond the annotated judgment itself:**

* Evidence of Non-Compliance by the Defaulting Party
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule. Sourced (row 58) as potentially arising twice: an initial fee, and — for the online channel specifically — additional e-application fees where a follow-up e-application is needed 15 days after notice.

## 9. Payment Required

**Yes**

Payment timing differs by channel — see Processing Workflow.

**Service Center:** documents are submitted and the application is entered and audited first; payment is completed at that point.

**Online:** payment is completed after submitting documents, and again for any subsequent e-applications filed 15 days after notice, where necessary — the only Group D service sourced with a genuinely two-stage payment possibility.

## 10. Processing Authority

**Dispute Adjudication Officer** (Group A) — sourced (approver column, row 58).

## 11. Expected Processing Time

Registration completion: **10 minutes**
Service completion: **Business day**

Sourced from row 58.

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

────────────────────────

Option 2 – Online

Sign Up / Log In
↓
Obtain Judgment Annotated with Execution
↓
Submit Documents
↓
Pay Fees (e-Pay)
↓
*(If Necessary, 15 Days After Notice)* Submit e-Applications
↓
Pay e-Application Fees
↓
Receive Judge's Resolution

## 13. Application Status Flow

Draft
↓
Payment Pending
↓
Payment Successful
↓
Submitted
↓
Under Review
↓
Awaiting Follow-Up e-Application *(online channel only, where applicable, 15 days after notice)*
↓
Decision Issued
↓
Completed

### Additional Statuses

* Returned
* Rejected
* Withdrawn
* Audited — Awaiting Payment *(Service Center channel only, same shape as Service #25)*

## 14. Possible Outcomes

* Judgment Successfully Executed
* Judge's Resolution Issued
* Payment Failed

## 15. Output

* **Execution of the judgement awarded by the judicial committees** — sourced (row 58)

## 16. Related Services

* Service #25 – Primary Suit (Joint Property)
* Service #1 – Register Company for JOP Administrative Supervision

## 17. UI Screens

**Corrected 2026-08-16 — Phase 4 is complete; this section previously said "Not yet built."** Online channel only — the Service Center channel is out of scope pending resolution of whether Group D has any assisted-mode surface at all (`navigation.md`).

* Services
* Execution Case (Joint Ownership)
* Judgment Reference
* Execution Information
* Document Upload
* Payment
* Payment Successful
* Application Review
* Application Submitted
* Application Details
* Follow-Up e-Application (where applicable)
* Judge's Resolution

## 18. API Requirements

* Retrieve Original Judgment Record
* Upload Supporting Documents
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Submit Execution Application
* Submit Follow-Up e-Application *(where necessary)*
* Retrieve Application Status
* Generate Judge's Resolution
* Send Notifications

## 19. Database Entities

* Company
* Original Judgment
* Execution Case
* Follow-Up e-Application *(where applicable)*
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Any of the company's four Group D roles can file an execution case referencing an existing judgment.
* Payment is completed at the point(s) required by the selected channel, including any follow-up e-application fee where applicable.
* Application receives a unique reference number.
* A judge's resolution is issued upon completion.
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the company's four Group D roles may file this case — no role restriction.
2. An existing judgment (typically from Service #25) must be referenced for execution to be sought.
3. Payment must be completed at the point required by the selected channel; the online channel may require a second payment for a follow-up e-application 15 days after notice.
4. Every execution case receives a unique reference number.
5. All applications, payments, resolutions, and communications must be permanently recorded in the audit trail.

## Open Questions

1. **What triggers the need for a follow-up e-application 15 days after notice**, and what it contains, is not fully specified in source beyond "if necessary." Client data.
2. **Required information and document lists are proposed, not sourced.** Needs client confirmation.
3. **Exact fee amount(s).** Client data.
4. **The Service Center channel has no designed screen**, pending `navigation.md`'s open question about whether Group D has any assisted-mode surface at all.
