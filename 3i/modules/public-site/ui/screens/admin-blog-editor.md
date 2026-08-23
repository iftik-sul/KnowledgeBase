---
project: 3i
module: public-site
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-PUB-UI-003
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
---

# Screen: Admin Blog Editor

Satisfies: FR-CMS-02, FR-CMS-03

---

## Purpose

Admin creates, edits, and schedules blog posts — the one open-ended content type this module owns.

## Access Gate

Admin only.

## Contents

A list of every `BlogPost` regardless of status, with a **New Post** action (the create path `Page` deliberately lacks). Per-post: title, body, cover image, category, scheduled publish date/time (see [validation-rules.md](../validation-rules.md#scheduled-post-timing)), and its own SEO title/meta description independent of the post's own title/body.

## Behaviour

**Draft → Scheduled → Published** is a real status progression here, unlike the fixed-page editor's immediate-save model — a blog post can sit as a draft indefinitely, be scheduled for a future date, or publish immediately, and the admin sees which state each post is in at a glance from the list.

## Role Variations

Admin only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).