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
  - "RERAN/modules/real-estate-developer/service-flows/service-10-withdraw-project-profit.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-13-register-real-estate-project.md"
tags:
  - real-estate-developer
  - shared-feature
  - application-management
---

# Shared Platform Features

> **Rebuilt 2026-08-16, bottom-up, from the module's actual 19 built screens** (`ui/screens/`), mirroring the same method applied to financial-trust-institutions the same day. The first version of this document (2026-08-15) proposed a generic four-feature Submit/Track/Respond/Resubmit split, copied from individual-user's framing without checking it against this module's own screens. That framing doesn't hold: **unlike individual-user and financial-trust-institutions, this module has no single canonical submission form.** Its derivation chain ran backwards — the 19 UI screens existed before any service flow was written (see [README.md](README.md)) — and what was actually built is five separate **domain workspaces**, each serving a cluster of the 27 numbered services, plus one cross-cutting **Applications** tracker and a set of general platform screens. Still `contains_proposals: true` throughout: none of this is sourced from `RERAN_service_flows_v2.md` as a named concept, only checked against what's built. Needs client confirmation.

**All 6 Application Lifecycle features are now written (2026-08-16).**

## Application Lifecycle (6, all written)

* [Feature #1 — Applications](service-flows/feature-01-applications.md) — the cross-cutting post-submission workspace: tracking, responding to RERA information requests, resubmitting after a return, downloading outputs. `applications.md` + `application-details.md` are the only screens covering anything post-submission — there was never a dedicated screen for tracking, responding, or resubmitting as separate things.
* [Feature #2 — Projects](service-flows/feature-02-projects.md) — Services #13–19 (project registration, cancellation, subdivision, rename, re-registration, settlements, termination). Confirmed via service-13's `derived_from`.
* [Feature #3 — Property Registrations](service-flows/feature-03-property-registrations.md) — Services #1–7 (initial sale, rent-to-own, usufruct, amendments, mortgage-linked sale, fee transfers). Confirmed via **two** services' `derived_from` (service-01 and service-06), not just one — the module's highest-volume domain workspace.
* [Feature #4 — Escrow Management](service-flows/feature-04-escrow-management.md) — Services #8–9, #20–21 (escrow activation, transfer, mortgage deposit, bank guarantee cancellation). Confirmed via service-08's `derived_from`; the module's own README flags cardinality mismatches for #9, #20, #21 against this screen — the mapping is directionally right but not field-exact, flagged rather than resolved.
* [Feature #5 — Fund Release Request](service-flows/feature-05-fund-release-request.md) — Services #10, #12 (project profit withdrawal, receive escrow payment). Confirmed via service-10's `derived_from`. **Carries a genuinely unresolved UI mismatch, flagged at source and not resolved here**: the screen is shaped as a milestone/construction-draw request, and Service #10 (a margin distribution, not a milestone draw) is documented against it as the closest match, not a confirmed fit.
* [Feature #6 — Sales & Disclosures](service-flows/feature-06-sales-and-disclosures.md) — **resolved 2026-08-16, not a domain workspace tied to a numbered service.** The prior version of this document flagged this screen's service mapping as genuinely unresolved. Checked directly this session: Services #1 and #6 both cite Property Registrations in their own `derived_from`, not this screen — so this is a **compliance-tracking layer** (sale record + separate disclosure obligation, two lifecycles) running parallel to Property Registrations, the same shape as financial-trust-institutions' Compliance Reports feature. **Whether every Property Registrations sale requires a Sales & Disclosures filing is itself unresolved** — flagged as an open question in the document itself, not assumed.

## General Platform Features (named, not yet written)

Screens exist for all of the following; none has a standalone shared-feature document yet:

* **Dashboard** (`dashboard.md`) — unified, no per-role variant (2026-08-15 correction, see [navigation.md](navigation.md#dashboard))
* **Documents** (`documents.md` / `document-details.md`)
* **Company Profile** (`company-profile.md`)
* **Reports** (`reports.md`)
* **Notifications** (`notifications.md`)
* **Help & Support** (`help-and-support.md`)

## Platform Features Summary

| Category | Count | Status |
| :---- | :---: | :---- |
| Application Lifecycle (Applications + 5 domain workspaces) | 6 | Written |
| General Platform | 6 | Named, not yet written |
| **Total** | **12** | 6 of 12 written |

## Superseded

The original 2026-08-15 version of this document proposed four features (Submit Application, Track Application Status, Respond to Information Request, Resubmit Returned Application) modeled directly on individual-user's shared-platform-features.md, without checking this module's own screens first. That framing is retired, not extended — see the rebuild note at the top of this document. The lifecycle diagram it included (Choose Service → Complete Form → Submit → Track → Respond/Resubmit → Approved/Rejected) is still directionally accurate for any one domain workspace's own flow, but the "Submit Application" step was never a real, separate screen — it happens inside whichever domain workspace the service belongs to.

## Open Questions

1. Do the six General Platform features named above (not yet written) correctly represent the module's shared layer? Needs client confirmation before writing them.
2. **Sales & Disclosures' relationship to Property Registrations** (Feature #6's own Open Question #1): is a disclosure required for every sale, or only some? No source document establishes this.
3. **Fund Release Request's UI-mismatch question** (Feature #5's own Open Question #1): is Service #10 genuinely the right fit for a milestone/construction-draw-shaped screen?
4. Should individual service-flow files (Services #1–27) be updated to cross-reference whichever domain-workspace or Applications feature they belong to?
