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

**Access:** Any of the company's four Group D roles — identical screen for every user, for every one of the 24 services this wizard covers.

## Purpose

One dynamic form for the module's 24 wizard-eligible services (all except Services #6 and #19, which route to a static email-instruction screen instead of this wizard, and Service #18, which has its own atypical screen — see Notes). The shell — company information, party/counterparty details, documents, payment, review — is identical for every service; only the service-specific transaction fields change per service.

> **Corrected 2026-08-16, twice, by client decision.** **B4** — Services #12–#15's payment step is no longer skipped during submission; it now happens here, the same as every other upfront-paying service, since the client normalized these four services to pay before lodging. **A2** — Service #18 stays in Group D but does not use this wizard at all; it has its own atypical screen, not yet designed — see Notes.

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

Pre-filled if arriving from [Service Details](service-details.md); otherwise a service picker identical to [Services Catalog](services-catalog.md)'s list. Confirms the service before the rest of the form renders.

### Section 2 — Company & Party Information

Fixed shell fields, same for every service:

* Company name, acting officer identifier (auto-filled from the signed-in user, editable where filed on behalf of a different named officer)
* Represented party (property, agent, tenant, or the company itself, depending on the service) — name, identification, contact details

### Section 3 — Service-Specific Details (dynamic)

**Checked service-by-service, not assumed from another module's pattern count (module build playbook, Phase 4).** Three patterns found across the 24 wizard-eligible services:

| Services | Pattern | Basis |
| :---- | :---- | :---- |
| #1–#5, #8–#17, #20–#26 (21 services) | **A — Flat fields** | One value per named field, single entity, no repeatable-count control. |
| **#7 (Accredit Escrow Signatories)** | **B — Repeatable groups** | "Signatory Information (per proposed signatory)" — an add/remove list, not a fixed field set. |
| **#17 (Amend Professional Practice Card)** | **C — Field-selection, conditional pairs** | "Field(s) to be Updated" is attribute selection, not entity repetition — the same shape Financial & Trust Institutions' Service #15 uses. Checking a field reveals a Current Value / Requested New Value pair for that field only. |

**Result: 21 Pattern A, 1 Pattern B, 1 Pattern C, 2 excluded (email-only, #6/#19), 1 excluded with its own atypical screen (#18).**

### Section 4 — Documents

Required and optional documents for the selected service, per its own Section 7. Supports fresh upload; attach-by-reference from a company document repository is **proposed**, not yet confirmed necessary given this module's generally simpler document lists compared to Financial & Trust Institutions'.

### Section 5 — Payment

Shown or skipped depending on the service's payment model:

* **19 no-fee services (#1–#11, #16, #17, #20–#23)** — this step is skipped entirely.
* **Services #12–#15** — this step now appears here, as part of submission, before the application is lodged. **Corrected 2026-08-16** — previously skipped here entirely, with payment collected on a separate, undesigned post-acceptance screen; the client's B4 normalization removes that separate step, and these four services now behave identically to Service #24 in this wizard's shape.
* **Service #24** — payment step appears here, as the last step before Review & Submit, matching the sourced pay-then-output sequence.
* **Services #25/#26** — payment step appears here for the online channel; the Service Center channel is out of this wizard's scope entirely (a different, assisted or counter-based flow — flagged, not designed, given `navigation.md`'s finding that Group D likely has no Trustee Centre channel sourced at all).

**With B4's normalization, every payment-bearing service this wizard handles now pays here, during submission — there is no longer a service where Submit Application completes without collecting payment.** This is a meaningfully simpler wizard than the one designed in Phase 4, before B4 was resolved.

### Section 6 — Review & Submit

Read-only summary of every prior step. See [Application Review](application-review.md).

## Empty State

Not applicable — this screen is always mid-workflow once reached.

## Reused Components

Progress Tracker, Document Uploader, Information Cards, Buttons, **Repeatable Field Group** (Pattern B — #7), **Conditional Field Selector** (Pattern C — #17).

## Validation

1. Where the selected service requires payment (now every fee-bearing service this wizard handles: #12–#15, #24, #25/#26 online), the application cannot reach Review & Submit without a successful payment.
2. Required documents (per the selected service's own Section 7) must all be attached before Review & Submit is reachable.
3. Section 3's field set — and its pattern (A, B, or C) — is entirely determined by the service selected in Section 1.
4. For Pattern B (#7), the repeatable group must contain at least one signatory before Review & Submit is reachable.
5. For Pattern C (#17), at least one field must be selected before Review & Submit is reachable.

## Access

Identical for all four roles, for every one of the 24 services this wizard covers.

## User Flow

```
Services Catalog / Service Details / Dashboard
↓
Submit Application
├─ Service Confirmation → Company & Party → Service-Specific Details (Pattern A, B, or C) →
│    Documents → [Payment, where applicable] → Review
└─ Review → Submit → Application Review confirmation → Applications
```

## Notes

* **Services #12–#15's post-acceptance payment step, and the undesigned separate screen it would have needed, are both retired as of 2026-08-16.** The Phase 4 version of this file flagged that gap directly; B4's normalization resolves it by removing the scenario entirely rather than by designing the missing screen.
* **Service #18 is confirmed to stay in Group D (`open-questions.md` A2) but is excluded from this wizard.** Its own sourced workflow — an evaluation company accepting or rejecting a customer's valuation request, performing the evaluation itself, and issuing a certificate — does not fit the company-files-an-application-RERA-reviews-it shape every other service in this wizard shares. This service needs its own screen, not yet designed, matching an evaluation-request-handling shape rather than the Progress Tracker / Company & Party / Service-Specific Details structure above.
* **Services #25/#26's Service Center channel is out of scope for this wizard** and needs its own design once `navigation.md`'s open question about whether Group D has any assisted-mode channel at all is resolved.
