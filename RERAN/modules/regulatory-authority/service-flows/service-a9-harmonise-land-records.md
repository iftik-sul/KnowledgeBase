---
project: RERAN
module: regulatory-authority
type: service-flow
status: draft
contains_proposals: true
source_type: derived
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/services-overview.md"
  - "RERAN/modules/regulatory-authority/open-questions.md"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - latent
  - reconciliation
---

# Regulatory Authority Service A-9 — Harmonise Land Records

> **LATENT SERVICE.** No current front-office service routes to A-9; it is a background
> reconciliation function, so its functional build stays deferred (open-questions A5).
> **A4 is now resolved: AGIS is a design reference, not a live integration** — so this
> service is *manual periodic reconciliation*, not a system-to-system sync.

## 1. Service Overview

**Harmonise Land Records** is the federalism service: it keeps RERAN's records in step
with the State Lands Bureaus and Surveyors-General, resolves jurisdictional conflicts,
and harmonises Certificate-of-Occupancy (C-of-O) data across federal and state
authorities. AGIS informs how this work is modelled, but is not a system RERAN connects
to (A4).

## 2. Purpose

Prevent the platform's land records from diverging from the state systems of record —
so a C-of-O or boundary the platform relies on matches what the relevant bureau holds.

## 3. Description

A State Liaison Coordinator compares platform records against a state bureau's records,
detects conflicts between the two, and resolves or escalates them.

Per the A4 resolution this is **periodic manual reconciliation**: bureau records are
obtained out-of-band and compared against platform records. There is no sync API, no
scheduled push/pull, and no live dependency on an external system.

## 4. Who Can Act

**State Liaison Coordinator** (RA), under RBAC + MFA.

## 5. Trigger

Internal/periodic, or when a jurisdictional conflict is detected. No applicant queue.

## 6. What the Coordinator Works With

- Platform land/C-of-O records.
- State-bureau records obtained out-of-band (AGIS or equivalent) — reference only.
- Detected conflicts between the two.

## 7. Task Checklist

- Records are compared against the authoritative state source.
- Conflicts are identified and characterised.
- Resolutions are recorded and, where needed, escalated.

> **Proposed** — conflict-resolution rules (who arbitrates, what evidence is required)
> still need client confirmation. The *mechanism* is settled: manual reconciliation.

## 8. Service Fee / 9. Payment Required

**N/A.**

## 10. Authority & Access Control

- **Role:** State Liaison Coordinator (RA).
- **Access control:** RBAC + MFA.
- **Sub-system:** cross-cutting data-harmonisation layer.

## 11. Expected Processing Time

N/A — background/periodic.

## 12. Processing Workflow

```
Reconciliation triggered  (periodic / conflict detected)
        ↓
Compare platform records ↔ state-bureau records  (obtained out-of-band)
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

1. **AGIS — resolved (A4):** design reference only. No integration, no data contract, no
   external uptime dependency.
2. Any service relying on C-of-O/boundary data depends on this staying reconciled.

## 16. Related Services

- **A-2** (registry consistency, adjacent) and **A-6** (RBAC).

## 17. UI Screens

- **Harmonisation dashboard** — reconciliation runs, reconciled vs conflicted records,
  drill-in.
- **Conflict resolution view** — compare platform vs bureau record; resolve/escalate.

## 18. API Requirements

- Fetch platform land/C-of-O records
- Import / record state-bureau records (manual upload or out-of-band file)
- Run comparison; flag conflicts
- Record resolutions
- Write audit-log entry

## 19. Database Entities

- Harmonisation Run *(period, status)*
- Land / C-of-O Record *(platform)*
- Bureau Record *(imported reference snapshot)*
- Conflict / Resolution
- Staff User + Role + Permission *(RBAC)*
- Audit Log

## 20. Acceptance Criteria

- Only a State Liaison Coordinator with MFA can run reconciliation.
- Conflicts between platform and bureau records are surfaced, not hidden.
- Resolutions are recorded and escalatable.
- Every run is written to the audit trail.

## 21. Business Rules

1. Access is role-gated (State Liaison Coordinator) + MFA.
2. The authoritative source for state-held data is the state bureau, not the platform.
3. All runs and resolutions are recorded in the audit trail with the acting officer.
4. **Latent** — functional build deferred until services exercise it (A5). No longer
   blocked: A4 is resolved (design reference, manual reconciliation).
