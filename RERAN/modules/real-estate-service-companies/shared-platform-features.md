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
tags:
  - real-estate-service-companies
  - shared-platform-features
---

# Real Estate Service Companies — Shared Platform Features

**Derived bottom-up from the 12 built UI screens (Phase 4), not proposed by analogy to another module's feature count** — per the module build playbook's Phase 5 instruction, and the specific lesson both Group B's and Group C's shared-features layers had to learn the hard way after their first, analogy-based feature lists turned out wrong once checked against actual screens.

## Application Lifecycle Features (2)

### Feature #1 — Service Requests

**Screens:** Services Catalog, Service Details, Submit Application, Application Review.

Covers browsing the 25 selectable services (all except Service #18 — see Open Questions), reviewing a service's requirements, completing the dynamic submission form (three field-layout patterns — see `ui/screens/submit-application.md`), and the final read-only checkpoint before submission. Two services (#6, #19) route out of this feature entirely into a static email-instruction screen rather than the wizard.

### Feature #2 — Applications

**Screens:** Applications, Application Details.

Covers everything a submitted application does from `Submitted` onward: tracking, responding to RERA's information requests, and — uniquely in this module — completing a post-decision payment for Services #12–15. No internal certification loop exists to carve out as a separate concern here, unlike Financial & Trust Institutions' equivalent feature, which has to explicitly scope itself to "the RERA-side loop only."

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

Six categories, one of which (**Payment Due**, Services #12–15 only) is an un-mutable Priority Alert — checked directly against those four services' own sourced payment timing, not built by analogy to Financial & Trust Institutions' now-retired equivalent category. See `ui/screens/notifications.md`'s own Notes for why that comparison needed an explicit caution rather than a silent copy.

### Feature #7 — Company Profile

**Screen:** Company Profile.

Company licensing standing, agent roster and practice cards, staff records, and corporate information. Surfaced a genuine open question while being built: whether Service #12 covers renewal at all, given its own source text lacks the explicit "approval **/ renewal**" framing Financial & Trust Institutions' comparable service has.

### Feature #8 — Help & Support

**Screen:** Help & Support.

Not sourced — built at Claude's discretion, matching the precedent already established for Financial & Trust Institutions' equivalent feature (itself adapted from Real Estate Developer's). Scoped for this module's brokerage/JOP/property-management audience.

## Features Considered and Not Built

**Payment History** — Financial & Trust Institutions builds this as its own institution-specific feature, given that module's payment complexity. Group D also has genuine payment complexity (four distinct timing models, including a two-stage possibility on Service #26), but no dedicated screen was actually built for it in Phase 4 — payment receipts display within Application Details' own Outputs section, and the Applications list already carries a Payment State filter covering the same ground at lower fidelity. **Flagged here rather than silently omitted**: if Phase 6 or later use reveals that Applications' filter-level payment visibility isn't sufficient (particularly for tracking the #12–15 payment-due state across many applications at once, or the #26 two-stage payment), this feature should be added and a dedicated screen built for it — not assumed unnecessary just because this pass didn't need it.

**Internal Certification Queue** — not built. No Group D service sources an internal company-side certification gate (`open-questions.md` A5). If a future service or client decision introduces one, this feature would need adding, following Financial & Trust Institutions' equivalent as the template.

**Escrow Request Queue** — not built. JOP's escrow-adjacent services route directly to RERA with no Trustee intermediary (`open-questions.md` A3). If A3 is revisited and found wrong, this feature would need adding.

**Compliance Reports** — not built. No Group D row sources a reporting obligation comparable to Financial & Trust Institutions' Auditing Bureau Officer function. Group D's own audit-related services (#8–#10) are one-time appointment actions, not a recurring reporting cycle.

## Feature Count Summary

| Category | Count |
| :---- | :---: |
| Application Lifecycle | 2 |
| Company-Specific | 1 |
| General Platform | 5 |
| **Total** | **8** |

Fewer than Financial & Trust Institutions' 12 or Real Estate Developer's 13 — not because Group D is a smaller module (26 services is comparable to Financial & Trust Institutions' 18), but because several of those modules' features exist specifically to model mechanisms (internal certification, Trustee-mediated escrow, recurring compliance reporting) that Group D's own source material simply doesn't have.

## Open Questions

1. Same adoption question every other module's shared-features layer carries: does this eight-feature structure hold up once actual screen mockups are built against it, the way Financial & Trust Institutions' and Real Estate Developer's first-pass feature lists didn't? Flagged for the same kind of audit pass those two modules needed.
2. Should Payment History be built as its own feature preemptively, given the module's genuine payment complexity, rather than waiting to find it's needed? See "Features Considered and Not Built" above — deliberately left as a flagged decision, not resolved here.
