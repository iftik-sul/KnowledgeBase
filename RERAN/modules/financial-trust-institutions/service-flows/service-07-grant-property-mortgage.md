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
  - "RERAN/modules/financial-trust-institutions/service-flows/service-03-mortgage-registration.md"
tags:
  - financial-trust-institutions
  - service-flow
  - mortgage
---

# Service #7 – Grant Property Mortgage

**Service Category:** Mortgage Services

**Source row:** **39** of `RERAN_service_flows_v2.md`. Row order in the source is not file order — row 39 maps to this file (Service #7), not row 34. See the issue's row-to-file mapping table.

## 1. Service Overview

The **Grant Property Mortgage** service records the bank's origination of a mortgage secured by a customer's property, entered by the bank, audited internally, and audited by RERA before the fee is settled and outputs are delivered.

## 2. Purpose

Give legal and registry effect to a bank's grant of a property-secured loan, so the mortgage is recognized on the property record from the point of origination.

## 3. Description

The customer prepares the mortgage requirements with the bank. Any of the institution's four Group C roles enters the transaction documents through the Online Mortgage System and pays the fee upfront via the shared platform payment gateway; it is audited by the bank's internal auditor before being sent to RERA. Outputs are delivered to the customer by email.

> **Proposed / flagged** — row 39's workflow text is nearly identical to Service #3 (Mortgage Registration, row 30): both describe a bank employee entering documents via the online mortgage system, internal bank-auditor certification, RERA audit, account-debited fees, and email delivery. The source does not state what functionally distinguishes "granting" a mortgage from "registering" one. One plausible reading is that Grant Property Mortgage is the bank's origination of a new loan secured by the property (the lending event itself), while Mortgage Registration records an already-arranged mortgage onto the RERAN registry. This distinction is not confirmed by source and is flagged for the client — see Open Questions and the PR's template-fit notes.

## 4. Who Can Apply

### Applicant (Lending Institution)

* Any of the institution's four Group C roles. **Confirmed 2026-08-15** — previously listed as Mortgage Officer only; `open-questions.md` A4 confirms no service is role-specific.

> Unlike Services #3–#6, row 39 names only the **Land Department website (online mortgage system)** as channel — no Trustee Centre alternative is listed. This document does not add an assisted-mode variant here, since none is sourced; see `services-overview.md` C2 for the general principle that Trustee Centre access is documented only where the source supports it.

### Counterparty (Borrower / Property Owner)

* Registered Property Owner receiving the mortgage-secured loan

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with staff provisioned.  
* Property is registered with RERAN and its title is verified.  
* Customer has prepared mortgage requirements with the bank (loan approval, valuation) before system entry.  
* Payment has been completed via the shared platform payment gateway before the application is lodged (B1).

## 6. Required Information

### Institution Information

* Institution Name  
* Acting Officer Identifier

### Borrower (Property Owner) Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information

### Property & Mortgage Information

* Property Registration Number  
* Loan Amount  
* Mortgage Term  
* Interest Rate

## 7. Required Documents

> **Proposed** — by analogy with Service #3, since row 39 does not enumerate documents beyond "docs."

* Existing Certificate of Title  
* Mortgage Agreement / Deed of Mortgage  
* Loan Offer Letter  
* Property Valuation Report  
* Government-issued Identification (Borrower)  
* Internal Certification Record  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Corrected 2026-08-14** — per the corrected `open-questions.md` B6, RERA sets this fee directly, per service code. Previously proposed as ad valorem/banded; that basis is retired. The exact fee is a configuration fact (B5), not client data awaiting collection.

## 9. Payment Required

**Yes**

Paid upfront by the institution via the shared platform payment gateway, before the application is lodged. Row 39's source text — "fees deducted from bank account" — is read as describing the payment *method* (a bank-transfer rail on the shared gateway), not a standing-account debit mechanism.

> **Corrected 2026-08-14 — this row's terminology was right all along.** Row 39 names the output artefact "**Payment receipts**," which this document previously treated as the one exception against rows 30–37's "Fee balance" pattern (`open-questions.md` B9, now superseded). With B9 superseded and no standing account left to produce a "balance," row 39's "Payment receipts" is the terminology every mortgage-service row should be read as matching — not an anomaly to preserve as-sourced-but-different. See Section 15.

## 10. Processing Authority

**Two gates**, sourced from row 39 ("audited by bank auditor" before being "sent to Department"):

1. **Internal Certifier** — a functional label, not a role or scope: any of the institution's four Group C users may act as internal certifier, including the person who filed the transaction. **Corrected 2026-08-14** — previously `checker permission scope` (A1/D2), now retired; see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).  
2. **Compliance & Escrow Auditor** (Group A).

## 11. Expected Processing Time

**15–20 minutes.** Per the issue's row-to-file mapping (row 39's SLA is assigned to this file).

