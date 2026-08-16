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
  - submit-application
---

# Screen: Submit Application

**Access:** Any of the company's four Group D roles — identical screen for every user, for every one of the 25 selectable services.

## Purpose

One dynamic form for the module's 25 selectable services (all except Service #18 — see `navigation.md`; and excluding Services #6 and #19, which route to a static email-instruction screen instead of this wizard). The shell — company information, party/counterparty details, documents, payment, review — is identical for every service; only the service-specific transaction fields change per service.

## Layout

A progress-tracked wizard, not a single scrolling form:

```
Top Bar
↓
Progress Tracker (Service · Company & Party · Details · Documents · Payment · Review)
↓
Current Step
↓
Step Navigation (Back / Continue)
```

## Sections

### Section 1 — Service Confirmation

Pre-filled if arriving from [Service Details](service-details.md); otherwise a service picker identical to [Services Catalog](services-catalog.md)'s list. Confirms the service before the rest of the form renders, since every subsequent step depends on which service is selected — including which field-layout pattern the Details step uses.

### Section 2 — Company & Party Information

Fixed shell fields, same for every service:

* Company name, acting officer identifier (auto-filled from the signed-in user, editable where filed on behalf of a different named officer)
* Represented party (property, agent, tenant, or the company itself, depending on the service) — name, identification, contact details

### Section 3 — Service-Specific Details (dynamic)

**Checked service-by-service, not assumed from another module's pattern count (module build playbook, Phase 4).** Three patterns found across the 25 selectable services:

| Services | Pattern | Basis |
| :---- | :---- | :---- |
| #1–#5, #8–#17, #20–#26 (21 services) | **A — Flat fields** | One value per named field, single entity, no repeatable-count control. |
| **#7 (Accredit Escrow Signatories)** | **B — Repeatable groups** | "Signatory Information (per proposed signatory)" — an add/remove list, not a fixed field set. |
| **#17 (Amend Professional Practice Card)** | **C — Field-selection, conditional pairs** | "Field(s) to be Updated" is attribute selection, not entity repetition — the same shape Financial & Trust Institutions' Service #15 uses. Checking a field reveals a Current Value / Requested New Value pair for that field only. |

**Result: 21 Pattern A, 1 Pattern B, 1 Pattern C, 2 excluded (email-only, #6/#19), 1 excluded pending provenance (#18).**

**No service in this module needed a Pattern C treatment for anything other than #17** — unlike Financial & Trust Institutions, which found a second Pattern C candidate (#15, its own auction/title cluster). This module's flat-field dominance (21 of 25, 84%) is notably higher than Financial & Trust Institutions' equivalent (14 of 18, 78%) or Individual User's (lower still, given that module's eleven distinct patterns).

### Section 4 — Documents

Required and optional documents for the selected service, per its own Section 7. Supports fresh upload; attach-by-reference from a company document repository is **proposed**, not yet confirmed necessary given this module's generally simpler document lists compared to Financial & Trust Institutions'.

### Section 5 — Payment

Shown or skipped depending on the service's payment model:

* **19 no-fee services (#1–#11, #16, #17, #20–#23)** — this step is skipped entirely.
* **Services #12–#15** — this step is skipped **during** submission; payment happens after RERA's decision, as a separate action taken once notice of acceptance arrives (see each service's own Section 12). **This is a genuinely different wizard shape from every other payment-bearing service in the project** — the wizard here ends at Review & Submit without collecting payment, and a second, later screen (not yet designed — see Notes) handles the post-acceptance payment step.
* **Service #24** — payment step appears here, as the last step before Review & Submit, matching the sourced pay-then-output sequence.
* **Services #25/#26** — payment step appears here for the online channel; the Service Center channel is out of this wizard's scope entirely (a different, assisted or counter-based flow — flagged, not designed, given `navigation.md`'s finding that Group D likely has no Trustee Centre channel sourced at all; the Service Center path these two rows describe needs its own resolution before a screen is built for it).

### Section 6 — Review & Submit

Read-only summary of every prior step. See [Application Review](application-review.md).

## Empty State

Not applicable — this screen is always mid-workflow once reached.

## Reused Components

Progress Tracker, Document Uploader, Information Cards, Buttons, **Repeatable Field Group** (Pattern B — #7), **Conditional Field Selector** (Pattern C — #17). Both defined in `ui/components.md` (Phase 5), reused from the equivalent Financial & Trust Institutions components rather than redefined, since the underlying interaction pattern is identical.

## Validation

1. Where the selected service requires payment **during** submission (#24, #25/#26 online), the application cannot reach Review & Submit without a successful payment.
2. Where the selected service requires payment **after** decision (#12–#15), Review & Submit proceeds without a payment step, and the application's post-acceptance state must clearly show payment as the next action — see Application Details.
3. Required documents (per the selected service's own Section 7) must all be attached before Review & Submit is reachable.
4. Section 3's field set — and its pattern (A, B, or C) — is entirely determined by the service selected in Section 1.
5. For Pattern B (#7), the repeatable group must contain at least one signatory before Review & Submit is reachable.
6. For Pattern C (#17), at least one field must be selected before Review & Submit is reachable.

## Access

Identical for all four roles, for every one of the 25 selectable services.

## User Flow

```
Services Catalog / Service Details / Dashboard
↓
Submit Application
├─ Service Confirmation → Company & Party → Service-Specific Details (Pattern A, B, or C) →
│    Documents → [Payment, where applicable during submission] → Review
└─ Review → Submit → Application Review confirmation → Applications
```

## Notes

* **Services #12–#15's post-acceptance payment step needs its own screen, not yet designed.** Unlike every payment-bearing service in Financial & Trust Institutions or Real Estate Developer, this cluster's payment happens after a notice of acceptance the user receives outside this wizard, then returns to pay separately. This is closer in shape to Financial & Trust Institutions' pre-normalization Services #12/#18 (before their 2026-08-16 normalization to pay-before-decision) than to anything currently built anywhere in the project. **Flagged directly for `open-questions.md` B4** — if the client normalizes these four services to pay-before-lodging, this entire Notes item and the wizard's Section 5 branching for #12–#15 become moot, and the wizard simplifies to match the #24 pattern instead.
* **Services #25/#26's Service Center channel is out of scope for this wizard** and needs its own design once `navigation.md`'s open question about whether Group D has any assisted-mode channel at all is resolved.
* **Service #18 is excluded from this wizard entirely**, pending its Group D vs. Group G provenance resolution.
