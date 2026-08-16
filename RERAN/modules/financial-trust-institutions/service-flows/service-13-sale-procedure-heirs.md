---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - service-flow
  - title-ownership
  - heirs
---

# Service #13 – Sale Procedure (Heirs)

**Service Category:** Title & Ownership Transaction Services

**Source row:** 40 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Sale Procedure (Heirs)** service processes the sale of a deceased owner's property among or on behalf of the heirs, distributing each heir's share of the proceeds to their bank account as part of registration.

## 2. Purpose

Give heirs a regulated path to sell an inherited property and receive their respective shares of the proceeds, with RERA recording the ownership change and coordinating the financial distribution through its Trusts Department.

## 3. Description

An heir or their representative visits a Real Estate Registration Trustee Centre, submits the required documents, and the Trustee Centre operator enters the transaction and performs an initial audit. The customer pays the applicable fees. The transaction is then sent to RERA's Trusts Department, which transfers each heir's share to their nominated bank account. Outputs are delivered by email.

## 4. Who Can Apply

### Applicant

* Any of the institution's four Group C roles — where the transaction is bank-originated
* Trustee Centre Operator (Group G) — otherwise, acting on the heirs' behalf in assisted mode

> **Confirmed 2026-08-15** — previously conditioned this on the Mortgage Officer specifically, following A4's earlier per-service re-derivation. `open-questions.md` A4 now confirms ownership is not role-specific at all. The Trustee Centre Operator path remains what row 40 itself sources (a walk-in "Move to Real Estate Registration Trustee centers" with no bank-employee involvement); whether a bank-originated variant exists for this service at all remains unconfirmed by source — see Open Questions — but that is now a channel question, not a role-ownership one.

### Heirs

* Registered heirs of the deceased property owner, or their authorized representative(s)

## 5. Prerequisites

* The property is registered with RERAN under the deceased owner.  
* Heirship is established (e.g., grant of probate or letters of administration).  
* Each heir's bank account details are available for distribution of proceeds.  
* Required supporting documents are available.

## 6. Required Information

### Deceased Owner / Property Information

* Property Registration Number  
* Deceased Owner's Full Name and NIN

### Heir Information

* Full Name, NIN, and Contact Information (per heir)  
* Share of the Estate (per heir)  
* Bank Account Details for Distribution (per heir)

### Sale Information

* Sale Value  
* Purchaser Information, where the property is being sold to a third party

## 7. Required Documents

> **Proposed** — the source states only that "docs" are submitted, without enumerating them.

* Death Certificate of the Deceased Owner  
* Grant of Probate / Letters of Administration  
* Existing Certificate of Title  
* Government-issued Identification (Each Heir)  
* Sale Agreement, where applicable  
* Bank Account Confirmation (Each Heir)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Paid by the customer at the Trustee Centre, **before** RERA's audit and approval — sourced (row 40's own sequence: initial audit at the Trustee Centre, then payment, then RERA's audit). **Customer Payment at Counter** model, unaffected by the 2026-08-14 payment-model correction (`open-questions.md` B1). **Corrected 2026-08-14** — previously cited `B9` for the receipt-vs-fee-balance distinction; B9 is now superseded, since no Group C service produces a "fee balance" any more.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 40). RERA's Trusts Department additionally executes the distribution of heirs' shares to their bank accounts after audit, a financial-execution step distinct from the regulatory approval itself.

## 11. Expected Processing Time

**25–30 minutes.** Sourced from row 40.

## 12. Processing Workflow

Heir(s) / Authorized Representative

Visit Real Estate Registration Trustee Centre *(C2: this is the sourced path for this service; Section 4 carries the bank-originated branch as unconfirmed rather than asserting a direct online path here — see Open Questions)*  
↓  
Submit Required Documents

↓

Trustee Centre Operator

Enter Transaction Data  
↓  
Perform Initial Audit

↓

Heir(s) / Authorized Representative

