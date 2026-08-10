---
project: RERAN
module: financial-trust-institutions
type: user-group
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
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
| Auditing Bureau Officer | Approved auditor | 0 — see below | Trust-Account Approval & Renewal |

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

Provides independent audit of developer escrow accounts under the institution's trusteeship, and submits independent compliance reports to RERA. This role does **not** perform the institution's own internal certification of Mortgage Officer filings — see the correction below.

> **Corrected per `open-questions.md` A1.** Earlier versions of this document proposed that the mortgage registration workflow's "bank's internal auditor reviews and certifies the transaction" step belonged to this role. Answer A1 supersedes that: internal certification is a `certify` **permission scope**, held by any delegated staff member the Institution Relationship Manager provisions under registration Flow 5 — not a fifth capability bolted onto this role, and not a duty this role performs by virtue of its title. The user group structure's own description of this role — auditing developer escrow accounts and submitting independent compliance reports — was the accurate source all along; the certification duty below has been removed to match it. **Confidence: High**, per the answers doc. Screen-level detail for the corrected role is in [ui/screens/compliance-reports.md](ui/screens/compliance-reports.md) and [ui/screens/trust-accounts.md](ui/screens/trust-accounts.md).

### Responsibilities

* Audit developer escrow accounts and trust accounts under the institution's trusteeship
* Prepare and submit independent compliance reports to RERA, on a RERA-defined template (per answer A7)
* Raise findings against trust accounts, escalating material findings for regulatory attention
* Maintain an audit history for each trust account and compliance report reviewed
* Open and close audit engagements against trust accounts under examination

### Practical Example

A trust account's periodic statement shows a movement the Auditing Bureau Officer cannot reconcile against the certified milestones on file. The Officer opens an audit engagement against the account, raises a finding categorised as a balance discrepancy, and — because the discrepancy is material — escalates it for RERA's attention as part of the next compliance report. The finding sets the trust account to Flagged until resolved.

### To Confirm

* **Resolved by A1** — whether the "bank's internal auditor" in the mortgage workflow is this role: no. It is the `certify` permission scope, held by whichever delegated staff member the institution assigns it to. This is no longer an open question about this role.
* **Resolved by A1** — whether certification is per-transaction or batch-level: moot for this role, since certification is not this role's responsibility. The certify scope's own certification cadence is addressed in [ui/screens/internal-certification-queue.md](ui/screens/internal-certification-queue.md), which documents it as per-record, with no bulk action, for the same reasoning answer A3 applies to milestone certification.
* Do compliance reports follow a RERA-defined template? **Proposed answered** by A7 (Medium confidence) — RERA-defined template, structured with a free-text findings narrative. The exact structure and reporting cycle remain undetermined; see [ui/screens/compliance-reports.md](ui/screens/compliance-reports.md#notes).

---

## How They Work Together

| Stage | Role / Scope | Action |
| :---- | :---- | :---- |
| 1 | Mortgage Officer | Enters the transaction and attaches documentation |
| 2 | `certify` permission scope *(corrected — was "Auditing Bureau Officer")* | Certifies the transaction internally, where the institution has configured this gate for the service |
| 3 | — | Routed to the RERA Transaction Audit queue |
| 4 | Compliance & Escrow Auditor (Group A) | Approves, queries or rejects |
| 5 | — | Fees settled; output document issued |
| 6 | Institution Relationship Manager | Retains oversight of institution-wide outcomes |

Stage 2 is corrected per answer A1: certification is held by any delegated staff member with the `certify` scope, which the Auditing Bureau Officer may or may not hold — it is not attached to that role by title. See the Auditing Bureau Officer section above for the full correction.

For escrow work originating with developers, the Account Trustee replaces stages 1–2: the request arrives from Group B, the Trustee assesses and certifies, and it proceeds to the same RERA audit gate.

**The two-gate pattern — sourced for the mortgage and finance-lease lifecycle, not proven universal.** Services #3–#7 source an explicit internal "bank auditor" step before RERA review. The remaining Group C services do not carry the same explicit language in the master service table, and the module's service-flow documents (see `service-flows/`) do not assert a `certify` gate for them by default — each states, service by service, whether the gate is sourced, configurable, or simply not addressed. Treat "every Group C action passes through both gates" as the working design intent for services where the institution enables it, not as a sourced fact for all eighteen. This paragraph previously stated the pattern as unconditional; that overstated what rows 28–45 actually support, and the correction is carried into every screen this document informs — see [ui/README.md](ui/README.md#structural-characteristic).

---

## To Confirm — Summary

Seven items originally listed here; four survive as genuinely open, three are resolved by the answers doc and kept below with pointers rather than dropped.

**Still open:**

1. Account Trustee interface: dedicated platform queue or external system with recorded outcome? **Resolved by A2** — dedicated platform queue, sourced from rows 8–12. See [ui/screens/escrow-request-queue.md](ui/screens/escrow-request-queue.md).
2. Milestone certification: document upload or structured assessment? **Resolved by A3** — structured assessment. See [ui/screens/escrow-request-details.md](ui/screens/escrow-request-details.md#section-4--milestone-certification).
3. **SLA for Trustee action on routed developer requests — still open.** Answer A6 proposes reading the source's split SLA figures as queue-time versus RERA-processing-time, which would supply this, but flags that reading as an inference needing explicit client confirmation. Not resolved.
6. Compliance report template — RERA-defined or institution's own? **Proposed answered by A7** (Medium confidence) — RERA-defined. Structure and cycle remain open; see [ui/screens/compliance-reports.md](ui/screens/compliance-reports.md#notes).
7. **Does the Institution Relationship Manager get an institution-wide oversight dashboard? — still open in the general sense**, though a proposed answer now exists in the form of a specific screen: [ui/screens/dashboard.md](ui/screens/dashboard.md#institution-relationship-manager) and [ui/screens/institution-profile.md](ui/screens/institution-profile.md) implement one. Whether this is the *right* dashboard remains for the client to confirm; that it should exist is answer A5's High-confidence position.

**Resolved, kept for record:**

4. ~~Is the bank's internal auditor the Auditing Bureau Officer?~~ **Resolved by A1** — no. It is the `certify` permission scope, held by any delegated staff member, not this or any other named role.
5. ~~Transaction certification: per-transaction or batch?~~ **Moot per A1** — this was a question about the Auditing Bureau Officer's certification cadence; the role does not certify. The certify scope's own cadence is per-record, with no bulk action (see [ui/screens/internal-certification-queue.md](ui/screens/internal-certification-queue.md)).
