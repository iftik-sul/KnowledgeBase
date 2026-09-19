---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-18
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a7-conduct-site-inspection.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, inspection, report, mobile]
---

# Screen: Inspection Report

**Archetype:** 2 — Detail (read-only report). **Form factor: mobile / tablet** for the field officer;
also viewable on desktop by the consuming decision service.
**Access (RBAC-gated):** Inspection & Enforcement Officer (author). The report is **consumed** by A-1
Application Review (the decision reviewer reads it). Navigation is governed by [role-screen-matrix.md](../role-screen-matrix.md).

The finalised inspection output (A-7): the geo-tagged findings, evidence, milestone results, and
overall pass/fail, assembled into a single report that a dependent A-1 decision can act on. Reached
after submitting [Inspection Capture](inspection-capture.md), or opened from the queue for a completed
inspection. Read-only once produced.

## Purpose

Give the dependent decision (A-1) — and the officer — a single, evidenced, accountable record of what
was found on site, so a decision can be made on verified ground truth.

## Layout

* **Visible Sidebar:** none on mobile (field view); the desktop A-1 consumer opens it as a linked
  panel/record from Application Review.
* **Top Bar Title:** {Site / project} — Inspection Report
* **Breadcrumb (desktop consumer view):** Application Review › Inspection Report

```
Top Bar → Report header → Site + geo-tag result → Milestone results → Findings + evidence →
Overall result → (returned to dependent decision)
```

## Sections

### Section 1 — Report header

Site / project reference · inspecting officer · inspection date · overall result (Passed / Failed-
Discrepant) as a Badge · linked dependent item (the A-1 item that requested it).

### Section 2 — Site + geo-tag result

Filed location vs captured geo-tag, with the match/mismatch outcome.

### Section 3 — Milestone results

The completed checklist — each item with its pass/fail/NA result (read-only).

### Section 4 — Findings + evidence

Each recorded finding with its note and attached photo(s) — a read-only gallery/list.

### Section 5 — Overall result

Passed → the dependent decision may proceed. Failed / Discrepant → feeds a return/reject in the
dependent A-1 decision (or an A-8 enforcement action, deferred).

## Role Variations / Permissions

- **Inspection & Enforcement Officer** authors/views the report (read-only once submitted).
- **A-1 reviewer** (C&E Auditor / Licensing Officer) consumes it read-only from Application Review as
  the field-check evidence for a decision. The report does not itself make the decision.

## Notes

- Once produced the report is immutable; corrections require a new/amended inspection, not an edit.
- The report is the hand-off artefact between A-7 and A-1 — its "Passed/Failed" result is what the
  Registry Checks / decision on Application Review keys off for field-visit items.
