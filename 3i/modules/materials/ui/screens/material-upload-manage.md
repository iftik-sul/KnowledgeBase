---
project: 3i
module: materials
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-MTL-UI-004
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - materials
  - instructor
---

# Screen: Material Upload / Manage

Satisfies: FR-MAT-01, FR-MAT-02, FR-MAT-03, FR-MAT-06, FR-MAT-09

---

## Purpose

An instructor uploads, reorders, edits, and deletes materials within a course they own.

## Access Gate

Instructor only, and only for courses they own (`Course.instructorId`, owned by `catalogue`, a real reference to `instructors`' `InstructorProfile`).

## Contents

[Material List Item](../components.md#material-list-item)s in management mode — drag handle for reordering, edit and delete per item. An **Add Material** action opens a type selector (video / document / audio / external link) leading into the appropriate upload flow.

**Video upload:** TUS resumable upload (FR-MAT-02) with a visible, accurate resume-from-last-chunk progress bar (see [validation-rules.md](../validation-rules.md#video-upload--resumable)), plus the required English caption file field — surfaced **before** the video upload begins, not after, per [validation-rules.md](../validation-rules.md#caption-requirement).

**Document/audio upload:** standard upload against the size limits in [validation-rules.md](../validation-rules.md#upload-size-limits).

**External link:** just a URL field and a title — no upload, no hosting.

## Behaviour

**No publish/approval step at the material level** (FR-MAT-09) — saving a material makes it live immediately within its course (subject to the course's own publication status in `catalogue`; a material added to a `draft` course is naturally not visible to anyone, but that's the course's state, not a per-material moderation gate).

**Reordering is drag-and-drop**, persisting the new order immediately — not a separate "save order" step, since a half-reordered list left unsaved is a worse failure mode than an eagerly-persisted one.

## Role Variations

Instructor only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring (FR-LOC-04): drag handles and reorder direction mirror.