---
project: 3i
module: public-site
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-PUB-UI-000
derived_from:
  - requirements/cms-content-management-and-public-site.md
tags:
  - ui
  - matrix
---

# Public Site — UI Index

Role × screen matrix. Every screen in this module, and who sees it.

---

## Roles

| Column | Who |
| :---- | :---- |
| **Public** | Any visitor, no session |
| **Admin** | The platform's single Admin role — all CMS editing happens here, confirmed 2026-08-23, no separate content-editor tier |

---

## Matrix

| Screen | Public | Admin |
| :---- | :---: | :---: |
| [Public page render](screens/public-page-render.md) | ● | |
| [Admin fixed-page editor](screens/admin-fixed-page-editor.md) | | ● |
| [Admin blog editor](screens/admin-blog-editor.md) | | ● |

Three screens. **The public blog listing/post pages are covered by [Public Page Render](screens/public-page-render.md)**, not a separate screen — a fixed page and a blog post share the same rendering, SEO, and structured-data machinery, differing only in which entity supplies the content.

---

## Shared

| Document | Covers |
| :---- | :---- |
| [components.md](components.md) | SEO Head, Structured Data Block |
| [validation-rules.md](validation-rules.md) | Fixed-slug enforcement, scheduled-post timing |

---

## Blocked

| Item | Blocks |
| :---- | :---- |
| Terms, privacy, and refund policy copy — §22.2 item 3, outstanding client dependency (from the institute's lawyer) | The actual text of three of the eight fixed pages. Does not block this module's own specification — the Page entity and rendering machinery are equally ready for placeholder or final legal copy |