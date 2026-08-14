---
project: ERP
type: standard
status: current
updated: 2026-08-14
tags:
  - standard
  - meta
---

# ERP Project Standards

This document declares ERP's vocabulary under the repository-wide rules in [/documentation-standards.md](/documentation-standards.md). Where the two differ, the repository standards win; this document only fills in what they leave to each project.

---

## What a Module Means Here

ERP is a platform serving one company at a time (multi-tenant-ready, not yet multi-tenant-live), where every company runs the same functional modules. **A module is a functional area** — not a user group, unlike RERAN. Every company that runs this platform uses the same module set; what varies per company is configuration and, for a handful of fields, industry-specific extensions.

| Module folder | Covers | Abbrev. | Status |
|---|---|---|---|
| `platform` | Multi-tenancy, company/letterhead config, numbering formats, Item Master, custom-fields layer, roles | PLAT | Architecture defined; custom-fields layer mechanism not yet designed |
| `sales-and-billing` | Order model, delivery, billing, multi-currency | SLB | Core model defined |
| `procurement` | Purchase requests, approval chains, vendor management | PROC | Core flow defined |
| `inventory` | Item/raw material stock, stock ledger | INV | Core model defined |
| `manufacturing` | Production Orders, BOM, material requisitions | MFG | Core model defined |
| `financials` | General Ledger, AR, AP, cash management, financial reports | FIN | Core model defined |
| `hr` | Employees, attendance, leave, payroll, shifts | HR | Core model defined |

---

## Industry Variations

Unlike a per-industry top-level module, industry-specific behavior is documented **inline, inside the functional module it varies from**, under a `## Industry Variations` heading in the relevant document. This keeps a generic rule and its industry-specific deviations next to each other instead of split across the repository.

**Naming rule:** industry variations are named at the **industry-category level** (e.g., "Woven Label," "Packaging," "Plastic"), never after the specific client company whose process happened to inform the profile. A category name must describe a class of companies any prospective client could recognize themselves in, not one deployment. If a rule turns out to be true only of one specific company rather than the industry as a whole, it belongs in that company's own configuration data, not in an Industry Variations section.

Current industry categories (config profiles on top of the core platform, not separate schemas):
- **Woven Label** — single-product-per-company legacy build; informed by an initial reference deployment.
- **Packaging** — multi-category product portfolio; the live test case for the generic Item Master and a trade-finance-heavy (PI/LC) workflow; informed by an initial reference deployment.

**Rule:** an Industry Variations section names the category explicitly (e.g., "Woven Label: adds Color Code 1–8 as a custom field on Order") rather than referring to it vaguely as "some companies." If a variation turns out to be common enough across categories that it stops looking like a variation, that's a signal to promote it into the core rule and remove the section — flag this rather than letting it linger.

---

## Stage Folders

ERP's derivation chain:

```
reference/discovery/  →  process-flows/  →  ui/
```

No `source-of-truth/` folder exists yet for this project — there is no client-supplied specification document; all input originates from our own discovery (design conversations). If a client-supplied document is ever received, `reference/source-of-truth/` is created at that point per the repository standard.

```
modules/<module-name>/
├── README.md                    # module index
├── <topic>.md                   # core rules for this module (data model, workflow) — module root, no stage folder
├── process-flows/
│   └── process-NN-<name>.md
└── ui/
    ├── README.md                 # screen index
    └── screens/
        └── <screen-name>.md
```

A module is not required to have every stage. Most modules currently have core-rule documents at the module root but no `process-flows/` or `ui/` content yet — that follows as Figma screens are generated and reviewed.

---

## Additional Document Types

Beyond the base types in the repository standards, ERP uses:

| Type | Purpose |
|---|---|
| `process-flow` | A business process: steps, actors, status transitions, triggers |
| `config-spec` | A company-configurable rule (numbering format, rate-calculation rule, status workflow) — documents the configuration mechanism, not one company's chosen values |

---

## File Naming

| Location | Pattern | Example |
|---|---|---|
| `process-flows/` | `process-NN-<name>.md` | `process-01-material-requisition.md` |
| `ui/screens/` | `<screen-name>.md` | `work-order-details.md` |
| module root | `<document-name>.md` | `order-model.md`, `decisions-log.md` |

---

## Decisions

Each module's `decisions-log.md` (module root, `type: decision`) records architectural decisions specific to that module, one `##` section per decision, newest at the bottom. Cross-module/platform-wide decisions live in `modules/platform/decisions-log.md`.

---

## Exceptions

None currently.
