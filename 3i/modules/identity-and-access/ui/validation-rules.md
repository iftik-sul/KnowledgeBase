---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Identity and Access — Validation Rules

Shared across registration and profile forms. Screens link here rather than restating.

---

## Date of Birth

- Real date picker, not a checkbox (FR-AUTH-02). No default value — an unset field is unset, never silently defaulted to a passing date.
- On submit, computed age determines the registration path: **under 18 blocks** ([3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md), widened from under 13), **18+ proceeds normally.** There is no middle branch — the 13–17 guardian-field path (formerly FR-AUTH-05) no longer exists.
- **The under-18 block fires client-side for immediate feedback, and is re-validated server-side before any account record is created.** Client-side validation alone is not the control — FR-AUTH-04's hashed-attempt logging happens server-side regardless of what the client showed.
- Once submitted on a learner profile, date of birth becomes read-only in every subsequent view (FR-FAM-07). There is no edit affordance in the profile UI at all — not a disabled field, an absent one. Correction is reached only via [Admin — DOB correction](screens/admin-dob-correction.md).

## Email

- Standard format validation, plus uniqueness check against existing accounts.
- **Changing a verified email requires re-verification** of the new address before it takes effect for login purposes; the account keeps working on the old (still verified) address until confirmed.
- **No guardian email field exists anywhere in this module.** [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) removed it along with the standalone-teen path it supported.

## Password

- Minimum 10 characters. No composition rule is enforced or displayed — do not add a strength meter that implies otherwise (FR-AUTH-08).
- Breach check runs after the length check passes, via k-anonymity hash-prefix lookup. The password itself is never transmitted to the breach-check service.

## PIN

- Exactly 4 digits. Set by the guardian only — the form for this is reached from [Profile create/edit](screens/profile-create-edit.md) and [Guardian dashboard](screens/guardian-dashboard.md), never from any learner-facing surface.
- No composition restriction (no "cannot be 0000" rule) — lockout is the real defence, per [3I-DEC-022](/3i/decisions/dec-022-pin-lockout-and-dob-correction-notification.md), matching FR-AUTH-09 exactly.
- Confirmation field required on set (enter twice), no confirmation required on entry at the picker.

## Profile Display Name

- Free text, reasonable length limit (not specified in the baseline — default to 50 characters pending client input).
- **Editable until a certificate is issued to the profile, then locked** (FR-FAM-05). The edit control itself should disappear or disable once locked, with a message naming the reason ("Locked after certificate issue — contact support to change") rather than silently rejecting a submitted change.

## Guardian Age Gate for Profile Creation

- Only a Member whose own account date of birth indicates 18+ can reach the profile creation form (FR-FAM-01). **Every Account is 18+** — [3I-DEC-023](/3i/decisions/dec-023-no-standalone-accounts-under-18.md) — so this gate is now a consistency check rather than an exclusion against a real alternative account type. The "Add profile" affordance is simply absent from any UI surface a profile itself might render, since profiles never have their own session to render it from.
