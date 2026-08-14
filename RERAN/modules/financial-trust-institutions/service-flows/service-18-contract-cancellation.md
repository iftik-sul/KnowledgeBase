---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
updated: 2026-08-14
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

The Institution Relationship Manager moves the request to the Land Department's Customer Center and submits documents to an employee, who enters, audits, and approves the cancellation. The customer pays the fee and receives an e-receipt. Outputs are received online.

## 4. Who Can Apply

### Applicant

* Institution Relationship Manager

Row 45 is the one Group C row whose source responsible-role column already names the **Institution Relationship Manager** — unlike Services #1, #2, and #12–#17, this is not an A4 re-derivation; it matches the source directly and the existing `services-overview.md` table.

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with an Institution Relationship Manager provisioned.  
* An existing contract held by the institution that is eligible for cancellation.  
* Required supporting documents are available.

## 6. Required Information

### Institution Information

* Institution Legal Name  
* Institution Relationship Manager Identifier

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

Paid by the customer, with an e-receipt issued — sourced (row 45: "Customer pays fees, gets e-receipt"). **Customer Payment at Counter** model, unaffected by the 2026-08-14 payment-model correction (`open-questions.md` B1). **Corrected 2026-08-14** — previously cited `B9` for the receipt-vs-fee-balance distinction; B9 is now superseded, since no Group C service produces a "fee balance" any more.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced: the Land Department employee "enters, audits and approves." Documented here as the RERA regulatory gate. No separate internal institutional certification step is described in source for this service. *(Wording corrected 2026-08-14 — previously "no separate institutional maker-checker layer"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).)*

## 11. Expected Processing Time

**15 minutes.** Sourced from row 45.

## 12. Processing Workflow

Institution Relationship Manager

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

Institution Relationship Manager

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

* Service #1 — Approval / Renewal of Account Trustee & Auditing Company *(also owned by the Institution Relationship Manager)*  
* Service #2 — Cancellation of Account Trustee & Auditing Company *(also owned by the Institution Relationship Manager)*

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

* Institution Relationship Manager can initiate a contract cancellation application.  
* Required information and documents are validated before submission.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Payment is completed with an e-receipt voucher issued before completion.  
* Approved cancellations are recorded against the contract.  
* Institution receives an approved e-certificate and e-receipt voucher on completion.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Typically the Institution Relationship Manager submits this application, though any authorized representative of the institution may act on its behalf — the platform does not gate this by a provisioned scope; the acting user and their role are recorded in the audit trail. **Corrected 2026-08-14** — previously required "an authorized representative under a delegated permission scope"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).  
2. The contract being cancelled must exist and be held by the institution.  
3. Cancellation, return, and rejection decisions must carry documented reasoning.  
4. Payment is required, with an e-receipt voucher issued as proof, before the cancellation is finalized.  
5. Every application receives a unique application reference number.  
6. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Grounds for contract cancellation** (e.g., mutual termination, breach, expiry) and whether different grounds require different evidence. Not specified in source.  
2. **What happens to any registered interest (e.g., mortgage) tied to the cancelled contract.** Not specified in source.  
3. **Exact fee amount.** Client data — see `open-questions.md` B5.
