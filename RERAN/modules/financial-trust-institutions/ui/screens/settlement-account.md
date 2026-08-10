---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
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

# Screen: Settlement Account

**Roles:** Institution Relationship Manager (`settlement` scope) · Mortgage Officer (read)

The standing pre-funded account from which Group C fees are deducted after approval.

## Purpose

Show the institution's settlement position, let it be funded, and make visible the one thing that can strand an approved transaction: an approval that has passed RERAN's audit but cannot be settled.

Answer B1 establishes the model. Fees are **not** paid at submission as in the individual-user module — they are deducted from a held balance after approval. The evidence is that source rows 30–37 list *"Fee balance"* among the issued deliverables, and a balance is not a receipt. Answer B9 follows: fee balance and payment receipt are two artefacts, and both appear here.

## Layout

* **Visible Sidebar:** Institution Operations Sidebar
* **Active Menu:** **Settlement Account**
* **Top Bar Title:** Settlement Account
* **Subtitle:** Fund the account and settle approved transactions.
* **Search Bar:** Search ledger by application, receipt or reference...
* **Page Actions:** Fund Account · Export Statement

The Institution Context Header is suppressed — its settlement figure is this screen's subject.

```
Top Bar
↓
Balance Summary
↓
Awaiting Settlement
↓
Tabs: Ledger | Funding History | Statements
↓
Filters & Search
↓
Table
↓
Pagination
```

**Awaiting Settlement sits above the ledger, not below it.** The ledger is history; awaiting settlement is work with a 30-day fuse on it.

## Sections

### Section 1 — Balance Summary

Uses the Balance Card component.

| Figure | Description |
| :---- | :---- |
| Available Balance | Funds available to settle |
| Committed | Fees on approved transactions not yet settled |
| Projected Balance | Available less committed |
| Low Balance State | Neutral, warning or error against the configured threshold |
| Last Funded | Date and amount |

Projected balance is the operative number. Available balance alone tells an institution nothing about whether its approved pipeline can clear.

### Section 2 — Awaiting Settlement

Approved transactions with fees not yet deducted.

| Column | Description |
| :---- | :---- |
| Application Reference | Links to [application-details.md](application-details.md) |
| Service | Which of the eighteen |
| Approved | Date RERAN approved |
| Fee Due | Amount |
| Expires | 30-day countdown per answer B3 — amber at 7 days, red at 24 hours |
| Status | Approved — Awaiting Payment, or Approval Expired |
| Action | Settle · Settle All |

Where the projected balance cannot cover everything listed, the section carries a warning stating the shortfall and the earliest expiry it would affect. An institution should learn it is about to lose an approval before it loses it, not after.

**Expired rows remain visible** under an Expired filter, with a Resubmit action routing to a new service request. They are not silently removed — an expired approval is a fee already earned and a transaction still undone.

### Section 3 — Ledger Tab

| Column | Description |
| :---- | :---- |
| Date | Transaction timestamp |
| Description | Charge, credit, funding or reversal |
| Application | Linked application reference, where applicable |
| Service | Which of the eighteen |
| Charge | Debit amount |
| Credit | Credit amount |
| Balance After | Running balance — the *fee balance* artefact |
| Receipt | Payment receipt reference, downloadable |

The last two columns are answer B9 made concrete: **Balance After** is the fee balance, **Receipt** is the payment receipt. Different columns because they are different artefacts.

**Filters:** Transaction type · Service · Date range · Amount range · Application reference

### Section 4 — Funding History Tab

| Column | Description |
| :---- | :---- |
| Date | Funding date |
| Method | Bank transfer or payment gateway |
| Reference | Institution funding reference |
| Amount | Credited |
| Authorised By | User who initiated |
| Status | Pending · Cleared · Failed |

### Section 5 — Statements Tab

Periodic statements, exportable. Per FR-19, exports are available as PDF and Excel.

### Section 6 — Fund Account

Opened by the page action. Per answer B2:

* **Bank transfer** — displays the institution's unique funding reference and destination details. For large amounts.
* **Payment gateway** — for smaller top-ups.

Shows the shortfall against committed fees as a suggested amount. Recommend this uses the same wallet primitive proposed for individuals in `proposed-services.md` P-22, with two account types rather than two builds.

## Empty State

**Message**

> This settlement account has not been funded. Group C fees are deducted from a standing balance after RERAN approval, so the account must hold funds before approved transactions can complete.

**Primary Button:** Fund Account
**Secondary Button:** How Settlement Works

The empty state explains the payment model, because the model differs from every other module in the platform and this screen is where an institution first meets it.

## Reused Components

See [components.md](../components.md). Uses the Institution Operations Sidebar, Top Bar, Balance Card, Ledger Table, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination, Empty State and Buttons.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. Only the `settlement` scope may fund the account or settle a transaction. Read-only roles see balances and ledger but no actions.
2. The account may not go negative. Settle is not rendered where the available balance is insufficient; the row instead offers Fund Account (answer B4).
3. Settle All settles in expiry order, nearest first, and stops when the balance is exhausted rather than failing the batch.
4. Funding is not reversible from this screen. A credit correction is a RERAN-side action.
5. Ledger entries are immutable. A correction is a reversal entry, never an edit.

## Role Variations

### Institution Relationship Manager

Full operation. Sees institution-wide committed fees across all users.

### Mortgage Officer

Read-only, and filtered: sees the balance summary and only the ledger entries and awaiting-settlement rows arising from their own filings. The reason is practical rather than confidential — the officer needs to know whether their own approved transaction can clear, and does not need the institution's whole financial position to answer that.

No Fund Account action. Where their own transaction cannot settle, they see the shortfall and a prompt to contact the Relationship Manager.

### Auditing Bureau Officer

Read-only, institution-wide: sees the full Balance Summary and Ledger, not filtered to any one officer's filings — the same institution-wide read this role has on Applications and Documents, for the same audit reason. No Fund Account or Settle action, and no Funding History tab access beyond viewing; funding authorisation is not part of an audit function.

> **Added in the issue #27 navigation cross-check.** Both `navigation.md` and this screen's entry in `README.md`'s Role × Screen Matrix grant this role Read access, but the previous version of this file only documented Institution Relationship Manager and Mortgage Officer. The role was reachable per the matrices and had nothing to see when it got here — this closes that gap rather than leaving the matrix as the only source of truth for what the role can do.

## User Flow

```
Dashboard
↓
Settlement Account
├─ Fund Account → Funding Method → Confirmation → Funding History
├─ Settle → Confirmation → Receipt → Application Details (Completed)
├─ Settle All → Batch Confirmation → Ledger
├─ Resubmit (expired) → Service Request
└─ Export Statement → Statements
```

## Notes

* **Fee amounts are unknown.** Answer B5 is the one question in twenty-three that is genuinely client data. The schedule is configuration under FR-16, so this screen is built against a configurable schedule and displays whatever it returns.
* **The 30-day expiry is proposed, not sourced.** Answer B3 argues the principle — approvals must expire, because an indefinite hold accumulates approved-but-unregistered interests that are invisible to a searcher, which is the fraud surface the platform exists to close. The duration is ours.
* **This subsystem is unestimated.** Balance, funding, ledger, alerting and statements appear in no source document. Answer B1 flags this as the commercial item to raise — not the mechanism, which the source supports, but the build cost of it.
* The low-balance threshold is a per-institution setting, configured on [institution-profile.md](institution-profile.md).
* Group B developers settle escrow-related fees through their own module. This account covers the institution's own Group C fees only.
