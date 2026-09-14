---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-12
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

**Access (RBAC-gated):** Compliance & Escrow Auditor (transaction + escrow items);
Licensing & Registration Officer (licensing items). Only the item's primary decision role
may record a decision here. MFA required. See [role-screen-matrix.md](../role-screen-matrix.md).

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

### Section 5 — Escrow panels *(escrow items only)*

- **Trustee Assessment** — the FTI Account Trustee's uploaded assessment (A-1 §6).
- **Escrow Account** — current account state; account-movement context for the escrow
  checklist (A-1 §7). For mortgage-linked items, the live FTI mortgage status (must read
  `Completed`).

### Section 6 — Decision Panel *(the core control)*

Four mutually exclusive outcomes:

| Outcome | Effect | Reason field |
| :-- | :-- | :-- |
| Approve | Issues the originating service's output; item completes | Optional |
| Request Additional Information | Returns to applicant; re-enters the queue on response | **Required** |
| Return | Sends back for correction | **Required** |
| Reject | Terminal | **Required** |

On approve, the output (certificate / title deed / map / registry update) is triggered per
the originating service. Every outcome writes the decision, actor, and reason to the audit
trail.

## Role Variations / Permissions

- **Compliance & Escrow Auditor** — full view + decide on transaction and escrow items;
  the escrow panels (Section 5) render only for escrow items and only for this role.
- **Licensing & Registration Officer** — full view + decide on licensing items; sees a
  Practitioner-Register check in place of the property registry checks; no escrow panels.
- **View-only roles** (if any are later granted read access, e.g. for oversight) see all
  panels but the Decision Panel is disabled.
- The Decision Panel is **enabled only for the item's primary decision role**; reaching the
  screen does not by itself grant decide rights (per the matrix).

## Status transitions

Uses the shared platform status vocabulary (A-1 §13): `Under Review → Information Requested
/ Returned / Approved / Rejected`. This screen must not introduce local status words — the
originating modules' status displays read these.

## Notes

- A reason is mandatory for request-info / return / reject (A-1 §21).
- Escrow items cannot be decided until the trustee assessment is present (A-1 §22.3).
- A mortgage-registration approval flips the mortgage to `Completed` for RED #6's live check
  (A-1 §16.2).

> **Proposed** — whether any non-decision role gets read-only access here (for oversight)
> is open; the escrow review checklist itself is a `Proposed` item on A-1 §7.
