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
tags: [regulatory-authority, ui-spec, inspection, capture, mobile]
---

# Screen: Inspection Capture

**Archetype:** Capture / Form (on-site). **Form factor: mobile / tablet** — used in the field at the
building, not at a desk (per A-7 service flow).
**Access (RBAC-gated):** Inspection & Enforcement Officer. MFA required. Navigation is governed by [role-screen-matrix.md](../role-screen-matrix.md).

The on-site data-capture screen (A-7): the officer records geo-tagged findings, photos, and milestone
verification while physically at the site. Reached by tapping a scheduled inspection in the
[Inspection Queue](inspection-queue.md). On completion it produces the
[Inspection Report](inspection-report.md).

## Purpose

Let the officer capture geo-tagged, evidenced findings on the ground — the things documents alone
cannot confirm — quickly and reliably from a phone/tablet.

## Layout (mobile / tablet)

* **Visible Sidebar:** none — mobile top bar with a Back affordance to the queue.
* **Top Bar Title:** {Site / project} — Inspection
* Single-column, stacked, touch-first form.

```
Mobile Top Bar → Site header (with geo-tag capture) → Milestone / checklist → Findings +
Photo evidence → Overall result → Submit (produces report)
```

## Sections

### Section 1 — Site header + geo-tag

Site / project reference and filed location, plus a **Capture location** control that records the
device's geo-tag and shows it against the filed location (match / mismatch indicator). Geo-tagging is
mandatory (A-7 business rule).

### Section 2 — Milestone / checklist

The inspection checklist for the matter — each item a pass/fail/NA control (mobile toggle or radio),
e.g. construction milestone verification for a RED field visit.

> **Proposed** — the specific checklist items are not detailed in current source (A-7 §7 marks the
> procedure/checklist as proposed).

### Section 3 — Findings + photo evidence

Per finding: a short note (text) + one or more **photos** captured from the device camera. Evidence
must be attached (A-7 business rule: findings geo-tagged and evidenced).

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

- **Mobile/tablet form factor**, camera + location permissions required. Design for one-handed,
  on-site use.
- Geo-tag and evidence are mandatory before submit (A-7 acceptance criteria).
