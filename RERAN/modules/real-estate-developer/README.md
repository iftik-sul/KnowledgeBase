---
project: RERAN
module: real-estate-developer
type: overview
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - real-estate-developer
  - index
---

# Real Estate Developer Module

Documentation for RERAN user Group B — licensed development companies that register projects and off-plan sales, operate escrow accounts, and file construction progress. The most heavily regulated external group.

## Roles (4)

* [roles-and-responsibilities.md](roles-and-responsibilities.md) — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison.
* [role-workflows.md](role-workflows.md) — the linear path each role takes through the system.

## Navigation & Access

* [navigation.md](navigation.md) — sidebar structure, role permission matrix, dashboard-by-role summary.

## Service Flows

> Not yet written. This module currently has UI documentation without the service flows it should derive from — the reverse of the normal pipeline. `role-workflows.md` is the seed of what these should cover.

## UI Specifications

* [ui/README.md](ui/README.md) — role × screen matrix and screen index (19 distinct screens).

## Open Questions

* The Role Permission Matrix grants the Sales & Disclosure Officer full access to Documents, but no Documents list screen exists for that role in [ui/documents.md](ui/documents.md) — only Document Details. Every other role with Document Details also has a Documents list. A fragment matching a Documents screen for this role was found misplaced (at the wrong heading level) inside that role's Application Details section of the original UI source during migration, but was left out of `documents.md` rather than silently resolving the discrepancy — it's a client question, not a documentation call. See [ui/documents.md](ui/documents.md) for the pointer.
* Service flows for this module do not exist yet; the UI was documented first. `role-workflows.md` is the seed of what these should cover. Every UI file's `derived_from` currently points at `reference/source-of-truth/RERAN_service_flows_v2.md` and `RERAN_user_group_structure_v2.md` as a temporary measure, since there is no module-level service-flow document yet to cite as the immediate parent.

## Known Gap from Source Retirement

The original combined UI document (`ui-design/RERAN_real_estate_developer_ui.md`) has been migrated into this module's structured files and deleted. Two pieces of its content were never migrated and no longer exist anywhere:

* A short "Module Overview" paragraph and a second, shorter "Roles & Responsibilities" section (four roles, Purpose/Responsibilities format) that duplicated — in briefer form — what [roles-and-responsibilities.md](roles-and-responsibilities.md) already documents in full. Flagged as unmigrated when found, and left out on the judgment that it was redundant with content already captured elsewhere, not a distinct business rule.
* The misplaced Sales & Disclosure Officer Documents-screen fragment referenced in Open Questions above.

Both were reported at the time they were found. Recorded here since the source they lived in no longer exists to consult.
