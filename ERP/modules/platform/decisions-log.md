---
project: ERP
module: platform
type: decision
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
  - reference/discovery/module-catalog-review.md
---

# Platform Decisions Log

One `##` section per decision. Newest at the bottom. Superseded decisions are marked, not deleted.

## D1 — Multi-tenant-ready from day one via `company_id`

**Decision:** Every table includes `company_id`, even in the single-company deployment phase.
**Alternatives considered:** Add tenant isolation later, when/if true SaaS is needed.
**Rationale:** Retrofitting tenant isolation later touches every table and query. Including it now costs almost nothing while single-tenant, and makes the later SaaS conversion an auth/billing change rather than a data model rewrite.

## D2 — Item/Product Master is always first-class

**Decision:** Every company gets a real Item Master (UOM, rate basis, source-type/category), even a single-product company.
**Alternatives considered:** Keep the single-product assumption from the original build; add an Item Master only when a multi-product company needs it.
**Rationale:** Circle Packaging proved the single-product assumption doesn't generalize. Building it in from the start avoids a second migration.

## D3 — Order model split into core entity + custom-fields/metadata layer

**Decision:** The core Order entity holds only generic fields. Industry-specific fields attach via a separate metadata layer.
**Alternatives considered:** Nullable columns per industry added to the core Order table as needed.
**Rationale:** Nullable-columns-per-industry doesn't scale — every new industry template would widen and pollute the core table.
**Status: mechanism not yet designed** — top open item.

## D4 — Trade name / letterhead is a company-level config, not a hardcoded constant

**Decision:** A Company can have multiple trade names, each mapped to which document types it prints on.
**Alternatives considered:** Hardcode two fixed letterhead constants, as the original single-company build did.
**Rationale:** The reference company genuinely operates under two legal names for the same business. Generalizing made the pattern reusable instead of a one-off hack.

## D6 — No formal Goods Receipt step in procurement

**Decision:** Inventory Manager stocks purchased items in directly on arrival — no separate goods-received approval step.
**Alternatives considered:** Standard three-way match (PO → Goods Receipt → Invoice).
**Rationale:** Deliberate SMB-tier simplification; the extra step wasn't part of the real operating process being modeled.

## D7 — MRP, capacity planning, and CRM pipeline excluded from core scope

**Decision:** No Material Requirements Planning, no Routing/Work Center/Capacity Planning, no Lead/Opportunity CRM pipeline.
**Alternatives considered:** Build lightweight versions of each as "nice to have."
**Rationale:** These separate SMB-tier ERP from enterprise-tier systems. Excluding them keeps the platform focused; they can be added later as genuine extensions if an industry template requires one.

## D8 — Knowledge Base migrated to this repository as the source of truth

**Decision:** Project knowledge is maintained here, under `documentation-standards.md`, not as ad-hoc chat memory summaries.
**Alternatives considered:** Continue relying on chat memory alone.
**Rationale:** Memory is auto-summarized and can drift or lose nuance across reframes. A versioned, structured document set gives an explicit, reviewable, correctable record.

## D9 — Industry variations documented inline per module, not as separate top-level modules

**Decision:** Industry-specific behavior (Woven Label Manufacturing, Circle Packaging) is documented under an "Industry Variations" section inside the relevant functional module's document, not as its own top-level module.
**Alternatives considered:** A dedicated `industry-templates/` module with one sub-module per industry.
**Rationale:** Keeps a generic rule and its industry-specific deviation adjacent and easy to compare, rather than requiring a reader to cross-reference two separate module trees.
