---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
tags:
  - financial-trust-institutions
  - service-flow
  - contract
  - cancellation
---

# Service #18 – Contract Cancellation

**Service Category:** Contract Services

**Source row:** 45 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Contract Cancellation** service cancels a real-estate contract at the Land Department's Customer Center, on the institution's own initiative, with RERA reviewing, auditing and approving the cancellation before an approved e-certificate and e-receipt voucher are issued.

## 2. Purpose

Give an institution a regulated path to cancel a real-estate contract it holds, so the registry and any relying party reflect that the contract no longer stands.

## 3. Description

An institution user moves the request to the Land Department's Customer Center and submits documents to an employee, who enters, audits, and approves the cancellation. The customer pays the fee and receives an e-receipt. Outputs are received online.

## 4. Who Can Apply

### Applicant

* Any of the institution's four Group C roles

Row 45's source responsible-role column names the **Institution Relationship Manager** — unlike Services #1, #2, and #12–#17, this was never an A4 re-derivation; it matched the source directly. **Confirmed 2026-08-15** — per `open-questions.md` A4, ownership is not role-specific for any Group C service, including this one: the IRM is typically who submits this application in practice, but any of the four roles may act on the institution's behalf, consistent with Business Rule 1 below (already unrestricted before this correction).

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with staff provisioned under the corporate account.  
* An existing contract held by the institution that is eligible for cancellation.  
* Required supporting documents are available.

## 6. Required Information

### Institution Information

* Institution Legal Name  
* Acting Officer Identifier

### Contract Information

* Contract Reference Number  
* Parties to the Contract  
* Reason for Cancellation

## 7. Required Documents

> **Proposed** — the source states only that "docs" are submitted to the employee, without enumerating them.

* Original Contract / Agreement Being Cancelled  
* Cancellation Request / Board Resolution Authorizing Cancellation  
* Evidence of Settlement of Any Outstanding Obligations Under the Contract  
* Government-issued Identification (Authorized Representative)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Paid by the customer, **after** RERA's audit and approval, with an e-receipt issued — sourced (row 45's own sequence: the employee "enters, audits and approves," and only then does "Customer pay fees, gets e-receipt"). **Customer Payment at Counter** model, unaffected by the 2026-08-14 payment-model correction (`open-questions.md` B1). **Corrected 2026-08-14** — previously cited `B9` for the receipt-vs-fee-balance distinction; B9 is now superseded, since no Group C service produces a "fee balance" any more.

**This service is one of two exceptions to the general Customer-Payment-at-Counter pattern, confirmed 2026-08-15.** Most services in this category (#13–#17) have the applicant pay *before* RERA's review, per their own sourced workflows. This one, along with Service #12, sources payment *after* RERA's decision — see Section 13 for what that means for this service's status flow.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced: the Land Department employee "enters, audits and approves." Documented here as the RERA regulatory gate. No separate internal institutional certification step is described in source for this service. *(Wording corrected 2026-08-14 — previously "no separate institutional maker-checker layer"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).)*

## 11. Expected Processing Time

**15 minutes.** Sourced from row 45.

## 12. Processing Workflow

Institution User

Move Request to Customer Center at Land Department  
↓  
Submit Documents to Employee

↓

Land Department Employee (Compliance & Escrow Auditor)

Enter Cancellation Data  
↓  
Audit Cancellation  
↓  
Approve, Return, or Reject

↓

Institution User

Pay Fees  
↓  
Obtain e-Receipt

↓

RERA

Generate Approved e-Certificate of Title / Title Deed  
↓  
Generate Approved e-Receipt Voucher  
↓  
Deliver Outputs Online

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
Approved — Awaiting Payment  
↓  
Completed

### Additional Statuses

* Rejected  
* Withdrawn

**Confirmed 2026-08-15 — `Approved — Awaiting Payment` is kept, and is genuinely sourced for this service, not a leftover from an earlier model.** Row 45's own sequence has the Land Department employee audit and approve, return, or reject *before* the institution pays fees (Section 12, Section 9) — the opposite order from most of Services #13–#17, where payment happens first. This is one of exactly two Group C services (the other being Service #12) where an approved-but-unpaid state genuinely exists in the sourced workflow. `services-overview.md`'s Application Status Vocabulary section is corrected to note this exception rather than claim the status "does not occur for any Group C service" without qualification.

## 14. Possible Outcomes

* Contract Successfully Cancelled  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Approved e-Certificate of Title / Title Deed — sourced (row 45)  
* Approved e-Receipt Voucher — sourced (row 45), the same artefact every Group C service now issues (see [payments.md](../payments.md))

## 16. Related Services

* Service #1 — Approval / Renewal of Account Trustee & Auditing Company  
* Service #2 — Cancellation of Account Trustee & Auditing Company

**Corrected 2026-08-15** — the "(also owned by the Institution Relationship Manager)" notes previously attached to both related services above are removed. Per `open-questions.md` A4, no service — including these two or this one — is owned by a particular role; any of the institution's four Group C roles may act on any of them.

## 17. UI Screens

* Services  
* Contract Cancellation  
* Institution Information  
* Contract Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Cancellation Confirmation

## 18. API Requirements

* Retrieve Institution Profile  
* Retrieve Contract Record  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Contract Cancellation Application  
* Retrieve Application Status  
* Generate Approved e-Certificate  
* Generate Approved e-Receipt Voucher  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff  
* Contract  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can initiate a contract cancellation application.  
* Required information and documents are validated before submission.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Payment is completed with an e-receipt voucher issued after RERA's approval, before completion.  
* Approved cancellations are recorded against the contract.  
* Institution receives an approved e-certificate and e-receipt voucher on completion.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Typically the Institution Relationship Manager submits this application, though any of the institution's four Group C roles may act on its behalf — the platform does not gate this by role or a provisioned scope; the acting user and their role are recorded in the audit trail. **Corrected 2026-08-14** — previously required "an authorized representative under a delegated permission scope"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle). **Confirmed 2026-08-15** — `open-questions.md` A4 confirms this was never an A4 re-derivation contest; the rule already matched the unrestricted model.  
2. The contract being cancelled must exist and be held by the institution.  
3. Cancellation, return, and rejection decisions must carry documented reasoning.  
4. Payment is required, with an e-receipt voucher issued as proof, after RERA's approval and before the cancellation is finalized.  
5. Every application receives a unique application reference number.  
6. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Grounds for contract cancellation** (e.g., mutual termination, breach, expiry) and whether different grounds require different evidence. Not specified in source.  
2. **What happens to any registered interest (e.g., mortgage) tied to the cancelled contract.** Not specified in source.  
3. **Exact fee amount.** Client data — see `open-questions.md` B5.
