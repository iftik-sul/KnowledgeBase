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
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
tags:
  - financial-trust-institutions
  - service-flow
  - mortgage
---

# Service #3 – Mortgage Registration

**Service Category:** Mortgage Services

**Source row:** 30 of `RERAN_service_flows_v2.md`. This is the reference workflow for the mortgage lifecycle — Services #4 (amendment), #5 (transfer) and #6 (release) are defined by the source as variants of this flow and are expanded in full in their own documents, per the issue's instruction not to reproduce a bare cross-reference.

## 1. Service Overview

The **Mortgage Registration** service records a new mortgage against a registered property title, on the bank's initiative and at the bank's cost, subject to internal certification and RERA audit before the record and the associated fee take effect.

## 2. Purpose

Register a mortgage against a verified title so the lending institution's security interest is legally recognized on the property registry, protecting the interests of the lender, the borrower, and any subsequent party who searches the title.

## 3. Description

The customer (borrower) completes mortgage requirements directly with the bank — loan approval, valuation, executed mortgage deed. A Mortgage Officer then enters the transaction into the Online Mortgage System, attaching the required documents. The transaction is certified internally by any of the institution's four Group C users, including the person who filed it, before it is sent to RERA's Transaction Audit queue. On approval, the fee is deducted from the institution's settlement account and the output documents are delivered to the customer by email. The same service can alternatively be processed in assisted mode at a Real Estate Registration Trustee Centre.

## 4. Who Can Apply

### Applicant (Lending Institution)

* Mortgage Officer — primary channel, via the Online Mortgage System  
* Trustee Centre Operator (Group G) — assisted mode, acting on the institution's behalf at a Real Estate Registration Trustee Centre *(C2: this is the same online service in assisted mode, not a separate channel)*

### Counterparty (Borrower / Property Owner)

* Registered Property Owner granting the mortgage, who must hold a verified RERAN title

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with a Mortgage Officer provisioned under the corporate account.  
* Property is registered with RERAN and its title is verified.  
* Customer has completed mortgage requirements with the bank (loan approval, valuation, executed mortgage deed) before system entry.  
* Institution's settlement account holds a sufficient prefunded balance to absorb the fee once approved (B1, B4).

## 6. Required Information

### Institution Information

* Institution Name  
* Mortgage Officer Identifier  
* Institution Reference Number

### Borrower (Property Owner) Information

* Full Name  
* National Identification Number (NIN)  
* Contact Information

### Property Information

* Property Registration Number  
* Property Address  
* Property Type

### Mortgage Information

* Loan Amount  
* Mortgage Term  
* Interest Rate  
* Mortgagee (Institution) Details  
* Mortgage Deed Reference

## 7. Required Documents

> **Proposed** — the source names the documents entered ("all documents") without enumerating them. The list below is proposed by analogy with the individual-user module's Service #8 (which shares the same instrument) and what a mortgage registration plainly requires.

