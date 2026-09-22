---
project: RERAN
type: skill
scope: figma-build
status: superseded
updated: 2026-09-21
description: >
  SUPERSEDED. The RA-only Figma build rules have been promoted to the platform-wide standard at
  RERAN/reran-design-standard.md. Read that instead — it holds the universal tokens/components/
  status/geometry (Section A), the back-office-vs-portal split (Section B), and RA specifics
  (Section C1). This stub remains only so existing references to this path resolve.
tags: [reran, figma, skill, superseded]
---

# RERAN — Figma build rules → MOVED

**This document has moved and been promoted platform-wide.**

The rules that used to live here (RA-only) are now the **RERAN Platform Design Standard**:

➡ **`RERAN/reran-design-standard.md`**

That doc covers every module, not just the Regulatory Authority:

- **Section A (universal)** — colour tokens, typography, geometry (1440×927), the shared components
  (stat card, top bar, sidebar, Badge, buttons, inputs, pagination), composed patterns, the
  status-by-treatment → Badge-Color rule, and the legacy **hex→token migration map**.
- **Section B (surface-specific)** — back-office (RA: `N20` workspace, drill-down breadcrumbs) vs
  applicant portal (FTI/RED/IU: don't force back-office shell rules onto flow screens).
- **Section C1 (Regulatory Authority)** — the RA-specific detail that used to be this whole file:
  `RA-Sidebar` and its 8 personas, RA's status vocabularies (`status-badges.md` §1–§5), nav/guards
  (`role-screen-matrix.md`, `validation-rules.md`), and that RA's design lives in Figma (the
  `figma-prompts/` folder was deliberately removed, not to be recreated).

**For anything Figma-build related, read `reran-design-standard.md`.** This stub is kept only so old
links/references to `figma-build-rules.md` don't break.
