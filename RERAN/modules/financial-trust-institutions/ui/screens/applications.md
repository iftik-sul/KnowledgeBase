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

# Screen: Applications

**Roles:** all Group C filing and assisted-operation contexts.

## Purpose

Find, filter and action service requests across all 18 Group C services.

## Layout

Sidebar → Top Bar → Filter Bar → Application Table → Pagination.

## Sections

1. **Filters** — service, status, represented party, date, SLA state and assisted-mode flag.
2. **Application Table** — reference, service, applicant, current owner, status, submitted date, SLA and actions.
3. **Exports** — list export only; decisions remain record-level. **Proposed**

## Empty State

> No applications match these filters. Start a new request or clear filters.

## Reused Components

Filter Bar, Application Table, Status Badges, Pagination and Overflow Action Menu.

## Validation

Actions appear only where current status and permission scope permit them.

## Role Variations

IRM sees institution-wide activity; Mortgage Officer sees bank-originated requests; delegated certifier sees pending-certification items; operator sees their assisted requests.

## User Flow

Applications → Application Details → Service Request / Internal Certification Queue.

## Notes

All list fields are **Proposed**.
