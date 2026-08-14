---
project: ERP
module: platform
type: overview
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Platform Module

Cross-cutting architecture that every other module depends on: multi-tenancy, company/letterhead configuration, the Item Master, the custom-fields layer, and roles.

## Documents

| Document | Status |
|---|---|
| [architecture.md](architecture.md) | Current |
| [custom-fields-layer.md](custom-fields-layer.md) | Current |
| [decisions-log.md](decisions-log.md) | Current |

## Open work

Custom field values are not yet reportable (filterable in list views, exportable) — the current mechanism covers capture and display only. See "Open sub-decisions" in [custom-fields-layer.md](custom-fields-layer.md).
