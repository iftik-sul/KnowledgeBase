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

> **Replaces `settlement-account.md` entirely, 2026-08-15.** The previous screen described a standing pre-funded account — balance, top-up, ledger, low-balance alerting, periodic statements — debited after RERAN approval. That model is retired (`open-questions.md` B1, B11): Group C now pays per-transaction, via the shared platform gateway, upfront for Services #1 and #3–#11, at the point of service for #13–#17, and at the point of service after RERAN's decision for #12 and #18. Service #2 carries no fee at all. There is no balance to display, nothing to fund, and no low-balance state. This screen is not the old screen corrected in place — it is a different screen for a different model, per `services-overview.md`'s Feature #8 (Payment History).
>
> **Corrected 2026-08-15, second pass.** This screen previously described a two-way payer/timing split (institution upfront vs. customer at point of service) without distinguishing #12/#18's post-decision counter payment from #13–#17's pre-decision one — the same gap found and fixed in `payments.md`, `services-overview.md`, and several other files. Fixed throughout below.

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
| Payments Failed | Count, current period — retryable, pre-lodging (#1, #3–#17) |
| Awaiting Counter Payment | Count of approved #12/#18 applications not yet paid — **added 2026-08-15, second pass**, since this screen previously had no summary figure at all for the one genuinely outstanding-payment state left in the module |
| Refunds Requested | Count, under review |
| Refunds Completed This Month | Count and amount |

No balance figure appears anywhere on this screen — there is no account balance to report. Selecting a card filters the table.

### Section 2 — Filters & Search

**Search by:** Application reference · Receipt reference · Service

**Filters**

* **Service** — all eighteen
* **Status** — Successful · Failed · Refund Requested · Refunded · **Awaiting Payment** (added — #12/#18 only, see below)
* **Payer** — Institution (Services #1, #3–#11) · Customer (Services #12–#18)
* **Payment Timing** — **added 2026-08-15, second pass** — Upfront, before lodging (#1, #3–#11) · At counter, before decision (#13–#17) · At counter, after decision (#12, #18) · No fee (#2, excluded from this screen)
* **Date Range** — payment date
* **Amount Range**
* **Sort By** — Most recent (default) · Amount · Service

**Corrected 2026-08-15, second pass** — the Payer filter previously carried a note claiming it reflected "the two payer/timing models" in `payments.md`; `payments.md` now documents three timings, not two, so a separate Payment Timing filter is added rather than folding a third value into Payer, which describes *who* pays, not *when*.

### Section 3 — Payment History Table

| Column | Description |
| :---- | :---- |
| Receipt Reference | Payment Receipt reference, downloadable — blank for #12/#18 rows still awaiting payment |
| Application Reference | Links to [application-details.md](application-details.md) |
| Service | Which of the eighteen |
| Payer | Institution or customer, per the service's payer model |
| Amount | Fee charged |
| Method | Card · bank transfer · USSD, via the shared platform gateway |
| Paid | Date and time — blank for #12/#18 rows still awaiting payment |
| Status | Successful · Failed · Refund Requested · Refunded · **Awaiting Payment** |
| Action | View Receipt (where paid) · View Application |

**Added 2026-08-15, second pass — Awaiting Payment status and rows.** This table previously assumed every row represented a completed or failed transaction. For #12 and #18, an approved application sits with no payment record at all until the counter payment clears — this table needs a row for that state too, not just a gap where the record would eventually appear. The row is populated once RERA approves (application reference, service, amount owed) with Receipt Reference, Method and Paid left blank until the counter payment happens.

**Row actions:** View Receipt (where paid) · View Application

**Bulk actions:** Export Selected

Service #2 (Cancellation) never appears in this table — it carries no fee at any point (`open-questions.md` B11), so it produces no payment record.

### Section 4 — Receipt Detail

Opened by View Receipt; renders alongside the table. Shows the full Payment Receipt: institution/customer details, service, amount, VAT (applied to all 18 services, per answer B7, confirmed 2026-08-15), payment method, gateway reference, and timestamp. Downloadable as PDF, matching the platform-wide Tax Invoice requirement (PRD). **Not available for a row still Awaiting Payment** — there is no receipt to show until the payment happens.

## Empty State

**Message**

> No payments have been made yet. Payments made via the shared platform gateway — upfront for most services, at the point of service (before or after RERA's decision, depending on the service) for title, ownership and contract transactions — will appear here.

**Primary Button:** View Applications

## Reused Components

See [components.md](../components.md). Uses the Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State. **Does not use the Balance Card component** — there is no balance to display; see Notes.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. This is a read-only reporting screen for every institution user — there is no role or scope restriction, and no action here initiates, retries, or reverses a payment. **Corrected 2026-08-15, second pass** — this rule previously said a failed payment "is retried from the service request itself, not from here," which is accurate for #1 and #3–#17's digital checkout, but doesn't describe #12/#18 at all: their payment is a physical counter transaction with no online "service request" retry step. Nothing on this screen or elsewhere in the module currently specifies what happens if a #12/#18 customer's counter payment attempt fails or they never return — flagged in `payments.md`'s To Confirm — Summary and `validation-rules.md`'s Payments section, not resolved here.
2. Refund status is display-only. Which route a refund follows — the platform's public refund service or an institution-specific process — is unresolved (`open-questions.md` B10, superseded; `payments.md`'s To Confirm — Summary); this screen shows whatever status the eventual mechanism produces, without asserting the mechanism itself.
3. **Added 2026-08-15, second pass.** Awaiting Payment rows (#12/#18) update in place once the counter payment is recorded — from wherever that recording happens (Trustee Centre / Land Department operator entry, most likely) — rather than a new row being created. The application reference is the same row throughout.

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

* **This is a reporting screen, not an account.** The single biggest structural difference from the retired `settlement-account.md`: there is nothing to fund, no balance to project, and no low-balance state to warn about. Every figure on this screen is a fact about a transaction that already happened — or, for #12/#18 specifically, one genuinely still pending — not a position that needs managing.
* **What happens to the fee on a rejected application is unresolved** (`payments.md`'s To Confirm — Summary, item 1). This screen shows the payment as Successful regardless of the application's own outcome, since the payment itself settled; whether a rejected application's fee should route to a distinct status here is not decided. **This doesn't apply to #12/#18** — a rejection there happens before any payment is collected, so there's no fee to route anywhere.
* **Fee amounts are configuration, not sourced figures** (`open-questions.md` B5). This screen displays whatever the fee-schedule engine actually charged for a given transaction, not a fixed number.
* Group B developers settle escrow-related fees through their own module; this screen covers only the institution's own Group C fees.
