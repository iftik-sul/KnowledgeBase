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

# Screen: Service Request

**Roles:** Institution Relationship Manager, Mortgage Officer, assisted operator

## Purpose

Configurable service form used by all 18 Group C services.

## Layout

Institution Operations Sidebar → Top Bar → record workspace → actions and activity timeline.

## Sections

1. **Service Header** — selected service, source SLA and access mode.
2. **Applicant & Representation** — institution/customer and authority.
3. **Transaction Details** — dynamic fields for property, mortgage, lease, contract, fund, heirs or title action.
4. **Supporting Documents** — proposed service-specific document slots.
5. **Review & Submit** — validation summary and certification requirement.
6. **Assisted Mode** — operator identity and customer consent/representation record.

## Empty State

> No relevant records yet. Start a service request or adjust filters.

## Reused Components

Institution Operations Sidebar, Top Bar, Status Badges, Progress Tracker, Information Cards, Audit Timeline and Buttons.

## Validation

**Proposed** — actions are available only to users with the relevant permission scope and only when the current status permits them.

## Role Variations

Institution Relationship Manager sees institution-wide context; Mortgage Officer sees bank-originated work; delegated certifier scope sees only items awaiting certification; assisted operators see only represented-customer work.

## User Flow

Dashboard / Applications → Service Request → Internal Certification Queue or Application Details.

## Notes

All screen detail is **Proposed**, derived from the completed Group C service flows.
