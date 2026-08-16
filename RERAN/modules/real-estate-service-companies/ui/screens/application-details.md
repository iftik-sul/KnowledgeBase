---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/service-flows/"
  - "RERAN/modules/real-estate-service-companies/payments.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - application-details
---

# Screen: Application Details

**Access:** Any of the company's four Group D roles — identical screen for every user.

The full record of one application, from draft to output issue.

## Purpose

Let anyone with visibility into a record see its full history and current position, and take the one action available from here — respond to a query, or complete a post-decision payment where the service requires it.

## Layout

```
Top Bar
↓
Header
↓
Progress
↓
Request Details
↓
Documents
↓
RERA Decision
↓
Outputs
↓
Audit Timeline
```

## Sections

### Section 1 — Header

Application reference, service, represented party, current status badge, sourced SLA, and a single **"Currently with"** line: the filer (drafting), "RERA" (submitted/under review), **"Your company — payment due" (Services #12–#15 only, once accepted and before payment)**, or nobody (completed, rejected, withdrawn).

### Section 2 — Progress

A Progress Tracker: `Draft → Submitted → RERA Review → Approved → Completed`. **For Services #12–#15 specifically**, an additional `Payment Pending` step sits between `Approved` and `Completed`, matching the sourced sequence — payment genuinely follows acceptance for these four services, unlike every other fee-bearing service in this module.

### Section 3 — Request Details

Read-only display of everything entered on [Submit Application](submit-application.md). Editable only while the record is in Draft and held by its filer.

### Section 4 — Documents

Required and optional documents, upload status, version history per attachment.

### Section 5 — RERA Decision

Read-only. Shows RERA's decision (Approved / Returned for Correction / Information Requested / Rejected) with their stated reason. Where the status is Information Requested, a **Respond to Information Request** action is shown.

### Section 6 — Outputs

Shown once the record reaches Completed, **or, for Services #12–#15, once RERA accepts the application and the record enters the payment-due state.**

* **Complete Payment** action — shown for Services #12–#15 only, in the payment-due state. Selecting it opens the payment step this module's build still needs to design (see `submit-application.md`'s own Notes for the same flagged gap).
* Payment Receipt — issued once payment succeeds, for every fee-bearing service.
* Issued output document(s), matching the specific list in the service's own service-flow document.

### Section 7 — Audit Timeline

Full reverse-chronological event history: actor, role held at time of action, action, timestamp, reason where given.

## Empty State

Not applicable — this screen only renders for an existing record.

> This application could not be found, or you do not have access to it.

## Reused Components

Company Operations Sidebar, Top Bar, Progress Tracker, Information Cards, Document Uploader, Status Badge, Audit Timeline, Buttons.

## Validation

1. Editability follows status and ownership, not role.
2. A reason is mandatory on Return and on Respond to Information Request.
3. **For Services #12–#15, the Complete Payment action is only enabled once RERA's acceptance has been recorded** — attempting payment before acceptance is blocked, matching the sourced sequence.

## Access

Identical for all four roles.

## User Flow

```
Applications / Dashboard
↓
Application Details
├─ Edit (Draft, own record) → Submit Application
├─ Respond to Information Request → back to Submitted
├─ Complete Payment (Services #12–#15 only) → payment step (not yet designed)
└─ Download Output → local
```

## Notes

* **This screen's "Currently with" line and Complete Payment action for #12–#15 are the most consequential open design item in this module's UI package**, carried forward from `submit-application.md`'s own flagged gap. Whichever screen or step eventually collects that payment, this screen needs to link to it correctly once it exists.
* This screen does not need Financial & Trust Institutions' "Certification & RERA Decision" two-part section, since no internal certification gate exists anywhere in Group D (`open-questions.md` A5) — there is only ever one decision-maker (RERA) to display.
