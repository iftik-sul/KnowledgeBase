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
**Rationale:** The Packaging category's reference deployment proved the single-product assumption doesn't generalize. Building it in from the start avoids a second migration.

## D3 — Order model split into core entity + custom-fields/metadata layer

**Decision:** The core Order entity holds only generic fields. Industry-specific fields attach via a separate metadata layer.
**Alternatives considered:** Nullable columns per industry added to the core Order table as needed; a per-industry table subclassing approach.
**Rationale:** Nullable-columns-per-industry doesn't scale — every new industry category would widen and pollute the core table.
**Status: resolved, then refined.** Mechanism designed — see [custom-fields-layer.md](custom-fields-layer.md). Originally scoped fields to the whole Order; **superseded by D15** once it became clear an Order can span multiple industry categories in a single Order.

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

**Decision:** Industry-specific behavior is documented under an "Industry Variations" section inside the relevant functional module's document, not as its own top-level module.
**Alternatives considered:** A dedicated `industry-templates/` module with one sub-module per industry.
**Rationale:** Keeps a generic rule and its industry-specific deviation adjacent and easy to compare, rather than requiring a reader to cross-reference two separate module trees.

## D10 — Industry variations are named at the industry-category level, never after a client company

**Decision:** Industry Variations sections are named by industry category (e.g., "Woven Label," "Packaging," "Plastic"), not by the specific client company whose process informed the profile (previously "Woven Label Manufacturing" and "Circle Packaging," both actual client/company names).
**Alternatives considered:** Keep naming variations after the reference client, since that's where the requirements actually came from.
**Rationale:** The platform's premise is that any company in an industry can be configured onto the same profile — naming a variation after one client implies the profile is specific to that client, undermining the reusability the platform is built for. Company-specific facts (e.g., a particular company's address or exact letterhead names) stay out of the category-level documentation entirely; only industry-general patterns belong there.

## D11 — New industry categories are only documented from real discovery, never invented to test genericity

**Decision:** A new `### <Category>` section only enters `modules/` once a real reference case (actual client requirements) exists for it. Genericity is validated by designing the underlying mechanism (e.g., the custom-fields layer, D3) to be provably config-driven, not by writing speculative examples for hypothetical industries.
**Alternatives considered:** Add plausible categories (e.g., Plastic Bottle) proactively, based on general knowledge of those industries, to stress-test the platform ahead of real demand.
**Rationale:** An invented business rule that reads plausibly is worse than a gap — it looks authoritative but isn't backed by anything real, and someone will build against it as if it were validated. The actual test of "any product should be addable" is whether onboarding a new category requires only configuration (field definitions, numbering, rate rules) with zero core schema changes — that's now verifiable directly from the custom-fields layer design, without needing to fabricate example industries.

## D12 — Order Line introduced as the atomic fulfillment unit, not the Order

**Decision:** Per-product data (custom fields, fulfillment tracking) attaches to a new **Order Line** entity, one per item within an Order — not to the Order as a whole.
**Alternatives considered:** Keep per-product data implicitly folded into "Production Order," one per product, as originally modeled.
**Rationale:** A single Order can contain items from multiple industry categories (e.g., a Woven Label item and a Plastic Bag item in the same Order). Category-specific fields and fulfillment logic cannot be scoped to the whole Order once that's true — they need a line-level home. Order Line is that home; Production Order becomes one possible fulfillment path for a line, not a synonym for it.

## D13 — Item Master gains `is_manufacturable`; determines default (not fixed) fulfillment path

**Decision:** Add `is_manufacturable` to the Item Master. Items not flagged this way are always sourced (no BOM exists for them). Items flagged `true` default to Production Order fulfillment but are not locked to it.
**Alternatives considered:** Fix the manufactured/outsourced choice permanently per item; decide it fresh with no default every time an Order Line is created.
**Rationale:** In practice, the company has a defined list of items it manufactures — that's a real default worth capturing. But a manufacturable item can still need to be sourced for a specific order (e.g., a capacity issue) without that becoming a permanent reclassification of the item itself. A default that's overridable per Order Line matches how the business actually operates, better than either a hard rule or no default at all.

## D14 — An Order Line can be split across Production Order(s) and Sourcing Order(s), including mid-course conversion

**Decision:** An Order Line's Balance Qty is computed across the combined qty committed to all its Production Orders and Sourcing Orders. A line does not have to resolve to exactly one fulfillment path; it can be partially manufactured and partially sourced, and a Production Order's remaining balance can be converted to a Sourcing Order after production has already started.
**Alternatives considered:** Require each Order Line to pick exactly one fulfillment path (Make or Buy) at creation, with no later change.
**Rationale:** A single up-front choice doesn't survive real production issues — a shortfall partway through a manufacturing run is a normal operational event, not an edge case, and the model needs to absorb it without cancelling or recreating the Order Line.

## D15 — Custom fields rescoped from Order to Order Line (supersedes the original D3 scoping)

**Decision:** Category-specific custom fields (`field_definitions`) are scoped `document_type: 'order_line'`, keyed to that line's item category — not `document_type: 'order'`.
**Alternatives considered:** Keep fields scoped to the whole Order (the original D3 design), and require a company to run a single-category Order.
**Rationale:** Once an Order can mix categories, whole-Order scoping is simply wrong — it would either force every line in an Order to share one category's fields, or force single-category Orders as an artificial constraint. Line-level scoping is what actually lets categories mix freely within one Order, which is the real requirement.

## D16 — Sourcing Order wraps a Procurement Purchase Request rather than a fully separate purchasing system

**Decision:** Sourcing Order is a thin, order-linked layer over the existing Procurement Purchase Request flow — same vendor-selection and approval/payment mechanics, plus a link back to the Order Line it fulfills and a status lifecycle mirroring Production Order.
**Alternatives considered:** Build a fully independent purchasing flow for order-linked sourcing, separate from the raw-material Purchase Request flow.
**Rationale:** The existing Procurement flow's approval/payment mechanics are already designed and don't need to be reinvented; what was missing was order-traceability, not a different approval process. A thin wrapper gets the traceability without duplicating the underlying purchasing system. Trade-off accepted: whether Sourcing Order purchases need their own approval category (distinct from raw material) is still open — see modules/procurement/README.md.
