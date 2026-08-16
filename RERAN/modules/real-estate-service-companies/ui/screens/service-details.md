---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/service-flows/"
  - "RERAN/modules/real-estate-service-companies/payments.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - service-details
---

# Screen: Service Details

**Access:** Any of the company's four Group D roles — identical screen for every user.

## Purpose

Give any company user everything they need to decide whether and how to apply for one specific service, before committing to the application form.

## Layout

```
Top Bar
↓
Service Header
↓
Overview
↓
Fees & Payment
↓
Eligibility & Prerequisites
↓
Required Documents
↓
Process Timeline
↓
Start Application (sticky action)
```

## Sections

### Section 1 — Service Header

Service name and number, category, one-line description, SLA where sourced.

### Section 2 — Overview

The service's own Purpose and Description, drawn directly from the corresponding `service-flows/service-NN-*.md` document — this screen does not maintain a separate copy of that text.

### Section 3 — Fees & Payment

* **Fee** — "No fee" (19 services), or "Set by RERA, configuration-based" where a fee applies.
* **When you pay** — one of four states, matching `payments.md` exactly:
  * "No fee for this service" (19 services)
  * "Paid after your application is reviewed and accepted" (#12–#15)
  * "Paid before your output is delivered, as the final step of submission" (#24)
  * "Payment timing depends on channel — Service Center or online" (#25, #26)

### Section 4 — Eligibility & Prerequisites

Drawn from the service's own Section 5 (Prerequisites).

### Section 5 — Required Documents

The service's own Section 7 list. Most are marked Proposed at the service-flow level — this screen inherits that status rather than asserting completeness.

### Section 6 — Process Timeline

A simplified version of the service's own Processing Workflow (Section 12). For Services #25/#26, shows both the Service Center and Online paths side by side, since the two channels genuinely differ in payment timing.

## Empty State

Not applicable — this screen only renders for one of the 25 selectable services.

## Reused Components

Top Bar, Information Cards, Status Badge, Buttons.

## Validation

1. Every field on this screen must trace to the corresponding service's own `service-flows/service-NN-*.md` document.
2. Fee timing must match `payments.md` exactly, per service.

## Access

Identical for all four roles.

## User Flow

```
Services Catalog
↓
Service Details
└─ Start Application → Submit Application, pre-populated with this service selected
```

**For Services #6 and #19 (email-only):** the sticky action changes from "Start Application" to a static instructional note directing the user to the appropriate email address, matching the module's own service-flow files' description of these two channels. No wizard opens.

## Notes

* This screen is read-only and pre-application — it does not collect any data.
* Services #6 and #19 are the only two in the catalogue where this screen doesn't lead into Submit Application at all.
