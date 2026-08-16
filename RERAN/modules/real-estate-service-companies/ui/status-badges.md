---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
  - "RERAN/modules/real-estate-service-companies/payments.md"
  - "RERAN/modules/real-estate-service-companies/ui/screens/"
tags:
  - real-estate-service-companies
  - ui-spec
  - status
---

# Status Badges

Every vocabulary here is checked against the individual service-flow files' own Section 13 (Application Status Flow), not against a UI screen's filter dropdown values. **This distinction matters specifically because Financial & Trust Institutions built this exact mistake into its own `status-badges.md` on 2026-08-15 and needed a same-day multi-file correction to fix it** — see that module's own file for the full history. Building this module's vocabulary the correct way from the start, rather than risking the same error and correcting it later.

> **Corrected 2026-08-16, by client decision (`open-questions.md` B4).** The `Payment Pending` application status, added specifically for Services #12–15's post-decision payment timing, is removed. Those four services now pay upfront, before lodging, the same as most fee-bearing services in the project.

## Application Status

Used on: Submit Application, Application Review, Applications, Application Details, Dashboard.

Per `open-questions.md` C1, Group D adopts the platform-core lifecycle (D1, established in Financial & Trust Institutions' `open-questions.md`) **unextended, without exception** — no `Pending Internal Certification` / `Returned by Certifier` states (no internal certification gate exists anywhere in Group D, A5), and, as of 2026-08-16, no `Payment Pending` addition either.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Draft | Neutral | Started, not submitted |
| Submitted | Info | Lodged, awaiting RERA pickup |
| Under Review | Info | With RERA |
| Information Requested | Warning | RERA has raised a query |
| Returned for Correction | Warning | Sent back to the company |
| Approved | Success | RERA has approved |
| Rejected | Error | Refused, with documented reason |
| Completed | Success | Settled and output document issued |
| Withdrawn | Neutral | Abandoned by the company |

**`Payment Pending` no longer appears in this table — see the corrected banner note above.** This module briefly carried the status during Phase 4, scoped specifically to Services #12–15's then-sourced post-decision payment timing. That timing was normalized on 2026-08-16 (`open-questions.md` B4), the same day Financial & Trust Institutions' own comparable `Approved — Awaiting Payment` status was retired for the same underlying reason (its own #12/#18 normalization) — two unrelated modules reaching the same status-removal outcome via the same mechanism, on the same day, coincidentally.

**This module now has the simplest Application Status vocabulary of any documented so far** — the platform core, entirely unextended. No other module has achieved this: Financial & Trust Institutions needed its own Group C extension for internal certification; Individual User's vocabulary varies by service pattern.

## Jointly Owned Property Supervision Status

Used on: Jointly Owned Property.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Active | Success | Service #1 registration approved and current |
| Pending | Warning | Service #1 submitted, awaiting RERA decision |
| Not Registered | Neutral | No Service #1 registration exists for this property |

## Owners' Association Status

Used on: Jointly Owned Property.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Registered | Success | Service #4 approved |
| Pending | Warning | Service #4 submitted, awaiting RERA decision |
| Not Registered | Neutral | No Service #4 registration exists for this property |

## Practice Card Status

Used on: Company Profile.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Active | Success | Card issued (Service #14) and current |
| Expiring | Warning | Approaching renewal window — threshold not sourced, see `service-flows/service-15-renew-professional-practice-card.md`'s own Open Questions |
| Cancelled | Neutral | Revoked via Service #16 |

## Company Licence Status

Used on: Dashboard (Company Context Header), Company Profile.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Active | Success | Service #12 approved and current |
| Renewal Due | Warning | **Proposed** — whether Service #12 even covers renewal is itself unresolved; see `ui/screens/company-profile.md`'s own Notes |
| Not Registered | Error | No approved licence — blocks submission per `navigation.md` Access Rule 3 |

## Payment State

Used on: Applications (filter and column, not a record-level status badge in the same sense as the above).

| Value | Meaning |
| :---- | :---- |
| No Fee | 19 services — nothing to pay, ever |
| Pending | Payment required as part of submission (#12–15, #24, #25/#26 online) |
| Paid | Payment settled |

**Corrected 2026-08-16 — `Awaiting Payment` (post-decision) removed.** With Services #12–15 normalized to pay before lodging, every fee-bearing service in this module now shows either `Pending` (during submission) or `Paid` (settled) — no service ever sits in an approved-but-unpaid intermediate state.

This is a coarser, filter-level vocabulary layered over Application Status above, not a separate badge shown on every record — most Group D applications (the 19 no-fee services) never show a Payment State value at all beyond "No Fee."

## Note On Reuse

Each vocabulary above is defined once, in this one file, and every screen that displays it links here rather than maintaining its own copy — the discipline that actually prevents drift, not a role-based subsetting rule, since this module has none of the role-scoped variants the platform-wide lesson originally targeted.
