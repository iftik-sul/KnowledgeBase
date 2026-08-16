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

**Access:** Any of the company's four Group D roles — identical screen for every user, for every one of the 22 services this wizard covers.

## Purpose

One dynamic form for the module's 22 wizard-eligible services (all except Services #6, #11, and #19, which route to a static email-instruction screen instead of this wizard, and Service #18, which has its own atypical screen — see Notes). The shell — company information, party/counterparty details, documents, payment, review — is identical for every service; only the service-specific transaction fields change per service.

> **Corrected 2026-08-16, three times, by client decision and by audit finding.** **B4** — Services #12–#15's payment step is no longer skipped during submission; it now happens here, the same as every other upfront-paying service, since the client normalized these four services to pay before lodging. **A2** — Service #18 stays in Group D but does not use this wizard at all; it has its own atypical screen, not yet designed — see Notes. **Audit correction, 2026-08-16** — this screen previously miscounted wizard-eligible services twice over: it claimed 24, when 26 minus the three services excluded at the time (#6, #18, #19) is 23, not 24; and it never excluded Service #11 at all, since #11's own email-only channel wasn't corrected until a later same-day audit pass. Both errors are fixed here: **26 total − 4 excluded (#6, #11, #18, #19) = 22 wizard-eligible services.**

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

**Checked service-by-service, not assumed from another module's pattern count (module build playbook, Phase 4).** Three patterns found across the 22 wizard-eligible services:

| Services | Pattern | Basis |
| :---- | :---- | :---- |
| #1–#5, #8–#10, #12–#16, #20–#26 (20 services) | **A — Flat fields** | One value per named field, single entity, no repeatable-count control. |
| **#7 (Accredit Escrow Signatories)** | **B — Repeatable groups** | "Signatory Information (per proposed signatory)" — an add/remove list, not a fixed field set. |
| **#17 (Amend Professional Practice Card)** | **C — Field-selection, conditional pairs** | "Field(s) to be Updated" is attribute selection, not entity repetition — the same shape Financial & Trust Institutions' Service #15 uses. Checking a field reveals a Current Value / Requested New Value pair for that field only. |

**Corrected 2026-08-16** — Pattern A's range previously read "#1–#5, #8–#17, #20–#26 (21 services)," which incorrectly included Service #11 as a wizard-eligible flat-field service. #11 is email-only (see the banner note above) and does not use this wizard at all; it's excluded here the same way #6 and #19 always were.

**Result: 20 Pattern A, 1 Pattern B, 1 Pattern C = 22 wizard-eligible, plus 3 excluded (email-only, #6/#11/#19) and 1 excluded with its own atypical screen (#18) = 26 total.**

### Section 4 — Documents

Required and optional documents for the selected service, per its own Section 7. Supports fresh upload; attach-by-reference from a company document repository is **proposed**, not yet confirmed necessary given this module's generally simpler document lists compared to Financial & Trust Institutions'.

### Section 5 — Payment

Shown or skipped depending on the service's payment model:

* **18 no-fee services within this wizard (#1–#10, #16, #17, #20–#23)** — this step is skipped entirely. **Corrected 2026-08-16** — previously listed as "#1–#11," which included Service #11; #11 is now excluded from this wizard entirely (email-only channel) and no longer appears in any of this screen's per-service lists.
* **Services #12–#15** — this step now appears here, as part of submission, before the application is lodged. **Corrected 2026-08-16 (B4)** — previously skipped here entirely, with payment collected on a separate, undesigned post-acceptance screen; the client's B4 normalization removes that separate step, and these four services now behave identically to Service #24 in this wizard's shape.
* **Service #24** — payment step appears here, as the last step before Review & Submit, matching the sourced pay-then-output sequence.
* **Services #25/#26** — payment step appears here for the online channel; the Service Center channel is out of this wizard's scope entirely (a different, assisted or counter-based flow — flagged, not designed, given `navigation.md`'s finding that Group D likely has no Trustee Centre channel sourced at all).

**With B4's normalization, every payment-bearing service this wizard handles now pays here, during submission — there is no longer a service where Submit Application completes without collecting payment.**

### Section 6 — Review & Submit

Read-only summary of every prior step. See [Application Review](application-review.md).

## Empty State

Not applicable — this screen is always mid-workflow once reached.

## Reused Components

Progress Tracker, Document Uploader, Information Cards, Buttons, **Repeatable Field Group** (Pattern B — #7), **Conditional Field Selector** (Pattern C — #17).

## Validation

1. Where the selected service requires payment (every fee-bearing service this wizard handles: #12–#15, #24, #25/#26 online), the application cannot reach Review & Submit without a successful payment.
2. Required documents (per the selected service's own Section 7) must all be attached before Review & Submit is reachable.
3. Section 3's field set — and its pattern (A, B, or C) — is entirely determined by the service selected in Section 1.
4. For Pattern B (#7), the repeatable group must contain at least one signatory before Review & Submit is reachable.
5. For Pattern C (#17), at least one field must be selected before Review & Submit is reachable.

## Access

Identical for all four roles, for every one of the 22 services this wizard covers.

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
* **Service #11 joined the email-only exclusion group on 2026-08-16, corrected the same day it was found.** It was originally written as a Pattern A wizard-eligible service, inheriting a portal-based workflow incorrectly cross-referenced from Service #5; the correction to its own service-flow file (matching its actual sourced email-only channel) wasn't propagated to this screen at the time, producing exactly the count errors fixed in this pass.
* **Services #25/#26's Service Center channel is out of scope for this wizard** and needs its own design once `navigation.md`'s open question about whether Group D has any assisted-mode channel at all is resolved.
