---
project: 3i
type: overview
status: current
updated: 2026-08-16
tags:
  - decision
  - index
---

# 3i Decision Register

One file per recorded decision. Each records the context, the decision, and its consequences. See [../project-standards.md](../project-standards.md#the-decisions-folder) for how decisions are retired.

## Index

| ID | Decision | Status | Primary modules affected |
| :---- | :---- | :---- | :---- |
| [3I-DEC-001](dec-001-learner-as-unit-of-study.md) | `Learner` is the universal unit of study, not `User` | current | IDA, CAT, LDL, ASM, CRT |
| [3I-DEC-002](dec-002-guardian-held-accounts.md) | Minors are reached through guardian-held accounts carrying learner profiles | current | IDA, COM, BIL |
| [3I-DEC-003](dec-003-web-only-stripe-checkout.md) | Checkout is web-only, via Stripe | current | BIL |
| [3I-DEC-004](dec-004-bunny-stream-video-hosting.md) | Video is hosted on Bunny Stream | current | LDL, PLT |
| [3I-DEC-005](dec-005-denormalised-certificates.md) | Certificates are denormalised at issuance | current | CRT |
| [3I-DEC-006](dec-006-question-bank-isolation.md) | Question bank isolation is enforced at the query layer | current | ASM |
| [3I-DEC-007](dec-007-single-admin-role-at-launch.md) | RBAC is fully modelled; one admin role ships at launch | current | IDA, ADM |

## Provenance Note

These decisions were reached through client clarification rounds that have not yet been migrated into `reference/discovery/`. None therefore carries a `derived_from` field, because the parent documents do not exist in this repository yet. Adding the citation is part of the discovery migration, not a separate task.
