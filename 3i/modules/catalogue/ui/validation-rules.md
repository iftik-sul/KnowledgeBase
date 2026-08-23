---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CAT-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Catalogue — Validation Rules

Field-level validation shared across two or more catalogue screens.

---

## Age Field — No Default

On [Course create / edit](screens/course-create-edit.md): `minimumAge` has **no pre-selected value, ever** (FR-CRS-02). Not a dropdown defaulting to "5", not a blank that silently saves as some fallback — the save action itself is refused with a specific validation message until the instructor makes an explicit choice. This applies at **every** save, including intermediate drafts, not only at publish.

## Publish Gate

On [Course create / edit](screens/course-create-edit.md): the **Publish** action is disabled (not hidden — an instructor should see the action exists and understand why it's unavailable) until all three publish-gate conditions are met: age tag present, thumbnail uploaded, and at least one material or batch exists (FR-CRS-03). See [data-model.md](../data-model.md#publish-gate) for the full status-transition table. The two content-existence checks are forward-referenced to `materials` and `learning-delivery` — until those modules exist, this gate condition cannot actually be evaluated and should be treated as **not satisfied** (fail closed, never fail open) rather than skipped.

## Category Requirement

Category is **required at save**, same strictness as the age field — a course cannot exist uncategorised. Unlike age, category has no safeguarding weight; it's required for catalogue usability (filtering, FR-CRS-08 depends on every course having one).