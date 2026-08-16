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
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - service-details
---

# Screen: Service Details

**Access:** Any of the company's four Group D roles — identical screen for every user.

## Purpose

Give any company user everything they need to decide whether and how to apply for one specific service, before committing to the application form.

> **Corrected 2026-08-16, three times, by client decision and by audit finding.** **B4** — Section 3's payment-timing description for Services #12–15 is corrected from "paid after decision" to "paid upfront." **A2** — this screen now renders for Service #18 too, though its Start Application action leads to a placeholder rather than Submit Application, since #18 has no designed wizard entry yet. **Audit correction** — Service #11 joins Services #6 and #19 as email-only; this screen's email-only references previously listed only two services.

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
  * "Paid upfront, before your application is submitted" (#12–#15) — **corrected 2026-08-16**, previously "Paid after your application is reviewed and accepted"
  * "Paid before your output is delivered, as the final step of submission" (#24)
  * "Payment timing depends on channel — Service Center or online" (#25, #26)

### Section 4 — Eligibility & Prerequisites

Drawn from the service's own Section 5 (Prerequisites).

### Section 5 — Required Documents

The service's own Section 7 list. Most are marked Proposed at the service-flow level — this screen inherits that status rather than asserting completeness.

### Section 6 — Process Timeline

A simplified version of the service's own Processing Workflow (Section 12). For Services #25/#26, shows both the Service Center and Online paths side by side, since the two channels genuinely differ in payment timing.

## Empty State

Not applicable — this screen renders for any of the module's 26 services.

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
    (or, for Service #18, a placeholder — see Notes)
```

**For Services #6, #11, and #19 (email-only):** the sticky action changes from "Start Application" to a static instructional note directing the user to the appropriate email address, matching the module's own service-flow files' description of these three channels. No wizard opens. **Corrected 2026-08-16** — previously named only Services #6 and #19; Service #11 was found during the same-day Phase 6 audit to be email-only as well.

**For Service #18:** the sticky action currently has nowhere designed to lead — see Notes.

## Notes

* This screen is read-only and pre-application — it does not collect any data.
* **Services #6, #11, and #19 are three of the four services in the catalogue where this screen doesn't lead into Submit Application** — corrected 2026-08-16, previously described as "two of the three," which undercounted both the email-only group (missing #11) and the total non-wizard group (missing the resulting fourth member).
* **Service #18 is the fourth — corrected 2026-08-16.** Previously excluded from the catalogue entirely pending its `open-questions.md` A2 provenance question; now confirmed to stay in Group D, so this screen renders for it, but Start Application has no designed destination yet. Until Service #18's own screen exists (see `ui/screens/submit-application.md`'s and `ui/screens/services-catalog.md`'s own Notes), this screen's Start Application button should show a "This service's dedicated interface is still being designed" state for #18 specifically.
