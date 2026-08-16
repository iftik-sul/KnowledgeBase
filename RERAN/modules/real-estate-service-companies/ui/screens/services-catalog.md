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

> **Corrected 2026-08-16, twice, by client decision.** **A2** — Service #18 is confirmed in Group D and now appears in this catalogue's Licensing category (8 of 8 services listed, not 7 of 8), though selecting it leads to a placeholder rather than the standard wizard — its own screen isn't designed yet. **B4** — Services #12–15's Fee Indicator label changes from "Pay after decision" to "Pay upfront," reflecting the normalization to pay-before-lodging.

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
| Real Estate Licensing Services | #12–#19 | 8 |
| Real Estate Rental Services | #20–#22 | 3 |
| Real Estate Transaction Services | #23–#24 | 2 |
| Real Estate Dispute Services | #25–#26 | 2 |

**Real Estate Licensing Services shows 8 selectable, matching `services-overview.md` exactly.** Service #18 (Real Estate Evaluation Details Certificate) is confirmed in Group D and listed here, per `open-questions.md` A2's 2026-08-16 client decision — the 7-of-8-selectable exclusion this screen previously carried is retired.

### Section 2 — All Services

Every one of the module's 26 services, as a card or row: name, one-line description, sourced or proposed SLA, and fee indicator.

| Field | Description |
| :---- | :---- |
| Service Name | e.g. "Register Owners Association" |
| Description | One line, drawn from the service's own Service Overview section |
| Fee Indicator | "Free" (19 services) · "Pay upfront" (#12–#15) · "Pay before output" (#24) · "Channel-dependent" (#25, #26) |
| Channel | Portal · Email-only (#6, #19) · Evaluation-request (#18 — see Notes) |
| SLA | Sourced figure where one exists |

**Fee Indicator's "Pay upfront" label replaces the previous "Pay after decision" for Services #12–#15**, per `payments.md`'s 2026-08-16 normalization — those four services now behave like most other upfront-paying services across the project.

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

1. Every one of the 26 services is now listed in this catalogue and reachable by every company user — no category or individual service hidden.
2. Fee Indicator badges must match `payments.md`'s current model split exactly.
3. Service #18 is listed, not excluded — but selecting it does not currently lead to Submit Application, since no screen exists for its own atypical shape yet. See Notes.

## Access

Identical for all four roles.

## User Flow

```
Dashboard
↓
Services Catalog
├─ Select Category → filtered All Services list
├─ Search → filtered All Services list
└─ Select Service → Service Details (or, for #18, a placeholder — see Notes)
```

## Notes

* **Service #6 and #19's email-only channel is surfaced as a Channel badge, not hidden.** Selecting either opens Service Details with a static instructional note rather than a Start Application button — matching the pattern established for Individual User's Service #40 and Financial & Trust Institutions' Service #23 (Accreditation of Training Entities), both similarly email-only.
* **Service #18 is now listed but leads to a placeholder, not a designed screen.** Its own sourced workflow — an evaluation company deciding on a customer's valuation request, not a company filing an application RERA reviews — doesn't fit either the standard Submit Application wizard or the simple email-instruction pattern used for #6/#19. Until its own screen is designed, selecting it from this catalogue should show a "This service's dedicated interface is still being designed" state rather than either silently failing or being force-fit into Service Details' standard layout.
* **Category counts (11/8/3/2/2 = 26) match `services-overview.md` exactly, and — as of 2026-08-16 — so does the selectable count.** This module's catalogue no longer has a gap between "documented" and "selectable" the way it briefly did pending Service #18's ownership resolution.
