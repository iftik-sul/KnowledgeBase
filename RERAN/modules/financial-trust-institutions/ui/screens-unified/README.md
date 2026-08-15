---
project: RERAN
module: financial-trust-institutions
type: navigation
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/services-overview.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - unified-portal
---

# The 5 Unified Portal Screens

Five screens covering the "customer applies for and reviews one service" journey, named in issue #50: [Dashboard](dashboard.md), [Services Catalog](services-catalog.md), [Service Details](service-details.md), [Submit Application](submit-application.md), [Application Review](application-review.md).

## Why this folder exists, separate from `ui/screens/`

These 5 screens were originally drafted as Figma AI prompt text earlier in this project's working history, discussed but never committed to the repository. Issue #50's Phase-1 catalogue pass (see that issue's first comment) found nothing but the five bare names anywhere in the repo, and could only produce a low-confidence, name-based mapping against the existing 13 `ui/screens/*.md` files as a result.

This folder is that content, written for the first time as real files rather than chat text — regenerated 2026-08-15, against the *current* corrected model (unified access, two payment models, no role-specific service ownership), not reconstructed from memory of the original draft. It is kept separate from `ui/screens/` so the two sets can be compared side by side rather than one silently overwriting pieces of the other before a retire-vs-rewrite decision is made.

## The mapping, redone against real content

Issue #50's original catalogue compared 13 screens against 5 *names*. With real content now written, the mapping is clearer on some rows and unchanged on others:

| Existing screen (`ui/screens/`) | Unified screen | Verdict |
| :---- | :---- | :---- |
| `dashboard.md` | [dashboard.md](dashboard.md) | **Real overlap, still needs work to reconcile.** The existing screen is built as four structurally different role dashboards; the unified version is one screen by design. Retiring the existing one in favour of this one is now a much more concrete option than it was against a bare name — the sections genuinely map (KPI cards, quick actions, work-requiring-attention list) — but the existing screen's institution-wide activity and expiry tracking need to be checked against this version's Sections 3–4 before anything is deleted. |
| `service-request.md` | [submit-application.md](submit-application.md) | **Confirmed close match**, now with real content to compare rather than just matching names. Both are "one configurable form behind eighteen services." The genuinely open question — whether the per-service field matrix survives as a single wizard step or needs per-service step layouts — is now visible in both documents rather than assumed. |
| `applications.md` | none | **No mapping, now confirmed rather than merely likely.** [Application Review](application-review.md), regenerated, turns out to be a pre-submission wizard step, not a searchable post-submission list. `applications.md` has no counterpart in this set. |
| `application-details.md` | none | **No mapping, confirmed.** Same reasoning — [Application Review](application-review.md) has no role once a record is actually submitted; a submitted record's status, certification, and audit trail stay with `application-details.md`. |
| `escrow-request-queue.md`, `escrow-request-details.md`, `internal-certification-queue.md`, `trust-accounts.md`, `compliance-reports.md`, `payment-history.md`, `institution-profile.md`, `documents.md`, `notifications.md` | none | **No mapping**, as issue #50's original pass already found by name. Nothing in this regenerated set changes that — these 9 screens cover escrow work, compliance work, institution administration and payment reporting, none of which this 5-screen set was ever scoped to cover (see each unified screen's own Notes section). |

**The structural finding from issue #50's original catalogue stands, now on firmer footing:** these 5 screens are not a full replacement for the 13. They cover one journey — browse, apply, review, submit — cleanly. Everything else the module does (escrow, compliance, certification, payment reporting, staff/institution administration) has no counterpart here and was never going to, by design.

## What's still not decided

1. **`dashboard.md`** — retire the 13-screen version in favour of this one, rework this one to absorb what the 13-screen version covers that this one doesn't (institution-wide activity, in more depth), or keep both for different contexts? Not decided here.
2. **`service-request.md`** — does the unified wizard genuinely replace the single-form version, or does the existing screen's approach to the per-service field matrix turn out to matter in a way the wizard doesn't handle? Not decided here.
3. Everything else in the 13-screen set stays, regardless of how 1 and 2 resolve — that much is no longer in question.