Pay Fees at Counter

↓

RERA (Compliance & Escrow Auditor)

Audit and Approve, Return, or Reject Transaction

↓

RERA Trusts Department

Transfer Each Heir's Share to Their Bank Account

↓

RERA

Generate Output Documents  
↓  
Deliver Outputs via Email

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

**Corrected 2026-08-15 — `Approved — Awaiting Payment` removed.** This status previously sat between `Returned for Correction` and `Completed`, but contradicts this service's own sourced workflow (Section 12, Section 9): the heir pays at the Trustee Centre counter *before* RERA's audit and approval, not after. By the time a decision is reached, payment has already happened. This is now the pattern for every fee-bearing Group C service, without exception — see [status-badges.md](../ui/status-badges.md#application-status) for the module-wide confirmation following the 2026-08-16 normalization of Services #12 and #18, the last two services that previously paid after RERA's decision.

## 14. Possible Outcomes

* Sale Successfully Registered and Heirs' Shares Distributed  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Certificate of Title — sourced (row 40)  
* Title Deed — sourced (row 40)  
* Map — sourced (row 40)  
* Payment Receipts — sourced (row 40), the same artefact every Group C service now issues (see [payments.md](../payments.md))

## 16. Related Services

* Service #12 — Registration of Real Estate Fund Companies in the Register of Privileges  
* Service #14 — Company Shares Sale  
* Service #16 — Split Ownership

## 17. UI Screens

* Services  
* Sale Procedure (Heirs)  
* Heir Information  
* Property & Sale Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Distribution Confirmation  
* Registration Confirmation

## 18. API Requirements

* Retrieve Property Details  
* Validate Heirship Documentation  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Heirs' Sale Application  
* Retrieve Application Status  
* Distribute Heir Shares to Bank Accounts  
* Generate Certificate of Title / Title Deed  
* Generate Map  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Deceased Owner Record  
* Heir  
* Heir Bank Account  
* Property Sale  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* An heir or authorized representative can initiate the sale procedure at a Trustee Centre.  
* System validates heirship documentation before allowing the transaction to proceed.  
* Required information and documents are validated before submission.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Payment is completed at the counter with a payment receipt issued, before RERA's audit.  
* Each heir's share is transferred to their nominated bank account upon approval.  
* Certificate of Title, Title Deed, and Map are generated upon completion.  
* All heirs receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. This application may be processed by any of the institution's four Group C roles where bank-originated, or otherwise by a Trustee Centre operator acting on the heirs' behalf. **Confirmed 2026-08-15** — previously conditioned on the Mortgage Officer specifically; `open-questions.md` A4 confirms no service is role-specific. *(Whether a bank-originated variant exists for this service at all remains unconfirmed by source — only the Trustee-Centre path is confirmed by row 40.)*
2. Heirship must be established by valid probate or administration documentation before the sale can proceed.  
3. Payment is required at the counter, before RERA's audit and approval.  
4. Each heir's share of proceeds is distributed to their nominated bank account as part of completion.  
5. Approved applications update the official property ownership registry.  
6. Every application receives a unique application reference number.  
7. All applications, approvals, payments, distributions, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **How disputes among heirs over shares are handled** within this workflow. Not specified in source.  
2. **Validation method for bank account details** used for distribution (e.g., account-name matching against the heir's identity). Not specified in source.  
3. ~~Whether a bank-originated path (Mortgage Officer, per A4's conditional) exists for this service at all.~~ **Reframed 2026-08-15** — the role-conditional part of this question is resolved: if a bank-originated path exists, any of the four Group C roles may use it, not just a Mortgage Officer (A4). What remains genuinely open is narrower: **whether a bank-originated channel exists for this service at all.** No row among 38, 40–44 describes bank-employee entry the way the mortgage rows (30–33, 39) do; this document still sources only the Trustee-Centre-assisted path.  
4. **Exact fee amount.** Client data — see `open-questions.md` B5.
