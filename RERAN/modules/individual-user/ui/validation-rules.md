---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/service-flows/"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - validation
---

# Individual User — Validation Rules

Shared validation patterns, referenced by screens rather than restated.

## Identity Fields

* National Identification Number (NIN) — required on every pattern except A (search) and K (complaint, optional). Format validation only — this project does not specify a NIN checksum or format beyond "the identifier used platform-wide."
* Government-issued Identification (document upload) — required wherever a service's own Required Documents list names it. Not substituted by NIN alone.

## Property Fields

* Property Registration Number — validated against the account's own registered properties (via the Property Selector, `components.md`) for any service requiring the applicant to already own the property (#5, #7, #9–#16, #19, #21, #23, #24, #25, #27, #29, #31–#35). Not validated against ownership for services where the applicant is establishing a *new* record (#4, #17, #18, #20, #22, #41) or acting on someone else's property under authority (#30).
* Plot Number / Land Area — free text / numeric where sourced; no format rule specified in source.

## Two-Party Confirmation (Pattern C)

* The counterparty's identity (NIN or equivalent) must match what the primary applicant entered before the counterparty's confirmation is accepted — prevents a wrong party confirming a transaction meant for someone else.
* OTP verification is explicitly sourced for #6 (row 86) only. Whether the other Pattern C services (#5, #8, #9, #10, #11, #14) should carry the same OTP step is **not settled by source** — #6 is the only one where OTP appears in the master table's own workflow description. Proposed: extend OTP to all of Pattern C for consistency, but flagged as a design choice, not a sourced requirement.

## Payment

* No payment step may be skipped or bypassed for a fee-bearing service — matches the platform-wide submission rule.
* No payment step may be *shown* for a confirmed no-fee service (#17, #18, #33, #40, #42, #7's Owner/Entity-Amendment path) — the inverse error is just as real as skipping a required one.
* Payment timing (before vs. after RERAN's decision) must match `payments.md`'s per-service finding exactly. This is the single most-corrected fact in this module's documentation history — any UI implementation should treat `payments.md` as the single source of truth for this field, not infer it from a neighbouring service.

## Category-Conditional Fields (Pattern G, #26)

* The dispute category selector must be answered before any category-specific field or document requirement is shown — the wizard cannot present a generic "upload evidence" step before knowing which of the ten sub-types applies, since required documents genuinely differ by sub-type per source.
* Once a category is selected, changing it should clear category-specific fields already entered rather than silently carry them into a new category's field set, which could mismatch what that category actually requires.

## Power of Attorney (Pattern H)

* #30 (Act on Behalf of Property Owner) must validate an Active PoA status (see `status-badges.md`) before allowing any downstream service selection — this is already how #30's own service-flow file describes its Application Status Flow (`Authorization Validation` as the first real status), carried into this package as a hard gate rather than a soft warning.
* A PoA scope that does not cover the selected downstream service must block submission, not just warn — matches #30's own Business Rule 4: "Representatives cannot perform services outside the approved scope of authority."

## Documents

* Accepted file formats and maximum size are **Proposed**, not sourced — no service-flow file specifies them. Suggest matching whatever the platform-wide standard from other modules turns out to be (not yet documented in any module as of this writing) rather than setting an Individual-User-specific rule.

## Diaspora / Identity (Pattern J)

* #37 cannot proceed until #36 (Remote Identity Verification) shows a completed/verified status — sourced directly in #37's own Prerequisites section.
* Biometric capture format/requirements are **Proposed**, not sourced.
