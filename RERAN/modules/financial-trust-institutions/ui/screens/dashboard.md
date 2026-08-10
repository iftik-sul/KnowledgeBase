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

# Screen: Institution Dashboard

**Roles:** Institution Relationship Manager, Mortgage Officer, delegated certifier scope and assisted operator.

## Purpose

Provide a role-scoped overview of applications, institutional standing and settlement work.

## Layout

Institution Operations Sidebar → Top Bar → KPI Cards → Action Queue → Recent Applications → Settlement Summary → Notifications.

## Sections

1. **KPI Cards** — draft, awaiting certification, under review, awaiting payment, completed and expiring approvals.
2. **My Action Queue** — filing, certification, response and settlement actions.
3. **Recent Applications** — reference, service, represented party, status, SLA and next action.
4. **Settlement Summary** — available balance, pending charges and low-balance alert.
5. **Institution Standing** — trustee/auditor approval status, expiry countdown and renewal action.

## Empty State

> No applications need action. Start a service request from the Services catalogue.

## Reused Components

KPI Cards, Application Table, Status Badges, Settlement Balance Card and Permission Scope Chip.

## Validation

Dashboard is read-only; destination actions enforce permission scopes.

## Role Variations

IRM sees institution standing, staff scopes and balance; Mortgage Officer sees bank-originated requests; delegated certifier sees certification work; assisted operator sees represented-customer work.

## User Flow

Dashboard → Application Details / Service Request / Internal Certification Queue / Settlement Account.

## Notes

All detail is **Proposed**, derived from Group C flows.
