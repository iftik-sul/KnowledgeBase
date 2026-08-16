---
project: RERAN
module: real-estate-developer
type: overview
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/README.md"
  - "RERAN/modules/real-estate-developer/README.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-01-register-initial-sale.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-06-register-mortgage-linked-sale.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-08-activate-escrow-account.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-10-withdraw-project-profit.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-13-register-real-estate-project.md"
tags:
  - real-estate-developer
  - shared-feature
  - application-management
---

# Shared Platform Features

> **Rebuilt 2026-08-16, bottom-up, from the module's actual 19 built screens** (`ui/screens/`), mirroring the same method applied to financial-trust-institutions the same day. The first version of this document (2026-08-15) proposed a generic four-feature Submit/Track/Respond/Resubmit split, copied from individual-user's framing without checking it against this module's own screens. That framing doesn't hold: **unlike individual-user and financial-trust-institutions, this module has no single canonical submission form.** Its derivation chain ran backwards — the 19 UI screens existed before any service flow was written (see [README.md](README.md)) — and what was actually built is five separate **domain workspaces**, each serving a cluster of the 27 numbered services, plus one cross-cutting **Applications** tracker and a set of general platform screens. Still `contains_proposals: true` throughout: none of this is sourced from `RERAN_service_flows_v2.md` as a named concept, only checked against what's built. Needs client confirmation.

**All 12 of 12 features are now written (2026-08-16).**

## Application Lifecycle (6)

