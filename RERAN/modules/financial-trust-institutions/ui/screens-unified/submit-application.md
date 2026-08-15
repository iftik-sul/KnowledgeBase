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

**Full audit completed 2026-08-15, including #14 and #18 — resolved 2026-08-15.** All eighteen services' Section 6 (Required Information) checked individually. Three distinct patterns are needed, not one, and every service is now classified — none left flagged:

| Services | Pattern | Basis |
| :---- | :---- | :---- |
| #1, #2, #3–#11, #12, #17, #18 (14 services) | **A — Flat fields** | One value per named field, single entity, no repeatable-count control. Checked individually, not assumed — e.g. #12's beneficial-owners list is a *document upload* (Section 7), not a repeatable form field, so it stays Pattern A despite involving multiple people. **#18 added 2026-08-15** — see resolution note below. |
| **#13 (Sale Procedure — Heirs), #14 (Company Shares Sale), #16 (Split Ownership)** | **B — Repeatable groups** | #13 and #16 confirmed against explicit "(per heir)"/per-parcel structure in `service-flows/`. **#14 added 2026-08-15** — see resolution note below. All three need an add/remove repeatable-group control for at least one sub-block, not a fixed field set throughout. |
| **#15 (Update Title Deed Information)** | **C — Field-selection, conditional pairs** | A genuinely different problem from Pattern B: "Field(s) to be Updated" is not entity repetition — it's *attribute selection*. The applicant picks which recorded fields are changing, and the step then shows a Current Value / Requested New Value pair only for the fields picked. Needs a checklist-then-conditional-fields UI, not a repeatable-group UI. |

**Result: 14 Pattern A, 3 Pattern B, 1 Pattern C. All eighteen services resolved — nothing left flagged or defaulted.**

**Resolution of #14 and #18 (2026-08-15).** Both were previously left as "ambiguous, defaulted to Pattern A" after the initial audit found plural, unstructured fields with no explicit "(per X)" tag. Resolved by reasoning from typical Nigerian corporate and real-estate practice rather than waiting on a source that doesn't disambiguate — **Medium confidence, a design judgement, not sourced data**, same confidence level the rest of this module uses for unsourced proposals:

* **#14 (Company Shares Sale) → Pattern B.** The source names "Selling Shareholder(s)" with the plural marker, but "Purchasing Party" without one — that asymmetry is itself a signal, not noise. Nigerian private companies (under CAMA 2020) commonly have multiple shareholders, and a single share-sale transaction converging several sellers into one buyer — co-owning family members each selling their stake in one filing, for example — is an ordinary shape for this transaction type, not an edge case. Each selling shareholder needs their own name, shareholding, and identification to support the share transfer instrument; that's a repeatable group (Selling Shareholder(s)) inside an otherwise flat form (Purchasing Party, Number/Percentage of Shares Sold, Sale Value, Agreed Sale Date stay Pattern A), the same hybrid shape #13 and #16 already have.
* **#18 (Contract Cancellation) → Pattern A, not B.** "Parties to the Contract" carries none of the per-party identification fields (no NIN, no contact, no bank details) that #13/#14/#16 all have — it reads as a reference line naming who's involved, not a structured multi-entity capture. Nigerian real estate contracts are also typically bilateral (buyer/seller, lessor/lessee). This stays Pattern A, sized to hold a small, fixed set of party names rather than an unlimited add/remove control — a genuinely different shape of problem from #13/#14/#16's variable-count case, not a weaker version of it.

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

Progress Tracker, Document Uploader, Document Reference Picker, Information Cards, Buttons, **Repeatable Field Group** (Pattern B — #13, #14, #16), **Conditional Field Selector** (Pattern C — #15). Both are now formally defined in [components.md](../components.md).

## Validation

1. **An application cannot advance past the Payment step, where one applies, until payment succeeds.** For #1 and #3–#11, this means the application cannot reach Review & Submit at all without a successful upfront payment — there is no draft-then-pay-later path.
2. Required documents (per the selected service's own Section 7) must all be attached before Review & Submit is reachable.
3. Section 3's field set — and its pattern (A, B, or C) — is entirely determined by the service selected in Section 1. Changing the service selection after entering Section 3 data must warn that service-specific data will be lost, since switching between patterns discards a different *shape* of data, not just different values.
4. For Pattern B services, the repeatable group count must match any quantity field that governs it (e.g. Split Ownership's parcel count vs. the number of owner groups actually filled in; Company Shares Sale has no separate quantity field, so the count is simply however many shareholder groups the filer adds) before Review & Submit is reachable — a mismatch, where a quantity field exists, is an error, not a silent truncation or padding.
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
* **#14 and #18's resolution is a design judgement, not a sourced fact — flagged at Medium confidence, matching this module's own convention for unsourced proposals.** If the client's actual practice differs (e.g. Contract Cancellation genuinely needs full per-party identification in some cases, or Company Shares Sale transactions at this institution are always single-seller), the classification should be revisited against real transaction data rather than treated as settled.
* Payment step visibility is service-dependent, not a single fixed step — a direct consequence of the two-model payment split (`payments.md`), unaffected by the Pattern A/B/C audit above.
* Whether internal certification (Pending Internal Certification status) is a step inside this wizard or something that happens entirely after submission, on a separate screen, is not resolved here — this document treats certification as post-submission, consistent with the existing [internal-certification-queue.md](../screens/internal-certification-queue.md) screen owning that step rather than this form.
