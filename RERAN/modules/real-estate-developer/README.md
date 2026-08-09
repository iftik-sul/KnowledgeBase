---
project: RERAN
module: real-estate-developer
type: overview
status: draft
updated: 2026-08-09
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - real-estate-developer
  - index
---

# Real Estate Developer Module

Documentation for RERAN user Group B — licensed development companies that register projects and off-plan sales, operate escrow accounts, and file construction progress. The most heavily regulated external group.

> **Status: scaffold.** The folder and file structure is in place; content is being migrated from `ui-design/RERAN_real_estate_developer_ui.md` (295 KB, retained until migration completes).

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

* The Role Permission Matrix grants the Sales & Disclosure Officer full access to Documents, but the source UI file documents no Documents list screen for that role — only Document Details. Every other role with Document Details also has a Documents list. Either the matrix is wrong or the screen is missing.
* Service flows for this module do not exist yet; the UI was documented first.
