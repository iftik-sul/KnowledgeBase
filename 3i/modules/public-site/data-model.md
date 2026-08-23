---
project: 3i
module: public-site
type: data-model
status: current
updated: 2026-08-23
id: 3I-PUB-DM-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - data-model
  - public-site
---

# Public Site — Data Model

Entities owned by this module. Other modules reference these; they do not restate them.

---

## Page

| Field | Notes |
| :---- | :---- |
| Slug | One of exactly eight fixed values — `home`, `about`, `contact`, `faq`, `terms`, `privacy`, `refund`, `safety` (FR-CMS-01). **Not a free-text field** — there is no way to create a Page with any other slug, since that's what "fixed page set, not a page builder" means structurally, not just as a UI convention |
| Content | Rich text/structured body, English only (FR-CMS-03) |
| SEO title, meta description | Per page |
| Updated at, updated by | |

**Eight rows, seeded at launch, never more, never fewer.** This table has no create action anywhere in this module — only edit.

**Some of this content is legally supplied, not authored here.** Terms, privacy, and refund policy pages are drafted by the client's lawyer (§22.2 item 3, an outstanding client dependency already tracked in `open-questions.md`) — this module stores and renders whatever text arrives, it doesn't originate legal copy. The refund policy page specifically must carry the Australian Consumer Law disclaimer verbatim (FR-REF-05, already noted in `commerce`) — worth restating here since this is the module that actually renders that page.

---

## BlogPost

| Field | Notes |
| :---- | :---- |
| Title, slug | Slug auto-generated from title, editable |
| Body | Rich text, English only (FR-CMS-03) |
| Cover image | |
| Category | Free text or simple tag — not the same `Category` entity `catalogue` owns for courses; blog categories and course categories are unrelated taxonomies that happen to share a name |
| Scheduled publish at | Nullable — a post with a future date doesn't appear until it passes (FR-CMS-02's "scheduling") |
| SEO title, meta description | Per post, independent of the post's own title/body |
| Status | `draft`, `scheduled`, `published` |

**Unlike Page, this table has a real create action** — the blog is the one part of this module that grows without a fixed ceiling.

---

## Structured Data — Generated, Not Stored

FR-CMS-05's five schema.org types (`Course`, `Organization`, `FAQPage`, `BreadcrumbList`, `Article`) are **rendered at request time from live data**, never a separately stored field on Page or BlogPost that could drift out of sync:

| Type | Source |
| :---- | :---- |
| `Course` | `catalogue`'s published Course records — real reference, already built |
| `Organization` | Static institute details, configured once, not per-page |
| `FAQPage` | The `faq` Page's own content, structured into Q\&A pairs at render time |
| `BreadcrumbList` | Computed from the current page's position in the site's own navigation, not stored |
| `Article` | Each `BlogPost`, at render time |

Same principle as every other derived value elsewhere in this project (age bands, course-level progress, certificate eligibility) — compute from the source of truth at read time rather than duplicate it into a field that could go stale.

---

## Forward References

None. `catalogue` (for `Course` structured data) is already built.

---

## Referenced By

No other module reads from this one — `public-site` is a leaf: it reads `catalogue`'s Course data outward, but nothing in the platform's authenticated, learning-flow side reads Page or BlogPost content back. This is by design; public marketing content and the learning platform are deliberately separate concerns (FR-CMS-07: authenticated areas are `noindex` and client-rendered, distinct from this module's server-rendered public surface).

## Referenced

| Entity | Owned by | Read here |
| :---- | :---- | :---- |
| Course | `catalogue` | `Course` structured-data type on public course pages |