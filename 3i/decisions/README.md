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
| [3I-DEC-006](dec-006-question-bank-isolation.md) | Question bank isolation at the query layer, returning 404 | current | QB |
| [3I-DEC-007](dec-007-rbac-without-hardcoded-roles.md) | No hard-coded role checks; new roles are data, not code | current | RBAC |
| [3I-DEC-008](dec-008-ageing-up-at-13.md) | A profile reaching 13 is offered its own account | **deferred** | AUTH, FAM |
| [3I-DEC-009](dec-009-seats-as-account-pool.md) | A seat is a permanent, non-transferable grant to one profile | current | BILL, ENR, FAM |
| [3I-DEC-010](dec-010-waiver-covers-all-seats.md) | A waiver applies to the whole subscription, seats included | current | WAV |
| [3I-DEC-011](dec-011-attendance-certificate-without-exam.md) | A course with no final exam yields attendance certificates only | current | CERT |
| [3I-DEC-012](dec-012-chat-history-on-profile-deletion.md) | ~~Profile deletion removes chat messages~~ | **superseded** by 016 | CHAT, FAM |
| [3I-DEC-013](dec-013-instructor-removal-dismisses-course.md) | Losing an instructor mid-course dismisses the course | current | INST, BAT |
| [3I-DEC-014](dec-014-cap-counts-active-profiles-only.md) | The cap counts active and never-activated profiles only | current | FAM, BILL |
| [3I-DEC-015](dec-015-device-allowance-scales-with-seats.md) | Device allowance is seats plus two, floor of three | current | AUTH |
| [3I-DEC-016](dec-016-deletion-removes-content-retains-record.md) | Deletion removes message content, retains the moderation record | current | CHAT, FAM |
| [3I-DEC-017](dec-017-account-holder-renamed-member.md) | The account holder role is renamed `Member` | current | RBAC |
| [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md) | Profile PIN is mandatory and guardian-controlled | current | FAM |
| [3I-DEC-019](dec-019-safeguarding-strings-exempt-from-ai-translation.md) | Safeguarding strings bypass AI translation | current | LOC, AUTH, CHAT |
| [3I-DEC-020](dec-020-guardian-on-behalf-chat-retained.md) | Guardian-on-behalf chat participation is retained | current | CHAT |
| [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) | Attendance is measured against sessions delivered | current | CERT, INST, BAT |

**`deferred`** marks a decision taken but consciously parked — not to be built or documented until approved. **`superseded`** marks a reversed decision, retained for its reasoning and never a basis for implementation.

## Scope Changes Against SRD v2.0

These change the baseline rather than interpret it. Each requires a change request under §21.3 **before** being built.

| ID | Changes |
| :---- | :---- |
| [3I-DEC-008](dec-008-ageing-up-at-13.md) | Adds a feature not in the baseline. Deferred — no UI to be documented until approved |
| [3I-DEC-014](dec-014-cap-counts-active-profiles-only.md) | Reinterprets what FR-FAM-02's "maximum 6 profiles" counts |
| [3I-DEC-015](dec-015-device-allowance-scales-with-seats.md) | FR-AUTH-11's flat 3 devices becomes variable |
| [3I-DEC-016](dec-016-deletion-removes-content-retains-record.md) | Extends FR-CHAT-14's treatment to profile deletion |
| [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md) | FR-FAM-03's optional PIN becomes mandatory |
| [3I-DEC-019](dec-019-safeguarding-strings-exempt-from-ai-translation.md) | Carves an exemption out of FR-LOC-02 |
| [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) | Reinterprets FR-CERT-02's denominator; adds a WWCC scheduling constraint |

Seven items. Worth raising as a single change request rather than seven, since several interact.

[3I-DEC-017](dec-017-account-holder-renamed-member.md) sits near this line without crossing it: it renames a role label without changing behaviour, but the repository and FR-RBAC-02 now disagree on one word.

## Provenance

Decisions 001–007 derive from SRD v2.0 and cite the requirement codes that fix them. Decisions 008–021 were taken in review on 2026-08-18 and are **not in the baseline**.

The client supplied no written material, so no decision here cites a client document. None exists.
