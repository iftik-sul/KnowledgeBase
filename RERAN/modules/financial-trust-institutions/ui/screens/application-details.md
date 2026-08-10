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
  - "RERAN/modules/financial-trust-institutions/service-flows/"
tags:
  - financial-trust-institutions
  - ui-spec
  - application-details
---

# Screen: Application Details

**Roles:** Mortgage Officer (own) · Institution Relationship Manager (institution-wide) · certifier scope (where the record awaits certification) · Auditing Bureau Officer (read)

The full record of one service request, from draft to output issue. This screen's one job the list screens cannot do: show **which of the two gates the record currently sits at, and who holds it.**

## Purpose

Let anyone with visibility into a record see its full history and current position, and let whoever currently holds it — filer, certifier, or nobody (with RERAN) — take the one action available to them from here.

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
Certification & RERAN Decision
↓
Settlement & Outputs
↓
Audit Timeline
```

## Sections

### Section 1 — Header

Application reference, service, represented party, current status badge, sourced SLA, and a single **"Currently with"** line: the filer (drafting), the certifier by name (pending internal certification), "RERAN — Compliance & Escrow Auditor" (submitted/under review), or nobody (completed, rejected, withdrawn, expired). This line exists because the two-gate pattern makes "who acts next" genuinely ambiguous without it.

### Section 2 — Progress

The Progress Tracker (see [components.md](../components.md#progress-tracker)): `Draft → Internal Certification → Submitted → RERAN Review → Approved → Settled → Completed`. Where the institution has not enabled internal certification for this service, or the service does not source it, that step is omitted from the tracker rather than shown as skipped — the record moves straight from Draft to Submitted.

Each step carries the actor who completed it and the date, pulled from the Audit Timeline rather than duplicating it — this section is the summary, Section 7 is the record.

### Section 3 — Request Details

Read-only display of everything entered on [service-request.md](service-request.md) for this record: institution/officer, represented party, property or instrument reference, and the service-specific transaction fields from the relevant `service-flows/service-NN-*.md` document. Editable only while the record is in Draft and held by its filer.

### Section 4 — Documents

Required and optional documents for this service, upload status, and version history per attachment. Uses [components.md](../components.md#document-uploader) while the record is editable, and read-only preview once submitted. See [validation-rules.md](../validation-rules.md#documents) for the attach-by-reference and version-pinning rules.

### Section 5 — Certification & RERAN Decision

Two sub-sections, shown according to the record's current gate and the viewer's scope:

**Internal Certification** — visible once the record has been submitted for certification. Shows the certifier's decision if made (Certified / Returned, with reason). Where the record is currently awaiting certification and the viewer holds `certify` **and is not the filer of this record**, the certification Decision Panel is shown (see [components.md](../components.md#decision-panel)): Certify or Return, reason mandatory on Return. Maker ≠ checker is enforced here, not just described — the panel is not rendered for the filer even if they hold `certify`.

**RERAN Decision** — read-only for every Group C role; the Compliance & Escrow Auditor is a Group A user outside this module. Shows RERAN's decision (Approved / Returned for Correction / Information Requested / Rejected) with their stated reason. Where the status is Information Requested, a **Respond to Information Request** action is shown to the filer (or the Institution Relationship Manager, institution-wide) — this is the one action a Group C user takes against a RERAN decision from this screen.

### Section 6 — Settlement & Outputs

Shown once the record reaches Approved — Awaiting Payment or later.

* Fee charged, and — per answer B9 — whichever artefact this service produces: a **fee balance** entry (institution account debit services) or a **payment receipt / e-receipt voucher** (counter-paid services). Both are never shown as the same thing.
* Settle action, where the viewer holds `settlement` and the record is Approved — Awaiting Payment. Routes to [settlement-account.md](settlement-account.md) rather than settling inline, since settlement is a ledger operation with its own balance checks.
* Issued output document(s) once Completed, downloadable, matching the specific list in the service's own service-flow document (Certificate of Title, Mortgage Release Letter, etc. — these vary by service and are not restated here).

### Section 7 — Audit Timeline

Full reverse-chronological event history: actor, scope used, action, timestamp, reason where given, attachments added. See [components.md](../components.md#audit-timeline). This is the canonical record; Section 2's Progress summary is derived from it, not the other way round.

## Empty State

Not applicable — this screen only renders for an existing record. Reaching it with no record shows a not-found state:

> This application could not be found, or you do not have access to it.

**Primary Button:** Back to Applications

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Progress Tracker, Information Cards, Document Uploader, Decision Panel, Status Badge, Audit Timeline, Buttons.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. Editability follows status and ownership, not role: only the current holder of a Draft record may edit Request Details or Documents.
2. The certification Decision Panel is never rendered for the record's own filer, regardless of scope held (maker ≠ checker, [validation-rules.md](../validation-rules.md#permission-scope)).
3. A reason is mandatory on Return, on any RERAN-side negative decision display prompting a response, and on Respond to Information Request being submitted without addressing the query is not itself blocked — RERAN's own review catches an inadequate response.
4. Settle is offered only where the balance check would pass; where it would not, the panel shows the shortfall and a Fund Account link instead of a disabled button.

## Role Variations

### Mortgage Officer

Full access to their own filed records: view, edit while Draft, respond to information requests, view settlement and outputs. No certification action, even where they hold `certify` — see maker ≠ checker above.

### Institution Relationship Manager

Same as Mortgage Officer, institution-wide, plus the Settle action where they hold `settlement`. Can respond to information requests on any institution record, not just their own #1/#2/#18 filings.

### Certifier scope

Sees the certification Decision Panel on any record currently awaiting certification that they did not file. Otherwise sees the record read-only, same as their underlying role would without the scope.

### Auditing Bureau Officer

Read-only throughout. Sees Sections 1–4 and 6–7 in full; Section 5's Decision Panel never renders for this role under any status, since the role does not certify or approve — only RERAN's own decision is visible, as with every role.

## User Flow

```
Applications / Dashboard / Internal Certification Queue
↓
Application Details
├─ Edit (Draft, own record) → Service Request
├─ Certify / Return → Internal Certification Queue (record leaves this user's queue)
├─ Respond to Information Request → back to Submitted
├─ Settle → Settlement Account
└─ Download Output → local
```

## Notes

* **"Currently with" is the load-bearing addition this rewrite makes.** The previous version showed a generic Progress Tracker with no indication of who held the record, which is the exact gap the issue calling for this rewrite flagged.
* The RERAN Decision sub-section is deliberately read-only for every role in this module — Compliance & Escrow Auditor is Group A, and no Group C screen should imply that role's action happens here.
* Output document lists differ by service and are sourced in each service's own `service-flows/service-NN-*.md` document (Section 15, Output) — this screen displays whatever that document specifies, and does not maintain its own copy of the list.
* Whether internal certification applies at all to a given record is itself service-dependent and, for several services, an open question at the service-flow level (see the Service × Form Matrix in [README.md](../README.md#service--form-matrix)) — the Progress Tracker's omission of that step is not always a configuration choice; sometimes it is because the step is unsourced for that service.
