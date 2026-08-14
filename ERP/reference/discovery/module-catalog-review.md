---
project: ERP
type: requirements
status: current
updated: 2026-08-14
tags:
  - discovery
  - scope
---

# Discovery: Standard ERP Module Catalog Review

Captured from a design session comparing this platform's scope against the standard module set found in commercial ERPs (SAP, NetSuite, Odoo, Dynamics). Used to identify what's covered, what's deliberately excluded, and what's a genuine gap.

## Method

Enumerated the standard module categories (Financials, Sales & CRM, Procurement, Inventory & Warehouse, Manufacturing/Production, Order Fulfillment/Logistics, HR/HCM, Project Management, Customer Service, Cross-cutting Platform Services) and mapped each sub-module to one of: designed, deferred, or deliberately out of scope.

## Key conclusion

This platform targets the SMB/mid-market make-to-order manufacturing and trading segment, not enterprise-scale ERP. The modules explicitly excluded are the ones that separate SMB-tier from SAP/Oracle-class systems:

- MRP (auto material planning from demand)
- Routing/Work Centers, Capacity Planning
- Lead/Opportunity CRM pipeline
- Multi-warehouse, Lot/Batch/Serial tracking, Cycle Counts
- Fixed Assets/Depreciation, Budgeting, Cost Centers
- Project time/expense billing
- Support tickets/SLAs
- Transportation Management, Returns/RMA
- Recruitment, Performance Management, Training (HR)

These are treated as deliberate scope boundaries, not oversights. Full per-sub-module status is broken out by module in each module's own documentation (see modules/*/README.md).

## Open question raised, not yet decided

Should some industries get a formal Quotation → Accept → convert-to-Order stage before the core Order, or does the platform stay "Order is the first document" everywhere? No decision made. See modules/sales-and-billing/README.md.
