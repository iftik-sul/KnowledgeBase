---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/services-overview.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - catalog
---

# Screen: Services Catalog

**Access:** Any authenticated Individual User — full catalog visible to everyone, per `navigation.md`'s Access Model (see Layout note on actionability).

## Purpose

Let a user browse and select from all 43 services, organized the way `services-overview.md` already categorizes them, rather than as a flat alphabetical list of 43 items.

## Layout

```
Search Bar
↓
Category Tabs / Accordion (8 categories)
↓
Service Cards (within selected category)
```

## Sections

### Section 1 — Search

Free-text search across all 43 service names, independent of category — a user who knows they want "Transfer Property Ownership" shouldn't have to know it's filed under Property Ownership & Transaction Services first.

### Section 2 — Categories

The 8 categories from `services-overview.md`, each expandable/tabbed:

| Category | Services |
| :---- | :---: |
| Verification Services | 3 |
| Property Ownership & Transaction Services | 14 |
| Title & Land Registration Services | 7 |
| Tenancy Services | 7 |
| Power of Attorney Services | 3 |
| Property Information & Certificate Services | 5 |
| Diaspora Services | 2 |
| Consumer Protection Services | 2 |

### Section 3 — Service Cards

Each card shows: service name, one-line description (from each service-flow file's Purpose section), fee indicator (chargeable / free / conditional / **depends on selection** — see the #30/#37 note below — matching `payments.md`'s findings, not a generic "chargeable" assumption), and expected processing time. Selecting a card opens [Service Details](service-details.md).

**Fee indicator accuracy matters here specifically** — this is the first place a user sees whether a service costs money, and `payments.md`'s audit found the module's own documentation got this wrong for at least 5 services before correction. The catalog must read fee status from the corrected service-flow files, not from any older assumption that "everything is chargeable."

## Empty State

Not applicable — the catalog always has content; it doesn't depend on the user's own data.

## Reused Components

Search Bar, Buttons.

## Validation

Category counts must sum to 43 and match `services-overview.md`'s own Business Services Summary table exactly — if that table is ever corrected, this screen's counts must be corrected the same day, not left to drift (the same standing instruction that governed the analysis-layer work).

## Access

Every service is browsable by every user, including services the user's account can't currently act on (e.g. Transfer Property Ownership, if they own no property). Actionability is enforced at the wizard's Property/Lease Selector step, not by hiding cards here — matches the Access Model's "see everything, act on what applies" principle.

## User Flow

```
Dashboard / Sidebar → Services Catalog → Service Details → Submit Application
```

## Notes

* #40 (Upload Building Details for Leasing) still appears as a catalog card even though it has no in-app wizard — its card, when selected, routes to a "this is an email-based process" explanation rather than Service Details' usual "Start Application" button. See `ui/README.md`.
* #30 and #37's cards route into a different first step (PoA/identity validation) rather than straight into the wizard's field-collection steps — see [submit-application.md](submit-application.md). **Their fee indicator, added 2026-08-15:** neither has an independent fee status of its own — both were corrected to explicitly inherit whichever fee/timing rule the eventually-selected underlying service carries (`payments.md` Category 9). Their cards show "depends on selection" rather than a fixed chargeable/free/conditional label, since no single answer is accurate until the user picks what they're actually doing. This gap was found in the same audit pass that fixed #30 and #37's own files — the catalog's fee-indicator options had never been extended to cover them.
