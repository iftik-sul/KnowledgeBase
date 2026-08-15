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
tags:
  - financial-trust-institutions
  - service-flow
  - title-ownership
  - company-shares
---

# Service #14 – Company Shares Sale

**Service Category:** Title & Ownership Transaction Services

**Source row:** 41 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Company Shares Sale** service records the sale of shares in a company that holds registered real estate, updating RERA's ownership records to reflect the change of beneficial ownership.

## 2. Purpose

Give a company shares sale involving RERAN-registered property formal registration, so the property's beneficial-ownership chain remains accurate even where legal title to the property itself does not change hands.

## 3. Description

A representative of the seller or purchaser visits a Real Estate Registration Trustee Centre, submits the required documents, and the Trustee Centre operator enters the transaction into the system. The customer pays the applicable fees. RERA reviews and approves the transaction, and outputs are delivered by email.

## 4. Who Can Apply

### Applicant

* Any of the institution's four Group C roles — where the transaction is bank-originated
* Trustee Centre Operator (Group G) — otherwise, acting on the parties' behalf in assisted mode

> **Confirmed 2026-08-15** — previously conditioned this on the Mortgage Officer specifically, following A4's earlier per-service re-derivation. `open-questions.md` A4 now confirms ownership is not role-specific at all. The Trustee Centre Operator path remains what row 41 itself sources (a walk-in Trustee Centre visit with no bank-employee involvement); whether a bank-originated variant exists for this service at all remains unconfirmed by source — see Open Questions — but that is now a channel question, not a role-ownership one.

### Parties

* Selling Company (through its authorized representative)  
* Purchasing Party (individual or company)

## 5. Prerequisites

* The company holds registered real estate with RERAN.  
* The share sale has been agreed and is legally executable.  
* Required supporting documents are available.

## 6. Required Information

### Company Information

* Company Legal Name  
* Certificate of Incorporation Number  
* Property Registration Number(s) Held by the Company

### Sale Information

* Selling Shareholder(s)  
* Purchasing Party  
* Number / Percentage of Shares Sold  
* Sale Value  
* Agreed Sale Date

## 7. Required Documents

> **Proposed** — the source states only that "docs" are submitted, without enumerating them.

* Share Sale Agreement  
* Certificate of Incorporation  
* Register of Members / Shareholding Structure (Before and After)  
* Existing Certificate of Title / Title Deed (property held by the company)  
* Board Resolution Approving the Sale  
* Government-issued Identification (Signatories)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Paid by the customer at the Trustee Centre, **before** RERA's review and approval — sourced (row 41's own sequence: transaction entered, then "pay... receive output via email," with RERA's review sitting between payment and output). **Customer Payment at Counter** model, unaffected by the 2026-08-14 payment-model correction (`open-questions.md` B1). **Corrected 2026-08-14** — previously cited `B9` for the receipt-vs-fee-balance distinction; B9 is now superseded, since no Group C service produces a "fee balance" any more.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 41).

## 11. Expected Processing Time

**25–30 minutes.** Sourced from row 41.

## 12. Processing Workflow

Seller / Purchaser Representative

Visit Real Estate Registration Trustee Centre *(C2: this is the sourced path for this service; Section 4 carries the bank-originated branch as unconfirmed rather than asserting a direct online path here — see Open Questions)*  
↓  
Submit Required Documents

↓

Trustee Centre Operator

Enter Transaction into System

↓

Seller / Purchaser Representative

Pay Fees at Counter

↓

RERA (Compliance & Escrow Auditor)

Review and Approve, Return, or Reject

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

**Corrected 2026-08-15 — `Approved — Awaiting Payment` removed.** This status previously sat between `Returned for Correction` and `Completed`, but contradicts this service's own sourced workflow (Section 12, Section 9): the customer pays at the Trustee Centre counter *before* RERA's review and approval, not after. By the time a decision is reached, payment has already happened. Compare Services #12 and #18, where RERA's row-sourced sequence has approval *before* payment, and where this status is kept as accurate.

## 14. Possible Outcomes

* Company Shares Sale Successfully Registered  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Certificate of Title — sourced (row 41)  
* Title Deed — sourced (row 41)  
* Payment Receipts — sourced (row 41), the same artefact every Group C service now issues (see [payments.md](../payments.md))

## 16. Related Services

* Service #12 — Registration of Real Estate Fund Companies in the Register of Privileges  
* Service #13 — Sale Procedure (Heirs)  
* Service #15 — Updating Title Deed Information

## 17. UI Screens

* Services  
* Company Shares Sale  
* Company Information  
* Sale Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Registration Confirmation

## 18. API Requirements

* Retrieve Company / Property Records  
* Validate Company Registration and Shareholding  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Company Shares Sale Application  
* Retrieve Application Status  
* Update Beneficial Ownership Record  
* Generate Certificate of Title / Title Deed  
* Send Notifications

## 19. Database Entities

* User  
* Company  
* Company Shareholding  
* Property  
* Property Ownership  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Seller or purchaser representative can initiate a company shares sale at a Trustee Centre.  
* System validates the company's existing registration and shareholding structure.  
* Required information and documents are validated before submission.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Payment is completed at the counter with a payment receipt issued, before RERA's review.  
* Approved applications update the official beneficial-ownership record.  
* Parties receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. This application may be processed by any of the institution's four Group C roles where bank-originated, or otherwise by a Trustee Centre operator acting on the parties' behalf. **Confirmed 2026-08-15** — previously conditioned on the Mortgage Officer specifically; `open-questions.md` A4 confirms no service is role-specific. *(Whether a bank-originated variant exists for this service at all remains unconfirmed by source — only the Trustee-Centre path is confirmed by row 41.)*
2. The company must hold registered real estate with RERAN for the sale to be within scope of this service.  
3. Payment is required at the counter, before RERA's review and approval.  
4. Approved applications update the official ownership registry to reflect the new shareholding.  
5. Every application receives a unique application reference number.  
6. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Threshold for what share of a company sold triggers this service** (e.g., any transfer, or only a controlling-interest change). Not specified in source.  
2. **Whether the property's Certificate of Title / Title Deed is reissued** or only the beneficial-ownership record is updated. Not specified in source.  
3. ~~Whether a bank-originated path (Mortgage Officer, per A4's conditional) exists for this service at all.~~ **Reframed 2026-08-15** — the role-conditional part of this question is resolved: if a bank-originated path exists, any of the four Group C roles may use it, not just a Mortgage Officer (A4). What remains genuinely open is narrower: **whether a bank-originated channel exists for this service at all.** No row among 38, 40–44 describes bank-employee entry the way the mortgage rows (30–33, 39) do; this document still sources only the Trustee-Centre-assisted path.  
4. **Exact fee amount.** Client data — see `open-questions.md` B5.
