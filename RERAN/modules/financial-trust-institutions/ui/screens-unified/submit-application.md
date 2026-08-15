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
  - submit-application
---

# Screen: Submit Application

**Access:** Any of the institution's four Group C roles — identical screen for every user, for every one of the eighteen services.

> **This is the canonical form screen for all eighteen services, as of 2026-08-15.** The existing single-page `service-request.md` is retired in this screen's favour — see `ui/screens-unified/README.md` for the decision and reasoning. This screen is not a Figma-prompt draft any more; it is the module's one configurable application form.

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

Pre-filled if arriving from [Service Details](service-details.md); otherwise a service picker identical to [Services Catalog](services-catalog.md)'s list. Confirms the service before the rest of the form renders, since every subsequent step depends on which of the eighteen is selected — including which **layout pattern** the Details step itself uses.

### Section 2 — Institution & Party Information

Fixed shell fields, same for every service:

* Institution name, acting officer identifier (auto-filled from the signed-in user, editable where the application is filed on behalf of a different named officer)
* Represented party (borrower, lessee, heir, purchaser, or the institution itself for #1/#2/#18) — name, identification, contact details

### Section 3 — Service-Specific Details (dynamic)

**Full audit completed 2026-08-15.** All eighteen services' Section 6 (Required Information) checked individually. Three distinct patterns are needed, not one:

| Services | Pattern | Basis |
| :---- | :---- | :---- |
| #1, #2, #3–#11, #12, #17 (13 services) | **A — Flat fields** | One value per named field, single entity, no repetition. Checked individually, not assumed — e.g. #12's beneficial-owners list is a *document upload* (Section 7), not a repeatable form field, so it stays Pattern A despite involving multiple people. |
| **#13 (Sale Procedure — Heirs), #16 (Split Ownership)** | **B — Repeatable groups** | Confirmed against source: #13's heir fields (name, NIN, contact, bank details) are explicitly tagged "(per heir)" in `service-flows/`; #16's owner fields repeat once per resulting parcel, a count the applicant sets earlier in the same step. Both need an add/remove repeatable-group control, not a fixed field set. |
| **#15 (Update Title Deed Information)** | **C — Field-selection, conditional pairs** | A genuinely different problem from Pattern B: "Field(s) to be Updated" is not entity repetition — it's *attribute selection*. The applicant picks which recorded fields are changing, and the step then shows a Current Value / Requested New Value pair only for the fields picked. Needs a checklist-then-conditional-fields UI, not a repeatable-group UI. |
| **#14 (Company Shares Sale), #18 (Contract Cancellation)** | **Ambiguous — flagged, not resolved** | Both have plural, unstructured fields ("Selling Shareholder(s)," "Property Registration Number(s)," "Parties to the Contract") with no "(per X)" tag the way #13 has. The source genuinely doesn't disambiguate single-value-listing-multiple-names versus a true repeatable structure. **Default to Pattern A** (a single multi-value text field) until a product decision says otherwise — this is a safe, reversible default, not a resolution of the ambiguity. |

**Result: 13 Pattern A, 2 Pattern B, 1 Pattern C, 2 defaulted-to-A-but-flagged.** This is the complete picture across all eighteen services — no service remains unchecked.

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

Progress Tracker, Document Uploader, Document Reference Picker, Information Cards, Buttons. **Repeatable Field Group** — add/remove a group of sub-fields, count tied to a preceding quantity field, for Pattern B (#13, #16). **Conditional Field Selector** — a checklist that reveals a current/new value pair per item checked, for Pattern C (#15).

## Validation

1. **An application cannot advance past the Payment step, where one applies, until payment succeeds.** For #1 and #3–#11, this means the application cannot reach Review & Submit at all without a successful upfront payment — there is no draft-then-pay-later path.
2. Required documents (per the selected service's own Section 7) must all be attached before Review & Submit is reachable.
3. Section 3's field set — and its pattern (A, B, or C) — is entirely determined by the service selected in Section 1. Changing the service selection after entering Section 3 data must warn that service-specific data will be lost, since switching between patterns discards a different *shape* of data, not just different values.
4. For Pattern B services, the repeatable group count must match any quantity field that governs it (e.g. Split Ownership's parcel count vs. the number of owner groups actually filled in) before Review & Submit is reachable — a mismatch is an error, not a silent truncation or padding.
5. For Pattern C (#15), at least one field must be selected before Review & Submit is reachable — an empty "nothing is changing" submission is not a valid update.

## Access

Identical for all four roles, for every one of the eighteen services. There is no service any role cannot initiate through this form.

## User Flow

```
Services Catalog / Service Details / Dashboard
↓
Submit Application
├─ Service Confirmation → Institution & Party → Service-Specific Details (Pattern A, B, or C) → Documents →
│    [Payment, where applicable] → Review
└─ Review → Submit → Application Review confirmation → Applications (existing screen set)
```

## Notes

* **This screen replaces `service-request.md` outright, not alongside it.** The retire-vs-rewrite question from issue #50 is resolved: the field-matrix problem this screen surfaced (three patterns, not one) applies identically to a single-page form, so it was never a reason to prefer the single-page design. The wizard was chosen because the payment step's three-way conditional behaviour and the Pattern B/C UI needs are both cleaner as dedicated steps than as dynamically-appearing sections on one long page — see `ui/screens-unified/README.md` for the full reasoning.
* **Pattern C (#15) was not identified until the full audit.** The earlier partial pass (which found #13 and #16) treated "plural field name" as the signal to look for; #15's "Field(s) to be Updated" is plural for a different reason entirely — it names which attributes change, not how many people are involved. Worth remembering as a general lesson: a repeatable-entity problem and a conditional-attribute problem can look similar in a field list and are not the same UI problem.
* **#14 and #18 are defaulted, not resolved.** If the client or a later design pass determines either genuinely needs multiple structured entries (e.g. a shares sale with three distinct selling shareholders, each needing separate identification), both would move to Pattern B and need the same Repeatable Field Group component #13 and #16 already require — no new component, just a reclassification.
* Payment step visibility is service-dependent, not a single fixed step — a direct consequence of the two-model payment split (`payments.md`), unaffected by the Pattern A/B/C audit above.
* Whether internal certification (Pending Internal Certification status) is a step inside this wizard or something that happens entirely after submission, on a separate screen, is not resolved here — this document treats certification as post-submission, consistent with the existing [internal-certification-queue.md](../screens/internal-certification-queue.md) screen owning that step rather than this form.
