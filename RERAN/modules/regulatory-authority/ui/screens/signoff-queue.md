---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-18
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a10-executive-signoff-revocation.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, back-office, governance, queue]
---

# Screen: Sign-off Queue

**Archetype:** 1 — Queue.
**Access (RBAC-gated):** Director-General / Registrar. MFA required. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

The executive worklist (A-10): matters escalated to the Director-General for authorisation —
licence revocations (A-2, live) and, when active, final enforcement (A-8, deferred). Follows the
Queue archetype; row click opens the [Sign-off Detail](signoff-detail.md). This is the most
privileged and least-frequently-used surface in the module — not a first-line applicant queue.

## Purpose

Give the Director-General a single accountable list of matters awaiting executive authorisation,
with enough context to pick up the right one, so serious/final actions are never taken without
recorded executive authority.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** Sign-off Queue
* **Search Bar:** Search by reference, matter, or originating tier...

```
Top Bar → Summary Cards → Filters & Search → Sign-off Table → Pagination
```

## Sections

### Section 1 — Summary Cards

Pending sign-off · Authorised this month · Declined this month · Oldest pending (age).

### Section 2 — Filters & Search

**Filter by:** escalation source (Revocation A-2 / Final Enforcement A-8) · status (status-badges §3
config/governance vocabulary) · age. **Search by:** reference · matter.

### Section 3 — Sign-off Table

| Column | Notes |
| :-- | :-- |
| Reference | The escalation reference |
| Matter | What is being authorised (e.g. licence revocation of {practitioner}) |
| Source | Originating tier — A-2 Licensing (live) / A-8 Enforcement (deferred) |
| Recommendation | The lower tier's recommendation, in brief |
| Status | Pending Sign-off / Authorised / Declined (status-badges §3) |
| Escalated | Date the matter reached the DG |

Row click → [Sign-off Detail](signoff-detail.md).

## Role Variations / Permissions

- Director-General / Registrar only reaches this screen. No authorisation is taken here — it happens
  on the Sign-off Detail screen with step-up re-authentication (`M-GOV-01`).

## Notes

- Only the A-2 revocation source is live; the A-8 enforcement source is supported in the layout but
  no matters currently arrive from it (per A-10 service flow). Not a defect.
- Statuses use the config/governance vocabulary (status-badges §3), not the shared four-state
  decision vocabulary.
