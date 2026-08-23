---
project: 3i
module: catalogue
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-CAT-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - catalogue
  - instructor
---

# Screen: Course Create / Edit

Satisfies: FR-CRS-01, FR-CRS-02, FR-CRS-03

---

## Purpose

An instructor creates a new course or edits an existing one, and publishes it once the [Publish Gate](../validation-rules.md#publish-gate) is satisfied.

## Access Gate

Instructor only, and only for courses they own (`Course.instructorId`, forward-referenced — see [data-model.md](../data-model.md#forward-references)). An instructor cannot see or edit another instructor's course, consistent with FR-INST-06's one-instructor-per-course ownership model.

## Fields

Title, summary, description, learning outcomes, thumbnail upload, category (required select), type (Regular / Online Class / Mixed), level, language, minimum age (**no default — see [validation-rules.md](../validation-rules.md#age-field--no-default)**), maximum age (optional).

**No instructor field** — ownership is implicit from the authenticated instructor creating the course, never a selectable field even for admin (an admin reassigning course ownership, if ever needed, is a distinct future capability, not this form).

## Behaviour

**Save** persists a `draft` at any time, with only the age-field validation enforced (FR-CRS-02) — every other field may be incomplete in a draft.

**Publish** is disabled until the full [Publish Gate](../validation-rules.md#publish-gate) passes: age tag, thumbnail, and at least one material or batch. On a `draft` with `minimumAge` \< 13, Publish moves the course to `pending_review` (FR-CRS-04) rather than `published` directly — the instructor sees this distinction stated plainly ("submitted for review" vs. "published"), not just a generic success message.

**Materials and batches are not managed from this screen** — they belong to `materials` and `learning-delivery` respectively (neither built yet). This screen only checks whether at least one exists, for the publish gate; the instructor navigates elsewhere to actually add them.

## Role Variations

Instructor only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring (FR-LOC-04): field order, label alignment.