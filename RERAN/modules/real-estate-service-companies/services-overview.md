---
project: RERAN
module: real-estate-service-companies
type: overview
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - real-estate-service-companies
  - services-overview
---

# Real Estate Service Companies — Services Overview

26 business services, verified against the master service table (rows 46–71). Reconciles with the source workbook summary: JOP 11 + Licensing 8 + Rental 3 + Transaction 2 + Disputes 2 = 26.

## Business Services

### 1. Jointly Owned Property Services (11)

Owner: Owners'-Association Manager · Approver: Compliance & Escrow Auditor

* Service #1 — Register real estate company for administrative supervision of joint ownership properties
* Service #2 — Approval of service fees and utilisation fees
* Service #3 — Register employees with professional competence in JOP management
* Service #4 — Registration of Owners Association
* Service #5 — Approval for transferring the JOP escrow account
* Service #6 — Approval for issuing a no-objection letter to close the project escrow account
* Service #7 — Approval to accredit authorised signatories on the escrow account
* Service #8 — Appoint a financial auditor with specific responsibilities
* Service #9 — Approval to appoint an audit office for auditing JOP financial accounts
* Service #10 — Approval to appoint an audit office to audit the budget for a joint property
* Service #11 — Approval / renewal of a Financial Auditing company

### 2. Licensing Services (8)

Owner: Brokerage Principal · Approver: Licensing & Registration Officer

* Service #12 — Real estate licensing application
* Service #13 — Real estate permit application
* Service #14 — Issuance of a real estate professional practice card
* Service #15 — Renewing a professional practice card
* Service #16 — Cancellation of a professional practice card
* Service #17 — Professional practice card amendment
* Service #18 — Real estate evaluation details certificate registration
* Service #19 — Accreditation of Training Entities

### 3. Rental Services (3)

Owner: Property Management Officer · Approver: Compliance & Escrow Auditor

* Service #20 — Registration and renewal of the real estate management contract
* Service #21 — Cancel the real estate management contract
* Service #22 — Registration of a user in the tenancy system

### 4. Transaction Services (2)

Owner: Brokerage Principal · Approver: Compliance & Escrow Auditor

* Service #23 — Permit to sell real estate by public auction
* Service #24 — Registration of a property sold by auction

### 5. Dispute Services (2)

Owner: Company Dispute Filing Officer · Approver: Dispute Adjudication Officer

* Service #25 — Primary suit (joint property)
* Service #26 — Execution case (joint ownership)

## Summary

| Category | Services | Owner |
| :---- | :---: | :---- |
| Jointly Owned Property | 11 | Owners'-Association Manager |
| Licensing | 8 | Brokerage Principal |
| Rental | 3 | Property Management Officer |
| Transaction | 2 | Brokerage Principal |
| Disputes | 2 | Company Dispute Filing Officer |
| **Total** | **26** | |

Category names here follow the source's own grouping, unlike Group C where a user-facing regrouping was proposed. The source categories already describe distinct business activities rather than internal filing structure, so no regrouping is warranted.

## Notable Patterns

**Seven JOP services share one workflow.** Services #5 through #11 all follow the identical five-step shape: sign up or log in to the Owner system, fill details and attach documents, submit, audit and acceptance or rejection, receive approval by email. Several are recorded in the source as "same as transferring escrow account steps". One flow document with parameterised variations may serve better than seven near-identical files.

**Two services are automatically approved.** Practice card renewal and amendment are approved by the system with no officer review, per the source. These need a distinct flow shape with no audit stage.

**One service runs entirely over email.** JOP escrow account closure no-objection (#6) is submitted by attaching an approved form to an email, with a three-business-day turnaround. There is no online path today.

**Two services run over email rather than the platform.** Accreditation of Training Entities (#19) is a five-step manual process — apply, meet, view proposal, submit partnership application, sign agreement — conducted by email over four business days. It is barely a platform service at all.

> **Proposed** — the observations above are ours, drawn from reading the 26 source rows. The consolidation suggestion for the seven JOP services is a documentation recommendation, not a client requirement. Needs confirmation.

## Channels

* Land Department website (Owner system) — JOP services
* Land Department website (Digital system) — licensing and practice cards
* Land Department website (Tenancy system) — rental services
* RERA App — evaluation certificates, some permits, practice card renewal
* Official email — JOP closure no-objection, training entity accreditation
* Real Estate Services Trustee Centres — dispute filing

## To Confirm

1. Should the seven near-identical JOP escrow services be documented as one parameterised flow or seven separate documents?
2. Are the email-only services (#6, #19) intended to move onto the platform, or stay manual?
3. Automatic approval for practice card renewal and amendment — is that correct, and are there conditions that would force manual review?
4. Does JOP warrant its own module rather than sitting inside Group D?
5. Service #11 (approval/renewal of a Financial Auditing company) closely resembles Group C Service #1 (approval/renewal of Account Trustee & Auditing company). Are these the same process viewed from two sides?
