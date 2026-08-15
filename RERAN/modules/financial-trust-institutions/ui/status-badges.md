---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - status
---

# Status Badges

**Proposed.** Four vocabularies are used in this module. Screens link to the relevant section rather than restating it.

The application vocabulary is the platform core proposed in answer D1 plus the Group C extension. It should be adopted platform-wide — FR-18's live dashboard and FR-19's cross-service reporting cannot be built over per-module vocabularies.

> **Corrected 2026-08-15 — this file had not been touched by any of the module's other corrections until now.** Three things were wrong: it still listed `Approved — Awaiting Payment` and `Approval Expired` as live Application Status states, when both were removed from the module months — in document time — ago (`open-questions.md` B1, B11: no Group C service is ever approved while payment is still pending, and Service #1's approval no longer lapses unpaid); it referenced `service-request`, a screen deleted in favour of `screens-unified/submit-application.md`; and its closing note described role-based status subsetting, which contradicts the unified-access model. All three fixed below.

---

## Application Status

Used on: [submit-application](../screens-unified/submit-application.md), applications, application-details, internal-certification-queue, dashboard.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Draft | Neutral | Started, not submitted |
| Pending Internal Certification | Warning | At the institution's own gate — Group C extension |
| Returned by Certifier | Warning | Sent back by the internal checker — Group C extension |
| Submitted | Info | Lodged, awaiting RERAN pickup |
| Under Review | Info | With the Compliance & Escrow Auditor |
| Information Requested | Warning | RERAN has raised a query |
| Returned for Correction | Warning | Sent back to the institution |
| Rejected | Error | Refused, with documented reason |
| Completed | Success | Settled and output document issued |
| Withdrawn | Neutral | Abandoned by the institution |

**Removed 2026-08-15 — `Approved — Awaiting Payment` and `Approval Expired`.** Both described a state where an application could be approved while payment remained outstanding. Per `open-questions.md` B1 and B11 (confirmed 2026-08-15), payment now happens before lodging for Services #1 and #3–#11, at the point of service for #12–#18, and not at all for Service #2 — there is no Group C service left where approval can occur ahead of payment. Neither status has a live scenario anywhere in the module; see `services-overview.md`'s own Application Status Vocabulary section for the same removal.

The two Group C extension statuses sit **before** Submitted. Where an institution has not enabled internal certification, neither appears.

## Escrow Request Status

Used on: escrow-request-queue, escrow-request-details, trust-accounts, dashboard.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Received | Info | Routed from the developer module |
| Under Trustee Assessment | Info | Any of the institution's four Group C roles reviewing solvency and milestone evidence — typically the Account Trustee in practice |
| Information Requested | Warning | Has queried the developer |
| Certified | Success | Certified; forwarded to RERAN escrow audit |
| Returned to Developer | Warning | Sent back with documented reason |
| RERAN Approved | Success | Escrow department has approved the release |
| RERAN Rejected | Error | Refused at the regulatory gate |
| Executed | Success | Funds transferred; developer notified |

**Corrected 2026-08-15** — "Under Trustee Assessment" previously implied this stage is exclusively the Account Trustee's. Per the unified-access model, any of the institution's four Group C roles may hold this stage; the Account Trustee is who typically does in practice, not who is permitted to.

## Trust Account Status

Used on: trust-accounts, escrow-request-details.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Pending Activation | Warning | Registered, not yet active |
| Active | Success | Operating normally |
| Statement Overdue | Warning | Periodic audited statement not filed |
| Under Audit | Info | Subject to an open audit engagement |
| Flagged | Error | Irregularity raised for regulatory attention |
| Suspended | Error | Frozen by RERAN |
| Closed | Neutral | No-objection issued and account closed |

## Institutional Approval Status

Used on: institution-profile, dashboard, Institution Context Header.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Approved | Success | Standing current |
| Renewal Due | Warning | Inside 60 days of expiry |
| Renewal Urgent | Error | Inside 14 days of expiry |
| Renewal Submitted | Info | Application lodged, awaiting RERAN |
| Expired | Error | Standing lapsed — submission blocked |
| Suspended | Error | Withdrawn by RERAN |
| Cancelled | Neutral | Voluntarily surrendered (Service #2) |

This vocabulary is unaffected by the B1/B11 payment corrections — it describes the institution's own approval standing (Service #1's renewal cycle), not an individual application's payment state, and none of its statuses were ever tied to the retired post-approval payment step.

---

## Note On Reuse

**Corrected 2026-08-15 — this section previously described role-based status subsetting, which no longer applies.** It read: "each vocabulary above is defined once and is the same for every role. A role may see a subset, never a variant." That second sentence assumed role-scoped visibility, which the unified-access model retires — every institution user sees every status on every record, with no subset at all. What survives from Group B's status-badges lesson is narrower: each vocabulary here is defined once, in one place, and every screen that displays it must link to this file rather than maintaining its own copy — that discipline is what actually prevents the two-roles-two-lists conflict Group B had, not a role-based subsetting rule that no longer exists in this module.
