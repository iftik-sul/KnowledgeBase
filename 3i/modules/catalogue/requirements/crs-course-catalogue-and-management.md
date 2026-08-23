---
project: 3i
module: catalogue
type: requirements
status: current
updated: 2026-08-23
id: 3I-CAT-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - catalogue
---

# Course Catalogue and Management

Baseline §8. Eleven requirements, one amended by decision — [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md) (guardian submits reviews for under-13 profiles).

---

## Creation and Publishing

| ID | Requirement |
| :---- | :---- |
| **FR-CRS-01** | Course creation captures title, summary, description, learning outcomes, thumbnail, category, type, level, language, **minimum age (mandatory)**, and optional maximum age |
| **FR-CRS-02** | The age field has **no default**. A course cannot be saved without an explicit choice |
| **FR-CRS-03** | A course cannot be published without an age tag, at least one material or batch, and a thumbnail |

FR-CRS-02 applies at **save**, not just at publish — a course cannot exist in the database with an implicit or blank age. This is stricter than the publish gate (FR-CRS-03), which additionally requires the thumbnail and at least one piece of content, and only applies at the publish action. See [data-model.md](../data-model.md#publish-gate) for the full status-transition table.

---

## Admin Review and Moderation

| ID | Requirement |
| :---- | :---- |
| **FR-CRS-04** | Courses tagged **under 13 require admin approval** before publication. All other courses publish without approval |
| **FR-CRS-05** | Admin may edit, suspend, or take down any course |

FR-CRS-04's threshold is the course's `minimumAge`, not its maximum — a course open to ages 10–16 requires approval; a course open to 13–17 does not, even though both include the 13–15 band. This mirrors the platform's general pattern of gating on the more restrictive boundary a course could be used against, consistent with FR-AUTH-03's under-13 registration block using the same threshold for the same underlying reason.

FR-CRS-05's suspend and take-down actions are distinct: suspension is reversible and the baseline elsewhere (FR-INST-07) treats a suspended course's enrolled learners as retaining access to completed materials — the same principle applies here, since suspending a course is an availability change for *new* enrolment, not a retroactive removal of what existing learners already have.

---

## Age Bands

| ID | Requirement |
| :---- | :---- |
| **FR-CRS-06** | Course cards display the age band (5–8, 9–12, 13–15, 16–17, 18+, All ages) |

This is the same six-band system already defined for learner profiles — [Age Band Badge](/3i/modules/identity-and-access/ui/components.md#age-band-badge) — reused rather than redefined, since FR-CRS-10's age filtering depends on a course's band and a learner's band meaning the same thing. See [data-model.md](../data-model.md#course) for how a course's two-field age range (`minimumAge`/`maximumAge`) reduces to a single displayed band on a card.

---

## Search

| ID | Requirement |
| :---- | :---- |
| **FR-CRS-07** | Catalogue search covers title, summary, description, and instructor name, using PostgreSQL full-text search with trigram fuzzy matching |

Instructor name is searched by reference to the `instructors` module (not yet built — see [data-model.md](../data-model.md#forward-references)); the search index itself can be built against Course's own fields today and extended once instructor records exist.

---

## Filters and Sort

| ID | Requirement |
| :---- | :---- |
| **FR-CRS-08** | Filters: category, course type, level, age band, minimum rating, language, has upcoming batch |
| **FR-CRS-09** | Sort: relevance, newest, most enrolled, highest rated, title A–Z |

"Has upcoming batch" and "most enrolled" both read from `learning-delivery` (not yet built). Both filters/sorts are specified here against the Course entity's eventual join to Batch and Enrolment; neither can be implemented before that module exists, and both should be treated as no-op (or simply hidden) filter options until it does, rather than silently returning wrong results.

---

## The Age Gate

| ID | Requirement |
| :---- | :---- |
| **FR-CRS-10** | **When a learner profile is active, the catalogue displays only courses whose age range includes that learner's age.** |

This is the module's one safeguarding-relevant requirement, and it is a hard filter, not a sort weight or a "recommended for you" ranking signal — a course outside the active profile's age range must not appear at all, not appear lower. **Public browsing (no profile active) is unfiltered** — the age gate only engages once a specific learner's context is known, consistent with how [Profile Picker](/3i/modules/identity-and-access/ui/screens/profile-picker.md) establishes that context after login.

The enrolment-override path (FR-ENR-04, guardian may override upward by up to 2 years) is `learning-delivery`'s concern, not this module's — the catalogue's own filtering stays strict; the override happens at the enrolment step, after a learner has already found a course through some other means (a direct link, for instance) that the catalogue's own filter would not have surfaced.

---

## Ratings and Reviews

| ID | Requirement |
| :---- | :---- |
| **FR-CRS-11** | Learners may rate a course 1–5 with an optional written review, once per course, only after enrolment. Admin may hide a review |

**Amended by [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md):** for an under-13 profile, the guardian submits on the profile's behalf, displayed with the same guardian-attribution format used in chat. The one-review-per-course limit is keyed to the learner profile, not the submitting account. The enrolment check this requirement depends on reads from `learning-delivery` (not yet built) — see [data-model.md](../data-model.md#forward-references).

---

## Acceptance Criteria

1. Saving a course without an age tag is refused, at save time, not only at publish.
2. A course tagged minimum age 8 enters `pending_review` rather than `published` on the publish action; a course tagged minimum age 13 publishes directly.
3. A nine-year-old profile's catalogue view contains zero courses whose `minimumAge` exceeds 9 or whose `maximumAge` (where set) is below 9.
4. Search returns results for a misspelt instructor name.
5. A guardian account with two under-13 profiles, both enrolled in the same course, can submit two separate reviews for it — one per profile.
6. Hiding a review removes it from the public course detail page without deleting the underlying record.
7. A `suspended` or `taken_down` course does not appear in catalogue search or browse results, regardless of a learner's age band.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-CAT-DM-001](../data-model.md) |
| Age bands, reused from | [Age Band Badge](/3i/modules/identity-and-access/ui/components.md#age-band-badge) |
| Guardian-on-behalf reviews | [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md) |
| Guardian-on-behalf pattern origin | [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md) |
| Enrolment override (not this module's concern) | FR-ENR-04, `learning-delivery` (not yet built) |