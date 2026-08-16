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
  - validation
---

# Validation Rules

Validation patterns shared by two or more screens in this module. Validation genuinely specific to a single screen stays documented in that screen's own file and is linked from here.

## Access

Every action is available to any of the company's four Group D roles — there is no permission gating any screen, action, or record. Role is recorded as audit-trail attribution only. Built this way from the start (`navigation.md`), not corrected into it after an earlier role-scoped design.

**Rules**

1. No action is hidden or disabled based on role. What varies between records is status and ownership (e.g. only the current holder of a Draft record may edit it), never who the signed-in user is.
2. There is no maker≠checker restriction to enforce, since no internal certification gate exists anywhere in this module (`open-questions.md` A5). This rule is recorded for consistency with every other module's equivalent document, in case a future service introduces one.
3. Every action is written to the audit timeline with the acting user and the role they held at the time (`navigation.md#audit-trail-principle`).

## Company Standing

1. No service request may be submitted while the company's licence is not active. The form is reachable and saveable as draft; submission is blocked with a message pointing to Company Profile.
2. **Proposed** — expiry-warning thresholds (comparable to Financial & Trust Institutions' 60/14-day windows) are not sourced for Group D's Service #12, and whether Service #12 covers renewal at all is itself unresolved (`ui/screens/company-profile.md`'s own Notes). This rule is a placeholder pending that resolution, not a confirmed mechanic.

## Payments

**Four distinct timing models, not one** — checked service-by-service in `payments.md`, not assumed uniform:

* **No fee at all** — 19 services (#1–11, #16, #17, #20–23). No payment step ever renders.
* **Pay before submission completes** — Service #24, and Services #25/#26 (online channel). Submission is blocked until payment succeeds.
* **Pay after decision** — Services #12–15. Submission completes *without* collecting payment; a separate Complete Payment action becomes available on Application Details once RERA accepts.
* **Channel-dependent, possibly two-stage** — Services #25/#26 (Service Center channel: pay after audit; online: pay near-upfront; #26 additionally may require a second e-application fee 15 days after notice).

1. **Submission is blocked until payment succeeds, only for the services where payment happens *during* submission** (#24, #25/#26 online). Do not build a single "block submission on unpaid" rule against every fee-bearing service — applied to #12–15, it would make those four services impossible to ever submit, since their payment step doesn't exist yet at submission time.
2. **For Services #12–15, submission completing without payment is the correct, sourced behavior, not a bug.** The Complete Payment action appears later, on Application Details, gated on the application having reached an Approved/accepted state first.
3. Service #26's possible second payment (the 15-day follow-up e-application fee) is not itself blocking — whether the follow-up is "necessary" is a RERA determination communicated to the company, not something this module's validation layer can pre-determine.
4. A failed payment, wherever it occurs in a given service's sequence, is retryable and does not itself constitute an application-lifecycle event.

## Documents

1. Required documents are defined per service and must all be present before submission — where the service's own Section 7 specifies them. **Most Group D service-flow files mark their Required Documents section as Proposed rather than sourced** — a materially higher proportion than Financial & Trust Institutions or Real Estate Developer. Treat an unconfirmed document list as a placeholder to validate against provisionally, not as settled requirements.
2. Accepted formats and size limits are platform-level settings, displayed in the uploader rather than hard-coded per screen.

## Service-Specific Field Patterns

1. **Pattern B (Service #7 only):** the repeatable signatory group must contain at least one entry before the application can proceed.
2. **Pattern C (Service #17 only):** at least one field must be selected in the Conditional Field Selector before the application can proceed — an empty "nothing is changing" submission is not valid.

## Concurrency

Two users at the same company may not hold the same record in an editing state simultaneously. The second user sees a read-only view and who holds it.

## Audit

Every create, edit, submit, respond, approve, reject, and document action is written to the audit timeline, capturing the acting user and the role they held at the time. Nothing is editable after submission except through a documented return.
