---
project: RERAN
type: skill
scope: figma-build
status: draft
updated: 2026-09-18
description: >
  Self-contained rules for building or prompting any RERAN Group A (Regulatory Authority) screen in
  Figma. Read this BEFORE writing any figma prompt. The design system lives in the Figma file itself
  (RERAN-Web-App, vBSCiJLpyP8KLCTsmySVrS) — this doc is the durable, KB-side record of its tokens,
  components, and conventions, since design-prompt .md files are no longer kept in the KB (see
  Section 11). status-badges.md, role-screen-matrix.md, and validation-rules.md remain in the KB and
  are the content-authority for status words, nav/visibility, and business guards respectively.
authorities:
  - "RERAN/modules/regulatory-authority/ui/status-badges.md      (status vocabulary)"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md (role-scoped navigation)"
  - "RERAN/modules/regulatory-authority/ui/validation-rules.md   (guards)"
  - "Figma: RERAN-Web-App file, Component library page (0:1) — the actual design-system components"
  - "Figma: Regulatory body page (113:18070) — built Group A screens + Group A's own components"
tags: [reran, figma, skill, rules, design-system]
---

# RERAN — Figma build rules (skill)

The RERAN web app exists in Figma (file `vBSCiJLpyP8KLCTsmySVrS`, "RERAN-Web-App"): 550+ built screens
across Onboarding, Financial & Trust Institution (FTI/Group C), Real Estate Developer (RED/Group B),
Individual User, and the Regulatory Authority (Group A, page `113:18070`, in progress) — built from a
shared team library ("RERAN Design UI Kit & Design System") plus a file-local **Component library page
(`0:1`)**. New Group A screens must look like they were always part of it. This document captures
everything needed to write a build/fix prompt for any Group A screen — colours, components, and
patterns are inlined below so this file alone is sufficient.

## 0. Golden rules (non-negotiable)
1. **Bind to real tokens/components, never raw hex or hand-built substitutes.** Use the values in
   Section 1 and the components in Section 5.
2. **Use components; don't hand-build what exists.** Sidebar, top bar, buttons, badges, checkboxes,
   dropdowns, search, pagination, icons are all real components (Section 5). Compose only what has no
   component (tables, card sections, decision panels) — matching the patterns in Section 6.
3. **Adapt, don't reinvent.** Every new screen has a close sibling already built (Group A's own, or
   FTI/RED as a structural reference). Find it, mirror its structure/dimensions, change only content.
4. **Don't invent content.** Status words come from `status-badges.md`; nav items and visibility from
   `role-screen-matrix.md`; guards from `validation-rules.md`. Don't localise or paraphrase them.
5. **Verify against the Figma file, not memory.** Pull real dimensions/tokens/components before
   asserting them — this doc is a snapshot, the file is ground truth if they ever disagree.
6. **Normalise HTML-imported patterns.** The Individual User portal screens are HTML imports —
   replicate their clean structure, but convert off-palette hex, Liberation Mono, and sub-pixel values
   to the tokens in Section 1.
7. **All sample data is Nigerian.** Names, companies, addresses, phone numbers, currency (₦/NGN),
   institutions, and locations in every screen's sample content must be Nigerian — this is RERAN, the
   Nigerian real estate regulatory platform. Never default to generic/Western placeholder data (e.g.
   "Acme Corp", "John Smith", US-style addresses).

## 1. Colour tokens
| Token | Hex | Role |
| :-- | :-- | :-- |
| `N900` | `#091E42` | primary text, headings |
| `N400` | `#505F79` | secondary text, placeholders |
| `N40` | `#DFE2E6` | input/search borders, dividers |
| `N30` | `#EBEDF0` | card borders, chips |
| `N20` | `#F5F6F7` | field-group fill, **Workspace background** |
| `Color/blue-600` | `#006FE8` | primary / links / active nav |
| `Color/blue-700` | `#0057B5` | hover/pressed |
| `Blue/50` | `#EFF6FF` | Badge Color=Blue background |
| `Color/green-700` | `#258D3F` | success text |
| `Green/50` | `#F0FDF4` | Badge Color=Success background |
| `Color/orange-700` | `#B56A00` | warning text |
| `Yellow/50` | `#FEFCE8` | Badge Color=Warning background |
| `Red/600` | `#DC2626` | **the confirmed named red** — `Buttons/Button destructive`'s own default; use for Error/Rejected |
| `#D33128` | — | narrower use only: Input field's required-asterisk/error colour, not the button/status red |
| `Background/primary` | `#FFFFFF` | surfaces — sidebar, top bar, every card |
| `Brand/600` | `#7F56D9` | ⚠ kit default for `Buttons/Button` Hierarchy=Primary — **wrong for Group A, must be overridden** (see Section 5) |
| `Gradients/Blue 1` | 157° `#44009B → #2370CA` | portal-only primary button fill — **not used in Group A back-office** |

