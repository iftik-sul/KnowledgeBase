---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - escrow
---

# Screen: Trust Accounts

**Access:** Any of the institution's four Group C roles — unified access, not scope-gated (`navigation.md`, confirmed 2026-08-14).

The register of trust accounts under the institution's trusteeship: what exists, whether its periodic statement is current, and whether it carries an audit flag. Referenced by [escrow-request-queue.md](escrow-request-queue.md) (Trust Accounts Managed KPI, View Trust Account row action) and [compliance-reports.md](compliance-reports.md) (View Covered Accounts).

> **Corrected 2026-08-15.** This screen previously gated File Statement behind the `escrow` scope and Mark Under Audit behind the `audit` scope. Both scopes are retired; any of the institution's four Group C roles may file a statement or open/close an audit engagement.

## Purpose

The register of trust accounts, the object escrow requests draw against and compliance reports cover — the other two screens reference accounts; this screen is where an account itself lives.

## Layout

```
Top Bar
↓
Institution Context Header
↓
Register Summary Cards
↓
Filters & Search
↓
Trust Accounts Table
↓
Pagination
```

Selecting a row opens the **Account Detail Panel** (Section 4) rather than navigating to a separate screen.

## Sections

### Section 1 — Register Summary Cards

| KPI | Description |
| :---- | :---- |
| Active Accounts | Operating normally |
| Pending Activation | Registered, not yet active |
| Statement Overdue | Periodic audited statement not filed |
| Under Audit | Open audit engagement |
| Flagged | Irregularity raised — see Notes on how an account reaches this state |
| Suspended | Frozen by RERAN |

Selecting a card filters the table. Statuses match [status-badges.md](../status-badges.md#trust-account-status) exactly.

### Section 2 — Filters & Search

**Search by:** Account reference · Project · Developer

**Filters**

* **Status** — the Trust Account Status vocabulary
* **Project** — dropdown
* **Developer** — dropdown
* **Statement Filing State** — Current · Due Soon · Overdue
* **Sort By** — Statement due date (default) · Account reference · Balance

Default sort is statement due date, not recency — the register's failure mode is the same shape as the escrow queue's: an obligation aging unnoticed, this time a filing rather than a request.

### Section 3 — Trust Accounts Table

| Column | Description |
| :---- | :---- |
| Account Reference | Unique trust account identifier |
| Project | Development project |
| Developer | Owning institution (Group B) |
| Current Balance | Latest known balance |
| Statement Filed | Date of last filed periodic statement |
| Statement Due | Next filing date, with overdue treatment |
| Status | See [status-badges.md](../status-badges.md#trust-account-status) |
| Open Findings | Count, links to [compliance-reports.md](compliance-reports.md#section-4--findings-table) filtered to this account |
| Action | View |

**Row actions:** View · File Statement · Mark Under Audit · View Escrow Requests · Download Statement History

**Corrected 2026-08-15** — File Statement and Mark Under Audit are no longer restricted to a specific role; any institution user can take either action.

**Bulk actions:** Export Selected

### Section 4 — Account Detail Panel

Opened by View or by selecting a row; renders alongside the table rather than replacing it.

* **Account Particulars** — reference, project, developer, registration date, current balance.
* **Statement History** — every filed periodic statement, date, filer, and a link to the document.
* **Linked Escrow Requests** — every request against this account, most recent first, linking to [escrow-request-details.md](escrow-request-details.md).
* **Findings** — open and resolved, linking to [compliance-reports.md](compliance-reports.md#section-4--findings-table).
* **Audit History** — audit engagements opened and closed against this account, distinct from the findings they may have produced.

## Empty State

**Message**

> No trust accounts are registered under this institution's trusteeship yet. Accounts appear here once escrow activity for a project routes through this institution.

**Primary Button:** View Escrow Requests

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Information Cards, Status Badge, Document Uploader (File Statement), Pagination, Empty State.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. **Corrected 2026-08-15** — previously restricted File Statement to `escrow` and Mark Under Audit to `audit`. Both scopes are retired; any institution user may take either action.
2. **An account reaches Flagged only through a Material finding raised on [compliance-reports.md](compliance-reports.md#section-4--findings-table)** — there is no manual "Flag" action on this screen. This keeps the flag traceable to a specific finding rather than becoming a status anyone with access can set at will.
3. A Suspended account blocks new escrow requests being certified against it (enforced on [escrow-request-details.md](escrow-request-details.md#validation), not duplicated here) but remains visible and filterable in the register.
4. Statement filing does not require the account to be Active — a Statement Overdue account can still have its statement filed, which is the action that clears the overdue state.

## Role Variations

**Corrected 2026-08-15 — collapsed to typical-practice framing.** Every institution user can file a statement, view every account, and open or close an audit engagement. In practice: the Account Trustee typically maintains the register and files statements; the Auditing Bureau Officer typically opens and closes audit engagements; the Institution Relationship Manager typically uses this screen for oversight. None of this is an access restriction — any user can take any action described above.

## User Flow

```
Escrow Request Queue / Compliance Reports / Dashboard
↓
Trust Accounts
├─ View → Account Detail Panel
├─ File Statement → Document Uploader → Statement History (updated)
├─ Mark Under Audit → Status updated, Audit History entry created
└─ View Escrow Requests → Escrow Request Queue (filtered to this account)
```

## Notes

* **Account Detail Panel, not a fourth new screen file.** A trust account's detail did not need independent structure once statements, findings and escrow requests each already have their own home elsewhere.
* **How an account becomes Flagged is explicit** (Validation point 2) — this was implicit in [compliance-reports.md](compliance-reports.md)'s Notes and had no screen-side statement of the rule before.
* Account activation (Pending Activation → Active) is not specified anywhere in source — this document does not propose who triggers it or what evidence it requires.
* Statement filing frequency ("periodic") is not given a concrete cycle by any answer, matching the same gap [compliance-reports.md](compliance-reports.md#notes) flags for reporting cycle generally.
