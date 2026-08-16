---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/individual-user/payments.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - payments
---

# Screen: Payment History

**Access:** Any authenticated Individual User — own payments only.

## Purpose

A per-transaction record of every payment the account has made — receipts, amounts, service references, status. No standing account or wallet balance to show, since `payments.md` (C1) confirmed there is no separate Wallet Account mechanism anywhere in this module; every payment is a single, self-contained gateway transaction.

## Layout

```
Search / Filter
↓
Payment List
```

## Sections

### Section 1 — Search / Filter

By service, application reference, date, and payment status (Successful, Failed, Refund Requested).

### Section 2 — Payment List

Each row: application reference, service name, amount, date, status, and a downloadable Payment Receipt. For fee-bearing services, this is the only per-transaction artefact this module issues — no "Fee Balance" concept exists anywhere in this module at all, confirmed directly by the client (`open-questions.md` C2, `payments.md`'s Payment Artefacts section). *(Corrected 2026-08-16 — this section previously described an earlier, superseded reading of `payments.md`: that "Fee Balance" "most plausibly means a single-transaction line," an inference from before the client's direct confirmation that no such concept exists at all, not even that narrower reading. This screen was never updated when `payments.md` was corrected the same day; found during a full file-by-file UI audit.)*

## Empty State

**Message:**

> No payments yet.

## Reused Components

Search Bar, Status Badge (payment-specific: Successful, Failed, Refund Requested — not the Application/Complaint/PoA vocabularies).

## Validation

Every row here must correspond to an actual payment event — services with no fee (#17, #18, #33, #40, #42, #7's Owner/Entity-Amendment path) never generate a row, and services with after-decision payment timing (#28 and the relevant counter-channel paths) only generate a row once the payment is actually made, not at application submission.

## Access

No role variation.

## User Flow

```
Sidebar → Payment History → [search/filter] → [select row] → Application Details
```

## Notes

* Named `payment-history.md` rather than `payments.md` to avoid colliding with the module's own analysis document of the same name at `modules/individual-user/payments.md` — matching the disambiguation Group C already established for its own equivalent screen.
