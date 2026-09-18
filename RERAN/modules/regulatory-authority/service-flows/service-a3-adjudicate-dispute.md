---
project: RERAN
module: regulatory-authority
type: service-flow
status: draft
contains_proposals: true
source_type: derived
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/service-flows/service-a1-audit-and-decide.md"
  - "RERAN/modules/real-estate-service-companies/service-flows/ (services #25, #26)"
  - "RERAN/modules/individual-user/service-flows/ (services #26, #38)"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - tribunal
---

# Regulatory Authority Service A-3 — Adjudicate (Dispute)

> **Back-office service — the one that breaks the mould.** A-1 and A-2 are single
> approve/reject decisions. A-3 is a *multi-session case process*: file → assign →
> mediate/hear → judgment → close. Its Workflow (§12), Status Flow (§13), and Outcomes
> (§14) therefore differ from the A-1 template on purpose. All other conventions
> (RBAC + MFA, N/A fee/payment, audit trail) still hold.

## 1. Service Overview

**Adjudicate** is the Regulatory Authority's dispute-resolution service. It finishes the
**4 dispute services** — joint-property suits, execution cases, tenancy disputes, and
complaints — through the Tribunal & Remote-Litigation sub-system. A Dispute Adjudication
Officer receives a filing, runs it through mediation and/or a hearing (which may be
conducted remotely), and records a judgment. Unlike every other Regulatory Authority
service, resolving one item can take several sessions over time.

## 2. Purpose

Give RERA a structured, on-record forum to resolve conflicts between parties —
mediation and remote litigation with recorded judgments — so disputes have a
regulated path to resolution without a physical court appearance.

## 3. Description

A party files a suit, dispute, or complaint through the originating front-office
service. It arrives as a case in the Tribunal queue. A Dispute Adjudication Officer is
assigned, schedules mediation or a hearing, conducts one or more sessions (remotely
where applicable), may request further information or evidence between sessions, and
records a judgment. The case then closes with its outcome and any assignment recorded.

## 4. Who Can Act *(replaces "Who Can Apply")*

**Dispute Adjudication Officer** (RA), under real RBAC + MFA — the same
permission-gated model as A-1. Only a user holding this role may act on a case.

## 5. Entry Conditions *(replaces "Prerequisites")*

