---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/internal-certification-queue.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - certification
---

# Feature #3 – Internal Certification Queue

**Feature Category:** Shared Platform Features – Institution-Specific

## 1. Feature Overview

The **Internal Certification Queue** is the institution's own gate, worked before a record ever reaches RERA: a single, institution-wide queue of every application awaiting internal certify-or-return, open to any of the institution's four Group C roles — including the person who filed the record.

## 2. Purpose

Give the institution a shared checkpoint on the mortgage and finance-lease lifecycle (Services #3–#11) before those transactions leave the institution and enter RERA's Transaction Audit queue.

## 3. Description

Any of the institution's four Group C roles can open the queue, see every record institution-wide awaiting certification — including their own filings — and Review a record to reach its Decision Panel on `application-details.md`, where they Certify or Return it. There is no bulk certify: certification is a per-record judgement, not a batch action, matching the same reasoning applied to escrow certification. A returned record loops back to Draft; a certified one proceeds to RERA.

## 4. Used By

Services #3–#11 only — the mortgage and finance-lease lifecycle:

* Mortgage Registration, Amendment, Transfer, Release
* Grant Property Mortgage
* Finance Lease Registration, Amendment, Transfer, Release

Services #1, #2, and #12–#18 do not carry this gate — no internal certification step is described in source for those rows.

## 5. Prerequisites

* User is logged into a verified institution account.
* At least one record from Services #3–#11 has been submitted and is pending certification.

## 6. Required Information

Search/filter by: Application reference · Service · Filed by (including the current viewer) · Represented party · Age (Under 24h / 24–72h / Over 72h).

## 7. Required Documents

None to access the queue. Download Request Pack is available per row for the documents already attached to the underlying application.

## 8. Service Fee

No separate fee — certification is part of the underlying application's own submission.

## 9. Payment Required

**No.** Certification never requires payment; the underlying service's own payment model (upfront, per `payments.md`, for all of Services #3–#11) is unaffected by this feature.

## 10. Processing Authority

**Any of the institution's four Group C roles**, unrestricted — not a fifth role, not a permission scope. **Corrected 2026-08-14/15**: previously gated by a `certify` scope excluding the filer's own records; both the scope and the self-exclusion are retired. A user may certify a record they filed themselves.

## 11. Expected Processing Time

**No SLA is sourced for this internal step specifically.** Default sort is oldest-first, and an Age column (Under 24h / 24–72h / Over 72h) surfaces waiting time, but neither is a client-confirmed figure — a working design choice against a genuine source gap, not a sourced SLA.

## 12. Processing Workflow

Dashboard (certification count badge)
↓
Open Internal Certification Queue
↓
Search / Filter / Sort (default: oldest first)
↓
Review a Record
↓
Open Application Details → Decision Panel
↓
Certify (record proceeds to RERA) **or** Return (record loops back to Draft, filer notified)
↓
Record Removed from Queue

## 13. Application Status Flow

Submitted (institution-side)
↓
Pending Internal Certification
↓
Certified → Submitted (RERA-side, per Feature #1 – Service Requests)
↓
*or* Returned by Certifier → Draft (loops back to the filer, distinct from a RERA-side return)

## 14. Possible Outcomes

* Record Certified, Forwarded to RERA
* Record Returned to Filer, Reason Recorded

## 15. Output

* Certification decision recorded with the acting user, their role, and a timestamp
* On Return: a mandatory reason, visible to the filer
* On Certify: the record proceeds into Feature #1's routing to RERA's Transaction Audit queue

## 16. Related Features

* Service Requests *(where the record originated)*
* Applications *(where the record continues once certified and routed to RERA)*
* Escrow Request Queue *(a structurally similar certify/return gate, for a different object)*

## 17. UI Screens

* Internal Certification Queue
* Application Details (Decision Panel)

## 18. API Requirements

* Retrieve Institution-Wide Certification Queue
* Retrieve Application Details
* Submit Certification Decision (Certify / Return)
* Record Return Reason
* Update Application Status
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Institution, Institution Staff, User
* Application, Application Status
* Certification Record *(acting user and role at time of certification)*
* Notification, Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can view and act on every Services #3–#11 record awaiting certification, institution-wide, including their own filings.
* Certification and return both happen on Application Details' Decision Panel — the queue itself has no inline decision controls.
* No bulk certification exists.
* A Return requires a reason and notifies the filer.
* A Certify routes the record into RERA's Transaction Audit queue.
* All certification activity is recorded in the audit log, including the acting user's role.

## 21. Business Rules

1. Only Services #3–#11 carry this gate — the mortgage and finance-lease lifecycle, sourced from the master table's "bank auditor" step for those rows specifically.
2. Any of the institution's four Group C roles may certify or return any record institution-wide, including one they filed themselves — there is no maker ≠ checker restriction.
3. Certification is a per-record decision; there is no bulk certify action.
4. A returned record loops back to Draft and notifies the filer with a mandatory reason — distinct from a RERA-side return, which uses Feature #2's Applications workflow instead.
5. Every certification decision is recorded with the acting user, their role, and a timestamp, permanently in the audit trail.

## Open Questions

1. What SLA, if any, should apply to the internal certification step itself? Not sourced — the Age column and default sort are working assumptions pending a client figure.
2. `services-overview.md` To Confirm item 2 (module-wide adoption of this shared-features layer) remains open and covers this feature too.
