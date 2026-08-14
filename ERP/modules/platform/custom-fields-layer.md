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

A Woven Label Order Line needs a Pick/Acc field. A Plastic Bag Order Line does not. Neither should require a schema migration, and neither company's (or category's) field choices should affect another's table structure. The core schema must stay identical for every company regardless of industry — and, since a single Order can now mix categories across its lines, the scoping has to work at the **line** level, not the whole Order.

## Design

**`field_definitions` table** — configuration, not transactional data.

| Column | Purpose |
|---|---|
| `company_id` | Whose field this is |
| `document_type` | Which entity it attaches to — `order_line`, `order`, `item`, `production_order`, and any future entity that needs custom attributes |
| `field_key` | Machine key, e.g. `pick_acc` |
| `label` | Display name, e.g. "Pick/Acc" |
| `field_type` | `text` \| `number` \| `date` \| `select` \| `textarea` |
| `validation_pattern` | Optional regex, e.g. `^\d+/\d+$` for a slash-separated value |
| `options` | JSON array, for `select` type |
| `required` | Boolean |
| `display_order` | Render order on the form |
| `section` | Optional grouping label, e.g. "Production Details" |
| `active` | Soft-disable without deleting — historical records may still hold values under a retired field |

**On the entity record itself:** a single `custom_fields JSONB` column. No per-company columns are ever added to the core table.

**Scoping rule, given multi-category Orders:** category-specific fields (Pick/Acc, Color Code 1–8, etc.) are scoped `document_type: 'order_line'`, keyed to that line's Item category — not `document_type: 'order'`. This is what lets a Woven Label line and a Plastic Bag line coexist in the same Order, each rendering only its own category's fields. `document_type: 'order'` remains available, but only for fields genuinely true of the whole Order regardless of which categories its lines belong to (there are currently no confirmed examples of this — flagged as an open question rather than assumed).

`document_type` is not fixed to these values — some industries will need custom fields on the Item Master instead of any Order-related entity (e.g., a material property). The same table and mechanism cover that; only `document_type` differs.

## Industry category field templates

Each industry category (Woven Label, Packaging, and future categories) can define a default field-definition template — a starter set of `field_definitions` rows, scoped `document_type: 'order_line'`, not yet tied to any company. When a new company selects a category during setup, the system copies that template's rows into the company's own `field_definitions`, scoped to `company_id`. The company can then edit or remove any of them.

## Validation

`validation_pattern` (and `required`) are enforced at save time against the field definition, not hardcoded in application code per company.

## UI rendering rule — Figma prompt risk

The custom-fields section of an Order Line (in an Order-creation screen with multiple lines) must be prompted as a **dynamic, per-line, data-driven field list**, rendered from that line's Item category's active `field_definitions` — not a fixed set of inputs, and not one field set applied uniformly to every line in the Order. This compounds the existing dynamic-rows risk already flagged for line items generally: Figma AI may not only collapse the field list into fixed inputs, but may also apply one line's fields to every line in a multi-category Order. Every future prompt for an Order-creation screen must state this explicitly.

## Open sub-decisions (not yet resolved)

- Whether `field_definitions` are versioned (what happens to old Order Line data if a field's type changes after records exist).
- Whether/how custom field values become reportable (filterable in list views, exportable).
- Whether any genuinely whole-Order (not per-line) custom fields actually exist in practice, or whether `document_type: 'order'` for custom fields turns out to be unused.
