---
project: RERAN
module: regulatory-authority
type: reference
screen: _library-assets
status: draft
updated: 2026-09-15
derived_from:
  - "RERAN-Web-App / Individual user page (113:17666) — the tokenised, component-driven layer"
  - "Button Primary (374:17399) · Badge (249:20113) · Background+HorizontalBorder (252:11940)"
  - "Background+Border card (243:2973) · Input (995:38168) · Checkbox (521:30710)"
  - "Dropdown menu (516:28731) · Search (243:3249) · StatusChip (243:7383) · Warning banner (314:5765)"
tags: [regulatory-authority, figma-prompt, design-system, tokens, library-assets]
---

# RERAN library assets — tokens, components & patterns (single source of truth)

Extracted from the **Individual User portal**, the tokenised layer of the app. **Group A binds to these
— do not hand-build with raw hex.** app-shell.md and the screen prompts reference this file.

> **Two important caveats (read first):**
> 1. **The portal screens are HTML-imported** (semantic frame names `Heading 1/Paragraph/Margin/Link`,
>    Liberation Mono, sub-pixel values, off-palette greys). Follow the **components + Foundation tokens +
>    the clean structural patterns**, but **normalise the artifacts** (see "Normalisation" below).
> 2. **The kit blends two token systems.** Portal screens, buttons, badge, cards, inputs, search use
>    **`Foundation/*`** (below). Some form atoms (Checkbox, Dropdown) use an Untitled-UI-style **`Neutral/*`**
>    set (`Neutral/200 #E5E5E5`, `Neutral/300 #D4D4D4`, `Neutral/700 #404040`, `Base/White`, `Text sm/Medium`,
>    `Shadow/lg`). Prefer Foundation; accept the secondary tokens inside those atoms.

## Colour tokens (bind to the variable name)
| Token | Hex | Role |
| :-- | :-- | :-- |
| `Neutral/N900` | `#091E42` | primary text, headings |
| `Neutral/N400` | `#505F79` | secondary text, placeholders |
| `Neutral/N40` | `#DFE2E6` | input/search borders, dividers |
| `Neutral/N30` | `#EBEDF0` | **card borders**, chips (search/bell) |
| `Neutral/N20` | `#F5F6F7` | **input fill**, subtle fills, column bars |
| `Blue/blue-600` | `#006FE8` | primary / links / active nav |
| `Blue/blue-700` | `#0057B5` | primary hover/pressed |
| `Green/green-600` · `green-700` | `#2FB551` · `#258D3F` | success text/icon |
| `Orange/orange-600` · `orange-700` | `#E88800` · `#B56A00` | warning text/icon |
| `Green/50` · `Blue/50` · `Yellow/50` | `#F0FDF4` · `#EFF6FF` · `#FEFCE8` | soft status/badge backgrounds |
| error red (unnamed) | `#D33128` | required asterisk / error / candidate for `Rejected` |
| `Background/primary` | `#FFFFFF` | surfaces |
| `Gradients/Blue 1` | 157° `#44009B → #2370CA` | **primary button fill** |

> The Foundation palette has no *named* red; `#D33128` is used for required/error and is the best
> candidate for `Rejected` — confirm whether it should be promoted to a named token.

## Type styles
`Body Large/Medium` 18/27 · `Body/Medium` 16/24 · `Footnote/Medium` 14/20 · `Footnote/Regular` 14/20 ·
`Caption/Medium` 13/20 · `Caption/Regular` 13/20 · `Small/Regular` 12/18 · `Text xs/Medium` 12/18 ·
(secondary) `Text sm/Medium` 14/20. All **Inter**; logo IBM Plex Sans Bold 14.

## Spacing / effect / radii tokens
`Button/gap 8` · `Button/horizontal-padding 12` · `Button/vertical-padding 4` · `Button/corner-radius 8` ·
`Button/foreground #FFFFFF` · `Blur/20` (backdrop) · `Shadow/lg` (dropdown/popover elevation: dual drop
shadow). Radii: 8 (buttons, inputs, chips, nav items) · 10 (checkbox) · 12 (cards, banners) ·
16 (library badges) · full (avatars, dots, pills). Sizes: icon 16 · avatar 32 · chips 36 · input h-42 ·
sidebar 240 · shell rows 78.

## Components (use these; don't rebuild) — from the Component library page (0:1)
- **Buttons/Button** (variant set) — **Hierarchy:** Primary · Secondary color · Secondary gray · Tertiary
  color · Tertiary gray · Link color · Link gray. **Size:** sm/md/lg/xl. **Icon:** False/Leading/Trailing/
  Dot/Only. **State:** Default/Hover/Focused/Disabled. Group A: Primary = main action, Secondary gray =
  secondary, Link = inline. **`Buttons/Button destructive`** (same API) for Reject / delete.
  *(The gradient "Button Primary" is portal-only — do not use it in Group A back-office.)*
