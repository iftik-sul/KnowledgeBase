---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
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

> **Corrected 2026-08-15.** This screen previously gated the certification Decision Panel behind a `certify` permission scope and enforced maker ≠ checker by hiding the panel from a record's own filer. Both are retired. Certification is now an unrestricted action any of the institution's four roles may perform — **including the filer of the same record** — attributed by role in the audit trail rather than gated by scope or by who filed it (`navigation.md#access-rules` rule 2; `open-questions.md` A1).

> **Corrected 2026-08-16.** An earlier same-day correction found `Approved — Awaiting Payment` genuinely applied to Services #12 and #18, and reworked this screen's Header, Progress tracker, and Outputs section around a payment-outstanding wait state for those two services. The client has since reviewed that #12/#18 exception directly and normalized both to pay before RERA's decision, the same as #13–#17. That wait state — and every reference to it below — is now retired for the same reason it was added: the sourced sequencing it was built on has changed. See [status-badges.md](../status-badges.md#application-status) for the full three-pass history of this status.

## Purpose

Let anyone with visibility into a record see its full history and current position, and let whoever currently holds it — filer, RERAN, or nobody — take the one action available to them from here.

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

## Sections

### Section 1 — Header

Application reference, service, represented party, current status badge, sourced SLA, and a single **"Currently with"** line: the filer (drafting), "Awaiting Internal Certification" (any of the institution's four users may act, including the filer), "RERAN — Compliance & Escrow Auditor" (submitted/under review), or nobody (completed, rejected, withdrawn). This line exists because the two-gate pattern makes "who acts next" genuinely ambiguous without it.

**Corrected 2026-08-16** — a third "Currently with" state, "Customer — awaiting counter payment" for Services #12/#18, is removed. Both services now pay at the counter before RERA's review, the same point every other counter-paid service (#13–#17) pays at — there is no longer a payment-outstanding wait state for this line to describe.

### Section 2 — Progress

The Progress Tracker (see [components.md](../components.md#progress-tracker)): `Draft → Internal Certification → Submitted → RERAN Review → Approved → Completed`. Where the institution has not enabled internal certification for this service, or the service does not source it, that step is omitted from the tracker rather than shown as skipped — the record moves straight from Draft to Submitted.

Each step carries the actor who completed it and the date, pulled from the Audit Timeline rather than duplicating it — this section is the summary, Section 7 is the record.

### Section 3 — Request Details

Read-only display of everything entered on [Submit Application](../screens-unified/submit-application.md) for this record: institution/officer, represented party, property or instrument reference, and the service-specific transaction fields from the relevant `service-flows/service-NN-*.md` document. Editable only while the record is in Draft and held by its filer. **Corrected 2026-08-15** — previously linked to `service-request.md`, retired; see `ui/screens-unified/README.md` for the decision.

### Section 4 — Documents

Required and optional documents for this service, upload status, and version history per attachment. Uses [components.md](../components.md#document-uploader) while the record is editable, and read-only preview once submitted. See [validation-rules.md](../validation-rules.md#documents) for the attach-by-reference and version-pinning rules.

### Section 5 — Certification & RERAN Decision

Two sub-sections, shown according to the record's current gate:

**Internal Certification** — visible once the record has been submitted for certification. Shows the certifier's decision if made (Certified / Returned, with reason). Where the record is currently awaiting certification, the certification Decision Panel is shown to any of the institution's four roles (see [components.md](../components.md#decision-panel)): Certify or Return, reason mandatory on Return. **Corrected 2026-08-15** — previously required the viewer to hold `certify` and not be the record's own filer; both conditions are retired. Any institution user, including the filer, may certify or return their own or another user's filing.

**RERAN Decision** — read-only for every Group C role; the Compliance & Escrow Auditor is a Group A user outside this module. Shows RERAN's decision (Approved / Returned for Correction / Information Requested / Rejected) with their stated reason. Where the status is Information Requested, a **Respond to Information Request** action is shown to any institution user — this is the one action a Group C user takes against a RERAN decision from this screen.

### Section 6 — Outputs

Shown once the record reaches Completed.

* Payment Receipt — issued at checkout, before the application was lodged (#1, #3–#11), or at the counter, before RERA's decision at the point of service (#13–#17, and now #12, #18 as well). No fee applies to Service #2. This is now a uniform two-timing model across all eighteen services — see [payments.md](../../payments.md) and the correction note at the top of this file.
* Issued output document(s), downloadable, matching the specific list in the service's own service-flow document (Certificate of Title, Mortgage Release Letter, etc. — these vary by service and are not restated here).

**Corrected 2026-08-16 — no post-approval payment wait for any service.** This section previously described a payment-outstanding state for Services #12 and #18 specifically, where this screen displayed `Approved — Awaiting Payment` and waited for a counter payment collected outside this screen's own action set. That state no longer exists for any Group C service: #12 and #18 now pay at the counter as part of lodging, the same as #13–#17, so Outputs renders identically for all eighteen services — it appears once, at Completed, with a receipt already on file. Per-transaction payment history is [payment-history.md](payment-history.md).

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
4. **Corrected 2026-08-16** — there is no Settle *action* on this screen, for any service, and no service reaches Approved with payment still outstanding either. This rule previously had to carve out an exception for #12/#18; it no longer needs to.

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
├─ Edit (Draft, own record) → Submit Application
├─ Certify / Return → Internal Certification Queue (record leaves this user's queue)
├─ Respond to Information Request → back to Submitted
└─ Download Output → local
```

## Notes

* **"Currently with" is the load-bearing addition this screen was built with.** It replaced an earlier generic Progress Tracker with no indication of who held the record.
* The RERAN Decision sub-section is deliberately read-only for every role in this module — Compliance & Escrow Auditor is Group A, and no Group C screen should imply that role's action happens here.
* Output document lists differ by service and are sourced in each service's own `service-flows/service-NN-*.md` document (Section 15, Output) — this screen displays whatever that document specifies, and does not maintain its own copy of the list.
* Whether internal certification applies at all to a given record is itself service-dependent (see the Service × Form Matrix in [README.md](../README.md#service--form-matrix)) — the Progress Tracker's omission of that step is not always a configuration choice; sometimes it is because the step is unsourced for that service.
* **`Approved — Awaiting Payment` no longer applies to any service, as of 2026-08-16.** This screen was corrected twice in one day (2026-08-15) around this status — first removing it entirely, then partially restoring it for #12/#18 once their exception was found sourced. A third correction (2026-08-16) removes it again, this time because the client normalized #12/#18's payment timing rather than because the earlier audit was wrong. Worth remembering as a general lesson distinct from the 2026-08-15 one: a correction can be accurate when made and still need revisiting later if the underlying business decision itself changes — check whether a "sourced exception" is still current, not just whether it was correctly read from source at the time.
