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
  - "RERAN/modules/regulatory-authority/roles-and-actions-analysis.md"
tags:
  - regulatory-authority
  - service-flow
  - back-office
  - latent
  - inspection
---

# Group A Service A-7 — Conduct Site Inspection

> **LATENT SERVICE.** No current front-office service routes to A-7 as a primary
> decision; it appears only as a *sub-step* inside a couple of services (RED #27 field
> visit; IU items that flag "inspection required"). Its functional build is deferrable
> until services that exercise it exist (open-questions A5). This flow is a structured
> sketch, not a build-ready spec.

## 1. Service Overview

**Conduct Site Inspection** is the physical-world verification service: a RERA field
officer visits a site, records geo-tagged findings, and verifies that what was filed
matches reality. Its output feeds back into an A-1 decision for the items that require it.

## 2. Purpose

Let RERA confirm on the ground what documents alone cannot — that a project, boundary,
or construction milestone is real and as described — before a dependent decision is made.

## 3. Description

An inspection is triggered (as a sub-step of a decision, or proactively). An Inspection
& Enforcement Officer schedules and conducts a site visit, records geo-tagged findings
and milestone verification, and returns an inspection report that a decision service
(A-1) can act on.

## 4. Who Can Act

**Inspection & Enforcement Officer** (Group A), under RBAC + MFA.

## 5. Trigger

A decision service requests a field check (e.g. RED #27), an item flags inspection
required, or the officer initiates one proactively. Not a standing applicant queue.

## 6. What the Officer Works With

- The site/project reference and its registry record.
- The inspection checklist for the matter.
- Geo-tag / location tools for on-site capture.

## 7. Task Checklist

- The site matches the filed location and description.
- Construction milestones (where relevant) are as claimed.
- Findings are geo-tagged and evidenced (photos/notes).

> **Proposed** — inspection procedure and checklist are not detailed in current source.

## 8. Service Fee / 9. Payment Required

**N/A.**

## 10. Authority & Access Control

- **Role:** Inspection & Enforcement Officer (Group A).
- **Access control:** RBAC + MFA.
- **Sub-system:** Inspection & Enforcement Module.

## 11. Expected Processing Time

Depends on scheduling and site; inherited by the dependent decision's SLA where it is a
sub-step.

## 12. Processing Workflow

```
Inspection triggered  (sub-step of a decision, or proactive)
        ↓
Schedule visit
        ↓
Conduct site visit  →  record geo-tagged findings + milestone verification
        ↓
Produce inspection report
        ↓
Return report to the dependent decision (A-1)  /  file proactively
        ↓
Write to the audit trail
```

## 13. Status

An inspection is **Requested**, **Scheduled**, **Completed**, or **Cancelled**.

## 14. Possible Outcomes

- **Passed** — findings match; the dependent decision may proceed.
- **Failed / Discrepant** — findings differ; feeds a return/reject in the dependent
  decision, or an enforcement action (A-8).

## 15. Cross-Module Dependencies

- **A-1** consumes inspection reports for items that require a field visit.
- **A-8 Issue enforcement notice** may follow a failed inspection.

## 16. Related Services

- **A-1** (consumer), **A-8** (downstream), **A-6** (RBAC, prerequisite).

## 17. UI Screens

- **Inspection queue** — requested and scheduled inspections.
- **Inspection capture** — on-site findings, geo-tag, photos, milestone checklist.
- **Inspection report** — the finalised report returned to a decision.

## 18. API Requirements

- Fetch inspection requests
- Schedule inspection
- Capture geo-tagged findings + evidence
- Produce/return inspection report
- Write audit-log entry

## 19. Database Entities

- Inspection *(request, schedule, status)*
- Finding / Evidence *(geo-tagged)*
- Inspection Report
- Staff User + Role + Permission *(RBAC)*
- Audit Log

## 20. Acceptance Criteria

- Only an Inspection & Enforcement Officer with MFA can conduct inspections.
- Findings are geo-tagged and evidenced.
- A completed inspection returns a report the dependent decision can act on.
- Every inspection is recorded in the audit trail.

## 21. Business Rules

1. Access is role-gated (Inspection & Enforcement Officer) + MFA.
2. Findings must be geo-tagged and evidenced.
3. All inspections are recorded in the audit trail with the acting officer.
4. **Latent** — functional build deferred until services exercise it (A5).
