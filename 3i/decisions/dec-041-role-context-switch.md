---
project: 3i
type: decision
status: current
updated: 2026-08-26
id: 3I-DEC-041
tags: [decision, navigation, ux, instructors, identity-and-access]
---

# Role-Context Switch — Instructor and Member Views Differ Without Splitting the Account

## Context

[`instructors/README.md`](/3i/modules/instructors/README.md#instructor-is-a-role-held-by-an-account-not-a-separate-identity) is explicit and load-bearing: an instructor is the same Account as the Member who applied, not a separate identity — [`instructor-application.md`](/3i/modules/instructors/ui/screens/instructor-application.md)'s "Path 2" (an existing Member applying later, on the same account) and the `instructorId` fields already built into `catalogue` and `learning-delivery` both depend on this being true. That principle is not up for reversal.

But [3I-DEC-040](dec-040-instructor-registration-confirmation-screen.md) routed a just-registered instructor applicant's "Continue" button to **Guardian Dashboard** — ordinary Member UI, regardless of why they registered. For someone who registered specifically to teach, landing in "manage your children's profiles" content is a genuine mismatch, even though the underlying account is correctly unified. The fix is a **navigation-layer** concept, not a data-model one: which "home" an Account with more than one usable role sees, without that role ever being a second account.

This also resolves a gap [3I-DEC-040](dec-040-instructor-registration-confirmation-screen.md) explicitly left open: no persistent "application under review" view existed anywhere — only a one-time confirmation screen, shown once and never again.

## Decision

**A Role Context determines what an Account's login lands on, evaluated in this order:**

1. **Approved Instructor role exists** (`InstructorProfile` present) → lands on [Instructor Dashboard](/3i/modules/instructors/ui/screens/instructor-dashboard.md).
2. **A `pending` `InstructorApplication` exists, no approved role yet** → lands on a new screen, [Instructor Application Status](/3i/modules/instructors/ui/screens/instructor-application-status.md) — shown on **every** login while pending, not just once (unlike [3I-DEC-040](dec-040-instructor-registration-confirmation-screen.md)'s one-time Confirmation screen, which remains a separate, single-occurrence welcome moment immediately after verification).
3. **Neither** → the existing, unchanged Member flow (Profile Picker or single-profile PIN skip, per [3I-DEC-026](dec-026-single-profile-skips-picker.md)).

**This is a login-time default, not an account split.** An Account satisfying case 1 that *also* holds learner profiles (i.e. is also a parent using the platform as a guardian) defaults to Instructor Dashboard — reasoned as the more likely primary intent once the role is actually granted — but can **switch context** via a new control on the [Account Menu](/3i/modules/identity-and-access/ui/components.md#account-menu): "Switch to Member view" / "Switch to Instructor view," shown only when an Account genuinely holds more than one context. This mirrors the existing active-learner-profile pattern already used elsewhere in this module — a context selected inside one session, not a second identity.

**[3I-DEC-040](dec-040-instructor-registration-confirmation-screen.md)'s Confirmation screen's "Continue" button now routes to [Instructor Application Status](/3i/modules/instructors/ui/screens/instructor-application-status.md)**, not Guardian Dashboard — the one concrete change to that decision's behaviour, made here rather than by editing DEC-040 itself.

**Rejected applications are not a new context.** Once a `pending` application resolves to `rejected` with no new pending row, case 2 no longer applies and login falls through to the ordinary Member flow (case 3) — [`instructor-application.md`](/3i/modules/instructors/ui/screens/instructor-application.md)'s existing re-application path already covers what happens next, unchanged by this decision.

## Consequences

- New screen: [`instructor-application-status.md`](/3i/modules/instructors/ui/screens/instructor-application-status.md) (`3I-INS-UI-007`) — persistent pending-state view, distinct from the one-time Confirmation screen.
- [`instructor-application-confirmation.md`](/3i/modules/instructors/ui/screens/instructor-application-confirmation.md) updated: "Continue" destination changed.
- [`identity-and-access/ui/components.md`](/3i/modules/identity-and-access/ui/components.md)'s Account Menu entry updated with the role-context switch control.
- [`login.md`](/3i/modules/identity-and-access/ui/screens/login.md)'s Post-Login Routing section gains the three-case priority order above.

## Cost

One new screen, one new control on an existing shared component, and a routing-priority rule that must stay correct as more roles are potentially added later (this project currently only has Member and Instructor as contexts a single Account can hold — Admin is deliberately excluded from this switch, since an Admin account's own portal is a separate, still-paused surface under [3I-DEC-033](dec-033-admin-instructor-surface-provisional.md)/[3I-DEC-039](dec-039-instructor-self-service-unpaused.md), not part of this context system).
