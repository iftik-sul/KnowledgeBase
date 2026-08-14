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
  - title-deed
---

# Service #17 – Issuance of Title Deed

**Service Category:** Title & Ownership Transaction Services

**Source row:** 44 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Issuance of Title Deed** service issues an electronic title deed certificate for a registered property, whether as a first issuance or a replacement of an existing one.

## 2. Purpose

Give a property owner formal, electronic evidence of registered title, issued directly by RERA following review of the ownership record and supporting evidence.

## 3. Description

The applicant visits the Land Department, submits the required documents, and the transaction data is entered into the system. The applicant pays the fee, RERA reviews and approves the issuance, and the applicant receives the title deed by email.

## 4. Who Can Apply

### Applicant

* Mortgage Officer — where the transaction is bank-originated (A4's conditional)
* Trustee Centre Operator (Group G) / Land Department counter staff — otherwise, acting on the customer's behalf in assisted mode

> **Proposed** — the source assigns responsible role to the **Mortgage Officer**. `open-questions.md` A4's rule is conditional — "Mortgage Officer where bank-originated; otherwise executed by a Trustee Centre operator on the customer's behalf" — not an unconditional reassignment. This document keeps both branches: the Land Department counter path is what row 44 itself sources (a walk-in visit with no bank-employee involvement); the Mortgage Officer / bank-originated branch is preserved because A4 allows for it in principle, but **no row among the title & ownership transaction rows (38, 40–44) describes a bank-originated workflow**, so that branch is not sourced here and is carried forward as an open question rather than asserted as fact or silently dropped. **Confidence: Medium**, per the answers doc — the counter-staff branch contradicts the source's responsible-role column, and that should be visible to the client.

### Customer

* Registered Property Owner, or Authorized Representative

## 5. Prerequisites

* The property's ownership is established and registrable with RERAN.  
* Required supporting documents are available.

## 6. Required Information

### Property Information

* Property Registration Number *(where an existing record exists)*  
* Property Address  
* Property Type

### Applicant Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information  
* Basis for Issuance (first issuance, replacement, allocation)

## 7. Required Documents

> **Proposed** — the source states only that documents are "submitted," without enumerating them.

* Application Form  
* Proof of Prior Ownership / Allocation  
* Survey Plan  
* Government-issued Identification (Applicant)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Paid by the customer — sourced (row 44, Step 2–6 includes "pay"). **Customer Payment at Counter** model, unaffected by the 2026-08-14 payment-model correction (`open-questions.md` B1). *(Corrected 2026-08-14 — previously cited `B9`, now superseded.)*

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 44; Step 2–6 includes "review & approval").

## 11. Expected Processing Time

**25 minutes.** Sourced from row 44.

## 12. Processing Workflow

Customer

Visit Land Department *(C2: this is the sourced path for this service; Section 4 carries A4's Mortgage Officer / bank-originated branch as unconfirmed rather than asserting a direct online path here — see Open Questions)*  
↓  
Submit Documents

↓

Trustee Centre / Land Department Operator

Enter Transaction Data

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

Generate Electronic Title Deed Certificate  
↓  
Deliver Title Deed via Email

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

* Title Deed Successfully Issued  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Electronic Title Deed Certificate — sourced (row 44)

## 16. Related Services

* Service #15 — Updating Title Deed Information  
* Service #16 — Split Ownership  
* Service #13 — Sale Procedure (Heirs)

## 17. UI Screens

* Services  
* Issuance of Title Deed  
* Applicant Information  
* Property Information  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Title Deed Issued

## 18. API Requirements

* Retrieve Property Record, Where Applicable  
* Validate Ownership Evidence  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Title Deed Issuance Application  
* Retrieve Application Status  
* Generate Electronic Title Deed Certificate  
* Send Notifications

## 19. Database Entities

* User  
* Property  
* Property Ownership  
* Title Deed  
* Application  
* Service Request  
* Document  
* Payment  
* Payment Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Owner or authorized representative can initiate a title deed issuance application at the Land Department.  
* System validates ownership evidence before allowing issuance.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Payment is completed before the title deed is issued.  
* Approved applications result in an issued electronic title deed.  
* Customer receives the title deed on completion.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. This application may be processed by a Mortgage Officer where bank-originated, or otherwise by a Trustee Centre / Land Department operator acting on the customer's behalf (A4's conditional). *(Proposed — no row sources a bank-originated variant for this service; only the counter path is confirmed by row 44.)*
2. Ownership must be established and registrable before a title deed can be issued.  
3. Payment is required before the application is finalized.  
4. Approved applications result in an issued electronic title deed on the official registry.  
5. Every application receives a unique application reference number.  
6. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **How this service differs from a first-time property registration performed outside Group C** (e.g., under the individual-user or developer modules) versus a replacement issuance. Not specified in source.  
2. **Grounds for replacement issuance** (e.g., lost, damaged, or superseded deed). Not specified in source.  
3. **Whether a bank-originated path (Mortgage Officer, per A4's conditional) exists for this service at all.** No row among 38, 40–44 describes bank-employee entry the way the mortgage rows (30–33, 39) do; this document sources only the Land Department counter path and treats the bank-originated branch as unconfirmed rather than absent.  
4. **Exact fee amount.** Client data — see `open-questions.md` B5.
