---
project: RERAN
module: financial-trust-institutions
type: user-group
status: draft
updated: 2026-08-09
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - financial-trust-institutions
  - roles
---

# Financial & Trust Institutions — Roles & Responsibilities

Group C covers banks, mortgage institutions, account trustees and auditing bureaux that finance, secure and audit real-estate transactions. Four roles operate under a single verified institution account.

This document describes post-login responsibilities only. Account creation and onboarding are out of scope for this project.

## Role Summary

| Role | Player | Services owned | Primary sub-system |
| :---- | :---- | :---: | :---- |
| Mortgage Officer | Bank lending desk | 17 | Online Mortgage System |
| Institution Relationship Manager | Bank admin | 1 | Trust-Account Approval & Renewal |
| Account Trustee | Approved escrow trustee | 0 — see below | Trust-Account Approval & Renewal |
| Auditing Bureau Officer | Approved auditor | 0 — see below | Transaction Audit Queue |

> **Source gap.** The master service table assigns 17 of 18 Group C services to the Mortgage Officer and 1 to the Institution Relationship Manager. Account Trustee and Auditing Bureau Officer own no numbered services, yet the user group structure describes substantial functions for both. Their post-login behaviour below is proposed, not sourced.

---

## 1. Mortgage Officer

**Player:** Bank lending desk

### Purpose

Registers, modifies and discharges mortgages and finance leases against registered titles, and submits completed transactions for departmental audit. The highest-volume role in the module.

### Responsibilities

* Register new mortgages against a verified title
* Amend, transfer and release existing mortgages
* Register, amend, transfer and release finance leases
* Register real estate fund companies in the register of privileges
* Execute title-deed transactions arising from financing: heirs' sale, company share sale, split ownership, title deed issuance and updates
* Attach supporting documentation and submit for internal certification
* Track submitted transactions through the RERA audit queue
* Respond to information requests raised by the Compliance & Escrow Auditor

### Practical Example

A customer completes a mortgage application at the bank. The Mortgage Officer opens the Online Mortgage System, selects the property by title reference, enters the loan particulars and attaches the executed mortgage deed and party identification. The transaction is certified internally, then routed to the RERA Transaction Audit queue. On approval, fees are deducted from the bank's account and the mortgage registration certificate is delivered to both the bank and the property owner.

---

## 2. Institution Relationship Manager

**Player:** Bank admin

### Purpose

Maintains the institution's standing on the platform and manages the people who act under it.

### Responsibilities

* Maintain institutional registration details and banking credentials
* Renew trustee and auditor approvals before expiry
* Provision, scope and revoke staff access within the institution
* Submit contract cancellation applications (Service #18)
* Monitor institution-wide transaction volume and audit outcomes

> **Proposed** — not in source material. Rationale: the source describes this role as maintaining registration, renewing approvals and provisioning users, but only one numbered service exists for it. An institution-level oversight view is implied by the responsibility for renewals and user management, which cannot be discharged without visibility of expiry dates and staff activity. Needs client confirmation.

### Practical Example

The institution's trustee approval is due to expire in 45 days. The Relationship Manager receives a renewal notification, opens the Trust-Account Approval & Renewal system, uploads the updated audited accounts and CBN standing documentation, and submits the renewal. The Compliance & Escrow Auditor reviews and approves; the institution's approved status is extended and reflected in the public register of approved trustees.

---

## 3. Account Trustee

**Player:** Approved escrow trustee

### Purpose

Manages developer project trust accounts, certifies that milestone conditions are met before funds are released, and files audited account statements.

> **Proposed** — not in source material. Rationale: the user group structure names these three functions explicitly, and the Group B developer services show the Account Trustee acting as an approval step in escrow activation, transfer, profit withdrawal and payment requests. Those developer-side services describe the Trustee as a participant but define no Group C interface for them. The responsibilities below reconstruct what that interface must provide. Needs client confirmation.

### Responsibilities

* Review and act on escrow requests routed from developers: account activation, account transfer, profit withdrawal, payment release, mortgage deposit, bank guarantee cancellation
* Assess project solvency before certifying a release
* Upload supporting documentation and forward to the RERA escrow department
* Certify that construction milestones justify the requested drawdown
* File periodic audited statements for each managed trust account
* Maintain the register of trust accounts under management

### Practical Example

A developer submits a request to draw down against a completed construction milestone. The request arrives in the Account Trustee's queue. The Trustee reviews the project's solvency position and the milestone evidence, uploads the supporting assessment, and certifies the request. It is forwarded to the RERA escrow department for final audit. On approval, the Trustee executes the transfer and the developer is notified.

### To Confirm

* Does the Account Trustee work from a dedicated queue in the RERA platform, or from the bank's own systems with only the outcome recorded here?
* Is milestone certification a document upload, or a structured assessment with defined fields?
* What is the SLA for a Trustee to act on a routed developer request?

---

## 4. Auditing Bureau Officer

**Player:** Approved auditor

### Purpose

Provides independent audit of developer escrow accounts and of the institution's own submitted transactions.

> **Proposed** — not in source material. Rationale: the user group structure states this role audits developer escrow accounts and submits independent compliance reports. Separately, the mortgage registration workflow includes a step where "the bank's internal auditor reviews and certifies the transaction" before it reaches RERA — an actor not mapped to any named role. This document proposes that step belongs to the Auditing Bureau Officer. Needs client confirmation.

### Responsibilities

* Certify transactions submitted by the Mortgage Officer before they are routed to the RERA audit queue
* Audit developer escrow accounts under the institution's trusteeship
* Prepare and submit independent compliance reports to RERA
* Flag irregularities in escrow movement for regulatory attention
* Maintain an audit history for each account and transaction reviewed

### Practical Example

A batch of mortgage registrations awaits internal certification. The Auditing Bureau Officer reviews each against the attached documentation, certifies those that are complete and returns one with a query for a missing valuation report. Certified transactions proceed automatically to the RERA Transaction Audit queue.

### To Confirm

* Is the "bank's internal auditor" in the mortgage workflow the same person as the Auditing Bureau Officer, or a separate unnamed role?
* Is transaction certification per-transaction or batch-level?
* Do compliance reports follow a RERA-defined template?

---

## How They Work Together

| Stage | Role | Action |
| :---- | :---- | :---- |
| 1 | Mortgage Officer | Enters the transaction and attaches documentation |
| 2 | Auditing Bureau Officer | Certifies the transaction internally |
| 3 | — | Routed to the RERA Transaction Audit queue |
| 4 | Compliance & Escrow Auditor (Group A) | Approves, queries or rejects |
| 5 | — | Fees settled; output document issued |
| 6 | Institution Relationship Manager | Retains oversight of institution-wide outcomes |

For escrow work originating with developers, the Account Trustee replaces stages 1–2: the request arrives from Group B, the Trustee assesses and certifies, and it proceeds to the same RERA audit gate.

**The two-gate pattern.** Every Group C action passes through an internal certification gate inside the institution and then an external audit gate at RERA. No Group C role can complete a regulated action unilaterally. This is the defining structural characteristic of the module and should be reflected in every service flow and screen.

---

## To Confirm — Summary

1. Account Trustee interface: dedicated platform queue or external system with recorded outcome?
2. Milestone certification: document upload or structured assessment?
3. SLA for Trustee action on routed developer requests
4. Is the bank's internal auditor the Auditing Bureau Officer?
5. Transaction certification: per-transaction or batch?
6. Compliance report template — RERA-defined or institution's own?
7. Does the Institution Relationship Manager get an institution-wide oversight dashboard?
