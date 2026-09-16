---
project: RERAN
type: skill
scope: figma-build
status: draft
updated: 2026-09-15
description: >
  Rules for building or prompting any RERAN screen in Figma. Read this BEFORE creating
  screens, writing figma-prompts, or generating with an agent, so output stays consistent
  with the existing app and design system.
authorities:
  - "RERAN/modules/<module>/ui/figma-prompts/library-assets.md   (tokens + components — source of truth)"
  - "RERAN/modules/<module>/ui/figma-prompts/app-shell.md         (sidebar + top bar)"
  - "RERAN/modules/<module>/ui/status-badges.md                   (status vocabulary)"
  - "RERAN/modules/<module>/ui/role-screen-matrix.md              (role-scoped navigation)"
  - "RERAN/modules/<module>/ui/validation-rules.md                (guards)"
tags: [reran, figma, skill, rules, design-system]
---

# RERAN — Figma build rules (skill)

The RERAN web app already exists in Figma (file `vBSCiJLpyP8KLCTsmySVrS`, "RERAN-Web-App"): 550+
built screens across Onboarding, Financial & Trust Institution (FTI/Group C), Real Estate Developer
(RED/Group B), and Individual User, built from a shared team library ("RERAN Design UI Kit & Design
System"). New screens must look like they were always part of it. These rules capture how.

## 0. Golden rules (non-negotiable)
1. **Bind to tokens, never raw hex.** Use the Foundation variables in `library-assets.md`
   (`Neutral/N900`, `Blue/blue-600`, `Green/green-700`, type styles, button tokens…). Raw hex is a
   last resort and must be flagged.
2. **Use components; don't hand-build what exists.** Sidebar, top bar, buttons, badges, checkboxes,
   dropdowns, search, icons are all components. Compose only what has no component (tables, KPI cards,
   detail panels) — and compose it to match the reference frames exactly.
3. **Adapt, don't reinvent.** Every new screen has a close sibling already built. Find it, mirror its
   structure/dimensions, change only the content.
4. **Don't invent content.** Status words come from `status-badges.md`; nav items and visibility from
   `role-screen-matrix.md`; guards from `validation-rules.md`. Don't localise or paraphrase them.
5. **Verify against the file, not memory.** Pull real dimensions/tokens before asserting them.
6. **Normalise HTML-imported patterns.** The portal screens are HTML imports — replicate their
   structure, but convert off-palette hex, Liberation Mono, and sub-pixel values to Foundation tokens.

## 1. The design system (see library-assets.md for the full catalogue)
- **Colour:** Foundation Neutral (`N900 #091E42`, `N400 #505F79`, `N40 #DFE2E6`, `N30 #EBEDF0`,
  `N20 #F5F6F7`), Blue (`blue-600 #006FE8`, `blue-700 #0057B5`), Green (`green-600/700`), Orange
  (`orange-600/700`), soft tints (`Green/50`, `Blue/50`, `Yellow/50`), `Background/primary #FFFFFF`,
  and `Gradients/Blue 1` (the primary-button fill). No *named* red token; `#D33128` is used for
  error/required and is the candidate for `Rejected` — confirm/name it.
- **Type:** `Body Large/Medium` 18/27 · `Body/Medium` 16/24 · `Footnote/Medium` 14/20 ·
  `Caption/Medium` 13/20 · `Caption/Regular` 13/20 · `Small/Regular` 12/18 · `Text xs/Medium` 12/18.
  Logo text is IBM Plex Sans Bold 14. All UI text is **Inter**.
- **Radii:** 8 (buttons, nav items, chips) · 12 (cards) · 16 (library badges) · full (avatars, dots).
- **Buttons:** `Button Primary` = **gradient** (`Gradients/Blue 1`), white label, 16px optional icon.
  There is no secondary-button component — secondary = white + `N40` border (compose it).
- **Badges:** `Badge` / `_Badge base` = pill + leading **dot** + `Text xs/Medium`, Foundation semantic
  pairs. This is the official status/label asset — prefer it over hand-built pills.

## 2. The app shell (see app-shell.md)
- **Sidebar = one component per module**, 240px, all built the same way (`FI-Sidebar`, `RED-Sidebar`,
  the portal's `Navigation`). For a new module, **duplicate `FI-Sidebar` and swap the nav items** —
  keep the RERA logo header, the Sign Out footer, and the active-item blue (`#006FE8`) pill.
  Nav is **role-scoped** where the module has real RBAC (Group A); otherwise it's the full set.
- **Top bar = the `Background+HorizontalBorder` component** (1200×78). Place it and override
  title/subtitle/profile. It has a global search, a notification bell, and a profile block; it has
  **no back button and no status slot** — put those in the workspace (breadcrumb row + item header).

## 3. Layout grid (back-office desktop)
```
1440 × 927  screen
├─ Sidebar 240 (full height)
└─ MainContent 1200
   ├─ Top bar 1200 × 78   (component)
   └─ Workspace           inner width 1136, 32px side padding
```
Sidebar header (78) aligns with the top bar (78) on the same baseline.

## 4. Screen archetypes
- **Queue / list** — reference: FTI **Escrow Request Queue** (`1247:36042`). Regions: Title+Actions →
  KPI card grid → Filters (search + dropdowns) → table (header + rows ~45 tall) → pagination. RED
  wraps its table in a titled card (`ProjectsTableCard`) with a grey column-label bar — either is valid.
- **Detail / decision** — reference: FTI **Application Review** (`1179:35755`) + **Application Details**
  (`1219:35155`). Card-based body (`Card → CardHeader → DetailsGrid → GridRow`), a documents table, and
  a decision/validation area. Reuse the `ValidationSummaryCard` pattern for check panels.

## 5. Component & pattern conventions
- **KPI cards** — two house styles exist: FTI `SummaryCard` (274×127, icon chip + 4px left accent,
  4/row) and RED `MetricCard` (218×108, no icon, 5/row). Pick per KPI count and **state which** in the
  prompt; don't mix silently.
- **Tables** — rows: p-12/14, gap-12/16, bottom border `N40`, cells Inter 13 (`N900`/`N400`), the
  reference/ID cell is a `blue-600` link, the row action ("View") is a `blue-600` link, right-aligned.
- **Status pills** — the back-office hand-builds pills (rounded-100, Inter 11); the library `Badge`
  is rounded-16 with a dot. **Prefer the library `Badge`** with the Foundation mapping in
  `library-assets.md`. Whatever you choose, apply it to every table in the module identically.
- **Two token systems:** portal/buttons/badge/cards/inputs use `Foundation/*`; some form atoms
  (Checkbox, Dropdown) use an Untitled-UI `Neutral/*` set (`Neutral/200/300/700`, `Text sm/Medium`,
  `Shadow/lg`). Prefer Foundation; accept the secondary tokens inside those atoms.
- **Composed patterns** (Card, Input, Dropdown, Search, Banner, Empty state, list rows) are documented
  in `library-assets.md` — replicate those layouts, don't invent new ones.

## 6. Known drift — standardise, don't copy blindly
The back-office (FTI/RED) screens predate full tokenisation and disagree with the portal in places:
| Element | Back-office | Portal / library | Use |
| :-- | :-- | :-- | :-- |
| Colours | raw hex | Foundation tokens | **tokens** |
| Primary button | flat `#006FE8` | gradient `Button Primary` | **gradient component** |
| Status badge | 3 off-standard variants (2 pills + `StatusChip`) | `Badge` dot-pill | **library `Badge`** |
| Card border | `#DFE2E6` / `#E4E7EC` mixed | — | pick one (`N40`) and keep it |

## 7. Writing figma-prompts
- One file per screen under `…/ui/figma-prompts/`, plus shared `app-shell.md` and `library-assets.md`.
- Frontmatter: `project, module, type: figma-prompt, screen, status, updated, derived_from[], reference_frame, tags`.
- **Reference real names + composed frames with dimensions.** Name the components (`Button Primary`,
  `Badge`, `RA-Sidebar`, `Background+HorizontalBorder`); for composed regions give the frame name,
  size, and token bindings from the reference.
- Point every prompt at `app-shell.md` (shell) and `library-assets.md` (tokens/components) instead of
  restating them — keep it DRY.
- Flag anything genuinely new (no reference) explicitly so the builder knows it's new.

## 8. Verification discipline
- **Dimensions:** `get_metadata` on a node, read frame sizes.
- **Tokens:** `get_variable_defs` on a screen/frame; **structure + tokens:** `get_design_context` on a
  component/frame (it also lists the named styles it uses).
- **The top-level page list is unreliable** — it has returned only "Cover" while hiding whole pages.
  Navigate by node IDs; never conclude "nothing exists" from an empty listing.
- **After any push, verify** with `get_file_contents` on the path — don't trust the push response alone.

## 9. Tooling & access constraints
- Figma is reached via the MCP as **Technovicinity** (`work@technovicinity.com`): **Full seat** on the
  Technovicinity team, **View seat** on the KINGSCOTT team (where RERAN-Web-App lives).
- **A View seat can read (with rate limits) but cannot generate.** `use_figma` (writing to canvas)
  needs an **edit-capable seat on the KINGSCOTT team**. `get_design_context` / `get_variable_defs` are
  intermittently gated on a View seat.
- In this environment, **bash cannot reach `figma.com`** and inline base64 screenshots render blank —
  so read design as **data** (`get_design_context`), not as images.
- **Never push to GitHub without explicit approval.** Commit messages: one-line summary + detail body.

## 10. Do / Don't
- ✅ Duplicate `FI-Sidebar`; place `Background+HorizontalBorder`; bind to Foundation tokens; mirror a
  reference frame; use `Button Primary` + `Badge`; keep status words from `status-badges.md`.
- ❌ Hand-build the shell; use raw hex; invent status words or nav items; add per-item count badges to
  the sidebar (the built sidebars have none); mix KPI-card or badge styles within a module; generate on
  a View seat; trust the page-list call; copy HTML-import artifacts verbatim (Liberation Mono,
  off-palette greys/greens, sub-pixel padding).
