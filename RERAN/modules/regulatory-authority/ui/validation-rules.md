---
project: RERAN
module: regulatory-authority
type: ui-validation
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
tags:
  - regulatory-authority
  - ui-spec
  - validation
---

# Group A — Validation Rules

Cross-screen validation and guard rules for the back-office app. Screen specs reference
these rather than restating them.

## Access & identity

- **RBAC + MFA gate:** no screen can be *acted on* without the acting user holding the
  required role and an enrolled MFA session (A-6). Reaching a screen never implies
  permission to act (role × screen matrix §2).
- **Decision rights are per-screen:** only the item's primary decision role can enable a
  Decision Panel (Application Review, Case Workspace).

## Decision screens (A-1, A-2)

- A **reason is mandatory** for Request Additional Information, Return, and Reject;
  optional for Approve.
- An item cannot be decided while its **live registry checks** are unavailable.
- **Escrow items** cannot be decided until the FTI Account Trustee assessment is present.
- A **mortgage-registration approval** must be blocked unless the mortgage's own
  prerequisites are met (its approval is what validates RED #6's live dependency).
- Status transitions may only use the shared vocabulary (status-badges §1).

## Case screens (A-3)

- A case cannot be **closed** without a recorded outcome (judgment, dismissal, or
  withdrawal).
- Every session and interim decision must be recorded before the next step.

## Config screens (A-4, A-5, A-6)

- **Fee entries** must map to a real service/levy with a valid amount and effective date;
  no fee-bearing service may be left without an entry.
- **Reconciliation** discrepancies must be flagged; they cannot be auto-cleared without a
  recorded reason. No standing balances.
- **Accounts** cannot act until they have a role and enrolled MFA; suspend/deactivate
  withdraws access immediately.

## Universal

- Every state-changing action writes an **audit-trail entry** with the acting officer.
- Screens must not introduce local status words outside status-badges.md.

> **Proposed** — separation-of-duties rules (e.g. whether the officer who requested info
> may later approve the same item) are open (role × screen matrix §3); this file will
> encode them once the client confirms.
