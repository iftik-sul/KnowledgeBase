---
project: RERAN
module: regulatory-authority
type: reference
screen: _library-assets
status: draft
updated: 2026-09-14
derived_from:
  - "RERAN-Web-App / Individual user page (113:17666) — the tokenised, component-driven layer"
  - "RERAN-Web-App / Button Primary (374:17399)"
  - "RERAN-Web-App / Badge + _Badge base (249:20113)"
  - "RERAN-Web-App / Background+HorizontalBorder top bar (252:11940)"
tags: [regulatory-authority, figma-prompt, design-system, tokens, library-assets]
---

# RERAN library assets — tokens & components (single source of truth)

Extracted from the **Individual User portal**, which (unlike the FTI/RED back-office screens) is built
on the real design system: Foundation colour/type variables + proper components. **Group A binds to
these — do not hand-build with raw hex.** app-shell.md and the screen prompts reference this file.

## Colour tokens (bind to the variable name, not the hex)
| Token | Hex | Role |
| :-- | :-- | :-- |
| `Neutral/N900` | `#091E42` | primary text, headings |
| `Neutral/N400` | `#505F79` | secondary text |
| `Neutral/N40` | `#DFE2E6` | borders, dividers |
| `Neutral/N30` | `#EBEDF0` | chips (search, bell) |
| `Neutral/N20` | `#F5F6F7` | subtle fills (column bars, count badge) |
| `Blue/blue-600` | `#006FE8` | primary / links / active nav |
| `Blue/blue-700` | `#0057B5` | primary hover/pressed |
| `Green/green-600` · `green-700` | `#2FB551` · `#258D3F` | success text/icon |
| `Orange/orange-600` · `orange-700` | `#E88800` · `#B56A00` | warning text/icon |
| `Green/50` · `Blue/50` · `Yellow/50` | `#F0FDF4` · `#EFF6FF` · `#FEFCE8` | soft status/badge backgrounds |
| `Background/primary` | `#FFFFFF` | surfaces |
| `Gradients/Blue 1` | 157° `#44009B → #2370CA` | **primary button fill** |

> **Gap:** no **red** token surfaced (needed for `Rejected`). Confirm/add a `Red/50` + `red-700` pair.

## Type styles
`Body Large/Medium` Inter 18/27 · `Body/Medium` 16/24 · `Footnote/Medium` 14/20 · `Caption/Medium` 13/20 ·
`Caption/Regular` 13/20 · `Small/Regular` 12/18 · `Text xs/Medium` 12/18. Logo: IBM Plex Sans Bold 14 (+0.4).

## Spacing / effect / button tokens
`Button/gap 8` · `Button/horizontal-padding 12` · `Button/vertical-padding 4` · `Button/corner-radius 8` ·
`Button/foreground #FFFFFF` · `Blur/20` (backdrop blur). Radii: 8 (buttons, nav items, chips) · 12 (cards) ·
16 (badges) · full (avatar, dot). Sizes: icon 16 · avatar 32 · chips 36 · sidebar 240 · shell rows 78.

## Components (use these; don't rebuild)
- **Button Primary** — gradient fill (`Gradients/Blue 1`), `Footnote/Medium` label in `Button/foreground`
  white, tokenised padding/gap/radius, optional 16px leading icon, backdrop-blur. The only button component
  (back-office "secondary" buttons are hand-built flat `#006FE8` + `N40` border — a drift).
- **Badge** / **_Badge base** — pill with a leading **dot** + `Text xs/Medium` label, rounded-16, Foundation
  semantic pairs (Verified = `Green/50` bg + `green-700` dot/text). The official status/label asset.
- **Form** — `Checkbox` · `_Dropdown list item` · `Dropdown menu` · `Search`.
- **Structure** — `Navigation` (240-wide portal sidebar) · `Background+HorizontalBorder` (top bar) ·
  `Avatar` · `Menu Hamburger` · `Tray Arrow Down` (upload dropzone) · `Credit Card Rectangle`.
- **Icons** (one set, ~40): Chevron Right/Down · Check · Check Circle · Check Badge · X Mark Circle ·
  Warning Circle · check-circle-broken · Action Eye Visible · Folder · File/File 2/File Add/File Success ·
  calendar/Calendar 2 · marker-pin-02 · building-06/07 · User/user-01/03/user-plus-02 · coins-hand ·
  credit-card-01 · tag-01 · Clipboard List · Trash Bin · Pen · Mail · Phone Left · bank · download-01 ·
  shield-tick · home-03 · repeat-04 · copy-03 · archive · certificate-01 · Slider Vertical Circle ·
  Arrow Expand Left · Tray Arrow Up · Help · Icon/Close-Circle.

## Three badge treatments exist — standardise on the component
1. **Library `Badge`** (portal): dot + Inter Medium 12, rounded-16, Foundation tokens. ← use this.
2. FTI back-office pill (hand-built): Inter Medium 11, no dot, rounded-100, `#FFFAEB`/`#B54708`.
3. RED back-office pill (hand-built): Inter Semi Bold 11 UPPERCASE, no dot, rounded-100, `#ECFDF3`/`#12B76A`.

## Group A status badge → token mapping (proposed; use the library `Badge`)
| Status (status-badges.md §1) | Background | Dot / text | Note |
| :-- | :-- | :-- | :-- |
| Approved | `Green/50` | `green-700` | matches library "Verified" (confirmed pattern) |
| Under Review | `Blue/50` | `blue-700` | proposed |
| Information Requested | `Yellow/50` | `orange-700` | proposed |
| Returned | `Yellow/50` | `orange-700` | proposed — differentiate from Info Requested (label/icon) |
| Rejected | (red) | (red) | **blocked — no red token yet** |
