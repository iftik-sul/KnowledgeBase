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

# Screen: Escrow Request Details

**Roles:** Account Trustee (`escrow`) · Institution Relationship Manager (read) · Auditing Bureau Officer (read)

**This screen did not previously exist.** Referenced by [escrow-request-queue.md](escrow-request-queue.md)'s Assess action, which had nowhere to route to.

## Purpose

Give the Account Trustee everything needed to reach a certification decision on one developer escrow request: the request's own context, a solvency assessment, and — per answer A3 — a structured milestone certification rather than a document upload standing in for one.

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

Everything routed from the developer module: the milestone or event cited, the developer's own supporting materials, and prior requests against the same trust account for comparison. Read-only — this is what the Trustee is assessing, not editing.

### Section 3 — Solvency Assessment

The judgement answer A2 says happens *inside* the platform, not externally with only an outcome recorded:

* **Project Financial Position** — narrative assessment field, structured minimums TBD (see Notes).
* **Requested vs. Available** — requested amount shown directly against the trust account's current balance (also visible on the queue row, repeated here at decision time because it is the single fact most likely to drive a Return).
* **Solvency Notes** — free text, required before the Decision Panel accepts a Certify action.

### Section 4 — Milestone Certification

Structured, per answer A3 — a free-form certification letter can be neither validated against KPI 8's data-integrity target nor aggregated for FR-19 reporting:

| Field | Description |
| :---- | :---- |
| Milestone Reference | Which construction milestone this certifies |
| Percentage Complete | Trustee's assessed completion |
| Valuation of Works Executed | Assessed value of work completed to date |
| Amount Certified | What the Trustee is certifying for release — validated against Available Balance, see Validation |
| Variance Against Previous Certificate | Difference from the last certification on this trust account, computed and shown, not entered |
| Certifier Declaration | A standard attestation the Trustee affirms before the record can be certified |
| Attachments | Supporting evidence for the assessment — a supplement to the structured fields above, not a replacement for them |

This is the mechanism behind the Account Trustee's stated responsibility to "certify that construction milestones justify the requested drawdown."

### Section 5 — Documents

Supporting assessment materials and anything the developer attached, using [components.md](../components.md#document-uploader) and [components.md](../components.md#document-reference-picker) where a document already exists in the repository.

### Section 6 — Decision Panel

See [components.md](../components.md#decision-panel), extended for this screen with the structured fields above rather than a bare reason box:

* **Certify** — forwards to RERAN escrow audit. Requires Section 4 fully completed and the Section 3 solvency notes populated.
* **Return** — sends back to the developer. Reason mandatory (FR-04).
* **Request Information** — queries the developer without closing the request. Reason mandatory, and the request remains in the queue at Information Requested status rather than leaving it.

### Section 6a — Execute Transfer

Appears in place of the Decision Panel once status reaches **RERAN Approved** — the request has passed both gates and the only step left is the Trustee moving the funds. This is a distinct action from Certify: certifying forwards a recommendation to RERAN's escrow audit; executing moves money, only after RERAN's own approval is on record.

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
3. A request cannot be certified by the user who last returned it to the developer on this same request (mirrors that screen's rule 3) — enforced here, where the decision actually happens.
4. All four Milestone Certification fields excluding Variance (which is computed) are required before Certify is enabled; Return and Request Information do not require them.

## Role Variations

### Account Trustee

Full operation, as described.

### Institution Relationship Manager

Read-only. Sees the full assessment and certification once made, but not a Decision Panel — matching this role's oversight-not-participation position on the queue screen.

### Auditing Bureau Officer

Read-only, with an **Audit Flag** indicator if this specific certification was later queried by RERAN — the same signal that populates the Audit Flags filter on the queue screen. No Decision Panel, for the same reason: this role audits certifications, and does not make them.

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
* **The SLA for this screen's own turnaround is the same open question as the queue's** — see [escrow-request-queue.md](escrow-request-queue.md#notes). Nothing here resolves it independently.
* Certified requests still complete an external RERAN audit gate; this screen's Certify action is the internal half of the same two-gate pattern that governs the eighteen Group C services, applied here to Group B-originated escrow work instead.
* **Execute Transfer closes a gap found while checking this screen against `role-workflows.md`.** The Account Trustee's journey there names "Execute Approved Transfer" as a step, and the Escrow Request Status vocabulary already includes `Executed`, but no action anywhere produced that transition until this pass. See the PR description for the full navigation/role-workflows cross-check.
