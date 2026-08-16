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

## Application Status

Used on: Submit Application, Application Review, Applications, Application Details, Dashboard.

Per `open-questions.md` C1, Group D adopts the platform-core lifecycle (D1, established in Financial & Trust Institutions' `open-questions.md`) **unextended** — no `Pending Internal Certification` / `Returned by Certifier` states, since no Group D service sources an internal certification gate (`open-questions.md` A5).

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Draft | Neutral | Started, not submitted |
| Submitted | Info | Lodged, awaiting RERA pickup |
| Under Review | Info | With RERA |
| Information Requested | Warning | RERA has raised a query |
| Returned for Correction | Warning | Sent back to the company |
| Approved | Success | RERA has approved |
| **Payment Pending** | **Warning** | **Services #12–15 only — approved, payment now required before completion** |
| Rejected | Error | Refused, with documented reason |
| Completed | Success | Settled and output document issued |
| Withdrawn | Neutral | Abandoned by the company |

**Payment Pending is checked directly against Services #12, #13, #14, and #15's own Section 9 and Section 13** — each sources payment happening after acceptance, not before. This is a genuinely different situation from Financial & Trust Institutions' now-retired `Approved — Awaiting Payment` (which was normalized away by client decision on 2026-08-16): Group D's #12–15 have not been normalized, and nothing in this module's build has changed their sourced sequencing. If `open-questions.md` B4 resolves toward normalizing these four services, this status should be revisited and likely removed the same way Financial & Trust Institutions' was.

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
| Pending | Payment required before submission completes (#24, #25/#26 online) |
| Awaiting Payment | Post-decision payment required (#12–15 only) |
| Paid | Payment settled |

This is a coarser, filter-level vocabulary layered over Application Status above, not a separate badge shown on every record — most Group D applications (the 19 no-fee services) never show a Payment State value at all beyond "No Fee."

## Note On Reuse

Each vocabulary above is defined once, in this one file, and every screen that displays it links here rather than maintaining its own copy — the discipline that actually prevents drift, not a role-based subsetting rule, since this module has none of the role-scoped variants the platform-wide lesson originally targeted.
