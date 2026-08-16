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
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-06-register-mortgage-linked-sale.md"
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

> **New inbound dependency, 2026-08-16, by client decision.** Real-estate-developer's Service #6 (Register Sale Associated with an Initial Mortgage) now validates its mortgage reference against this service's own records before that sale can proceed to RERA's audit. This module's own workflow is unchanged by that decision — it is documented here as an inbound dependency, not a change to this service's process. See Section 16 and Open Questions for what's still unsettled about it, particularly which stage of *this* service's own lifecycle (below) a validating query is expected to accept.

## 2. Purpose

Register a mortgage against a verified title so the lending institution's security interest is legally recognized on the property registry, protecting the interests of the lender, the borrower, and any subsequent party who searches the title.

## 3. Description

The customer (borrower) completes mortgage requirements directly with the bank — loan approval, valuation, executed mortgage deed. Any of the institution's four Group C roles then enters the transaction into the Online Mortgage System, pays the fee upfront via the shared platform payment gateway, and attaches the required documents. **Corrected 2026-08-15** — this previously named the Mortgage Officer specifically; `open-questions.md` A4 confirms no service is role-specific. The transaction is certified internally by any of the institution's four Group C users, including the person who filed it, before it is sent to RERA's Transaction Audit queue. On approval, the output documents are delivered to the customer by email. The same service can alternatively be processed in assisted mode at a Real Estate Registration Trustee Centre.

## 4. Who Can Apply

### Applicant (Lending Institution)

* Any of the institution's four Group C roles — primary channel, via the Online Mortgage System. **Confirmed 2026-08-15** — previously listed as Mortgage Officer only; `open-questions.md` A4 confirms no service is role-specific.
* Trustee Centre Operator (Group G) — assisted mode, acting on the institution's behalf at a Real Estate Registration Trustee Centre *(C2: this is the same online service in assisted mode, not a separate channel)*

### Counterparty (Borrower / Property Owner)

* Registered Property Owner granting the mortgage, who must hold a verified RERAN title

## 5. Prerequisites

* Registered RERAN institution (Group C) account, with staff provisioned under the corporate account.  
* Property is registered with RERAN and its title is verified.  
* Customer has completed mortgage requirements with the bank (loan approval, valuation, executed mortgage deed) before system entry.  
* Payment has been completed via the shared platform payment gateway before the application is lodged (B1).

## 6. Required Information

### Institution Information

* Institution Name  
* Acting Officer Identifier  
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

> **Corrected 2026-08-14** — per the corrected `open-questions.md` B6, RERA sets this fee directly, per service code, independent of the loan amount or any other figure from the institution's relationship with its customer. Previously proposed as ad valorem/banded on the secured amount; that basis is retired. The exact fee is a configuration fact (B5), not client data awaiting collection.

## 9. Payment Required

**Yes**

Paid upfront by the institution via the shared platform payment gateway, before the application is lodged — not deducted from a standing account, and not paid by the borrower. **Corrected 2026-08-14** — this service was previously described as Institution Account Debit, deducted after RERA approval; that model is retired. See [payments.md](../payments.md) and `open-questions.md` B1 for the corrected pipeline.

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

Institution User (any of the four Group C roles)

Login to Online Mortgage System  
↓  
Select Registered Property  
↓  
Enter Borrower & Mortgage Information  
↓  
Upload Required Documents  
↓  
Pay via Shared Platform Gateway  
↓  
Submit for Internal Certification

↓

Internal Certifier (any Group C role, including the filer)

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

> **Proposed** — the source's "–V" variant reads only as "Visit trustee office, submit docs, enter system, pay fees, receive output via email." Documented as the same online service in assisted mode per C2, paying via the same shared gateway, upfront, as the primary channel (`open-questions.md` B1) — whether the terminal integration itself is identical to the primary channel's checkout is carried forward as a narrower open item; see Open Questions.

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

**Corrected 2026-08-14** — `Approved — Awaiting Payment` and `Expired` (previously "approved but unsettled for 30 calendar days — B3") are removed: payment now happens before lodging, so nothing is ever approved while still awaiting payment, and B3's unsettled-after-approval scenario can no longer occur. B3 itself was not corrected and remains as written in `open-questions.md` — see [payments.md](../payments.md)'s Additional Statuses section for that tension.

Uses the platform core status vocabulary plus the Group C extension (D1): `Pending Internal Certification` and `Returned by Certifier` sit before `Submitted`, since this service's two-gate pattern is directly sourced (unlike Services #1/#2).

**Relevant to the new inbound dependency (see Feature Overview)**: a validating query from real-estate-developer's Service #6 could, in principle, find a mortgage record at any of these stages — `Pending Internal Certification`, `Under Review`, or fully `Completed`. Which of these should count as "validated" for that service's purposes is not settled here; see Open Questions.

## 14. Possible Outcomes

* Mortgage Successfully Registered  
* Additional Information Requested  
* Application Returned (internal certifier or RERA)  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* The applicable one of: Certificate of Title / Title Deed / Usufruct Title Deed / Statement Certificate / Provisional Sale Registration Certificate, depending on the property's existing registration type — sourced (row 30)  
* Payment Receipt — proof the fee settled, issued at checkout before the application was lodged. **Corrected 2026-08-14** — previously "Fee Balance," a standing-account statement line (B9); that artefact no longer exists, see [payments.md](../payments.md).

