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
  - "RERAN/modules/financial-trust-institutions/service-flows/service-03-mortgage-registration.md"
tags:
  - financial-trust-institutions
  - service-flow
  - mortgage
  - transfer
---

# Service #5 – Mortgage Transfer

**Service Category:** Mortgage Services

**Source row:** 32 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as mortgage registration" — for both its bank-originated and Trustee-Centre-assisted variants. Expanded in full below, per the issue's instruction not to reproduce the bare cross-reference.

## 1. Service Overview

The **Mortgage Transfer** service changes the registered mortgagee of an existing mortgage — for example, when one lender assigns its secured interest to another institution. Unlike registration, transfer does not create a new encumbrance; unlike release, it does not discharge one. It reassigns an existing encumbrance to a new holder of record.

## 2. Purpose

Keep the property registry accurate when the beneficiary of a registered mortgage changes, so a title search reflects the true current mortgagee.

## 3. Description

The outgoing and incoming institutions agree the assignment of the mortgage. A Mortgage Officer at the transferring (or receiving) institution enters the transfer into the Online Mortgage System against the existing mortgage record, attaching the assignment documentation and the new mortgagee's details. The transaction is certified internally, then audited by RERA using the same workflow structure as mortgage registration (Service #3). On approval, the fee is deducted from the initiating institution's settlement account and the updated output documents are delivered to the customer by email. The service can alternatively be processed in assisted mode at a Real Estate Registration Trustee Centre.

## 4. Who Can Apply

### Applicant (Transferring or Receiving Institution)

* Mortgage Officer — primary channel, via the Online Mortgage System  
* Trustee Centre Operator (Group G) — assisted mode (C2)

### Counterparty (Borrower / Property Owner)

* The registered mortgagor of the mortgage being transferred, whose consent to the transfer is required

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with a Mortgage Officer provisioned.  
* An existing, active registered mortgage against the property.  
* The receiving institution is itself a registered RERAN Group C institution able to hold a registered mortgage.  
* Institution's settlement account holds a sufficient prefunded balance to absorb the fee once approved (B1, B4).

## 6. Required Information

### Existing Mortgage Reference

* Mortgage Registration Number  
* Property Registration Number  
* Current Mortgagee (Institution) Details

### Transfer Information

* New Mortgagee (Institution) Details  
* Effective Date of Transfer  
* Reason / Basis for Transfer (e.g., loan assignment, portfolio sale)

## 7. Required Documents

> **Proposed** — by analogy with Service #3 and what a mortgage assignment plainly requires.

* Existing Certificate of Title / Title Deed  
* Original Mortgage Agreement  
* Deed of Assignment / Novation Agreement  
* Consent of the Existing Mortgagee  
* Consent of the Mortgagor (Property Owner), where required  
* Government-issued Identification (Parties)  
* Internal Certification Record  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Proposed** — ad valorem/banded basis per B6. Exact schedule is client data (B5).

## 9. Payment Required

**Yes** — Institution Account Debit model (B1), same structure as Service #3. Deducted from the initiating institution's settlement account after RERA approval.

> **Proposed** — the source does not specify whether the fee is charged to the transferring or the receiving institution's settlement account when the two differ. See Open Questions.

## 10. Processing Authority

**Two gates**, same structure as Service #3:

1. **Internal Certifier** — a functional label, not a role or scope: any of the initiating institution's four Group C users may act as internal certifier, including the person who filed the transaction. **Corrected 2026-08-14** — previously `checker permission scope` (A1/D2), now retired; see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).  
2. **Compliance & Escrow Auditor** (Group A).

## 11. Expected Processing Time

**15–20 minutes.** Sourced from row 32 as a single end-to-end figure.

## 12. Processing Workflow

Transferring & Receiving Institutions

Agree Terms of Mortgage Assignment  
↓  
Obtain Mortgagor's Consent, Where Required

↓

Mortgage Officer (Initiating Institution)

Login to Online Mortgage System  
↓  
Select Existing Mortgage Record  
↓  
Enter New Mortgagee & Transfer Details  
↓  
Upload Assignment Documents  
↓  
Submit for Internal Certification

