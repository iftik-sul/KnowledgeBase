---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/service-flows/service-01-register-company-jop-supervision.md"
  - "RERAN/modules/real-estate-service-companies/service-flows/service-04-register-owners-association.md"
  - "RERAN/modules/real-estate-service-companies/service-flows/service-05-transfer-jop-escrow-account.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - jointly-owned-property
---

# Screen: Jointly Owned Property

**Access:** Any of the company's four Group D roles — identical screen for every user.

## Purpose

A standing register of every jointly-owned property under the company's administrative supervision — what exists, its escrow position, its auditor appointments, its owners' association status — separate from the transactional queue of individual applications filed against it. The same reasoning Financial & Trust Institutions used to justify Trust Accounts as its own feature, distinct from its Escrow Request Queue.

## Layout

```
Top Bar
↓
Register Summary Cards
↓
Filters & Search
↓
JOP Property Register
↓
Pagination
```

## Sections

### Section 1 — Register Summary Cards

| KPI | Description |
| :---- | :---- |
| Properties Under Supervision | Count with an active Service #1 registration |
| Owners Associations Registered | Count with an approved Service #4 |
| Pending Auditor Appointments | Services #8–#10 awaiting RERA decision |
| Active Escrow-Adjacent Requests | Services #5–#7 currently in flight |

### Section 2 — Filters & Search

**Search by:** Property name/reference · Owners' Association name

**Filters:** Supervision Status · Owners' Association Status · Escrow Activity

### Section 3 — JOP Property Register

| Column | Description |
| :---- | :---- |
| Property Reference | Links to Property Detail Panel |
| Property Name / Address | |
| Supervision Status | Active · Pending · Not Registered |
| Owners' Association | Registered · Not Registered |
| Appointed Auditor(s) | Where applicable |
| Last Activity | Most recent JOP-related application against this property |

**Row action:** View → opens a Property Detail Panel with the property's full JOP history — supervision registration, association status, fee-schedule approvals, escrow-adjacent requests, and auditor appointments, each linking to its own application in [Application Details](application-details.md).

## Empty State

**Message**

> No jointly-owned properties registered yet. Register your company's administrative supervision of a property to begin.

**Primary Button:** Register JOP Property (Service #1)

## Reused Components

Company Operations Sidebar, Top Bar, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State.

## Validation

1. A property must have an active Service #1 registration to appear in this register at all.
2. **No Account Trustee status appears anywhere on this screen** — confirmed against `open-questions.md` A3, JOP's escrow-adjacent services (#5–#7) route directly to RERA's Compliance & Escrow Auditor with no Trustee intermediary. Do not add a Trustee-facing status column here without revisiting A3 first.

## Access

Identical for all four roles.

## User Flow

```
Dashboard / Applications
↓
Jointly Owned Property
├─ Register JOP Property → Submit Application (Service #1)
└─ View → Property Detail Panel → individual applications → Application Details
```

## Notes

* **This screen exists because JOP is 11 of the module's 26 services (42%)** and the underlying properties persist as standing records the company returns to repeatedly — not because every module needs a domain-specific register the way this one does. Compare Real Estate Rental Services (3 services) or Real Estate Transaction Services (2 services), neither of which gets an equivalent dedicated screen; the generic Applications list is sufficient there.
* Property Detail Panel's exact field-by-field content is **proposed**, not fully specified — needs refinement once actual JOP field data (from Service #1's own Required Information) is available to design against directly.
