---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
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

**Access:** Any of the institution's four Group C roles — unified access, not role- or scope-gated (`navigation.md`, confirmed 2026-08-14). Auditing Bureau Officer has read-only access to this screen specifically, since the role does not certify or file — see Role Variations.

The full record of one service request, from draft to output issue. This screen's one job the list screens cannot do: show **which gate the record currently sits at, and who holds it.**

> **Corrected 2026-08-15.** This screen previously gated the certification Decision Panel behind a `certify` permission scope and enforced maker ≠ checker by hiding the panel from a record's own filer. Both are retired. Certification is now an unrestricted action any of the institution's four roles may perform — **including the filer of the same record** — attributed by role in the audit trail rather than gated by scope or by who filed it (`navigation.md#access-rules` rule 2; `open-questions.md` A1). The Settlement section is also retired — see Section 6, corrected for `open-questions.md` B1 and B11.

## Purpose

Let anyone with visibility into a record see its full history and current position, and let whoever currently holds it — filer, or nobody (with RERAN) — take the one action available to them from here.

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
Outputs
↓
Audit Timeline
```

**Corrected 2026-08-15** — "Settlement & Outputs" is renamed **Outputs**. There is no settlement step left to describe on any Group C record; see Section 6.

## Sections

### Section 1 — Header

Application reference, service, represented party, current status badge, sourced SLA, and a single **"Currently with"** line: the filer (drafting), "Awaiting Internal Certification" (any of the institution's four users may act, including the filer), "RERAN — Compliance & Escrow Auditor" (submitted/under review), or nobody (completed, rejected, withdrawn). This line exists because the two-gate pattern makes "who acts next" genuinely ambiguous without it.

### Section 2 — Progress

The Progress Tracker (see [components.md](../components.md#progress-tracker)): `Draft → Internal Certification → Submitted → RERAN Review → Approved → Completed`. Where the institution has not enabled internal certification for this service, or the service does not source it, that step is omitted from the tracker rather than shown as skipped — the record moves straight from Draft to Submitted.

**Corrected 2026-08-15** — "Settled" is removed as a tracker step, for the same reason Section 6 is renamed: no Group C record passes through a settlement stage between approval and completion any more.

Each step carries the actor who completed it and the date, pulled from the Audit Timeline rather than duplicating it — this section is the summary, Section 7 is the record.

### Section 3 — Request Details

Read-only display of everything entered on [service-request.md](service-request.md) for this record: institution/officer, represented party, property or instrument reference, and the service-specific transaction fields from the relevant `service-flows/service-NN-*.md` document. Editable only while the record is in Draft and held by its filer.

### Section 4 — Documents

Required and optional documents for this service, upload status, and version history per attachment. Uses [components.md](../components.md#document-uploader) while the record is editable, and read-only preview once submitted. See [validation-rules.md](../validation-rules.md#documents) for the attach-by-reference and version-pinning rules.

### Section 5 — Certification & RERAN Decision

Two sub-sections, shown according to the record's current gate:

**Internal Certification** — visible once the record has been submitted for certification. Shows the certifier's decision if made (Certified / Returned, with reason). Where the record is currently awaiting certification, the certification Decision Panel is shown to any of the institution's four roles (see [components.md](../components.md#decision-panel)): Certify or Return, reason mandatory on Return. **Corrected 2026-08-15** — previously required the viewer to hold `certify` and not be the record's own filer; both conditions are retired. Any institution user, including the filer, may certify or return their own or another user's filing.

**RERAN Decision** — read-only for every Group C role; the Compliance & Escrow Auditor is a Group A user outside this module. Shows RERAN's decision (Approved / Returned for Correction / Information Requested / Rejected) with their stated reason. Where the status is Information Requested, a **Respond to Information Request** action is shown to any institution user — this is the one action a Group C user takes against a RERAN decision from this screen.

### Section 6 — Outputs

Shown once the record reaches Completed.

* Payment Receipt — issued at checkout, before the application was lodged (#1, #3–#11) or at the point of service (#12–#18). No fee applies to Service #2. **Corrected 2026-08-15** — this section previously distinguished a "fee balance" artefact (institution account debit services) from a "payment receipt" (counter-paid services), per the now-superseded `open-questions.md` B9. There is only one artefact now, issued before or at lodging, never after approval — see [payments.md](../../payments.md).
* Issued output document(s), downloadable, matching the specific list in the service's own service-flow document (Certificate of Title, Mortgage Release Letter, etc. — these vary by service and are not restated here).

**Removed 2026-08-15.** This section previously included a **Settle** action, routing to a Settlement Account screen, available once a record reached `Approved — Awaiting Payment`. That status does not occur for any Group C service (`open-questions.md` B1, B11): #1 and #3–#11 pay upfront before lodging, #2 has no fee, #12–#18 pay at the point of service. There is nothing left to settle on this screen. Per-transaction payment history is [payment-history.md](payment-history.md) (formerly `settlement-account.md`), not this record view.

### Section 7 — Audit Timeline

Full reverse-chronological event history: actor, role held at time of action, action, timestamp, reason where given, attachments added. See [components.md](../components.md#audit-timeline). This is the canonical record; Section 2's Progress summary is derived from it, not the other way round. **Corrected 2026-08-15** — "scope used" is replaced with "role held at time of action," matching the audit-trail-attribution model (`navigation.md#audit-trail-principle`).