## 16. Related Services

* Service #4 — Mortgage Amendment  
* Service #5 — Mortgage Transfer  
* Service #6 — Mortgage Release  
* Service #7 — Grant Property Mortgage  
* Individual-user Service #8 — Register Sale of Mortgaged Property *(cross-module: describes the seller/purchaser side of a sale where the property carries a mortgage this service registered; that flow's Mortgage Release Letter corresponds to this module's Service #6)*
* **Added 2026-08-16, by client decision.** Real Estate Developer Service #6 — Register Sale Associated with an Initial Mortgage *(cross-module, inbound: that service now validates its mortgage reference against this service's own records before its own application can proceed to RERA's audit — see Feature Overview and Section 13. Not a sourced relationship; a documented product decision. This service's own workflow is unaffected — it is queried, not changed.)*

## 17. UI Screens

* Services  
* Mortgage Registration  
* Select Property  
* Borrower Information  
* Mortgage Information  
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
* Submit Mortgage Registration Application  
* Retrieve Application Status  
* Process Gateway Payment
* Generate Certificate of Title / Statement Certificate  
* Update Mortgage Registry  
* Send Notifications
* **Expose Mortgage Lookup / Validation** *(added 2026-08-16, by client decision — cross-module endpoint allowing real-estate-developer's Service #6 to check a mortgage reference against this service's records; exact response contract, including which application statuses count as a valid match, is not yet defined — see Open Questions)*

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
* Payment Transaction
* Notification  
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can initiate mortgage registration against a registered title (or a Trustee Centre operator, in assisted mode). **Confirmed 2026-08-15** — not restricted to the Mortgage Officer (A4).  
* System validates the property is registered and its title is verified before registration.  
* Internal certifier — any of the four Group C roles, including the filer — can certify or return the transaction before it reaches RERA.  
* Required information and documents are validated before submission.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Fee is paid via the shared platform payment gateway before the application is lodged.  
* An application cannot be lodged, certified, or submitted for audit until payment succeeds.  
* Application receives a unique application reference number.  
* Approved registrations update the official mortgage and property registry.  
* Institution and customer receive completion notifications.  
* All activities are recorded in the audit log.
* **Added 2026-08-16.** A validating lookup from real-estate-developer's Service #6 returns a result consistent with whatever stage-eligibility rule is eventually settled (see Open Questions) — not yet implemented as a testable criterion.

## 21. Business Rules

1. Any of the institution's four Group C roles acting under the lending institution's corporate account, or a Trustee Centre operator acting on the institution's behalf in assisted mode, may initiate mortgage registration. **Confirmed 2026-08-15** — previously restricted to "only a Mortgage Officer"; `open-questions.md` A4 confirms no service is role-specific.  
2. The property must be registered with RERAN and its title verified before a mortgage can be registered against it.  
3. The transaction must pass internal institutional certification before it is routed to RERA. Certification is an unrestricted action any of the institution's four Group C users may perform, including the filer — not a maker-checker restriction and not gated by a permission scope.  
4. Payment is made via the shared platform payment gateway, upfront, before the application can be lodged — not deducted from a settlement account, and not collected after approval (B1, corrected 2026-08-14).  
5. **Corrected 2026-08-14** — the previous rule 5 (low-balance warning against a projected settlement balance, B4) and rule 6 (approved-but-unsettled lapsing to Expired after 30 days, B3) are removed: there is no balance to project and no post-approval unsettled state to lapse from, once payment happens before lodging. B3 itself was not revisited by this correction and remains as written in `open-questions.md`; see `payments.md`'s Additional Statuses section for that tension.  
6. Every application receives a unique application reference number.  
7. All applications, certifications, approvals, payments, and notifications are permanently recorded in the audit trail.
8. **Added 2026-08-16.** This service does not itself change behavior to accommodate the Service #6 validation dependency — it is queried against, not altered. Any change to what counts as a "valid" match is a decision for that dependency, documented on real-estate-developer's side.

## Open Questions

The following could not be closed by row 30 or by the answers doc, and are carried forward rather than dropped:

1. ~~Does the Trustee-Centre-assisted variant draw from the institution's settlement account, or use a separate at-counter payment?~~ **Resolved by the 2026-08-14 correction** — there is no settlement account for either channel; both pay via the shared platform gateway, upfront. What remains genuinely open: whether the assisted-mode "pay fees at counter" step (Section 12) uses the identical gateway flow or a variant terminal integration — not addressed by source or by this correction.  
2. **Which of the five possible output documents applies to a given mortgage** (Certificate of Title vs. Title Deed vs. Usufruct Title Deed vs. Statement Certificate vs. Provisional Sale Registration Certificate)? The source lists all five as possibilities without stating the selection criteria.  
3. **Exact fee schedule** (bands, floor, cap). Client data — see `open-questions.md` B5, B6.
4. **New 2026-08-16, unresolved.** Which application status(es) of this service satisfy real-estate-developer Service #6's validation check — any existing record regardless of status, `Pending Internal Certification` or later, or only `Completed`? Given Service #6's own name ("Initial Mortgage") suggests the two may be filed around the same time, requiring `Completed` here could create an ordering deadlock between the two services. Not resolved — mirrored as an open question on Service #6's own file.
5. **New 2026-08-16, unresolved.** Real-time synchronous lookup, or asynchronous/batch reconciliation? Not specified.
