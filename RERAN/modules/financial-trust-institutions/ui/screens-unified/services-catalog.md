---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - unified-portal
  - services-catalog
---

# Screen: Services Catalog

**Access:** Any of the institution's four Group C roles — identical screen for every user.

> **Regenerated 2026-08-15**, written fresh against the current corrected model. **Corrected 2026-08-16.** The Fee Timing field (Section 2) previously described a four-way split, since Services #12 and #18 then sourced payment *after* RERA's decision. The client has since normalized both to pay before RERA's decision, the same as #13–#17. Back to three values.

## Purpose

Let any institution user browse and start any of the eighteen services, organized the way an institution user thinks about them — by task — rather than by RERA's internal filing categories.

## Layout

```
Top Bar
↓
Search Bar
↓
Category Cards
↓
All Services (filterable list)
↓
Recent / Frequent Services
```

## Sections

### Section 1 — Category Cards

Five cards, matching `services-overview.md`'s proposed grouping:

| Category | Services | Count |
| :---- | :---- | :---: |
| Institutional Approval Services | #1, #2 | 2 |
| Mortgage Services | #3–#7 | 5 |
| Finance Lease Services | #8–#11 | 4 |
| Title & Ownership Transaction Services | #12–#17 | 6 |
| Contract Services | #18 | 1 |

Selecting a card filters the All Services list below to that category. This grouping is itself proposed and unconfirmed by the client (`open-questions.md` C1) — the underlying eighteen services and their numbering are sourced and fixed regardless of how this screen labels the five groups around them.

### Section 2 — All Services

Every service, as a card or row (implementation detail, not specified here): name, one-line description, sourced or proposed SLA, and whether it charges a fee and when.

| Field | Description |
| :---- | :---- |
| Service Name | e.g. "Mortgage Registration" |
| Description | One line, drawn from the service's own Service Overview section |
| Fee Timing | "Pay upfront" (#1, #3–#11) · "Pay at counter, before decision" (#12–#18) · "No fee" (#2 only) |
| SLA | Sourced figure where one exists, otherwise omitted rather than guessed |
| Assisted Mode Available | Badge where the service has a Trustee Centre / Land Department assisted path (C2) |

**Corrected 2026-08-16 — Fee Timing back to three values, not four.** This field briefly carried a four-way split ("pay at counter, before decision" for #13–#17 vs. "pay at counter, after decision" for #12/#18), added when a fuller audit found #12/#18 genuinely sourced a different timing. The client has since reviewed that sourced timing directly and confirmed it was an artefact of the original physical-counter process rather than intentional design, normalizing #12 and #18 to match #13–#17. All six services (#12–#18) now share the same "pay at counter, before decision" badge.

**Filters:** Category · Fee Timing · Assisted Mode Available

**Search:** by service name or number.

Selecting a service opens [Service Details](service-details.md).

### Section 3 — Recent / Frequent Services

A short row above or beside the full list: the current institution's most recently used and most frequently used services, institution-wide — not filtered to the viewer's own usage, consistent with the unified-access model.

## Empty State

Not applicable to the catalogue itself (always populated — eighteen services always exist). Applies only where a filter/search combination matches nothing:

> No services match these filters.

**Primary Button:** Clear Filters

## Reused Components

Institution Operations Sidebar, Top Bar, Filter Bar, Buttons.

## Validation

1. Every one of the eighteen services is reachable by every institution user — there is no category or individual service hidden from any role, consistent with `open-questions.md` A4.
2. Fee Timing badges must match `payments.md`'s current timing split exactly — three values. A service showing the wrong badge is a factual error, not a display preference.

## Access

Identical for all four roles. No service is hidden, greyed, or shown as "not available to your role" anywhere on this screen.

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

* **The five-category grouping is a proposed regrouping, not sourced structure** — see `services-overview.md`'s own note on this. If the client rejects the five-category framing (C1), this screen's Category Cards section needs rework, but the underlying eighteen-service list and Service Details linkage do not.
* **Service #2 needs a visibly distinct treatment from the other seventeen** — it's the only service in the catalogue with no fee at all (`open-questions.md` B11). A "Free" badge or equivalent should be unmistakable, not just the absence of a price.
* **#12 and #18's payment timing is resolved, not merely flagged, as of 2026-08-16.** This section previously noted the two services' "pay after decision" timing as worth confirming with the client — whether it was intentional design or an artefact of the source's counter-based process that should be normalized once digitized. The client has since confirmed the latter and normalized both services to pay before RERA's decision, closing that open item.
* Assisted-mode availability is sourced per-service, not uniform — see each service's own Section 4 (Who Can Apply) and Section 12 (Processing Workflow) in `service-flows/` for which services actually carry a Trustee Centre or Land Department path.
