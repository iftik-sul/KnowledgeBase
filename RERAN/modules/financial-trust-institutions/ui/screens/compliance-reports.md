---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
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

**Roles:** Auditing Bureau Officer (`audit` scope) · Institution Relationship Manager (read)

Where the institution's approved auditor prepares and submits independent compliance reports to RERAN, and records escrow audit findings.

**This screen did not previously exist**, and the role's definition needed correcting first. `roles-and-responsibilities.md` proposes that the Auditing Bureau Officer performs internal certification of the Mortgage Officer's filings. Answer A1 supersedes that: internal certification is a `certify` permission scope on any delegated staff member, not this role. The Auditing Bureau Officer's actual work is what the user group structure describes — auditing developer escrow accounts and submitting independent compliance reports. That is what this screen serves.

## Purpose

Give the approved auditor a workspace for the two things the source says they produce: independent compliance reports filed with RERAN, and findings raised against trust accounts under the institution's trusteeship.

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
| Prepared By | Auditor |
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

A **Material** finding on an active trust account sets that account to Flagged — see [status-badges.md](../status-badges.md#trust-account-status). This is the mechanism behind the role's stated responsibility to "flag irregularities in escrow movement for regulatory attention."

### Section 5 — Report Composer

Opened by New Compliance Report. Structured, not a document upload — same reasoning as answer A3: a free-form attachment cannot be validated against KPI 8's data-integrity target or aggregated for FR-19 reporting.

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

1. Only the `audit` scope may create, edit or submit a report or finding.
2. **A user holding the `audit` scope may not also hold `escrow` or `certify` on the same institution.** The auditor cannot audit their own certifications, and the platform should prevent the combination at provisioning rather than rely on the institution's discretion.
3. A report covering a period cannot be submitted while a Material finding in that period is unresolved, unless the finding is explicitly carried into the report.
4. The auditor declaration is mandatory before submission.
5. Submitted reports are immutable. A correction is a new report referencing the original.

## Role Variations

### Auditing Bureau Officer

Full operation as described.

### Institution Relationship Manager

Read-only. Sees the obligation cards and both tables, and can see whether the institution is meeting its reporting duties — relevant because an overdue report bears on the institution's own approval renewal. Cannot open the composer, raise a finding, or see draft reports before filing. Draft audit work is not management's to read.

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

* **The role definition needs correcting.** `roles-and-responsibilities.md` §4 lists internal certification as this role's first responsibility. Answer A1 supersedes it. The roles document should be updated in the same pass — see PR description.
* **Reporting cycle is unresolved.** Answer A7 settles that the template is RERA-defined; it does not settle the frequency. The obligation cards are built against a configurable cycle.
* Answer B8 gives institutional approvals a validity term. An overdue compliance report should bear on renewal, and the Institution Profile screen should surface it. Whether RERAN actually gates renewal on reporting compliance is a client question.
* Escrow audit here concerns *developer* trust accounts under this institution's trusteeship. It is distinct from RERAN's own audit of the institution, which is a Group A function.
