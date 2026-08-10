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

# Screen: Documents

**Roles:** all Group C contexts with document access

## Purpose

Find, review and manage documents attached to Group C service requests.

## Layout

Institution Operations Sidebar → Top Bar → record workspace → actions and activity timeline.

## Sections

1. **Filters** — application, service, document status and date.
2. **Document Table** — name, linked request, version, upload status and action.
3. **Preview & Version History** — read-only audit-safe preview.
4. **Upload Action** — available only to current owner at an editable status.

## Empty State

> No relevant records yet. Start a service request or adjust filters.

## Reused Components

Institution Operations Sidebar, Top Bar, Status Badges, Progress Tracker, Information Cards, Audit Timeline and Buttons.

## Validation

**Proposed** — actions are available only to users with the relevant permission scope and only when the current status permits them.

## Role Variations

Institution Relationship Manager sees institution-wide context; Mortgage Officer sees bank-originated work; delegated certifier scope sees only items awaiting certification; assisted operators see only represented-customer work.

## User Flow

Dashboard / Applications → Documents → Application Details.

## Notes

All screen detail is **Proposed**, derived from the completed Group C service flows.
