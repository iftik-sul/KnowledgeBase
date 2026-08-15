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

# Screen: Escrow Request Details

**Access:** Any of the institution's four Group C roles — unified access, not scope-gated (`navigation.md`, confirmed 2026-08-14). Typically worked by the Account Trustee in practice.

Referenced by [escrow-request-queue.md](escrow-request-queue.md)'s Assess action.

> **Corrected 2026-08-15.** This screen previously gated the Decision Panel and Execute Transfer behind an `escrow` permission scope. That scope is retired; any of the institution's four Group C roles may assess, certify, and execute a transfer.

## Purpose

Give whoever is working an escrow request everything needed to reach a certification decision: the request's own context, a solvency assessment, and — per answer A3, confirmed 2026-08-15 — a structured milestone certification rather than a document upload standing in for one.

## Layout

```
Top Bar
↓
Header
↓
Request Context
↓
Solvency Assessment
↓
Milestone Certification
↓
Documents
↓
Decision Panel (or Execute Transfer, once RERAN Approved)
↓
Audit Timeline
```

## Sections

### Section 1 — Header

Request ID, request type (one of the six inbound types), project, developer, trust account, requested amount against available balance, SLA countdown, status badge — see [status-badges.md](../status-badges.md#escrow-request-status).

### Section 2 — Request Context

Everything routed from the developer module: the milestone or event cited, the developer's own supporting materials, and prior requests against the same trust account for comparison. Read-only — this is what is being assessed, not edited.

### Section 3 — Solvency Assessment

The judgement answer A2 says happens *inside* the platform, not externally with only an outcome recorded:

* **Project Financial Position** — narrative assessment field, structured minimums TBD (see Notes).
* **Requested vs. Available** — requested amount shown directly against the trust account's current balance (also visible on the queue row, repeated here at decision time because it is the single fact most likely to drive a Return).
* **Solvency Notes** — free text, required before the Decision Panel accepts a Certify action.

### Section 4 — Milestone Certification

Structured, per answer A3 (confirmed 2026-08-15) — a free-form certification letter can be neither validated against KPI 8's data-integrity target nor aggregated for FR-19 reporting:

| Field | Description |
| :---- | :---- |
| Milestone Reference | Which construction milestone this certifies |
| Percentage Complete | Assessed completion |
| Valuation of Works Executed | Assessed value of work completed to date |
| Amount Certified | What is being certified for release — validated against Available Balance, see Validation |
| Variance Against Previous Certificate | Difference from the last certification on this trust account, computed and shown, not entered |
| Certifier Declaration | A standard attestation affirmed before the record can be certified |
| Attachments | Supporting evidence for the assessment — a supplement to the structured fields above, not a replacement for them |

### Section 5 — Documents

Supporting assessment materials and anything the developer attached, using [components.md](../components.md#document-uploader) and [components.md](../components.md#document-reference-picker) where a document already exists in the repository.

### Section 6 — Decision Panel

See [components.md](../components.md#decision-panel), extended for this screen with the structured fields above rather than a bare reason box:

* **Certify** — forwards to RERAN escrow audit. Requires Section 4 fully completed and the Section 3 solvency notes populated.
* **Return** — sends back to the developer. Reason mandatory (FR-04).
* **Request Information** — queries the developer without closing the request. Reason mandatory, and the request remains in the queue at Information Requested status rather than leaving it.

### Section 6a — Execute Transfer

Appears in place of the Decision Panel once status reaches **RERAN Approved** — the request has passed both gates and the only step left is moving the funds. This is a distinct action from Certify: certifying forwards a recommendation to RERAN's escrow audit; executing moves money, only after RERAN's own approval is on record.

* **Execute Transfer** — confirms the transfer has been made against the trust account. Requires a settlement/transfer reference. Moves status to **Executed** (see [status-badges.md](../status-badges.md#escrow-request-status)) and notifies the developer.
* Not available before RERAN Approved, and not reversible from this screen — a correction after execution is a new request, not an edit to this one.

No bulk equivalent exists anywhere this decision could be made — see [escrow-request-queue.md](escrow-request-queue.md#section-3--escrow-requests-table).

### Section 7 — Audit Timeline

Full history: who assessed, what was queried, what was certified or returned and why, per [components.md](../components.md#audit-timeline).

## Empty State

Not applicable — this screen only renders for an existing request. Reaching it without one:

> This escrow request could not be found, or you do not have access to it.

**Primary Button:** Back to Escrow Requests

## Reused Components

See [components.md](../components.md). Uses Top Bar, Information Cards, Document Uploader, Document Reference Picker, Decision Panel, Status Badge, Audit Timeline, Buttons. Execute Transfer is not a defined shared component — it is specific to this screen and this status.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. **Amount Certified cannot exceed the trust account's Available Balance.** This is the concrete form of the "requested amount against available balance" visibility the queue screen already surfaces — here it is enforced, not just shown.
2. Certify is not available where the trust account is Suspended or Flagged (mirrors [escrow-request-queue.md](escrow-request-queue.md#validation) rule 2) — the panel shows the account's status in place of the action.
3. A request cannot be certified by the user who last returned it to the developer on this same request (mirrors that screen's rule 3) — enforced here, where the decision actually happens. Unaffected by the 2026-08-15 unified-access correction; this is a return-cycle rule, not a role/scope restriction.
4. All four Milestone Certification fields excluding Variance (which is computed) are required before Certify is enabled; Return and Request Information do not require them.

## Role Variations

**Corrected 2026-08-15 — collapsed from a three-tier scope/role split.** Any institution user can reach the full Decision Panel and Execute Transfer. Typically the Account Trustee does this work in practice; the Institution Relationship Manager and Auditing Bureau Officer more typically use this screen to review an assessment already made, but hold the same access if a specific situation calls for it.

## User Flow

```
Escrow Request Queue
↓
Assess (Escrow Request Details)
├─ Certify → RERAN Escrow Audit (record leaves this queue)
├─ Return → Developer (record leaves this queue, developer notified)
├─ Request Information → status updates, record remains
├─ View Trust Account → Trust Accounts
└─ (on RERAN approval) Execute Transfer → Executed, developer notified, record moves to Certified filter's history
```

## Notes

* **Structured fields, not a free-form certificate**, is the one thing this screen exists to get right — answer A3 is explicit that a document-upload certification cannot be validated or aggregated, and Section 4 is built as data entry, not attachment.
* **Minimum content for the Project Financial Position field is undefined.** Answer A3 settles the *shape* of milestone certification; it does not settle what counts as an adequate solvency narrative. This document does not propose a minimum-length or structured-subfield answer, since nothing in source addresses it.
* **The SLA for this screen's own turnaround is confirmed** — see [escrow-request-queue.md](escrow-request-queue.md#notes), answer A6 (confirmed 2026-08-15).
* Certified requests still complete an external RERAN audit gate; this screen's Certify action is the internal half of the same two-gate pattern that governs the eighteen Group C services, applied here to Group B-originated escrow work instead.
