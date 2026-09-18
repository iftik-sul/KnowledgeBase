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
- Super Admin's access-change entries and decision entries share this one trail; the
  "Access audit" referenced by A-6 is this screen filtered to access actions.

## Notes

- Append-only by design; there is no edit or delete action anywhere on this screen.
