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
  - title-deed
---

# Service #15 – Updating Title Deed Information

**Service Category:** Title & Ownership Transaction Services

**Source row:** 42 of `RERAN_service_flows_v2.md`.

## 1. Service Overview

The **Updating Title Deed Information** service corrects or updates information recorded on an existing title deed — for example, a name change or a correction to recorded particulars — without transferring ownership or creating a new encumbrance.

## 2. Purpose

Keep title deed information accurate and current, so the property registry reflects the true, present-day particulars of the registered owner and property.

## 3. Description

The customer visits a Real Estate Services Trustees Centre and submits the required documents, which are checked for completeness. A Trustee Centre employee enters the transaction data. The customer pays the fee and receives a receipt. RERA reviews and approves the update, and the customer receives a link to the updated electronic title deed by email.

## 4. Who Can Apply

### Applicant

* Any of the institution's four Group C roles — where the transaction is bank-originated
* Trustee Centre Operator (Group G) — otherwise, acting on the customer's behalf in assisted mode

> **Confirmed 2026-08-15** — previously conditioned this on the Mortgage Officer specifically, following A4's earlier per-service re-derivation. `open-questions.md` A4 now confirms ownership is not role-specific at all. The Trustee Centre Operator path remains what row 42 itself sources (a walk-in Trustees Centre visit with no bank-employee involvement); whether a bank-originated variant exists for this service at all remains unconfirmed by source — see Open Questions — but that is now a channel question, not a role-ownership one.

### Customer

* Registered Property Owner, or Authorized Representative

## 5. Prerequisites

* The property is registered with RERAN.  
* The requested update is supported by evidence (e.g., legal name change, correction of a recorded error).  
* Required supporting documents are available.

## 6. Required Information

### Property Information

* Property Registration Number  
* Property Address

### Update Information

* Field(s) to be Updated  
* Current Recorded Value  
* Requested New Value  
* Reason for Update

## 7. Required Documents

> **Proposed** — the source states only that documents are "submitted and verified for completeness," without enumerating them.

* Existing Certificate of Title  
* Evidence Supporting the Update (e.g., deed poll / name-change certificate, marriage certificate, corrected survey document)  
* Government-issued Identification (Owner)  
* Other supporting documents required by RERAN

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes**

Paid by the customer at the Trustees Centre, **before** RERA's review and approval — sourced (row 42's own sequence, Step 4 "Pay fees, get receipt" precedes Step 5 "Review and approval"). **Customer Payment at Counter** model, unaffected by the 2026-08-14 payment-model correction (`open-questions.md` B1). *(Corrected 2026-08-14 — previously cited `B9`, now superseded.)*

## 10. Processing Authority

**Compliance & Escrow Auditor** (Group A) — sourced (approver column, row 42; Step 5: "Review and approval").

## 11. Expected Processing Time

**25 minutes.** Sourced from row 42.

## 12. Processing Workflow

Customer

Visit Real Estate Services Trustees Centre *(C2: this is the sourced path for this service, alongside Land Department, also named as a channel in source; Section 4 carries the bank-originated branch as unconfirmed rather than asserting a direct online path here — see Open Questions)*  
↓  
Submit Documents

↓

Trustee Centre Operator

Verify Documents for Completeness  
↓  
Enter Transaction Data

↓

Customer

Pay Fees  
↓  
Obtain Receipt

↓

RERA (Compliance & Escrow Auditor)

Review Application  
↓  
Approve, Return, or Reject

↓

RERA

Generate Updated Electronic Title Deed  
↓  
Deliver Title Deed Link via Email

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

**Corrected 2026-08-15 — `Approved — Awaiting Payment` removed.** This status previously sat between `Returned for Correction` and `Completed`, but contradicts this service's own sourced workflow (Section 12, Section 9): the customer pays at the counter *before* RERA's review and approval (row 42, Step 4 before Step 5), not after. By the time a decision is reached, payment has already happened. This is now the pattern for every fee-bearing Group C service, without exception — see [status-badges.md](../ui/status-badges.md#application-status) for the module-wide confirmation following the 2026-08-16 normalization of Services #12 and #18, the last two services that previously paid after RERA's decision.

## 14. Possible Outcomes

* Title Deed Information Successfully Updated  
* Additional Information Requested  
* Application Returned  
* Application Rejected  
* Payment Failed  
* Application Withdrawn

## 15. Output

Upon successful completion, the system generates:

* Electronic Title Deed Certificate (link delivered via email) — sourced (row 42)

## 16. Related Services

* Service #14 — Company Shares Sale  
* Service #16 — Split Ownership  
* Service #17 — Issuance of Title Deed

## 17. UI Screens

* Services  
* Update Title Deed Information  
* Select Property  
* Update Details  
* Document Upload  
* Application Review  
* Payment  
* Payment Successful  
* Application Submitted  
* Application Details  
* Updated Title Deed

## 18. API Requirements

* Retrieve Property / Title Deed Record  
* Validate Property Ownership  
* Upload Documents  
* Calculate Service Fee  
* Initiate Payment  
* Verify Payment  
* Submit Title Deed Update Application  
* Retrieve Application Status  
* Update Title Deed Record  
* Generate Electronic Title Deed Link  
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

* Property owner or authorized representative can initiate an update at a Trustees Centre.  
* System verifies documents are complete before data entry.  
* Application receives a unique application reference number.  
* Compliance & Escrow Auditor can approve, return, or reject with documented reasoning.  
* Payment is completed at the counter with a receipt issued, before RERA's review.  
* Approved updates are reflected in the official title deed record.  
* Customer receives an updated electronic title deed link on completion.  
* All activities are recorded in the audit log.

## 21. Business Rules

1. This application may be processed by any of the institution's four Group C roles where bank-originated, or otherwise by a Trustee Centre operator acting on the customer's behalf. **Confirmed 2026-08-15** — previously conditioned on the Mortgage Officer specifically; `open-questions.md` A4 confirms no service is role-specific. *(Whether a bank-originated variant exists for this service at all remains unconfirmed by source — only the Trustee-Centre path is confirmed by row 42.)*
2. The property must be registered with RERAN before its title deed information can be updated.  
3. The requested update must be supported by evidence.  
4. Payment is required at the counter, before RERA's review and approval.  
5. Approved updates are reflected in the official title deed record.  
6. Every application receives a unique application reference number.  
7. All applications, approvals, payments, and notifications are permanently recorded in the audit trail.

## Open Questions

1. **Which fields may be updated through this service** versus requiring a different service (e.g., ownership transfer). Not specified in source.  
2. **Whether a new physical/electronic certificate is reissued** or only the underlying record is updated with a link to the same document. Not specified in source.  
3. ~~Whether a bank-originated path (Mortgage Officer, per A4's conditional) exists for this service at all.~~ **Reframed 2026-08-15** — the role-conditional part of this question is resolved: if a bank-originated path exists, any of the four Group C roles may use it, not just a Mortgage Officer (A4). What remains genuinely open is narrower: **whether a bank-originated channel exists for this service at all.** No row among 38, 40–44 describes bank-employee entry the way the mortgage rows (30–33, 39) do; this document still sources only the Trustee-Centre-assisted path.  
4. **Exact fee amount.** Client data — see `open-questions.md` B5.
