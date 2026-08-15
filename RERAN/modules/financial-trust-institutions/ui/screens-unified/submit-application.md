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
>
> **Resolved 2026-08-15.** Section 3's field set does *not* survive as a single generic layout across all eighteen services — see Section 3 below, rewritten to describe two layout patterns rather than one.

## Purpose

One dynamic form for all eighteen services. The shell — institution information, party/counterparty details, documents, payment, review — is identical for every service; only the service-specific transaction fields (Section 3 below) change per service, matching the field groups in each service's own `service-flows/service-NN-*.md` Section 6.

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

Pre-filled if arriving from [Service Details](service-details.md); otherwise a service picker identical to [Services Catalog](services-catalog.md)'s list. Confirms the service before the rest of the form renders, since every subsequent step depends on which of the eighteen is selected — including, as of this correction, which **layout pattern** the Details step itself uses.

### Section 2 — Institution & Party Information

Fixed shell fields, same for every service:

* Institution name, acting officer identifier (auto-filled from the signed-in user, editable where the application is filed on behalf of a different named officer)
* Represented party (borrower, lessee, heir, purchaser, or the institution itself for #1/#2/#18) — name, identification, contact details

### Section 3 — Service-Specific Details (dynamic)

**Corrected 2026-08-15 — this section does not use one layout for all eighteen services.** Two distinct patterns are needed, determined by the selected service's own `service-flows/service-NN-*.md` Section 6:

**Pattern A — Flat fields.** A single set of named inputs, one value each. This is most of the eighteen services. Example, **Mortgage Registration (#3)**: Loan Amount, Mortgage Term, Interest Rate, Mortgagee Details, Mortgage Deed Reference — five fields, five inputs, no repetition.

**Pattern B — Repeatable groups.** One or more sub-fields that repeat once per item in a variable-length list, with an add/remove control. **Confirmed needed for at least two services**, both found by checking their Section 6 directly rather than assuming Pattern A would do:

* **Sale Procedure — Heirs (#13):** Full Name, NIN, Contact Information, Share of the Estate, and Bank Account Details, each **per heir** — an application with three heirs needs three repeated groups of these five fields, not five fields total.
* **Split Ownership (#16):** Number of Resulting Parcels, then Owner(s) of Each Resulting Parcel — an application splitting a property into four parcels needs four repeated owner-detail groups, keyed to a number the applicant enters earlier in the same step.

A single static form template — the assumption this document carried before this correction — cannot render either of these without either an artificial cap on how many heirs or parcels an applicant can enter, or the add/remove repeatable-group control this correction now specifies.

**Not yet audited against the full eighteen.** Only #13 and #16 have been explicitly checked and confirmed to need Pattern B. The remaining sixteen are assumed to be Pattern A based on their Section 6 field lists reading as flat, but nobody has gone through all sixteen specifically looking for a repeatable structure the way #13 and #16 were found — Company Shares Sale (#14)'s "Selling Shareholder(s)" (plural) and Fund Company Registration (#12)'s beneficial-owner document requirement are two candidates worth checking before this list is treated as complete.

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

Progress Tracker, Document Uploader, Document Reference Picker, Information Cards, Buttons. **Added 2026-08-15:** a Repeatable Field Group component, for Pattern B services — add/remove a group of sub-fields, with a running count matching whatever quantity field precedes it in the same step (e.g. Split Ownership's Number of Resulting Parcels).

## Validation

1. **An application cannot advance past the Payment step, where one applies, until payment succeeds.** For #1 and #3–#11, this means the application cannot reach Review & Submit at all without a successful upfront payment — there is no draft-then-pay-later path.
2. Required documents (per the selected service's own Section 7) must all be attached before Review & Submit is reachable.
3. Section 3's field set is entirely determined by the service selected in Section 1 — changing the service selection after entering Section 3 data must warn that service-specific data will be lost, since the field sets are not compatible across services, and switching between a Pattern A and Pattern B service discards a different shape of data, not just different values.
4. **Added 2026-08-15.** For Pattern B services, the repeatable group count must match any quantity field that governs it (e.g. Split Ownership's parcel count vs. the number of owner groups actually filled in) before Review & Submit is reachable — a mismatch is an error, not a silent truncation or padding.

## Access

Identical for all four roles, for every one of the eighteen services. There is no service any role cannot initiate through this form.

## User Flow

```
Services Catalog / Service Details / Dashboard
↓
Submit Application
├─ Service Confirmation → Institution & Party → Service-Specific Details (Pattern A or B) → Documents →
│    [Payment, where applicable] → Review
└─ Review → Submit → Application Review confirmation → Applications (existing screen set)
```

## Notes

* **This is the one screen in the unified set with the clearest 1:1 purpose match to an existing screen** ([service-request.md](../screens/service-request.md)) — both are "one configurable form behind eighteen services." The design question this document previously carried as open — whether a single generic layout survives across all eighteen — is now resolved: it doesn't, for at least Services #13 and #16, and this document is corrected to specify a second layout pattern rather than assume the first one stretches to cover everything.
* **`service-request.md` (the existing single-form screen) has the identical unresolved question**, framed differently: its own Section 3 Transaction Details matrix lists "Heir/company/property reference — see each service's Required Information" for #13–#17 without flagging that #13 and #16 specifically need a repeatable structure a single-page form also has to build, not just a wizard step. This isn't a wizard-specific problem — whichever screen design is ultimately kept needs the Repeatable Field Group pattern for these services.
* **Payment step visibility is service-dependent, not a single fixed step.** This is a direct consequence of the two-model payment split (`payments.md`) and remains a separate, already-handled piece of this screen's design — unaffected by the Pattern A/B correction above.
* Whether internal certification (Pending Internal Certification status) is a step inside this wizard or something that happens entirely after submission, on a separate screen, is not resolved here — this document treats certification as post-submission, consistent with the existing [internal-certification-queue.md](../screens/internal-certification-queue.md) screen owning that step rather than this form.
