---
project: RERAN
module: real-estate-service-companies
type: user-group
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - real-estate-service-companies
  - roles
---

# Real Estate Service Companies — Roles & Responsibilities

Four roles operating under a licensed firm. Unlike Group C, service ownership here is well distributed — every role owns services.

Post-login responsibilities only.

## Role Summary

| Role | Player | Services owned | Sub-domain |
| :---- | :---- | :---: | :---- |
| Owners'-Association Manager | JOP / strata manager | 11 | Jointly Owned Property |
| Brokerage Principal | Licensed broker | 10 | Licensing, Transactions |
| Property Management Officer | Management firm | 3 | Rental |
| Company Dispute Filing Officer | Firm legal staff | 2 | Disputes |

---

## 1. Owners'-Association Manager

**Player:** JOP / strata manager

### Purpose

Registers and administers jointly owned properties on behalf of owners' associations, managing service-charge budgets, escrow accounts and the appointment of auditors.

### Responsibilities

* Register the firm for administrative supervision of jointly owned properties
* Register owners' associations
* Submit service fees and utilisation fees for approval
* Register employees with professional competence in JOP management
* Manage the JOP escrow account: transfers, authorised signatories, closure no-objection letters
* Appoint financial auditors and audit offices for accounts and budgets
* Submit auditing firm approvals and renewals

### Practical Example

A residential tower's owners' association appoints the firm to manage the building. The Manager registers the association on the platform, submits the annual service-charge budget for RERA approval, nominates an audit office to review the accounts, and applies to add two new authorised signatories to the building's escrow account.

---

## 2. Brokerage Principal

**Player:** Licensed broker

### Purpose

Holds the firm's licence, maintains the professional standing of its agents, and handles auction-related transactions.

### Responsibilities

* Apply for and maintain the firm's real estate licence
* Apply for real estate permits, including advertising permits
* Issue, renew, amend and cancel professional practice cards for agents
* Register real estate evaluation certificates
* Apply for accreditation of training entities
* Obtain permits to sell property by public auction
* Register properties sold at auction

### Practical Example

A new agent joins the firm. The Principal applies for a professional practice card, which is issued electronically and printable from the system. Separately, the firm secures a permit to auction a commercial property and, once sold, registers the auction sale — producing a title certificate, map and payment receipt for the buyer.

---

## 3. Property Management Officer

**Player:** Management firm

### Purpose

Registers and maintains real estate management contracts and the tenancy-system users who work under them.

### Responsibilities

* Register and renew real estate management contracts
* Cancel management contracts
* Register users in the tenancy system

### Practical Example

A landlord engages the firm to manage a portfolio of rental units. The Officer registers the management contract in the tenancy system, receives the registered contract by email, and provisions a colleague as a tenancy-system user to handle day-to-day lease registrations.

---

## 4. Company Dispute Filing Officer

**Player:** Firm legal staff

### Purpose

Files and pursues disputes relating to managed or jointly owned properties.

### Responsibilities

* File primary suits concerning joint property
* File execution cases to enforce judgments awarded by the judicial committees
* Attend hearings through the remote-litigation system
* Track case status and retrieve judgments

### Practical Example

Several owners in a managed building have not paid service charges for two years. The Officer files a primary suit through the Dispute Filing Portal, attaches the arrears schedule and association resolution, pays the filing fee, attends the hearing remotely, and later files an execution case to enforce the judgment.

---

## How They Work Together

Unlike Group C, these four roles rarely interact. Each operates in its own sub-domain with its own sub-system, its own approver, and its own outputs.

| Role | Approver |
| :---- | :---- |
| Owners'-Association Manager | Compliance & Escrow Auditor |
| Brokerage Principal | Licensing & Registration Officer |
| Property Management Officer | Compliance & Escrow Auditor |
| Company Dispute Filing Officer | Dispute Adjudication Officer |

> **Proposed** — not in source material. Rationale: the source assigns each service a responsible role and an approver, and the pattern above emerges consistently across all 26 rows. The observation that the roles do not interact is ours, drawn from the absence of any service naming two Group D roles. Needs client confirmation.

**Implication for the UI:** a shared dashboard serving all four roles would show four unrelated sets of work. Role-specific landing pages are likely to fit this module better than the single-dashboard pattern used elsewhere.

## To Confirm

1. Can one firm hold multiple Group D roles at once — brokerage and property management, for example?
2. Do the four roles genuinely never interact, or is there coordination the source omits?
3. Is the Brokerage Principal the only role that can issue practice cards, or can agents self-apply?
4. Who acts when a firm manages a jointly owned property *and* brokers sales within it?
