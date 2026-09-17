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

## A1 — Role assignments where the source named no officer *(resolved 2026-09-17)*

Twenty services did not name a Group A role in their source; each was assigned by
service pattern. **All twenty confirmed 2026-09-17.** The `[proposed]` tags have been
removed from the touchpoint register accordingly.

Breakdown — **12 Individual User + 8 Real Estate Service Companies**. (An earlier
version of this entry undercounted RESC as 5; it omitted #18, #21 and #22.)

The twenty fall into three kinds of assignment:

**No Group A officer required (9).** Confirmed that these need no decision at all:
IU #1 Verify Developer, #2 Verify Development Project, #3 Verify Property, #39 Track
Complaint (registry lookups); IU #30 Act on Behalf of Property Owner, #37 Remote
Property Transactions (wrappers — the selected service's officer decides); RESC #18
Register Evaluation Certificate, #21 Cancel Management Contract, #22 Register Tenancy
System User (immediate, no review).

**Compliance & Escrow Auditor (8).** IU #4 Register Property Ownership, #6 Register
Property Sale, #25 Manage Lease, #29 Register Power of Attorney, #36 Remote Identity
Verification; RESC #23 Permit to Sell by Public Auction; and on the escrow side RESC
#6 Close Escrow Account, #11 Approve/Renew Financial Auditing Company.

**Automatic approval, officer as system-of-record (2).** RESC #15 Renew Professional
Practice Card, #17 Amend Professional Practice Card — the system issues without manual
review; the Licensing & Registration Officer is recorded as the responsible role.

**Plus one unambiguous:** IU #38 Submit Complaint → Dispute Adjudication Officer.

> **Note for spec writers:** IU #36 Remote Identity Verification is the odd member of
> the Auditor group — every other item there is a property or money transaction, and
> this one is identity. It is correctly filed; the note exists so a later reader does
> not assume it is misplaced.

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

**Status: open — deliberately parked 2026-09-17.** Nothing currently being built
depends on it, and clearing it means editing other modules' service-flow files (RED,
FTI), so it is a separate correction pass. The Survey split across two roles is the
least certain of the three: if RERA has one person doing all survey checking, it
should map to one role, not two.

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

## A5 — Which non-transactional roles get screens *(resolved 2026-09-17)*

Three of the eight roles had no screens: Director-General / Registrar, Inspection &
Enforcement Officer, and State Liaison Coordinator.

**Resolved by dependency, not by completeness.** A role gets screens when an **active
service already escalates work into it**; it is deferred when nothing currently routes
to it. This replaces the earlier proposed position (defer all three), which would have
shipped a broken path.

**Build now (5 screens):**

- **Director-General / Registrar — 2 screens** (sign-off queue; sign-off detail).
  A-2 Licensing is active and already escalates revocations here (`M-LIC-04`). Without
  these screens that escalation dead-ends.
- **Inspection Officer — 3 screens** (inspection queue; on-site findings capture;
  inspection report). A-1 expects an inspection report for field-visit items (RED #27
  and the IU inspection-required services), and nothing can currently produce one.

**Deferred (4 screens):**

- **Enforcement (A-8) — 2 screens.** Proactive only; no service triggers it.
- **Harmonisation (A-9) — 2 screens.** Nothing routes to it, and following the A4
  resolution it is now simple manual reconciliation.

**Consequences to carry into the specs:**

- The DG sign-off screens handle **two** escalation sources — licence revocations
  (A-2) and final enforcement (A-8) — but only the A-2 path is live while A-8 is
  deferred. This must be stated in the spec so it is not later read as a defect.
- **The Inspection Officer works on site**, capturing geo-tagged findings and photos at
  a building. Every other Group A screen is desk-based back-office. These screens
  therefore need a phone/tablet form factor — a different design shape from the rest of
  the module.
- All eight roles remain defined in RBAC regardless; this decision concerns functional
  screens only.

## A6 — Group A back-office operating decisions *(added 2026-09-17)*

Surfaced by walking the Compliance & Escrow Auditor journey
(`ui/flows/compliance-escrow-auditor.md`). **All items resolved as of 2026-09-17.**

- **SLA clock on returned items.** ✅ **Resolved 2026-09-17: the clock RESETS on
  resubmission** — a resubmitted item gets a fresh full window from the originating
  service's published processing time (not pause-and-resume, not continuous). Because a
  repeatedly-queried item could then accumulate long real elapsed time while always showing
  green, the queue also carries a non-resetting **Total elapsed** figure so overall delay
  stays visible for oversight.
- **Claim lapse period.** ✅ **Resolved 2026-09-17: 30 minutes of inactivity**, after
  which the claim lapses and the item returns to the pool (`M-QUE-02`).
- **Supervisory review tier.** ✅ **Resolved 2026-09-17: none — one auditor's decision is
  final.** An approval issues its output directly; no senior countersignature exists. The
  eight-role model stands, with no senior/junior auditor tier, so an officer who cannot
  decide an item **releases** it rather than escalating. No pending-approval state, no
  second-approver queue.
- **Work allocation.** ✅ **Resolved 2026-09-17: shared pool** (claim-on-open), unlike
  A-3 dispute cases which are assigned to a named officer.
- **Notification delivery.** ✅ **Resolved 2026-09-17: in-app only.** No email or SMS —
  not for SLA breaches, not for DG escalations. Notifications remain a convenience
  surface; the queues and audit trail stay authoritative.
- **Step-up authentication.** ✅ **Resolved 2026-09-17: required** on the five
  widest-consequence actions (modals.md §9) — `M-ADM-03` change role permissions,
  `M-ADM-06` deactivate account, `M-LIC-03` revoke credential, `M-GOV-01` authorise
  sign-off, `M-FIN-02` publish fee schedule. The officer re-authenticates before the
  action proceeds.

## A7 — Back-office access and screen behaviour *(resolved 2026-09-17)*

Decisions taken on screen-level questions that were previously flagged only inside
individual specs.

- **Read-only oversight on Application Review.** ✅ The **Director-General / Registrar**
  may open a decided item and read it, but cannot change it — the Decision Panel is
  disabled for this role. No other non-deciding role gets access.
- **Separation of duties.** ✅ **Not required.** The officer who requested additional
  information on an item **may** later approve that same item. This is a deliberate
  loosening for simplicity and speed, not an oversight: it removes a second-pair-of-eyes
  check that some regulators require. Recorded explicitly so the trade-off is visible.
- **Super Administrator scope.** ✅ **One role**, covering both staff accounts and role
  permissions — not split into separate security-admin and user-admin roles.
- **Super Administrator break-glass.** ✅ **No override.** The Super Administrator
  reaches the Admin Console only and cannot open other officers' work screens. Being
  locked out of operational queues is the intended control, not a gap.
- **Work Queue summary cards and sort.** ✅ Four cards: **Breaching deadline**, **Due
  soon**, **Waiting to be picked up**, **My open items**. Sorted **most-urgent-deadline
  first, not oldest** — because the 92 services carry wildly different SLAs (25 minutes
  to 6 business days), so age is a misleading proxy for urgency. Dropped from the
  earlier draft: *Decided this month* (a performance statistic, not a triage signal),
  *Information requested* (work sitting with the applicant, so not actionable — better
  as a filter), and *Under review* (vague, and overlaps My open items).
