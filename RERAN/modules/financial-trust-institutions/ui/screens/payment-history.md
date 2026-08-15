---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - payments
---

# Screen: Payment History

**Access:** Any of the institution's four Group C roles — unified access, not scope-gated (`navigation.md`, confirmed 2026-08-14).

A per-transaction record of every payment the institution has made: receipts, amounts, service references, and status.

> **Replaces `settlement-account.md` entirely, 2026-08-15.** The previous screen described a standing pre-funded account — balance, top-up, ledger, low-balance alerting, periodic statements — debited after RERAN approval. That model is retired (`open-questions.md` B1, B11): Group C now pays per-transaction, via the shared platform gateway, upfront for Services #1 and #3–#11, at the point of service for #12–#18, and not at all for Service #2. There is no balance to display, nothing to fund, and no low-balance state. This screen is not the old screen corrected in place — it is a different screen for a different model, per `services-overview.md`'s Feature #8 (Payment History).

## Purpose

Let any institution user see what has been paid, when, for which application, and whether a payment succeeded, failed, or is under refund review — a reporting view over completed and attempted transactions, not an account to manage.

## Layout

* **Visible Sidebar:** Institution Operations Sidebar
* **Active Menu:** **Payment History**
* **Top Bar Title:** Payment History
* **Subtitle:** Every payment made by the institution, by transaction.
* **Search Bar:** Search by application, receipt or reference...

```
Top Bar
↓
Institution Context Header
↓
Payment Summary Cards
↓
Filters & Search
↓
Payment History Table
↓
Pagination
```

## Sections

### Section 1 — Payment Summary Cards

| KPI | Description |
| :---- | :---- |
| Paid This Month | Total amount, successful payments |
| Payments Failed | Count, current period — retryable, pre-lodging |
| Refunds Requested | Count, under review |
| Refunds Completed This Month | Count and amount |

No balance figure appears anywhere on this screen — there is no account balance to report. Selecting a card filters the table.

### Section 2 — Filters & Search

**Search by:** Application reference · Receipt reference · Service

**Filters**

* **Service** — all eighteen
* **Status** — Successful · Failed · Refund Requested · Refunded
* **Payer** — Institution (Services #1, #3–#11) · Customer (Services #12–#18) — reflecting the two payer/timing models in [payments.md](../../payments.md)
* **Date Range** — payment date
* **Amount Range**
* **Sort By** — Most recent (default) · Amount · Service

### Section 3 — Payment History Table

| Column | Description |
| :---- | :---- |
| Receipt Reference | Payment Receipt reference, downloadable |
| Application Reference | Links to [application-details.md](application-details.md) |
| Service | Which of the eighteen |
| Payer | Institution or customer, per the service's payer model |
| Amount | Fee charged |
| Method | Card · bank transfer · USSD, via the shared platform gateway |
| Paid | Date and time |
| Status | Successful · Failed · Refund Requested · Refunded |
| Action | View Receipt |

**Row actions:** View Receipt · View Application

**Bulk actions:** Export Selected

Service #2 (Cancellation) never appears in this table — it carries no fee at any point (`open-questions.md` B11), so it produces no payment record.

### Section 4 — Receipt Detail

Opened by View Receipt; renders alongside the table. Shows the full Payment Receipt: institution/customer details, service, amount, VAT (applied to all 18 services, per answer B7, confirmed 2026-08-15), payment method, gateway reference, and timestamp. Downloadable as PDF, matching the platform-wide Tax Invoice requirement (PRD).

## Empty State

**Message**

> No payments have been made yet. Payments made via the shared platform gateway — upfront for most services, at the point of service for title and ownership transactions — will appear here.

**Primary Button:** View Applications

## Reused Components

See [components.md](../components.md). Uses the Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State. **Does not use the Balance Card component** — there is no balance to display; see Notes.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. This is a read-only reporting screen for every institution user — there is no role or scope restriction, and no action here initiates, retries, or reverses a payment. A failed payment is retried from the service request itself, not from here (see [payments.md](../../payments.md#failed-and-reversed-payments)).
2. Refund status is display-only. Which route a refund follows — the platform's public refund service or an institution-specific process — is unresolved (`open-questions.md` B10, superseded; `payments.md`'s To Confirm — Summary); this screen shows whatever status the eventual mechanism produces, without asserting the mechanism itself.

## Role Variations

None. Every institution user sees the same institution-wide payment history, with no role-based partitioning.

## User Flow

```
Dashboard
↓
Payment History
├─ View Receipt → Receipt Detail
└─ View Application → Application Details
```

## Notes

* **This is a reporting screen, not an account.** The single biggest structural difference from the retired `settlement-account.md`: there is nothing to fund, no balance to project, and no low-balance state to warn about. Every figure on this screen is a fact about a transaction that already happened, not a position that needs managing.
* **What happens to the fee on a rejected application is unresolved** (`payments.md`'s To Confirm — Summary, item 1). This screen shows the payment as Successful regardless of the application's own outcome, since the payment itself settled; whether a rejected application's fee should route to a distinct status here is not decided.
* **Fee amounts are configuration, not sourced figures** (`open-questions.md` B5). This screen displays whatever the fee-schedule engine actually charged for a given transaction, not a fixed number.
* Group B developers settle escrow-related fees through their own module; this screen covers only the institution's own Group C fees.
