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

The customer prepares the mortgage requirements with the bank. A Mortgage Officer enters the transaction documents through the Online Mortgage System; it is audited by the bank's internal auditor before being sent to RERA, where fees are deducted from the bank's settlement account. Outputs are delivered to the customer by email.

> **Proposed / flagged** — row 39's workflow text is nearly identical to Service #3 (Mortgage Registration, row 30): both describe a bank employee entering documents via the online mortgage system, internal bank-auditor certification, RERA audit, account-debited fees, and email delivery. The source does not state what functionally distinguishes "granting" a mortgage from "registering" one. One plausible reading is that Grant Property Mortgage is the bank's origination of a new loan secured by the property (the lending event itself), while Mortgage Registration records an already-arranged mortgage onto the RERAN registry. This distinction is not confirmed by source and is flagged for the client — see Open Questions and the PR's template-fit notes.

## 4. Who Can Apply

### Applicant (Lending Institution)

* Mortgage Officer

> Unlike Services #3–#6, row 39 names only the **Land Department website (online mortgage system)** as channel — no Trustee Centre alternative is listed. This document does not add an assisted-mode variant here, since none is sourced; see `services-overview.md` C2 for the general principle that Trustee Centre access is documented only where the source supports it.

### Counterparty (Borrower / Property Owner)

* Registered Property Owner receiving the mortgage-secured loan

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with a Mortgage Officer provisioned.  
* Property is registered with RERAN and its title is verified.  
* Customer has prepared mortgage requirements with the bank (loan approval, valuation) before system entry.  
* Institution's settlement account holds a sufficient prefunded balance to absorb the fee once approved (B1, B4).

## 6. Required Information

### Institution Information

* Institution Name  
* Mortgage Officer Identifier

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

> **Proposed** — ad valorem/banded basis per B6. Exact schedule is client data (B5).

## 9. Payment Required

**Yes**

Deducted from the institution's settlement account after RERA approval — sourced (row 39: "fees deducted from bank account"), same Institution Account Debit mechanism as Service #3 (B1).

> **Proposed / flagged** — row 39 names the output artefact "**Payment receipts**," not "Fee balance" as rows 30, 31, 32, 33, and 34–37 all do. B9 reasons that "fee balance" (a standing-account statement line) is the correct artefact wherever the account-debit mechanism applies, and every other institution-account-debit mortgage row uses that term. This row is the one exception in the source, and it is preserved as sourced rather than silently normalized to match the pattern — see Section 15 and Open Questions.

## 10. Processing Authority

**Two gates**, sourced from row 39 ("audited by bank auditor" before being "sent to Department"):

1. **Internal Certifier** — checker permission scope (A1/D2).  
2. **Compliance & Escrow Auditor** (Group A).

## 11. Expected Processing Time

**15–20 minutes.** Per the issue's row-to-file mapping (row 39's SLA is assigned to this file).

## 12. Processing Workflow

Borrower (Customer)

Prepare Mortgage Requirements with Bank

↓

Mortgage Officer

Login to Online Mortgage System  
↓  
Enter Borrower & Property/Mortgage Information  
↓  
Upload Required Documents  
↓  
Submit for Internal Certification

↓

Internal Certifier

Review Transaction  
↓  
Certify, or Return to Mortgage Officer

↓

RERA

Receive Transaction in Transaction Audit Queue  
↓  
Audit Transaction  
↓  
Approve, Return, or Reject  
↓  
Deduct Fee from Institution Settlement Account  
↓  
Generate Output Documents  
↓  
Deliver Outputs to Customer via Email

## 13. Application Status Flow

Draft  
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
Approved — Awaiting Payment  
↓  
Completed

### Additional Statuses

* Returned by Certifier  
* Rejected  
* Withdrawn  
* Expired *(B3)*

## 14. Possible Outcomes

* Mortgage Successfully Granted  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Insufficient Settlement Balance / Payment Failed  
* Approval Expired  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Payment Receipts — sourced (row 39), the only mortgage-service row that uses this term instead of "Fee balance"

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
* Settlement Account Confirmation  
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
* Check Settlement Account Balance  
* Submit Mortgage Grant Application  
* Retrieve Application Status  
* Deduct Settlement Account Fee  
* Generate Payment Receipt  
* Update Mortgage Registry  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff  
* Permission Scope  
* Property  
* Mortgage  
* Certification Record  
* Application  
* Service Request  
* Document  
* Settlement Account  
* Settlement Transaction  
* Payment Receipt  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Mortgage Officer can initiate a mortgage grant against a registered title.  
* System validates the property is registered and its title is verified.  
* Internal certifier can certify or return the transaction before it reaches RERA.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is deducted from the institution's settlement account only after approval.  
* Application receives a unique application reference number.  
* Approved grants update the official mortgage registry.  
* Institution and customer receive completion notifications, including a payment receipt.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Mortgage Officer acting under the lending institution's corporate account may initiate a mortgage grant.  
2. The property must be registered with RERAN and its title verified.  
3. The transaction must pass internal institutional certification before routing to RERA.  
4. Payment is deducted from the institution's settlement account only after RERA approval (B1).  
5. Submission is blocked if the projected settlement balance after fees would go negative (B4).  
6. An approved but unsettled transaction lapses to Expired after 30 calendar days (B3).  
7. Every application receives a unique application reference number.  
8. All applications, certifications, approvals, settlement deductions, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **What functionally distinguishes "Grant Property Mortgage" from "Mortgage Registration" (Service #3)?** The source's workflow text for both is nearly identical, and this is flagged in the PR as a template-fit issue rather than resolved by inference.  
2. **Why does row 39 name "Payment receipts" as output instead of "Fee balance,"** when its fee mechanism (deduction from the bank's account) matches the other institution-account-debit mortgage services? Not resolved — recorded as sourced rather than normalized.  
3. **Whether an assisted Trustee-Centre mode genuinely does not exist for this service**, or whether its absence from row 39 is an omission in the source workbook (every other mortgage-lifecycle row lists one). Not specified.  
4. **Exact fee schedule.** Client data — see `open-questions.md` B5, B6.