## 2. Type (Inter throughout; logo text is IBM Plex Sans Bold 14)
`Body Large/Medium` 18/27 (top-bar title) · `Body/Medium` 16/24 (card titles) · `Heading 5` Semibold
24/−0.96 (KPI value) · `Footnote/Medium` 14/20 (buttons, input labels) · `Caption/Medium` 13/20 (table
cells, nav, filter labels) · `Caption/Regular` 13/20 (secondary cells) · `Small/Regular` 12/18
(subtitles, field labels, KPI label, sublabels).

## 3. Screen shell — every screen, no exceptions
```
1440 × 927  FIXED — never taller, never auto/hug (scroll the Workspace internally if content overflows)
├─ RA-Sidebar (240, component instance — correct persona + active item)
└─ Main 1200
   ├─ Background+HorizontalBorder (1200×78, component instance — override Title/Subtitle/Role)
   └─ Workspace — inner 1136, 32px padding, FILL = N20 #F5F6F7
      (sidebar + top bar + every card inside stay white; N20 is only the workspace backdrop)
```
Sidebar header (78) aligns with the top bar (78) on the same baseline.

## 4. Screen archetypes
- **Queue / list** — Title+Actions → KPI card row → Filters (Search Bar + Filter Dropdowns) → table
  (header + rows) → Pagination. Reference: Work Queue (built, Regulatory body page).
- **Detail / decision** — breadcrumb → item header → two-column body (Card-pattern sections; nested
  double-card for grouped fields) → sticky Decision/Judgment Panel (Buttons/Button outcomes +
  Textarea input field reason) → Activity/Audit Trail. Reference: Application Review (built).
- **Dashboard** — KPI row + Card-pattern sections (e.g. Recent Activity as a table-in-card). Reference:
  Dashboard (built).
- **Editor/Config** — a list (table pattern) + a detail/editor panel using the nested double-card,
  form fields via `Input field`/`Textarea input field`/`Checkbox`. No canonical build yet — apply this
  archetype from the components in Section 5.

## 5. Components (real, in the Figma file — don't rebuild)
**From the Component library page (`0:1`):**
- **`Buttons/Button`** — Hierarchy: Primary/Secondary color/Secondary gray/Tertiary color/Tertiary
  gray/Link color/Link gray. Size sm/md/lg/xl. Icon False/Leading/Trailing/Dot/Only. State
  Default/Hover/Focused/Disabled. Group A: Primary = main action, Secondary gray = secondary, Link =
  inline. **⚠ Hierarchy=Primary's fill defaults to `Brand/600` purple — override to `Color/blue-600`
  on every instance placed in Group A (never edit the master component).**
- **`Buttons/Button destructive`** — same API; its Primary-hierarchy default (`Red/600 #DC2626`) is
  already correct — **no override needed**. Use for Reject/Dismiss/delete actions.
- **`Badge`** — Size sm/md/lg, Icon False/Dot/Avatar/Icon left/right/Only, **Color**
  Brand/Gray/Error/Warning/Success/Blue/Sky/Indigo/Purple/Pink/Rose/Orange/Slate. **Group A's verified
  usage is Size=sm, Icon=False** (no dot) — set Color per the status mapping in Section 8. This is the
  only status/label asset; never hand-build a pill.
- **`Input field`** — Type Default/Leading dropdown/Trailing dropdown/Leading text/Payment, Leading
  icon, Label, Hint text, Destructive, State. Use for form inputs (not table filters — see Group A's
  own Search Bar/Filter Dropdown below).
- **`Textarea input field`** — decision/judgment reasons, comments, notes.
- **`Verification code input field`** — MFA/OTP entry (every Group A role requires MFA).
- **`Checkbox`** — Checked/Indeterminate, Size sm/md, Type Checkbox/Radio, Text, State. Doc mark-seen/
  flag, table multi-select, role/permission toggle lists.
- **`Dropdown menu`** — the open-state menu list for select fields and row/kebab action menus.
- **`Avatar`** / **`Avatar label group`** — top-bar profile, user cells, audit actors.
- **Icon library** — categorized frames (General, Arrows, Users, Files, Communication, Alerts &
  feedback, Finance, Editor, Time, Maps, Weather, Security, …) on the same page. Pull all icons here.

