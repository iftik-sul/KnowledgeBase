---
project: RERAN
module: financial-trust-institutions
type: overview
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/"
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - index
---

# Financial & Trust Institutions UI Specifications

This package derives reusable UI specifications from the 18 Group C service flows. **Proposed** — the source gives workflows but no screen designs; this package applies the established RERAN UI-spec format.

## Service × Form Matrix

| Service | Primary service form | Assisted mode | Internal certification |
| :---- | :---- | :---: | :---: |
| #1 Approval / renewal | [service-request.md](screens/service-request.md) | — | Optional |
| #2 Cancellation | service-request.md | — | Optional |
| #3–#7 Mortgage lifecycle | service-request.md | Where source names centre | Yes when configured |
| #8–#11 Finance lease lifecycle | service-request.md | Yes | Optional |
| #12 Fund company registration | service-request.md | Yes | Optional |
| #13 Heirs' sale procedure | service-request.md | Yes | Optional |
| #14 Company shares sale | service-request.md | Yes | Optional |
| #15 Title deed update | service-request.md | Yes | Optional |
| #16 Split ownership | service-request.md | Yes | Optional |
| #17 Issue title deed | service-request.md | Yes | Optional |
| #18 Contract cancellation | service-request.md | Yes | Optional |

## Screens

| Screen | Purpose |
| :---- | :---- |
| [dashboard.md](screens/dashboard.md) | Institution work, approvals and settlement overview |
| [applications.md](screens/applications.md) | Search, filter and action all requests |
| [application-details.md](screens/application-details.md) | Review one request, its workflow and audit trail |
| [service-request.md](screens/service-request.md) | Configurable form used by all 18 services |
| [internal-certification-queue.md](screens/internal-certification-queue.md) | Maker-checker queue for delegated certifier scopes |
| [assisted-service-terminal.md](screens/assisted-service-terminal.md) | Same online service operated for a customer at a centre |
| [settlement-account.md](screens/settlement-account.md) | Balance, funding, ledger and settlement state |
| [institution-profile.md](screens/institution-profile.md) | Approval standing, users and permission scopes |
| [documents.md](screens/documents.md) | Shared document repository and request attachments |
| [notifications.md](screens/notifications.md) | Operational, approval and low-balance alerts |

## Shared Documentation

* [components.md](components.md)
* [validation-rules.md](validation-rules.md)
* [status-badges.md](status-badges.md)

## Screen File Template

Every screen uses: Purpose, Layout, Sections, Empty State, Reused Components, Validation, Role Variations, User Flow and Notes.
