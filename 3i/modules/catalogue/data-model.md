---
project: 3i
module: catalogue
type: data-model
status: current
updated: 2026-08-23
id: 3I-CAT-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - catalogue
---

# Catalogue — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## Course

| Field | Notes |
| :---- | :---- |
| Title, summary, description | FR-CRS-01 |
| Learning outcomes | List of short statements, FR-CRS-01 |
| Thumbnail | Required before publish (FR-CRS-03), not before |
| Category | FK to **Category** (below) |
| Type | `Regular`, `Online Class`, or `Mixed` — §8.1. Determines whether the course can carry materials, batches, or both |
| Level | **Not specified in the baseline.** Defaulted to `Beginner` / `Intermediate` / `Advanced`, a reasonable placeholder pending client confirmation |
| Language | **Not specified whether limited to the platform's 5 UI locales.** Modelled as free text — flagged in [README.md](README.md#open-against-this-module), not decided |
| Minimum age | **Mandatory, no default** (FR-CRS-02). The field this entire module's safeguarding behaviour derives from |
| Maximum age | Optional |
| Status | `draft`, `pending_review`, `published`, `suspended`, `taken_down` — see Publish Gate below |
| Instructor | FK, forward-referenced — see Forward References |

**Age band** (FR-CRS-06: 5–8, 9–12, 13–15, 16–17, 18+, All ages) is **derived, not stored** — same principle as a learner profile's own age band, computed from `minimumAge`/`maximumAge` rather than kept as a separate field that could drift out of sync. A course card shows the band containing `minimumAge`; the course detail page shows the full numeric range, since a card showing only "13–15" for a course actually open to ages 13–17 would misrepresent it.

### Publish Gate

A course cannot be published without an age tag, at least one material or batch, and a thumbnail (FR-CRS-03). The age tag and thumbnail are fields on this record; **the material/batch check reads from two modules that don't exist yet** — see Forward References.

**Status transitions:**

| From | Action | To | Condition |
| :---- | :---- | :---- | :---- |
| — | Create | `draft` | Always allowed, no gate |
| `draft` | Publish | `pending_review` | Gate passes, `minimumAge` \< 13 (FR-CRS-04) |
| `draft` | Publish | `published` | Gate passes, `minimumAge` ≥ 13 |
| `pending_review` | Admin approves | `published` | Admin action |
| `pending_review` | Admin rejects | `draft` | Reason recorded, same pattern as instructor application rejection (FR-INST-02) |
| `published` | Admin suspends | `suspended` | FR-CRS-05, admin discretion |
| any | Admin takes down | `taken_down` | FR-CRS-05, admin discretion |

**Only `published` courses appear in the catalogue.** `pending_review`, `suspended`, and `taken_down` are all invisible to the public and to Members — the catalogue does not distinguish *why* a course is absent, since none of those reasons are the browsing learner's concern.

---

## Category

| Field | Notes |
| :---- | :---- |
| Name | |
| Active | Boolean. An inactive category is not offered on new courses but existing courses keep it, rather than being silently recategorised |

**Simple flat list, admin-managed** — confirmed direction. No nesting, no nested nesting, no per-category metadata beyond a name. If the institute's catalogue grows complex enough to need subcategories, that's new scope, not an extension of this entity.

---

## Review

| Field | Notes |
| :---- | :---- |
| Course | FK |
| Learner | FK to `identity-and-access` Learner — the profile the review is **about** |
| Submitted by | FK to `identity-and-access` Account — who **submitted** it. Identical to the learner's own account for a self-submitted review (13–17, adult); the guardian's account for an under-13 profile ([3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md)) |
| Rating | 1–5 integer, required (FR-CRS-11) |
| Text | Optional |
| Status | `visible` or `hidden` — admin may hide (FR-CRS-11) |
| Submitted at | |

**Unique on (Learner, Course).** One review per profile per course, not per account — a guardian with several enrolled children can submit one review per child for the same course, since each is a distinct learning experience even though one adult is doing the typing.

**Requires an active enrolment to submit** (FR-CRS-11: "only after enrolment") — this check reads from `learning-delivery`'s Enrolment record, which doesn't exist yet. Same forward-reference treatment as the publish gate; see below.

**Display attribution** for a guardian-submitted review follows the existing chat convention exactly — *"Fatima (guardian of Aisha)"* — per [3I-DEC-020](/3i/decisions/dec-020-guardian-on-behalf-chat-retained.md) and [3I-DEC-027](/3i/decisions/dec-027-guardian-reviews-on-behalf.md). A self-submitted review shows the learner's own display name.

---

## Forward References

Three places this module reads from a module that doesn't exist yet, flagged plainly per each rather than assumed or silently stubbed — the same treatment `commerce` gave its dependency on `identity-and-access` before that module existed:

| Reference | Reads from | Module status |
| :---- | :---- | :---- |
| `Course.instructorId` | `instructors` (INST) — the instructor record owning the course (FR-CRS-01, FR-INST-06) | Not yet built |
| Publish gate's "at least one material" check | `materials` (MAT) — whether the course has any Material record | Not yet built |
| Publish gate's "at least one batch" check | `learning-delivery` (BAT/ENR) — whether the course has any Batch record | Not yet built |
| `Review` submission's enrolment check | `learning-delivery` (ENR) — whether the submitting Learner has an Enrolment on this Course | Not yet built |

None of these block this module's own specification. Each is a foreign key or a query this module will make once the referenced module exists; the fields and check points are documented here now so the dependency is visible rather than discovered later.

---

## Referenced By

| Module | Reads |
| :---- | :---- |
| `materials` | Course — materials are ordered within a course (FR-MAT-01) |
| `learning-delivery` | Course — batches and enrolments both reference a course |
| `assessment` | Course — question banks and exams are scoped to a course |
| `certification` | Course — certificate title is snapshotted from the course title at issue |
| `reporting` | Course, Review — course performance and rating reports (FR-REP-01) |

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Learner | `identity-and-access` | Age, for catalogue filtering (FR-CRS-10); review authorship |
| Account | `identity-and-access` | Review submitter identity |