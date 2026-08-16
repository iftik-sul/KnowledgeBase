---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - service-flow
  - title-ownership
  - split-ownership
---

# Service #16 – Split Ownership

**Service Category:** Title & Ownership Transaction Services

**Source row:** 43 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Split Ownership** service divides a single registered property into separately titled parcels or ownership shares, issuing a new electronic title deed and map for the resulting split.

## 2. Purpose

Give co-owners, or an owner subdividing a holding, a regulated path to formalize a division of a registered property into distinct, separately registered ownership records.

## 3. Description

The applicant visits the Land Department, submits the required documents, and the transaction data is entered into the system. The applicant pays the fee, RERA reviews and approves the split, and the applicant receives the new title deed and map by email.

## 4. Who Can Apply

### Applicant

* Any of the institution's four Group C roles — where the transaction is bank-originated
* Trustee Centre Operator (Group G) / Land Department counter staff — otherwise, acting on the customer's behalf in assisted mode

> **Confirmed 2026-08-15** — previously conditioned this on the Mortgage Officer specifically, following A4's earlier per-service re-derivation. `open-questions.md` A4 now confirms ownership is not role-specific at all. The Land Department counter path remains what row 43 itself sources (a walk-in visit with no bank-employee involvement); whether a bank-originated variant exists for this service at all remains unconfirmed by source — see Open Questions — but that is now a channel question, not a role-ownership one.

### Customer

* All co-owners of the property being split, or the sole owner subdividing it

## 5. Prerequisites

* The property is registered with RERAN.  
* All co-owners consent to the split, where applicable.  
* A survey plan for the resulting parcels is available.  
* Required supporting documents are available.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address  
* Current Ownership Structure

### Split Information

* Number of Resulting Parcels / Shares  
* Proposed Boundaries or Share Allocation  
* Owner(s) of Each Resulting Parcel / Share

## 7. Required Documents

> **Proposed** — the source states only that documents are "submitted," without enumerating them.

* Existing Certificate of Title  
* Subdivision / Partition Agreement Among Co-Owners  
* Survey Plan for the Split Parcels  
* Government-issued Identification (All Owners)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Paid by the customer, **before** RERA's review and approval — sourced (row 43's own sequence: transaction data entered, then payment, then "review & approval"). **Customer Payment at Counter** model, unaffected by the 2026-08-14 payment-model correction (`open-questions.md` B1). *(Corrected 2026-08-14 — previously cited `B9`, now superseded.)*

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 43; Step 2–6 includes "review & approval").

## 11. Expected Processing Time

**25 minutes.** Sourced from row 43.

## 12. Processing Workflow

Customer

Visit Land Department *(C2: this is the sourced path for this service; Section 4 carries the bank-originated branch as unconfirmed rather than asserting a direct online path here — see Open Questions)*  
↓  
Submit Documents

↓

Trustee Centre / Land Department Operator

Enter Split Ownership Data

↓

Customer

Pay Fees

↓

RERA (Compliance & Escrow Auditor)

Review Application  
↓  
Approve, Return, or Reject

↓

RERA

Generate Electronic Title Deed Certificate(s) for Split Parcels  
↓  
Generate Electronic Map  
↓  
Deliver Title Deed & Map via Email

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
Approved  
↓  
Completed

### Additional Statuses

* Rejected  
* Withdrawn

**Corrected 2026-08-15 — `Approved — Awaiting Payment` removed.** This status previously sat between `Returned for Correction` and `Completed`, but contradicts this service's own sourced workflow (Section 12, Section 9): the customer pays *before* RERA's review and approval, not after. By the time a decision is reached, payment has already happened. This is now the pattern for every fee-bearing Group C service, without exception — see [status-badges.md](../ui/status-badges.md#application-status) for the module-wide confirmation following the 2026-08-16 normalization of Services #12 and #18, the last two services that previously paid after RERA's decision.

## 14. Possible Outcomes

* Property Ownership Successfully Split  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Electronic Title Deed Certificate (per resulting parcel) — sourced (row 43)  
* Electronic Map — sourced (row 43)

## 16. Related Services

* Service #15 — Updating Title Deed Information  
* Service #17 — Issuance of Title Deed  
* Service #14 — Company Shares Sale

## 17. UI Screens

* Services  
* Split Ownership  
* Select Property  
* Split Details  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Split Title Deeds & Map

## 18. API Requirements

* Retrieve Property / Ownership Record  
* Validate Property Ownership  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Split Ownership Application  
* Retrieve Application Status  
* Create New Split Property Records  
* Generate Electronic Title Deed(s)  
* Generate Electronic Map  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Property Split Record  
* Survey Plan  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Owner(s) can initiate a split ownership application at the Land Department.  
* System validates the property's registration and current ownership before allowing a split.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Payment is completed before RERA's review.  
* Approved splits create new, separately registered property records.  
* Customer receives new title deeds and a map on completion.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. This application may be processed by any of the institution's four Group C roles where bank-originated, or otherwise by a Trustee Centre / Land Department operator acting on the owner(s)' behalf. **Confirmed 2026-08-15** — previously conditioned on the Mortgage Officer specifically; `open-questions.md` A4 confirms no service is role-specific. *(Whether a bank-originated variant exists for this service at all remains unconfirmed by source — only the counter path is confirmed by row 43.)*
2. The property must be registered with RERAN before it can be split.  
3. All co-owners must consent to the split, where applicable.  
4. Payment is required before RERA's review and approval.  
5. Approved splits create new, separately registered property records, each with its own title deed.  
6. Every application receives a unique application reference number.  
7. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Minimum parcel size or other subdivision restrictions**, if any. Not specified in source.  
2. **Whether an encumbrance (e.g., an active mortgage) on the original property blocks a split**, or how it is apportioned across the resulting parcels. Not specified in source.  
3. ~~Whether a bank-originated path (Mortgage Officer, per A4's conditional) exists for this service at all.~~ **Reframed 2026-08-15** — the role-conditional part of this question is resolved: if a bank-originated path exists, any of the four Group C roles may use it, not just a Mortgage Officer (A4). What remains genuinely open is narrower: **whether a bank-originated channel exists for this service at all.** No row among 38, 40–44 describes bank-employee entry the way the mortgage rows (30–33, 39) do; this document still sources only the Land Department counter path.  
4. **Exact fee amount.** Client data — see `open-questions.md` B5.
