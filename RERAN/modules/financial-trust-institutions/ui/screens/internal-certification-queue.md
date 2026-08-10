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

# Screen: Internal Certification Queue

**Roles:** delegated staff with certifier permission scope

## Purpose

Allow scoped makers/checkers to certify or return institutional filings before RERAN submission.

## Layout

Institution Operations Sidebar → Top Bar → record workspace → actions and activity timeline.

## Sections

1. **Queue Filters** — service, submitter, age and SLA.
2. **Request Review** — details, documents and validation results.
3. **Decision Panel** — Certify or Return by Certifier; return reason mandatory.
4. **Delegation Context** — certifier scope and audit record.

## Empty State

> No relevant records yet. Start a service request or adjust filters.

## Reused Components

Institution Operations Sidebar, Top Bar, Status Badges, Progress Tracker, Information Cards, Audit Timeline and Buttons.

## Validation

**Proposed** — actions are available only to users with the relevant permission scope and only when the current status permits them.

## Role Variations

Institution Relationship Manager sees institution-wide context; Mortgage Officer sees bank-originated work; delegated certifier scope sees only items awaiting certification; assisted operators see only represented-customer work.

## User Flow

Dashboard → Internal Certification Queue → Application Details → Submitted to RERAN.

## Notes

All screen detail is **Proposed**, derived from the completed Group C service flows.