## 12. Processing Workflow

Borrower (Customer)

Prepare Mortgage Requirements with Bank

↓

Institution User (any of the four Group C roles)

Login to Online Mortgage System  
↓  
Enter Borrower & Property/Mortgage Information  
↓  
Upload Required Documents  
↓  
Pay via Shared Platform Gateway  
↓  
Submit for Internal Certification

↓

Internal Certifier

Review Transaction  
↓  
Certify, or Return to Filer

↓

RERA

Receive Transaction in Transaction Audit Queue  
↓  
Audit Transaction  
↓  
Approve, Return, or Reject  
↓  
Generate Output Documents  
↓  
Deliver Outputs to Customer via Email

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
↓  
Pending Internal Certification  
↓  
*(Returned by Certifier → back to Draft)*  
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

* Payment Failed *(retryable, pre-lodging — see [payments.md](../payments.md))*  
* Returned by Certifier  
* Rejected  
* Withdrawn

**Corrected 2026-08-14** — `Approved — Awaiting Payment` and `Expired` (B3) removed; see Service #3's Application Status Flow section for the reasoning, which applies identically here.

## 14. Possible Outcomes

* Mortgage Successfully Granted  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Payment Receipts — sourced (row 39). **Corrected 2026-08-14**: previously flagged as the only mortgage-service row using this term instead of "Fee balance"; now understood as the universal pattern every mortgage-service row follows, since "Fee balance" no longer describes anything (B9 superseded, see [payments.md](../payments.md))

## 16. Related Services

* Service #3 — Mortgage Registration  
* Service #4 — Mortgage Amendment  
* Service #5 — Mortgage Transfer  
* Service #6 — Mortgage Release  
* Individual-user Service #8 — Register Sale of Mortgaged Property *(cross-module)*

## 17. UI Screens

* Services  
* Grant Property Mortgage  
* Borrower Information  
* Property & Mortgage Information  
* Document Upload  
* Internal Certification Queue  
* Application Review  
* Payment Confirmation
* Application Submitted  
* Application Details  
* Grant Confirmation

## 18. API Requirements

* Retrieve Property Details  
* Validate Property Ownership  
* Validate Title Status  
* Upload Documents  
* Submit for Internal Certification  
* Retrieve Certification Status  
* Calculate Service Fee  
* Verify Payment Status
* Submit Mortgage Grant Application  
* Retrieve Application Status  
* Process Gateway Payment
* Generate Payment Receipt  
* Update Mortgage Registry  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff *(no scope field — every staff member has identical system access; role is recorded per-action, not per-account)*  
* Property  
* Mortgage  
* Certification Record *(now includes the acting user and their role at time of certification, per [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle) — not a scope reference)*  
* Application  
* Service Request  
* Document  
* Payment Receipt  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can initiate a mortgage grant against a registered title. **Confirmed 2026-08-15** — not restricted to the Mortgage Officer (A4).  
* System validates the property is registered and its title is verified.  
* Internal certifier — any of the four Group C roles, including the filer — can certify or return the transaction before it reaches RERA.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is paid via the shared platform payment gateway before the application is lodged.  
* Application receives a unique application reference number.  
* Approved grants update the official mortgage registry.  
* Institution and customer receive completion notifications, including a payment receipt.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the institution's four Group C roles acting under the lending institution's corporate account may initiate a mortgage grant. **Confirmed 2026-08-15** — previously restricted to "only a Mortgage Officer"; `open-questions.md` A4 confirms no service is role-specific.  
2. The property must be registered with RERAN and its title verified.  
3. The transaction must pass internal institutional certification before routing to RERA.  
4. Payment is made via the shared platform payment gateway, upfront, before the application can be lodged — not deducted from a settlement account (B1, corrected 2026-08-14).  
5. **Corrected 2026-08-14** — the previous low-balance-warning and 30-day-expiry rules (B4, B3) are removed; see Service #3's Business Rules for the reasoning, which applies identically here.  
6. Every application receives a unique application reference number.  
7. All applications, certifications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **What functionally distinguishes "Grant Property Mortgage" from "Mortgage Registration" (Service #3)?** The source's workflow text for both is nearly identical, and this is flagged in the PR as a template-fit issue rather than resolved by inference.  
2. **Why does row 39 name "Payment receipts" as output instead of "Fee balance,"** when its fee mechanism (deduction from the bank's account) matches the other institution-account-debit mortgage services? Not resolved — recorded as sourced rather than normalized.  
3. **Whether an assisted Trustee-Centre mode genuinely does not exist for this service**, or whether its absence from row 39 is an omission in the source workbook (every other mortgage-lifecycle row lists one). Not specified.  
4. **Exact fee schedule.** Client data — see `open-questions.md` B5, B6.
