---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a6-provision-and-manage-access.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, back-office, rbac, admin]
---

# Screen: Admin Console

**Archetype:** 3 — Editor / Config.
**Access (RBAC-gated):** System Super Administrator only. MFA required. This is the most
sensitive surface in the app — it administers the RBAC that every other screen relies on.

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

> **Proposed** — whether the platform-wide Super Admin is one role or split (e.g. security
> admin vs user admin) is open; modelled here as one per source.
