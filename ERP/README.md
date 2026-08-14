---
project: ERP
type: overview
status: current
updated: 2026-08-14
tags:
  - project
  - overview
---

# ERP

## Purpose

A unified, reusable ERP platform — designed to work for any company or industry, not hardcoded to one. The core (Financials, Procurement, Inventory, Manufacturing, HR, Sales & Billing, and cross-cutting Platform config) applies to any company. Industry-specific behavior is layered on as configuration and documented inline, per module, as an "Industry Variations" section — never as changes to the core schema.

Multi-tenant-ready from day one: every table carries `company_id`, so the same schema supports a single-company template deployment now and a true multi-tenant SaaS model later without a rewrite.

## Status

Active design phase. Two industry templates are in progress as proof cases:
- **Woven Label Manufacturing** — design substantially complete.
- **Circle Packaging** — early design phase; the live test case for the generalized Item Master.

This repository is the authoritative source of project knowledge, per [documentation-standards.md](/documentation-standards.md). Content is being migrated in from prior design conversations; treat anything not yet present here as not yet authoritative.

## Modules

See [project-standards.md](project-standards.md) for the full module definition and vocabulary.

| Module | Abbrev. | Covers |
|---|---|---|
| [platform](modules/platform/README.md) | PLAT | Multi-tenancy, company/letterhead config, Item Master, custom-fields layer, roles |
| [sales-and-billing](modules/sales-and-billing/README.md) | SLB | Order model, delivery, billing, multi-currency |
| [procurement](modules/procurement/README.md) | PROC | Purchase requests, approval chains, vendor management |
| [inventory](modules/inventory/README.md) | INV | Item/raw material stock, stock ledger |
| [manufacturing](modules/manufacturing/README.md) | MFG | Production Orders, BOM, material requisitions |
| [financials](modules/financials/README.md) | FIN | GL, AR, AP, cash management, financial reports |
| [hr](modules/hr/README.md) | HR | Employees, attendance, leave, payroll, shifts |

## Tech Stack

Node.js backend · Next.js frontend (mobile responsive) · Supabase database · Vercel deployment.

## Stakeholders

Saitama — product/design lead. Claude — architecture and system design collaborator. Figma AI — screen generation from structured prompts written by Claude and reviewed against these documents.

## Entry Points

The core `Order` entity is the platform's default entry point (no formal pre-Order Quotation stage exists in the core model). Whether some industries should get a Quotation → Accept → Order stage ahead of the core Order is an open question — see [modules/sales-and-billing/README.md](modules/sales-and-billing/README.md).
