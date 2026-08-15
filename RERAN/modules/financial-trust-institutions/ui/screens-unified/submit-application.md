---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/"
  - "RERAN/modules/financial-trust-institutions/payments.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - unified-portal
  - submit-application
---

# Screen: Submit Application

**Access:** Any of the institution's four Group C roles — identical screen for every user, for every one of the eighteen services.

> **Regenerated 2026-08-15**, written fresh against the current corrected model. This is the same design concept as the existing 13-screen set's [service-request.md](../screens/service-request.md) — one configurable form behind all eighteen services — redrawn as a wizard rather than a single long form, per this unified set's own structure.

## Purpose

One dynamic form for all eighteen services. The shell — institution information, party/counterparty details, documents, payment, review — is identical for every service; only the service-specific transaction fields (Section 4 below) change per service, matching the field groups in each service's own `service-flows/service-NN-*.md` Section 6.

## Layout

A progress-tracked wizard, not a single scrolling form:

```
Top Bar
↓
Progress Tracker (Service · Institution & Party · Details · Documents · Payment · Review)
↓
Current Step
↓
Step Navigation (Back / Continue)
```

## Sections

### Section 1 — Service Confirmation

Pre-filled if arriving from [Service Details](service-details.md); otherwise a service picker identical to [Services Catalog](services-catalog.md)'s list. Confirms the service before the rest of the form renders, since every subsequent step depends on which of the eighteen is selected.

### Section 2 — Institution & Party Information

Fixed shell fields, same for every service:

* Institution name, acting officer identifier (auto-filled from the signed-in user, editable where the application is filed on behalf of a different named officer)
* Represented party (borrower, lessee, heir, purchaser, or the institution itself for #1/#2/#18) — name, identification, contact details

### Section 3 — Service-Specific Details (dynamic)

The one section that changes per service. Pulls its field set directly from the selected service's own `service-flows/service-NN-*.md` Section 6 (Required Information) — e.g. Mortgage Registration shows loan amount, mortgage term, interest rate, mortgagee details; Split Ownership shows number of resulting parcels and boundary/share allocation. This document does not enumerate all eighteen field sets — each is the source-of-truth service-flow document's own Section 6, verbatim.

### Section 4 — Documents

Required and optional documents for the selected service, per its own Section 7. Supports both fresh upload and attach-by-reference from the institution's existing document repository.

### Section 5 — Payment

Shown or skipped depending on the service's payer/timing model:

* **Services #1, #3–#11** — payment step appears here, before the application can be submitted. Shared platform gateway checkout: card, bank transfer, or USSD.
* **Service #2** — this step is skipped entirely. No fee applies (`open-questions.md` B11).
* **Services #12–#18** — this step is skipped here; payment happens at the point of service (Trustee Centre counter or online checkout), not as part of this wizard.

### Section 6 — Review & Submit

Read-only summary of every prior step. See [Application Review](application-review.md) for the full specification of this step — it is substantial enough to warrant its own document rather than being folded into this one.

## Empty State

Not applicable — this screen is always mid-workflow once reached.

## Reused Components

Progress Tracker, Document Uploader, Document Reference Picker, Information Cards, Buttons.

## Validation

1. **An application cannot advance past the Payment step, where one applies, until payment succeeds.** For #1 and #3–#11, this means the application cannot reach Review & Submit at all without a successful upfront payment — there is no draft-then-pay-later path.
2. Required documents (per the selected service's own Section 7) must all be attached before Review & Submit is reachable.
3. Section 3's field set is entirely determined by the service selected in Section 1 — changing the service selection after entering Section 3 data must warn that service-specific data will be lost, since the field sets are not compatible across services.

## Access

Identical for all four roles, for every one of the eighteen services. There is no service any role cannot initiate through this form.

## User Flow

```
Services Catalog / Service Details / Dashboard
↓
Submit Application
├─ Service Confirmation → Institution & Party → Service-Specific Details → Documents →
│    [Payment, where applicable] → Review
└─ Review → Submit → Application Review confirmation → Applications (existing screen set)
```

## Notes

* **This is the one screen in the unified set with the clearest 1:1 purpose match to an existing screen** ([service-request.md](../screens/service-request.md)) — both are "one configurable form behind eighteen services." The genuinely open question, carried over from the earlier catalogue pass in issue #50, is whether the per-service Section 3 field matrix survives cleanly as a single generic step in a wizard, or whether some services' field sets are different enough in shape (not just content) to need their own step layout. This document assumes the former without proof.
* **Payment step visibility is service-dependent, not a single fixed step.** This is a direct consequence of the two-model payment split (`payments.md`) and is likely the single most—important behavioral difference this screen needs to get right, since getting it wrong means either charging Service #2 a fee it doesn't have, or asking #12–#18 to pay upfront when they should pay at the counter.
* Whether internal certification (Pending Internal Certification status) is a step inside this wizard or something that happens entirely after submission, on a separate screen, is not resolved here — this document treats certification as post-submission, consistent with the existing [internal-certification-queue.md](../screens/internal-certification-queue.md) screen owning that step rather than this form.