↓

Internal Certifier

Review Transfer  
↓  
Certify, or Return to Mortgage Officer

↓

RERA

Receive in Transaction Audit Queue  
↓  
Audit Transfer  
↓  
Approve, Return, or Reject  
↓  
Deduct Fee from Institution Settlement Account  
↓  
Generate Updated Output Documents  
↓  
Deliver Outputs to Customer via Email

### Assisted-Mode Alternative (C2)

Trustee Centre Operator

Visit Real Estate Registration Trustee Centre  
↓  
Submit Documents  
↓  
Enter Transfer into System on the Institution's Behalf  
↓  
Pay Fees at Counter  
↓  
Receive Output via Email

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

* Mortgage Successfully Transferred  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Insufficient Settlement Balance / Payment Failed  
* Approval Expired  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* The applicable one of: Certificate of Title / Title Deed / Usufruct Title Deed / Statement Certificate / Provisional Sale Registration Certificate, reissued naming the new mortgagee — sourced (row 32)  
* Fee Balance — settlement-account statement line, not a receipt (B9)

## 16. Related Services

* Service #3 — Mortgage Registration  
* Service #4 — Mortgage Amendment  
* Service #6 — Mortgage Release  
* Individual-user Service #8 — Register Sale of Mortgaged Property *(cross-module)*

## 17. UI Screens

* Services  
* Mortgage Transfer  
* Select Existing Mortgage  
* New Mortgagee Information  
* Document Upload  
* Internal Certification Queue  
* Application Review  
* Settlement Account Confirmation  
* Application Submitted  
* Application Details  
* Transfer Confirmation

## 18. API Requirements

* Retrieve Existing Mortgage Record  
* Validate Mortgage Status  
* Validate Receiving Institution Standing  
* Upload Documents  
* Submit for Internal Certification  
* Retrieve Certification Status  
* Calculate Service Fee  
* Check Settlement Account Balance  
* Submit Mortgage Transfer Application  
* Retrieve Application Status  
* Deduct Settlement Account Fee  
* Generate Updated Certificate / Statement Certificate  
* Update Mortgage Registry  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff *(no scope field — every staff member has identical system access; role is recorded per-action, not per-account)*  
* Property  
* Mortgage  
* Mortgage Transfer  
* Certification Record *(now includes the acting user and their role at time of certification, per [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle) — not a scope reference)*  
* Application  
* Service Request  
* Document  
* Settlement Account  
* Settlement Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Mortgage Officer can select an existing mortgage and submit transfer details naming a new mortgagee.  
* System validates the mortgage is active and the receiving institution holds valid RERAN standing.  
* Internal certifier — any of the four Group C roles, including the filer — can certify or return the transfer before it reaches RERA.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is deducted from the initiating institution's settlement account only after approval.  
* Application receives a unique application reference number.  
* Approved transfers update the official mortgage registry with the new mortgagee.  
* All parties receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Mortgage Officer, or a Trustee Centre operator acting on an institution's behalf, may initiate a transfer.  
2. The mortgage being transferred must be active and registered.  
3. The receiving institution must hold valid RERAN Group C standing able to hold a registered mortgage.  
4. The transaction must pass internal institutional certification before routing to RERA.  
5. Payment is deducted from the initiating institution's settlement account only after approval (B1).  
6. Submission is blocked if the projected settlement balance after fees would go negative (B4).  
7. An approved but unsettled transaction lapses to Expired after 30 calendar days (B3).  
8. Every application receives a unique application reference number.  
9. All applications, certifications, approvals, settlement deductions, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Which institution's settlement account is debited** — the transferring institution's or the receiving institution's — when they differ? Not specified in source.  
2. **Whether mortgagor consent is mandatory for every transfer**, or only for certain transfer bases (e.g., loan-portfolio sale vs. internal restructuring). Not specified in source.  
3. **Exact fee schedule for transfers.** Client data — see `open-questions.md` B5, B6.