- **Badge** (variant set) — **Size** sm/md/lg · **Icon** False/Dot/Avatar/Icon left/Icon right/Only ·
  **Color** Brand/Gray/Error/Warning/Success/Blue/Sky/Indigo/Purple/Pink/Rose/Orange/Slate. The status/label
  asset — set its Color; never hand-build a pill (see Status badges below).
- **Input field** (variant set) — Type (Default/Leading dropdown/Trailing dropdown/Leading text/Payment),
  Leading icon, Label, Hint text, Help icon, Destructive, State (Placeholder/Filled/Focused/Disabled).
  Use for search (Leading icon=True), filter fields, and form inputs.
- **Textarea input field** — Label, Hint text, Destructive, State. Decision reason, comments/notes.
- **Verification code input field** — Size, Label, Digits 4/6. MFA / OTP entry (Group A requires MFA).
- **Checkbox** — Checked, Indeterminate, Size sm/md, Type Checkbox/Radio, Text, Supporting text, State.
  Doc mark-seen/flag, table multi-select, filter checklists.
- **Dropdown menu** — Icon, Checkbox, Shortcut, Header (Avatar group/Heading/False). Filter menus, select
  fields, row/kebab action menus. (`Dropdown` = the trigger control.)
- **Avatar** (variant set) + **Avatar label group** — Size xs–2xl, Placeholder, Text, Status icon
  (Online/Company), State. Top-bar profile, user cells (applicant/assignee), audit-trail actors.
- **Pagination** (`Pagination` component) — table footer, ~1134×64, flex space-between. Left: page indicator
  (`Small/Regular` `N400`; "Showing 1–N of M"). Right: 32×32 rounded-8 buttons — prev/next (white, `N40`
  border, chevron), active page (`Color/blue-600`, white), inactive (`N400`, not the off-palette `#6B7280`).
- **Navigation** — nav-item component, but its label variants are IU-specific (Applications/Complaints/
  Dashboard/…). Group A uses its own **`RA-Sidebar`**; reuse the nav-item *pattern*, not these labels.
- **Icon library** — lives on the Component library page (0:1), in categorized frames (General, Arrows,
  Users, Files, Communication, Alerts & feedback, Finance, Editor, Time, Maps, Weather, Security, …).
  Pull all icons from here.

## Composed patterns (built from the above; replicate these layouts)
- **KPI card — canonical (used on ALL Group A screens)** — white, border `N30 #EBEDF0`, **radius 14**,
  **no icon, no accent**, Foundation-tokenised. **flex-1** width (five share the 1136 row; ≈214 each),
  height 127. Vertical stack: label (all-caps type style, `N400`) → value (`Heading 5`, Semibold 24/−0.96,
  bound `foreground/primary`) → sublabel (`Small/Regular`, `N400`). Props: Label / Value / Sublabel.
  **Do NOT use the FTI `SummaryCard` or RED `MetricCard`** for Group A.
- **Card (`Background+Border`)** — white, border **`N30`**, rounded-12, content **px-24 py-20**. Title row =
  `Body/Medium` `N900` + inline `Badge`. **Metadata row** = `16px icon + Caption/Regular 13 N400` pairs (gap-24).
  **Footer** = `N30` top border + action **links** (`16px icon + Caption/Medium 13 blue-600`, gap-6).
- **Reference/ID chip** — monospace 12 on `#F0F2F5`, rounded-4 *(import artifact: normalise the mono font +
  grey to Foundation)*.
- **Warning / info banner** — rounded-12, `#E4E7EC` border, tinted (gradient) background, 40px icon chip +
  title (`Semi Bold 13`) + description (`Regular 12`). Use for decision-screen guards/alerts.
- **Empty state** — centred in a card: illustration (undraw-style, ~117×114) + one line of guidance
  (`Caption`/`Small`, centred). e.g. "Select an application on the left to see details."
- **List item / row** — icon/label pairs, `Caption` text, dividers via `HorizontalBorder` (`N30`/`N40`).

## Status badges — use the `Badge` component (Color prop)
Status pills = the **`Badge`** component (Size sm/md, Icon = **Dot**) with its **Color** set per status.
Do NOT hand-build pills or use the portal `StatusChip` (legacy).

| Status (status-badges.md §1) | Badge Color |
| :-- | :-- |
| Under Review | `Blue` |
| Information Requested | `Warning` |
| Returned | `Warning` (or `Orange` to differentiate) |
| Approved | `Success` |
| Rejected | `Error` |

> Using the Badge `Color` prop resolves the earlier "no red token" gap — `Error` is built in. The FTI/RED
> hand-built pills and the portal `StatusChip` are legacy; standardise every Group A table/screen on `Badge`.

## Normalisation (when copying a portal pattern into Group A)
- Colours → Foundation tokens (drop `#6B7280`, `#F0F2F5`, emerald `#ECFDF5`/`#007A55`).
- Fonts → Inter + the named styles (replace Liberation Mono with a chosen mono or `Caption`).
- Round sub-pixel values to whole px; drop `Margin`/`Link`/`Container` import wrappers.
- Status → the `Badge` component (not `StatusChip` or hand-built pills).
