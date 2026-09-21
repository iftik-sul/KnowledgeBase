---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-18
derived_from:
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
  - "RERAN/modules/regulatory-authority/service-flows/service-a6-provision-and-manage-access.md"
tags: [regulatory-authority, ui-spec, back-office, audit]
---

# Screen: Audit Trail

**Archetype:** 1 — Queue (read-only, no decision).
**Access (RBAC-gated):** all roles, read-only. MFA required. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

The permanent, searchable record of every state-changing action in the back-office app.
Every Regulatory Authority service writes to it; this screen reads it. It is the
accountability surface the whole module's "recorded to the audit trail" claims resolve
to.

## Purpose

Let any staff member (and oversight roles) see who did what, when, and why — across
decisions, config changes, and access changes — without being able to alter it.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** Audit Trail
* **Search Bar:** Search by actor, item reference, or action...

```
Top Bar → Filters & Search → Audit Table → Pagination
```

## Sections

### Section 1 — Filters & Search

**Filter by:** actor (staff user) · action type (decision / config / access) · date range ·
subsystem · item reference.

### Section 2 — Audit Table

| Column | Notes |
| :-- | :-- |
| Timestamp | When |
| Actor | Staff user + role acted under |
| Action | e.g. "Approved", "Fee published", "Role assigned" |
| Subject | Item reference / account / record |
| Reason | Where the action required one |

Row click → read-only detail of the entry.

## Role Variations / Permissions

- **All roles: read-only.** The audit trail cannot be edited or deleted by anyone,
  including Super Admin (append-only).
- **Decision and config actions are visible to all roles.** The trail is one shared,
  module-wide record; narrowing the view is done by **filtering** (actor, action type,
  date range, subsystem, item reference), never by giving each role a siloed trail.
- **Access-control actions are gated to oversight roles (open-questions A9, resolved
  2026-09-18).** The `access` action type — role assignments, account activations /
  suspensions / deactivations, MFA resets (the A-6 access actions) — is visible **only to
  the System Super Administrator and the Director-General / Registrar**. Ordinary
  operational roles (C&E Auditor, Licensing Officer, Dispute Officer, Revenue & Finance
  Officer, Inspection & Enforcement Officer) do **not** see access-type rows. This is a
  row-level RBAC rule on one action-type, not a siloing of the trail as a whole — those
  roles still see every decision and config entry.
- The "Access audit" referenced by A-6 is this screen filtered to access actions, shown
  to the two oversight roles that are permitted to see them.

## Notes

- Append-only by design; there is no edit or delete action anywhere on this screen.
- Sample content per role: the five ordinary-officer Audit Trails show only decision and
  config rows; the Super Admin and DG / Registrar Audit Trails additionally show access
  rows.
