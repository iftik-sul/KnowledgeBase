---
project: 3i
module: public-site
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-PUB-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - public
  - seo
---

# Screen: Public Page Render

Satisfies: FR-CMS-04, FR-CMS-05, FR-CMS-06, FR-CMS-07

---

## Purpose

The actual public-facing rendering of any fixed page or blog post — one template, shared machinery, different content sources.

## Access Gate

Public, always — no session of any kind gates any page this module renders. This is the deliberate opposite of every authenticated screen elsewhere in the platform (FR-CMS-07).

## Contents

The Page or BlogPost's own content, wrapped in [SEO Head](../components.md#seo-head) and [Structured Data Block](../components.md#structured-data-block). A blog listing page (all published posts, paginated) and individual post pages both use this same render path — the listing is simply a page whose "content" is a generated index rather than authored prose.

## Behaviour

**Server-rendered (SSR/ISR), not client-rendered** (FR-CMS-04) — a crawler receives full HTML with no JavaScript execution required, the opposite of how every authenticated screen in this platform works. This is the one screen in the whole project where that rendering strategy is a requirement rather than an implementation detail left to the developer.

**A scheduled blog post simply isn't reachable before its time** — not shown with a "coming soon" placeholder, genuinely absent from the render path and the sitemap alike, consistent with the absent-not-disabled convention used throughout this project for content that isn't yet available.

## Role Variations

None — identical for every visitor.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04) for page chrome and layout — navigation, alignment, icon direction — even though the content itself stays English per [README.md](/3i/modules/public-site/README.md#pages-are-locale-routed-content-is-not).