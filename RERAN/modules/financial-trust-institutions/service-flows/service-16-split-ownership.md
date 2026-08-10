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

* Mortgage Officer — where the transaction is bank-originated (A4's conditional)
* Trustee Centre Operator (Group G) / Land Department counter staff — otherwise, acting on the customer's behalf in assisted mode

> **Proposed** — the source assigns responsible role to the **Mortgage Officer**. `open-questions.md` A4's rule is conditional — "Mortgage Officer where bank-originated; otherwise executed by a Trustee Centre operator on the customer's behalf" — not an unconditional reassignment. This document keeps both branches: the Land Department counter path is what row 43 itself sources (a walk-in visit with no bank-employee involvement); the Mortgage Officer / bank-originated branch is preserved because A4 allows for it in principle, but **no row among the title & ownership transaction rows (38, 40–44) describes a bank-originated workflow**, so that branch is not sourced here and is carried forward as an open question rather than asserted as fact or silently dropped. **Confidence: Medium**, per the answers doc — the counter-staff branch contradicts the source's responsible-role column, and that should be visible to the client.

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

Paid by the customer — sourced (row 43, Step 2–6 includes "pay"). **Customer Payment at Counter** model (B9).

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 43; Step 2–6 includes "review & approval").

## 11. Expected Processing Time

**25 minutes.** Sourced from row 43.

## 12. Processing Workflow

Customer

Visit Land Department *(C2: this is the sourced path for this service; Section 4 carries A4's Mortgage Officer / bank-originated branch as unconfirmed rather than asserting a direct online path here — see Open Questions)*  
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
Approved — Awaiting Payment  
↓  
Completed

### Additional Statuses

* Rejected  
* Withdrawn

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
* Payment is completed before the split is finalized.  
* Approved splits create new, separately registered property records.  
* Customer receives new title deeds and a map on completion.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. This application may be processed by a Mortgage Officer where bank-originated, or otherwise by a Trustee Centre / Land Department operator acting on the owner(s)' behalf (A4's conditional). *(Proposed — no row sources a bank-originated variant for this service; only the counter path is confirmed by row 43.)*
2. The property must be registered with RERAN before it can be split.  
3. All co-owners must consent to the split, where applicable.  
4. Payment is required before the application is finalized.  
5. Approved splits create new, separately registered property records, each with its own title deed.  
6. Every application receives a unique application reference number.  
7. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Minimum parcel size or other subdivision restrictions**, if any. Not specified in source.  
2. **Whether an encumbrance (e.g., an active mortgage) on the original property blocks a split**, or how it is apportioned across the resulting parcels. Not specified in source.  
3. **Whether a bank-originated path (Mortgage Officer, per A4's conditional) exists for this service at all.** No row among 38, 40–44 describes bank-employee entry the way the mortgage rows (30–33, 39) do; this document sources only the Land Department counter path and treats the bank-originated branch as unconfirmed rather than absent.  
4. **Exact fee amount.** Client data — see `open-questions.md` B5.
