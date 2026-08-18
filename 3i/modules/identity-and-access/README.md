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

**Module status: complete.** Overview, data model, all three requirements documents, and the full UI stage are written.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| AUTH | Registration and authentication | 13 |
| RBAC | Roles and permissions | 5 |
| FAM | Family accounts and learner profiles | 10 |

Twenty-eight baseline requirements, plus eight decisions since that amend, narrow, or add to them ([014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md), [015](/3i/decisions/dec-015-device-allowance-scales-with-seats.md), [016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md), [017](/3i/decisions/dec-017-account-holder-renamed-member.md), [018](/3i/decisions/dec-018-profile-pin-mandatory-guardian-controlled.md), [019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md), [020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md), [021](/3i/decisions/dec-021-attendance-measured-against-sessions-delivered.md)). Six of the eight are scope changes requiring sign-off under §21.3 — see the [decision register's scope-changes table](/3i/decisions/README.md#scope-changes-against-srd-v20).

## The Two Entities

The baseline refuses the word "student" as ambiguous. It uses two entities instead, and the distinction is load-bearing everywhere:

| Entity | Owns |
| :---- | :---- |
| **Account** | Credentials, billing, devices, notifications, chat participation |
| **Learner** | Enrolments, progress, attendance, exam attempts, certificates |

**Every account has at least one learner.** An adult studying alone is one account with one learner. A guardian with three children is one account with three learners — the guardian is not a learner unless they study, in which case they are a fourth, flagged as the account holder.

See [3I-DEC-001](/3i/decisions/dec-001-learner-as-unit-of-study.md). The practical consequence: every query in the study path filters on **learner**, never on the authenticated account. Authorisation is a separate question — *may this account act for this learner?*

## Account Types

| Type | Age | Logs in | Creates profiles | Chat |
| :---- | :---- | :---- | :---- | :---- |
| Adult account holder | 18+ | Yes | Yes, up to 6 (active + never-activated) | Yes |
| Standalone student | 13–17 | Yes | No | Yes |
| Learner profile | Any — **mandatory under 13** | No: profile picker + mandatory PIN | N/A | Under 13: never. 13–17: guardian toggle |

A 13–17 learner may exist as *either* a standalone account or a profile. Both are supported, they do not behave identically, and any feature touching this band must be specified for both. See [3I-DEC-002](/3i/decisions/dec-002-under-13-family-accounts.md).

## Roles

Three seeded: **Admin**, **Instructor**, **Member**. "Member" replaces the baseline's "Account holder" — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md). No admin UI for role management at launch; adding a role is a database operation, satisfying FR-RBAC-04's "no code change" requirement without a screen.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-IDA-DM-001 | current |
| [requirements/auth-registration-and-authentication.md](requirements/auth-registration-and-authentication.md) | 3I-IDA-REQ-001 | current |
| [requirements/rbac-roles-and-permissions.md](requirements/rbac-roles-and-permissions.md) | 3I-IDA-REQ-002 | current |
| [requirements/fam-family-accounts-and-profiles.md](requirements/fam-family-accounts-and-profiles.md) | 3I-IDA-REQ-003 | current |
| [ui/README.md](ui/README.md) | 3I-IDA-UI-000 | current — 15 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| Every age-dependent rule in the platform | [age-and-safeguarding.md](/3i/age-and-safeguarding.md) |
| What a seat is, and the four-state profile lifecycle | [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md), [3I-DEC-014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md) |
| Ageing up at 13 — **deferred**, no UI documented | [3I-DEC-008](/3i/decisions/dec-008-ageing-up-at-13.md) |

## Delivery

Phase 1, Foundation (§21.1) — RBAC, identity, registration, age gate, family accounts, email. Everything else in the project sits downstream of this module.

## Open Against This Module

| Item | Effect |
| :---- | :---- |
| [OQ-10](/3i/open-questions.md#oq-10--pin-attempt-rate-limiting) | PIN lockout behaviour unspecified. Blocks final sign-off of [Profile picker](ui/screens/profile-picker.md), which documents the gap explicitly rather than guessing |

Everything else previously open against this module — the cap ([OQ-08](/3i/open-questions.md)), devices versus seats ([OQ-03](/3i/open-questions.md)) — is resolved. Ageing up ([OQ-05](/3i/open-questions.md)) is deferred by design, not open.

## Change Requests Owed to the Client

Six decisions in this module change SRD v2.0 rather than interpret it, and interact with each other (the cap, PIN, and device scaling all touch the same profile/seat lifecycle). Worth raising as one consolidated request under §21.3 — full list in [decisions/README.md](/3i/decisions/README.md#scope-changes-against-srd-v20).
