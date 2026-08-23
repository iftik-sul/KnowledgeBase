---
project: 3i
module: platform
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-PLT-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Platform — Validation Rules

---

## Audit Log Immutability

On [Admin Audit Log](screens/admin-audit-log.md): no edit or delete action exists anywhere in this screen's UI, for any row, regardless of admin permission level — see [data-model.md](../data-model.md#auditlog) for why an editable audit record isn't one. This isn't a permission the highest-privilege admin lacks; the action simply doesn't exist in the interface at all.