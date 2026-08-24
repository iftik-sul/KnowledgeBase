---
project: 3i
type: decision
status: current
updated: 2026-08-24
id: 3I-DEC-031
tags: [decision, navigation, ux, identity-and-access]
---

# A Persistent Account Menu Is the Single Entry Point to Guardian Dashboard

## Context

[Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md) holds every account-level action that matters regardless of which profile is active or locked — seat purchase, cancellation, PIN reset, profile deletion. Its access gate is simply "an authenticated Member" ([`profile-create-edit.md`](/3i/modules/identity-and-access/ui/screens/profile-create-edit.md#access-gate) states the same gate for its own reachability): it is **not** PIN-gated.

The gap: nothing in the module actually routes a Member *to* Guardian Dashboard. [`login.md`](/3i/modules/identity-and-access/ui/screens/login.md) routes into [Profile Picker](/3i/modules/identity-and-access/ui/screens/profile-picker.md) or directly to a PIN pad. Profile Picker only describes selecting a tile toward PIN entry. Every other screen that leads *from* Guardian Dashboard states so explicitly (e.g. [`profile-deletion-confirmation.md`](/3i/modules/identity-and-access/ui/screens/profile-deletion-confirmation.md): "reached only from Guardian dashboard") — but Guardian Dashboard itself never states how a Member gets there in the first place.

This surfaced concretely while designing Profile Picker: a forgotten-PIN question exposed that there is no path back to account-level actions either **before** picking a profile, or **from within an active study session** after one is already picked.

## Decision

**A persistent account-menu affordance is the single entry point to Guardian Dashboard, present consistently in two places:**

1. **On [Profile Picker](/3i/modules/identity-and-access/ui/screens/profile-picker.md) itself**, reachable before any PIN is entered — a Member should never be forced through a child's PIN just to reset that same PIN.
2. **In the header chrome of every screen inside an authenticated study session**, regardless of which profile is currently active — a small, always-visible account affordance (not tied to any one module's screen) that opens straight to Guardian Dashboard.

**The access rule is identical in both places, matching Guardian Dashboard's own gate exactly: any authenticated Member, never PIN-gated, regardless of study-session or lockout state.** A PIN lockout on every single profile on the account still leaves the Member's own login able to reach billing and PIN resets — the two are deliberately independent, the same separation [`profile-picker.md`](/3i/modules/identity-and-access/ui/screens/profile-picker.md) already establishes between a Member's own login and a profile's PIN.

**Reference pattern, not a literal copy:** Netflix uses exactly this shape — a persistent profile/account icon, present on the profile-selection screen and inside every active profile's session alike, opening a menu that includes profile management and account/billing. Resetting a Netflix profile's PIN lock requires the **account password**, never the old PIN — the same two-key separation this project already committed to independently via [3I-DEC-018](dec-018-profile-pin-mandatory-guardian-controlled.md). What was missing here was purely the entry point, not the underlying access model, which was already correct.

## Consequences

- [`profile-picker.md`](/3i/modules/identity-and-access/ui/screens/profile-picker.md) needs an explicit account-menu affordance added to its default frame, reachable before PIN entry.
- [`guardian-dashboard.md`](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md) needs an explicit "reached from" statement added — the one screen in the module missing this, now that there's something concrete to name.
- The account-menu affordance itself is documented as a shared component in [`identity-and-access/components.md`](/3i/modules/identity-and-access/ui/components.md), even though it physically renders in the header chrome of screens belonging to every other module. This mirrors an existing precedent: `localisation`'s Locale Switcher is documented the same way — global chrome, owned by the module whose screen it routes to, not restated per module. See [`localisation/ui/README.md`](/3i/modules/localisation/ui/README.md).
- Every module's authenticated screens now implicitly inherit this piece of chrome. Retrofitting an explicit mention into all thirteen modules' existing screen docs is not required by this decision — new screens designed from here forward should include it as a matter of course; existing screens are not blocked on a retroactive documentation pass.

## Cost

This is the first component in `identity-and-access/components.md` whose footprint is genuinely platform-wide rather than module-local — every authenticated screen, in every module, on both web and the eventual Flutter build, needs to carry this chrome consistently. That is a larger and more diffuse surface than a typical shared component, and worth a future reader knowing was a deliberate choice, not scope creep into `identity-and-access`'s own boundaries.
