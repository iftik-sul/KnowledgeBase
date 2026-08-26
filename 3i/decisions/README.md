---
project: 3i
type: overview
status: current
updated: 2026-08-26
tags:
  - decision
  - index
---

# 3i Decision Register

One file per decision: context, decision, consequences, cost. A decision is never edited to reflect a change of mind — it is superseded or deprecated, and the file stays for history.

## Index

| ID | Decision | Status | Client sign-off | Codes |
| :---- | :---- | :---- | :---- | :---- |
| [3I-DEC-001](dec-001-learner-as-unit-of-study.md) | `Learner` is the unit of study, not `Account` | current | n/a — interpretation | AUTH, FAM |
| [3I-DEC-002](dec-002-under-13-family-accounts.md) | ~~Under-13s exist only as profiles; 13–17 may go standalone~~ | **superseded** (13–17 portion) by 023 | n/a | AUTH, FAM, CHAT |
| [3I-DEC-003](dec-003-web-only-stripe-checkout.md) | Checkout is web-only; the apps carry no purchase surface | current | n/a — interpretation | BILL |
| [3I-DEC-004](dec-004-bunny-stream-video-hosting.md) | Video is hosted on Bunny Stream | current | n/a — interpretation | MAT |
| [3I-DEC-005](dec-005-denormalised-certificates.md) | Certificates are snapshotted at issue | current | n/a — interpretation | CERT |
| [3I-DEC-006](dec-006-question-bank-isolation.md) | Question bank isolation at the query layer, returning 404 | current | n/a — interpretation | QB |
| [3I-DEC-007](dec-007-rbac-without-hardcoded-roles.md) | No hard-coded role checks; new roles are data, not code | current | n/a — interpretation | RBAC |
| [3I-DEC-008](dec-008-ageing-up-at-13.md) | ~~A profile reaching 13 is offered its own account~~ | **deprecated** — idea dropped, see 023 | n/a | AUTH, FAM |
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
| [3I-DEC-023](dec-023-no-standalone-accounts-under-18.md) | No standalone accounts under 18 — every minor is a guardian profile | current | **approved — proceed to build** | AUTH, FAM |
| [3I-DEC-024](dec-024-two-tier-age-based-seat-pricing.md) | Two-tier, age-based seat pricing — two Stripe subscription items per account, not one flat quantity | current | **approved — proceed to build** | BILL |
| [3I-DEC-025](dec-025-waiver-single-profile-cap.md) | Waiver caps the account to one profile, chosen at application, auto-deactivated on approval | current | **approved — proceed to build** | WAV, FAM |
| [3I-DEC-026](dec-026-single-profile-skips-picker.md) | A Member with exactly one profile skips the picker's tile-selection step | current | n/a — UX interpretation | FAM |
| [3I-DEC-027](dec-027-guardian-reviews-on-behalf.md) | Guardian submits ratings/reviews on behalf of under-13 profiles | current | n/a — interpretation, extends 020 | CRS |
| [3I-DEC-028](dec-028-session-delivery-floor-attendance-eligibility.md) | A batch-level session-delivery floor gates attendance-certificate eligibility; resolves OQ-11 | current | **approved — proceed to build** | CERT |
| [3I-DEC-029](dec-029-no-instructor-storage-quota.md) | No per-instructor storage quota — FR-INST-05 dropped | current | **approved — proceed to build** | INST |
| [3I-DEC-030](dec-030-account-type-selector-is-copy-only.md) | Account Type Selector at registration entry is copy-only, not a new account type | current | n/a — UX interpretation | AUTH |
| [3I-DEC-031](dec-031-persistent-account-menu-entry-to-guardian-dashboard.md) | A persistent account menu is the single entry point to Guardian Dashboard, reachable pre-PIN and from any authenticated screen | current | n/a — UX interpretation | AUTH, FAM |
| [3I-DEC-032](dec-032-account-settings-hub.md) | An Account Settings hub sits between the Account Menu and Guardian Dashboard/Device Management/Seat Management/Login \& Security | current | n/a — UX interpretation | AUTH |
| [3I-DEC-033](dec-033-admin-instructor-surface-provisional.md) | The entire admin/instructor surface is provisional pending a separate portal design, including already-confirmed commerce admin screens | current | n/a — design-sequencing | — |
| [3I-DEC-034](dec-034-login-preserves-course-intent.md) | Login preserves which course a visitor was trying to enrol in via return-to redirect; registration does not | current | n/a — UX interpretation | AUTH, CRS, ENR |
| [3I-DEC-035](dec-035-course-detail-cta-three-states.md) | Course Detail's enrolment CTA has three states, not two — an enrolled viewer goes to Course Materials List, not back into enrolment | current | n/a — UX interpretation | CRS, MAT |

