---
project: 3i
module: public-site
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-PUB-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
---

# Screen: Admin Fixed-Page Editor

Satisfies: FR-CMS-01, FR-CMS-03

---

## Purpose

Admin edits the content of one of the eight fixed pages.

## Access Gate

Admin only — the platform's single Admin role, confirmed as the sole editor of this content.

## Contents

A list of the eight fixed pages (never more, never fewer — see [validation-rules.md](../validation-rules.md#fixed-slug-enforcement)), each opening a content editor plus SEO title/meta description fields. **No "add page" action exists anywhere on this screen.**

## Behaviour

Saving updates the live `Page` content immediately — no draft/publish distinction for fixed pages, unlike blog posts, since a fixed page (terms, privacy, safety) being briefly "in progress" while an admin edits it is an acceptable trade-off the baseline doesn't ask this module to avoid, whereas a genuinely unfinished blog post going live prematurely is a different kind of mistake.

**English-only content field** (FR-CMS-03) — no locale switcher on this editor, since there's nothing to switch between.

## Role Variations

Admin only.

## Contrast and RTL

Standard form contrast, 4.5:1 minimum (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).