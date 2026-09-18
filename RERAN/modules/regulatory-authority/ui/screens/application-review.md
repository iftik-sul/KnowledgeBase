---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a1-audit-and-decide.md"
  - "RERAN/modules/regulatory-authority/service-flows/service-a2-vet-and-decide-licensing.md"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
tags:
  - regulatory-authority
  - ui-spec
  - back-office
  - decision
---

# Screen: Application Review

**Archetype:** 2 — Detail / Decision.
**Access (RBAC-gated):** Compliance & Escrow Auditor (transaction + escrow items); Licensing & Registration Officer (licensing items). Only the item's primary decision role may record a decision here. MFA required. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

The screen where the actual decision happens. A reviewer opens one item from the
[Work Queue](work-queue.md), sees the application, its documents, and live registry checks
in one view, and records one of four outcomes. This is **the highest-leverage screen in the
platform**: A-1 alone routes 92 services through it.

## Purpose

Put everything a reviewer needs to decide an item on one screen — the application, its
documents, the registry verification, and (for escrow) the trustee assessment — and let
them record an auditable decision with a mandatory reason where required.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** {Reference} — {Originating service}
* **Top Bar meta:** status badge · SLA state · applicant

```
Top Bar (reference, status, SLA)
↓
Item Header  (applicant · subject · originating service)
↓
Two-column body:
  Left  → Application panel · Documents panel
  Right → Registry Checks panel · (escrow) Trustee Assessment + Escrow Account panels
↓
Decision Panel  (sticky footer)
↓
Activity / Audit trail (collapsible)
```

## Sections

### Section 1 — Item Header

Applicant, subject (project / property / title / practitioner), originating service and its
expected output and SLA.

### Section 2 — Application Panel

The application exactly as submitted (all fields), read-only.

### Section 3 — Documents Panel

All uploaded supporting documents, viewable inline; each can be marked seen / flagged.

### Section 4 — Registry Checks Panel

Live registry verification, pulled not re-keyed: developer / project / unit / title /
applicant validity and consistency, each with a pass / attention indicator. This is the
review checklist (A-1 §7) rendered as live checks.

If a guard prevents a decision, the screen explains why rather than silently disabling the
panel: `M-BLK-01` (registry checks unavailable), `M-BLK-02` (escrow item with no trustee
assessment), `M-BLK-03` (mortgage prerequisites unmet), `M-BLK-05` (no decide rights),
`M-BLK-06` (MFA not enrolled).

### Section 5 — Escrow panels *(escrow items only)*

- **Trustee Assessment** — the FTI Account Trustee's uploaded assessment (A-1 §6).
- **Escrow Account** — current account state; account-movement context for the escrow
  checklist (A-1 §7). For mortgage-linked items, the live FTI mortgage status (must read
  `Completed`).

### Section 5b — Claim, draft, and release *(resolves flow gaps G5, G6, G7)*

- **Claim.** Opening an item from the queue claims it to this officer (shared-pool model,
  work-queue §4). The header shows the claim and when it was taken. Opening an item another
  officer holds raises `M-QUE-03`; a lapsed claim raises `M-QUE-02`.
- **Draft note.** The officer may save a part-written decision note against the item,
  visible only to the claiming officer. A considered review can span a break or a shift
  without losing work; `M-SYS-04` warns on exit with unsaved changes.
- **Release.** "Release item" (`M-QUE-01`) returns it to the pool with a recorded reason —
  the path for "this isn't mine to decide" (conflict of interest, wrong specialism). The
  draft note is discarded on release.

> **No escalation path exists, by design (confirmed).** One auditor's decision is final —
> an approval issues its output directly, with no senior countersignature. The eight-role
> model has no senior/junior auditor tier, so there is no one to escalate a transaction
> audit *to*: an officer who cannot decide an item releases it. There is therefore no
> pending-approval state on this screen and no second-approver queue (open-questions A6).

### Section 6 — Decision Panel *(the core control)*

Four mutually exclusive outcomes:

| Outcome | Modal | Effect | Reason field |
| :-- | :-- | :-- | :-- |
| Approve | `M-DEC-01` | Issues the originating service's output; item completes | Optional |
| Request Additional Information | `M-DEC-02` | Returns to applicant; re-enters the queue on response | **Required** |
| Return | `M-DEC-03` | Sends back for correction | **Required** |
| Reject | `M-DEC-04` | Terminal | **Required** |

Modal wording and fields are owned by [modals.md](../modals.md) §2.

On approve, the output (certificate / title deed / map / registry update) is triggered per
the originating service. Every outcome writes the decision, actor, and reason to the audit
trail. Field-level guards (mandatory reasons, escrow/mortgage blocks) are in
[validation-rules.md](../validation-rules.md).

**After the decision (resolves flow gap G8).** The officer is returned to the queue with a
success toast naming the outcome and a link back to the decided item (read-only). The queue
does **not** auto-advance to the next item: these decisions carry mandatory written reasons
and legal weight, so deliberate re-entry is preferred over momentum. There is **no undo** —
approval issues the output immediately (`M-DEC-01`); the link returns to view, not to
reverse.

## Role Variations / Permissions

- **Compliance & Escrow Auditor** — full view + decide on transaction and escrow items;
  the escrow panels (Section 5) render only for escrow items and only for this role.
- **Licensing & Registration Officer** — full view + decide on licensing items; sees a
  Practitioner-Register check in place of the property registry checks; no escrow panels.
- **Director-General / Registrar — read-only oversight (confirmed).** May open a decided
  item and read every panel, but the Decision Panel is **disabled**; the DG cannot change
  an auditor's decision. No other non-deciding role has access (open-questions A7).
- The Decision Panel is **enabled only for the item's primary decision role**; reaching the
  screen does not by itself grant decide rights (per the matrix).

## Status transitions

Uses the shared decision status vocabulary — see [status-badges.md](../status-badges.md) §1
(the single source; do not localise). This screen must not introduce local status words, as
the originating modules' status displays read them.

## Notes

- A reason is mandatory for request-info / return / reject (A-1 §21).
- Escrow items cannot be decided until the trustee assessment is present (A-1 §22.3).
- A mortgage-registration approval flips the mortgage to `Completed` for RED #6's live check
  (A-1 §16.2).

**Separation of duties — not required (confirmed).** The officer who requested additional
information on an item **may** later approve that same item; nothing blocks it. This is a
deliberate simplification rather than an oversight — it removes a second-pair-of-eyes check
that some regulators impose (open-questions A7).

> **Proposed** — the escrow review checklist remains a `Proposed` item on A-1 §7.
