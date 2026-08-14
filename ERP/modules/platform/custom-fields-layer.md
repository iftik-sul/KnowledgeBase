---
project: ERP
module: platform
type: architecture
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Custom Fields Layer

Resolves the mechanism flagged as undesigned in `architecture.md` (D3): how an industry-specific field attaches to a core entity without becoming a fixed column on the core schema.

## Problem

A Woven Label company needs a Pick/Acc field on its Orders. A Plastic Bag company does not. Neither should require a schema migration, and neither company's field choices should affect the other's table structure. The core `Order` (and `Item`, `Production Order`, etc.) schema must stay identical for every company regardless of industry.

## Design

**`field_definitions` table** — configuration, not transactional data.

| Column | Purpose |
|---|---|
| `company_id` | Whose field this is |
| `document_type` | Which entity it attaches to — `order`, `item`, `production_order`, and any future entity that needs custom attributes |
| `field_key` | Machine key, e.g. `pick_acc` |
| `label` | Display name, e.g. "Pick/Acc" |
| `field_type` | `text` \| `number` \| `date` \| `select` \| `textarea` |
| `validation_pattern` | Optional regex, e.g. `^\d+/\d+$` for a slash-separated value |
| `options` | JSON array, for `select` type |
| `required` | Boolean |
| `display_order` | Render order on the form |
| `section` | Optional grouping label, e.g. "Production Details" |
| `active` | Soft-disable without deleting — historical records may still hold values under a retired field |

**On the entity record itself** (e.g. `Order`): a single `custom_fields JSONB` column. No per-company columns are ever added to the core table. A value is stored as `{"pick_acc": "1652/72"}`; the shape of that JSON is entirely driven by that company's active `field_definitions` rows, not by the table schema.

This applies to `document_type` generically, not just Order — some industries will need custom fields on the Item Master instead of the Order (e.g., a material property). The same table and mechanism cover both; only `document_type` differs.

## Industry category field templates

Each industry category (Woven Label, Packaging, and future categories) can define a **default field-definition template** — a starter set of `field_definitions` rows not yet tied to any company. When a new company selects a category during setup, the system copies that template's rows into the company's own `field_definitions`, scoped to `company_id`. The company can then edit or remove any of them.

This is the actual mechanism that makes "add a new industry" a configuration exercise: a new category template is a set of rows in this table, not a schema change. A category can define fields that attach to `order`, to `item`, to both, or to neither — a category with no genuinely distinguishing fields needs no template rows at all.

## Validation

`validation_pattern` (and `required`) are enforced at save time against the field definition, not hardcoded in application code per company. A change to a company's validation rule is a config edit, not a deploy.

## UI rendering rule — Figma prompt risk

The custom-fields section of any entity-creation screen (e.g., Order Create) must be prompted as a **dynamic, data-driven field list** rendered from that company's active `field_definitions` for the relevant `document_type` — not as a fixed set of inputs. This is the same class of risk already flagged for dynamic line-item rows: Figma AI tends to collapse dynamic sections into what it sees in the reference example (i.e., it may hardcode Pick/Acc and Color Code 1–8 as permanent inputs). Every future prompt for an entity-creation screen must state this explicitly.

## Open sub-decisions (not yet resolved)

- Whether `field_definitions` are versioned (what happens to old Order data if a field's type changes after records exist) — likely `active: false` + a new field_key rather than mutating in place, consistent with the platform's general "never silently overwrite" versioning principle, but not formally decided.
- Whether/how custom field values become reportable (filterable in list views, exportable) — deferred; the mechanism above only covers capture and display, not analytics.
