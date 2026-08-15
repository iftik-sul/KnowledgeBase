---
project: RERAN
module: individual-user
type: navigation
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/roles-and-responsibilities.md"
  - "RERAN/modules/individual-user/services-overview.md"
  - "RERAN/modules/individual-user/navigation.md"
  - "RERAN/modules/individual-user/payments.md"
  - "RERAN/modules/individual-user/open-questions.md"
  - "RERAN/modules/individual-user/role-workflows.md"
tags:
  - individual-user
  - ui-spec
  - index
---

# Individual User — UI Specifications

**First pass.** This module had no `ui/` folder at all before this package — the "mirror-image gap" `module-roadmap.md` names relative to Real Estate Developer, which had UI before service flows. Individual User now has the reverse derivation Group C used: source → service flows → analysis layer (`payments.md`, `open-questions.md`, `navigation.md`, `role-workflows.md`) → UI, in that order. This package is built directly against the corrected 43 service-flow files and the analysis layer, not against the pre-correction versions.

## Why This Package Looks Different From Group C's

Group C (18 services) found it needed three field-layout patterns and built one configurable wizard, `screens-unified/submit-application.md`, to cover all eighteen. Individual User has more than double the services (43) and — because it spans eight very different service categories rather than one institution's transaction lifecycle — meaningfully more field-shape variety. Checking every one of the 43 services' own Required Information sections before assuming a Group-C-style single wizard would work found **eleven distinct field-layout patterns**, not three. The Service × Form Matrix below records that check. A single configurable wizard is still the right architecture — the alternative is 43 near-duplicate screen specs — but it needs eleven pattern definitions, not three, and two services (#30, #37) that don't fit the wizard model at all because they route into *other* services rather than collecting their own fields.

## Service × Form Matrix

Every one of the 43 services' Required Information sections was checked individually against the others before any service was assigned a pattern, per the standing instruction not to assume a pattern found in one service applies to its neighbours without checking.

**Corrected 2026-08-15 — #43 was missing from this table entirely, found in a later audit pass.** Counting every pattern's service list against the module's own 43-service total left exactly two unaccounted for: #40 (explained separately below, correctly) and #43 (simply never classified anywhere — an omission, not a documented exclusion). #43's own service-flow file already flags a genuine ambiguity the source doesn't resolve: whether an exchange needs both property owners to separately confirm (like #6's purchaser confirmation) or whether one applicant can register on behalf of both. Classified below as Pattern B by default, matching its Title & Land Registration siblings and the fact that the source describes it "from a single applicant's perspective," but flagged rather than silently resolved — if the client confirms both owners must independently confirm, this moves to Pattern C instead, and the wizard gains a second user session the way #6 has.

| Pattern | Shape | Services |
| :---- | :---- | :---- |
| **A — Search/Lookup** | Search criteria only; no documents, no confirmation step | #1, #2, #3 |
| **B — Standard single-applicant** | Applicant + Property + transaction-specific flat fields | #4, #17, #18, #20, #22, #41, #43 (provisional — see note above) |
| **C — Two-party with counterparty confirmation** | Primary applicant fills and submits; a named second party receives a notification and must separately confirm before the application proceeds | #5, #6, #8, #9, #10, #11, #14 |
| **D — Amend/release/terminate an existing record** | "Select registered X" step first, then a shorter amendment-specific field set | #7 (two sub-flows), #12, #13, #15, #16, #19 (+ repeatable heir group), #21 (+ repeatable partner group) |
| **E — Tenancy** | Property + Landlord + Tenant + lease terms; dual online/counter channel with different payment timing | #23, #24, #27 |
| **F — Management workspace, not a single submission** | Select a record, then choose an action; the action itself may open a Pattern D-shaped sub-form | #25 |
| **G — Category-conditional** | A category selector changes the required fields and documents; #26 alone spans ten source procedures collapsed into one service | #26 |
| **H — Power of Attorney / scope-based** | Principal + Attorney + Scope; #30 additionally re-opens *any other service's* own form once authorization is validated, rather than collecting its own fields | #29, #30, #42 |
| **I — Certificate / statement / valuation request** | Property search + purpose + optional inspection scheduling | #31, #32, #33, #34, #35, #28 |
| **J — Diaspora / identity** | Personal info + document + biometric capture; #37 is a routing wrapper into whichever other pattern the selected transaction actually is | #36, #37 |
| **K — Complaint** | Category + free-text description + evidence upload; no property required | #38, #39 (read-only variant) |

**#40 (Upload Building Details for Leasing) has no UI at all** — the source specifies it as an off-platform, email-based intake process, not an in-app form (already flagged this way in its own service-flow file). It is documented in this package only as a note on [my-leases.md](screens/my-leases.md), not as a screen.

**#30 and #37 are not independent forms.** #30 (Act on Behalf of Property Owner) validates a Power of Attorney and then hands off into whichever of #4–#35's own forms the representative selects — it reuses those forms' patterns rather than defining a new one. #37 (Remote Property Transactions) does the same after identity verification. Both are documented as routing behaviour inside [submit-application.md](screens-unified/submit-application.md), not as separate wizard patterns. Neither has an independent fee status either — see `payments.md` Category 9.

## Screens

| Screen | Purpose |
| :---- | :---- |
| [dashboard](screens/dashboard.md) | Entry point: properties, leases, applications, and notifications requiring action |
| [Services Catalog](screens-unified/services-catalog.md) | Browse all 43 services by the 8 categories in `services-overview.md` |
| [Service Details](screens-unified/service-details.md) | One service: fee, documents, processing time, before starting |
| [Submit Application](screens-unified/submit-application.md) | The configurable wizard behind all patterns A–K |
| [Application Review](screens-unified/application-review.md) | Final review step inside the wizard, before payment/submission |
| [my-properties](screens/my-properties.md) | Registered properties and the actions available on each |
| [my-leases](screens/my-leases.md) | Registered leases, as landlord or as tenant |
| [applications](screens/applications.md) | Search, filter and track all submitted applications |
| [application-details](screens/application-details.md) | One application: particulars, documents, status, audit trail |
| [my-complaints](screens/my-complaints.md) | Submitted complaints and their resolution status |
| [power-of-attorney](screens/power-of-attorney.md) | PoAs granted (as owner) and PoAs held (as representative) |
| [documents](screens/documents.md) | Personal document repository |
| [payment-history](screens/payment-history.md) | Per-transaction payment records: receipts, amounts, status |
| [notifications](screens/notifications.md) | Information requests, returned applications, decisions |
| [profile-kyc](screens/profile-kyc.md) | Identity, KYC status, and where Remote Identity Verification (#36) lives |
| [help-and-support](screens/help-and-support.md) | Help content and support contact |

## Access Model

**Activity-scoped, not role-gated** — see `navigation.md` for the full reasoning. Individual User is not a corporate account: one person can be Property Owner/Seller, Landlord, and Property Buyer/Investor at different times using the same login. No screen in this package gates content by which of the six roles the user "is" — every screen is reachable by every authenticated user, and what's *actionable* depends on what's actually in their account (properties owned, leases held, PoAs granted or held), not a declared role. Where a service has a primary-vs-secondary applicant distinction resolved elsewhere (Register/Renew Lease, #23/#24 — see `open-questions.md` B1), both paths are documented, not just the primary one.

## Shared Documentation

* [components.md](components.md) — component library, including the sidebar definition from `navigation.md`
* [validation-rules.md](validation-rules.md) — validation patterns shared across the eleven wizard patterns
* [status-badges.md](status-badges.md) — status vocabularies: application status, complaint/dispute status, PoA status

## Screen File Template

Every screen file uses, in order: **Purpose, Layout, Sections, Empty State, Reused Components, Validation, Access, User Flow, Notes.** Where a screen has no meaningful access variation (the norm in this module, per the Access Model above), the Access section states that plainly rather than carrying an empty Role Variations heading.

## What's Proposed, Not Sourced

None of the 43 service-flow files or the analysis layer describe actual screen designs — `payments.md`, `open-questions.md`, `navigation.md`, and `role-workflows.md` establish the underlying business rules and access model this package is built against, but the screens themselves, the eleven-pattern classification, and the component library are all **design work**, not source-derived facts. Confidence on individual design choices is noted in each screen file where it matters; the pattern classification itself is High confidence, since it was checked service-by-service against actual Required Information sections rather than assumed.

## Open Items

1. **Pattern G's ten sub-types (#26)** need their own field/document matrix before the wizard's dispute branch can be built out fully — this package documents the pattern shape and the branching principle, not all ten sub-type field sets individually. Same category of open item as Group C's `service-request.md`/`submit-application.md` field-matrix gap.
2. **#42's field set is unknown** — its own service-flow file already documents this as the thinnest-specified service in the module, with no confirmed Required Information, output, or status flow. Its screen entry in this package is built on inference from #29's mirror-image shape, flagged as such.
3. **Whether My Properties / My Leases render as first-class sidebar screens or inline selection steps** was left open in `navigation.md`. This package builds them as first-class screens (the richer option), which is reversible if the client prefers inline selection only.
4. **#43's pattern is provisional (Pattern B), pending client confirmation of whether an exchange needs two-sided confirmation** — added 2026-08-15. If confirmed two-sided, it moves to Pattern C and needs the same counterparty-confirmation treatment as #5/#6/#9–#11/#14, including a second user session and the Counterparty Confirmation Card component.
