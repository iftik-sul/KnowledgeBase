---
project: 3i
type: decision
status: current
updated: 2026-08-26
id: 3I-DEC-038
tags: [decision, navigation, ux, instructors, identity-and-access]
---

# Instructor Registration Combines Account Creation and Application at a Dedicated Landing-Page Entry Point

## Context

[`instructor-application.md`](/3i/modules/instructors/ui/screens/instructor-application.md) already documented a "general 'become an instructor' entry point," but assumed the applicant was already a registered Member — the form only ever collected application-specific fields (bio, expertise, CV, WWCC), never core account fields. A dedicated landing-page button for prospective instructors, reached by someone with **no existing account**, needs the same underlying mechanism to also handle account creation.

This surfaced a real structural question, since two shapes were possible: does the resulting account work normally while only instructor-specific capability stays locked (matching how every other pending/incomplete state on this platform already works — e.g. an unverified email doesn't block the rest of the account), or does approval itself gate all access, a genuinely new kind of locked-account state nothing else in the system has? **Resolved as the former.**

## Decision

**A distinct "Become an Instructor" button exists on the landing page, separate from the general "Get started" button** (which leads to [Account Type Selector](/3i/modules/identity-and-access/ui/screens/account-type-selector.md)'s Myself/Family split, per [3I-DEC-030](/3i/decisions/dec-030-account-type-selector-is-copy-only.md)). This is a third, parallel front door — it does **not** become a third card on Account Type Selector, since it leads somewhere structurally different (a combined registration-and-application form), not a copy variant of the same form.

**The resulting form combines two things previously separate:** the same core account fields and date-of-birth gate as [Registration — Adult](/3i/modules/identity-and-access/ui/screens/registration-adult.md) (name, email, password, DOB — evaluated identically; an instructor applicant under 18 hits the same [Registration Blocked](/3i/modules/identity-and-access/ui/screens/registration-blocked-under-18.md) screen as anyone else, no exception carved out just because this is the instructor entry point), plus the [InstructorApplication](/3i/modules/instructors/data-model.md#instructorapplication) fields already documented (bio, expertise, CV, WWCC number/state/expiry).

**Submission creates both records in one action:** the Account (pending email verification, exactly as any registration) and an `InstructorApplication` row with `status = pending`.

**Per the resolved question above (Option B): the account works normally.** Email verification proceeds exactly as it does for anyone. Once verified, the Member can log in and use the platform like any other Member — **only instructor-specific capability is locked**, not the account itself. Where and how "your application is under review" is actually shown to them is a UI detail, deferred under [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md)'s pause, not resolved by this decision.

**A Notification is sent to the applicant confirming their application is under review** (`communication`, FR-NOT) — new; the existing spec only documented notifying admin of a new submission, never the applicant themselves.

**On admin approval:** [`InstructorProfile`](/3i/modules/instructors/data-model.md#instructorprofile) is created exactly as already documented, unchanged. **An email is sent to the instructor with a link to log in.** Since the account already works (per the resolution above), this email is not unlocking basic access for the first time — it's directing the now-approved instructor toward their newly-unlocked instructor view, functioning as a notification-with-shortcut rather than a first-ever authentication gate.

**The pre-existing path is unaffected and continues to coexist.** An ordinary Member who registered via the standard Myself/Family flow and later decides to apply, reached from account settings, still works exactly as already documented — same `InstructorApplication` mechanism, just without the account-creation fields bundled in, since the account already exists.

## Consequences

- [`instructor-application.md`](/3i/modules/instructors/ui/screens/instructor-application.md) updated to describe both entry paths (existing-Member-via-settings vs. new-landing-page-direct-with-account-creation) and the new applicant-facing notification.
- **The entire screen, in both forms, remains under [3I-DEC-033](/3i/decisions/dec-033-admin-instructor-surface-provisional.md)'s pause for visual design** — this decision locks in behaviour and data flow only, not Figma work. [`instructors/ui/README.md`](/3i/modules/instructors/ui/README.md) updated to flag it accordingly, extending DEC-033's scope to a module it didn't originally enumerate (nothing in `instructors` had been touched yet when DEC-033 was written).

## Cost

None beyond documentation — no new account state, no new data model beyond what already existed. The landing page needs one new button; everything downstream reuses mechanisms already built (Registration's DOB gate, Email Verification, the existing `InstructorApplication` flow).
