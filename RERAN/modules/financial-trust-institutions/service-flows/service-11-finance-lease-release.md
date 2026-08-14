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
  - release
---

# Service #11 – Finance Lease Release

**Service Category:** Finance Lease Services

**Source row:** 37 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as finance lease registration" — expanded in full below. **A release discharges the lease; a registration creates it — they are not the same flow**, consistent with the same distinction drawn for Service #6 (Mortgage Release).

## 1. Service Overview

The **Finance Lease Release** service discharges an existing registered finance lease once its term ends, the lease is terminated early, or a purchase option is exercised — removing the leasing encumbrance from the property registry.

## 2. Purpose

Formally end a finance lease's effect on the property registry once the lease itself has ended, so the registry reflects the property's true, unencumbered leasing status.

## 3. Description

The lessor confirms the lease has ended (term completion, early termination, or exercised purchase option). The release is submitted at a Real Estate Registration Trustee Centre, following the same institution-to-RERA pipeline as Finance Lease Registration, with the fee paid upfront via the shared platform payment gateway. On approval, the lease is discharged on the registry, and outputs are delivered to the lessee by email.

## 4. Who Can Apply

### Applicant (Lessor Institution)

* Mortgage Officer  
* Trustee Centre Operator (Group G) — assisted mode (C2)

### Counterparty (Lessee)

* The lessee of record on the finance lease being released

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with a Mortgage Officer provisioned.  
* An existing, active registered finance lease against the property.  
* The lease has ended (term completion, early termination, or exercised purchase option).  
* Payment has been completed via the shared platform payment gateway before the application is lodged (B1).

## 6. Required Information

### Existing Lease Reference

* Finance Lease Registration Number  
* Property Registration Number

### Release Information

* Grounds for Release (e.g., term completion, early termination, purchase option exercised)  
* Date of Release Event

## 7. Required Documents

> **Proposed** — by analogy with Service #6 (Mortgage Release) and Service #8.

* Existing Certificate of Title / Title Deed  
* Original Finance Lease Agreement  
* Evidence of Lease Completion / Termination / Purchase Option Exercise  
* Deed of Release  
* Government-issued Identification (Lessee)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Corrected 2026-08-14** — per the corrected `open-questions.md` B6, RERA sets this fee directly, per service code (the earlier flat-vs-ad-valorem question is moot once the fee no longer scales off any secured amount). Exact fee is a configuration fact (B5), not client data awaiting collection.

## 9. Payment Required

**Yes** — paid upfront by the institution via the shared platform payment gateway, before the application is lodged, by extension of Service #8. **Corrected 2026-08-14** — previously Institution Account Debit, deducted after RERA approval; that model is retired, see [payments.md](../payments.md) and `open-questions.md` B1.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 37).

## 11. Expected Processing Time

**10–15 minutes.** Sourced from row 37.

## 12. Processing Workflow

Lessor Institution

Confirm Lease Completion / Termination / Purchase Option Exercise

↓

Mortgage Officer / Trustee Centre Operator

Visit Real Estate Registration Trustee Centre *(C2: assisted mode)*  
↓  
Submit Release Documents  
↓  
Enter Release into System  
↓  
Pay via Shared Platform Gateway

↓

RERA

Receive in Transaction Audit Queue  
↓  
Audit Release  
↓  
Approve, Return, or Reject  
↓  
Discharge Finance Lease on Property Registry  
↓  
Generate Output Documents  
↓  
Deliver Outputs to Lessee via Email

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

* Finance Lease Successfully Released / Discharged  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Certificate of Title / Title Deed, reissued free of the discharged lease — sourced (row 37)  
* Map — sourced (row 37)  
* Payment Receipt — proof the fee settled, issued at checkout before the application was lodged. **Corrected 2026-08-14** — previously "Fee Balance" (B9); see [payments.md](../payments.md).

## 16. Related Services

* Service #8 — Finance Lease Registration  
* Service #9 — Finance Lease Amendment  
* Service #10 — Finance Lease Transfer

## 17. UI Screens

* Services  
* Finance Lease Release  
* Select Existing Lease  
* Release Information  
* Document Upload  
* Application Review  
* Payment Confirmation
* Application Submitted  
* Application Details  
* Release Confirmation

## 18. API Requirements

* Retrieve Existing Finance Lease Record  
* Validate Lease Status  
* Upload Documents  
* Calculate Service Fee  
* Verify Payment Status
* Submit Finance Lease Release Application  
* Retrieve Application Status  
* Process Gateway Payment
* Discharge Finance Lease on Property Registry  
* Generate Updated Certificate of Title  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff  
* Property  
* Finance Lease  
* Finance Lease Release  
* Application  
* Service Request  
* Document  
* Payment Transaction
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Mortgage Officer can select an existing finance lease and submit release information.  
* System validates the lease is active and registered before allowing release.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is paid via the shared platform payment gateway before the application is lodged.  
* Application receives a unique application reference number.  
* Approved releases discharge the lease on the official property registry.  
* Institution and lessee receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Mortgage Officer, or a Trustee Centre operator acting on the institution's behalf, may initiate a release.  
2. The finance lease being released must be active and registered.  
3. Payment is made via the shared platform payment gateway, upfront, before the application can be lodged — not deducted from a settlement account (B1, corrected 2026-08-14).  
4. **Corrected 2026-08-14** — the previous low-balance-warning and 30-day-expiry rules (B4, B3) are removed; see Service #3's Business Rules for the reasoning, which applies identically here.  
5. Every application receives a unique application reference number.  
6. All applications, approvals, payments, discharges, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Grounds for release beyond term completion** and any evidentiary differences between them (early termination vs. purchase option). Not specified in source.  
2. **Fee basis for release**, given there is no new leased value to apply an ad valorem rate to. Not specified in source.  
3. **Exact fee schedule.** Client data — see `open-questions.md` B5, B6.
