---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/navigation.md"
  - "RERAN/modules/individual-user/service-flows/"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - properties
---

# Screen: My Properties

**Access:** Any authenticated Individual User — own properties only, never another account's.

## Purpose

The account's registered properties, and the actions available on each — the screen `navigation.md` flagged as needing a first-class-vs-inline decision; this package builds it as first-class (see that document's still-open item 1).

## Layout

```
Search / Filter
↓
Property Cards / List
↓
Per-Property Actions
```

## Sections

### Section 1 — Property List

Each row: address, property type, registration number, and Property Record Status badge (Registered, Under Mortgage, Under Lease-to-Own, Under Usufruct — see `status-badges.md`).

### Section 2 — Per-Property Actions

Selecting a property opens a detail view listing every service actionable against it, filtered from the full 43-service catalog to only those relevant to a property the account already owns: Transfer (#5), Sale (#6), Update Info (#7), Sale of Mortgaged Property (#8), Gift Transfer (#9), Lease-to-Own lifecycle (#10–#13), Usufruct lifecycle (#14–#16), Grant Completion (#18, if applicable), amendments and certificates (#19–#22, #31–#35), Register Lease (#23, as landlord), Register PoA (#29), Exchange (#43).

Each action opens [Submit Application](../screens-unified/submit-application.md) with this property pre-selected, skipping the Property Selector step the wizard would otherwise show.

## Empty State

**Message** (new account, no properties):

> No properties registered yet. Register a property you own, or verify one before purchasing.

Two actions: Register Property Ownership (#4), Verify Property (#3).

## Reused Components

Property Selector (inverted — this screen *is* the selector's underlying data), Status Badge, Buttons.

## Validation

The per-property action list must stay in sync with whichever services actually require "select a registered property owned by the applicant" as a prerequisite — this is the same list the Property Selector component (`components.md`) draws from, and the two must not diverge.

## Access

No role variation — every account sees only its own properties, which is not a role restriction, just what "own account" means.

## User Flow

```
Sidebar → My Properties → [select property] → Per-Property Actions →
  Submit Application (property pre-filled)
```

## Notes

* This screen doubles as the Property Selector component's data source when reached from inside the wizard rather than directly from the sidebar.
