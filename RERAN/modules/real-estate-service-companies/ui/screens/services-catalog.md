---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - services-catalog
---

# Screen: Services Catalog

**Access:** Any of the company's four Group D roles — identical screen for every user.

## Purpose

Let any company user browse and start any of the module's services, organized the way `services-overview.md` already categorizes them.

## Layout

```
Top Bar
↓
Search Bar
↓
Category Cards
↓
All Services (filterable list)
```

## Sections

### Section 1 — Category Cards

Five cards, matching `services-overview.md`'s categories:

| Category | Services | Count |
| :---- | :---- | :---: |
| Jointly Owned Property Services | #1–#11 | 11 |
| Real Estate Licensing Services | #12–#19 | 8 *(see note below)* |
| Real Estate Rental Services | #20–#22 | 3 |
| Real Estate Transaction Services | #23–#24 | 2 |
| Real Estate Dispute Services | #25–#26 | 2 |

**Real Estate Licensing Services shows 8 in the category count, matching `services-overview.md`, but only 7 are currently reachable through this catalogue.** Service #18 (Real Estate Evaluation Details Certificate) is documented in `service-flows/` but deliberately excluded from this catalogue's selectable list, per `navigation.md`'s provenance note — its own workflow doesn't fit the RERA-application shape every other catalogued service has. Selecting the Licensing category card shows a note explaining the exclusion rather than silently omitting the service with no explanation.

### Section 2 — All Services

Every selectable service (25, not 26 — see above), as a card or row: name, one-line description, sourced or proposed SLA, and fee indicator.

| Field | Description |
| :---- | :---- |
| Service Name | e.g. "Register Owners Association" |
| Description | One line, drawn from the service's own Service Overview section |
| Fee Indicator | "Free" (19 services) · "Pay after decision" (#12–#15) · "Pay before output" (#24) · "Channel-dependent" (#25, #26) |
| Channel | Portal · Email-only (#6, #19) |
| SLA | Sourced figure where one exists |

**Fee Indicator uses four values, not the simpler "chargeable / free" split other modules could get away with**, since `payments.md` found four genuinely distinct timing models for this module — the highest proportion of free services (19 of 26) of any module documented so far, worth making immediately visible here rather than defaulting to a "most services cost something" assumption.

**Filters:** Category · Fee Indicator · Channel

**Search:** by service name or number.

Selecting a service opens [Service Details](service-details.md).

## Empty State

Not applicable to the catalogue itself. Applies only where a filter/search combination matches nothing:

> No services match these filters.

**Primary Button:** Clear Filters

## Reused Components

Company Operations Sidebar, Top Bar, Search Bar, Filter Bar, Buttons.

## Validation

1. Every selectable service is reachable by every company user — no category or individual service hidden from any role.
2. Fee Indicator badges must match `payments.md`'s current model split exactly — four values.
3. Service #18 is excluded from the selectable list, with an explanatory note, not silently omitted.

## Access

Identical for all four roles.

## User Flow

```
Dashboard
↓
Services Catalog
├─ Select Category → filtered All Services list
├─ Search → filtered All Services list
└─ Select Service → Service Details
```

## Notes

* **Service #6 and #19's email-only channel is surfaced as a Channel badge, not hidden.** Selecting either opens Service Details with a static instructional note rather than a Start Application button — matching the pattern established for Individual User's Service #40 and Financial & Trust Institutions' Service #23 (Accreditation of Training Entities), both similarly email-only.
* **Category counts (11/8/3/2/2 = 26) match `services-overview.md` exactly**, even though only 25 services are selectable here — the count integrity is preserved at the category-total level; the exclusion is scoped narrowly to what this one screen's selectable list shows, per its own note above.
