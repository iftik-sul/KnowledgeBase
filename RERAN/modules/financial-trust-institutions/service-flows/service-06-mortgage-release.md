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
  - release
---

# Service #6 – Mortgage Release

**Service Category:** Mortgage Services

**Source row:** 33 of `RERAN_service_flows_v2.md`. The source defines this row by reference — "Same as mortgage registration" — for both its bank-originated and Trustee-Centre-assisted variants. Expanded in full below, per the issue's instruction. **A release discharges an encumbrance; a registration creates one — they are not the same flow**, and the difference is reflected throughout this document.

## 1. Service Overview

The **Mortgage Release** service discharges an existing registered mortgage once the underlying loan has been settled (or the security is otherwise released), removing the encumbrance from the property registry. It is the mechanism referenced by individual-user Service #8 (Register Sale of Mortgaged Property) as the source of the Mortgage Release Letter required before a mortgaged property can complete a sale.

## 2. Purpose

Formally discharge a mortgage once it is no longer secured, so the property registry — and any party relying on it, including a purchaser under individual-user Service #8 — reflects that the title is no longer encumbered.

## 3. Description

The bank confirms settlement (or other release grounds) of the underlying loan. A Mortgage Officer enters the release into the Online Mortgage System against the existing mortgage record, attaching evidence of settlement. The transaction is certified internally, then audited by RERA using the same workflow structure as mortgage registration. On approval, the fee is deducted from the institution's settlement account, the mortgage is discharged on the registry, and the output documents — including the Mortgage Release Letter, where the mortgage was itself registered — are delivered to the customer by email. The service can alternatively be processed in assisted mode at a Real Estate Registration Trustee Centre.

## 4. Who Can Apply

### Applicant (Mortgagee Institution)

* Mortgage Officer — primary channel, via the Online Mortgage System  
* Trustee Centre Operator (Group G) — assisted mode (C2)

### Counterparty (Borrower / Property Owner)

* The registered mortgagor whose mortgage is being released

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with a Mortgage Officer provisioned.  
* An existing, active registered mortgage against the property.  
* The underlying loan has been settled, or other grounds for release apply.  
* Institution's settlement account holds a sufficient prefunded balance to absorb the fee once approved (B1, B4).

## 6. Required Information

### Existing Mortgage Reference

* Mortgage Registration Number  
* Property Registration Number

### Release Information

* Grounds for Release (e.g., loan settlement, refinancing, court order)  
* Date of Settlement / Release Event  
* Confirming Institution Officer

## 7. Required Documents

> **Proposed** — by analogy with Service #3 and with individual-user Service #8, which requires a Mortgage Release Letter from the mortgage lender as a precondition of its own workflow.

* Existing Certificate of Title / Title Deed  
* Original Mortgage Agreement  
* Evidence of Loan Settlement (e.g., final payment confirmation, discharge statement)  
* Deed of Release / Discharge of Mortgage  
* Government-issued Identification (Borrower)  
* Internal Certification Record  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

> **Proposed** — ad valorem/banded basis per B6, or a flat discharge fee, given the service does not create a new secured amount to base a percentage on. Exact schedule is client data (B5). See Open Questions.

## 9. Payment Required

**Yes** — Institution Account Debit model (B1), same structure as Service #3. Deducted from the institution's settlement account after RERA approval.

## 10. Processing Authority

**Two gates**, same structure as Service #3:

1. **Internal Certifier** — a functional label, not a role or scope: any of the institution's four Group C users may act as internal certifier, including the person who filed the transaction. **Corrected 2026-08-14** — previously `checker permission scope` (A1/D2), now retired; see [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle).  
2. **Compliance & Escrow Auditor** (Group A).

## 11. Expected Processing Time

**10–15 minutes.** Sourced from row 33 as a single end-to-end figure.

## 12. Processing Workflow

Mortgagee Institution

Confirm Loan Settlement / Release Grounds

↓

Mortgage Officer

Login to Online Mortgage System  
↓  
Select Existing Mortgage Record  
↓  
Enter Release Information  
↓  
Upload Settlement / Discharge Evidence  
↓  
Submit for Internal Certification

↓

Internal Certifier

Review Release  
↓  
Certify, or Return to Mortgage Officer