* [Feature #1 — Applications](service-flows/feature-01-applications.md) — the cross-cutting post-submission workspace: tracking, responding to RERA information requests, resubmitting after a return, downloading outputs. `applications.md` + `application-details.md` are the only screens covering anything post-submission — there was never a dedicated screen for tracking, responding, or resubmitting as separate things.
* [Feature #2 — Projects](service-flows/feature-02-projects.md) — Services #13–19 (project registration, cancellation, subdivision, rename, re-registration, settlements, termination). Confirmed via service-13's `derived_from`.
* [Feature #3 — Property Registrations](service-flows/feature-03-property-registrations.md) — Services #1–7 (initial sale, rent-to-own, usufruct, amendments, mortgage-linked sale, fee transfers). Confirmed via **two** services' `derived_from` (service-01 and service-06), not just one — the module's highest-volume domain workspace.
* [Feature #4 — Escrow Management](service-flows/feature-04-escrow-management.md) — Services #8–9, #20–21 (escrow activation, transfer, mortgage deposit, bank guarantee cancellation). Confirmed via service-08's `derived_from`; the module's own README flags cardinality mismatches for #9, #20, #21 against this screen — the mapping is directionally right but not field-exact, flagged rather than resolved. **Status vocabulary corrected 2026-08-16** — see Cross-Module Correction below.
* [Feature #5 — Fund Release Request](service-flows/feature-05-fund-release-request.md) — Services #10, #12 (project profit withdrawal, receive escrow payment). Confirmed via service-10's `derived_from`. **Carries a genuinely unresolved UI mismatch, flagged at source and not resolved here**: the screen is shaped as a milestone/construction-draw request, and Service #10 (a margin distribution, not a milestone draw) is documented against it as the closest match, not a confirmed fit. **Status vocabulary corrected 2026-08-16** — see Cross-Module Correction below.
* [Feature #6 — Sales & Disclosures](service-flows/feature-06-sales-and-disclosures.md) — **resolved 2026-08-16, not a domain workspace tied to a numbered service.** Checked directly: Services #1 and #6 both cite Property Registrations in their own `derived_from`, not this screen — so this is a **compliance-tracking layer** (sale record + separate disclosure obligation, two lifecycles) running parallel to Property Registrations, the same shape as financial-trust-institutions' Compliance Reports feature. **Whether every Property Registrations sale requires a Sales & Disclosures filing is itself unresolved** — flagged as an open question in the document itself, not assumed.

## General Platform (6)

All six rebuilt 2026-08-15 from four role-based designs into one screen apiece, then written as standalone feature docs 2026-08-16:

* [Feature #7 — Dashboard](service-flows/feature-07-dashboard.md) — unified landing screen, KPIs a deliberate superset of what four prior role dashboards each defined.
* [Feature #8 — Documents](service-flows/feature-08-documents.md) — organization-wide repository; category taxonomy is the union of four domain-specific lists with zero overlap at the domain end.
* [Feature #9 — Company Profile](service-flows/feature-09-company-profile.md) — the organization's master profile. Unlike every other screen in this module, this one had **only one design in source**, no role variant to merge — and was consequently missed by the earlier access-model correction pass, carrying a leftover permission-scope statement found and removed only during this write-up.
* [Feature #10 — Reports](service-flows/feature-10-reports.md) — the most structurally divergent screen to rebuild: four **entirely separate** report catalogues with almost no overlap, unioned rather than chosen between. No report was removed.
* [Feature #11 — Notifications](service-flows/feature-11-notifications.md) — organization-wide alert feed; notification-type vocabulary is the union of four domain-specific lists, same pattern as Documents.
* [Feature #12 — Help & Support](service-flows/feature-12-help-and-support.md) — four designs with genuinely disagreeing section sets (System Status/Feedback & Suggestions vs. Training Resources/Quick Help Categories); all sections kept, the omissions read as source gaps rather than deliberate restrictions.

## Platform Features Summary

| Category | Count | Status |
| :---- | :---: | :---- |
| Application Lifecycle (Applications + 5 domain workspaces) | 6 | Written |
| General Platform | 6 | Written |
| **Total** | **12** | **12 of 12 written** |

## Cross-Module Correction: Escrow Status Vocabulary

**Corrected 2026-08-16, superseding an earlier same-day resolution that was itself wrong.** The first pass adopted `No Request → Pending Approval → Under Review → Approved → Released` as canonical — this was taken from Escrow Management's own UI screen filter values, never checked against the individual service files it was meant to describe.

**Checked directly against all six escrow service files (#8, #9, #10, #12, #20, #21) — all six independently use the same sourced vocabulary:**

`Draft → Submitted → Trustee Review → RERA Escrow Audit → Approved → [service-specific terminal state]`, plus additional statuses `Information Requested / Returned / Rejected`. The terminal state varies by service: `Active` (#8), `Transferred` (#9), `Released` (#10, #12), `Deposited` (#20), `Cancelled` (#21).

**This is now the corrected canonical vocabulary, applied as follows:**

* **This module's Escrow Management (Feature #4)** — corrected to use the sourced vocabulary; its own UI screen's filter values are retained as filter labels only, no longer treated as the status flow itself.
* **This module's Fund Release Request (Feature #5)** — its 9-stage detailed tracker now maps onto the sourced vocabulary (`Trustee Review`, `RERA Escrow Audit`), not the incorrect one; its "Under Bank Review" label is also corrected — the reviewing party is the Account Trustee, not a bank.
* **Financial & Trust Institutions' Escrow Request Queue** — corrected to the same sourced vocabulary, which fixes that feature's original gap (no status for RERA's post-certification review) more precisely than the first correction did: `RERA Escrow Audit` is now an explicit named stage, not an ambiguous continuation of a shared "Under Review."

See Features #4 and #5's own Feature Overview sections, and financial-trust-institutions' `feature-04-escrow-request-queue.md`, for the full detail.

## Superseded

The original 2026-08-15 version of this document proposed four features (Submit Application, Track Application Status, Respond to Information Request, Resubmit Returned Application) modeled directly on individual-user's shared-platform-features.md, without checking this module's own screens first. That framing is retired, not extended — see the rebuild note at the top of this document. The lifecycle diagram it included (Choose Service → Complete Form → Submit → Track → Respond/Resubmit → Approved/Rejected) is still directionally accurate for any one domain workspace's own flow, but the "Submit Application" step was never a real, separate screen — it happens inside whichever domain workspace the service belongs to.

## Open Questions

1. Does the full 12-feature structure correctly represent the module's shared layer? Needs client confirmation.
2. **Sales & Disclosures' relationship to Property Registrations** (Feature #6's own Open Question #1): is a disclosure required for every sale, or only some? No source document establishes this.
3. **Fund Release Request's UI-mismatch question** (Feature #5's own Open Question #1): is Service #10 genuinely the right fit for a milestone/construction-draw-shaped screen?
4. **Company Profile's missing Validation Summary** (Feature #9's own Open Question #1): every other form screen in the module has one; this one doesn't — confirm whether that's a genuine gap or not applicable to a profile page.
5. Should individual service-flow files (Services #1–27) be updated to cross-reference whichever domain-workspace or Applications feature they belong to?
