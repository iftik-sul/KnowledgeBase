---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a2-vet-and-decide-licensing.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, back-office, licensing, register]
---

# Screen: National Practitioner Register

**Archetype:** 3 — Editor / Config (with a read-heavy list).
**Access (RBAC-gated):** Licensing & Registration Officer (write); other roles may read where the register backs a check (e.g. Application Review's practitioner check reads it). MFA required. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

The authoritative record of who is licensed to operate — developers, agents, surveyors,
companies, and their practice cards. A-2 is its **sole writer**; every front-office
verification lookup reads it. This screen is where the register is browsed and its entries
maintained.

## Purpose

Keep one authoritative, searchable register of licensed practitioners and credentials, and
give the Licensing Officer the surface to maintain entries as licences/cards are issued,
renewed, amended, or cancelled.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** National Practitioner Register
* **Search Bar:** Search by name, credential no., or company...

```
Top Bar → Filters & Search → Register Table → Entry Detail/Editor → History
```

## Sections

### Section 1 — Filters & Search

**Filter by:** credential type (licence / permit / practice card / accreditation) · status ·
credential expiry. **Search by:** practitioner name · credential number · company.

### Section 2 — Register Table

| Column | Notes |
| :-- | :-- |
| Practitioner / company | |
| Credential type | |
| Credential number | |
| Status | Active / suspended / cancelled / expired |
| Valid to | Expiry, where applicable |

### Section 3 — Entry Detail / Editor

The full register entry; the Licensing Officer can amend or cancel it (writes flow from
A-2's decisions, not free-hand edits). Shows the entry's issue/renew/amend/cancel history.

## Role Variations / Permissions

- **Licensing & Registration Officer** — read + write (issue/renew/amend/cancel via A-2).
- **Other roles** — the register is read-only and reached indirectly (e.g. Application
  Review reads a practitioner check against it); direct navigation is Licensing-only per the
  matrix.

## Notes

- A-2 is the **only writer** of this register (A-2 §16); this screen must not allow writes
  from any other path.
- Auto-approval card renew/amend (A-2 §15b) update entries here without a manual queue item.
