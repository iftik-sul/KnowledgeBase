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
  - "RERAN/modules/real-estate-developer/service-flows/service-10-withdraw-project-profit.md"
  - "RERAN/modules/real-estate-developer/service-flows/service-13-register-real-estate-project.md"
tags:
  - real-estate-developer
  - shared-feature
  - application-management
---

# Shared Platform Features

> **Rebuilt 2026-08-16, bottom-up, from the module's actual 19 built screens** (`ui/screens/`), mirroring the same method applied to financial-trust-institutions the same day. The first version of this document (2026-08-15) proposed a generic four-feature Submit/Track/Respond/Resubmit split, copied from individual-user's framing without checking it against this module's own screens. That framing doesn't hold: **unlike individual-user and financial-trust-institutions, this module has no single canonical submission form.** Its derivation chain ran backwards — the 19 UI screens existed before any service flow was written (see [README.md](README.md)) — and what was actually built is five separate **domain workspaces**, each serving a cluster of the 27 numbered services, plus one cross-cutting **Applications** tracker and a set of general platform screens. Still `contains_proposals: true` throughout: none of this is sourced from `RERAN_service_flows_v2.md` as a named concept, only checked against what's built. Needs client confirmation.

## Application Lifecycle (1 written, 5 domain workspaces named)

**Feature #1 — Applications**, [written](service-flows/feature-01-applications.md) 2026-08-16, replacing what were three separate docs (Track Application Status / Respond to Information Request / Resubmit Returned Application). `applications.md` + `application-details.md` are the only screens covering anything post-submission — there was never a dedicated screen for any of the three as a separate thing.

The five **domain workspaces** below are where applications actually originate — there is no generic "Submit Application" screen sitting above them. Each is confirmed (or reasonably inferred) to serve a specific cluster of the 27 services, checked against individual service files' own `derived_from` frontmatter rather than assumed:

* **Projects** (`projects.md` / `project-details.md`) — Services #13–19 (project registration, cancellation, subdivision, rename, re-registration, settlements, termination). Confirmed via service-13's `derived_from`.
* **Property Registrations** (`property-registrations.md` / `property-registration-details.md`) — Services #1–7 (initial sale, rent-to-own, usufruct, amendments, mortgage-linked sale, fee transfers). Confirmed via service-01's `derived_from`.
* **Escrow Management** (`escrow-management.md` / `escrow-details.md`) — Services #8–9, #20–21 (escrow activation, transfer, mortgage deposit, bank guarantee cancellation). Confirmed via service-08's `derived_from`; the module's own README flags cardinality mismatches for #9, #20, #21 against this screen — the mapping is directionally right but not field-exact.
* **Fund Release Request** (`fund-release-request.md` / `fund-release-request-details.md`) — Services #10, #12 (project profit withdrawal, receive escrow payment). Confirmed via service-10's `derived_from`. Service-10 itself flags an unresolved **UI mismatch**: the screen is shaped as a milestone/construction-draw request, and profit withdrawal (a margin distribution, not a milestone draw) is documented against it as the closest match, not a confirmed fit.
* **Sales & Disclosures** (`sales-and-disclosures.md` / `sales-and-disclosure-details.md`) — **not yet confirmed against a specific service number.** The screen's own primary actions ("Record Property Sale," "Create Sales Disclosure") suggest overlap with Service #1 (Register Initial Sale), but service-01's own `derived_from` points to Property Registrations, not this screen — so the exact relationship between the two screens for the same likely service is unresolved, not assumed. Worth a direct question to the client rather than a guess.

None of the five domain-workspace features has a standalone 21-section document yet — named and scoped here, same treatment as financial-trust-institutions' Trust Accounts / Compliance Reports / Internal Certification Queue at this stage. Writing them is the natural next step once this structure is confirmed.

## General Platform Features (named, not yet written)

Screens exist for all of the following; none has a standalone shared-feature document yet:

* **Dashboard** (`dashboard.md`) — unified, no per-role variant (2026-08-15 correction, see [navigation.md](navigation.md#dashboard))
* **Documents** (`documents.md` / `document-details.md`)
* **Company Profile** (`company-profile.md`)
* **Reports** (`reports.md`)
* **Notifications** (`notifications.md`)
* **Help & Support** (`help-and-support.md`)

## Platform Features Summary

| Category | Count |
| :---- | :---: |
| Application Lifecycle — Applications (written) | 1 |
| Application Lifecycle — Domain Workspaces (named, not written) | 5 |
| General Platform (named, not written) | 6 |
| **Total** | **12** |

## Superseded

The original 2026-08-15 version of this document proposed four features (Submit Application, Track Application Status, Respond to Information Request, Resubmit Returned Application) modeled directly on individual-user's shared-platform-features.md, without checking this module's own screens first. That framing is retired, not extended — see the rebuild note at the top of this document. The lifecycle diagram it included (Choose Service → Complete Form → Submit → Track → Respond/Resubmit → Approved/Rejected) is still directionally accurate for any one domain workspace's own flow, but the "Submit Application" step was never a real, separate screen — it happens inside whichever domain workspace the service belongs to.

## Open Questions

1. Do the six domain/general-platform features named above (not yet written) correctly represent the module's shared layer, or does grouping by "domain workspace" miss something a service-by-service reading would catch? Needs client confirmation before writing the remaining docs.
2. What does Sales & Disclosures actually serve, precisely? Flagged above — worth resolving before writing its standalone doc, since documenting it against a guessed service number would repeat the mistake this rebuild was meant to fix.
3. Should individual service-flow files (Services #1–27) be updated to cross-reference whichever domain-workspace or Applications feature they belong to?