**`deferred`** marks a decision taken but consciously parked. **`superseded`** marks a reversed decision, replaced by a specific successor. **`deprecated`** marks a decision whose entire premise no longer applies and is not being replaced — the idea itself was dropped, not redirected. All three keep the file for history; none are rewritten.

**On 3I-DEC-002:** only its 13–17-standalone-account content is superseded by DEC-023. Its under-13-is-profile-only content remains correct and is now also stated directly in DEC-023 itself — see [3I-DEC-002](dec-002-under-13-family-accounts.md)'s superseded notice for the full explanation of what changed and what didn't.

**On the "client sign-off" column, updated 2026-08-18:** all eight decisions carrying client-facing scope changes (014–016, 018–019, 021–023) are marked **approved — proceed to build**, on the basis that Saitama holds effective decision authority on the client's behalf for this engagement. This is a project-level operating assumption recorded here for traceability, not a claim that the institute's own §21.3 written-approval process has been formally exercised. 024, 025, 028, and 029 follow the same basis; 026, 027, 030–032, and 034–035 are UX/safeguarding interpretation only and need no such sign-off; 033 is an internal design-sequencing call with no client-facing behaviour to approve.

## Scope Changes Against SRD v2.0

Every decision below changes what the baseline document says rather than merely interpreting an ambiguity in it — **thirteen items**, updated 2026-08-23 to include everything added since the original eight.

| ID | What it changes |
| :---- | :---- |
| [3I-DEC-014](dec-014-cap-counts-active-profiles-only.md) | Cap counts active + never-activated only, not the flat 6 in FR-FAM-02 |
| [3I-DEC-015](dec-015-device-allowance-scales-with-seats.md) | Device allowance scales with seats, not a flat 3 |
| [3I-DEC-016](dec-016-deletion-removes-content-retains-record.md) | Profile deletion retains the moderation record |
| [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md) | Mandatory guardian-set PIN, not optional |
| [3I-DEC-019](dec-019-safeguarding-strings-exempt-from-ai-translation.md) | Five strings bypass AI translation, require human sign-off |
| [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) | Attendance measured on sessions delivered, plus the WWCC scheduling guard |
| [3I-DEC-022](dec-022-pin-lockout-and-dob-correction-notification.md) | PIN lockout matching FR-AUTH-09; guardian notified on chat-eligibility-changing DOB corrections |
| [3I-DEC-023](dec-023-no-standalone-accounts-under-18.md) | No standalone accounts under 18, at all — the largest single scope change in the project |
| [3I-DEC-024](dec-024-two-tier-age-based-seat-pricing.md) | Two-tier age-based seat pricing replaces the baseline's single flat price |
| [3I-DEC-025](dec-025-waiver-single-profile-cap.md) | Waiver caps the account to one profile while active |
| [3I-DEC-028](dec-028-session-delivery-floor-attendance-eligibility.md) | New session-delivery floor gates attendance-certificate eligibility, resolving OQ-11 and settling `Mixed`-course behaviour the baseline left silent |
| [3I-DEC-029](dec-029-no-instructor-storage-quota.md) | FR-INST-05's storage quota is dropped entirely |

3I-DEC-026, 027, 030–033, and 034–035 are not in this table: none changes stated baseline behaviour — each interprets a baseline silence, a navigation/presentation layer, or (033) a design-sequencing call with no requirements impact at all.

## Change Request — 8 Items, Two Tiers (Historical Record)

Internally approved 2026-08-18, and subsequently treated as approved for build purposes the same day per the note above. Retained here as the record of what was proposed, the reasoning, and the risk framing — useful if the institute is ever asked to review these directly, and as documentation of why each piece of behaviour differs from SRD v2.0.

