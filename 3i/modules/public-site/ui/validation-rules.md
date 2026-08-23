---
project: 3i
module: public-site
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-PUB-UI-VAL
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - validation
---

# Public Site — Validation Rules

Field-level validation shared across two or more public-site screens.

---

## Fixed-Slug Enforcement

On [Admin Fixed-Page Editor](screens/admin-fixed-page-editor.md): the eight `Page` slugs are the only values this screen can ever address — there is no field anywhere in this screen's form that accepts a new slug (FR-CMS-01). This is enforced by the screen simply not having a create action, not by validating a create attempt and rejecting it.

## Scheduled-Post Timing

On [Admin Blog Editor](screens/admin-blog-editor.md): a `scheduledPublishAt` in the past is treated as "publish immediately," not rejected — an admin backdating a schedule by mistake shouldn't produce an error on save, since the more useful behaviour is simply publishing the post rather than blocking the save entirely.