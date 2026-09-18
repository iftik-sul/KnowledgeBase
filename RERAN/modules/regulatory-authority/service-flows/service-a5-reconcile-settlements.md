---
project: RERAN
module: regulatory-authority
type: service-flow
status: draft
contains_proposals: true
source_type: derived
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/roles-and-actions-analysis.md"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - finance
---

# Regulatory Authority Service A-5 — Reconcile Settlements

> **Back-office finance service.** Not a decision queue and not applicant-facing. It
> reconciles what the payment gateway actually collected against what was owed, and
> manages remittance. Adapted from the A-1 template as a periodic finance task.

## 1. Service Overview

**Reconcile Settlements** is the service through which RERA matches gateway receipts to
the fees that were owed, flags discrepancies, and remits collected funds to the
appropriate government accounts. It closes the money loop that A-4 (fee schedule) opens.

## 2. Purpose

Ensure every naira the platform collects is accounted for — matched to a service and
a published fee, discrepancies surfaced, and funds remitted correctly to state/federal
accounts.

## 3. Description

A Revenue & Finance Officer runs reconciliation over a period: the system matches
gateway settlement records against the fees owed (per the published schedule and the
services transacted), flags mismatches for investigation, and produces remittance
records for the funds due to each account.

## 4. Who Can Act

**Revenue & Finance Officer** (RA), under RBAC + MFA.

## 5. Trigger *(replaces "Entry Conditions")*

Periodic (e.g. daily/weekly settlement cycles) or on a gateway settlement event. No
queue and no applicant submission.

## 6. What the Officer Works With

- Gateway settlement records for the period.
- The fees owed for the services transacted in the period (per A-4's schedule).
- Prior reconciliation state and any open discrepancies.

## 7. Task Checklist *(replaces "Review Checklist")*

- Every gateway receipt maps to a transacted service and its owed fee.
- Collected amounts equal owed amounts; differences are flagged.
- Remittances are computed correctly per destination account.

## 8. Service Fee / 9. Payment Required

**N/A.** This service handles settlement of fees already collected; it does not charge
or collect a fee itself, and (per platform policy) holds no standing balance.

## 10. Authority & Access Control

- **Role:** Revenue & Finance Officer (RA).
- **Access control:** RBAC-gated + MFA.
- **Sub-system:** Revenue & Settlement Dashboard.

## 11. Expected Processing Time

N/A — a periodic batch task, not a timed application.

## 12. Processing Workflow

```
Officer runs reconciliation for a period  (RBAC + MFA)
        ↓
Match gateway receipts ↔ fees owed  (per A-4 schedule + transacted services)
        ↓
Flag discrepancies  → investigate / resolve
        ↓
Compute remittances per destination account
        ↓
Record reconciliation result + remittances
        ↓
Write to the audit trail
```

## 13. Status *(not the shared decision vocabulary)*

A reconciliation run is **Open**, **Balanced**, or **Discrepant** (with flagged items);
remittances are **Pending** or **Remitted**.

## 14. Possible Outcomes

- **Balanced** — receipts match owed; remittances recorded.
- **Discrepant** — mismatches flagged for investigation.

## 15. Cross-Module Dependencies

1. **A-4 Configure fee schedule** — reconciliation is meaningless without the
   authoritative "owed" amounts A-4 publishes.
2. **The shared payment gateway (Remita).** This service reads gateway settlement data;
   it depends on that integration.

## 16. Related Services

- **A-4 Configure fee schedule** — the upstream counterpart.
- **A-6 Provision & manage access (RBAC)** — must exist first.

## 17. UI Screens

- **Reconciliation dashboard** — run reconciliation, view matched vs discrepant, drill
  into flagged items.
- **Remittance view** — computed remittances per destination account and their status.
  Delivered as a **tab within the Reconciliation Dashboard**, not a separate screen.

## 18. API Requirements

- Fetch gateway settlement records for a period
- Fetch fees owed for transacted services
- Run reconciliation; flag discrepancies
- Compute and record remittances
- Write audit-log entry

## 19. Database Entities

- Reconciliation Run *(period, status)*
- Gateway Settlement Record *(read)*
- Fee-Owed Record *(derived from A-4 + transactions)*
- Remittance *(destination account, amount, status)*
- Staff User + Role + Permission *(RBAC)*
- Audit Log

## 20. Acceptance Criteria

- Only a Revenue & Finance Officer with MFA can run reconciliation.
- Every gateway receipt is matched to a transacted service and owed fee, or flagged.
- Discrepancies are surfaced, not silently absorbed.
- Remittances are computed per destination account and recorded.
- Every run and remittance is written to the audit trail.

## 21. Business Rules

1. Access is role-gated (Revenue & Finance Officer) + MFA.
2. No standing/pre-funded balances exist; this service reconciles per-transaction
   receipts only.
3. Discrepancies must be flagged and cannot be auto-cleared without a recorded reason.
4. All runs and remittances are recorded in the audit trail with the acting officer.
