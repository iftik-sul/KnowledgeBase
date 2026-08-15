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

Four screens covering the "customer applies for and reviews one service" journey, named in issue #50: [Services Catalog](services-catalog.md), [Service Details](service-details.md), [Submit Application](submit-application.md), [Application Review](application-review.md). Dashboard was the fifth — see [Dashboard, resolved](#dashboard-resolved-2026-08-15) below for why it no longer lives in this folder.

## Why this folder exists, separate from `ui/screens/`

These 5 screens were originally drafted as Figma AI prompt text earlier in this project's working history, discussed but never committed to the repository. Issue #50's Phase-1 catalogue pass (see that issue's first comment) found nothing but the five bare names anywhere in the repo, and could only produce a low-confidence, name-based mapping against the existing 13 `ui/screens/*.md` files as a result.

This folder is that content, written for the first time as real files rather than chat text — regenerated 2026-08-15, against the *current* corrected model (unified access, two payment models, no role-specific service ownership), not reconstructed from memory of the original draft. It is kept separate from `ui/screens/` so the two sets can be compared side by side rather than one silently overwriting pieces of the other before a retire-vs-rewrite decision is made.

## Dashboard, resolved 2026-08-15

**Reworked and retired here, not kept as a separate screen.** The client decision on the retire-vs-rework question (below) was: rework the unified dashboard drafted here to absorb what the four retired role-dashboards covered, then retire the old `ui/screens/dashboard.md` (four structurally different dashboards) in its favour. That merged screen now lives at [`ui/screens/dashboard.md`](../screens/dashboard.md) — a single unified dashboard, no role variants, with the institution-wide Focus Area summaries (applications, escrow & trust accounts, compliance, institution standing) folded in as sections rather than separate screens. There is no longer a `dashboard.md` in this folder; the canonical version is the one in `ui/screens/`.

## The mapping, redone against real content

Issue #50's original catalogue compared 13 screens against 5 *names*. With real content now written, the mapping is clearer on some rows and unchanged on others:

| Existing screen (`ui/screens/`) | Unified screen | Verdict |
| :---- | :---- | :---- |
| `dashboard.md` | *(merged in, see above)* | **Resolved 2026-08-15.** The unified dashboard was reworked to absorb the retired screen's institution-wide summaries, and now lives at `ui/screens/dashboard.md` as the single canonical dashboard. No longer an open question. |
| `service-request.md` | [submit-application.md](submit-application.md) | **Confirmed close match**, now with real content to compare rather than just matching names. Both are "one configurable form behind eighteen services." The genuinely open question — whether the per-service field matrix survives as a single wizard step or needs per-service step layouts — is now visible in both documents rather than assumed. Still not resolved. |
| `applications.md` | none | **No mapping, confirmed.** [Application Review](application-review.md), regenerated, turns out to be a pre-submission wizard step, not a searchable post-submission list. `applications.md` has no counterpart in this set. |
| `application-details.md` | none | **No mapping, confirmed.** Same reasoning — [Application Review](application-review.md) has no role once a record is actually submitted; a submitted record's status, certification, and audit trail stay with `application-details.md`. |
| `escrow-request-queue.md`, `escrow-request-details.md`, `internal-certification-queue.md`, `trust-accounts.md`, `compliance-reports.md`, `payment-history.md`, `institution-profile.md`, `documents.md`, `notifications.md` | none | **No mapping**, as issue #50's original pass already found by name. Nothing in this regenerated set changes that — these 9 screens cover escrow work, compliance work, institution administration and payment reporting, none of which this screen set was ever scoped to cover (see each unified screen's own Notes section). Dashboard now links to a summary of several of these rather than replacing them. |

**The structural finding from issue #50's original catalogue stands, now on firmer footing:** these screens are not a full replacement for the 13. They cover one journey — browse, apply, review, submit — cleanly, plus (via the reworked Dashboard) a summary view over the rest. The underlying escrow, compliance, certification, payment-reporting and institution-administration screens have no counterpart here and were never going to, by design.

## What's still not decided

1. **`service-request.md`** — does the unified wizard genuinely replace the single-form version, or does the existing screen's approach to the per-service field matrix turn out to matter in a way the wizard doesn't handle? Not decided here.
2. Everything else in the 13-screen set stays, regardless of how that resolves — that's no longer in question.
