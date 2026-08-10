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
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - escrow
---

# Screen: Escrow Request Queue

**Roles:** Account Trustee (`escrow` scope) · Institution Relationship Manager (read) · Auditing Bureau Officer (read)

The Account Trustee's primary workspace. Developer escrow requests arrive here from Group B, are assessed and certified, and are forwarded to the RERAN escrow department.

**This screen did not previously exist.** The Account Trustee held no screen in the module despite owning six inbound request types. Answer A2 confirms from source rows 8–12 that the Trustee acts *inside* the platform — studying capability, uploading documents and sending them on — rather than working externally and recording an outcome.

## Purpose

Give the Account Trustee a single queue of every developer escrow request awaiting the institution's certification, ordered by regulatory urgency, with enough context on each row to triage without opening it.

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

1. Only users holding the `escrow` scope see Assess. Read-only roles see View.
2. A request whose trust account is Suspended or Flagged cannot be certified; the action is not rendered and the row carries the account's status.
3. A request cannot be certified by the user who last returned it to the developer, to preserve a second pair of eyes across the return cycle.

## Role Variations

### Account Trustee

Full operation. Sees only accounts under this institution's trusteeship. Assess opens [escrow-request-details.md](escrow-request-details.md) in an editing state.

### Institution Relationship Manager

Read-only, institution-wide. Gains a **Trustee Workload** card set — requests per trustee, average time to certify, breaches this period — in place of the Assess action. This is oversight of the function, not participation in it.

### Auditing Bureau Officer

Read-only. Gains an **Audit Flags** filter surfacing requests where a certification was later queried by RERAN, since those are the population an escrow audit examines. No Assess action — the auditor does not certify what they audit.

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

* **SLA is unresolved.** Answer A6 proposes reading the source's split SLA — "waiting time 20 business hours; service delivery 13 business hours" — as queue-and-counterparty time versus RERAN processing time, which would make the trustee window the waiting figure. That reading is an inference and sets the SLA for every escrow service in Group B as well as Group C. The countdown column is built; the number behind it needs the client.
* **No bulk certification.** Answer A3 makes milestone certification a structured assessment with a solvency judgement inside it. A control that certifies twenty requests in one action is incompatible with that, and would make the audit timeline useless as evidence of judgement exercised.
* Requests originate in the developer module. This screen never creates one.
* The six request types come from the Group B escrow services (source rows 8–12, 20–21), not from the eighteen Group C services.
* Certified requests leave this queue and appear in the RERAN audit gate. They remain visible under a Certified filter for the institution's own record.
