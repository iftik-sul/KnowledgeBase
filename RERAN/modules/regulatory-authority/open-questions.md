---
project: RERAN
module: regulatory-authority
type: open-questions
status: draft
updated: 2026-09-12
---

# Group A — Open Questions

Decisions this module is waiting on. Each carries a proposed position or, where
noted, a resolution. Nothing downstream (UI, service-flows) should be built on the
proposed items until they are confirmed.

## A1 — Unconfirmed role assignments (proposed)

Some services do not name a Group A role in their source; the assignment was proposed
by module pattern. These are marked `[proposed]` throughout the touchpoint register.

- **12 Individual User services** name only "RERAN" with no role. Proposed:
  complaint (#38) → Dispute Adjudication Officer; the rest → Compliance & Escrow
  Auditor.
- **A few RESC services** (#6, #11, #15, #17, #23) were assigned by pattern where the
  source workflow was thin.

**Proposed position:** proceed with the proposed assignments as documented, confirm
in a survey-first pass before they are treated as fact.

## A2 — Authority-label drift

Three authority labels used in existing service-flow files are not among Group A's 8
sourced roles:

- **"Survey Department"** (4 RED services) — this is AGIS vocabulary. Proposed:
  internal boundary confirmation → Inspection & Enforcement Officer; external
  Surveyor-General verification → State Liaison Coordinator.
- **"Registrar"** (RED #13, account-opening step) — proposed → System Super
  Administrator.
- **"Trusts Department"** (FTI #13, heirs' distribution) — proposed → Revenue &
  Finance Officer.

**Status: open.** Fixing the source service-flow labels is a separate correction
pass, not part of this module's foundation.

## A3 — Escrow sub-system: one queue or two? *(resolved 2026-09-12)*

The Compliance & Escrow Auditor's 92 services split into 79 general transaction
audits and 13 escrow / trust-account operations (verified against source).

**Resolved:** one service, not two. The decision loop is identical, so transaction
and escrow are modelled as a single Group A service (A-1 in services-overview.md)
with escrow handled as a documented variant — it arrives through the FTI Account
Trustee pre-gate, shows escrow-account context, and carries a heavier review
checklist. The UI gives escrow its own queue-view and checklist within the one
service. Splitting was rejected to avoid duplicating a service-flow that starts
identical (the drift risk); it can still be split later if escrow proves to need a
genuinely separate workflow.

## A4 — AGIS: design reference or live integration?

The client supplied the AGIS (Abuja GIS) documentation "for Group A." AGIS is the
FCT's real land-registry agency. It models Group A's land / title / survey / deeds /
licensing functions well but has **no escrow function at all** — so it cannot inform
the 92-service Compliance & Escrow Auditor core.

**Question:** is AGIS a *design reference* for Group A's land-side sub-systems, or a
*live system* Group A must integrate with (via the State Liaison Coordinator, which
is defined as syncing C-of-O data with state bureaus)? The two imply very different
work. **Status: open** — the largest external unknown for this module.

## A5 — Non-transactional roles: RBAC scope in Phase 1

Five of the eight roles (Director-General, System Super Administrator, Revenue &
Finance, Inspection & Enforcement, State Liaison) are not exercised by any current
service.

**Proposed position:** define all eight roles in RBAC (so the permission model and
MFA are complete), but build functional screens only for the three approval roles
plus System Super Administrator, with Revenue & Finance getting a configuration
surface and the last two roles deferred until services exist that use them.
**Status: open** — a client scope confirmation.
