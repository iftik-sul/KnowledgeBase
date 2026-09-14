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
  - enforcement
---

# Group A Service A-8 — Issue Enforcement Notice

> **LATENT SERVICE.** No current front-office service routes to A-8; enforcement is
> proactive, initiated by RERA rather than triggered by an applicant filing. Functional
> build is deferrable (open-questions A5). Structured sketch, not build-ready.

## 1. Service Overview

**Issue Enforcement Notice** is how RERA acts on a detected violation: it issues
stop-work or violation notices and escalates penalties. It is Group A initiating action
against an entity, not responding to a filing.

## 2. Purpose

Give RERA a recorded, escalable enforcement instrument — so violations (e.g. found via
inspection or monitoring) result in a formal, tracked notice rather than an ad-hoc one.

## 3. Description

An Inspection & Enforcement Officer, on detecting a violation (often via a failed A-7
inspection or compliance monitoring), assesses it, issues the appropriate notice
(stop-work or violation), and escalates to a penalty where warranted. Final enforcement
actions may require DG sign-off (A-10).

## 4. Who Can Act

**Inspection & Enforcement Officer** (Group A), under RBAC + MFA. Final/serious actions
escalate to **A-10 (Director-General sign-off)**.

## 5. Trigger

Proactive — a violation is detected (failed inspection, monitoring, or report). No
applicant queue.

## 6. What the Officer Works With

- The violation details and the entity concerned.
- Related inspection reports (A-7) and registry records.
- The enforcement/penalty schedule.

## 7. Task Checklist

- The violation is evidenced.
- The correct notice type and penalty tier are selected.
- Escalation to A-10 is applied where the action requires it.

> **Proposed** — enforcement categories, notice types, and penalty tiers are not
> detailed in current source.

## 8. Service Fee / 9. Payment Required

**N/A** (penalties are collected via the finance flow, not charged here).

## 10. Authority & Access Control

- **Role:** Inspection & Enforcement Officer (Group A); DG for final actions (A-10).
- **Access control:** RBAC + MFA.
- **Sub-system:** Inspection & Enforcement Module.

## 11. Expected Processing Time

N/A — proactive; not a timed application.

## 12. Processing Workflow

```
Violation detected  (failed A-7 inspection / monitoring / report)
        ↓
Assess violation + evidence
        ↓
Select notice type (stop-work / violation) + penalty tier
        ↓
[If final/serious] Escalate to A-10 (DG sign-off)
        ↓
Issue notice to the entity
        ↓
Escalate penalty where warranted  → finance (A-5) for collection
        ↓
Write to the audit trail
```

## 13. Status

A notice is **Draft**, **Issued**, **Escalated**, or **Resolved**.

## 14. Possible Outcomes

- **Notice issued** — the entity is formally notified.
- **Penalty escalated** — referred for collection.
- **Resolved** — the violation is remedied and the notice closed.

## 15. Cross-Module Dependencies

- **A-7** commonly precedes it (failed inspection).
- **A-10** for final/serious actions (DG sign-off).
- **A-5** for penalty collection.

## 16. Related Services

- **A-7** (upstream), **A-10** (sign-off), **A-5** (collection), **A-6** (RBAC).

## 17. UI Screens

- **Enforcement queue** — open violations and notices.
- **Notice editor** — assess, select type/tier, issue, escalate.

## 18. API Requirements

- Create / issue enforcement notice
- Escalate to DG sign-off (A-10)
- Escalate penalty to finance (A-5)
- Update notice status
- Write audit-log entry

## 19. Database Entities

- Enforcement Notice *(type, tier, status)*
- Violation *(details, evidence)*
- Entity *(the party notified)*
- Staff User + Role + Permission *(RBAC)*
- Audit Log

## 20. Acceptance Criteria

- Only an Inspection & Enforcement Officer with MFA can issue notices.
- Serious/final actions require DG sign-off before issue.
- Penalties are escalated to the finance flow, not collected here.
- Every notice and escalation is recorded in the audit trail.

## 21. Business Rules

1. Access is role-gated (Inspection & Enforcement Officer) + MFA.
2. Final/serious enforcement actions require DG sign-off (A-10).
3. Penalties settle through the finance flow (no collection here).
4. All actions are recorded in the audit trail with the acting officer.
5. **Latent** — functional build deferred until exercised (A5).
