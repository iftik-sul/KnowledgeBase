---
project: ERP
module: procurement
type: overview
status: current
updated: 2026-08-14
---

# Procurement Module

Purchase requests, approval chains, and vendor management. Covers all business purchases, not just raw materials — including order-linked sourcing (buying a specific item to fulfill a customer Order Line, as opposed to restocking general inventory).

## Documents

| Document | Status |
|---|---|
| [purchase-flow.md](purchase-flow.md) | Current — raw material flow defined; non-raw-material approval chains deferred |
| [sourcing-order.md](sourcing-order.md) | Current — order-linked Make/Buy fulfillment, wraps the Purchase Request flow |

## Open work

Non-raw-material approval chains (which differ by purchase category) are deferred, tied to the Roles implementation (see modules/platform/architecture.md). Whether Sourcing Order purchases get their own approval category, or fall under "non-raw-material," is not yet decided.
