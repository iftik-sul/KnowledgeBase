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
| Date of birth | Real date, not an age checkbox (FR-AUTH-02). Determines account type |
| Locale | One of five (FR-LOC-01). Drives notification and email language (FR-NOT-05) |
| Guardian name, guardian email | **Only for 13–17 standalone accounts** (FR-AUTH-05) |
| Social identity | Google or Apple (FR-AUTH-07). DOB still captured on first login |
| TOTP secret | Optional, admin accounts only (FR-RBAC-05) |

**Account type is derived from date of birth, not stored as a flag.** Under 13 cannot exist as an account at all (FR-AUTH-03). 13–17 is a standalone student. 18+ is an adult account holder.

The **billing contact is separable from the account identity** — name and email on the Stripe customer may differ. For accounts with minor profiles it defaults to the guardian (FR-BILL-05). The Stripe customer record itself is owned by `commerce`, not here.

---

## Learner

A person who studies. Owns enrolments, progress, attendance, exam attempts, and certificates — all of which reference **Learner**, never Account.

| Field | Notes |
| :---- | :---- |
| Display name | **Locks permanently once a certificate is issued** (FR-FAM-05). Admin may unlock with a recorded reason |
| Date of birth | Set at creation, **not user-editable** (FR-FAM-07). Corrections go through admin |
| Avatar | Optional |
| PIN | Optional, 4-digit (FR-FAM-03) |
| Account | Owning account. Maximum 6 learners per account (FR-FAM-02) |
| Activation state | See below — **not in the baseline** |

A learner profile has **no email address and no credentials** (FR-FAM-03). It is selected after account login via a profile picker (FR-FAM-04).

**Chat access is derived from age, never stored as a permission:** under 13 is permanently off; 13–17 is a guardian-controlled toggle (FR-FAM-08). Deriving rather than storing is deliberate — a stored flag can be edited, and the non-editable date of birth is the safeguarding control.

### Activation state — introduced by decision, not by the baseline

The baseline describes only two states: a profile exists, or it is deleted (FR-FAM-10). [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) introduces a third.

| State | Meaning |
| :---- | :---- |
| **Active** | A seat is bound to this profile. May enrol and study |
| **Inactive** | Seat cancelled. Unenrolled, cannot study. **All history preserved** — progress, exam results, certificates |
| **Deleted** | FR-FAM-10. Progress, enrolments and exam results removed. Issued certificates remain valid and publicly verifiable |

A seat is permanently bound to the profile it activates and is never reassigned. Reactivation requires a fresh payment.

**Inactive and deleted must remain visibly distinct in every interface.** They sit close together conceptually and one destroys history while the other does not.

**Unresolved:** whether an inactive profile occupies one of the six cap slots — [OQ-08](/3i/open-questions.md#oq-08--do-inactive-profiles-count-against-the-six-profile-cap). If it does, a guardian must delete a child's history to add a seventh profile.

---

## Role, Permission, and Assignment

Permissions are discrete keys in `module.action` form, assigned to roles, which are assigned to accounts (FR-RBAC-01).

| Entity | Notes |
| :---- | :---- |
| **Permission** | A `module.action` key. Every API route declares the key it requires (FR-RBAC-03) |
| **Role** | A named set of permissions. Held as **data** — adding a role requires no code change and no deployment (FR-RBAC-04) |
| **Assignment** | Account to role |

Three roles are seeded: **Admin** (holds every permission), **Instructor**, **Account holder** (FR-RBAC-02). Admin is the single *admin* role at launch; sub-admin roles and the wider permission matrix are deferred (§23 item 5). See [3I-DEC-007](/3i/decisions/dec-007-rbac-without-hardcoded-roles.md).

An account holder may also be a learner — role and learner status are orthogonal.

---

## Device

| Field | Notes |
| :---- | :---- |
| Account | Owning account |
| Identifier, last seen | Visible and de-authorisable by the account holder (FR-AUTH-11) |

Maximum **3 registered devices** per account. Device swap permitted **twice per 30 days** (FR-AUTH-11).

Concurrent video streams are limited to purchased seats, minimum one (FR-AUTH-12) — but per [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md) this is **satisfied automatically** and must not be built as a second concurrency check. A profile without a seat cannot enrol, so it cannot stream.

The device cap and the seat count can conflict: a family buying five seats cannot use them from three devices. Unresolved — [OQ-03](/3i/open-questions.md#oq-03--devices-versus-seats).

---

## Blocked Registration Attempt

| Field | Notes |
| :---- | :---- |
| Hashed session identifier | FR-AUTH-04 |
| Timestamp | |

Recorded when a date of birth indicates under 13 (FR-AUTH-03), so that a retry with an amended birth year is identifiable as a retry rather than appearing as a fresh attempt.

This exists purely as a safeguarding control. It holds no personal data — only a hash — and should not be repurposed as general analytics.

---

## Referenced By

Entities here are read across the project. Those modules link to this document rather than restating fields.

| Module | Reads |
| :---- | :---- |
| `learning-delivery` | Learner — enrolment, waitlist, attendance |
| `assessment` | Learner — exam attempts and grades |
| `certification` | Learner — name snapshotted at issue ([3I-DEC-005](/3i/decisions/dec-005-denormalised-certificates.md)) |
| `commerce` | Account — subscription, seats; Learner — seat binding |
| `communication` | Account — chat participation; Learner — age-derived access |
| `catalogue` | Learner — age-filtered catalogue (FR-CRS-10) |
| `instructors` | Account — instructor role assignment |
