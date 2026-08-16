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
  - application-review
---

# Screen: Application Review

**Access:** Any of the company's four Group D roles — identical screen for every user.

## Purpose

A read-only, final checkpoint before an application is submitted — everything entered across [Submit Application](submit-application.md)'s steps, in one place, so a filer catches an error before it becomes a submitted record.

## Layout

```
Top Bar
↓
Review Summary
↓
Company & Party
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

Service name and number, completeness indicator, Edit link back into Submit Application at the relevant step.

### Section 2 — Company & Party

Read-only display of Submit Application's Section 2, with an Edit link.

### Section 3 — Service-Specific Details

Read-only display of Submit Application's Section 3, with an Edit link.

### Section 4 — Documents

Every attached document, by name and type, with a preview action.

### Section 5 — Payment Confirmation

**Shown only for Service #24 and Services #25/#26 (online channel)** — the amount charged, payment method, and Payment Receipt reference, confirming payment already succeeded in the prior step. **Not shown** for the 19 no-fee services, or for Services #12–#15, whose payment happens after this point in the process entirely — see Submit Application's own Notes.

### Section 6 — Declaration

A standard attestation — information provided is accurate to the best of the filer's knowledge — required before Submit is enabled.

## Empty State

Not applicable — this screen only renders once every prior Submit Application step is complete.

## Reused Components

Information Cards, Status Badge, Buttons.

## Validation

1. Submit is disabled until the Declaration checkbox is checked.
2. Any Edit link returns to this screen after the edited step is resaved.
3. Where payment was required during submission (#24, #25/#26 online), Submit is not reachable unless Section 5 shows a successful Payment Receipt reference.

## Access

Identical for all four roles.

## User Flow

```
Submit Application (Review & Submit step)
↓
Application Review
├─ Edit (any section) → back to the relevant Submit Application step → Application Review
└─ Submit → confirmation → Applications
```

## Notes

* **For Services #12–#15, this screen's confirmation should say so explicitly** — "Submitted for RERA review. You will be notified when payment is due" — rather than a generic "Submitted" message that could read as though payment is already settled.
* No internal certification loop exists anywhere in this module (`open-questions.md` A5), so unlike Financial & Trust Institutions' equivalent screen, this confirmation message never needs to distinguish "submitted for internal certification" from "submitted to RERA" — every submission goes straight to RERA.
