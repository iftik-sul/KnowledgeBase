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
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - escrow
---

# Screen: Escrow Request Queue

**Access:** Any of the institution's four Group C roles — unified access, not scope-gated (`navigation.md`, confirmed 2026-08-14; extended to escrow-queue access specifically by `roles-and-responsibilities.md`, confirmed 2026-08-15).

Developer escrow requests arrive here from Group B, are assessed and certified, and are forwarded to the RERAN escrow department. Typically worked by the Account Trustee in practice, but not restricted to that role.

> **Corrected 2026-08-15.** This screen previously gated action behind an `escrow` permission scope, held by the Account Trustee. That scope is retired; any of the institution's four Group C roles may assess and certify an escrow request. See Role Variations, rewritten accordingly.

## Purpose

Give the institution a single queue of every developer escrow request awaiting the institution's certification, ordered by regulatory urgency, with enough context on each row to triage without opening it — typically worked by the Account Trustee, but reachable and actionable by any of the four roles.

## Layout

* **Visible Sidebar:** Institution Operations Sidebar
* **Active Menu:** **Escrow Requests** (carries a count badge)
* **Top Bar Title:** Escrow Requests
* **Subtitle:** Assess and certify developer escrow requests before regulatory audit.
* **Search Bar:** Search by request ID, project, developer or account...

```
Top Bar
↓
Institution Context Header
↓
Queue Summary Cards
↓
Filters & Search
↓
Escrow Requests Table
↓
Pagination
```

## Sections

### Section 1 — Queue Summary Cards

Six KPI cards. Selecting one filters the table.

| KPI | Description |
| :---- | :---- |
| Awaiting Assessment | Received, not yet opened |
| Under Assessment | Open with this institution |
| Information Requested | Queried back to the developer |
| Certified This Month | Forwarded to RERAN |
| Breaching SLA | Past the response window — see Notes |
| Trust Accounts Managed | Links to [trust-accounts.md](trust-accounts.md) |

### Section 2 — Filters & Search

**Search by:** Request ID · Project name · Project registration number · Developer · Trust account number

**Filters**

* **Request Type** — All · Account Activation · Account Transfer · Profit Withdrawal · Payment Release · Mortgage Deposit · Bank Guarantee Cancellation
* **Status** — the Escrow Request Status vocabulary in [status-badges.md](../status-badges.md#escrow-request-status)
* **Trust Account** — dropdown of accounts under management
* **Developer** — dropdown
* **SLA State** — All · Within window · Approaching breach · Breached
* **Received Date** — date range
* **Sort By** — SLA urgency (default) · Date received · Release amount · Developer

Default sort is SLA urgency rather than recency. The queue's failure mode is a request aging quietly, not a request being hard to find.

### Section 3 — Escrow Requests Table

| Column | Description |
| :---- | :---- |
| Request ID | Inbound reference from the developer module |
| Request Type | One of the six inbound types |
| Project | Development project |
| Developer | Originating institution |
| Trust Account | Account the request draws against |
| Requested Amount | Where the type carries one |
| Available Balance | Current balance on that trust account |
| Milestone | Construction milestone cited, where applicable |
| Received | Date and time the request arrived |
| SLA Remaining | Countdown — amber approaching, red breached |
| Status | See [status-badges.md](../status-badges.md#escrow-request-status) |
| Action | Assess |

Showing requested amount against available balance on the row is deliberate: a request exceeding its account's balance should be visible before it is opened.

**Row actions:** Assess · View Trust Account · View Project History · Download Request Pack

**Bulk actions:** Export Selected · Generate Queue Report

No bulk certify. Certification is a per-request regulated judgement and must not be available as a batch operation — see Notes.

## Empty State

**Message**

> No escrow requests are awaiting assessment. Requests routed from developers will appear here.

**Primary Button:** View Trust Accounts
**Secondary Button:** View Certified History

## Reused Components

See [components.md](../components.md). This screen uses the Institution Operations Sidebar, Top Bar, Institution Context Header, KPI Summary Cards, Filter Bar, Data Table, Status Badge, Pagination and Empty State.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. **Corrected 2026-08-15** — previously restricted Assess to users holding the `escrow` scope. Any of the institution's four roles may Assess; there is no scope check left to enforce.
2. A request whose trust account is Suspended or Flagged cannot be certified; the action is not rendered and the row carries the account's status.
3. A request cannot be certified by the user who last returned it to the developer, to preserve a second pair of eyes across the return cycle. **Unaffected by the 2026-08-15 correction** — this is a distinct return-cycle rule, not the retired scope-based maker≠checker restriction, and it stands on its own regardless of who holds what role.

## Role Variations

**Corrected 2026-08-15 — collapsed from a three-tier scope/role split to a description of typical practice.** Every institution user can Assess; the split below describes who typically does, not who is permitted to.

### Typically the Account Trustee

Full operation, in practice. Sees only accounts under this institution's trusteeship. Assess opens [escrow-request-details.md](escrow-request-details.md) in an editing state. Any other institution user has identical access, per the unified model.

### Institution Relationship Manager and Auditing Bureau Officer, in practice

Both roles can Assess like any other user, but their more typical use of this screen is oversight: the Institution Relationship Manager for a **Trustee Workload** card set (requests per user, average time to certify, breaches this period), the Auditing Bureau Officer for an **Audit Flags** filter surfacing requests where a certification was later queried by RERAN. Neither is a restriction — both roles retain the Assess action, and use it if a specific situation calls for it.

## User Flow

```
Dashboard
↓
Escrow Requests
├─ Assess → Escrow Request Details → Certify / Return / Request Information
├─ View Trust Account → Trust Accounts
└─ Download Request Pack → Documents
```

## Notes

* **SLA is confirmed.** Answer A6 (confirmed 2026-08-15, client decision) reads the source's split SLA — "waiting time 20 business hours; service delivery 13 business hours" — as queue-and-counterparty time versus RERAN processing time, meaning the trustee window is the waiting figure. This applies to every escrow service in Group B as well as Group C. The countdown column can be built directly against this reading.
* **No bulk certification.** Answer A3 (confirmed 2026-08-15) makes milestone certification a structured assessment with a solvency judgement inside it. A control that certifies twenty requests in one action is incompatible with that, and would make the audit timeline useless as evidence of judgement exercised.
* Requests originate in the developer module. This screen never creates one.
* The six request types come from the Group B escrow services (source rows 8–12, 20–21), not from the eighteen Group C services.
* Certified requests leave this queue and appear in the RERAN audit gate. They remain visible under a Certified filter for the institution's own record.
