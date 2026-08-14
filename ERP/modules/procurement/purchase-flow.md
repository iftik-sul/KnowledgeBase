---
project: ERP
module: procurement
type: process-flow
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Purchase Flow

## Raw material flow

1. Inventory Manager creates a Purchase Request (supplier, material, qty).
2. Admin approves.
3. Accounts pays.
4. Inventory Manager stocks the items in directly on arrival — no separate goods-received approval step (see modules/platform/decisions-log.md, D6).

## Non-raw-material purchases

Covers all other business purchases (office supplies, equipment, services). Approval chains differ by category and are configurable per company — tied to Roles configuration, not yet implemented.
