---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-16
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

> **Replaces `settlement-account.md` entirely, 2026-08-15.** The previous screen described a standing pre-funded account — balance, top-up, ledger, low-balance alerting, periodic statements — debited after RERAN approval. That model is retired (`open-questions.md` B1, B11): Group C now pays per-transaction, via the shared platform gateway, upfront for Services #1 and #3–#11, and at the point of service, before RERAN's decision, for #12–#18. Service #2 carries no fee at all. There is no balance to display, nothing to fund, and no low-balance state. This screen is not the old screen corrected in place — it is a different screen for a different model, per `services-overview.md`'s Feature #8 (Payment History).
>
> **Corrected 2026-08-16.** A same-day correction on 2026-08-15 had added a third payment timing — Services #12/#18 paying at the counter *after* RERA's decision — along with an Awaiting Payment status, summary card, filter, and table treatment built around it. The client has since reviewed that #12/#18 exception directly, confirmed it was an artefact of the source's original physical-counter process rather than intentional design, and normalized both services to pay before RERA's decision, the same as #13–#17. Every addition made for that exception is removed below, since the scenario it existed to represent no longer occurs.

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

**Corrected 2026-08-16 — Awaiting Counter Payment card removed.** Added 2026-08-15 for Services #12/#18's then-sourced post-decision payment timing; that timing is retired, and with it the one summary figure that existed solely to track it.

### Section 2 — Filters & Search

**Search by:** Application reference · Receipt reference · Service

**Filters**

* **Service** — all eighteen
* **Status** — Successful · Failed · Refund Requested · Refunded
* **Payer** — Institution (Services #1, #3–#11) · Customer (Services #12–#18)
* **Date Range** — payment date
* **Amount Range**
* **Sort By** — Most recent (default) · Amount · Service

**Corrected 2026-08-16 — Payment Timing filter removed.** Added 2026-08-15 to distinguish #12/#18's post-decision counter payment from #13–#17's pre-decision one. With both services now normalized to the pre-decision pattern, every counter-paid service shares one timing, and the Payer filter (institution vs. customer) is sufficient again.

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
| Action | View Receipt · View Application |

**Corrected 2026-08-16 — Awaiting Payment status and blank-field rows removed.** Every row on this table now represents a payment that has actually happened, the same as before the 2026-08-15 exception was found; #12/#18 no longer produce a row with Receipt Reference, Method, and Paid left blank pending a later counter payment.

**Row actions:** View Receipt · View Application

**Bulk actions:** Export Selected

Service #2 (Cancellation) never appears in this table — it carries no fee at any point (`open-questions.md` B11), so it produces no payment record.

### Section 4 — Receipt Detail

Opened by View Receipt; renders alongside the table. Shows the full Payment Receipt: institution/customer details, service, amount, VAT (applied to all 18 services, per answer B7, confirmed 2026-08-15), payment method, gateway reference, and timestamp. Downloadable as PDF, matching the platform-wide Tax Invoice requirement (PRD).

## Empty State

**Message**

> No payments have been made yet. Payments made via the shared platform gateway — upfront for most services, at the point of service for title, ownership and contract transactions — will appear here.

**Primary Button:** View Applications

## Reused Components

See [components.md](../components.md). Uses the Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State. **Does not use the Balance Card component** — there is no balance to display; see Notes.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. This is a read-only reporting screen for every institution user — there is no role or scope restriction, and no action here initiates, retries, or reverses a payment. A failed payment is retried from the originating service request itself, not from here.
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
* **This screen's Awaiting Payment history is worth recording in full, since it changed direction twice in two days.** It was added 2026-08-15 after a fuller per-service audit found Services #12/#18 genuinely sourced a post-decision payment step this screen had no way to represent. It is removed again 2026-08-16 — not because that addition was wrong when made, but because the client has since decided to build #12/#18 differently from what the source described, normalizing their payment timing to match #13–#17.
