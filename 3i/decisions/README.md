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
| [3I-DEC-014](dec-014-cap-counts-active-profiles-only.md) | The cap counts active and never-activated profiles only | current | **pending — hard-ask** | FAM, BILL |
| [3I-DEC-015](dec-015-device-allowance-scales-with-seats.md) | Device allowance is seats plus two, floor of three | current | **pending — hard-ask** | AUTH |
| [3I-DEC-016](dec-016-deletion-removes-content-retains-record.md) | Deletion removes message content, retains the moderation record | current | **pending — hard-ask** | CHAT, FAM |
| [3I-DEC-017](dec-017-account-holder-renamed-member.md) | The account holder role is renamed `Member` | current | n/a — label only | RBAC |
| [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md) | Profile PIN is mandatory and guardian-controlled | current | pending — proceed unless objected | FAM |
| [3I-DEC-019](dec-019-safeguarding-strings-exempt-from-ai-translation.md) | Safeguarding strings bypass AI translation | current | pending — proceed unless objected | LOC, AUTH, CHAT |
| [3I-DEC-020](dec-020-guardian-on-behalf-chat-retained.md) | Guardian-on-behalf chat participation is retained | current | n/a — interpretation | CHAT |
| [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) | Attendance is measured against sessions delivered | current | pending — proceed unless objected | CERT, INST, BAT |
| [3I-DEC-022](dec-022-pin-lockout-and-dob-correction-notification.md) | PIN lockout matches FR-AUTH-09; DOB corrections notify the guardian on chat-eligibility change | current | pending — proceed unless objected | AUTH, FAM, NOT |

**`deferred`** marks a decision taken but consciously parked — not to be built or documented until approved. **`superseded`** marks a reversed decision, retained for its reasoning and never a basis for implementation.

**`current` and "pending sign-off" are not in tension.** `status: current` means this repository's authoritative position, ready to build from. The **client sign-off** column is a separate axis: whether the *client* has agreed to the scope change under §21.3. A decision can be fully specified and internally approved while still awaiting the client's yes — that is the normal state for anything in the change request below, and it should not be read as unsettled or half-finished documentation.

## Change Request — 7 Items, Two Tiers

Internally approved 2026-08-18. Sent to the client as one consolidated request rather than seven separate ones, split by how it is framed:

**Tier 1 — explicit written sign-off requested, with the risk of not approving stated plainly:**

| ID | Ask |
| :---- | :---- |
| [3I-DEC-014](dec-014-cap-counts-active-profiles-only.md) | Cap counts active + never-activated only, not the flat 6 in FR-FAM-02 |
| [3I-DEC-015](dec-015-device-allowance-scales-with-seats.md) | Device allowance scales with seats — risk framing: a flat 3-device cap against 6 purchasable seats may not survive an Australian Consumer Law challenge |
| [3I-DEC-016](dec-016-deletion-removes-content-retains-record.md) | Profile deletion retains the moderation record — risk framing: without this, a guardian can erase evidence of a reported safety incident |

**Tier 2 — proceeding on this basis unless the client objects:**

| ID | Ask |
| :---- | :---- |
| [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md) | Mandatory guardian-set PIN |
| [3I-DEC-019](dec-019-safeguarding-strings-exempt-from-ai-translation.md) | Human sign-off on ~12 safeguarding strings per language — framed as a small task owed by the client, not a design objection |
| [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) | Attendance measured on sessions delivered, plus the WWCC scheduling guard — raised **together with [OQ-11](/3i/open-questions.md#oq-11--minimum-sessions-before-an-attendance-certificate)**, since the client is likely to ask whether one delivered session should really be enough to qualify |
| [3I-DEC-022](dec-022-pin-lockout-and-dob-correction-notification.md) | PIN lockout matching FR-AUTH-09; guardian notified when an admin DOB correction changes chat eligibility |

**On #22 / item 7 specifically:** "admin" here is the single seeded platform Admin role (FR-RBAC-02) — the same role that already approves instructors, moderates chat, and approves under-13 courses. Not a separate system-administrator tier, and not something a Member can do to their own child's profile — FR-FAM-07 makes date of birth explicitly non-editable by the account holder. Confirmed in review 2026-08-18; worth stating in the client-facing document since "admin" is otherwise ambiguous out of context.

[3I-DEC-017](dec-017-account-holder-renamed-member.md) is intentionally not on this list — it is an internal label change with no behavioural effect, and does not need client sign-off, only note that our documentation and FR-RBAC-02 now use different words for the same role.

## Provenance

Decisions 001–007 derive from SRD v2.0 and cite the requirement codes that fix them. Decisions 008–022 were taken in review on 2026-08-18 and are **not in the baseline**.

The client supplied no written material, so no decision here cites a client document. None exists.
