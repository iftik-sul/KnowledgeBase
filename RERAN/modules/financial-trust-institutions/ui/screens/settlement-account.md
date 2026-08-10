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

# Screen: Settlement Account

**Roles:** Institution Relationship Manager; read-only visibility where permitted

## Purpose

Show the standing pre-funded account used for post-approval Group C fee settlement.

## Layout

Institution Operations Sidebar → Top Bar → record workspace → actions and activity timeline.

## Sections

1. **Balance Summary** — available balance, pending fees and low-balance state.
2. **Funding** — funding instructions and top-up history.
3. **Ledger** — charge, credit, receipt, balance-after and linked application.
4. **Awaiting Settlement** — approved requests that need funds, expiry date and retry action.
5. **Statements** — exportable periodic statement.

## Empty State

> No relevant records yet. Start a service request or adjust filters.

## Reused Components

Institution Operations Sidebar, Top Bar, Status Badges, Progress Tracker, Information Cards, Audit Timeline and Buttons.

## Validation

**Proposed** — actions are available only to users with the relevant permission scope and only when the current status permits them.

## Role Variations

Institution Relationship Manager sees institution-wide context; Mortgage Officer sees bank-originated work; delegated certifier scope sees only items awaiting certification; assisted operators see only represented-customer work.

## User Flow

Dashboard → Settlement Account → Application Details / receipt.

## Notes

All screen detail is **Proposed**, derived from the completed Group C service flows.
