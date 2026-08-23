---
project: 3i
module: public-site
type: overview
status: current
updated: 2026-08-23
id: 3I-PUB-OVW-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - module
  - overview
---

# Public Site

The module that owns everything a search engine crawls and everything a visitor reads before they ever create an account — the fixed page set, the blog, and the SEO/structured-data layer underneath both.

**Module status: complete.** README, data model, requirements, and the full UI stage are written.

## Scope

| Code | Area | FRs |
| :---- | :---- | ----: |
| CMS | Content management and public site | 7 |

No existing decisions touch CMS — this is one of two modules (alongside `catalogue`) scaffolded with a completely clean slate against the decision register. One new operating note, not a decision: **all content editing is done by the existing single Admin role** (FR-RBAC-02), confirmed 2026-08-23 — "super admin" in conversation refers to that same role, not a new tier. Sub-admin roles remain out of scope (§23 item 5), unchanged.

## A Fixed Set, Not a Page Builder

FR-CMS-01 is explicit: eight named pages — home, about, contact, FAQ, terms, privacy policy, refund policy, safety — and nothing else. Admin edits **content within** these eight; there is no "add new page" action anywhere in this module. If the institute later wants a ninth page, that's new scope against this requirement, not a feature this module was ever meant to support.

The **blog** (FR-CMS-02) is the one genuinely dynamic content type here — posts, categories, cover images, scheduling, its own SEO fields — and is not part of the fixed set; it can grow without limit.

## Pages Are Locale-Routed. Content Is Not.

Easy to conflate, worth stating precisely: every fixed page and blog post gets locale-prefixed routes, `hreflang` tags, and appears correctly in the sitemap across all five locales (FR-CMS-06) — but the **content itself is English-only and never machine-translated** (FR-CMS-03), consistent with how user-authored content works everywhere else in the platform (FR-LOC-03). The routing infrastructure exists in five languages; the words on the page don't change with it. This is a genuine SEO/reach decision (a Bengali-speaking visitor lands on a Bengali-URL'd page that still reads in English), not an oversight — the baseline states it this way deliberately.

## Documents

| Document | ID | Status |
| :---- | :---- | :---- |
| [data-model.md](data-model.md) | 3I-PUB-DM-001 | current |
| [requirements/cms-content-management-and-public-site.md](requirements/cms-content-management-and-public-site.md) | 3I-PUB-REQ-001 | current |
| [ui/README.md](ui/README.md) | 3I-PUB-UI-000 | current — 3 screens, matrix, components, validation rules |

## Rules Defined Elsewhere

This module does not restate these. It links.

| Rule | Lives in |
| :---- | :---- |
| User-generated content is never translated (the same principle FR-CMS-03 applies here) | FR-LOC-03 |
| Published course data this module's structured-data markup reads | `catalogue` |

## Delivery

Phase 7, Surface (§21.1) — CMS, blog, SEO, reports, exports, admin panel. This module is the CMS/blog/SEO third of that phase; `reporting` covers reports and exports.

## Forward References

None. It reads `catalogue`'s published Course data for FR-CMS-05's `Course` structured-data type — a real reference.

## Open Against This Module

None.

## Change Requests Owed to the Client

None. Nothing in this module amends or reverses the baseline.