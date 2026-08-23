---
project: 3i
module: public-site
type: requirements
status: current
updated: 2026-08-23
id: 3I-PUB-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - public-site
---

# Content Management and Public Site

Baseline §17. Seven requirements, none amended by decision.

---

## Fixed Pages and Blog

| ID | Requirement |
| :---- | :---- |
| **FR-CMS-01** | A **fixed page set** — home, about, contact, FAQ, terms, privacy policy, refund policy, safety. Not a general page builder |
| **FR-CMS-02** | A **blog/news module** with posts, categories, cover images, scheduling, and SEO fields |

See [data-model.md](../data-model.md#page) for why the fixed set has no create action at all, structurally, not just by convention. The blog is the module's only genuinely open-ended content type.

---

## Language

| ID | Requirement |
| :---- | :---- |
| **FR-CMS-03** | CMS content is **not** multi-language and is **not** machine-translated |

Same principle FR-LOC-03 applies to every other piece of user-authored content on the platform — course descriptions, chat, reviews — extended here to institute-authored CMS content too. See [README.md](../README.md#pages-are-locale-routed-content-is-not) for the distinction between locale-routed pages and untranslated content, which this requirement is entirely about.

---

## Rendering and SEO

| ID | Requirement |
| :---- | :---- |
| **FR-CMS-04** | Public pages are **server-rendered (SSR/ISR)** for SEO |
| **FR-CMS-05** | Structured data: `Course`, `Organization`, `FAQPage`, `BreadcrumbList`, `Article` |
| **FR-CMS-06** | `hreflang` across all five locales, canonical URLs, locale-prefixed routes, auto-generated sitemap and robots files, Open Graph and Twitter cards |
| **FR-CMS-07** | Authenticated areas are client-rendered and `noindex` |

FR-CMS-04 and FR-CMS-07 together draw the line this module lives on: everything public is server-rendered and crawlable; everything behind login is the opposite, deliberately. FR-CMS-05's structured data is generated at render time from live sources, never stored separately — see [data-model.md](../data-model.md#structured-data--generated-not-stored) for where each type's data actually comes from.

---

## Acceptance Criteria

1. A published course page returns full HTML content to a crawler without JavaScript execution.
2. The sitemap includes all published courses and blog posts, and excludes every authenticated route.
3. No Page record exists with a slug outside the eight fixed values — there is no code path that could create one.
4. A scheduled blog post does not appear on the public site before its scheduled time, and appears automatically once it passes, with no manual publish action required at that moment.
5. The refund policy page renders the Australian Consumer Law disclaimer (FR-REF-05) as supplied by the client's lawyer, not paraphrased.
6. Switching the site's locale changes page URLs and `hreflang` tags but not the underlying English content.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-PUB-DM-001](../data-model.md) |
| User-generated content is never translated (same principle) | FR-LOC-03 |
| Course structured-data source | `catalogue` |
| Refund policy legal copy | `commerce` (FR-REF-05), §22.2 item 3 client dependency |