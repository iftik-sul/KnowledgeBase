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

Let anyone with visibility into a record see its full history and current position, and take the one action available from here — respond to a query.

> **Corrected 2026-08-16, by client decision (`open-questions.md` B4).** The "Currently with... payment due" state, the Payment Pending progress step, and the Complete Payment action — all built specifically for Services #12–#15's now-retired post-decision payment timing — are removed. This screen is simpler than the version Phase 4 produced, not more complex, since the scenario those additions existed to handle no longer occurs.

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

Application reference, service, represented party, current status badge, sourced SLA, and a single **"Currently with"** line: the filer (drafting), "RERA" (submitted/under review), or nobody (completed, rejected, withdrawn).

**Corrected 2026-08-16** — the third state this line carried in Phase 4, "Your company — payment due" for Services #12–#15, is removed. Those four services now pay during submission, the same as every other fee-bearing service, so there is no post-decision payment-due state left for this line to describe.

### Section 2 — Progress

A Progress Tracker: `Draft → Submitted → RERA Review → Approved → Completed`.

**Corrected 2026-08-16** — the additional `Payment Pending` step this tracker carried between Approved and Completed for Services #12–#15 specifically is removed. Every service now follows the same four-stage tracker, with payment (where applicable) already resolved before `Submitted`, consistent with `ui/components.md`'s own corrected Progress Tracker definition.

### Section 3 — Request Details

Read-only display of everything entered on [Submit Application](submit-application.md). Editable only while the record is in Draft and held by its filer.

### Section 4 — Documents

Required and optional documents, upload status, version history per attachment.

### Section 5 — RERA Decision

Read-only. Shows RERA's decision (Approved / Returned for Correction / Information Requested / Rejected) with their stated reason. Where the status is Information Requested, a **Respond to Information Request** action is shown.

### Section 6 — Outputs

Shown once the record reaches Completed.

**Corrected 2026-08-16** — the Complete Payment action previously shown here for Services #12–#15 in their payment-due state is removed; payment for these four services now happens on Submit Application, before the record ever reaches this screen in a completed state.

* Payment Receipt — issued at checkout, before the application was lodged, for every fee-bearing service.
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

## Access

Identical for all four roles.

## User Flow

```
Applications / Dashboard
↓
Application Details
├─ Edit (Draft, own record) → Submit Application
├─ Respond to Information Request → back to Submitted
└─ Download Output → local
```

## Notes

* **This screen's most consequential Phase 4 open item — where and how Services #12–#15's post-decision payment would be collected — is now resolved by removing the scenario, not by designing the missing screen.** B4's normalization means every payment this module collects happens on Submit Application, during the same session as the rest of submission; this screen never needs a payment-collection action of its own.
* This screen does not need Financial & Trust Institutions' "Certification & RERA Decision" two-part section, since no internal certification gate exists anywhere in Group D (`open-questions.md` A5) — there is only ever one decision-maker (RERA) to display.