* Existing Certificate of Title  
* Mortgage Agreement / Deed of Mortgage  
* Loan Offer Letter  
* Property Valuation Report  
* Government-issued Identification (Borrower / Property Owner)  
* Internal Certification Record *(the institution's own internal certify-or-return record — see Section 10)*  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Proposed** — per `open-questions.md` B6, fees for mortgage services are proposed as **ad valorem on the secured amount, banded, with a floor and a cap**. The exact schedule is client data (B5).

## 9. Payment Required

**Yes**

Deducted from the institution's standing, prefunded settlement account **after** RERA approval — not paid by the borrower, and not collected before submission. This is the **Institution Account Debit** model (B1): the source lists "Fee balance" among this service's issued deliverables, which is a standing-account statement line rather than a per-transaction receipt (B9), and is only meaningful if a running balance exists to report.

This differs from the individual-user pay-then-submit model: here, submission is free; the fee is settled only once RERA has approved the transaction, per the platform's Lodge → Validate → Audit → **Pay** → Issue pipeline.

## 10. Processing Authority

**Two gates**, sourced from row 30 ("transaction audited by bank auditor" before it is "sent to Department for auditing"):

1. **Internal Certifier** — a functional label, not a role or scope: any of the institution's four Group C users may act as internal certifier for a given transaction, including the person who filed it, with the acting user and their role recorded in the audit trail. **Corrected 2026-08-14** — previously modelled as a `checker permission scope` (A1/D2); permission scopes are retired module-wide, see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle). The source's "bank auditor" step is this unrestricted internal certify-or-return action.  
2. **Compliance & Escrow Auditor** (Group A) — the external regulatory gate. All 18 Group C services are approved here; no Group C service is self-approving.

## 11. Expected Processing Time

**20–25 minutes.**

Sourced from row 30 as a single end-to-end figure (unlike Services #1/#2, this SLA is not split into waiting/delivery components, so the A6 reading does not apply here).

## 12. Processing Workflow

Borrower (Customer)

Complete Mortgage Requirements with Bank  
↓  
Provide Mortgage Documents to Bank

↓

Mortgage Officer

Login to Online Mortgage System  
↓  
Select Registered Property  
↓  
Enter Borrower & Mortgage Information  
↓  
Upload Required Documents  
↓  
Submit for Internal Certification

↓

Internal Certifier (any Group C role, including the filer)

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

### Assisted-Mode Alternative (C2)

Trustee Centre Operator

Customer / Institution Representative Visits Real Estate Registration Trustee Centre  
↓  
Submit Documents  
↓  
Enter Transaction into System on the Institution's Behalf  
↓  
Pay Fees at Counter  
↓  
Receive Output via Email

> **Proposed** — the source's "–V" variant reads only as "Visit trustee office, submit docs, enter system, pay fees, receive output via email," without stating whether the counter payment still draws from the institution's settlement account or is a separate at-counter mechanism. Documented as the same online service in assisted mode per C2, but the payment-source question is carried forward — see Open Questions.

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
* Expired *(approved but unsettled for 30 calendar days — B3)*

Uses the platform core status vocabulary plus the Group C extension (D1): `Pending Internal Certification` and `Returned by Certifier` sit before `Submitted`, since this service's two-gate pattern is directly sourced (unlike Services #1/#2).

## 14. Possible Outcomes

* Mortgage Successfully Registered  
* Additional Information Requested  
* Application Returned (internal certifier or RERA)  
* Application Rejected  
* Insufficient Settlement Balance / Payment Failed  
* Approval Expired  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* The applicable one of: Certificate of Title / Title Deed / Usufruct Title Deed / Statement Certificate / Provisional Sale Registration Certificate, depending on the property's existing registration type — sourced (row 30)  
* Fee Balance — the institution's updated settlement-account statement line, **not** a payment receipt (B9)

## 16. Related Services

* Service #4 — Mortgage Amendment  
* Service #5 — Mortgage Transfer  
* Service #6 — Mortgage Release  
* Service #7 — Grant Property Mortgage  
* Individual-user Service #8 — Register Sale of Mortgaged Property *(cross-module: describes the seller/purchaser side of a sale where the property carries a mortgage this service registered; that flow's Mortgage Release Letter corresponds to this module's Service #6)*

## 17. UI Screens

* Services  
* Mortgage Registration  
* Select Property  
* Borrower Information  
* Mortgage Information  
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
* Submit Mortgage Registration Application  
* Retrieve Application Status  
* Deduct Settlement Account Fee  
* Generate Certificate of Title / Statement Certificate  
* Update Mortgage Registry  
* Send Notifications

## 19. Database Entities

* User  
* Institution  
* Institution Staff *(no scope field — every staff member has identical system access; role is recorded per-action, not per-account)*  
* Property  
* Property Ownership  
* Mortgage  
* Certification Record *(now includes the acting user and their role at time of certification, per [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle) — not a scope reference)*  
* Application  
* Service Request  
* Document  
* Settlement Account  
* Settlement Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Mortgage Officer can initiate mortgage registration against a registered title (or a Trustee Centre operator, in assisted mode).  
* System validates the property is registered and its title is verified before registration.  
* Internal certifier — any of the four Group C roles, including the filer — can certify or return the transaction before it reaches RERA.  
* Required information and documents are validated before submission.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is deducted from the institution's settlement account only after approval.  
* Submission is blocked if the projected settlement balance after fees would go negative.  
* Application receives a unique application reference number.  
* Approved registrations update the official mortgage and property registry.  
* Institution and customer receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Mortgage Officer acting under the lending institution's corporate account, or a Trustee Centre operator acting on the institution's behalf in assisted mode, may initiate mortgage registration.  
2. The property must be registered with RERAN and its title verified before a mortgage can be registered against it.  
3. The transaction must pass internal institutional certification before it is routed to RERA. Certification is an unrestricted action any of the institution's four Group C users may perform, including the filer — not a maker-checker restriction and not gated by a permission scope.  
4. Payment is deducted from the institution's standing settlement account only after RERA approval, never before submission (B1).  
5. Submission is blocked if the projected settlement account balance after fees would go negative; a low-balance warning is shown at a configurable threshold (B4).  
6. An approved but unsettled transaction lapses to Expired after 30 calendar days (B3).  
7. Every application receives a unique application reference number.  
8. All applications, certifications, approvals, settlement deductions, and notifications are permanently recorded in the audit trail.

## Open Questions

The following could not be closed by row 30 or by the answers doc, and are carried forward rather than dropped:

1. **Does the Trustee-Centre-assisted variant draw from the institution's settlement account, or use a separate at-counter payment?** The source's "pay fees" at the counter is ambiguous against the account-debit model established for the primary channel.  
2. **Which of the five possible output documents applies to a given mortgage** (Certificate of Title vs. Title Deed vs. Usufruct Title Deed vs. Statement Certificate vs. Provisional Sale Registration Certificate)? The source lists all five as possibilities without stating the selection criteria.  
3. **Exact fee schedule** (bands, floor, cap). Client data — see `open-questions.md` B5, B6.
