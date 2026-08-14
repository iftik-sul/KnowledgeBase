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
  - amendment
---

# Service #4 – Mortgage Amendment

**Service Category:** Mortgage Services

**Source row:** 31 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Mortgage Amendment** service modifies the terms of an existing registered mortgage — for example, a change in loan amount, term, or interest rate — without creating a new encumbrance or discharging the existing one. It follows the same institution-to-RERA pipeline as Mortgage Registration (Service #3), reused here in full rather than by cross-reference.

## 2. Purpose

Keep the registered mortgage record accurate when the underlying loan terms change, so the property registry continues to reflect the true state of the encumbrance.

## 3. Description

The customer agrees amended terms with the bank. A Mortgage Officer enters the amendment into the Online Mortgage System against the existing mortgage record, pays the fee upfront via the shared platform payment gateway, and attaches the amendment documentation. The transaction is certified internally, then audited by RERA. On approval, the updated output documents are delivered to the customer by email. The service can alternatively be processed in assisted mode at a Real Estate Registration Trustee Centre.

## 4. Who Can Apply

### Applicant (Lending Institution)

* Mortgage Officer — primary channel, via the Online Mortgage System  
* Trustee Centre Operator (Group G) — assisted mode, acting on the institution's behalf (C2)

### Counterparty (Borrower / Property Owner)

* The registered mortgagor of the mortgage being amended

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with a Mortgage Officer provisioned.  
* An existing, active registered mortgage against the property.  
* Payment has been completed via the shared platform payment gateway before the application is lodged (B1).

## 6. Required Information

### Institution Information

* Institution Name  
* Mortgage Officer Identifier

### Existing Mortgage Reference

* Mortgage Registration Number  
* Property Registration Number

### Amendment Details

* Nature of Amendment (e.g., loan amount, term, interest rate)  
* Amended Terms  
* Reason for Amendment

## 7. Required Documents

> **Proposed** — by analogy with Service #3 and what a mortgage amendment plainly requires.

* Existing Certificate of Title / Title Deed  
* Original Mortgage Agreement  
* Amendment Deed / Addendum to Mortgage Agreement  
* Government-issued Identification (Borrower)  
* Internal Certification Record  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Corrected 2026-08-14** — per the corrected `open-questions.md` B6, RERA sets this fee directly, per service code, independent of the loan amount or the amended terms. Previously proposed as ad valorem/banded; that basis is retired. The exact fee is a configuration fact (B5), not client data awaiting collection.

## 9. Payment Required

**Yes** — paid upfront by the institution via the shared platform payment gateway, before the application is lodged, same as Service #3. **Corrected 2026-08-14** — previously Institution Account Debit, deducted after RERA approval; that model is retired, see [payments.md](../payments.md) and `open-questions.md` B1.

## 10. Processing Authority

**Two gates**, identical structure to Service #3:

1. **Internal Certifier** — a functional label, not a role or scope: any of the institution's four Group C users may act as internal certifier, including the person who filed the transaction. **Corrected 2026-08-14** — previously `checker permission scope` (A1/D2), now retired; see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).  
2. **Compliance & Escrow Auditor** (Group A).

## 11. Expected Processing Time

**10–15 minutes.** Sourced from row 31 as a single end-to-end figure — shorter than registration, consistent with amending an existing record rather than creating one.

## 12. Processing Workflow

Borrower (Customer)

Agree Amended Terms with Bank

↓

Mortgage Officer

Login to Online Mortgage System  
↓  
Select Existing Mortgage Record  
↓  
Enter Amendment Details  
↓  
Upload Amendment Documents  
↓  
Pay via Shared Platform Gateway  
↓  
Submit for Internal Certification

↓

Internal Certifier

Review Amendment  
↓  
Certify, or Return to Mortgage Officer

↓

RERA

Receive in Transaction Audit Queue  
↓  
Audit Amendment  
↓  
Approve, Return, or Reject  
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
Enter Amendment into System on the Institution's Behalf  
↓  
Pay Fees at Counter  
↓  
Receive Output via Email

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

* Mortgage Successfully Amended  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* The applicable one of: Certificate of Title / Title Deed / Usufruct Title Deed / Statement Certificate / Provisional Sale Registration Certificate, reissued to reflect amended terms — sourced (row 31)  
* Payment Receipt — proof the fee settled, issued at checkout before the application was lodged. **Corrected 2026-08-14** — previously "Fee Balance" (B9); see [payments.md](../payments.md).

## 16. Related Services

* Service #3 — Mortgage Registration  
* Service #5 — Mortgage Transfer  
* Service #6 — Mortgage Release  
* Individual-user Service #8 — Register Sale of Mortgaged Property *(cross-module)*

## 17. UI Screens

* Services  
* Mortgage Amendment  
* Select Existing Mortgage  
* Amendment Details  
* Document Upload  
* Internal Certification Queue  
* Application Review  
* Payment Confirmation
* Application Submitted  
* Application Details  
* Amendment Confirmation

## 18. API Requirements

* Retrieve Existing Mortgage Record  
* Validate Mortgage Status  
* Upload Documents  
* Submit for Internal Certification  
* Retrieve Certification Status  
* Calculate Service Fee  
* Verify Payment Status
* Submit Mortgage Amendment Application  
* Retrieve Application Status  
* Process Gateway Payment
* Generate Updated Certificate / Statement Certificate  
* Update Mortgage Registry  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff *(no scope field — every staff member has identical system access; role is recorded per-action, not per-account)*  
* Property  
* Mortgage  
* Mortgage Amendment  
* Certification Record *(now includes the acting user and their role at time of certification, per [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle) — not a scope reference)*  
* Application  
* Service Request  
* Document  
* Payment Transaction
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Mortgage Officer can select an existing mortgage and submit amendment details.  
* System validates the mortgage is active and registered before allowing amendment.  
* Internal certifier — any of the four Group C roles, including the filer — can certify or return the amendment before it reaches RERA.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is paid via the shared platform payment gateway before the application is lodged.  
* Application receives a unique application reference number.  
* Approved amendments update the official mortgage registry.  
* Institution and customer receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Mortgage Officer, or a Trustee Centre operator acting on the institution's behalf, may initiate an amendment.  
2. The mortgage being amended must be active and registered.  
3. The transaction must pass internal institutional certification before routing to RERA.  
4. Payment is made via the shared platform payment gateway, upfront, before the application can be lodged — not deducted from a settlement account (B1, corrected 2026-08-14).  
5. **Corrected 2026-08-14** — the previous low-balance-warning and 30-day-expiry rules (B4, B3) are removed; see Service #3's Business Rules for the reasoning, which applies identically here.  
6. Every application receives a unique application reference number.  
7. All applications, certifications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **What changes qualify as an "amendment" versus requiring a new registration or a release-and-re-register?** Not specified in source.  
2. ~~Does the Trustee-Centre-assisted variant draw from the institution's settlement account, or a separate at-counter payment?~~ **Resolved — same item as Service #3, resolved the same way.**  
3. **Exact fee schedule for amendments.** Resolved by B5 — RERA sets it directly as configuration, not client data. See `open-questions.md` B5, B6.