↓

RERA

Receive in Transaction Audit Queue  
↓  
Audit Release  
↓  
Approve, Return, or Reject  
↓  
Deduct Fee from Institution Settlement Account  
↓  
Discharge Mortgage on Property Registry  
↓  
Generate Output Documents, Including Mortgage Release Letter (Where Registered)  
↓  
Deliver Outputs to Customer via Email

### Assisted-Mode Alternative (C2)

Trustee Centre Operator

Visit Real Estate Registration Trustee Centre  
↓  
Submit Documents  
↓  
Enter Release into System on the Institution's Behalf  
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

* Mortgage Successfully Released / Discharged  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Insufficient Settlement Balance / Payment Failed  
* Approval Expired  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Mortgage Release Letter *(where the mortgage was itself registered)* — sourced (row 33)  
* The applicable one of: Certificate of Title / Title Deed / Usufruct Title Deed / Statement Certificate / Provisional Sale Registration Certificate, reissued free of the discharged encumbrance — sourced (row 33)  
* Fee Balance — settlement-account statement line, not a receipt (B9)

## 16. Related Services

* Service #3 — Mortgage Registration  
* Service #4 — Mortgage Amendment  
* Service #5 — Mortgage Transfer  
* Individual-user Service #8 — Register Sale of Mortgaged Property *(cross-module — this service is the source of that flow's required Mortgage Release Letter, which must be received before individual-user Service #8 can complete ownership transfer)*

## 17. UI Screens

* Services  
* Mortgage Release  
* Select Existing Mortgage  
* Release Information  
* Document Upload  
* Internal Certification Queue  
* Application Review  
* Settlement Account Confirmation  
* Application Submitted  
* Application Details  
* Release Confirmation

## 18. API Requirements

* Retrieve Existing Mortgage Record  
* Validate Mortgage Status  
* Upload Documents  
* Submit for Internal Certification  
* Retrieve Certification Status  
* Calculate Service Fee  
* Check Settlement Account Balance  
* Submit Mortgage Release Application  
* Retrieve Application Status  
* Deduct Settlement Account Fee  
* Discharge Mortgage on Property Registry  
* Generate Mortgage Release Letter  
* Generate Updated Certificate / Statement Certificate  
* Send Notifications

## 19. Database Entities

* Institution  
* Institution Staff *(no scope field — every staff member has identical system access; role is recorded per-action, not per-account)*  
* Property  
* Mortgage  
* Mortgage Release  
* Certification Record *(now includes the acting user and their role at time of certification, per [navigation.md#audit-trail-principle](../navigation.md#audit-trail-principle) — not a scope reference)*  
* Application  
* Service Request  
* Document  
* Settlement Account  
* Settlement Transaction  
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Mortgage Officer can select an existing mortgage and submit release information with settlement evidence.  
* System validates the mortgage is active and registered before allowing release.  
* Internal certifier — any of the four Group C roles, including the filer — can certify or return the release before it reaches RERA.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is deducted from the institution's settlement account only after approval.  
* Application receives a unique application reference number.  
* Approved releases discharge the mortgage on the official property registry and issue a Mortgage Release Letter.  
* Institution and customer receive completion notifications.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. Only a Mortgage Officer, or a Trustee Centre operator acting on the institution's behalf, may initiate a release.  
2. The mortgage being released must be active and registered.  
3. The transaction must pass internal institutional certification before routing to RERA.  
4. Payment is deducted from the institution's settlement account only after approval (B1).  
5. Submission is blocked if the projected settlement balance after fees would go negative (B4).  
6. An approved but unsettled transaction lapses to Expired after 30 calendar days (B3).  
7. A Mortgage Release Letter is issued only where the mortgage was itself registered on the platform.  
8. Every application receives a unique application reference number.  
9. All applications, certifications, approvals, settlement deductions, discharges, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Fee basis for release**, given there is no new secured amount to apply an ad valorem rate to — flat fee or a rate against the original secured amount? Not specified in source.  
2. **Grounds for release beyond loan settlement** (e.g., refinancing, court order) and any evidentiary differences between them. Not specified in source.  
3. **Exact fee schedule.** Client data — see `open-questions.md` B5, B6.