- An originating dispute/complaint service has been filed (and paid, where the
  originating service carries a fee — e.g. IU #38 complaint filing).
- The acting officer is authenticated (MFA) and holds the Dispute Adjudication Officer
  role.

## 6. What the Officer Works With *(replaces "What the Reviewer Sees")*

- The filing and the parties named in it.
- All submitted evidence and documents.
- Any related registry records (the property/ownership the dispute concerns).
- The case history — prior sessions, notes, and interim decisions.

## 7. Case Checklist *(replaces "Review Checklist")*

- The filing is complete and names the parties and the matter in dispute.
- The dispute falls within RERA's adjudication remit.
- Required evidence is present; further evidence can be requested between sessions.
- Sessions and their outcomes are recorded as they happen.

> **Proposed** — the adjudication procedure (mediation-before-hearing rules, session
> scheduling, judgment format) is not detailed in the current source; needs client
> confirmation against RERA's tribunal procedure.

## 8. Service Fee

**N/A (the Regulatory Authority side).** Any filing fee belongs to the originating
service (e.g. IU #38).

## 9. Payment Required

**N/A (the Regulatory Authority side).**

## 10. Decision Authority & Access Control *(replaces "Processing Authority")*

- **Role:** Dispute Adjudication Officer (RA).
- **Access control:** RBAC-gated + MFA.
- **Sub-system:** Tribunal & Remote-Litigation System.

## 11. Expected Processing Time

**Case-based, not a single SLA.** Adjudication spans multiple sessions and depends on
the matter; the originating services record only the registration/filing time, not the
resolution time. Measured per-case against RERA's tribunal service standards.

## 12. Processing Workflow *(multi-session — differs from A-1)*

```
Case filed  (from originating dispute service)
        ↓
Assign to Dispute Adjudication Officer
        ↓
Schedule mediation / hearing  ←────────────┐
        ↓                                   │
Conduct session (remote where applicable)   │  (repeat across
        ↓                                   │   multiple sessions)
Request further information / evidence  ─────┘
        ↓
Deliberate
        ↓
Record judgment
        ↓
Close case  (outcome + any assignment recorded)
        ↓
Write every session, decision, and actor to the audit trail
```

## 13. Case Status Flow *(differs from the shared four-state vocabulary)*

A case lifecycle, not the approve/reject loop:

```
Filed
   ↓
Assigned
   ↓
Scheduled  →  In Session  →  Information Requested → (back to Scheduled)
   ↓
Under Deliberation
   ↓
Judgment Recorded
   ↓
Closed
```
Terminal side-states: **Dismissed**, **Withdrawn**.

> **Dependency.** The originating dispute services (IU #26, #38; RESC #25, #26) have
> their own status vocabularies (e.g. IU #38's "Complaint Assigned → Investigation →
> Final Decision → Complaint Closed"). A-3's lifecycle must map cleanly onto each so
> the applicant's status display stays coherent. **Proposed** — the exact mapping needs
> confirming per originating service.

## 14. Possible Outcomes

- **Resolved** — a judgment is recorded and the case closes.
- **Partially Resolved** — some matters settled, others referred or continued.
- **Dismissed** — the case is closed without a substantive judgment.
- **Withdrawn** — the filing party withdraws.
- **Referred** — sent to another forum/authority beyond RERA's remit.

## 15. Service Variants *(back-office-specific section)*

The 4 services differ mainly in matter type, not workflow: joint-property suits (RESC
#25) and execution cases (RESC #26) are formal tribunal matters; tenancy disputes
(IU #26) and complaints (IU #38, proposed) are lighter but follow the same
file → session → judgment lifecycle. The complaint flow (IU #38) additionally has an
**investigation** phase before deliberation, which fits inside the "In Session /
Information Requested" loop.

## 16. Cross-Module Dependencies *(back-office-specific section)*

1. **Per-originating-service status mapping** (see §13) — the main dependency.
2. **Shared audit-trail and RBAC model** — as with all Regulatory Authority services.
3. No FTI handshake, no escrow two-gate, and no shared four-state decision vocabulary
   (A-3 is the exception on the last point).

## 17. Related Services

- **A-6 Provision & manage access (RBAC)** — must exist before this service can be used.
- **The 4 originating dispute services** — RESC #25, #26; IU #26, #38 (see
  touchpoint-register.md).

## 18. UI Screens

- **Case queue** — filed and in-progress cases, filterable by status and matter type.
- **Case workspace** — parties, evidence, session history, and interim notes in one
  view; the hub the officer works a case from.
- **Session / hearing view** — schedule and conduct a (remote) session; record its
  outcome.
- **Judgment record** — enter and finalise the judgment and any assignment.

## 19. API Requirements

- Fetch case queue (filtered)
- Fetch case detail (parties, evidence, history)
- Schedule session; record session outcome
- Request further information/evidence
- Record judgment + assignment
- Update case status; close case
- Notify parties
- Write audit-log entry (per session and decision)

## 20. Database Entities

- Case *(new — the dispute case record)*
- Party *(the disputing parties)*
- Session / Hearing *(new — scheduled and conducted sessions)*
- Evidence / Document
- Judgment *(new — outcome and assignment)*
- Staff User + Role + Permission *(RBAC)*
- Registry records *(read — the property/ownership in dispute)*
- Audit Log
- Notification

## 21. Acceptance Criteria

- Only a Dispute Adjudication Officer with MFA can act on a case.
- A case can move through multiple scheduled sessions before a judgment.
- Evidence and information can be requested between sessions.
- A judgment, once recorded, closes the case with a defined outcome.
- Dismissed and Withdrawn are available terminal states.
- Each originating service's applicant-facing status stays coherent with the case
  lifecycle (per the §13 mapping).
- Every session and decision, with its actor, is written to the audit trail.

## 22. Business Rules

1. Access is role-gated (Dispute Adjudication Officer) + MFA.
2. A case may not be closed without a recorded outcome (judgment, dismissal, or
   withdrawal).
3. Every session and interim decision is recorded and attributable.
4. The case lifecycle must map to each originating service's own status vocabulary.
5. All actions are permanently recorded in the audit trail with the acting officer.
