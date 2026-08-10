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
  - "RERAN/modules/financial-trust-institutions/service-flows/service-08-finance-lease-registration.md"
tags:
  - financial-trust-institutions
  - service-flow
  - finance-lease
  - amendment
---

# Service #9 – Finance Lease Amendment

**Service Category:** Finance Lease Services

**Source row:** 35 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as finance lease registration" — expanded in full below.

## 1. Service Overview

The **Finance Lease Amendment** service modifies the terms of an existing registered finance lease — for example, a change to the payment schedule, lease term, or residual/purchase option — without creating a new lease or discharging the existing one.

## 2. Purpose

Keep the registered finance lease record accurate when its terms change, so the property registry continues to reflect the true state of the lease.

## 3. Description

The lessor and lessee agree amended lease terms. The amendment is submitted at a Real Estate Registration Trustee Centre, following the same institution-to-RERA pipeline as Finance Lease Registration (Service #8). On approval, the fee is deducted from the institution's settlement account and updated outputs are delivered to the lessee by email.

## 4. Who Can Apply

### Applicant (Lessor Institution)

* Mortgage Officer  
* Trustee Centre Operator (Group G) — assisted mode (C2)

### Counterparty (Lessee)

* The registered lessee of the finance lease being amended

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with a Mortgage Officer provisioned.  
* An existing, active registered finance lease against the property.  
* Institution's settlement account holds a sufficient prefunded balance to absorb the fee once approved (B1, B4).

## 6. Required Information

### Existing Lease Reference

* Finance Lease Registration Number  
* Property Registration Number

### Amendment Details

* Nature of Amendment (e.g., payment schedule, lease term, residual terms)  
* Amended Terms  
* Reason for Amendment

## 7. Required Documents

> **Proposed** — by analogy with Service #8.

* Existing Certificate of Title / Title Deed  
* Original Finance Lease Agreement  
* Amendment Deed / Addendum to Finance Lease Agreement  
* Government-issued Identification (Lessee)  
* Internal Certification Record *(where applicable — see Service #8 Open Questions)*  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Proposed** — ad valorem/banded basis per B6. Exact schedule is client data (B5).

## 9. Payment Required

**Yes** — Institution Account Debit model, by extension of B1 as applied in Service #8, deducted from the institution's settlement account after RERA approval.

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 35).

> **Proposed** — whether an internal institutional certification gate precedes RERA review is inherited as an open question from Service #8; not explicit in row 35.

## 11. Expected Processing Time

**10–15 minutes.** Sourced from row 35.

## 12. Processing Workflow

Lessor & Lessee

Agree Amended Lease Terms

↓

Mortgage Officer / Trustee Centre Operator

Visit Real Estate Registration Trustee Centre *(C2: assisted mode)*  
↓  
Submit Amendment Documents  
↓  
Enter Amendment into System  
↓  
Pay Fees

↓

RERA

Receive in Transaction Audit Queue  
↓  
Audit Amendment  
↓  
Approve, Return, or Reject  
↓  
Deduct Fee from Institution Settlement Account  
↓  
Generate Updated Output Documents  
↓  
Deliver Outputs to Lessee via Email

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
* Expired *(B3)*

> **Proposed** — `Pending Internal Certification` / `Returned by Certifier` are omitted pending resolution of Service #8's open question on whether an internal certification gate applies to finance lease services at all.

## 14. Possible Outcomes

* Finance Lease Successfully Amended  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Insufficient Settlement Balance / Payment Failed  
* Approval Expired  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Certificate of Title / Title Deed, reissued to reflect amended terms — sourced (row 35)  
* Map — sourced (row 35)  
* Fee Balance — settlement-account statement line, not a receipt (B9)

## 16. Related Services

* Service #8 — Finance Lease Registration  
* Service #10 — Finance Lease Transfer  
* Service #11 — Finance Lease Release

## 17. UI Screens

* Services  
* Finance Lease Amendment  
* Select Existing Lease  
* Amendment Details  
* Document Upload  
* Application Review  
* Settlement Account Confirmation  
* Application Submitted  
* Application Details  
* Amendment Confirmation

## 18. API Requirements

* Retrieve Existing Finance Lease Record  
* Validate Lease Status  
* Upload Documents  
* Calculate Service Fee  
* Check Settlement Account Balance  
* Submit Finance Lease Amendment Application  
* Retrieve Application Status  
* Deduct Settlement Account Fee  
* Generate Updated Certificate of Title  
* Update Finance Lease Registry  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff  
* Property  
* Finance Lease  
* Finance Lease Amendment  
* Application  
* Service Request  
* Document  
* Settlement Account  
* Settlement Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Mortgage Officer can select an existing finance lease and submit amendment details.  
* System validates the lease is active and registered before allowing amendment.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is deducted from the institution's settlement account only after approval.  
* Application receives a unique application reference number.  
* Approved amendments update the official finance lease registry.  
* Institution and lessee receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Mortgage Officer, or a Trustee Centre operator acting on the institution's behalf, may initiate an amendment.  
2. The finance lease being amended must be active and registered.  
3. Payment is deducted from the institution's settlement account only after approval (B1, by extension).  
4. Submission is blocked if the projected settlement balance after fees would go negative (B4).  
5. An approved but unsettled transaction lapses to Expired after 30 calendar days (B3).  
6. Every application receives a unique application reference number.  
7. All applications, approvals, settlement deductions, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Does an internal certification gate apply to finance lease amendments?** Carried forward from Service #8.  
2. **What changes qualify as an "amendment" versus requiring a new registration?** Not specified in source.  
3. **Exact fee schedule.** Client data — see `open-questions.md` B5, B6.
