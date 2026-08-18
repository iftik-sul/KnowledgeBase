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

| ID | Decision | Status | Client sign-off | Codes |
| :---- | :---- | :---- | :---- | :---- |
| [3I-DEC-001](dec-001-learner-as-unit-of-study.md) | `Learner` is the unit of study, not `Account` | current | n/a — interpretation | AUTH, FAM |
| [3I-DEC-002](dec-002-under-13-family-accounts.md) | Under-13s exist only as profiles under a guardian account | current | n/a — interpretation | AUTH, FAM, CHAT |
| [3I-DEC-003](dec-003-web-only-stripe-checkout.md) | Checkout is web-only; the apps carry no purchase surface | current | n/a — interpretation | BILL |
| [3I-DEC-004](dec-004-bunny-stream-video-hosting.md) | Video is hosted on Bunny Stream | current | n/a — interpretation | MAT |
| [3I-DEC-005](dec-005-denormalised-certificates.md) | Certificates are snapshotted at issue | current | n/a — interpretation | CERT |
| [3I-DEC-006](dec-006-question-bank-isolation.md) | Question bank isolation at the query layer, returning 404 | current | n/a — interpretation | QB |
| [3I-DEC-007](dec-007-rbac-without-hardcoded-roles.md) | No hard-coded role checks; new roles are data, not code | current | n/a — interpretation | RBAC |
| [3I-DEC-008](dec-008-ageing-up-at-13.md) | A profile reaching 13 is offered its own account | **deferred** | not raised | AUTH, FAM |
| [3I-DEC-009](dec-009-seats-as-account-pool.md) | A seat is a permanent, non-transferable grant to one profile | current | n/a — interpretation | BILL, ENR, FAM |
| [3I-DEC-010](dec-010-waiver-covers-all-seats.md) | A waiver applies to the whole subscription, seats included | current | n/a — interpretation | WAV |
| [3I-DEC-011](dec-011-attendance-certificate-without-exam.md) | A course with no final exam yields attendance certificates only | current | n/a — interpretation | CERT |
| [3I-DEC-012](dec-012-chat-history-on-profile-deletion.md) | ~~Profile deletion removes chat messages~~ | **superseded** by 016 | n/a | CHAT, FAM |
| [3I-DEC-013](dec-013-instructor-removal-dismisses-course.md) | Losing an instructor mid-course dismisses the course | current | n/a — interpretation | INST, BAT |
| [3I-DEC-014](dec-014-cap-counts-active-profiles-only.md) | The cap counts active and never-activated profiles only | current | **approved — proceed to build** | FAM, BILL |
| [3I-DEC-015](dec-015-device-allowance-scales-with-seats.md) | Device allowance is seats plus two, floor of three | current | **approved — proceed to build** | AUTH |
| [3I-DEC-016](dec-016-deletion-removes-content-retains-record.md) | Deletion removes message content, retains the moderation record | current | **approved — proceed to build** | CHAT, FAM |
| [3I-DEC-017](dec-017-account-holder-renamed-member.md) | The account holder role is renamed `Member` | current | n/a — label only | RBAC |
| [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md) | Profile PIN is mandatory and guardian-controlled | current | **approved — proceed to build** | FAM |
| [3I-DEC-019](dec-019-safeguarding-strings-exempt-from-ai-translation.md) | Safeguarding strings bypass AI translation | current | **approved — proceed to build** | LOC, AUTH, CHAT |
| [3I-DEC-020](dec-020-guardian-on-behalf-chat-retained.md) | Guardian-on-behalf chat participation is retained | current | n/a — interpretation | CHAT |
| [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) | Attendance is measured against sessions delivered | current | **approved — proceed to build** | CERT, INST, BAT |
| [3I-DEC-022](dec-022-pin-lockout-and-dob-correction-notification.md) | PIN lockout matches FR-AUTH-09; DOB corrections notify the guardian on chat-eligibility change | current | **approved — proceed to build** | AUTH, FAM, NOT |

**`deferred`** marks a decision taken but consciously parked — not to be built or documented until approved. **`superseded`** marks a reversed decision, retained for its reasoning and never a basis for implementation.

**On the "client sign-off" column, updated 2026-08-18:** all seven previously-pending items (014, 015, 016, 018, 019, 021, 022) are now marked **approved — proceed to build**, on the basis that Saitama holds effective decision authority on the client's behalf for this engagement. This is a project-level operating assumption recorded here for traceability, not a claim that the institute's own §21.3 written-approval process has been formally exercised. If that assumption changes — if the institute later needs to review these seven items directly — the affected code and documents are identifiable via this table and the [scope-changes list](#change-request--7-items-two-tiers) below, which is retained as the record of what was changed and why.

[3I-DEC-008](dec-008-ageing-up-at-13.md) remains **deferred**, not approved. It was not part of the seven-item batch and has not been raised — see [OQ-05](/3i/open-questions.md#oq-05--ageing-up-at-13).

## Change Request — 7 Items, Two Tiers (Historical Record)

Internally approved 2026-08-18, and subsequently treated as approved for build purposes the same day per the note above. Retained here as the record of what was proposed, the reasoning, and the risk framing — useful if the institute is ever asked to review these directly, and as documentation of why each piece of behaviour differs from SRD v2.0.

**Tier 1 — carried the most risk if not approved:**

| ID | Ask |
| :---- | :---- |
| [3I-DEC-014](dec-014-cap-counts-active-profiles-only.md) | Cap counts active + never-activated only, not the flat 6 in FR-FAM-02 |
| [3I-DEC-015](dec-015-device-allowance-scales-with-seats.md) | Device allowance scales with seats — risk framing: a flat 3-device cap against 6 purchasable seats may not survive an Australian Consumer Law challenge |
| [3I-DEC-016](dec-016-deletion-removes-content-retains-record.md) | Profile deletion retains the moderation record — risk framing: without this, a guardian can erase evidence of a reported safety incident |

**Tier 2 — lower-stakes, expected routine approval:**

| ID | Ask |
| :---- | :---- |
| [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md) | Mandatory guardian-set PIN |
| [3I-DEC-019](dec-019-safeguarding-strings-exempt-from-ai-translation.md) | Human sign-off on ~12 safeguarding strings per language — a small task owed by the client, not a design objection. **This item still requires the institute's actual participation** (native-speaker sign-off) regardless of build-approval status, and is not satisfied by the operating assumption above |
| [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) | Attendance measured on sessions delivered, plus the WWCC scheduling guard — [OQ-11](/3i/open-questions.md#oq-11--minimum-sessions-before-an-attendance-certificate) (minimum sessions before a certificate) remains genuinely open and is not resolved by this approval |
| [3I-DEC-022](dec-022-pin-lockout-and-dob-correction-notification.md) | PIN lockout matching FR-AUTH-09; guardian notified when an admin DOB correction changes chat eligibility |

**On #22 / item 7:** "admin" is the single seeded platform Admin role (FR-RBAC-02), not a separate system-administrator tier, and not something a Member can do to their own child's profile — FR-FAM-07 makes date of birth explicitly non-editable by the account holder.

[3I-DEC-017](dec-017-account-holder-renamed-member.md) was not part of this batch — internal label change only, no client-facing behaviour to approve.

## Provenance

Decisions 001–007 derive from SRD v2.0 and cite the requirement codes that fix them. Decisions 008–022 were taken in review on 2026-08-18 and are **not in the baseline**. Seven of them (014–016, 018–019, 021–022) are approved for build per the note above; one (008) remains deferred.

The client supplied no written material, so no decision here cites a client document. None exists.
