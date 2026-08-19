---
project: 3i
module: identity-and-access
type: data-model
status: current
updated: 2026-08-18
id: 3I-IDA-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - identity
---

# Identity and Access — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## Account

A login identity. Owns credentials, billing relationship, devices, notification preferences, and chat participation.

| Field | Notes |
| :---- | :---- |
| First name, last name | FR-AUTH-01 |
| Email | Unique. Verification mandatory before enrolment, checkout, or chat (FR-AUTH-06) |
| Password hash | Argon2id (FR-AUTH-08) |
| Date of birth | Real date, not an age checkbox (FR-AUTH-02). Determines eligibility to hold an account at all |
| Locale | One of five (FR-LOC-01). Drives notification and email language (FR-NOT-05) |
| Social identity | Google or Apple (FR-AUTH-07). DOB still captured on first login |
| TOTP secret | Optional, admin accounts only (FR-RBAC-05) |

**Every Account is 18+. There is no other kind.** [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) removed the 13–17 standalone account entirely — under-18 registration is refused outright, with no account of any shape created. **`guardianName` and `guardianEmail` fields, previously carried for FR-AUTH-05's standalone-teen path, are removed from this model.** They served no other purpose and have no remaining reader.

**Email changes require re-verification**, following the same mandatory-verification rule as FR-AUTH-06 applies at registration. An account with an unverified new email retains its prior verified state until the new address is confirmed — it does not drop to unverified mid-change.

The **billing contact is separable from the account identity** — name and email on the Stripe customer may differ. For accounts with minor profiles it defaults to the guardian (FR-BILL-05). The Stripe customer record itself is owned by `commerce`, not here.

**An account holder who stops studying keeps their own learner record.** §3.1 requires every account to have at least one learner; there is no path that removes it while leaving the account itself intact. An account holder who stops enrolling in anything simply has a learner profile with no active enrolments — the same shape as any other inactive-by-disuse learner, not a special case.

---

## Learner

A person who studies. Owns enrolments, progress, attendance, exam attempts, and certificates — all of which reference **Learner**, never Account.

| Field | Notes |
| :---- | :---- |
| Display name | **Locks permanently once a certificate is issued** (FR-FAM-05). Admin may unlock with a recorded reason |
| Date of birth | Set at creation, **not user-editable** (FR-FAM-07). Corrections go through admin |
| Avatar | Optional |
| PIN | **Mandatory**, 4-digit, guardian-set (FR-FAM-03 as amended by [3I-DEC-018](/3i/decisions/dec-018-profile-pin-mandatory-guardian-controlled.md)) |
| Account | Owning account. Maximum 6 **active or never-activated** learners per account (FR-FAM-02 as amended by [3I-DEC-014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md)) |
| Activation state | See below — **not in the baseline** |

A learner profile has **no email address and no credentials** (FR-FAM-03). It is selected after account login via a profile picker (FR-FAM-04), which now requires the profile's PIN to enter.

**Every learner under 18 is a profile. There is no other route onto the platform for a minor.** [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) removed the standalone 13–17 account, so a Learner record is now how *every* person under 18 is represented, without exception.

**Chat access is derived from age, never stored as a permission:** under 13 is permanently off; 13–17 is a guardian-controlled toggle (FR-FAM-08). Deriving rather than storing is deliberate — a stored flag can be edited, and the non-editable date of birth is the safeguarding control. **This distinction is unaffected by DEC-023** — it was always about age, not account type, and remains exactly as it was.

### PIN — mandatory, guardian-set, guardian-reset

[3I-DEC-018](/3i/decisions/dec-018-profile-pin-mandatory-guardian-controlled.md) changes FR-FAM-03's optional PIN to mandatory, with three rules the baseline does not state:

- Set by the **guardian** at profile creation, never by the learner.
- Reset only from the **guardian dashboard** — no learner-facing or email recovery, since a profile has no email.
- Required on **every** profile, including the account holder's own.

Rate limiting on entry attempts matches FR-AUTH-09 exactly — [3I-DEC-022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md).

### Activation state — introduced by decision, not by the baseline

