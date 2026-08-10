---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - status
---

# Status Badges

**Proposed.** Four vocabularies are used in this module. Screens link to the relevant section rather than restating it.

The application vocabulary is the platform core proposed in answer D1 plus the Group C extension. It should be adopted platform-wide — FR-18's live dashboard and FR-19's cross-service reporting cannot be built over per-module vocabularies.

---

## Application Status

Used on: service-request, applications, application-details, internal-certification-queue, dashboard.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Draft | Neutral | Started, not submitted |
| Pending Internal Certification | Warning | At the institution's own gate — Group C extension |
| Returned by Certifier | Warning | Sent back by the internal checker — Group C extension |
| Submitted | Info | Lodged, awaiting RERAN pickup |
| Under Review | Info | With the Compliance & Escrow Auditor |
| Information Requested | Warning | RERAN has raised a query |
| Returned for Correction | Warning | Sent back to the institution |
| Approved — Awaiting Payment | Info | Passed audit; fee not yet settled |
| Approval Expired | Error | Unsettled beyond 30 days (answer B3) |
| Rejected | Error | Refused, with documented reason |
| Completed | Success | Settled and output document issued |
| Withdrawn | Neutral | Abandoned by the institution |

The two Group C extension statuses sit **before** Submitted. Where an institution has not enabled internal certification, neither appears.

## Escrow Request Status

Used on: escrow-request-queue, escrow-request-details, trust-accounts, dashboard.

| Status | Treatment | Meaning |
| :---- | :---- | :---- |
| Received | Info | Routed from the developer module |
| Under Trustee Assessment | Info | Trustee reviewing solvency and milestone evidence |
| Information Requested | Warning | Trustee has queried the developer |
| Certified | Success | Trustee has certified; forwarded to RERAN escrow audit |
| Returned to Developer | Warning | Sent back with documented reason |
| RERAN Approved | Success | Escrow department has approved the release |
| RERAN Rejected | Error | Refused at the regulatory gate |
| Executed | Success | Funds transferred; developer notified |

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

---

## Note On Reuse

Group B's status-badges file records a conflict between two roles' status lists for the same object. Group C should not repeat that: each vocabulary above is defined once and is the same for every role. A role may see a subset, never a variant.
