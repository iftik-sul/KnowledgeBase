---
project: 3i
type: decision
status: current
updated: 2026-08-26
id: 3I-DEC-034
tags: [decision, navigation, ux, catalogue, identity-and-access, learning-delivery]
---

# Login Preserves Course Intent via Return-To Redirect — Registration Does Not

## Context

[Course Detail](/3i/modules/catalogue/ui/screens/course-detail.md) is public — reachable with no session at all — and its enrolment call-to-action links to [Enrol & Waitlist](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md), whose access gate requires a Member session. Nothing documented what happens when an unauthenticated visitor clicks that button. [Login](/3i/modules/identity-and-access/ui/screens/login.md) has no "return to where you were" mechanism today — it only describes routing to Profile Picker or a single profile's PIN pad.

The naive default — authenticate, then land on Profile Picker or Guardian Dashboard with zero memory of the course — would mean re-finding the course from scratch after every login-to-enrol journey, a real conversion cost for a platform whose funnel depends on public browsing leading to enrolment.

## Decision

**Login preserves which course a visitor was trying to enrol in. Registration does not.**

**Login path (existing account holder):** [Course Detail](/3i/modules/catalogue/ui/screens/course-detail.md)'s enrolment CTA, clicked with no session active, routes to [Login](/3i/modules/identity-and-access/ui/screens/login.md) carrying a reference to that specific course. After successful authentication — including the normal profile-selection step (Profile Picker, or the direct-to-PIN-pad skip for a single-profile Member, per [3I-DEC-026](/3i/decisions/dec-026-single-profile-skips-picker.md)) — the Member lands on [Enrol & Waitlist](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md) for that exact course, not the default post-login destination.

**Registration path (new account):** carries **no** course reference. A visitor who registers from Course Detail's CTA lands on Guardian Dashboard with zero profiles, exactly as already documented — no special memory of the originating course. If "Don't have an account? Register" is clicked from within the Login screen reached via this flow, the course reference is dropped at that point rather than threaded into registration.

**Why the asymmetry is deliberate, not an oversight:** registration requires profile creation and seat purchase before enrolment in *any* course is even valid — too many required steps stand between "just registered" and "able to enrol" for a return-to redirect to meaningfully bridge them. Most of the value is in not losing an *already-authenticated* Member's context; threading a course reference through the entire registration funnel for a much smaller payoff was considered and declined.

**Ordinary login (not reached via this flow) is unaffected** — default routing (Profile Picker or single-profile PIN skip) applies unchanged when no course reference is present.

## Consequences

- [`course-detail.md`](/3i/modules/catalogue/ui/screens/course-detail.md): enrolment CTA behaviour now stated explicitly for both the authenticated and unauthenticated cases.
- [`login.md`](/3i/modules/identity-and-access/ui/screens/login.md): documents the return-to behaviour when a course reference is present.
- [`enrol-and-waitlist.md`](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md): access gate section now states both entry paths — direct (already authenticated) and via Login's return-to redirect.

## Cost

A small amount of state (the course reference) needs to survive across the Login screen and whatever authentication steps follow it — typically a query parameter or short-lived session value. Registration deliberately does not carry this complexity, per the scoping above.
