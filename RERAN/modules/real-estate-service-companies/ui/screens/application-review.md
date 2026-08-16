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

> **Corrected 2026-08-16, by client decision (`open-questions.md` B4).** Section 5 (Payment Confirmation) now shows for Services #12–#15 as well as #24 and #25/#26 online, since all of these now pay during submission.

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

**Shown for Services #12–#15, #24, and #25/#26 (online channel)** — the amount charged, payment method, and Payment Receipt reference, confirming payment already succeeded in the prior step. **Not shown** for the 19 no-fee services.

**Corrected 2026-08-16** — previously excluded #12–#15 from this section, since those four services paid after submission at the time. With B4's normalization, they pay during submission like every other fee-bearing service this wizard handles, and this section now covers all of them uniformly.

### Section 6 — Declaration

A standard attestation — information provided is accurate to the best of the filer's knowledge — required before Submit is enabled.

## Empty State

Not applicable — this screen only renders once every prior Submit Application step is complete.

## Reused Components

Information Cards, Status Badge, Buttons.

## Validation

1. Submit is disabled until the Declaration checkbox is checked.
2. Any Edit link returns to this screen after the edited step is resaved.
3. Where payment was required during submission (now every fee-bearing service this wizard handles), Submit is not reachable unless Section 5 shows a successful Payment Receipt reference.

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

* **This screen's confirmation message no longer needs a #12–#15-specific variant.** The Phase 4 version of this file proposed "Submitted for RERA review. You will be notified when payment is due" for those four services specifically, since payment happened after submission at the time. With B4's normalization, a single confirmation message works for every service this wizard handles: payment (where applicable) has already succeeded by the time this screen's Submit action fires.
* No internal certification loop exists anywhere in this module (`open-questions.md` A5), so this confirmation message never needs to distinguish "submitted for internal certification" from "submitted to RERA" — every submission goes straight to RERA.
