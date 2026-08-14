---
project: ERP
module: platform
type: architecture
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Platform Architecture

## Multi-tenancy

Every table includes `company_id` from day one. Phase 1: reusable template, one company active per deployment. Phase 2: multi-tenant SaaS, same schema, isolation by `company_id` — an auth/billing layer addition, not a schema rewrite.

## Company entity

- A Company can have multiple trade names/letterheads.
- Each trade name maps to specific document types (e.g., one name on Orders, a different one on Bills/Requisitions).
- Each trade name can have its own address or share the parent company's.
- Numbering formats (Order Number, Card No, any document number) are configured per company, per document type — pattern + digit length, not hardcoded.
- Status workflows are configurable per company, not fixed globally.
- Chart of Accounts and Roles ship as default templates a company starts from and can edit.

## Item / Product Master

Always first-class, for every company — even a single-product company has one row.

| Field | Purpose |
|---|---|
| UOM | Per-item unit of measure |
| Rate basis | Pricing logic can differ per item, not one global rule |
| Source-type / category | Distinguishes item types; where needed, manufactured vs. traded |

## Order model layering

The core `Order` entity holds: customer, dates, status, line items, delivery, billing. Industry-specific fields must not be fixed columns on this schema — they belong in a custom-fields/metadata layer attached to the core Order.

**Status: the layer's mechanism (schema design, dynamic UI rendering) is not yet designed. Top open architectural item.**

## Roles (definable per company, implementation deferred)

Super Admin, Admin/MD, Sales/Order Entry, Accountant, Production Manager, Inventory Manager, HR.

## Core conventions

- Use "Customer" everywhere, not "Party".
- Date format: dd/mm/yyyy.
- Numbering formats are configurable per company/document type — not fixed platform-wide.

## Design system

Built during the Woven Label Manufacturing reference build; treated as the reusable default theme, company-brandable. Color tokens (neutral scale, primary blue, five production status colors), spacing scale (4–48px), typography (Inter, 12–24px, tabular figures for numeric columns), full component library (Sidebar, Top Bar, Data Table, Cards, Buttons, Status Tags, Form Inputs, Modals, Drawers, Tabs, Pagination, Empty States, File/Attachment Chips, Alert/Banner).

## Navigation / IA pattern

Two top-level sections (e.g., Production, Business), accordion items for grouped modules (Inventory, Delivery & Billing, Accounts, HR), flat items for frequently-used single screens, Lucide icons on all top-level items.

## Working principles

- Presentation-first prioritization: screens are sequenced by demo/presentation value, not workflow order.
- Architectural reasoning is provided before writing Figma prompts.
- Figma AI rendering risks (collapsing per-row dropdowns, filling placeholder rows with fake data) are flagged explicitly in prompts.
- Open decision points are surfaced before a default is assumed.
- Repeated blank blocks on paper/Excel forms are artifacts, not real structure — the ERP uses dynamic add/remove rows.
