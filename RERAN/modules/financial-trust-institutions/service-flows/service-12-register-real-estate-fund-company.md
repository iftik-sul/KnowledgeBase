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
tags:
  - financial-trust-institutions
  - service-flow
  - title-ownership
  - real-estate-fund
---

# Service #12 – Registration of Real Estate Fund Companies in the Register of Privileges

**Service Category:** Title & Ownership Transaction Services

**Source row:** **38** of `RERAN_service_flows_v2.md`. Row order in the source is not file order — row 38 maps to this file (Service #12), not row 12. See the issue's row-to-file mapping table; rows 38 and 39 are transposed against file order.

## 1. Service Overview

The **Registration of Real Estate Fund Companies in the Register of Privileges** service records a real estate fund company's ownership interest in the register of privileges — a specific ownership register distinct from an ordinary property title — and issues an ownership certificate and registration record to the fund company.

## 2. Purpose

Give a real estate fund company's ownership interest formal, searchable standing in RERA's register of privileges, distinct from and in addition to ordinary property title registration.

## 3. Description

The fund company's representative visits a Real Estate Registration Trustee Centre and submits the required documents. A Trustee Centre operator enters the transaction data, checks it, and forwards it for approval. The customer pays the fee at the counter and receives an e-receipt. On completion, the customer receives an ownership certificate by email and a document confirming the registration number assigned in the privilege register.

## 4. Who Can Apply

### Applicant

* Mortgage Officer — where the transaction is bank-originated (A4's conditional)
* Trustee Centre Operator (Group G) — otherwise, acting on the fund company's behalf in assisted mode

> **Proposed** — the source assigns responsible role to the **Mortgage Officer**, but row 38's workflow shows no bank-employee or online-mortgage-system involvement: "Customer visits Real Estate Services Registration Trustees Centers. → Submit documents. → Employee enters all transaction data, checks and approves." `open-questions.md` A4's rule is conditional — "Mortgage Officer where bank-originated; otherwise executed by a Trustee Centre operator on the customer's behalf" — not an unconditional reassignment. This document keeps both branches: the Trustee Centre Operator path is what row 38 itself sources; the Mortgage Officer / bank-originated branch is preserved because A4 allows for it in principle, but **no row among the title & ownership transaction rows (38, 40–44) describes a bank-originated workflow**, so that branch is not sourced here and is carried forward as an open question rather than asserted as fact or silently dropped. **Confidence: Medium**, per the answers doc — the Trustee-Centre branch contradicts the source's responsible-role column, and that should be visible to the client.

### Customer

* The real estate fund company's authorized representative

## 5. Prerequisites

* The real estate fund company is validly constituted.  
* The fund company's interest is capable of registration in the register of privileges.  
* Required supporting documents are available.

## 6. Required Information

### Fund Company Information

* Fund Company Legal Name  
* Certificate of Incorporation Number  
* Authorized Representative Details

### Registration Information

* Nature of the Privilege / Interest Being Registered  
* Property or Asset Reference, Where Applicable

## 7. Required Documents

> **Proposed** — the source states only that "documents" are submitted, without enumerating them.

* Certificate of Incorporation of the Fund Company  
* Trust Deed / Fund Constitution  
* Register of Privileges Application Form  
* List of Unit Holders / Beneficial Owners  
* Government-issued Identification (Authorized Representative)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Paid by the customer (the fund company) at the Trustee Centre counter, and an e-receipt is issued — sourced (row 38: "Customer pays fees and obtains e-receipt"). This is the **Customer Payment at Counter** model, unaffected by the 2026-08-14 payment-model correction (`open-questions.md` B1) — this service was never account-debited, so it's a receipt here as it always was. **Corrected 2026-08-14** — previously cited `B9` for the receipt-vs-fee-balance distinction; B9 is now superseded, since no Group C service produces a "fee balance" any more.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced directly from row 38's approver column, as it is for every Group C service.

> **Proposed** — row 38's workflow text separately describes an "Employee [who] enters all transaction data, checks and approves." Whether that check-and-approve step *is* the Compliance & Escrow Auditor's regulatory review, or a preliminary Trustee Centre check distinct from a separate RERA audit step, is not stated in source — the two are bundled into one clause. This document treats the workflow's "checks and approves" as the Group A approval gate itself, since no internal institutional certification step applies here (no corporate account originates this transaction) — but that specific mapping is an inference, not a sourced fact, and is labeled as such rather than folded into the sourced claim above. *(Wording corrected 2026-08-14 — previously "no institutional maker-checker layer applies here"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).)*

## 11. Expected Processing Time

**25–30 minutes.** Sourced from row 38.

## 12. Processing Workflow

Customer (Fund Company Representative)

Visit Real Estate Registration Trustee Centre *(C2: this is the sourced path for this service; Section 4 carries A4's Mortgage Officer / bank-originated branch as unconfirmed rather than asserting a direct online path here — see Open Questions)*  
↓  
Submit Required Documents

↓

Trustee Centre Operator

Enter Transaction Data  
↓  
Check Transaction

↓

RERA (Compliance & Escrow Auditor)

Approve, Return, or Reject

↓

Customer

Pay Fees at Counter  
↓  
Obtain e-Receipt

↓

RERA

Generate Ownership Certificate  
↓  
Deliver Ownership Certificate via Email  
↓  
Issue Register of Privileges Registration Number  
↓  
Deliver Registration Document via Email

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

> Does not carry the Group C `Pending Internal Certification` / `Returned by Certifier` extension: this service is executed by a Trustee Centre operator on the customer's behalf, not by institutional staff performing an internal certify-or-return step. *(Wording corrected 2026-08-14 — previously "under a maker-checker scope (A1/D2)"; permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).)*

## 14. Possible Outcomes

* Fund Company Successfully Registered in the Register of Privileges  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* E-Ownership Certificate in the Name of the Real Estate Fund — sourced (row 38)  
* Receipt for Fees — sourced (row 38), a payment receipt, the same artefact every Group C service now issues (see [payments.md](../payments.md))  
* Register of Privileges Registration Number Document — sourced (row 38)

## 16. Related Services

* Service #13 — Sale Procedure (Heirs)  
* Service #14 — Company Shares Sale  
* Service #17 — Issuance of Title Deed

## 17. UI Screens

* Services  
* Register Real Estate Fund Company  
* Fund Company Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Ownership Certificate  
* Registration Confirmation

## 18. API Requirements

* Validate Fund Company Constitution  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Register of Privileges Application  
* Retrieve Application Status  
* Assign Register of Privileges Registration Number  
* Generate Ownership Certificate  
* Send Notifications

## 19. Database Entities

* User  
* Fund Company  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Register of Privileges Entry  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Fund company representative can initiate registration at a Trustee Centre.  
* Required information and documents are validated before submission.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Payment is completed and an e-receipt issued before completion.  
* Approved applications update the official register of privileges.  
* Ownership certificate and registration number document are generated on completion.  
* Customer receives completion notification.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. This application may be processed by a Mortgage Officer where bank-originated, or otherwise by a Trustee Centre operator acting on the fund company's behalf (A4's conditional). *(Proposed — no row sources a bank-originated variant for this service; only the Trustee-Centre path is confirmed by row 38.)*
2. The fund company must be validly constituted before its interest can be registered.  
3. Payment is required at the counter before the application is finalized, and an e-receipt is issued as proof.  
4. Approved registrations update the official register of privileges.  
5. Every application receives a unique application reference number.  
6. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Eligibility criteria for what qualifies as a "real estate fund company"** for register-of-privileges purposes. Not specified in source.  
2. **Relationship between the register of privileges and the ordinary property title register** — whether registration here also requires or triggers a separate title registration. Not specified in source.  
3. **Whether a bank-originated path (Mortgage Officer, per A4's conditional) exists for this service at all.** No row among 38, 40–44 describes bank-employee entry the way the mortgage rows (30–33, 39) do; this document sources only the Trustee-Centre-assisted path and treats the bank-originated branch as unconfirmed rather than absent.  
4. **Exact fee amount.** Client data — see `open-questions.md` B5.
