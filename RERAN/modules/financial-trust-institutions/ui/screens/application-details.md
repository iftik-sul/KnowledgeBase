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

# Screen: Application Details

**Roles:** all Group C filing and assisted-operation contexts

## Purpose

Review one service request from draft through output issue.

## Layout

Institution Operations Sidebar → Top Bar → record workspace → actions and activity timeline.

## Sections

1. **Header** — reference, service, represented party, status and SLA.
2. **Progress** — core lifecycle plus Group C certification extension.
3. **Request Details** — service-specific data, property/instrument and parties.
4. **Documents** — required/proposed slots, validation and version history.
5. **Certification & RERAN Decision** — visible according to role and status.
6. **Settlement & Outputs** — fee charge, balance-after, receipt and issued documents.
7. **Audit Timeline** — full event history.

## Empty State

> No relevant records yet. Start a service request or adjust filters.

## Reused Components

Institution Operations Sidebar, Top Bar, Status Badges, Progress Tracker, Information Cards, Audit Timeline and Buttons.

## Validation

**Proposed** — actions are available only to users with the relevant permission scope and only when the current status permits them.

## Role Variations

Institution Relationship Manager sees institution-wide context; Mortgage Officer sees bank-originated work; delegated certifier scope sees only items awaiting certification; assisted operators see only represented-customer work.

## User Flow

Applications → Application Details → Service Request / Internal Certification Queue / Settlement Account.

## Notes

All screen detail is **Proposed**, derived from the completed Group C service flows.
