---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - validation
---

# Validation Rules

**Proposed.** Validation patterns shared across Group C screens. Screens link here rather than restating them.

> **Corrected 2026-08-15, twice.** This document previously described a six-scope permission model, a maker≠checker rule, and a Settlement section describing a standing pre-funded account — all retired. **A second pass, later the same day, found the Payments section's rewrite itself contained a functionally serious error**: Rule 1 said submission is blocked until payment succeeds "for every service that charges a fee," which is backwards for Services #12 and #18 — both source RERA's decision *before* the counter payment, not after. Taken literally, that rule would have made #12 and #18 impossible to ever submit. Fixed below.

---

## Access

Every action is available to any of the institution's four Group C roles — there is no permission scope gating any screen, action, or record. Role is recorded as audit-trail attribution only, not as an access control.

**Rules**

1. No action is hidden or disabled based on role. What varies between records is status and ownership (e.g. only the current holder of a Draft record may edit it), never who the signed-in user is.
2. **A user may certify or return a record they themselves filed.** There is no maker≠checker restriction module-wide. This corrects the previous rule requiring maker and checker to be different users — that requirement was tied to the retired `certify` scope and does not survive its removal.
3. Every action is written to the audit timeline with the acting user and the role they held at the time (`navigation.md#audit-trail-principle`).

## Institutional Standing

1. No service request may be submitted while the institution's approval is expired. The form is reachable and saveable as draft; submission is blocked with a message pointing to Institution Profile.
2. Inside 60 days of expiry, a renewal prompt appears in the Institution Context Header; inside 14 days it escalates to a blocking-warning treatment. Per answer B8 (confirmed 2026-08-15, client decision), approvals run to a renewing, per-approval-term validity; the specific two-year duration remains a proposal.

## Payments

**Corrected 2026-08-15, second pass.** Group C runs three payment *timings*, not two, once every service is checked individually rather than trusted against a module-wide summary:

* **Upfront, before lodging** — Services #1 and #3–#11, via the shared platform gateway.
* **At the point of service, before RERA's decision** — Services #13–#17, at a Trustee Centre or Land Department counter.
* **At the point of service, after RERA's decision** — Services #12 and #18, at the counter, once approved.
* **No fee at all** — Service #2.

There is no standing account anywhere in Group C, but **#12 and #18 do have something to settle after approval** — the counter payment step — even though it isn't a settlement-account balance. "Nothing left to settle after approval," a claim this section previously made module-wide, was true for sixteen of the eighteen services and wrong for two.

1. **Submission is blocked until payment succeeds, for Services #1 and #3–#17 only.** For #12 and #18, the opposite order applies: the application is lodged and audited *first*, and payment is collected only once RERA has approved it, at the counter. Do not build a single "block submission on unpaid" rule against all fee-bearing services — it would make #12 and #18 impossible to submit at all.
2. A failed payment at checkout is retryable and is not an application-lifecycle event, for #1 and #3–#17 — nothing is submitted, certified, or audited until payment succeeds. **This does not apply to #12/#18**, where there is no checkout at lodging to fail; see rule 5 below for their payment-failure scenario instead.
3. Service #2 (Cancellation) presents no payment step at all, confirmed 2026-08-15 (`open-questions.md` B11) — this is not an omission to validate against; the service genuinely has no fee.
4. The low-balance-threshold setting, the negative-balance block, and the 30-calendar-day unsettled-approval expiry (previously tied to `open-questions.md` B3, B4) do not apply to any Group C service — there is no standing balance to fall below zero anywhere in the module. `open-questions.md` B3 itself was not revisited by any payment correction and remains as written there, flagging a tension rather than resolving it — see [payments.md](../payments.md#additional-statuses).
5. **Added 2026-08-15, second pass.** For #12/#18, an approved application that hasn't yet been paid at the counter shows `Approved — Awaiting Payment` (see [status-badges.md](status-badges.md#application-status)). What happens if the customer never returns to pay is not addressed by any source document or client decision — flagged in `payments.md`'s To Confirm — Summary, not resolved here.

## Documented Reasoning

Per FR-04, a reason is mandatory on every action that returns, rejects or queries a record — at the internal gate and at RERAN's. Free text, minimum length enforced, recorded in the audit timeline against the actor and the role they held at the time. **Corrected 2026-08-15** — previously "against the actor and the scope used"; there is no scope to record any more.

A positive decision does not require a reason but permits one.

## Documents

1. Required documents are defined per service and must all be present before submission. Optional documents may be added at any point before the internal gate.
2. A document already held in the institution repository may be attached by reference. The reference records which version was attached, so a later replacement does not silently alter a submitted record.
3. Accepted formats and size limits are platform-level settings, displayed in the uploader rather than hard-coded per screen.

## Property and Party References

1. A title reference must resolve to a registered property before the form will accept it. An unresolved reference is an error, not a warning.
2. Party identification is validated against NIN for individuals and CAC for companies, consistent with the platform's verification layer.
3. Where a service acts on an existing instrument — amendment, transfer, release — the instrument must be active. Acting on a released instrument is blocked.

## Concurrency

Two users in the same institution may not hold the same record in an editing state. The second user sees a read-only view and who holds it.

## Audit

Per FR-22, every create, edit, submit, certify, return, approve, reject and document action is written to the audit timeline, capturing the acting user and the role they held at the time. Nothing in the module is editable after submission except through a documented return. **Corrected 2026-08-15** — "settle" is removed from the list of logged actions; there is no self-service settle action anywhere in the module, though #12/#18's counter payment is still logged as an event when it happens.