The baseline describes only two states: a profile exists, or it is deleted (FR-FAM-10). [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) introduces a third, and it splits into four once creation and activation are distinguished:

| State | Meaning | Counts toward the cap? |
| :---- | :---- | :---: |
| **Never activated** | Created, free, no seat ever purchased | Yes |
| **Active** | A seat is bound to this profile. May enrol and study | Yes |
| **Inactive (cancelled)** | Seat cancelled. Unenrolled, cannot study. **All history preserved** — progress, exam results, certificates | **No** |
| **Deleted** | FR-FAM-10. Progress, enrolments and exam results removed. Issued certificates remain valid and publicly verifiable | No |

A seat is permanently bound to the profile it activates and is never reassigned. Reactivation requires a fresh payment and returns the profile to Active, which re-counts it toward the cap.

**Inactive and deleted must remain visibly distinct in every interface.** They sit close together conceptually and one preserves history while the other destroys it — including chat history, where deletion now removes message content but retains the moderation record ([3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md)).

**Cap resolved:** [3I-DEC-014](/3i/decisions/dec-014-cap-counts-active-profiles-only.md). Never-activated and active count; inactive sits outside the cap as archive.

---

## Role, Permission, and Assignment

Permissions are discrete keys in `module.action` form, assigned to roles, which are assigned to accounts (FR-RBAC-01).

| Entity | Notes |
| :---- | :---- |
| **Permission** | A `module.action` key. Every API route declares the key it requires (FR-RBAC-03) |
| **Role** | A named set of permissions. Held as **data** — adding a role requires no code change and no deployment (FR-RBAC-04) |
| **Assignment** | Account to role |

Three roles are seeded: **Admin** (holds every permission), **Instructor**, **Member** (FR-RBAC-02's "Account holder", renamed — [3I-DEC-017](/3i/decisions/dec-017-account-holder-renamed-member.md)). Admin is the single *admin* role at launch; sub-admin roles and the wider permission matrix are deferred (§23 item 5). See [3I-DEC-007](/3i/decisions/dec-007-rbac-without-hardcoded-roles.md).

**No admin UI for role management is planned at launch.** FR-RBAC-04's "no code change" requirement is satisfied by roles being data; creating one is a database operation at this stage.

A Member may also be a learner — role and learner status are orthogonal.

---

## Device

| Field | Notes |
| :---- | :---- |
| Account | Owning account |
| Identifier, last seen | Visible and de-authorisable by the account holder (FR-AUTH-11) |

**Device allowance scales with seats: seats plus two, floor of three** (FR-AUTH-11 as amended by [3I-DEC-015](/3i/decisions/dec-015-device-allowance-scales-with-seats.md)). One seat gives three devices; six seats gives eight. The swap limit is unchanged at twice per 30 days.

Concurrent video streams are limited to purchased seats, minimum one (FR-AUTH-12) — but per [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) this is **satisfied automatically** and must not be built as a second concurrency check. A profile without a seat cannot enrol, so it cannot stream.

---

## Blocked Registration Attempt

| Field | Notes |
| :---- | :---- |
| Hashed session identifier | FR-AUTH-04 |
| Timestamp | |

Recorded when a date of birth indicates under 18 (FR-AUTH-03 as extended by [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md)), so that a retry with an amended birth year is identifiable as a retry rather than appearing as a fresh attempt. The threshold widened from 13 to 18 when the standalone-teen path was removed — the mechanism itself is unchanged.

This exists purely as a safeguarding control. It holds no personal data — only a hash — and should not be repurposed as general analytics.

---

## Referenced By

Entities here are read across the project. Those modules link to this document rather than restating fields.

| Module | Reads |
| :---- | :---- |
| `learning-delivery` | Learner — enrolment, waitlist, attendance |
| `assessment` | Learner — exam attempts and grades |
| `certification` | Learner — name snapshotted at issue ([3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)) |
| `commerce` | Account — subscription, seats; Learner — seat binding, activation state |
| `communication` | Account — chat participation; Learner — age-derived access |
| `catalogue` | Learner — age-filtered catalogue (FR-CRS-10) |
| `instructors` | Account — instructor role assignment |
