---
project: 3i
type: overview
status: current
updated: 2026-08-18
tags:
  - decision
  - index
---

# 3i Decision Register

One file per decision: context, decision, consequences, cost. A decision is never edited to reflect a change of mind — it is superseded.

## Index

| ID | Decision | Status | Codes |
| :---- | :---- | :---- | :---- |
| [3I-DEC-001](dec-001-learner-as-unit-of-study.md) | `Learner` is the unit of study, not `Account` | current | AUTH, FAM |
| [3I-DEC-002](dec-002-under-13-family-accounts.md) | Under-13s exist only as profiles under a guardian account | current | AUTH, FAM, CHAT |
| [3I-DEC-003](dec-003-web-only-stripe-checkout.md) | Checkout is web-only; the apps carry no purchase surface | current | BILL |
| [3I-DEC-004](dec-004-bunny-stream-video-hosting.md) | Video is hosted on Bunny Stream | current | MAT |
| [3I-DEC-005](dec-005-denormalised-certificates.md) | Certificates are snapshotted at issue | current | CERT |
| [3I-DEC-006](dec-006-question-bank-isolation.md) | Question bank isolation is enforced at the query layer, returning 404 | current | QB |
| [3I-DEC-007](dec-007-rbac-without-hardcoded-roles.md) | No hard-coded role checks; new roles are data, not code | current | RBAC |
| [3I-DEC-008](dec-008-ageing-up-at-13.md) | A profile reaching 13 is offered its own account | draft | AUTH, FAM |
| [3I-DEC-009](dec-009-seats-as-account-pool.md) | Seats are an account-level pool, not tied to a profile | draft | BILL, ENR |
| [3I-DEC-010](dec-010-waiver-covers-all-seats.md) | A waiver applies to the whole subscription, seats included | current | WAV |
| [3I-DEC-011](dec-011-attendance-certificate-without-exam.md) | A course with no final exam yields attendance certificates only | current | CERT |
| [3I-DEC-012](dec-012-chat-history-on-profile-deletion.md) | Profile deletion removes that profile's chat messages | draft | CHAT, FAM |
| [3I-DEC-013](dec-013-instructor-removal-dismisses-course.md) | Losing an instructor mid-course dismisses the course | draft | INST, BAT |

`draft` marks a decision taken but carrying an unresolved consequence recorded in [../open-questions.md](../open-questions.md). It is not a weaker decision — it is one whose downstream effects are not yet specified.

## Provenance

Decisions 001–007 are derived from SRD v2.0 and cite the requirement codes that fix them. Decisions 008–013 were taken in review on 2026-08-18 and are **not in the baseline**; those that change scope require a change request under §21.3.

The client supplied no written material, so no decision here cites a client document. None exists.
