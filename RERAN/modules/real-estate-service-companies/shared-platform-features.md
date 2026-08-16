---
project: RERAN
module: real-estate-service-companies
type: overview
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/ui/screens/"
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
tags:
  - real-estate-service-companies
  - shared-platform-features
---

# Real Estate Service Companies — Shared Platform Features

**Derived bottom-up from the 12 built UI screens (Phase 4), not proposed by analogy to another module's feature count** — per the module build playbook's Phase 5 instruction, and the specific lesson both Group B's and Group C's shared-features layers had to learn the hard way after their first, analogy-based feature lists turned out wrong once checked against actual screens.

> **Corrected 2026-08-16, twice, by client decision.** **B4** — Feature #2's post-decision payment handling for Services #12–15 is removed; those four services now pay during submission, under Feature #1. **A2** — Service #18 stays in Group D; Feature #1's exclusion note is corrected, though the service still doesn't have a designed screen of its own yet — see Open Questions.

## Application Lifecycle Features (2)

### Feature #1 — Service Requests

**Screens:** Services Catalog, Service Details, Submit Application, Application Review.

Covers browsing 24 of the module's 25 services (all except the two email-only services, #6 and #19, which route to a static instruction screen instead), reviewing a service's requirements, completing the dynamic submission form (three field-layout patterns — see `ui/screens/submit-application.md`), and the final read-only checkpoint before submission.

**Service #18 is confirmed to stay in Group D (`open-questions.md` A2) but is not yet covered by this feature's screens.** Its own sourced workflow — an evaluation company deciding on a customer's valuation request, not a company filing an application RERA reviews — doesn't fit this feature's shared shell. It needs its own screen, not yet designed; see Open Questions.

### Feature #2 — Applications

**Screens:** Applications, Application Details.

Covers everything a submitted application does from `Submitted` onward: tracking and responding to RERA's information requests. **Corrected 2026-08-16** — this feature previously also covered "completing a post-decision payment for Services #12–15," the one respect in which it differed from Financial & Trust Institutions' equivalent feature's scope. With B4's normalization, that payment now happens under Feature #1 during submission, and this feature's scope is simpler than Phase 4 originally built it: tracking and response only, the same shape Financial & Trust Institutions' own Applications feature has for its RERA-side loop.

## Company-Specific Features (1)

### Feature #3 — Jointly Owned Property Register

**Screen:** Jointly Owned Property.

A standing register of properties under the company's JOP administrative supervision, separate from the transactional Applications list — the same reasoning Financial & Trust Institutions used for Trust Accounts, applied here because 11 of the module's 26 services (42%) concern JOP administration and the underlying properties persist as records the company returns to repeatedly.

**Not built as a separate feature, and why:** a Trustee-facing queue (comparable to Financial & Trust Institutions' Escrow Request Queue) was considered and rejected, since `open-questions.md` A3 found JOP's escrow-adjacent services route directly from company to RERA with no Trustee intermediary sourced anywhere.

## General Platform Features (5)

### Feature #4 — Dashboard

**Screen:** Dashboard.

Company-wide KPIs, quick actions, and Focus Area summaries for each of the five service categories, each linking to its own full feature rather than duplicating it.

### Feature #5 — Documents

**Screen:** Documents.

The company's document repository, categorized by what a document attaches to (Company/Licensing, JOP, Rental, Transaction, Dispute, Other). Notably thinner than Financial & Trust Institutions' or Real Estate Developer's equivalent — most Group D service-flow files mark their own Required Documents sections as Proposed rather than sourced, so this feature's category taxonomy is built from what's plausible, not a rich sourced list.

### Feature #6 — Notifications

**Screen:** Notifications.

Five categories. **Corrected 2026-08-16 — the sixth category, Payment Due (Services #12–15 only, an un-mutable Priority Alert), is removed.** It was checked directly against those four services' own sourced payment timing when built, not by analogy to any other module — that check was correct at the time. It's retired now because the underlying fact changed by client decision (`open-questions.md` B4), not because the original build was wrong. This module now has no Priority Alert category at all, unlike Financial & Trust Institutions, which retains its own Approval Expiry Warning.

### Feature #7 — Company Profile

**Screen:** Company Profile.

Company licensing standing, agent roster and practice cards, staff records, and corporate information. Surfaced a genuine open question while being built: whether Service #12 covers renewal at all, given its own source text lacks the explicit "approval **/ renewal**" framing Financial & Trust Institutions' comparable service has.

### Feature #8 — Help & Support

**Screen:** Help & Support.

Not sourced — built at Claude's discretion, matching the precedent already established for Financial & Trust Institutions' equivalent feature (itself adapted from Real Estate Developer's). Scoped for this module's brokerage/JOP/property-management audience.

## Features Considered and Not Built

**Payment History** — Financial & Trust Institutions builds this as its own institution-specific feature, given that module's payment complexity. Group D also has genuine payment complexity, but no dedicated screen was actually built for it in Phase 4 — payment receipts display within Application Details' own Outputs section, and the Applications list already carries a Payment State filter covering the same ground at lower fidelity.

**Corrected 2026-08-16** — this note previously cited "tracking the #12–15 payment-due state across many applications at once" as a specific scenario that might justify building this feature. That scenario no longer exists, since #12–15 now pay during submission and never sit in a payment-due state to track. The remaining case for this feature — Service #26's possible two-stage payment — is narrower on its own than the original note implied, and probably doesn't justify a dedicated feature by itself. Flagged as lower priority than it was before this correction, not resolved either way.

**Internal Certification Queue** — not built. No Group D service sources an internal company-side certification gate (`open-questions.md` A5). If a future service or client decision introduces one, this feature would need adding, following Financial & Trust Institutions' equivalent as the template.

**Escrow Request Queue** — not built. JOP's escrow-adjacent services route directly to RERA with no Trustee intermediary (`open-questions.md` A3). If A3 is revisited and found wrong, this feature would need adding.

**Compliance Reports** — not built. No Group D row sources a reporting obligation comparable to Financial & Trust Institutions' Auditing Bureau Officer function. Group D's own audit-related services (#8–#10) are one-time appointment actions, not a recurring reporting cycle.

**Evaluation Certificate Processing (Service #18)** — not built as its own feature, and deliberately not invented here to fill the gap A2's decision opened. Per the module build playbook's own Phase 5 discipline, features are derived from actual built screens, not proposed ahead of them — inventing a ninth feature for a service with no designed screen yet would repeat exactly the analogy-based-guessing mistake this document's own opening paragraph describes Group B and Group C making. Once Service #18's own screen is designed, revisit whether it needs a dedicated feature or folds into Feature #1.

## Feature Count Summary

| Category | Count |
| :---- | :---: |
| Application Lifecycle | 2 |
| Company-Specific | 1 |
| General Platform | 5 |
| **Total** | **8** |

Unaffected by either 2026-08-16 correction — B4 simplified Feature #2's scope without removing it, and A2 confirmed Service #18's module ownership without yet producing a screen that would change this count.

## Open Questions

1. Same adoption question every other module's shared-features layer carries: does this eight-feature structure hold up once actual screen mockups are built against it, the way Financial & Trust Institutions' and Real Estate Developer's first-pass feature lists didn't? Flagged for the same kind of audit pass those two modules needed.
2. **Service #18's screen is not yet designed**, despite its module ownership being confirmed (`open-questions.md` A2). This is the most concrete remaining gap in this module's Phase 4/5 output — every other confirmed-in-scope service has a screen path; this one doesn't yet.
