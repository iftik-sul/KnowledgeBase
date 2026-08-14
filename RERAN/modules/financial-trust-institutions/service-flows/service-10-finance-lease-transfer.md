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
  - "RERAN/modules/financial-trust-institutions/service-flows/service-08-finance-lease-registration.md"
tags:
  - financial-trust-institutions
  - service-flow
  - finance-lease
  - transfer
---

# Service #10 – Finance Lease Transfer

**Service Category:** Finance Lease Services

**Source row:** 36 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as finance lease registration" — expanded in full below.

## 1. Service Overview

The **Finance Lease Transfer** service changes the registered lessor (or, where legally permitted, lessee) of record on an existing finance lease — for example, when the lessor institution assigns its leasing interest to another institution. It reassigns an existing lease rather than creating or discharging one.

## 2. Purpose

Keep the property registry accurate when the party to a registered finance lease changes, so a title search reflects the true current lessor or lessee.

## 3. Description

The outgoing and incoming parties agree the assignment of the finance lease. The transfer is submitted at a Real Estate Registration Trustee Centre, following the same institution-to-RERA pipeline as Finance Lease Registration, with the fee paid upfront via the shared platform payment gateway. On approval, updated outputs are delivered by email.

## 4. Who Can Apply

### Applicant (Transferring or Receiving Institution)

* Mortgage Officer  
* Trustee Centre Operator (Group G) — assisted mode (C2)

### Counterparty

* The lessee of record, whose consent to the transfer is required

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with a Mortgage Officer provisioned.  
* An existing, active registered finance lease against the property.  
* The receiving institution is itself a registered RERAN Group C institution able to hold a registered finance lease.  
* Payment has been completed via the shared platform payment gateway before the application is lodged (B1).

## 6. Required Information

### Existing Lease Reference

* Finance Lease Registration Number  
* Property Registration Number  
* Current Lessor (Institution) Details

### Transfer Information

* New Lessor (Institution) Details  
* Effective Date of Transfer  
* Reason / Basis for Transfer

## 7. Required Documents

> **Proposed** — by analogy with Service #5 (Mortgage Transfer) and Service #8.

* Existing Certificate of Title / Title Deed  
* Original Finance Lease Agreement  
* Deed of Assignment / Novation Agreement  
* Consent of the Existing Lessor  
* Consent of the Lessee, where required  
* Government-issued Identification (Parties)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Corrected 2026-08-14** — per the corrected `open-questions.md` B6, RERA sets this fee directly, per service code. Previously proposed as ad valorem/banded; that basis is retired. The exact fee is a configuration fact (B5), not client data awaiting collection.

## 9. Payment Required

**Yes** — paid upfront by the initiating institution via the shared platform payment gateway, before the application is lodged, by extension of Service #8. **Corrected 2026-08-14** — previously Institution Account Debit, deducted after RERA approval; that model is retired, see [payments.md](../payments.md) and `open-questions.md` B1.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 36).

## 11. Expected Processing Time

**10–15 minutes.** Sourced from row 36.

## 12. Processing Workflow

Transferring & Receiving Institutions

Agree Terms of Finance Lease Assignment  
↓  
Obtain Lessee's Consent, Where Required

↓

Mortgage Officer (Initiating Institution) / Trustee Centre Operator

Visit Real Estate Registration Trustee Centre *(C2: assisted mode)*  
↓  
Submit Assignment Documents  
↓  
Enter Transfer into System  
↓  
Pay via Shared Platform Gateway

↓

RERA

Receive in Transaction Audit Queue  
↓  
Audit Transfer  
↓  
Approve, Return, or Reject  
↓  
Generate Updated Output Documents  
↓  
Deliver Outputs via Email

## 13. Application Status Flow

Draft  
↓  
Payment Pending  
↓  
Payment Successful  
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
* Rejected  
* Withdrawn

**Corrected 2026-08-14** — `Approved — Awaiting Payment` and `Expired` (B3) removed; see Service #3's Application Status Flow section for the reasoning, which applies identically here.

## 14. Possible Outcomes

* Finance Lease Successfully Transferred  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Certificate of Title / Title Deed, reissued naming the new lessor — sourced (row 36)  
* Map — sourced (row 36)  
* Payment Receipt — proof the fee settled, issued at checkout before the application was lodged. **Corrected 2026-08-14** — previously "Fee Balance" (B9); see [payments.md](../payments.md).

## 16. Related Services

* Service #8 — Finance Lease Registration  
* Service #9 — Finance Lease Amendment  
* Service #11 — Finance Lease Release

## 17. UI Screens

* Services  
* Finance Lease Transfer  
* Select Existing Lease  
* New Lessor Information  
* Document Upload  
* Application Review  
* Payment Confirmation
* Application Submitted  
* Application Details  
* Transfer Confirmation

## 18. API Requirements

* Retrieve Existing Finance Lease Record  
* Validate Lease Status  
* Validate Receiving Institution Standing  
* Upload Documents  
* Calculate Service Fee  
* Verify Payment Status
* Submit Finance Lease Transfer Application  
* Retrieve Application Status  
* Process Gateway Payment
* Generate Updated Certificate of Title  
* Update Finance Lease Registry  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff  
* Property  
* Finance Lease  
* Finance Lease Transfer  
* Application  
* Service Request  
* Document  
* Payment Transaction
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Mortgage Officer can select an existing finance lease and submit transfer details naming a new lessor.  
* System validates the lease is active and the receiving institution holds valid RERAN standing.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is paid via the shared platform payment gateway before the application is lodged.  
* Application receives a unique application reference number.  
* Approved transfers update the official finance lease registry.  
* All parties receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Mortgage Officer, or a Trustee Centre operator acting on an institution's behalf, may initiate a transfer.  
2. The finance lease being transferred must be active and registered.  
3. The receiving institution must hold valid RERAN Group C standing able to hold a registered finance lease.  
4. Payment is made via the shared platform payment gateway, upfront, before the application can be lodged — not deducted from a settlement account (B1, corrected 2026-08-14).  
5. **Corrected 2026-08-14** — the previous low-balance-warning and 30-day-expiry rules (B4, B3) are removed; see Service #3's Business Rules for the reasoning, which applies identically here.  
6. Every application receives a unique application reference number.  
7. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. ~~Which institution's settlement account is debited~~ — **reframed, not resolved, 2026-08-14.** There is no settlement account (B1). The underlying question survives, narrower: **which institution pays the upfront gateway fee** when transferring and receiving institutions differ? Same open item as Service #5.  
2. **Whether lessee consent is mandatory for every transfer.** Not specified in source.  
3. **Exact fee schedule.** Client data — see `open-questions.md` B5, B6.
