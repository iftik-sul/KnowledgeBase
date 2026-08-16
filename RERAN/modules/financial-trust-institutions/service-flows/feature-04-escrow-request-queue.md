---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-queue.md"
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-03-mortgage-registration.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-08-activate-escrow-account.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-10-withdraw-project-profit.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - escrow
---

# Feature #4 – Escrow Request Queue

**Feature Category:** Shared Platform Features – Institution-Specific

## 1. Feature Overview

The **Escrow Request Queue** is the institution-side counterpart to Group B's developer escrow services: a single queue of every developer-originated escrow request (account activation, account transfer, profit withdrawal, payment release, mortgage deposit, bank guarantee cancellation) awaiting the institution's assessment, before it is forwarded to RERA's escrow department for final audit.

> **Cross-module status vocabulary — corrected 2026-08-16, superseding an earlier same-day resolution.** A first pass renamed this feature's statuses to `Pending Approval → Under Review → Approved → Released`, taken from a real-estate-developer UI screen's filter values. That was wrong on both sides: neither term traces to source. **All six individual escrow service files on the developer side** (Services #8, #9, #10, #12, #20, #21 — verified directly, all six) use `Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → [service-specific terminal state]`, with additional statuses `Information Requested / Returned / Rejected`. That is now the corrected canonical vocabulary. `Trustee Review` is this feature's own assessment stage — the institution's Certify action is what advances a request out of `Trustee Review` into `RERA Escrow Audit`, not into an ambiguous shared "Under Review." See Section 13.

> **Terminology clarified 2026-08-16.** "RERA's Escrow Department" / "RERA Escrow Audit" (this feature's second stage) is the **same role** this module already calls the **Compliance & Escrow Auditor** everywhere else — Service #3 (Mortgage Registration) and every other two-gate FTI service names this exact role as the second, RERA-side gate. Confirmed against `RERAN_service_flows_v2.md`'s master Service Workflows table: real-estate-developer's six escrow rows (8–12, 20–21) and this module's mortgage/lease rows (30–39) carry the identical Regulator/Approver-column value **"Compliance & Escrow Auditor."** This feature was the one place in either module still calling that role by its Workflow-column narrative name ("escrow department") rather than its Groups & Roles name — now cross-linked rather than left as an unlabeled synonym. See Real Estate Developer's `feature-04-escrow-management.md` for the full source citation.

## 2. Purpose

Give the institution one place to triage and assess the six types of developer escrow requests, typically worked by the Account Trustee but reachable by any of the institution's four Group C roles, before RERA's own audit.

## 3. Description

Requests arrive from Group B's escrow services (Real Estate Developer module Services #8–#12, #20–#21) already at the `Trustee Review` stage — the developer-side `Draft` and `Submitted` stages happen before a request reaches this queue at all. Any institution user assesses a request — checking requested amount against the trust account's available balance, reviewing the cited construction milestone where applicable — and either **certifies** it (advancing the request to `RERA Escrow Audit`) or returns it to the developer, or requests further information. Certification is a structured assessment with a solvency judgement inside it (per `open-questions.md` A3), not a document upload, so there is no bulk-certify action — the same reasoning applied to the Internal Certification Queue.

## 4. Used By

Not one of the 18 numbered Group C services — this is the institution's side of Real Estate Developer's escrow services:

* Escrow Account Activation, Escrow Account Transfer
* Project Profit Withdrawal, Receive Payment from Escrow Account
* Depositing a Mortgage into an Escrow Account
* Bank Guarantee Cancellation

## 5. Prerequisites

* User is logged into a verified institution account.
* At least one escrow request has arrived from a developer, already at `Trustee Review`.
* The request's trust account is not Suspended or Flagged (both block certification).

## 6. Required Information

Search/filter by: Request ID · Project · Project registration number · Developer · Trust account number · Request type · Status · SLA state (Within window / Approaching breach / Breached).

## 7. Required Documents

Uploaded assessment documentation, attached by the assessing user before certifying or returning. Download Request Pack retrieves whatever the developer originally submitted.

## 8. Service Fee

Not sourced as a fee-bearing action for the institution — this is an assessment step, not a chargeable Group C service. Consistent with all six underlying developer services, none of which sources a payment step at any point.

## 9. Payment Required

**No**, for the assessment itself, and confirmed **no** for any of the six underlying developer services at any point in their own sourced workflows.

## 10. Processing Authority

**Any of the institution's four Group C roles**, unrestricted, for the `Trustee Review` stage; the **Compliance & Escrow Auditor** (Group A) — this module's standard second-gate regulator, used identically across all 18 numbered Group C services — for the subsequent `RERA Escrow Audit` that a Certify action advances a request into. Not a separate "escrow department"; see the terminology note under Feature Overview. **Corrected 2026-08-15**: previously gated by an `escrow` permission scope held by the Account Trustee; the scope is retired. Typically worked by the Account Trustee in practice — not a restriction.

## 11. Expected Processing Time

**Sourced.** Answer A6 (confirmed 2026-08-15) reads the source's split SLA — "waiting time 20 business hours; service delivery 13 business hours" — as the institution's own window (waiting time, covering `Trustee Review`) versus RERA's subsequent processing time (service delivery, covering `RERA Escrow Audit`). The SLA countdown on this queue is built against the waiting-time figure.

## 12. Processing Workflow

Dashboard
↓
Open Escrow Requests
↓
Search / Filter / Sort (default: SLA urgency)
↓
Assess a Request (status: Trustee Review)
↓
Review Requested Amount vs. Trust Account Balance, Milestone Evidence
↓
Certify (advances to RERA Escrow Audit, performed by the Compliance & Escrow Auditor) **or** Return (to developer) **or** Request Information
↓
Record Removed from Active Queue on Certify/Return; Remains, Updated, on Information Request
↓
*(after Certify)* Compliance & Escrow Auditor Audits → Approved → *(service-specific terminal state)*

## 13. Application Status Flow

**Corrected 2026-08-16.** Sourced directly from all six individual developer service files (#8, #9, #10, #12, #20, #21), not from either module's own UI filter values:

*(Developer-side, before this queue)* Draft → Submitted
↓
Trustee Review *(this feature's own assessment stage)*
↓
*(Certify action taken)*
↓
RERA Escrow Audit *(performed by the Compliance & Escrow Auditor — see the terminology note under Feature Overview)*
↓
Approved
↓
*Service-specific terminal state:*

| Request type | Terminal state |
| :---- | :---- |
| Escrow Account Activation (#8) | Active |
| Escrow Account Transfer (#9) | Transferred |
| Project Profit Withdrawal (#10) | Released |
| Receive Payment from Escrow Account (#12) | Released |
| Depositing a Mortgage into Escrow (#20) | Deposited |
| Bank Guarantee Cancellation (#21) | Cancelled |

Additional statuses (all six): Information Requested, Returned, Rejected — either during `Trustee Review` or `RERA Escrow Audit`.

SLA state (Within window / Approaching breach / Breached) tracks alongside status, not as a replacement for it, and applies to this feature's own `Trustee Review` window only.

**Superseded by this correction**: the previous vocabulary (`Awaiting Assessment / Under Assessment / Certified` in the original version of this document, and `Pending Approval / Under Review / Approved / Released` in the first same-day correction). Neither traced to the sourced service files. This also fully closes the original gap this document flagged: RERA's post-certification review is now an explicit named stage (`RERA Escrow Audit`), not folded into an ambiguous continuation of an institution-side status.

## 14. Possible Outcomes

* Request Approved and reaches its terminal state (Active / Transferred / Released / Deposited / Cancelled, per type)
* Request Returned to Developer
* Information Requested from Developer
* SLA Breached *(visibility only — does not block action, and applies only to the `Trustee Review` window)*

## 15. Output

* Certification decision, recorded with the acting user, their role, and a timestamp
* On Certify: request advances to `RERA Escrow Audit`
* On RERA's decision: status updates to `Approved`, then its service-specific terminal state
* Remains visible under a filtered view for the institution's own record after leaving the active `Trustee Review` queue

## 16. Related Features

* Trust Accounts *(the account a request draws against — View Trust Account row action)*
* Internal Certification Queue *(a structurally similar certify/return gate, for Services #3–#11 instead)*
* Compliance Reports *(findings may reference escrow activity on a covered account)*
* Real Estate Developer's Escrow Management and Fund Release Request *(cross-module — the developer's side of the same six request types; **status vocabulary corrected 2026-08-16, and the RERA-side approver confirmed to be the same Compliance & Escrow Auditor role in both modules**, see Feature Overview)*

## 17. UI Screens

* Escrow Requests (queue)
* Escrow Request Details (assessment)

## 18. API Requirements

* Retrieve Institution Escrow Request Queue
* Retrieve Request Details
* Retrieve Trust Account Balance
* Submit Assessment / Certification Decision
* Request Information from Developer
* Update Request Status (through RERA's subsequent Approved/terminal-state transitions)
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Institution, Institution Staff, User
* Escrow Request, Trust Account
* Certification Record
* Notification, Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can assess, certify, return, or request information on any escrow request institution-wide.
* Requested amount is checked against the trust account's available balance before certification.
* A request against a Suspended or Flagged trust account cannot be certified.
* A request cannot be certified by the same user who last returned it to the developer (return-cycle rule, unaffected by the unified-access correction).
* No bulk certification exists.
* Status vocabulary matches the sourced individual service files, not either module's own UI filter values.
* All assessment activity is recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Requests originate in the Real Estate Developer module; this feature never creates one, and never sees the developer-side `Draft`/`Submitted` stages.
2. Any of the institution's four Group C roles may assess and certify a request — not restricted to the Account Trustee by title.
3. A request cannot be certified by the user who last returned it to the developer, preserving a second pair of eyes across the return cycle — this rule stands independently of the retired scope model.
4. A Suspended or Flagged trust account blocks certification against it.
5. Certification is a structured, per-request assessment; there is no bulk-certify action.
6. Certify is an action that advances a request from `Trustee Review` to `RERA Escrow Audit` — not a terminal status.
7. The terminal state after `Approved` is service-specific (Active / Transferred / Released / Deposited / Cancelled), not a single uniform word.
8. `RERA Escrow Audit` is performed by the same Compliance & Escrow Auditor role that approves all 18 numbered Group C services — not a separate escrow department, confirmed against the master source table.
9. Every assessment, certification, and return is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
