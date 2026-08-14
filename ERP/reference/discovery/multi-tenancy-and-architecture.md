---
project: ERP
type: requirements
status: current
updated: 2026-08-14
tags:
  - discovery
  - architecture
---

# Discovery: Multi-Tenancy and Core Architecture

Captured from design discussion with Saitama on reframing the project from a single-company build into a reusable platform.

## Decision context

The project began as a build for a single woven label manufacturer (two trade names: one used on Work Orders, a different one on Bills/Requisitions, same Dhaka address). A second company, Circle Packaging, was then brought on as a second reference case, which exposed that the original single-product assumption did not generalize. This prompted a full reframe: build a reusable platform any company can be configured onto, not a system hardcoded to one company.

## Multi-tenancy approach

Saitama's stated goal: build a reusable template first, convert to a SaaS model later. Agreed approach:

- Every table includes `company_id` from day one, even though only one company is active per deployment today.
- Phase 1: reusable template, one company configured/activated per deployment.
- Phase 2: flip to true multi-tenant SaaS — an auth/billing layer change, not a schema rewrite, because the isolation key already exists everywhere.

Rationale: retrofitting tenant isolation onto an existing schema later would touch every table and query. Including it now costs little while single-tenant.

## Company / letterhead config

The reference company operates under two trade names for the same business (one for Orders, a different one for Bills/Requisitions), same address. This was generalized: a Company can have multiple trade names/letterheads, each mapped to which document types it prints on, each with its own address or a shared one.

## Item Master generalization

Original build assumed single-product-per-company (woven labels only). Circle Packaging's 17-product portfolio (labels, stickers/tags, packaging materials, trims, add-ons) forced generalization: every company gets a first-class Item/Product Master (per-item UOM, variable rate basis, source-type/category field), even a single-product company that ends up with one row.

## Order model layering — open item

The core Order entity should hold only generic fields (customer, dates, status, line items, delivery, billing). Industry-specific fields (e.g., the woven-label build's O/No, Card, File#, Color Code 1-8) should not be fixed columns on the core schema — they need a custom-fields/metadata layer. **The actual mechanism for this layer (schema design, dynamic UI rendering per company) has not yet been designed.** This is the current top architectural priority — see modules/platform/README.md.