**Group A's own components (built on the Regulatory body page, `113:18070`):**
- **`RA-Sidebar`** (component set, prop `Persona`) — 240 wide, full height. Currently has 2 variants
  (Compliance & Escrow Auditor, Licensing & Registration Officer); **3 more still need adding**
  (Dispute Adjudication Officer, Revenue & Finance Officer, System Super Administrator) before their
  screens can be built — same construction, only nav items + active state differ.
- **`Background+HorizontalBorder`** — the top bar, 1200×78. Real component; place an instance and
  override Title/Subtitle/Role — never hand-build a "TopBar" frame.
- **`KPI card`** — the canonical Group A stat card, used on every screen (queues, dashboards, editors).
  White, border `N30`, **radius 14**, **no icon, no accent border**, Foundation-tokenised, flex-1
  width. Vertical stack: Label (all-caps type style, `N400`) → Value (`Heading 5`, `foreground/primary`)
  → Sublabel (`Small/Regular`, `N400`). Props: Label/Value/Sublabel. Do NOT use the FTI `SummaryCard`
  or RED `MetricCard` (legacy, other modules only).
- **`Filter Dropdown`** — the canonical table filter trigger. 105×40 (auto-width, hug), white, border
  `N40`, radius 8, padding 12/8, gap 8: label (`Caption/Medium` `N900`, prop `Label`) + a **literal "▾"
  glyph** (not an icon component — intentional, built this way). Use for every filter chip.
- **`Search Bar`** — the canonical table search field. 180×40, white, border `N40`, radius 8, padding
  12/8: 16px search icon + placeholder. **Placeholder text is always exactly "Search..." — never vary
  it.** Sits first in the filters row, before the Filter Dropdown triggers.
- **`Pagination`** — table footer, ~1134×64, flex space-between. Left: page indicator (`Small/Regular`
  `N400`, "Showing 1–N of M"). Right: 32×32 rounded-8 buttons — prev/next (white, `N40` border,
  chevron), active page (`Color/blue-600`, white), inactive (`N400`, not off-palette `#6B7280`).

## 6. Composed patterns (no component exists — build these exactly)
- **Card (`Background+Border` pattern)** — white, border `N30`, radius 12, padding px-24 py-20. Title
  = `Body/Medium` `N900` (+ inline `Badge` if the card needs a status). Optional footer: `N30` top
  border + action links (16px icon + `Caption/Medium` 13 `blue-600`).
- **Nested double-card** — for any grouped read-only fields (confirmed on Application Review's
  "Application Summary"). Outer = the Card pattern above. Inside it, one or more **field-group**
  sub-cards: fill `N20` (not white), radius 8, **no border**, padding 16, gap 8 — group label (`Semi
  Bold` 13, `N900`) then a row of field pairs (flex-1 each, gap 24): label (`Small/Regular` 12, `N400`)
  over value (13, `N900`). Reuse this exact structure — don't invent a new grouping pattern.
- **Table row** — padding 12, gap 16, bottom border `N40`, cell text `Caption/Medium`/`Caption/Regular`
  13 (`N900`/`N400`). The reference/ID cell = `blue-600`, Semibold, **underlined** link. Status cells =
  real `Badge` (never a hand-built pill, never left showing the placeholder word "Label"). Table may
  sit bare in the Workspace or wrapped in a Card pattern (a titled table-in-card) — either is valid,
  pick one and use it consistently within a screen.
