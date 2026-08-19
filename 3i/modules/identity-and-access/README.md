---
project: 3i
module: identity-and-access
type: overview
status: current
updated: 2026-08-18
id: 3I-IDA-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Identity and Access

The module that governs who exists, who may log in, and what they may do.

§3 of the baseline is titled **"read this first"** and states that it governs the interpretation of every other section. That section is this module. Nothing elsewhere in the project can be read correctly without it — which is why AUTH, RBAC and FAM are one module rather than three.

**Module status: complete and fully specified.** Overview, data model, all three requirements documents, and the full UI stage are written. No open questions remain against this module.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| AUTH | Registration and authentication | 13, one (FR-AUTH-05) since removed |
| RBAC | Roles and permissions | 5 |
| FAM | Family accounts and learner profiles | 10 |

Twenty-eight baseline requirements, plus ten decisions since that amend, narrow, remove, or add to them ([014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md), [015](/3i/decisions/dec-015-device-allowance-scales-with-seats.md), [016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md), [017](/3i/decisions/dec-017-account-holder-renamed-member.md), [018](/3i/decisions/dec-018-profile-pin-mandatory-guardian-controlled.md), [019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md), [020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md), [021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md), [022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md), [023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md)). Eight of the ten are scope changes requiring sign-off under §21.3 — see the [decision register's scope-changes table](/3i/decisions/README.md#scope-changes-against-srd-v20).

## The Two Entities

The baseline refuses the word "student" as ambiguous. It uses two entities instead, and the distinction is load-bearing everywhere:

| Entity | Owns |
| :---- | :---- |
| **Account** | Credentials, billing, devices, notifications, chat participation |
| **Learner** | Enrolments, progress, attendance, exam attempts, certificates |

**Every account has at least one learner.** An adult studying alone is one account with one learner. A guardian with three children is one account with three learners — the guardian is not a learner unless they study, in which case they are a fourth, flagged as the account holder.

See [3I-DEC-001](/3i/decisions/dec-001-learner-as-unit-of-study.md). The practical consequence: every query in the study path filters on **learner**, never on the authenticated account. Authorisation is a separate question — *may this account act for this learner?*

## Account Types

**Per [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md): there are now only two shapes, not three.** The standalone 13–17 account is gone.

| Type | Age | Logs in | Creates profiles | Chat |
| :---- | :---- | :---- | :---- | :---- |
| Adult account holder | 18+ | Yes | Yes, up to 6 (active + never-activated) | Yes |
| Learner profile | Any under 18 — **no exceptions** | No: profile picker + mandatory PIN, lockout matching FR-AUTH-09 | N/A | Under 13: never. 13–17: guardian toggle |

**Every person under 18 is a profile.** There is no independent login for a minor of any age. The 13–17 chat toggle is unaffected by this change — it was always derived from age, not account type, and still is.

## Roles

Three seeded: **Admin**, **Instructor**, **Member**. "Member" replaces the baseline's "Account holder" — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md). No admin UI for role management at launch; adding a role is a database operation, satisfying FR-RBAC-04's "no code change" requirement without a screen.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-IDA-DM-001 | current |
| [requirements/auth-registration-and-authentication.md](requirements/auth-registration-and-authentication.md) | 3I-IDA-REQ-001 | current |
| [requirements/rbac-roles-and-permissions.md](requirements/rbac-roles-and-permissions.md) | 3I-IDA-REQ-002 | current |
| [requirements/fam-family-accounts-and-profiles.md](requirements/fam-family-accounts-and-profiles.md) | 3I-IDA-REQ-003 | current |
| [ui/README.md](ui/README.md) | 3I-IDA-UI-000 | current — **14** screens (was 15; the standalone-teen registration screen is removed), matrix, components, validation rules |
| [backend-spec.md](backend-spec.md) | 3I-IDA-IMPL-001 | current — Prisma schema and Express endpoints for a developer handoff |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| Every age-dependent rule in the platform | [age-and-safeguarding.md](/3i/age-and-safeguarding.md) |
| What a seat is, and the four-state profile lifecycle | [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md), [3I-DEC-014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md) |
| No standalone accounts under 18 | [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) |

## Ageing Up — Needs Re-Raising, Not Just Deferring

[3I-DEC-008](/3i/decisions/dec-008-ageing-up-at-13.md) — offering a 13-year-old profile its own standalone account — was already deferred pending a change request. **[3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) has since removed the thing DEC-008 proposed to offer.** There is no standalone account for anyone under 18 to age into anymore. DEC-008 as originally written cannot be approved into existence even if the client says yes — it describes a feature that no longer has anywhere to attach.

This needs one of two resolutions, not left as-is:

1. **Re-frame DEC-008 around 18, not 13** — a profile reaching 18 is offered its own standalone account, which is now the only age at which that transition could happen.
2. **Retire DEC-008 outright** if ageing out at 18 is considered obvious enough not to need a dedicated decision.

Tracked in [open-questions.md](/3i/open-questions.md) — not resolved here, since it's a product question, not a documentation one.

## Delivery

Phase 1, Foundation (§21.1) — RBAC, identity, registration, age gate, family accounts, email. Everything else in the project sits downstream of this module.

## Open Against This Module

**One item, newly raised by DEC-023's fallout:** DEC-008 needs re-framing or retirement, per above.

Everything else is resolved: the cap ([OQ-08](/3i/open-questions.md)), devices versus seats ([OQ-03](/3i/open-questions.md)), and PIN lockout ([OQ-10](/3i/open-questions.md), resolved by [3I-DEC-022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md)).

## Change Requests Owed to the Client

Eight decisions in this module change SRD v2.0 rather than interpret it. **[3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) is the largest of the batch** — it reverses FR-AUTH-05 outright rather than amending it, and should be flagged to the client distinctly from the other seven, not folded in silently. Full list in [decisions/README.md](/3i/decisions/README.md#scope-changes-against-srd-v20).
