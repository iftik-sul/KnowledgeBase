---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-26
id: 3I-CAT-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - catalogue
---

# Screen: Course Detail

Satisfies: FR-CRS-01, FR-CRS-06, FR-CRS-11

---

## Purpose

Full course information — the page a learner reads before enrolling, and the page a public visitor reads before creating an account.

## Access Gate

Public, for any `published` course. A `draft`, `pending_review`, `suspended`, or `taken_down` course returns a not-found response to anyone other than its owning instructor or an admin — same treatment as any other absent-not-disabled content on this platform.

## Contents

- Title, summary, description, learning outcomes, category, type, level, language (FR-CRS-01).
- **Full numeric age range** (`minimumAge`–`maximumAge`), not just the band — the one place on the platform this precision is shown, since [Course Card](../components.md#course-card) only shows the band.
- Instructor name and bio, read from `instructors`' `InstructorProfile`.
- Average rating and the list of `visible`-status Reviews, each showing the reviewer's display name — self-submitted reviews show the learner's own name; guardian-submitted reviews show the guardian-attribution format per [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md).
- Enrolment call-to-action — the actual enrolment flow lives in `learning-delivery`; this screen links out to it rather than duplicating it.

### Class Schedule — Online Class / Mixed Courses Only

Not specified in the eleven FR-CRS requirements; added here as a reasonable default, not confirmed with the client. **Regular courses have no schedule section at all** — nothing to schedule for self-paced materials.

For an Online Class or Mixed course, one card per open [`Batch`](/3i/modules/learning-delivery/data-model.md#batch), each showing the batch's start date and current seat availability (plain `slate-600` text when seats are readily available, `error-600` text-only when nearly full — no fill or badge either way, per [design-system.md](/3i/design-system.md)'s general treatment of nudge-weight states).

**Every session in the batch is listed individually, not just summarised as a session count.** Each batch card expands to show its full session list — one [Session Row](/3i/modules/learning-delivery/ui/components.md#session-row) (read-only variant) per session, showing that session's specific date, time, and duration. A 12-session batch shows 12 rows when expanded, not "12 sessions" as a single summary line — a learner deciding whether a class fits their schedule needs the actual dates and times, not just a count.

**Times are always shown in the viewer's own local time zone**, converted automatically — see [Session Row](/3i/modules/learning-delivery/ui/components.md#session-row)'s own note on this. No timezone selector exists anywhere on this screen or elsewhere in the platform; the conversion is transparent to the learner.

Batch cards remain **informational only** — selecting a specific batch happens on [Enrol \& Waitlist](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md), not here. Whether clicking a batch card here should pre-select that batch on arrival at Enrol & Waitlist is a related, still-open UX question, not resolved by this section.

### Enrolment CTA — Three States

Per [3I-DEC-034](/3i/decisions/dec-034-login-preserves-course-intent.md) and [3I-DEC-035](/3i/decisions/dec-035-course-detail-cta-three-states.md):

| State | Button reads | Destination |
| :---- | :---- | :---- |
| No active session | (per DEC-034) | [Login](/3i/modules/identity-and-access/ui/screens/login.md), carrying a reference to this course. On success, lands on [Enrol \& Waitlist](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md) for this course. **Registering instead of logging in drops the course reference** — lands on Guardian Dashboard with zero profiles, same as any new registration |
| Session active, no qualifying enrolment on this course | "View enrolment options" | [Enrol \& Waitlist](/3i/modules/learning-delivery/ui/screens/enrol-and-waitlist.md), directly — **no sign-in prompt**, since an active session already exists. The button label is deliberately identical to the logged-out state; only the destination differs |
| Session active, a qualifying enrolment already exists | "Go to course" | [Course Materials List](/3i/modules/materials/ui/screens/course-materials-list.md) — **not** back into enrolment |

**The enrolled-state check is at the Member level**, across any of the Member's profiles — not tied to whichever profile is currently active in the session, same check [Rate \& Review](rate-and-review.md) already performs. Resolving which specific profile's materials to open follows the same logic as Rate & Review's profile selection: implicit if only one profile qualifies, a selection step if more than one does.

### Review Display — Inline Preview + Full List Modal

Not specified in the eleven FR-CRS requirements; added here as a reasonable default, not confirmed with the client, matching how pagination on [Catalogue Browse](catalogue-browse.md) is flagged the same way.

**Inline on the page:** the 2 most recent `visible`-status reviews only, not the full list — a course with dozens of reviews should not make the page itself unboundedly long.

**The review count next to the average rating (e.g. "(24 reviews)") is a clickable trigger**, not static text. Clicking it opens a **modal** containing every `visible`-status review, in a scrollable list, without navigating away from Course Detail. The modal does not paginate internally — it scrolls, since a review list is bounded per-course and unlikely to reach a size where pagination inside a modal is warranted (unlike Catalogue Browse's platform-wide, 140+-result list, which does paginate).

Both the inline preview and the modal apply the same self-submitted/guardian-attribution display rule per review — the modal is not a simplified or stripped-down view, it's the same review cards shown at full list length.

## Role Variations

None for viewing — identical for Public and Member. An enrolled Member additionally sees a **Rate \& review** entry point once their enrolment qualifies (see [Rate \& Review](rate-and-review.md)); a non-enrolled visitor does not see that entry point at all, rather than seeing it disabled.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04). The review modal's scroll direction and close-button position also mirror for Arabic and Urdu. The Class Schedule section's session-list expansion direction mirrors as well.
