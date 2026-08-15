---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
updated: 2026-08-15
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

* Any of the institution's four Group C roles. **Confirmed 2026-08-15** — previously listed as Mortgage Officer only, on the strength of the source's responsible-role column and the retired A4 re-derivation; `open-questions.md` A4 now confirms no service is role-specific.
* Trustee Centre Operator (Group G) — assisted mode, entering the transaction on the institution's behalf at the Trustee Centre (C2)

### Counterparty (Lessee)

* Registered Individual User or Eligible Property User who is party to the finance lease

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with staff provisioned.  
* Property is registered with RERAN and its title is verified.  
* Lessor and lessee have agreed finance lease terms before system entry.  
* Payment has been completed via the shared platform payment gateway before the application is lodged (B1).

## 6. Required Information

### Institution (Lessor) Information

* Institution Name  
* Acting Officer Identifier

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

> **Corrected 2026-08-14** — per the corrected `open-questions.md` B6, RERA sets this fee directly, per service code, independent of the leased asset's value. Previously proposed as ad valorem/banded; that basis is retired. The exact fee is a configuration fact (B5), not client data awaiting collection.

## 9. Payment Required

**Yes**

Paid upfront by the institution via the shared platform payment gateway, before the application is lodged.

> **Corrected 2026-08-14 — the tension this section previously carried is resolved, from the other direction.** Row 34's workflow text reads as a counter transaction ("submit docs, enter system, **pay**, receive output via email") — a point-of-sale payment — which this document previously treated as being in tension with the account-debit model B1 assigned to it, on the strength of row 34 also listing "Fee balance" among outputs. With B1 corrected to a single upfront, per-transaction payment model for every Group C service, row 34's counter-transaction reading turns out to have been the more accurate one all along; the "Fee balance" wording is no longer read as implying a standing account (`open-questions.md` B9, superseded). No unresolved tension remains for this service.

## 10. Processing Authority

**Two gates**, by extension of the pattern established for mortgage services, since finance lease shares the same lender-side origination and Compliance & Escrow Auditor approval:

1. **Internal Certifier** — a functional label, not a role or scope: any of the institution's four Group C users may act as internal certifier, including the person who filed the transaction. **Corrected 2026-08-14** — previously `checker permission scope` (A1/D2), now retired; see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).  
2. **Compliance & Escrow Auditor** (Group A).

> **Proposed** — row 34 does not explicitly mention an internal bank-auditor step (unlike rows 30–33, 39, which say "audited by bank auditor"). This is inferred by extension from the mortgage lifecycle sharing the same institutional origination pattern. See Open Questions.

## 11. Expected Processing Time

**30–35 minutes.** Sourced from row 34 — the longest SLA of any Group C service, consistent with a full lease registration rather than a lifecycle amendment.

## 12. Processing Workflow

Lessee & Lessor Institution

Agree Finance Lease Terms

↓

Institution User / Trustee Centre Operator

Visit Real Estate Registration Trustee Centre *(C2: assisted mode of the same online service)*  
↓  
Submit Required Documents  
↓  
Enter Finance Lease Transaction into System  
↓  
Pay via Shared Platform Gateway  
↓  
Submit for Internal Certification

↓

Internal Certifier

Review Transaction  
↓  
Certify, or Return to Filer

↓

RERA

Receive Transaction in Transaction Audit Queue  
↓  
Audit Transaction  
↓  
Approve, Return, or Reject  
↓  
Generate Output Documents  
↓  
Deliver Outputs to Customer via Email

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

**Corrected 2026-08-14** — `Approved — Awaiting Payment` and `Expired` (B3) removed; see Service #3's Application Status Flow section for the reasoning, which applies identically here. **Corrected 2026-08-15** — a stray duplicate `Expired (B3)` bullet, left over from an earlier partial edit, is removed; this section now consistently omits both statuses.

## 14. Possible Outcomes

* Finance Lease Successfully Registered  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Certificate of Title / Title Deed — sourced (row 34)  
* Map — sourced (row 34); finance lease services list a Map among outputs where the mortgage services do not  
* Payment Receipt — proof the fee settled, issued at checkout before the application was lodged. **Corrected 2026-08-14** — previously "Fee Balance" (B9); see [payments.md](../payments.md).

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
* Payment Confirmation
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
* Verify Payment Status
* Submit Finance Lease Registration Application  
* Retrieve Application Status  
* Process Gateway Payment
* Generate Certificate of Title  
* Generate Map  
* Update Finance Lease Registry  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff *(no scope field — every staff member has identical system access; role is recorded per-action, not per-account)*  
* Property  
* Property Ownership  
* Finance Lease  
* Certification Record *(now includes the acting user and their role at time of certification, per [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle) — not a scope reference)*  
* Application  
* Service Request  
* Document  
* Payment Transaction
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles (or a Trustee Centre operator, in assisted mode) can initiate finance lease registration against a registered title. **Confirmed 2026-08-15** — not restricted to the Mortgage Officer (A4).  
* System validates the property is registered and its title is verified.  
* Internal certifier — any of the four Group C roles, including the filer — can certify or return the transaction before it reaches RERA.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is paid via the shared platform payment gateway before the application is lodged.  
* Application receives a unique application reference number.  
* Approved registrations update the official finance lease registry.  
* Institution and lessee receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Any of the institution's four Group C roles acting under the lessor institution's corporate account, or a Trustee Centre operator acting on its behalf, may initiate finance lease registration. **Confirmed 2026-08-15** — previously restricted to "only a Mortgage Officer"; `open-questions.md` A4 confirms no service is role-specific.  
2. The property must be registered with RERAN and its title verified.  
3. The transaction must pass internal institutional certification before routing to RERA. *(Proposed by extension — not explicit in row 34; see Open Questions.)*  
4. Payment is made via the shared platform payment gateway, upfront, before the application can be lodged — not deducted from a settlement account (B1, corrected 2026-08-14).  
5. **Corrected 2026-08-14** — the previous low-balance-warning and 30-day-expiry rules (B4, B3) are removed; see Service #3's Business Rules for the reasoning, which applies identically here.  
6. Every application receives a unique application reference number.  
7. All applications, certifications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Does an internal bank-auditor certification step apply to finance lease services**, as it does to mortgage services? Row 34 does not state it explicitly, unlike rows 30–33 and 39.  
2. ~~Is the "pay" step at the Trustee Centre a settlement-account deduction or a direct counter payment?~~ **Resolved by the 2026-08-14 correction** — there is no settlement account; it is a direct payment via the shared platform gateway, upfront, matching the workflow text's point-of-sale reading all along.  
3. **Does an online (non-Trustee-Centre) channel exist for finance lease services**, comparable to the Online Mortgage System for mortgage services? Row 34 names only the Trustee Centre.  
4. **Exact fee schedule.** Resolved by B5 — RERA sets it directly as configuration, not client data. See `open-questions.md` B5, B6.
