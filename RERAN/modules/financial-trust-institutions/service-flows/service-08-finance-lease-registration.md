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
  - finance-lease
---

# Service #8 – Finance Lease Registration

**Service Category:** Finance Lease Services

**Source row:** 34 of `RERAN_service_flows_v2.md`. This is the reference workflow for the finance-lease lifecycle — Services #9 (amendment), #10 (transfer) and #11 (release) are defined by the source as variants of this flow and are expanded in full in their own documents.

## 1. Service Overview

The **Finance Lease Registration** service records a new finance lease against a registered property — the lessor institution retains legal title while the lessee holds a registered right to use the property under lease terms — subject to internal certification and RERA audit.

## 2. Purpose

Register a finance lease against a verified title so the lessor institution's leasing interest and the lessee's rights of use are both legally recognized on the property registry.

## 3. Description

The customer (lessee) completes the finance lease arrangement with the institution. The transaction is entered and submitted at a Real Estate Registration Trustee Centre, where documents are submitted, the transaction is entered into the system, the fee is paid, and outputs are delivered by email. Per C2, this is the same online service in assisted mode, not a separate paper channel.

## 4. Who Can Apply

### Applicant (Lessor Institution)

* Mortgage Officer — owns the finance-lease lifecycle per the source's responsible-role column and the A4 re-derivation  
* Trustee Centre Operator (Group G) — assisted mode, entering the transaction on the institution's behalf at the Trustee Centre (C2)

### Counterparty (Lessee)

* Registered Individual User or Eligible Property User who is party to the finance lease

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with a Mortgage Officer provisioned.  
* Property is registered with RERAN and its title is verified.  
* Lessor and lessee have agreed finance lease terms before system entry.  
* Institution's settlement account holds a sufficient prefunded balance to absorb the fee once approved (B1, B4).

## 6. Required Information

### Institution (Lessor) Information

* Institution Name  
* Mortgage Officer / Officer Identifier

### Lessee Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Finance Lease Information

* Lease Term  
* Lease Payment Schedule  
* Residual / Purchase Option Terms, if any

## 7. Required Documents

> **Proposed** — the source states only that documents are submitted, without enumerating them. The list below is proposed by analogy with Service #3 and what a finance lease registration plainly requires.

* Existing Certificate of Title  
* Finance Lease Agreement / Deed of Finance Lease  
* Lease Payment Schedule  
* Government-issued Identification (Lessee)  
* Government-issued Identification (Lessor Institution Representative)  
* Internal Certification Record  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Proposed** — ad valorem/banded basis per B6, applied to the leased asset's value. Exact schedule is client data (B5).

## 9. Payment Required

**Yes**

> **Proposed / flagged** — row 34 lists "Fee balance (all e-deliverables)" among the issued outputs, the same evidentiary basis `open-questions.md` B1 uses to establish the Institution Account Debit model for the mortgage services, and B1 explicitly cites "every Group C mortgage **and finance-lease** row" as support. This document follows B1 and treats the fee as deducted from the institution's settlement account after approval. However, row 34's workflow text itself reads as a counter transaction ("submit docs, enter system, **pay**, receive output via email"), which looks like a point-of-sale payment rather than an account debit. This tension is not resolved by source and is carried forward — see Open Questions.

## 10. Processing Authority

**Two gates**, by extension of the pattern established for mortgage services, since finance lease shares the same Mortgage Officer ownership and Compliance & Escrow Auditor approval:

1. **Internal Certifier** — checker permission scope (A1/D2).  
2. **Compliance & Escrow Auditor** (Group A).

> **Proposed** — row 34 does not explicitly mention an internal bank-auditor step (unlike rows 30–33, 39, which say "audited by bank auditor"). This is inferred by extension from the mortgage lifecycle sharing the same institutional owner. See Open Questions.

## 11. Expected Processing Time

**30–35 minutes.** Sourced from row 34 — the longest SLA of any Group C service, consistent with a full lease registration rather than a lifecycle amendment.

## 12. Processing Workflow

Lessee & Lessor Institution

Agree Finance Lease Terms

↓

Mortgage Officer / Trustee Centre Operator

Visit Real Estate Registration Trustee Centre *(C2: assisted mode of the same online service)*  
↓  
Submit Required Documents  
↓  
Enter Finance Lease Transaction into System  
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

* Finance Lease Successfully Registered  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Insufficient Settlement Balance / Payment Failed  
* Approval Expired  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Certificate of Title / Title Deed — sourced (row 34)  
* Map — sourced (row 34); finance lease services list a Map among outputs where the mortgage services do not  
* Fee Balance — settlement-account statement line, not a receipt (B9)

## 16. Related Services

* Service #9 — Finance Lease Amendment  
* Service #10 — Finance Lease Transfer  
* Service #11 — Finance Lease Release  
* Service #3 — Mortgage Registration *(parallel lifecycle, different instrument)*

## 17. UI Screens

* Services  
* Finance Lease Registration  
* Select Property  
* Lessee Information  
* Finance Lease Information  
* Document Upload  
* Internal Certification Queue  
* Application Review  
* Settlement Account Confirmation  
* Application Submitted  
* Application Details  
* Registration Confirmation

## 18. API Requirements

* Retrieve Institution Properties  
* Retrieve Property Details  
* Validate Property Ownership  
* Validate Title Status  
* Upload Documents  
* Submit for Internal Certification  
* Retrieve Certification Status  
* Calculate Service Fee  
* Check Settlement Account Balance  
* Submit Finance Lease Registration Application  
* Retrieve Application Status  
* Deduct Settlement Account Fee  
* Generate Certificate of Title  
* Generate Map  
* Update Finance Lease Registry  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff  
* Permission Scope  
* Property  
* Property Ownership  
* Finance Lease  
* Certification Record  
* Application  
* Service Request  
* Document  
* Settlement Account  
* Settlement Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Mortgage Officer (or Trustee Centre operator, in assisted mode) can initiate finance lease registration against a registered title.  
* System validates the property is registered and its title is verified.  
* Internal certifier can certify or return the transaction before it reaches RERA.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is deducted from the institution's settlement account only after approval.  
* Application receives a unique application reference number.  
* Approved registrations update the official finance lease registry.  
* Institution and lessee receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Mortgage Officer acting under the lessor institution's corporate account, or a Trustee Centre operator acting on its behalf, may initiate finance lease registration.  
2. The property must be registered with RERAN and its title verified.  
3. The transaction must pass internal institutional certification before routing to RERA. *(Proposed by extension — not explicit in row 34; see Open Questions.)*  
4. Payment is deducted from the institution's settlement account only after RERA approval (B1, proposed for finance lease by extension).  
5. Submission is blocked if the projected settlement balance after fees would go negative (B4).  
6. An approved but unsettled transaction lapses to Expired after 30 calendar days (B3).  
7. Every application receives a unique application reference number.  
8. All applications, certifications, approvals, settlement deductions, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Does an internal bank-auditor certification step apply to finance lease services**, as it does to mortgage services? Row 34 does not state it explicitly, unlike rows 30–33 and 39.  
2. **Is the "pay" step at the Trustee Centre a settlement-account deduction or a direct counter payment?** B1's account-debit reasoning is inferred from the "Fee balance" output, but the workflow text reads as a point-of-sale transaction. Not resolved by source.  
3. **Does an online (non-Trustee-Centre) channel exist for finance lease services**, comparable to the Online Mortgage System for mortgage services? Row 34 names only the Trustee Centre.  
4. **Exact fee schedule.** Client data — see `open-questions.md` B5, B6.
