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
  - "RERAN/modules/regulatory-authority/roles-and-actions-analysis.md"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - latent
  - governance
---

# Group A Service A-10 — Executive Sign-off / Revocation

> **LATENT SERVICE.** No routine front-office service routes to A-10; it is an
> escalation/sign-off tier the Director-General acts on for the exceptional and the
> final, not the routine. Functional build is deferrable (open-questions A5). Structured
> sketch, not build-ready.

## 1. Service Overview

**Executive Sign-off / Revocation** is the governance service: the Director-General
approves policy, signs statutory instruments, and authorises the serious, final actions
that lower tiers escalate — licence revocations and final enforcement.

## 2. Purpose

Provide a single, accountable executive tier for the actions that must not be taken at
first-line level — so revocations, final enforcement, and statutory instruments carry
explicit executive authority and are recorded.

## 3. Description

A matter is escalated to the Director-General (e.g. a proposed revocation from A-2, or a
final enforcement action from A-8). The DG reviews the escalation and the underlying
recommendation, then signs off (authorise) or declines. The signed instrument or
revocation is recorded and returned to the originating service to execute.

## 4. Who Can Act

**Director-General / Registrar** (Group A), under RBAC + MFA. The most privileged and
least-frequently-used action surface in Group A.

## 5. Trigger

Escalation from another Group A service (revocation, final enforcement), or a policy /
statutory-instrument action initiated by the DG. No applicant queue.

## 6. What the DG Works With

- The escalated matter and the lower tier's recommendation.
- The underlying case/record (from A-2, A-8, etc.).
- The policy / statutory context.

## 7. Task Checklist

- The escalation is complete and carries a clear recommendation.
- The action is within the DG's authority and warranted.
- The decision and its basis are recorded.

## 8. Service Fee / 9. Payment Required

**N/A.**

## 10. Authority & Access Control

- **Role:** Director-General / Registrar (Group A).
- **Access control:** RBAC + MFA.
- **Sub-system:** Governance (spans Admin & Configuration and the enforcement layer).

## 11. Expected Processing Time

N/A — exceptional, not a timed application.

## 12. Processing Workflow

```
Matter escalated to DG  (from A-2 revocation / A-8 final enforcement / policy action)
        ↓
Review escalation + recommendation + underlying record
        ↓
Sign off (authorise)  /  Decline
        ↓
Record signed instrument / revocation
        ↓
Return to originating service to execute
        ↓
Write to the audit trail
```

## 13. Status

An escalation is **Pending Sign-off**, **Authorised**, or **Declined**.

## 14. Possible Outcomes

- **Authorised** — the revocation / instrument / final action is signed and returned to
  execute.
- **Declined** — sent back to the originating tier with reasons.

## 15. Cross-Module Dependencies

- **A-2** (licence revocations escalate here), **A-8** (final enforcement escalates
  here). A-10 is the sign-off other services defer to, not a first-line queue.

## 16. Related Services

- **A-2**, **A-8** (escalation sources), **A-6** (RBAC).

## 17. UI Screens

- **Sign-off queue** — matters pending executive authorisation.
- **Sign-off view** — the escalation, recommendation, and record; authorise/decline with
  reasons.

## 18. API Requirements

- Fetch pending sign-offs
- Fetch escalated matter + recommendation
- Authorise / decline with reasons
- Record signed instrument / revocation; return to originating service
- Write audit-log entry

## 19. Database Entities

- Sign-off / Escalation *(matter, recommendation, status)*
- Signed Instrument / Revocation Record
- Staff User + Role + Permission *(RBAC)*
- Audit Log

## 20. Acceptance Criteria

- Only the Director-General / Registrar with MFA can authorise a sign-off.
- Revocations and final enforcement cannot execute without DG authorisation.
- Declines return to the originating tier with recorded reasons.
- Every authorisation and decline is written to the audit trail.

## 21. Business Rules

1. Access is role-gated (Director-General / Registrar) + MFA.
2. Serious/final actions (revocation, final enforcement) require DG authorisation before
   execution.
3. Every authorisation and decline is recorded in the audit trail with reasons.
4. **Latent** — functional build deferred until exercised (A5).
