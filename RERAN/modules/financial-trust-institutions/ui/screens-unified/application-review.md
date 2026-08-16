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
  - application-review
---

# Screen: Application Review

**Access:** Any of the institution's four Group C roles — identical screen for every user.

> **Regenerated 2026-08-15**, written fresh against the current corrected model.

## Purpose

A read-only, final checkpoint before an application is submitted — everything entered across [Submit Application](submit-application.md)'s steps, in one place, so a filer catches an error before it becomes a submitted record rather than after.

## Layout

```
Top Bar
↓
Review Summary
↓
Institution & Party
↓
Service-Specific Details
↓
Documents
↓
Payment Confirmation (where applicable)
↓
Declaration
↓
Submit (sticky action)
```

## Sections

### Section 1 — Review Summary

Service name and number, at-a-glance completeness indicator (every required field and document present), and an Edit link back into [Submit Application](submit-application.md) at the relevant step.

### Section 2 — Institution & Party

Read-only display of Submit Application's Section 2, with an Edit link.

### Section 3 — Service-Specific Details

Read-only display of Submit Application's Section 3 — the dynamic field set for the selected service — with an Edit link.

### Section 4 — Documents

Every attached document, by name and type, with a preview action. Missing required documents (if somehow reached in this state) block Submit and are shown in an error treatment, not silently omitted.

### Section 5 — Payment Confirmation

Shown only where the service charges a fee upfront (#1, #3–#11): the amount charged, VAT applied, payment method, and the Payment Receipt reference — confirming payment already succeeded in the prior step, not collecting payment here. **Not shown** for Service #2 (no fee) or Services #12–#18 (pay at point of service, not part of this flow).

### Section 6 — Declaration

A standard attestation — information provided is accurate to the best of the filer's knowledge — required before Submit is enabled. Not a signature in the legal sense; a checkbox confirming review has actually happened.

## Empty State

Not applicable — this screen only renders once every prior step in Submit Application has been completed.

## Reused Components

Information Cards, Status Badge, Buttons.

## Validation

1. Submit is disabled until the Declaration checkbox is checked.
2. Any Edit link, when used, returns to this screen after the edited step is resaved — a filer reviewing their application never loses their place by correcting one field.
3. Where payment was required, Submit is not reachable at all unless Section 5 shows a successful Payment Receipt reference — this mirrors [Submit Application](submit-application.md)'s own validation rule 1 rather than re-implementing it.

## Access

Identical for all four roles.

## User Flow

```
Submit Application (Review & Submit step)
↓
Application Review
├─ Edit (any section) → back to the relevant Submit Application step → Application Review
└─ Submit → confirmation → Applications (existing screen set), status Submitted or Pending Internal Certification
```

## Notes

* **This screen's natural reading is a review step inside the submission wizard, not a persistent post-submission record view.** That distinction was the source of the low-confidence mapping in issue #50's original catalogue pass, where this name was tentatively compared against `applications.md` (a searchable list) and `application-details.md` (a submitted record's full history). Written fresh, this screen is neither — it exists only between "finished filling out the form" and "submitted," and has no role once a record exists in the Applications list. A submitted record's ongoing status, certification, and audit trail are [application-details.md](../screens/application-details.md)'s job, in the existing 14-screen set, not this one's.
* Where a service routes to internal certification after submission (#3–#11, sourced), this screen's confirmation should say so explicitly — "Submitted for internal certification" rather than a generic "Submitted" — so a filer isn't surprised the record doesn't go straight to RERA.
