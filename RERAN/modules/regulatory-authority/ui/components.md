---
project: RERAN
module: regulatory-authority
type: ui-components
status: placeholder
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/ui/screens/"
tags:
  - regulatory-authority
  - ui-spec
  - components
---

# Group A — UI Components (placeholder)

> **Placeholder — to be reconciled to the real Figma component library in the Figma
> thread.** The screen specs reference generic component types; this file lists them so
> the Figma thread has a checklist to map onto the actual library (real component names,
> tokens, variants). It is intentionally not authoritative yet — the figma-prompts must
> reference the *real* library components, not these generic names.

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

## Reconciliation checklist (for the Figma thread)

1. Map each generic type above to a real library component (or flag as genuinely new).
2. Confirm the Back-Office Sidebar is a variant of, or distinct from, the portal sidebar.
3. Identify the closest already-built screens (esp. FTI institution-side) to adapt rather
   than regenerate.
4. Only then write the figma-prompts, referencing real component names.
