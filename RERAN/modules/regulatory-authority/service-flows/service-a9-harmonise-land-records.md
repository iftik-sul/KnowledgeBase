---
project: RERAN
module: regulatory-authority
type: service-flow
status: draft
contains_proposals: true
source_type: derived
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/open-questions.md"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - latent
  - integration
---

# Group A Service A-9 — Harmonise Land Records

> **LATENT SERVICE, and the most open.** No current front-office service routes to A-9;
> it is a background integration function. Its scope depends entirely on open-question
> A4 — whether AGIS (and other state bureaus) is a *design reference* or a *live
> integration target*. Until A4 is decided, this flow is a placeholder sketch.

## 1. Service Overview

**Harmonise Land Records** is the federalism service: it keeps RERAN's records in step
with the State Lands Bureaus and Surveyors-General, resolves jurisdictional conflicts,
and harmonises Certificate-of-Occupancy (C-of-O) data across federal and state
authorities. It is the home of any AGIS-type integration.

## 2. Purpose

Prevent the platform's land records from diverging from the state systems of record —
so a C-of-O or boundary the platform relies on matches what the relevant bureau holds.

## 3. Description

A State Liaison Coordinator synchronises records with a state bureau (pull and/or push),
detects conflicts between platform and bureau data, and resolves or escalates them. The
concrete mechanics depend on A4: a design-reference answer means periodic manual
reconciliation; a live-integration answer means a system-to-system sync with AGIS.

## 4. Who Can Act

**State Liaison Coordinator** (Group A), under RBAC + MFA.

## 5. Trigger

Internal/periodic, or when a jurisdictional conflict is detected. No applicant queue.

## 6. What the Coordinator Works With

- Platform land/C-of-O records.
- State-bureau records (via AGIS or equivalent) — reference or live per A4.
- Detected conflicts between the two.

## 7. Task Checklist

- Records are compared against the authoritative state source.
- Conflicts are identified and characterised.
- Resolutions are recorded and, where needed, escalated.

> **Proposed / blocked on A4** — the sync mechanism and conflict-resolution rules cannot
> be specified until the reference-vs-integration decision is made.

## 8. Service Fee / 9. Payment Required

**N/A.**

## 10. Authority & Access Control

- **Role:** State Liaison Coordinator (Group A).
- **Access control:** RBAC + MFA.
- **Sub-system:** cross-cutting data-harmonisation layer.

## 11. Expected Processing Time

N/A — background/periodic.

## 12. Processing Workflow

```
Sync triggered  (periodic / conflict detected)
        ↓
Compare platform records ↔ state-bureau records  (reference or live per A4)
        ↓
Detect conflicts
        ↓
Resolve / harmonise  →  (escalate jurisdictional disputes where needed)
        ↓
Record reconciled state
        ↓
Write to the audit trail
```

## 13. Status

A harmonisation run is **Open**, **Reconciled**, or **Conflicted** (with flagged items).

## 14. Possible Outcomes

- **Reconciled** — platform and bureau records agree.
- **Conflicted** — discrepancies flagged/escalated.

## 15. Cross-Module Dependencies

1. **AGIS (open-question A4)** — determines whether this is reference reconciliation or
   live integration; the single biggest external unknown for the module.
2. Any service relying on C-of-O/boundary data depends on this staying reconciled.

## 16. Related Services

- **A-2** (registry consistency, adjacent), **A-6** (RBAC), and the AGIS decision (A4).

## 17. UI Screens

- **Harmonisation dashboard** — sync runs, reconciled vs conflicted records, drill-in.
- **Conflict resolution view** — compare platform vs bureau record; resolve/escalate.

## 18. API Requirements

- Fetch platform land/C-of-O records
- Fetch / integrate state-bureau records (per A4)
- Run comparison; flag conflicts
- Record resolutions
- Write audit-log entry

## 19. Database Entities

- Harmonisation Run *(period, status)*
- Land / C-of-O Record *(platform)*
- Bureau Record *(reference or live)*
- Conflict / Resolution
- Staff User + Role + Permission *(RBAC)*
- Audit Log

## 20. Acceptance Criteria

- Only a State Liaison Coordinator with MFA can run harmonisation.
- Conflicts between platform and bureau records are surfaced, not hidden.
- Resolutions are recorded and escalatable.
- Every run is written to the audit trail.

## 21. Business Rules

1. Access is role-gated (State Liaison Coordinator) + MFA.
2. The authoritative source for state-held data is the state bureau, not the platform.
3. All runs and resolutions are recorded in the audit trail with the acting officer.
4. **Latent + blocked on A4** — cannot be built until the AGIS reference-vs-integration
   decision is made.
