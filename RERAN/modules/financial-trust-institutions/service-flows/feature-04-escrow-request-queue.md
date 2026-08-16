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
tags:
  - financial-trust-institutions
  - shared-feature
  - escrow
---

# Feature #4 – Escrow Request Queue

**Feature Category:** Shared Platform Features – Institution-Specific

## 1. Feature Overview

The **Escrow Request Queue** is the institution-side counterpart to Group B's developer escrow services: a single queue of every developer-originated escrow request (account activation, account transfer, profit withdrawal, payment release, mortgage deposit, bank guarantee cancellation) awaiting the institution's assessment and certification, ordered by SLA urgency, before it is forwarded to RERA's escrow department.

> **Cross-module status mismatch, found 2026-08-16, not resolved.** This feature treats all six request types as one queue with one status vocabulary (Section 13). The real-estate-developer module's own docs for the same transactions — [`feature-04-escrow-management.md`](../../real-estate-developer/service-flows/feature-04-escrow-management.md) for #8/9/20/21, [`feature-05-fund-release-request.md`](../../real-estate-developer/service-flows/feature-05-fund-release-request.md) for #10/12 — split across two features with two different, non-matching vocabularies (`Pending Approval → Under Review → Approved → Released`, and a separate 9-stage `Draft → ... → Under Bank Review → Under RERA Review → Funds Released` tracker respectively). Neither developer-side term appears here. **Separately, this feature's own Section 13 has a gap**: it treats `Certified` as the end state, but this section's own prose says a certified request is then "forwarded to RERA's escrow department for final audit" — no status represents that subsequent RERA review, even though the developer side's `Under RERA Review` (Feature #5) shows exactly that stage exists. Not silently reconciled here — flagged in both modules' overview docs pending a decision on which vocabulary (if either, as-is) should be authoritative.

## 2. Purpose

Give the institution one place to triage, assess, and certify or return the six types of developer escrow requests, typically worked by the Account Trustee but reachable by any of the institution's four Group C roles.

## 3. Description

Requests arrive from Group B's escrow services (Real Estate Developer module Services #8–#12, #20–#21) rather than originating inside this module. Any institution user assesses a request — checking requested amount against the trust account's available balance, reviewing the cited construction milestone where applicable — and either certifies it (forwarding to RERA's escrow department) or returns it to the developer, or requests further information. Certification is a structured assessment with a solvency judgement inside it (per `open-questions.md` A3), not a document upload, so there is no bulk-certify action — the same reasoning applied to the Internal Certification Queue.

## 4. Used By

Not one of the 18 numbered Group C services — this is the institution's side of Real Estate Developer's escrow services:

* Escrow Account Activation, Escrow Account Transfer
* Project Profit Withdrawal, Receive Payment from Escrow Account
* Depositing a Mortgage into an Escrow Account
* Bank Guarantee Cancellation

## 5. Prerequisites

* User is logged into a verified institution account.
* At least one escrow request has arrived from a developer.
* The request's trust account is not Suspended or Flagged (both block certification).

## 6. Required Information

Search/filter by: Request ID · Project · Project registration number · Developer · Trust account number · Request type · Status · SLA state (Within window / Approaching breach / Breached).

## 7. Required Documents

Uploaded assessment documentation, attached by the assessing user before certifying or returning. Download Request Pack retrieves whatever the developer originally submitted.

## 8. Service Fee

Not sourced as a fee-bearing action for the institution — this is an assessment step, not a chargeable Group C service.

## 9. Payment Required

**No**, for the assessment itself. Where the underlying developer service disburses funds (e.g. Profit Withdrawal), that disbursement is the outcome of certification, not a payment collected here.

## 10. Processing Authority

**Any of the institution's four Group C roles**, unrestricted. **Corrected 2026-08-15**: previously gated by an `escrow` permission scope held by the Account Trustee; the scope is retired. Typically worked by the Account Trustee in practice — not a restriction.

## 11. Expected Processing Time

**Sourced.** Answer A6 (confirmed 2026-08-15) reads the source's split SLA — "waiting time 20 business hours; service delivery 13 business hours" — as the institution's own window (waiting time) versus RERA's subsequent processing time (service delivery). The SLA countdown on this queue is built against the waiting-time figure.

## 12. Processing Workflow

Dashboard
↓
Open Escrow Requests
↓
Search / Filter / Sort (default: SLA urgency)
↓
Assess a Request
↓
Review Requested Amount vs. Trust Account Balance, Milestone Evidence
↓
Certify (forwarded to RERA escrow department) **or** Return (to developer) **or** Request Information
↓
Record Removed from Queue on Certify/Return; Remains, Updated, on Information Request

## 13. Application Status Flow

Awaiting Assessment
↓
Under Assessment
↓
Information Requested *(back to developer, loop)*
↓
Certified → forwarded to RERA escrow department
↓
*or* Returned → back to developer

SLA state (Within window / Approaching breach / Breached) tracks alongside status, not as a replacement for it.

**Known gap, see the note under Feature Overview above**: no status here represents RERA's own subsequent review after `Certified` — the developer-side `Under RERA Review` stage (Feature #5) has no counterpart in this vocabulary.

## 14. Possible Outcomes

* Request Certified, Forwarded to RERA
* Request Returned to Developer
* Information Requested from Developer
* SLA Breached *(visibility only — does not block action)*

## 15. Output

* Certification or return decision, recorded with the acting user, their role, and a timestamp
* On Certify: routed to RERA's escrow department for final audit
* Remains visible under a Certified filter for the institution's own record after leaving the active queue

## 16. Related Features

* Trust Accounts *(the account a request draws against — View Trust Account row action)*
* Internal Certification Queue *(a structurally similar certify/return gate, for Services #3–#11 instead)*
* Compliance Reports *(findings may reference escrow activity on a covered account)*
* Real Estate Developer's Escrow Management and Fund Release Request *(cross-module — the developer's side of the same six request types; **status vocabulary does not currently reconcile**, see Feature Overview)*

## 17. UI Screens

* Escrow Requests (queue)
* Escrow Request Details (assessment)

## 18. API Requirements

* Retrieve Institution Escrow Request Queue
* Retrieve Request Details
* Retrieve Trust Account Balance
* Submit Assessment / Certification Decision
* Request Information from Developer
* Update Request Status
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
* All assessment activity is recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Requests originate in the Real Estate Developer module; this feature never creates one.
2. Any of the institution's four Group C roles may assess and certify a request — not restricted to the Account Trustee by title.
3. A request cannot be certified by the user who last returned it to the developer, preserving a second pair of eyes across the return cycle — this rule stands independently of the retired scope model.
4. A Suspended or Flagged trust account blocks certification against it.
5. Certification is a structured, per-request assessment; there is no bulk-certify action.
6. Every assessment, certification, and return is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. **Cross-module status vocabulary mismatch** (found 2026-08-16, detailed under Feature Overview) — needs a client or architecture decision on which side's vocabulary, if either as-is, should be authoritative, and needs this feature's own gap (no status for RERA's post-certification review) resolved regardless.
2. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
