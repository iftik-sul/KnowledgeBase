---
project: RERAN
module: real-estate-developer
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-19
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/payment-history.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - real-estate-developer
  - ui-spec
  - payments
---

# Screen: Payment History

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant (`navigation.md`, confirmed 2026-08-15; item added 2026-08-19).

A per-transaction record of every RERA service fee the developer company has paid: receipts, amounts, service references, and status.

> **New screen, added 2026-08-19.** RED had no consolidated payment view. Fee information existed only scattered across [application-details.md](application-details.md) (per-application fee status and payment reference), [notifications.md](notifications.md) (a payment-confirmation notification type), and [reports.md](reports.md) (Financial Reports, buried among revenue and sales figures). This screen follows the pattern established by Group C's [payment-history.md](../../financial-trust-institutions/ui/screens/payment-history.md), built for the identical payment model — per-transaction settlement through the shared platform gateway, no standing or pre-funded fee account (issue #58, confirmed 2026-08-15). It is not a straight copy: FTI's screen splits payer between institution and customer, which does not apply here — every RED payment is made by the developer company itself. RED's own axis is **payment timing**, drawn directly from the per-service audit in PR #59.

> **`contains_proposals: true`.** Two services (#25, #27) have no sourced fee amount — the audit marked them "unsourced, fee proposed." Everything else on this screen reflects sourced fee timing; those two rows' amounts do not, and should not be treated as confirmed until the client sources them.

## Purpose

Let any of the four Group B roles see what RERA fees the company has paid, when, for which application, and whether a payment succeeded, failed, or is under refund review — a reporting view over completed and attempted transactions, not an account to manage.

## Layout

* **Visible Sidebar:** Left Sidebar
* **Active Menu:** **Payment History**
* **Top Bar Title:** Payment History
* **Subtitle:** Every RERA service fee paid by the company, by transaction.
* **Search Bar:** Search by application, receipt or reference...

```
Top Bar
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
| Payments Failed | Count, current period — retryable from the originating application |
| Refunds Requested | Count, under review |
| Refunds Completed This Month | Count and amount |

No balance figure appears anywhere on this screen — there is no standing fee account to report. Selecting a card filters the table.

### Section 2 — Filters & Search

**Search by:** Application reference · Receipt reference · Service

**Filters**

* **Service** — all 27 Group B services
* **Status** — Successful · Failed · Refund Requested · Refunded (see [status-badges.md](../status-badges.md#payment-status))
* **Payment Timing** — Before Decision · After Decision · Dual-Stage
* **Date Range** — payment date
* **Amount Range**
* **Sort By** — Most recent (default) · Amount · Service

No Payer filter — unlike Group C's institution/customer split, every payment on this screen is made by the developer company. There is no second payer to distinguish.

### Section 3 — Payment History Table

| Column | Description |
| :---- | :---- |
| Receipt Reference | Payment receipt reference, downloadable |
| Application Reference | Links to [application-details.md](application-details.md) |
| Service | Which of the 27 |
| Timing | Before Decision · After Decision · Dual-Stage (Stage 1 / Stage 2) |
| Amount | Fee charged |
| Method | Card · bank transfer · USSD, via the shared platform gateway |
| Paid | Date and time |
| Status | Successful · Failed · Refund Requested · Refunded |
| Action | View Receipt · View Application |

**Row actions:** View Receipt · View Application

**Bulk actions:** Export Selected

**Which services appear on this table, and which don't — from the PR #59 per-service payment audit:**

| Group | Services | Appears here? |
| :---- | :---- | :---- |
| Fee, before decision | #1–7, #18, #19 | Yes — one row, Timing = Before Decision |
| Fee, after decision | #13, #15, #17, #22, #26 | Yes — one row, Timing = After Decision |
| Fee, dual-stage | #24 | Yes — **two rows**, same application reference, Timing = Dual-Stage, distinguished by a Stage 1 / Stage 2 label |
| No sourced RERA fee — escrow admin | #8, #9, #11, #20, #21 | No — these services charge no RERA fee; nothing to show |
| No sourced fee | #14, #16, #23 | No — same reason |
| Disbursement, not fee | #10, #12 | No — money movement here is a fund disbursement from escrow to the developer, not a RERA fee; tracked in [escrow-details.md](escrow-details.md) and [fund-release-request-details.md](fund-release-request-details.md) instead |
| Unsourced, fee proposed | #25, #27 | Yes, but flagged — Amount is marked *(proposed, not sourced)* on the row and in the receipt detail until the client confirms |

## Empty State

> No payments have been made yet. Payments made via the shared platform gateway — before RERA's decision for most services, at the point of decision for a smaller set — will appear here.

**Primary Button:** View Applications

## Reused Components

See [components.md](../components.md). Uses Left Sidebar, Top Bar, Search Bar, KPI Cards, Filter Bar, Data Table, Status Badges, Pagination, Empty State. Does not use a balance or account component — there is no balance to display.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. This is a read-only reporting screen for every Group B role — there is no role or scope restriction, and no action here initiates, retries, or reverses a payment. A failed payment is retried from the originating application itself, not from here.
2. Refund status is display-only. This screen shows whatever status the platform's refund mechanism produces, without asserting how that mechanism works.
3. Rows for Services #25 and #27 must visibly flag their Amount as proposed, not sourced, until the client confirms actual fee figures.

## User Flow

```
Dashboard
↓
Payment History
├─ View Receipt → Receipt Detail
└─ View Application → Application Details
```

## Notes

* **This is a reporting screen, not an account** — the same structural framing as Group C's `payment-history.md`. There is nothing to fund, no balance to project, and no low-balance state to warn about. Every figure on this screen is a fact about a transaction that already happened.
* **This screen is new, not a rebuild.** Unlike every other screen in this module, there was no source-material screen or role variant to retire here — RED's source material never described a consolidated payment view. It is built by adapting Group C's already-built equivalent to RED's own payment model.
* **Payment Timing (Before / After / Dual-Stage) replaces Group C's Payer (Institution / Customer) as this screen's second filter axis**, because the two modules diverge on that dimension: Group C's fee can be paid by either the institution or its customer depending on the service, while every Group B payment is made by the developer company itself. Timing — not payer — is what actually varies across RED's 27 services, per the PR #59 audit.
* **Service #24's dual-stage payment produces two table rows, not one.** This is a genuine structural difference from every other service on this screen and is called out explicitly rather than flattened into a single row with two amounts, since each stage has its own receipt, its own payment date, and potentially its own status.
* **Escrow account balances and fund-release disbursements are explicitly out of scope**, the same distinction [escrow-management.md](escrow-management.md) and [escrow-details.md](escrow-details.md) already draw for their own content. Services #10 and #12 move money between the developer and the escrow account; neither is a RERA service fee, so neither appears here.
* **Open — client confirmation needed on Services #25 and #27's fee amounts.** These are proposed pending source confirmation; see the audit in PR #59's description for the full per-service breakdown this screen's Timing categories are drawn from.
