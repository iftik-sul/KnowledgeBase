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

# Screen: Assisted Service Terminal

**Roles:** Trustee Centre and Land Department operators

## Purpose

Run the same online Group C service on a customer’s behalf where the source names a counter.

## Layout

Institution Operations Sidebar → Top Bar → record workspace → actions and activity timeline.

## Sections

1. **Operator & Customer Context** — operator identity, customer/institution and authority.
2. **Service Selection** — only scopes permitted to the operator.
3. **Transaction Capture** — dynamic service-request form.
4. **Document Capture** — upload, scan and preview.
5. **Review Handoff** — customer acknowledgement and submission summary.

## Empty State

> No relevant records yet. Start a service request or adjust filters.

## Reused Components

Institution Operations Sidebar, Top Bar, Status Badges, Progress Tracker, Information Cards, Audit Timeline and Buttons.

## Validation

**Proposed** — actions are available only to users with the relevant permission scope and only when the current status permits them.

## Role Variations

Institution Relationship Manager sees institution-wide context; Mortgage Officer sees bank-originated work; delegated certifier scope sees only items awaiting certification; assisted operators see only represented-customer work.

## User Flow

Dashboard / Applications → Assisted Service Terminal → Service Request → Application Details.

## Notes

All screen detail is **Proposed**, derived from the completed Group C service flows.
