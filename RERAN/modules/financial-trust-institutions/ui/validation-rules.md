---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
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

---

## Permission Scope

Every action is gated on the signed-in user's permission scope, not their job title. Scopes are provisioned by the Institution Relationship Manager (registration Flow 5) and are the mechanism behind the internal certification gate — see answer A1.

| Scope | Permits |
| :---- | :---- |
| `file` | Create and submit service requests |
| `certify` | Certify or return records at the internal gate |
| `escrow` | Act on developer escrow requests |
| `audit` | Submit compliance reports and view escrow audit records |
| `settlement` | Fund the settlement account and export statements |
| `admin` | Provision staff, manage scopes, renew institutional approvals |

**Rules**

1. An action a user's scope does not permit is not rendered — not rendered-and-disabled.
2. A user cannot certify a record they filed. Maker and checker must be different users, whatever scopes they hold.
3. Scope changes take effect at next sign-in and are recorded in the audit timeline.

## Institutional Standing

1. No service request may be submitted while the institution's approval is expired. The form is reachable and saveable as draft; submission is blocked with a message pointing to Institution Profile.
2. Inside 60 days of expiry, a renewal prompt appears in the Institution Context Header; inside 14 days it escalates to a blocking-warning treatment. Per answer B8, approvals run to a defined validity term.

## Settlement

Per answer B1, fees are deducted from a standing pre-funded account after approval, not paid at submission.

1. Submission is not blocked by an insufficient balance. Approval is not blocked either. **Settlement** is where insufficiency bites, and the record holds at `Approved — Awaiting Payment`.
2. Where the projected balance after committed fees would fall below zero, the service request form shows a warning at review, before submission.
3. The account may not go negative — no credit is extended (answer B4).
4. An approved record left unsettled for 30 calendar days moves to `Approval Expired` and requires resubmission (answer B3). A warning is issued at 7 days and 24 hours.
5. **The low-balance threshold is a per-institution setting**, edited by `admin` on [institution-profile.md](screens/institution-profile.md#section-3--settlement-preferences-tab), not a platform constant. Every screen that shows a low-balance state — the Settlement Account Balance Card, the Institution Context Header, the Dashboard — reads this one setting rather than each defining its own threshold. Added in this pass because the settlement-account and dashboard screens both referenced "the configured threshold" without either of them defining where it lived.

## Documented Reasoning

Per FR-04, a reason is mandatory on every action that returns, rejects or queries a record — at the internal gate and at RERAN's. Free text, minimum length enforced, recorded in the audit timeline against the actor and the scope used.

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

Per FR-22, every create, edit, submit, certify, return, approve, reject, settle and document action is written to the audit timeline. Nothing in the module is editable after submission except through a documented return.