**Tier 1 — carried the most risk if not approved:**

| ID | Ask |
| :---- | :---- |
| [3I-DEC-014](dec-014-cap-counts-active-profiles-only.md) | Cap counts active + never-activated only, not the flat 6 in FR-FAM-02 |
| [3I-DEC-015](dec-015-device-allowance-scales-with-seats.md) | Device allowance scales with seats — risk framing: a flat 3-device cap against 6 purchasable seats may not survive an Australian Consumer Law challenge |
| [3I-DEC-016](dec-016-deletion-removes-content-retains-record.md) | Profile deletion retains the moderation record — risk framing: without this, a guardian can erase evidence of a reported safety incident |
| [3I-DEC-023](dec-023-no-standalone-accounts-under-18.md) | No standalone accounts under 18, at all. Reverses FR-AUTH-05 outright rather than amending it — the largest single scope change in the project. Flag this to the client distinctly from the rest of the batch, not folded in silently |

**Tier 2 — lower-stakes, expected routine approval:**

| ID | Ask |
| :---- | :---- |
| [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md) | Mandatory guardian-set PIN |
| [3I-DEC-019](dec-019-safeguarding-strings-exempt-from-ai-translation.md) | Human sign-off on safeguarding strings per language — a small task owed by the client, not a design objection. **This item still requires the institute's actual participation** (native-speaker sign-off) regardless of build-approval status, and is not satisfied by the operating assumption above |
| [3I-DEC-021](dec-021-attendance-measured-against-sessions-delivered.md) | Attendance measured on sessions delivered, plus the WWCC scheduling guard — [OQ-11](/3i/open-questions.md#resolved) (minimum sessions before a certificate) has since been resolved by 3I-DEC-028 |
| [3I-DEC-022](dec-022-pin-lockout-and-dob-correction-notification.md) | PIN lockout matching FR-AUTH-09; guardian notified when an admin DOB correction changes chat eligibility |

**On #22 / item 7:** "admin" is the single seeded platform Admin role (FR-RBAC-02), not a separate system-administrator tier, and not something a Member can do to their own child's profile — FR-FAM-07 makes date of birth explicitly non-editable by the account holder.

[3I-DEC-017](dec-017-account-holder-renamed-member.md) was not part of this batch — internal label change only, no client-facing behaviour to approve.

## Change Items Added Since — 3I-DEC-024, 025, 028, 029

| ID | Ask |
| :---- | :---- |
| [3I-DEC-024](dec-024-two-tier-age-based-seat-pricing.md) | Two-tier age-based seat pricing replaces the baseline's single flat "additional seat" price. Confirmed directly by Saitama 2026-08-20 alongside the seat/payment architecture built on it |
| [3I-DEC-025](dec-025-waiver-single-profile-cap.md) | Waiver caps the account to one profile — chosen at application, auto-deactivated on approval — closing the seat-stacking exposure DEC-010 originally left open |
| [3I-DEC-028](dec-028-session-delivery-floor-attendance-eligibility.md) | New session-delivery floor gates attendance-certificate eligibility — resolves OQ-11 and settles `Mixed`-course behaviour the baseline never addressed |
| [3I-DEC-029](dec-029-no-instructor-storage-quota.md) | FR-INST-05's storage quota is dropped entirely, confirmed by Saitama 2026-08-23 |

None were part of the 2026-08-18 batch — all four raised and resolved separately, in direct response to specific client-facing questions as each relevant module was scaffolded.

## Provenance

Decisions 001–007 derive from SRD v2.0 and cite the requirement codes that fix them. Decisions 008–035 were taken outside the baseline: 008–023 in review on 2026-08-18, 024–025 on 2026-08-20 once pricing was confirmed, 026–029 on 2026-08-23, 030–032 on 2026-08-24, and 033–035 on 2026-08-26. Nineteen of them (014–016, 018–019, 021–032, 034–035) are approved for build or need no formal sign-off per the notes above, plus 033 on the same internal-sequencing basis; one (008) is deprecated; one (002) is partially superseded, per the note above.

The client supplied no written material, so no decision here cites a client document. None exists.
