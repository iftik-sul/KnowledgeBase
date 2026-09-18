---
project: RERAN
module: regulatory-authority
type: ui-components
status: placeholder
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/ui/screens/"
tags:
  - regulatory-authority
  - ui-spec
  - components
---

# Regulatory Authority — UI Components (placeholder)

> **Generic component vocabulary.** The screen specs reference component *types*, not
> library component names. This file lists them so design work in Figma has a checklist to
> map onto the real library. It is deliberately not authoritative on naming — the real
> component names live in Figma, not here.

## Generic component types the specs reference

| Generic type | Used by | Likely existing analogue |
| :-- | :-- | :-- |
| Back-Office Sidebar (role-scoped) | all screens | adapt from existing portal sidebar |
| Top Bar (title, meta, search) | all screens | existing |
| KPI / Summary Card | Queue, Dashboard archetypes | existing |
| Data Table (filterable, paginated) | Queue archetype | FTI escrow-request-queue table |
| Status Badge | all | existing; wording per status-badges.md |
| Filter / Search Bar | Queue archetype | existing |
| Detail Panel (read-only field group) | Detail/Decision archetype | FTI application-details |
| Documents Panel (inline viewer) | Detail/Decision | existing |
| Live Check row (pass/attention indicator) | Application Review | new — registry checks |
| Decision Panel (mutually-exclusive outcomes + reason) | Detail/Decision | new — the core control |
| Record Editor / Form | Editor archetype | existing |
| Version / History list | Editor archetype | new |
| Session Timeline | Case Workspace | new |
| Audit-trail list | all | existing |

## Reconciliation checklist (for design work in Figma)

1. Map each generic type above to a real library component (or flag as genuinely new).
2. Confirm the Back-Office Sidebar is a variant of, or distinct from, the portal sidebar.
3. Identify the closest already-built screens (esp. FTI institution-side) to adapt rather
   than regenerate.

Figma build prompts are **not kept in this repo** — they drifted from the specs they claimed
to derive from. The screen specs remain the single source of truth for behaviour.
