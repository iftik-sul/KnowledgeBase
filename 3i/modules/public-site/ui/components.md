---
project: 3i
module: public-site
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-PUB-UI-COMP
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - components
---

# Public Site — Shared Components

Documented once here. Screens link to this file rather than restating.

---

## SEO Head

Used on: [Public Page Render](screens/public-page-render.md).

Renders every FR-CMS-06 element for the current page: canonical URL, `hreflang` tags for all five locales, Open Graph and Twitter card meta, and the sitemap entry this page contributes. One implementation, reused for every fixed page and every blog post — not rebuilt per page type.

## Structured Data Block

Used on: [Public Page Render](screens/public-page-render.md).

Emits the correct schema.org JSON-LD block for the current page's type — `Course` on a course detail page (reading `catalogue`'s live data), `FAQPage` on the FAQ page, `Article` on a blog post, `BreadcrumbList` computed from the current navigation position, `Organization` on every page as static, shared data. See [data-model.md](/3i/modules/public-site/data-model.md#structured-data--generated-not-stored) for why none of this is stored.