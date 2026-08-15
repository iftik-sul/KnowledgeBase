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
  - audit
---

# Screen: Compliance Reports

**Access:** Any of the institution's four Group C roles — unified access, not scope-gated (`navigation.md`, confirmed 2026-08-14).

Where the institution's approved auditor prepares and submits independent compliance reports to RERAN, and records escrow audit findings. Typically worked by the Auditing Bureau Officer in practice.

> **Corrected 2026-08-15.** This screen previously gated report/finding creation behind an `audit` permission scope, and enforced an audit-exclusivity rule barring a user holding `audit` from also holding `escrow` or `certify`. Both are retired. Any of the institution's four Group C roles may create, edit or submit a report or finding; there is no scope combination to prohibit, since there are no scopes left.

## Purpose

Give the institution a workspace for the two things the source says an approved auditor produces: independent compliance reports filed with RERAN, and findings raised against trust accounts under the institution's trusteeship.

## Layout

* **Visible Sidebar:** Institution Operations Sidebar
* **Active Menu:** **Compliance Reports**
* **Top Bar Title:** Compliance Reports
* **Subtitle:** Prepare independent compliance reports and record escrow audit findings.
* **Search Bar:** Search by report reference, trust account or project...
* **Page Actions:** New Compliance Report · Raise Finding

```
Top Bar
↓
Institution Context Header
↓
Reporting Obligations
↓
Tabs: Reports | Findings
↓
Filters & Search
↓
Reports Table / Findings Table
↓
Pagination
```

## Sections

### Section 1 — Reporting Obligations

A banded card set showing what is owed and when. Answer A7 establishes that reports follow a RERA-defined template on a defined cycle, so the obligation is knowable in advance and should be shown rather than remembered.

| Card | Description |
| :---- | :---- |
| Reports Due | Obligations with a filing date in the current period |
| Overdue | Past filing date — error treatment |
| Accounts Statement Overdue | Trust accounts whose periodic statement is outstanding |
| Open Findings | Raised, not yet resolved |
| Findings Escalated to RERAN | Referred for regulatory attention |

### Section 2 — Tabs

**Reports** and **Findings** are different objects with different lifecycles and are separated rather than merged into one list.

### Section 3 — Reports Table

| Column | Description |
| :---- | :---- |
| Report Reference | System-issued |
| Report Type | Periodic escrow audit · Trust account statement · Ad hoc compliance report |
| Period Covered | Reporting period |
| Scope | Trust accounts or projects covered |
| Prepared By | Institution user who prepared it |
| Filing Deadline | With overdue treatment |
| Submitted | Date filed with RERAN |
| Status | Draft · Submitted · Under RERAN Review · Accepted · Returned |
| Action | Open |

**Row actions:** Open · Download · View Covered Accounts · Withdraw (drafts only)

### Section 4 — Findings Table

| Column | Description |
| :---- | :---- |
| Finding Reference | System-issued |
| Trust Account | Account the finding concerns |
| Project | Associated development project |
| Category | Irregular movement · Milestone evidence · Documentation · Balance discrepancy · Other |
| Severity | Observation · Concern · Material |
| Raised | Date |
| Escalated | Whether referred to RERAN |
| Status | Open · Under Response · Resolved · Escalated |
| Action | Open |

A **Material** finding on an active trust account sets that account to Flagged — see [status-badges.md](../status-badges.md#trust-account-status).

### Section 5 — Report Composer

Opened by New Compliance Report. Structured, not a document upload — same reasoning as answer A3 (confirmed 2026-08-15): a free-form attachment cannot be validated against KPI 8's data-integrity target or aggregated for FR-19 reporting.

* **Header** — report type, period, scope selection from trust accounts under management
* **Account Sections** — one per covered account: opening balance, movements, closing balance, statement reconciliation state
* **Findings** — attach findings raised in the period
* **Auditor Declaration** — independence confirmation and signature block
* **Attachments** — supporting working papers
* **Review & Submit** — completeness check before filing

## Empty State

**Message**

> No compliance reports have been prepared. Reports filed with RERAN and findings raised against trust accounts will appear here.

**Primary Button:** New Compliance Report
**Secondary Button:** View Trust Accounts

## Reused Components

See [components.md](../components.md). Uses the Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Document Uploader, Audit Timeline, Pagination and Empty State.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. **Corrected 2026-08-15** — previously restricted to the `audit` scope. Any institution user may create, edit or submit a report or finding.
2. **Removed 2026-08-15.** This screen previously enforced an audit-exclusivity rule — a user holding `audit` could not also hold `escrow` or `certify` — at provisioning. Permission scopes are retired module-wide; there is nothing left to exclude.
3. A report covering a period cannot be submitted while a Material finding in that period is unresolved, unless the finding is explicitly carried into the report.
4. The auditor declaration is mandatory before submission.
5. Submitted reports are immutable. A correction is a new report referencing the original.

## Role Variations

**Corrected 2026-08-15 — collapsed to typical-practice framing.** Every institution user can create, edit and submit a report or finding. In practice, the Auditing Bureau Officer typically does this work; the Institution Relationship Manager typically uses this screen for oversight — seeing the obligation cards and both tables, and whether the institution is meeting its reporting duties — but retains the same access as any other user if a specific situation calls for it.

## User Flow

```
Dashboard
↓
Compliance Reports
├─ New Compliance Report → Report Composer → Review & Submit → Submitted
├─ Raise Finding → Finding Detail → Open / Escalate
├─ Open (report) → Report Detail → Download / Withdraw
└─ View Covered Accounts → Trust Accounts
```

## Notes

* **Reporting cycle is unresolved.** Answer A7 settles that the template is RERA-defined; it does not settle the frequency. The obligation cards are built against a configurable cycle.
* Answer B8 (confirmed 2026-08-15) gives institutional approvals a renewing, per-approval-term validity. An overdue compliance report should bear on renewal, and the Institution Profile screen should surface it. Whether RERAN actually gates renewal on reporting compliance is a client question.
* Escrow audit here concerns *developer* trust accounts under this institution's trusteeship. It is distinct from RERAN's own audit of the institution, which is a Group A function.
* **The audit-exclusivity rule was never sourced**, and is now moot rather than merely unenforced — there is no permission-scope model left for it to constrain.
