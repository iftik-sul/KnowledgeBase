---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/"
  - "RERAN/modules/financial-trust-institutions/payments.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - unified-portal
  - service-details
---

# Screen: Service Details

**Access:** Any of the institution's four Group C roles — identical screen for every user.

> **Regenerated 2026-08-15**, written fresh against the current corrected model. **Corrected 2026-08-16.** Section 3 previously distinguished four fee-timing states, since Services #12 and #18 then sourced RERA's decision preceding the counter payment. The client has since normalized both services to pay before RERA's decision, the same as #13–#17. Back to three states.

## Purpose

Give any institution user everything they need to decide whether and how to apply for one specific service, before committing to the application form — fees, required documents, eligibility, and the process timeline.

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

Service name and number, category, one-line description, and the SLA where sourced.

### Section 2 — Overview

The service's own Purpose and Description, drawn directly from the corresponding `service-flows/service-NN-*.md` document's Sections 1–3 — this screen does not maintain a separate copy of that text; it displays whatever the source-of-truth service-flow file says.

### Section 3 — Fees & Payment

* **Fee** — "Set by RERA, configuration-based" (`open-questions.md` B5) rather than a hardcoded figure, since the exact amount is not sourced.
* **When you pay** — one of three states, matching `payments.md` exactly:
  * "Paid upfront, before your application is submitted" (#1, #3–#11)
  * "Paid at a Trustee Centre or the Land Department, before RERA reviews your application" (#12–#18)
  * "No fee for this service" (#2 only)
* **VAT** — "VAT applies" on every service except #2, per answer B7 (confirmed 2026-08-15, no exemptions).

**Corrected 2026-08-16.** This section previously listed four states, splitting #12/#18 (paid after approval) from #13–#17 (paid before). The client has since normalized #12 and #18 to pay before RERA's decision as well — the four-state list is retired, back to the original three-state split, now genuinely uniform across #12–#18 rather than an approximation.

### Section 4 — Eligibility & Prerequisites

Drawn from the service's own Section 5 (Prerequisites) in `service-flows/`. Where a prerequisite is itself proposed rather than sourced (several services flag this explicitly), the screen carries the same caveat rather than presenting it as settled.

### Section 5 — Required Documents

The service's own Section 7 (Required Documents) list. Most of these lists are themselves marked Proposed at the service-flow level — by analogy with similar services, not enumerated in source — and this screen inherits that status rather than asserting the list is definitively complete.

### Section 6 — Process Timeline

A simplified version of the service's own Processing Workflow (Section 12): who does what, in what order, ending in output delivery. Shows whether internal certification applies to this service (sourced for #3–#11; a configurable/open question for the rest) and whether an assisted-mode path exists.

**Corrected 2026-08-16** — this section previously called out #12/#18 specifically as paying after RERA's decision, "unlike the rest of the catalogue." That distinction no longer exists; every service's timeline now follows the same pattern within its payment model (upfront for #1/#3–#11, at-counter-before-decision for #12–#18).

## Empty State

Not applicable — this screen only renders for one of the eighteen known services.

## Reused Components

Top Bar, Information Cards, Status Badge, Buttons.

## Validation

1. Every field on this screen must trace to the corresponding service's own `service-flows/service-NN-*.md` document — this screen has no independent source of truth and must not diverge from it.
2. Fee timing and VAT applicability must match `payments.md` and `open-questions.md` B7 exactly, per service.

## Access

Identical for all four roles. Every service is fully visible to every user before they apply.

## User Flow

```
Services Catalog
↓
Service Details
└─ Start Application → Submit Application, pre-populated with this service selected
```

## Notes

* **This screen is read-only and pre-application.** It does not collect any data — that happens on [Submit Application](submit-application.md). Its job is entirely to inform the decision to apply, not to begin the application itself.
* Where a service's own Open Questions section (in `service-flows/`) flags something genuinely unresolved — e.g. which of several possible output documents applies, or whether a bank-originated path exists for a title & ownership service — this screen does not need to surface that uncertainty to the applicant; it's a documentation-completeness concern, not something an applicant needs to see before applying.
* **#12/#18's payment timing no longer needs special callout.** This section previously stressed surfacing #12/#18's post-approval payment timing clearly to applicants, since it broke from the #13–#17 pattern and could read as a broken flow if not flagged. That concern is moot now that all six services (#12–#18) share one timing.
