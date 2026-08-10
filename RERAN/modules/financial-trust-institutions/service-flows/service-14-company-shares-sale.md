---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
updated: 2026-08-10
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

* Trustee Centre Operator (Group G), acting on the parties' behalf in assisted mode

> **Proposed** — the source assigns responsible role to the **Mortgage Officer**. `open-questions.md` A4 names company share sales explicitly as a Trustee Centre counter transaction with no lending component. This document follows A4's re-derivation. **Confidence: Medium**, per the answers doc.

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

Paid by the customer at the Trustee Centre — sourced (row 41: "pay ... receive output via email"). **Customer Payment at Counter** model; the output includes Payment Receipts (B9), not a settlement-account fee balance.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 41).

## 11. Expected Processing Time

**25–30 minutes.** Sourced from row 41.

## 12. Processing Workflow

Seller / Purchaser Representative

Visit Real Estate Registration Trustee Centre *(C2: assisted mode)*  
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
Approved — Awaiting Payment  
↓  
Completed

### Additional Statuses

* Rejected  
* Withdrawn

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
* Payment Receipts — sourced (row 41); a payment receipt (B9), not a fee balance

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
* Payment is completed at the counter with a payment receipt issued.  
* Approved applications update the official beneficial-ownership record.  
* Parties receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Trustee Centre operator, acting on the parties' behalf, may process this application. *(Proposed — A4 re-derivation; the source assigns this to the Mortgage Officer.)*
2. The company must hold registered real estate with RERAN for the sale to be within scope of this service.  
3. Payment is required at the counter before the application is finalized.  
4. Approved applications update the official ownership registry to reflect the new shareholding.  
5. Every application receives a unique application reference number.  
6. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Threshold for what share of a company sold triggers this service** (e.g., any transfer, or only a controlling-interest change). Not specified in source.  
2. **Whether the property's Certificate of Title / Title Deed is reissued** or only the beneficial-ownership record is updated. Not specified in source.  
3. **Exact fee amount.** Client data — see `open-questions.md` B5.
