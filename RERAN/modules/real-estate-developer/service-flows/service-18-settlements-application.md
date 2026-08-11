---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-10
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/real-estate-developer/ui/screens/sales-and-disclosures.md"
  - "RERAN/modules/real-estate-developer/ui/screens/sales-and-disclosure-details.md"
tags:
  - real-estate-developer
  - service-flow
  - real-estate-development-services
---

# Service #18 – Settlements Application

**Service Category:** Real Estate Development Services

## 1. Service Overview

The **Settlements Application** service allows a developer to submit a settlement application in connection with a property sale, through the Title Deed portal.

> **UI framing mismatch — flagged, not resolved.** The source names this service "Settlements Application," terse and undetailed. The closest matching screens, `sales-and-disclosures.md` and `sales-and-disclosure-details.md`, are built around a considerably richer "Sales Disclosure" concept (buyer verification, disclosure validation, compliance review) that the source row's few words don't confirm or rule out as the same thing. Documented against these screens as the best available fit, with the terminology gap called out rather than silently resolved in either direction.

## 2. Purpose

Allow a developer to formally settle matters connected with a property sale — most plausibly a disclosure or completion step following a sale — with RERA review before parties are notified.

## 3. Description

The developer registers or logs in to the Title Deed portal, selects the settlements service, pays the applicable fee, and sends the application online. An employee receives and reviews the application, approving or rejecting it (re-sent to the developer if rejected). If approved, an e-mail is sent to the parties involved.

## 4. Who Can Apply

* Sales & Disclosure Officer

## 5. Prerequisites

* Registered developer company account.
* An underlying property sale (see Service #1) to settle.
* Required supporting documents available.

## 6. Required Information

* Sale/Property Reference Number
* Parties to the Settlement
* Settlement Terms

## 7. Required Documents

> **Proposed** — not itemized in the source. Following the general sales-disclosure document pattern this module's UI describes. Needs client confirmation.

* Settlement Agreement
* Proof of Payment
* Other supporting documents required by RERA

## 8. Service Fee

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes** — fees are paid before the application is sent.

## 10. Processing Authority

**Compliance & Escrow Auditor**

## 11. Expected Processing Time

**7 hours 30 minutes**

## 12. Processing Workflow

Register / Login to Title Deed Portal
↓
Select "Settlements Application"
↓
Pay Fees
↓
Send Application Online
↓
Employee Receives and Reviews Application
↓
Approval or Rejection
↓
If Rejected: Re-sent to Developer
↓
If Approved: E-mail Sent to Parties

## 13. Application Status Flow

Draft
↓
Payment Pending
↓
Payment Successful
↓
Submitted
↓
Under Review
↓
Approved
↓
Settled

### Additional Statuses

* Returned
* Rejected

## 14. Possible Outcomes

* Settlement Successfully Approved
* Application Returned
* Application Rejected
* Payment Failed

## 15. Output

Not specified in the source ("no doc" against this row) beyond the confirmation e-mail to parties. **Proposed**: an in-system Settlement Confirmation record in addition to the e-mail; needs client confirmation.

## 16. Related Services

* Service #1 – Register Initial Sale
* Individual User Service #26 – Submit Tenancy Dispute *(cross-module: the individual-user-side settlement/dispute path, if the two are related — flagged as a possible connection, not confirmed)*

## 17. UI Screens

* Sales & Disclosures *(closest match — see the framing-mismatch note in Section 1)*
* Sales & Disclosure Details
* Payment
* Application Submitted

## 18. API Requirements

* Validate Underlying Sale
* Calculate Service Fee
* Initiate Payment
* Verify Payment
* Submit Settlement Application
* Retrieve Application Status
* Notify Parties
* Send Notifications

## 19. Database Entities

* Developer Company
* Property Sale
* Settlement
* Application
* Document
* Payment
* Payment Transaction
* Notification
* Audit Log

## 20. Acceptance Criteria

* Developer can submit a settlement application referencing an underlying property sale.
* Payment is completed before the application is sent for review.
* Rejected applications are returned to the developer with reasons.
* Approved settlements trigger a notification e-mail to all parties.
* All activities are recorded in the audit log.

## 21. Business Rules

1. A settlement application must reference an underlying property sale.
2. Payment must be completed before the application is submitted for review.
3. Rejected applications are returned to the developer rather than silently closed.
4. All submissions, reviews, payments, and notifications must be permanently recorded in the audit trail.
5. **Terminology gap between source ("Settlements") and UI ("Sales Disclosure") not resolved** — flagged for client confirmation of whether these are the same service.
