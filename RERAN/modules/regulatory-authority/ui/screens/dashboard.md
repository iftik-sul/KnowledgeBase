---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
tags: [regulatory-authority, ui-spec, back-office, dashboard]
---

# Screen: Dashboard

**Archetype:** 4 — Dashboard / Monitor.
**Access (RBAC-gated):** all roles (the landing screen); tiles are role-scoped. MFA required. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

The staff landing screen. Each role sees at-a-glance state for *their* work and drills into
the screens that act. It shows nothing a role cannot reach elsewhere — it is a summary and
a router, not an action surface.

## Purpose

Give each staff member an immediate picture of what needs their attention and one-click
routes into it, scoped to their role.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** Dashboard
* **Subtitle:** {role name} — your work at a glance

```
Top Bar → KPI tiles (role-scoped) → Attention lists → Drill-in links
```

## Sections

### Section 1 — KPI tiles (role-scoped)

Each tile links to the underlying screen. Tiles shown depend on the role's reachable
screens (role × screen matrix §1):

| Role | Tiles |
| :-- | :-- |
| C&E Auditor | Awaiting review · Breaching SLA · Escrow awaiting decision · Decided this month |
| Licensing Officer | Awaiting review · Breaching SLA · Practitioner register changes |
| Dispute Officer | Open cases · Scheduled sessions · Awaiting judgment |
| Super Admin | Active staff · Pending invites · Recent access changes |
| Revenue & Finance | Open reconciliation · Discrepancies · Pending remittances |

### Section 2 — Attention lists

Short lists of the most urgent items for the role (e.g. SLA-breaching queue rows, sessions
today), each row linking into its screen.

## Role Variations / Permissions

- Tiles and lists render only for the role's reachable screens; no tile routes anywhere the
  role cannot already go.
- Read-only. No decisions are taken on the dashboard.

## Notes

- **Landing destination (resolves flow gap G1).** Every role lands here after
  authentication, not on their work screen. The SLA-breach tile is the triage signal that
  decides which queue to open, so the Dashboard earns the first click.
- SLA/urgency figures reuse each source screen's definitions (e.g. Work Queue SLA logic);
  the dashboard does not redefine them.