## Empty State

Not applicable — this screen only renders for an existing record. Reaching it with no record shows a not-found state:

> This application could not be found, or you do not have access to it.

**Primary Button:** Back to Applications

## Reused Components

See [components.md](../components.md). Uses Institution Operations Sidebar, Top Bar, Progress Tracker, Information Cards, Document Uploader, Decision Panel, Status Badge, Audit Timeline, Buttons.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. Editability follows status and ownership, not role: only the current holder of a Draft record may edit Request Details or Documents.
2. **Removed 2026-08-15** — the certification Decision Panel is no longer withheld from a record's own filer. Certification is unrestricted, including self-certification, per `navigation.md#access-rules` rule 2.
3. A reason is mandatory on Return, on any RERAN-side negative decision display prompting a response, and on Respond to Information Request — submitting a response without adequately addressing the query is not itself blocked; RERAN's own review catches an inadequate response.
4. **Removed 2026-08-15** — the balance-check rule for Settle no longer applies; there is no Settle action.

## Role Variations

**Corrected 2026-08-15 — collapsed from four role blocks to two.** Certification and filing are no longer role-gated, so there is nothing left to differentiate among Mortgage Officer, Institution Relationship Manager, or any user — they all get the same full access, described once below.

### Any institution user (Mortgage Officer, Institution Relationship Manager, Account Trustee, Auditing Bureau Officer acting on their own filing)

Full access to any record at the institution: view, edit while Draft and held by them, certify or return any record including their own, respond to information requests, view outputs.

### Auditing Bureau Officer, viewing a record they did not file and are not certifying

Read-only throughout, in the ordinary case where this role is examining rather than acting: sees Sections 1–4 and 6–7 in full. Nothing in the corrected model prevents this role from certifying a record if it chooses to act on one — certification is unrestricted for all four roles — but in practice this role's typical work is independent audit, not filing or certifying Group C transactions (see [roles-and-responsibilities.md](../../roles-and-responsibilities.md)).

## User Flow

```
Applications / Dashboard / Internal Certification Queue
↓
Application Details
├─ Edit (Draft, own record) → Service Request
├─ Certify / Return → Internal Certification Queue (record leaves this user's queue)
├─ Respond to Information Request → back to Submitted
└─ Download Output → local
```

## Notes

* **"Currently with" is the load-bearing addition this screen was built with.** It replaced an earlier generic Progress Tracker with no indication of who held the record.
* The RERAN Decision sub-section is deliberately read-only for every role in this module — Compliance & Escrow Auditor is Group A, and no Group C screen should imply that role's action happens here.
* Output document lists differ by service and are sourced in each service's own `service-flows/service-NN-*.md` document (Section 15, Output) — this screen displays whatever that document specifies, and does not maintain its own copy of the list.
* Whether internal certification applies at all to a given record is itself service-dependent (see the Service × Form Matrix in [README.md](../README.md#service--form-matrix)) — the Progress Tracker's omission of that step is not always a configuration choice; sometimes it is because the step is unsourced for that service.
