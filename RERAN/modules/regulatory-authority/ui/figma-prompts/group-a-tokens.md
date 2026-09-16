---
project: RERAN
module: regulatory-authority
type: reference
screen: _group-a-tokens
status: ready
updated: 2026-09-15
note: >
  Curated Group A palette — only the colours, type styles and buttons the module uses. Accents bind to
  the RERAN Design UI Kit `Color/*` variables. Neutrals, status backgrounds and the Rejected red have no
  matching kit token, so they are a small LOCAL variable set (`RA/*`) — see ra-variables.generate.md.
  Bind to the named variable everywhere; the hex is shown for reference only.
tags: [regulatory-authority, design-system, tokens, group-a]
---

# Group A — curated tokens (colours · type · buttons)

## Colours

### Neutrals — LOCAL variables (`RA/*`)
| Role | Variable | Value |
| :-- | :-- | :-- |
| Text — primary | `RA/text/primary` | `#091E42` |
| Text — secondary | `RA/text/secondary` | `#505F79` |
| Border | `RA/border` | `#DFE2E6` |
| Card border / divider | `RA/divider` | `#EBEDF0` |
| Subtle fill | `RA/fill/subtle` | `#F5F6F7` |
| Surface | kit `Background/primary` | `#FFFFFF` |

### Accents — kit variables (bind to these)
| Role | Kit variable | Value |
| :-- | :-- | :-- |
| Primary / link / active | `Color/blue-600` | `#006FE8` |
| Primary hover / pressed | `Color/blue-700` | `#0057B5` |
| Soft blue (icon chip) | `Color/blue-50` | `#E6F2FF` |

### Status pills — background (LOCAL) / text (kit, except Rejected)
| Status | Background variable | Text variable |
| :-- | :-- | :-- |
| Under Review | `RA/status/under-review-bg` `#EFF6FF` | `Color/blue-700` `#0057B5` |
| Information Requested | `RA/status/attention-bg` `#FEFCE8` | `Color/orange-700` `#B56A00` |
| Returned | `RA/status/attention-bg` `#FEFCE8` | `Color/orange-700` `#B56A00` |
| Approved | `RA/status/approved-bg` `#F0FDF4` | `Color/green-700` `#258D3F` |
| Rejected | `RA/status/rejected-bg` `#FDECEC` | `RA/status/rejected-fg` `#D33128` |

> **Local set = 10 variables** (5 neutrals + 4 status backgrounds + Rejected text). Everything else binds
> to the kit. Create the 10 via `ra-variables.generate.md`.

## Typography (Inter; kit text styles)
| Style | Font | Use |
| :-- | :-- | :-- |
| `Heading 5` | Semi Bold 24 (−0.96) | KPI value |
| `Body Large/Medium` | Medium 18/27 | top-bar title, section titles |
| `Body/Medium` | Medium 16/24 | large body |
| `Footnote/Medium` | Medium 14/20 | buttons, input labels |
| `Footnote/Regular` | Regular 14/20 | input text |
| `Text sm/Medium` | Medium 14/20 | dropdown items |
| `Caption/Medium` | Medium 13/20 | nav, profile name, search, table cells |
| `Caption/Regular` | Regular 13/20 | secondary cells |
| `Small/Regular` | Regular 12/18 | subtitle, sublabel, role, KPI label |
| (status / badge) | 11 (no named style) | status pill / count |
| logo | IBM Plex Sans Bold 14 | sidebar logo |

## Buttons
- **Primary** — `Button Primary` component: gradient `Gradients/Blue 1` (157° `#44009B → #2370CA`),
  white label (`Button/foreground`), radius 8, gap 8, padding 12/4, icon 16.
- **Secondary** — composed (no component): white fill, border `#E4E7EC`, text `RA/text/primary`, same radius/padding.
- Kit `Button/*` spacing: corner-radius 8 · gap 8 · h-padding 12 · v-padding 4 · icon-size 16 · size 28.

## Radii & spacing (kit)
- Radii: button/chip 8 · KPI card 14 · container 10.
- Spacing (`Content/*`): gap-small 0 · gap-medium 4 · gap-large 12 · gap-extra-large 20.
- Screen: width 1440 · content-gap 32 · content-padding 20.
