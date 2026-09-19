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
tags: [regulatory-authority, ui-spec, inspection, capture]
---

# Screen: Inspection Capture

**Archetype:** Capture / Form (on-site data entry). Desktop back-office.
**Access (RBAC-gated):** Inspection & Enforcement Officer. MFA required. Navigation is governed by [role-screen-matrix.md](../role-screen-matrix.md).

The on-site data-capture screen (A-7): the officer records geo-tagged findings, photos, and milestone
verification from a site visit. Reached by opening a scheduled inspection from the
[Inspection Queue](inspection-queue.md). On completion it produces the
[Inspection Report](inspection-report.md).

## Purpose

Let the officer record geo-tagged, evidenced findings from a site visit — the things documents alone
cannot confirm — into a single structured form.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** {Site / project} — Inspection
* **Breadcrumb:** Inspection Queue › {Site / project}

```
Top Bar → Breadcrumb → Site header (with geo-tag) → Milestone / checklist → Findings +
Photo evidence → Overall result → Submit (produces report)
```

## Sections

### Section 1 — Site header + geo-tag

Site / project reference and filed location, plus a **geo-tag** field recording the captured visit
coordinates against the filed location (match / mismatch indicator). Geo-tagging is mandatory (A-7
business rule).

### Section 2 — Milestone / checklist

The inspection checklist for the matter — each item a pass/fail/NA control (Checkbox/radio group),
e.g. construction milestone verification for a RED field visit.

> **Proposed** — the specific checklist items are not detailed in current source (A-7 §7 marks the
> procedure/checklist as proposed).

### Section 3 — Findings + photo evidence

Per finding: a short note (text) + one or more **photos** (uploaded/attached). Evidence must be
attached (A-7 business rule: findings geo-tagged and evidenced).

### Section 4 — Overall result

The officer's overall on-site call: **Passed** (findings match) or **Failed / Discrepant** (findings
differ) — A-7 §14. This feeds the dependent A-1 decision (or an A-8 enforcement action, deferred).

### Section 5 — Submit

Submit produces the [Inspection Report](inspection-report.md) and writes to the audit trail. Guard:
cannot submit without a captured geo-tag and at least the required evidence.

## Role Variations / Permissions

- Inspection & Enforcement Officer only. The officer captures findings; the pass/fail result feeds a
  decision elsewhere — it is not itself the A-1 decision.

## Notes

- Desktop back-office, same 1440×927 shell as every other Regulatory Authority screen.
- Geo-tag and evidence are mandatory before submit (A-7 acceptance criteria).
