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

> **Corrected 2026-08-16, by client decision (`open-questions.md` B4).** The Payments section below is simplified — Services #12–15 no longer need a carve-out exception in the submission-blocking rule, since they now pay during submission like every other fee-bearing service.

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

**Corrected 2026-08-16 — back to a simpler shape now that Services #12–15 are normalized.** Three distinct timing models, not four:

* **No fee at all** — 19 services (#1–11, #16, #17, #20–23). No payment step ever renders.
* **Pay during submission, before the application is lodged** — Services #12–15 (upfront gateway) and #24 (pay-then-output), and Services #25/#26 online channel. Submission is blocked until payment succeeds.
* **Channel-dependent, possibly two-stage** — Services #25/#26 (Service Center channel: pay after audit; online: covered above; #26 additionally may require a second e-application fee 15 days after notice).

1. **Submission is blocked until payment succeeds, for every fee-bearing service this module's wizard handles.** With B4's normalization, this rule is now uniform — the previous version had to explicitly carve out Services #12–15 as an exception (payment happens *after* submission, not before), since their post-decision timing made a blanket submission-blocking rule actively wrong for them. That exception is retired; the rule now applies without qualification.
2. Service #26's possible second payment (the 15-day follow-up e-application fee) is not itself blocking — whether the follow-up is "necessary" is a RERA determination communicated to the company, not something this module's validation layer can pre-determine.
3. A failed payment is retryable and does not itself constitute an application-lifecycle event.

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