- **Breadcrumb** — row, gap 8, `PathSegment` groups (confirmed on the reference screen "S3 – 02
  Application Info"). Every segment except the last: label (Inter Medium 13, `blue-600`, a link) + a
  real 14px `Chevron Right` icon instance (never a typed character). Last segment (current page):
  label (Inter Regular 13, `N400`), no link styling, no chevron after it. **Only on drill-down
  screens** (reached by clicking into something, e.g. Application Review from Work Queue). **Top-level
  sidebar destinations never get one** (Dashboard, Work Queue, Audit Trail, and by the same rule: Fee
  Schedule Editor, Reconciliation, Case Queue, Admin Console) — not even a single current-page segment.
- **Empty state** — centred in a card: illustration (undraw-style, ~117×114) + one line of guidance
  (`Caption`/`Small`, centred).
- **Warning / info banner** — rounded-12, `#E4E7EC` border, tinted background, 40px icon chip + title
  (`Semi Bold` 13) + description (`Regular` 12). Use for decision-screen guards/alerts.

## 7. KPI card and status counts
- The canonical `KPI card` (Section 5) is used on **every** screen type — queues, Dashboard, editors —
  not just decision screens. Lay out flex-1 in one row (1136 ÷ N cards).
- Sidebar nav items have **no per-item count badges** (the reference sidebars — FI-Sidebar, RA-Sidebar
  — don't carry them). Don't add them.

## 8. Status Badge Color mappings
Set the `Badge` component's **Color** prop per status word — never hand-build a pill, never leave the
placeholder text "Label" showing.

**§1 — decision vocabulary** (Work Queue / Application Review — confirmed, in production use):
Under Review=`Blue` · Information Requested=`Warning` · Returned=`Warning` (or `Orange` to
differentiate) · Approved=`Success` · Rejected=`Error`.

**§2 / §3 — case lifecycle and config/platform vocabularies** (Case Queue/Workspace, Fee Schedule,
Reconciliation, Admin Console): `status-badges.md` explicitly defers colour choice to the Figma build
thread — propose a mapping using the same `Badge` Color palette when building those screens, and record
the final choice back into `status-badges.md` once confirmed on canvas.

## 9. Known drift — legacy patterns to standardise away from
The FTI/RED back-office screens predate Group A's tokenisation work and disagree with it in places;
don't copy these into Group A:
| Element | Legacy (FTI/RED) | Group A standard |
| :-- | :-- | :-- |
| Colours | raw hex | tokens (Section 1) |
| Primary button | flat `#006FE8` hand-built, or portal gradient `Button Primary` | `Buttons/Button` Primary, fill overridden to `blue-600` |
| Status badge | hand-built pills, or the portal `StatusChip` | real `Badge` component, Color prop |
| KPI card | FTI `SummaryCard` / RED `MetricCard` | Group A's own `KPI card` (no icon) |
| Card border | `#DFE2E6` / `#E4E7EC` mixed | `N30` consistently |

## 10. Verification discipline
- **Dimensions:** `get_metadata` on a node, read frame sizes.
- **Tokens/structure:** `get_variable_defs` on a screen/frame; `get_design_context` on a
  component/frame (also lists the named styles it uses).
- **The top-level Figma page list is unreliable** — it has returned only "Cover" while hiding whole
  pages. Navigate by node IDs where known; never conclude "nothing exists" from an empty listing.
- **After any KB push, verify** with `get_file_contents` on the path — don't trust the push response
  alone; also check the file/commit still exists before assuming a prior push is intact (see Section 11
  — the whole `figma-prompts/` folder was intentionally removed once already).

## 11. Where design content lives (KB vs Figma)
- **The Figma file itself is the source of truth for the design** — not markdown prompt files kept in
  the KB. `RERAN/modules/regulatory-authority/ui/figma-prompts/` was deliberately removed (2026-09-18)
  and should **not** be recreated; design/build prompts are generated ad hoc, in-session, from this
  document + a fresh read of the Figma file, and delivered to the person as `.md` files to run
  themselves — they are not committed back to the KB.
- **This document (`figma-build-rules.md`) is the one persistent KB record of the design system** and
  is kept up to date as new components/patterns are confirmed on canvas.
- **`status-badges.md`, `role-screen-matrix.md`, `validation-rules.md`** remain in the KB under
  `RERAN/modules/regulatory-authority/ui/` — they're content/business-rule authorities, not design
  files, and are unaffected by the figma-prompts removal.
- Workflow is **prompts-only**: the assistant does not edit the Figma canvas (`use_figma`); every
  deliverable is a `.md` prompt the person runs themselves.
- The Figma file lives on the **KINGSCOTT** team; edit access requires a Full/Editor seat there.
  `get_design_context`/`get_variable_defs` work with read access but can be rate-limited on a View seat.
- In this environment, **bash cannot reach `figma.com`** and inline base64 screenshots render blank —
  read design as **data** (`get_design_context`), not as images.
- **Never push to GitHub without explicit approval.** Commit messages: one-line summary + detail body.

## 12. Do / Don't
- ✅ Instance `RA-Sidebar` + `Background+HorizontalBorder` + `KPI card`; bind to the tokens in Section 1;
  mirror a built reference screen's structure; use `Buttons/Button` (+ destructive) and `Badge`; keep
  status words from `status-badges.md`; verify against the Figma file before asserting anything.
- ❌ Hand-build the shell, buttons, badges, or pagination; use raw hex; invent status words or nav
  items; add per-item sidebar count badges; mix KPI-card styles within Group A; leave a Primary button
  purple; leave a Badge showing "Label"; add a breadcrumb to a top-level sidebar screen; recreate the
  `figma-prompts/` folder in the KB; generate on a View seat; trust the page-list call; copy HTML-import
  artifacts verbatim (Liberation Mono, off-palette greys/greens, sub-pixel padding).
