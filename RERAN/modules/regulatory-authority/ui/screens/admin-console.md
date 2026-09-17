---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a6-provision-and-manage-access.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, back-office, rbac, admin]
---

# Screen: Admin Console

**Archetype:** 3 — Editor / Config.
**Access (RBAC-gated):** System Super Administrator only. MFA required. This is the most sensitive surface in the app — it administers the RBAC that every other screen relies on. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

Where staff accounts, roles, and permissions are managed (A-6). It is the service that *is*
RBAC, rendered as three linked editor surfaces.

## Purpose

Let the Super Administrator provision and manage staff, assign the eight roles, configure
their permissions, and enrol MFA — with every access change recorded.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (Super Admin scope)
* **Top Bar Title:** Admin Console
* **Tabs:** Staff · Roles & Permissions

```
Top Bar → [Staff tab] Staff Directory → Account Editor
        → [Roles tab]  Role & Permission Editor
```

## Sections

### Section 1 — Staff Directory (Staff tab)

| Column | Notes |
| :-- | :-- |
| Staff member | Name / email |
| Role(s) | Assigned Group A role(s) |
| MFA | Enrolled / not |
| Status | Invited / Active / Suspended / Deactivated |

Row click → Account Editor.

### Section 2 — Account Editor

Create/edit an account, assign one or more of the eight roles, enrol/reset MFA, and
suspend/deactivate. An account cannot act until it has a role and enrolled MFA
(validation-rules).

### Section 3 — Role & Permission Editor (Roles tab)

The eight Group A roles and the permissions attached to each (least-privilege). All eight
roles are definable and assignable even where their functional screens are deferred (A-6
§15 / open-questions A5).

## Role Variations / Permissions

- **System Super Administrator only.** No other role reaches this console.
- Actions: create/edit/suspend/deactivate accounts; assign/revoke roles; configure role
  permissions; enrol/reset MFA. All are logged to the Audit Trail.

## Notes

- Suspending or deactivating an account withdraws its access immediately (validation-rules).
- Access changes are read (not edited) via the [Audit Trail](audit-trail.md), filtered to
  access actions.

**One role — confirmed.** The Super Administrator is a single role covering both staff
accounts and role permissions; it is **not** split into separate security-admin and
user-admin roles.

**No break-glass override — confirmed.** This console is the only screen the Super
Administrator reaches. It cannot open other officers' work queues or decision screens.
Being locked out of operational work is the intended control, not a gap (open-questions A7).

**Step-up authentication required** on `M-ADM-03` (change role permissions) and `M-ADM-06`
(deactivate account) — the officer re-authenticates before either proceeds.
