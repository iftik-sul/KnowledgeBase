---
project: RERAN
module: regulatory-authority
type: open-questions
status: draft
updated: 2026-09-17
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

## A4 — AGIS: design reference or live integration? *(resolved 2026-09-17)*

The client supplied the AGIS (Abuja GIS) documentation "for Group A." AGIS is the
FCT's real land-registry agency. It models Group A's land / title / survey / deeds /
licensing functions well but has **no escrow function at all** — so it cannot inform
the 92-service Compliance & Escrow Auditor core.

**Resolved: AGIS is a design reference, not a live integration target.** RERAN does
not connect to AGIS systems; there is no data contract, no sync API, and no
dependency on AGIS uptime or schema.

Consequences:

- **A-9 Harmonise Land Records is no longer blocked**, but its nature changes: the
  State Liaison Coordinator performs **periodic manual reconciliation** — comparing
  platform records against bureau records obtained out-of-band — rather than
  operating a system-to-system sync. Its screens should be specced on that basis.
- **Scope reduction:** no integration build, no AGIS schema mapping, no
  authentication/credentials with a third-party system, and no failure modes from an
  external dependency.
- **AGIS remains useful as source material** for the land-side service and screen
  design (titles, deeds, C-of-O, survey), per the AGIS ↔ Group A crosswalk — but it
  informs *how the work is modelled*, never *what the platform connects to*.
- The bureau remains the authoritative source for state-held data; the platform
  records what reconciliation found, not a live mirror.

## A5 — Non-transactional roles: RBAC scope in Phase 1

Five of the eight roles (Director-General, System Super Administrator, Revenue &
Finance, Inspection & Enforcement, State Liaison) are not exercised by any current
service.

**Proposed position:** define all eight roles in RBAC (so the permission model and
MFA are complete), but build functional screens only for the three approval roles
plus System Super Administrator, with Revenue & Finance getting a configuration
surface and the last two roles deferred until services exist that use them.
**Status: open** — a client scope confirmation.

## A6 — Group A back-office operating decisions *(added 2026-09-17)*

Surfaced by walking the Compliance & Escrow Auditor journey
(`ui/flows/compliance-escrow-auditor.md`). Items marked ✅ are confirmed; the rest are
resolved with a working default so design is unblocked, but remain business decisions the
client should confirm.

- **SLA clock on returned items.** ✅ **Resolved 2026-09-17: the clock RESETS on
  resubmission** — a resubmitted item gets a fresh full window from the originating
  service's published processing time (not pause-and-resume, not continuous). Because a
  repeatedly-queried item could then accumulate long real elapsed time while always showing
  green, the queue also carries a non-resetting **Total elapsed** figure so overall delay
  stays visible for oversight.
- **Claim lapse period.** Default: a claim lapses after **30 minutes** of inactivity and
  the item returns to the pool.
- **Supervisory review tier.** ✅ **Resolved 2026-09-17: none — one auditor's decision is
  final.** An approval issues its output directly; no senior countersignature exists. The
  eight-role model stands, with no senior/junior auditor tier, so an officer who cannot
  decide an item **releases** it rather than escalating. No pending-approval state, no
  second-approver queue.
- **Work allocation.** Default: the 92-service queue is a **shared pool** (claim-on-open),
  unlike A-3 dispute cases which are assigned. Confirm RERA does not allocate audit work
  to named officers.
- **Notification delivery.** Default: **in-app only.** Confirm whether SLA breaches and DG
  escalations also warrant email/SMS.
- **Step-up authentication.** Proposed for the five widest-consequence actions
  (modals.md §9). Trades friction for safety.
