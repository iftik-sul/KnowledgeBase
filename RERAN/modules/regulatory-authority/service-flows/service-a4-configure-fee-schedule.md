---
project: RERAN
module: regulatory-authority
type: service-flow
status: draft
contains_proposals: true
source_type: derived
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/roles-and-actions-analysis.md"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - configuration
---

# Regulatory Authority Service A-4 — Configure Fee Schedule

> **Back-office configuration service.** Not a decision queue and not applicant-facing:
> it is an internal action that maintains platform data every fee-bearing service
> depends on. The reviewer-decision sections of the A-1 template (queue, four outcomes,
> shared status vocabulary) do not apply and are adapted below.

## 1. Service Overview

**Configure Fee Schedule** is the service through which RERA maintains the fee and levy
schedule that every fee-bearing service on the platform reads at checkout. No external
service routes to it, but every fee-bearing front-office service depends on it: it is
the single source of truth for what each service costs.

## 2. Purpose

Keep the platform's fees and levies correct, current, and in one authoritative place —
so that pricing changes are made once and applied everywhere, and every fee charged is
traceable to a published schedule.

## 3. Description

A Revenue & Finance Officer creates or edits fee entries (per service, per levy) and
publishes the schedule. Published entries become the amounts front-office services
charge. Changes are versioned and recorded.

## 4. Who Can Act

**Revenue & Finance Officer** (RA), under RBAC + MFA.

## 5. Trigger *(replaces "Entry Conditions")*

Internal — a fee/levy policy change, or a new fee-bearing service that needs pricing.
There is no queue and no applicant submission.

## 6. What the Officer Works With

- The current published fee schedule (all entries).
- The catalogue of fee-bearing services that read the schedule.
- The proposed fee/levy definitions to add or change.

## 7. Task Checklist *(replaces "Review Checklist")*

- Each fee entry maps to a real service or levy.
- Amounts and effective dates are valid.
- No service that requires a fee is left without one.

## 8. Service Fee

**N/A.** This service sets fees; it does not charge one.

## 9. Payment Required

**N/A.**

## 10. Authority & Access Control

- **Role:** Revenue & Finance Officer (RA).
- **Access control:** RBAC-gated + MFA.
- **Sub-system:** Revenue & Settlement Dashboard.

## 11. Expected Processing Time

N/A — a configuration action, not a timed application.

## 12. Processing Workflow

```
Officer opens fee schedule  (RBAC + MFA)
        ↓
Create / edit fee or levy entries
        ↓
Validate (mapping, amounts, effective dates)
        ↓
Publish  → the new schedule becomes live for all fee-bearing services
        ↓
Version + record the change in the audit trail
```

## 13. Status *(not the shared decision vocabulary)*

Entries are **Draft** or **Published**; superseded entries are **Archived** with their
effective dates. No applicant-facing status.

## 14. Possible Outcomes

- **Published** — the schedule (or the changed entries) is live.
- **Reverted** — a change is rolled back to a prior published version.

## 15. Cross-Module Dependencies

1. **Every fee-bearing service reads this schedule.** A wrong or missing entry misprices
   or blocks checkout across the platform — this is the widest-blast-radius config
   surface in the Regulatory Authority.
2. **A-5 Reconcile settlements** reconciles gateway receipts against what this schedule
   said was owed.

## 16. Related Services

- **A-5 Reconcile settlements** — the downstream counterpart.
- **A-6 Provision & manage access (RBAC)** — must exist first.
- All fee-bearing front-office services (readers, not routed here).

## 17. UI Screens

- **Fee schedule editor** — list, create, edit, and publish fee/levy entries with
  effective dates and version history.

## 18. API Requirements

- Fetch current schedule (all entries, with versions)
- Create / edit fee or levy entry
- Publish schedule; revert to prior version
- Write audit-log entry

## 19. Database Entities

- Fee Schedule Entry *(service/levy, amount, effective dates, version, status)*
- Staff User + Role + Permission *(RBAC)*
- Audit Log

## 20. Acceptance Criteria

- Only a Revenue & Finance Officer with MFA can edit or publish the schedule.
- Every fee entry maps to a real service or levy with a valid amount and effective date.
- Published entries are what fee-bearing services charge at checkout.
- Every change is versioned and recorded in the audit trail.

## 21. Business Rules

1. Access is role-gated (Revenue & Finance Officer) + MFA.
2. This service is the sole source of truth for platform fees and levies.
3. Fee changes are versioned; superseded amounts are retained with their effective dates.
4. All changes are recorded in the audit trail with the acting officer.
