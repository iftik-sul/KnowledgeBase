---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
---

# Screen: Institution Profile & Permissions

**Roles:** Institution Relationship Manager

## Purpose

Manage approval standing, staff roster and maker-checker permission scopes.

## Layout

Institution Operations Sidebar → Top Bar → record workspace → actions and activity timeline.

## Sections

1. **Institution Standing** — approval/cancellation status and expiry.
2. **Staff Roster** — invited and active users.
3. **Permission Scopes** — file, certify and operator scopes; certification is not a role.
4. **Approval History** — renewal/cancellation audit history.

## Empty State

> No relevant records yet. Start a service request or adjust filters.

## Reused Components

Institution Operations Sidebar, Top Bar, Status Badges, Progress Tracker, Information Cards, Audit Timeline and Buttons.

## Validation

**Proposed** — actions are available only to users with the relevant permission scope and only when the current status permits them.

## Role Variations

Institution Relationship Manager sees institution-wide context; Mortgage Officer sees bank-originated work; delegated certifier scope sees only items awaiting certification; assisted operators see only represented-customer work.

## User Flow

Dashboard → Institution Profile → Service #1 / Service #2 / staff-scope action.

## Notes

All screen detail is **Proposed**, derived from the completed Group C service flows.
