---
project: 3i
type: decision
status: current
updated: 2026-08-26
id: 3I-DEC-036
tags: [decision, navigation, ux, identity-and-access, catalogue]
---

# Learner Dashboard Is the Profile-Level Study Context Landing Screen

## Context

[Profile Picker](/3i/modules/identity-and-access/ui/screens/profile-picker.md) and [Login](/3i/modules/identity-and-access/ui/screens/login.md) both describe a profile "entering its study context" on successful PIN entry — but neither, nor any other screen, ever defines what that context actually is. Parallel to the gap [3I-DEC-031](dec-031-persistent-account-menu-entry-to-guardian-dashboard.md) closed at the account level (nothing routed *to* Guardian Dashboard), this is the same gap one level down: nothing defines what a learner profile actually lands on.

This surfaced concretely while resolving where a per-profile wishlist ([Course Card](/3i/modules/catalogue/ui/components.md#wishlist-toggle)) should be viewed — confirmed as requiring login and scoped per profile, but with no screen to view it *from* until now.

## Decision

**A new screen, Learner Dashboard, is the definitive landing point for a profile's study context** — reached immediately after successful PIN entry on [Profile Picker](/3i/modules/identity-and-access/ui/screens/profile-picker.md), or the single-profile PIN skip on [Login](/3i/modules/identity-and-access/ui/screens/login.md).

**Where [Guardian Dashboard](/3i/modules/identity-and-access/ui/screens/guardian-dashboard.md) is the Member's account-level hub, Learner Dashboard is the active profile's study-level hub** — the two are deliberate counterparts, not overlapping screens. Guardian Dashboard manages profiles from outside any of them; Learner Dashboard is what one specific profile sees once inside its own session.

**Contents:** Continue Learning (in-progress courses, linking to [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md)), Enrolled Courses (the full list, both Regular and Online Class), Wishlist (this profile's saved courses — satisfies the login requirement automatically, since reaching this screen already requires an authenticated profile session), and Certificates (this profile's own, distinct from Guardian Dashboard's guardian-facing certificate view of the same profile).

## Consequences

- New screen: [`learner-dashboard.md`](/3i/modules/identity-and-access/ui/screens/learner-dashboard.md) (`3I-IDA-UI-019`).
- [`profile-picker.md`](/3i/modules/identity-and-access/ui/screens/profile-picker.md) and [`login.md`](/3i/modules/identity-and-access/ui/screens/login.md)'s "study context" language now links here explicitly instead of remaining undefined.
- [`catalogue/components.md`](/3i/modules/catalogue/ui/components.md)'s wishlist "genuinely open" questions are resolved: login required (confirmed), scoped per profile (confirmed), viewed from Learner Dashboard (confirmed).
- `identity-and-access`'s screen count rises to 18; `mobile-scope.md` totals update accordingly.

**This does not fully resolve the separate Online Class "Go to course" destination gap** flagged in [3I-DEC-035](dec-035-course-detail-cta-three-states.md). Learner Dashboard's Enrolled Courses section is a reasonable landing area for an Online-Class-enrolled profile, but the actual batch-schedule/session-join detail screen still does not exist anywhere in the platform. Related, not solved by this decision — left explicitly open rather than papered over.

## Cost

One new screen to design, and a routing correction on two existing screens. No requirements or data-model impact — this is a navigation and content-aggregation gap-fill, the same category as DEC-031 and DEC-032.
