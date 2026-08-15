---
project: RERAN
module: financial-trust-institutions
type: navigation
status: current
updated: 2026-08-15
derived_from:
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - unified-portal
---

# The Unified Portal Screens

Four screens: [Services Catalog](services-catalog.md), [Service Details](service-details.md), [Submit Application](submit-application.md), [Application Review](application-review.md). Dashboard and Submit Application were originally the fifth and fourth of five — see below for how both were resolved out of "open question" status into the module's actual, current screens.

## Why this folder exists, separate from `ui/screens/`

These screens were originally drafted as Figma AI prompt text earlier in this project's working history, discussed but never committed to the repository. Issue #50's Phase-1 catalogue pass found nothing but bare names anywhere in the repo, and could only produce a low-confidence, name-based mapping against the existing `ui/screens/*.md` files as a result.

This folder is that content, written for the first time as real files rather than chat text — regenerated 2026-08-15, against the *current* corrected model (unified access, two payment models, no role-specific service ownership). Dashboard has since been merged into `ui/screens/dashboard.md`; Submit Application has since been confirmed as the module's one canonical form screen, replacing `ui/screens/service-request.md` outright. Both moves are documented below rather than silently made.

## Dashboard, resolved 2026-08-15

**Reworked and retired here, not kept as a separate screen.** The unified dashboard drafted here was reworked to absorb what the four retired role-dashboards covered, then the old `ui/screens/dashboard.md` (four structurally different dashboards) was retired in its favour. The merged screen now lives at [`ui/screens/dashboard.md`](../screens/dashboard.md) — a single unified dashboard, no role variants, with institution-wide Focus Area summaries (applications, escrow & trust accounts, compliance, institution standing) folded in as sections. There is no `dashboard.md` in this folder any more.

## Submit Application, resolved 2026-08-15

**`ui/screens/service-request.md` is retired. [Submit Application](submit-application.md) is now the module's one canonical application form**, covering all eighteen services.

**Why this direction, not the reverse:** the open question was never really "wizard vs. single-page" as a style preference — it was whether the per-service field matrix survives as one generic layout at all. A full audit of all eighteen services' Section 6 (Required Information) found it doesn't: **14 services need a flat field layout (Pattern A), 3 need a repeatable-group layout (Pattern B — Sale Procedure/Heirs #13, Company Shares Sale #14, Split Ownership #16), and 1 needs a field-selection-then-conditional-pairs layout (Pattern C — Update Title Deed Information #15).** See [submit-application.md](submit-application.md)'s own Section 3 for the full per-service breakdown and the reasoning behind #14 and #18's classification specifically.

That finding applies identically to a single-page form — `service-request.md` needed the same fix and never got it. The choice between the two screens therefore came down to which layout handles the underlying complexity better, not which needed less work:

1. **The payment step has three different behaviours** (pay upfront, pay at counter, no fee at all), depending on service. A discrete step that appears or doesn't is a cleaner mechanism than a section that has to materialize and vanish mid-scroll on a single page.
2. **Pattern B and Pattern C are both easier to build and use as a dedicated step.** A repeatable "add another heir/shareholder" control, or a checklist-then-conditional-value-pairs interaction, gets cluttered embedded in the middle of a long single-page form; a step gives each room to be its own focused interaction.
3. **Per-step validation gives clearer error recovery** on a regulator-facing platform where getting a submission right matters — a user who fails on step 3 of 6 knows exactly where the problem is, which is harder to localize on one long page.

**The counterargument, named rather than dismissed:** an institution officer filing the same service repeatedly (e.g. Mortgage Registration, day after day) may find a multi-click wizard slower than a form they can fill in one scroll. That's a real cost, but it's addressable later with a "duplicate previous application" or saved-template feature — it isn't a reason to pick the weaker design for the other services and the payment/validation concerns above.

`service-request.md` is deleted, not archived — its content offered nothing `submit-application.md` doesn't already restate or improve on (see that document's own derivation from the same `service-flows/` source), so there was nothing worth preserving separately.

## The mapping, final state

| Existing screen | Unified screen | Verdict |
| :---- | :---- | :---- |
| `dashboard.md` | *(merged in)* | **Resolved.** Single canonical dashboard at `ui/screens/dashboard.md`. |
| `service-request.md` | [submit-application.md](submit-application.md) | **Resolved.** `service-request.md` deleted; Submit Application is canonical, with all eighteen services' field patterns fully classified. |
| `applications.md` | none | **No mapping, confirmed.** [Application Review](application-review.md) is a pre-submission wizard step, not a searchable post-submission list. |
| `application-details.md` | none | **No mapping, confirmed.** [Application Review](application-review.md) has no role once a record is submitted. |
| `escrow-request-queue.md`, `escrow-request-details.md`, `internal-certification-queue.md`, `trust-accounts.md`, `compliance-reports.md`, `payment-history.md`, `institution-profile.md`, `documents.md`, `notifications.md` | none | **No mapping.** These 9 cover escrow, compliance, and institution-administration work this screen set was never scoped to cover; Dashboard links to summaries of several rather than replacing them. |

Every screen named in issue #50's original scope is resolved, and every one of the eighteen services' field layout is classified. Nothing remains open on this issue.
