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

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| AUTH | Registration and authentication | 13 |
| RBAC | Roles and permissions | 5 |
| FAM | Family accounts and learner profiles | 10 |

Twenty-eight requirements. The largest module in the project, and deliberately so.

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
| Adult account holder | 18+ | Yes | Yes, up to 6 | Yes |
| Standalone student | 13–17 | Yes | No | Yes |
| Learner profile | Any — **mandatory under 13** | No: profile picker, optional PIN | N/A | Under 13: never. 13–17: guardian toggle |

A 13–17 learner may exist as *either* a standalone account or a profile. Both are supported, they do not behave identically, and any feature touching this band must be specified for both. See [3I-DEC-002](/3i/decisions/dec-002-under-13-family-accounts.md).

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-IDA-DM-001 | current |
| [requirements/auth-registration-and-authentication.md](requirements/auth-registration-and-authentication.md) | 3I-IDA-REQ-001 | current |
| [requirements/rbac-roles-and-permissions.md](requirements/rbac-roles-and-permissions.md) | 3I-IDA-REQ-002 | current |
| [requirements/fam-family-accounts-and-profiles.md](requirements/fam-family-accounts-and-profiles.md) | 3I-IDA-REQ-003 | current |
| `ui/` | — | not started |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| Every age-dependent rule in the platform | [age-and-safeguarding.md](/3i/age-and-safeguarding.md) |
| What a seat is, and the inactive-profile state | [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) |
| Ageing up at 13 | [3I-DEC-008](/3i/decisions/dec-008-ageing-up-at-13.md) |

## Delivery

Phase 1, Foundation (§21.1) — RBAC, identity, registration, age gate, family accounts, email. Everything else in the project sits downstream of this module.

## Open Against This Module

| Item | Effect |
| :---- | :---- |
| [OQ-08](/3i/open-questions.md#oq-08--do-inactive-profiles-count-against-the-six-profile-cap) | Whether inactive profiles occupy cap slots. Blocks the guardian dashboard and profile picker |
| [OQ-05](/3i/open-questions.md#oq-05--ageing-up-at-13) | Ageing up at 13 — scope change, chat permission handover undefined |
| [OQ-03](/3i/open-questions.md#oq-03--devices-versus-seats) | Device cap versus seat count |
