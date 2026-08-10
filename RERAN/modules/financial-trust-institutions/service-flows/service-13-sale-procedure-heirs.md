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

* Trustee Centre Operator (Group G), acting on the heirs' behalf in assisted mode

> **Proposed** — the source assigns responsible role to the **Mortgage Officer**. `open-questions.md` A4 identifies heirs' sale by name as one of the Trustee Centre counter transactions with no lending component that should not sit with the mortgage desk. This document follows A4's re-derivation. **Confidence: Medium**, per the answers doc — contradicts the source's responsible-role column.

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

Paid by the customer at the Trustee Centre — sourced (row 40: "Customer pays fees"). **Customer Payment at Counter** model; the output includes Payment Receipts (B9), not a settlement-account fee balance.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 40). RERA's Trusts Department additionally executes the distribution of heirs' shares to their bank accounts after audit, a financial-execution step distinct from the regulatory approval itself.

## 11. Expected Processing Time

**25–30 minutes.** Sourced from row 40.

## 12. Processing Workflow

Heir(s) / Authorized Representative

Visit Real Estate Registration Trustee Centre *(C2: assisted mode)*  
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
Approved — Awaiting Payment  
↓  
Completed

### Additional Statuses

* Rejected  
* Withdrawn

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
* Payment Receipts — sourced (row 40); a payment receipt (B9), not a fee balance

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
* Payment is completed at the counter with a payment receipt issued.  
* Each heir's share is transferred to their nominated bank account upon approval.  
* Certificate of Title, Title Deed, and Map are generated upon completion.  
* All heirs receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Trustee Centre operator, acting on the heirs' behalf, may process this application. *(Proposed — A4 re-derivation; the source assigns this to the Mortgage Officer.)*
2. Heirship must be established by valid probate or administration documentation before the sale can proceed.  
3. Payment is required at the counter before the application is finalized.  
4. Each heir's share of proceeds is distributed to their nominated bank account as part of completion.  
5. Approved applications update the official property ownership registry.  
6. Every application receives a unique application reference number.  
7. All applications, approvals, payments, distributions, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **How disputes among heirs over shares are handled** within this workflow. Not specified in source.  
2. **Validation method for bank account details** used for distribution (e.g., account-name matching against the heir's identity). Not specified in source.  
3. **Exact fee amount.** Client data — see `open-questions.md` B5.
