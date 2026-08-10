---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md" (row 44)
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - service-flow
---

# Service #17 – Issue Title Deed

**Service Category:** Title & Ownership Transaction Services

## 1. Service Overview

The **Issue Title Deed** service is a Group C service defined by row 44 of the master service table. This document carries forward the row’s workflow, channel, output and SLA, while marking design detail not enumerated by the source as proposed.

## 2. Purpose

Provide a controlled and auditable route to complete issue title deed and issue the source-specified output after regulatory review and settlement.

## 3. Description

Documents are submitted, data is entered, fees are paid, the transaction is reviewed and approved, and the title deed is emailed.

## 4. Who Can Apply

* **Mortgage Officer where bank-originated; otherwise a Trustee Centre operator acting for the customer** for the applicable transaction.
* An accredited Trustee Centre or Land Department operator may act for the customer where the source names that counter. **Proposed** — this is assisted access to the same online service, not a separate offline channel.
* The underlying institution or customer must be identified for the request. **Proposed**

## 5. Prerequisites

* Active corporate or operator account with a filing permission scope. **Proposed**
* Relevant property, institutional, mortgage, lease or contract reference.
* Authority to act for the represented institution or customer. **Proposed**
* Supporting documents ready for upload or operator-assisted capture. **Proposed**
* Sufficient settlement-account balance before fee settlement. **Proposed**

## 6. Required Information

* Applicant and represented customer/institution details. **Proposed**
* Relevant property, title, mortgage, lease, contract or register reference. **Proposed**
* Transaction-specific details, effective date and declarations. **Proposed**
* Contact email for delivery where the source says the output is emailed. **Proposed**

## 7. Required Documents

> **Proposed** — row 44 says to submit or enter documents but does not enumerate them. This working list is analogous to the individual-user template and remains client data for confirmation.

* current title/property reference
* transaction authority evidence
* party identity evidence
* supporting transaction documentation

## 8. Service Fee

> **Proposed** — fee amounts are unavailable client data.

Applicable according to the RERAN fee schedule.

## 9. Payment Required

**Yes.**

> **Proposed** — after approval, the fee is deducted from the institution’s standing pre-funded RERAN account, rather than through a pay-then-submit checkout. The source’s payment step remains applicable. An assisted operator records the same online transaction, not a separate offline payment flow.

## 10. Processing Authority

**Compliance & Escrow Auditor (Group A).** A configured internal certification is a maker-checker permission scope on the corporate account, not a fifth Group C role. **Proposed**

## 11. Expected Processing Time

**25 minutes.**

## 12. Processing Workflow

1. The applicant signs in, or an accredited operator opens the same service in assisted mode. **Proposed**
2. The applicant selects **Issue Title Deed**, enters required data and submits documents.
3. The platform validates completeness and relevant references. **Proposed**
4. For a bank-originated filing, a delegated checker scope certifies or returns it before RERAN submission. **Proposed**
5. The Compliance & Escrow Auditor reviews, approves, returns for correction or rejects.
6. After approval, the standing account settles the fee. **Proposed**
7. The platform issues the source-specified output and records the transaction; delivery is electronic where stated.

**Source workflow detail:** Documents are submitted, data is entered, fees are paid, the transaction is reviewed and approved, and the title deed is emailed.

## 13. Application Status Flow

> **Proposed** — the source gives no status vocabulary; this applies the agreed platform core and Group C extension.

Draft → Pending Internal Certification → Returned by Certifier → Submitted → Under Review → Information Requested → Returned for Correction → Approved — Awaiting Payment → Completed

Exception statuses: Rejected, Withdrawn, Payment Failed and Approval Expired. An approved but unsettled item expires after 30 calendar days. **Proposed**

## 14. Possible Outcomes

* Approved and completed, with output issued.
* Returned for correction or additional information.
* Rejected with documented reason.
* Payment failure for insufficient standing balance. **Proposed**
* Approval Expired after the 30-day settlement window. **Proposed**

## 15. Output

The source specifies the following output(s):

* Electronic Title Deed Certificate

A **fee balance** is the standing-account position after deduction; a payment receipt or e-receipt voucher proves a single settlement. They are distinct artefacts. **Proposed**

## 16. Related Services

* [Group C services overview](../services-overview.md) and [payment model](../payments.md).

* Application tracking, document management, corporate permission scopes and settlement account. **Proposed**

## 17. UI Screens

> **Proposed** — derived from the source workflow and the individual-user template.

* Service selection; application details; reference validation; document upload; review and submission.
* Internal certification queue where maker-checker is enabled.
* RERAN review, information request and decision view.
* Settlement-account balance/payment result; output download and application timeline.

## 18. API Requirements

> **Proposed** — derived from the source workflow and the individual-user template.

* Retrieve and validate relevant property, title, institution and transaction references.
* Create, save, submit, return and resubmit applications; upload/retrieve documents.
* Route internal certification and RERAN audit; record decision reasons.
* Calculate fees, check and debit standing balance, issue output/receipt/balance entry and send notifications.

## 19. Database Entities

> **Proposed** — derived from the source workflow and the individual-user template.

* Corporate Account, Permission Scope, User, Customer/Institution and assisted Operator.
* Property, Title Record and relevant Mortgage, Finance Lease or Contract record.
* Application, Service Request, Document, Certification Action, Audit Decision and Audit Log.
* Settlement Account, Fee Charge, Payment Receipt, Fee Balance Ledger Entry, Issued Document and Notification.

## 20. Acceptance Criteria

> **Proposed** — derived from the source workflow and the individual-user template.

* An authorised applicant or assisted operator can start and save the service request.
* Required information and documents validate before submission.
* A maker-checker scope can certify or return a bank-originated request where configured.
* RERAN can approve, return or reject with a reason.
* An approved request debits the standing account before outputs release.
* Source-specified outputs issue electronically and the full trail is auditable.
* Fee balance and receipt remain distinct where both apply.

## 21. Business Rules

1. The workflow, channel, output and SLA are sourced from row 44.
2. The source’s named Trustee Centre or Land Department is an assisted mode of the same online service. **Proposed**
3. Internal certification is a permission scope, not a new role. **Proposed**
4. Fees settle after approval from a standing pre-funded account; negative balances are prohibited. **Proposed**
5. No amount is invented: the fee schedule remains client data.
6. The detailed documents remain genuinely open because the source only says “submit documents”; Section 7 carries a marked working proposal instead of dropping that question.
7. No statutory window or SLA beyond row 44 is asserted.
