---
project: 3i
type: decision
status: current
updated: 2026-08-26
id: 3I-DEC-040
tags: [decision, navigation, ux, instructors, identity-and-access]
---

# Instructor Registration Gets a One-Time Post-Verification Confirmation Screen

## Context

[3I-DEC-038](dec-038-instructor-registration-account-works-normally.md) explicitly deferred where and how "your application is under review" is shown to a newly-registered instructor applicant, at the time under [3I-DEC-033](dec-033-admin-instructor-surface-provisional.md)'s blanket pause. [3I-DEC-039](dec-039-instructor-self-service-unpaused.md) has since unpaused exactly this kind of Member-facing screen, leaving the deferral outstanding rather than resolved — nobody had gone back to settle it until now.

## Decision

**A dedicated, one-time confirmation screen** is shown immediately after the [Email Verification](/3i/modules/identity-and-access/ui/screens/email-verification.md) link is clicked, **only for the combined instructor-registration path** ([`instructor-application.md`](/3i/modules/instructors/ui/screens/instructor-application.md) Path 1). An ordinary Member registering through the standard Myself/Family flow sees no such screen — this is specific to having just submitted a teaching application in the same action as account creation.

**Content:** confirms both things that just happened at once — the email is verified, and the teaching application is under review — rather than treating them as two separate moments the person has to piece together themselves.

**After acknowledging, the Member proceeds to [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md)**, the same destination any new registration reaches — no special instructor-only landing page exists at this stage, consistent with [3I-DEC-038](dec-038-instructor-registration-account-works-normally.md)'s core resolution that the account works exactly like any other Member's until approval. They can ignore Guardian Dashboard's profile-management content entirely if they have no interest in it; nothing about this decision changes what that screen contains.

**Scope, deliberately narrow:** this decision covers only the one-time confirmation screen. It does **not** introduce a persistent "application under review" indicator anywhere else (e.g. Account Settings) — that was a separate option considered and not chosen here. If ongoing visibility into a pending application turns out to be needed later, that's a distinct decision, not assumed by this one.

## Consequences

- New screen: [`instructor-application-confirmation.md`](/3i/modules/instructors/ui/screens/instructor-application-confirmation.md) (`3I-INS-UI-006`).
- [`email-verification.md`](/3i/modules/identity-and-access/ui/screens/email-verification.md) updated to name this as an explicit destination case, alongside its existing generic "returns to wherever the person was headed" language.
- [`instructor-application.md`](/3i/modules/instructors/ui/screens/instructor-application.md) updated to link forward to this screen from its Behaviour section.

## Cost

One small new screen. No data model impact — purely a presentation-layer addition confirming state that already exists (`InstructorApplication.status = pending`).
