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

## Components (use these; don't rebuild)
- **Button Primary** — gradient (`Gradients/Blue 1`), `Footnote/Medium` white label, tokenised
  padding/gap/radius, optional 16px leading icon, backdrop-blur. Only button component; secondary =
  white + `N40` border (compose).
- **Badge / _Badge base** — pill + leading **dot** + `Text xs/Medium`, rounded-16, Foundation semantic
  pairs (Verified = `Green/50` + `green-700`). The official status/label asset.
- **Input** — label `Footnote/Medium` `N900` + required `*` `#D33128`; field bg `N20`, border `N40`,
  rounded-8, h-42, px-13 py-11, placeholder `Footnote/Regular` `N400`; label→field gap-6.
- **Checkbox** (component set) — props: `type` Radio/Checkbox · `checked` · `indeterminate` · `size` ·
  `state`. Base: white, border `Neutral/300 #D4D4D4`, rounded-10, 20px.
- **Dropdown menu / _Dropdown list item** — white, border `Neutral/200 #E5E5E5`, rounded-8, `Shadow/lg`,
  240 wide; items px-16 py-10, `Text sm/Medium` `Neutral/700 #404040`; 1px divider.
- **Search** — white, border `N40`, rounded-8, `Blur/20`, 16px magnifier + `Caption/Medium` `N400`
  placeholder. (Top-bar variant is *filled* `N30`, no border.)
- **Pagination** (`Pagination` component) — table footer, ~1134×64, flex space-between. Left: page indicator
  (`Small/Regular` `N400`; use "Showing 1–N of M" for data tables). Right: 32×32 rounded-8 buttons (gap-4) —
  prev/next (white, `N40` border, 14px chevron), active page (`blue-600` fill, white, `Caption/Medium`),
  inactive pages (white, `N400`). Bind: active fill → `Color/blue-600`, borders → `N40`, inactive text →
  `N400` (not the off-palette `#6B7280`).
- **Structure** — `Navigation` (240 portal sidebar) · `Background+HorizontalBorder` (top bar) · `Avatar` ·
  `Menu Hamburger` · `Tray Arrow Down` (upload dropzone) · `Credit Card Rectangle`.
- **Icons** (~40, one set): Chevron Right/Down · Check · Check Circle · Check Badge · X Mark Circle ·
  Warning Circle · check-circle-broken · Action Eye Visible · Folder · File/File 2/Add/Success ·
  calendar/Calendar 2 · marker-pin-02 · building-06/07 · User/user-01/03/user-plus-02 · coins-hand ·
  credit-card-01 · tag-01 · Clipboard List · Trash Bin · Pen · Mail · Phone Left · bank · download-01 ·
  shield-tick · home-03 · repeat-04 · copy-03 · archive · certificate-01 · Slider Vertical Circle ·
  Arrow Expand Left · Tray Arrow Up · Help · Icon/Close-Circle.

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

## Status treatments — FOUR exist; standardise on the library `Badge`
1. **Library `Badge`** (portal): dot + Inter Medium 12, rounded-16, Foundation pairs. ← **use this.**
2. `StatusChip`: dot + Inter **Semi Bold** 12, rounded-full, **off-palette emerald** (`#ECFDF5`/`#007A55`) — drift.
3. FTI back-office pill: Inter Medium 11, no dot, rounded-100, `#FFFAEB`/`#B54708` — drift.
4. RED back-office pill: Inter Semi Bold 11 UPPERCASE, no dot, rounded-100, `#ECFDF3`/`#12B76A` — drift.

## Group A status badge → token mapping (use the library `Badge`)
| Status (status-badges.md §1) | Background | Dot / text | Note |
| :-- | :-- | :-- | :-- |
| Approved | `Green/50` | `green-700` | matches library "Verified" (confirmed) |
| Under Review | `Blue/50` | `blue-700` | proposed |
| Information Requested | `Yellow/50` | `orange-700` | proposed |
| Returned | `Yellow/50` | `orange-700` | proposed — differentiate by label/icon |
| Rejected | red tint | `#D33128` | candidate red now identified; confirm/name the token |

## Normalisation (when copying a portal pattern into Group A)
- Colours → Foundation tokens (drop `#6B7280`, `#F0F2F5`, emerald `#ECFDF5`/`#007A55`).
- Fonts → Inter + the named styles (replace Liberation Mono with a chosen mono or `Caption`).
- Round sub-pixel values to whole px; drop `Margin`/`Link`/`Container` import wrappers.
- Status → the `Badge` component (not `StatusChip` or hand-built pills).
