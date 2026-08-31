---
project: 3i
type: decision
status: current
updated: 2026-08-26
id: 3I-DEC-033
tags: [decision, design-system, admin-portal, scope]
---

> **Partially narrowed by [3I-DEC-039](dec-039-instructor-self-service-unpaused.md), 2026-08-26.** This decision's pause now applies to **Admin-role screens only**, across every module. Instructor-role self-service screens (applying, managing own courses/batches, a personal dashboard) originally swept in here are unpaused — see 3I-DEC-039 for the full narrowed scope and reasoning. This file's content below is otherwise unchanged and remains the record of the original, broader decision.

# The Admin/Instructor Surface Is Provisional Pending a Separate Portal Design

## Context

Every screen designed so far — `identity-and-access`, `commerce`, `catalogue` — has used one visual language: the cream/navy/serif system in [`design-system.md`](/3i/design-system.md), derived from the original public-site/learner-facing reference screens. That language has been applied uniformly to Member-facing screens (registration, catalogue browsing, checkout) and admin/instructor-facing screens alike (Waiver Admin Review, Refund Admin Action, and the catalogue module's Course Create/Edit, Admin Review Queue, Admin Course Management, just prompted but not yet confirmed).

**The admin and instructor portal will use a different design** — not yet specified, not yet designed. Continuing to build admin/instructor screens against the current learner-facing system risks producing work that gets discarded wholesale once the real portal design exists, rather than adapted.

## Decision

**The entire admin/instructor surface, across every module, is provisional.** This includes:

- **Already built and confirmed:** [Waiver Admin Review](/3i/modules/commerce/ui/screens/waiver-admin-review.md), [Refund Admin Action](/3i/modules/commerce/ui/screens/refund-admin-action.md) — these are **not final**, despite having passed review against the current design system. They were correct against the spec and the system in use at the time; they are not correct against a portal design that doesn't exist yet.
- **Prompted but not yet run/confirmed:** [Course Create/Edit](/3i/modules/catalogue/ui/screens/course-create-edit.md) (instructor-facing), [Admin Review Queue](/3i/modules/catalogue/ui/screens/admin-review-queue.md), [Admin Course Management](/3i/modules/catalogue/ui/screens/admin-course-management.md) — paused before generation, no Figma work produced against this batch.
- **Not yet started:** [Admin — profile name unlock](/3i/modules/identity-and-access/ui/screens/admin-name-unlock.md), [Admin — DOB correction](/3i/modules/identity-and-access/ui/screens/admin-dob-correction.md), [Admin — TOTP setup](/3i/modules/identity-and-access/ui/screens/admin-totp-setup.md).
- **Shared Member/Admin screens** — [Seat Management](/3i/modules/commerce/ui/screens/seat-management.md), [Billing Portal Redirect](/3i/modules/commerce/ui/screens/billing-portal-redirect.md) — are **not** included in this decision. Both are primarily Member-facing (Admin's access is a support-purpose secondary use of the same screen, not a distinct admin surface), and the confirmed Member-facing design stands.

**No further admin- or instructor-*only* screens should be designed in Figma until the admin/instructor portal's own design direction exists.** The underlying `ui-spec` documents (fields, behavior, access gates, requirements satisfied) are unaffected by this decision and remain the source of truth — only the visual design work pauses.

## Consequences

- `waiver-admin-review.md` and `refund-admin-action.md` carry an explicit provisional notice (added below) so a future reader doesn't mistake their `figma:` link, once added, for a final design.
- The `ui/README.md` in `commerce`, `catalogue`, and `identity-and-access` each note which of their screens fall under this decision.
- Sequencing changes: `catalogue`'s remaining batch (Course Create/Edit, Admin Review Queue, Admin Course Management) is paused, not completed — `catalogue` is **not** fully closed on web as a result, contrary to what would have been true had this batch proceeded.
- No change to requirement satisfaction, data model, or any `FR-` acceptance criteria — this is a design-sequencing decision, not a scope or behavior change.

## Cost

An unknown amount of admin/instructor screen work is now blocked on a portal design direction that doesn't exist yet, with no timeline attached. This includes two screens already spent effort confirming (Waiver Admin Review, Refund Admin Action) that will need to be revisited, not just extended, once that direction exists.
