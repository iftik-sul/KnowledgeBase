---
project: OstadLagbo
type: ui
status: current
updated: 2026-09-26
id: OL-UI-003
derived_from: /OstadLagbo/ui-overview.md
owner: Iftikher
---

# Design Foundations — Visual System & Slice 0 Screens

The visual layer the `ui-overview` deliberately left open ("colour, typography, spacing, iconography — produced later in Figma against a design system"). This document records the **decided** palette, type, logo, and the Slice 0 screen inventory, so the Flutter build (and any agent) implements one consistent look. It does **not** change scope or behaviour — those remain the module `ui` docs and the frozen `mvp-scope-v1.2`.

**Source of truth for pixels:** the Figma file below. This doc is the text mirror for review and handoff.

- **Figma file:** https://www.figma.com/design/yksNam3zlSoECaUzScjCFc/Untitled?node-id=1-2&t=FYHH6GAKbuginRmC-1 — the app screens live on **page 4**; ignore all other pages in the file.
- **Logo source:** the `athena` frame (editable vector) → component `Logo / Mark`.

## Brand palette (flat — no gradients)

Bound in Figma as the `Athena` variable collection; use the same tokens in the Flutter theme.

| Token | Hex | Role |
|---|---|---|
| `brand/green` | `#0E8A6E` | Primary. Pin, primary buttons, and **large/bold** text (headings, button labels). **Not for small/normal-weight text or links on white** — 4.3:1, fails WCAG AA at body size |
| `brand/green-dark` | `#0B7259` | Pressed/active state of primary |
| `brand/navy` | `#112841` | Figure, body text, **all links and small/normal-weight text on light backgrounds**, dark buttons |
| `brand/amber` | `#FBAE28` | Accent only (logo star, highlights). **Never text on white** — fails WCAG AA |
| `base/white` | `#FFFFFF` | Logo circle, card surfaces |
| `base/bg` | `#F7FAF8` | App background |
| `base/surface` | `#FFFFFF` | Cards, fields |
| `text/muted` | `#5B6B72` | Secondary text, hints, placeholders |
| `base/border` | `#E2E8E5` | Hairlines, field borders |
| `feedback/danger` | `#C8302A` | Errors, destructive (Log out) |
| `feedback/success` | `#1FA36B` | Success states |

Tints used for banners (backgrounds only): error `#FDECEA`, warning `#FEF6E6`.

## Typography

- **Latin (English UI):** Inter — Regular 400, Medium 500, Semi Bold 600, Bold 700.
- **Bangla:** Noto Sans Bengali — Regular, Medium, SemiBold, Bold. Renders conjuncts/vowel-signs correctly on the reference device (NFR-10).
- **Rule:** the client never mixes scripts in one run; pick the font by the string's script. Missing-translation fallback is English (NFR-11).
- **Digits:** phone numbers and OTP codes always Latin; counts/dates follow locale (NFR-11).
- Rough scale in use: screen title 22–26 / section 17–20 / body 14–15 / label 13 / caption 12.

## Logo

- **Mark:** reaching figure inside a location pin, amber star. Component `Logo / Mark`, sourced from the `athena` vector.
- **App icon:** fill the tile with `brand/green`, drop the white circle (the OS already draws a rounded square).
- **Open item:** the four-point star reads like the common "AI sparkle"; a 5-point star or simple spark is optional and would sidestep that. Export a clean **SVG** for the app/store assets before build.

## Accessibility (inherited from NFR-10)

Touch targets ≥ 44 dp (buttons/fields are 52–64 px); text respects OS font scaling; portrait-first, left-to-right in both languages. **Contrast (WCAG AA):** navy on white passes at every size; **green (`#0E8A6E`) on white is 4.3:1 — it passes only for large or bold text** (≥ 24 px regular / ≥ 18.66 px bold), so green is used for fills, the logo, headings, and bold button labels, while **links and small/normal-weight text use navy (`brand/navy`)**. Amber is accent-only, never text on white.

## Components (Figma library)

`Logo / Mark` · `Button / Primary` (green) · `Button / Secondary` (outline; recolour to danger for Log out) · `Field / Text` · `Field / Text-Error` · `OTP / Cell` · `Icon / Settings` · `Icon / Alert` · `Icon / WifiOff` · `Icon / Spinner`.

## Slice 0 screen inventory (English + Bangla each)

| # | Screen | Spec | Notes |
|---|---|---|---|
| 01 | Language choice | REG-14 | Bilingual by nature; lands on map after choice (temporary guest landing until MAP slice) |
| 02 | Role selection | REG-01 | Permanent-choice warning is unmissable |
| 03 | Registration | REG-02/03/04/13 | Phone, password (+rule), DOB (+18 note), optional email, consent |
| 04 | OTP verify | REG-02 | 6 cells, focused state, resend timer |
| 05 | Login | REG-05 | Forgot-password link; create-account footer |
| 06 | Forgot password | REG-06 | Step 1 (phone → reset code) |
| 07 | Settings | REG-07/Group G | Language, Account, Legal, Notifications; red Log out |
| 08 | Signed-in placeholder | — | Stands in for the map (next slice) |
| 09 | Server waking | NFR-13 | Render free tier sleeps ~50 s on first hit |
| 10 | Offline | NFR-03 | Retry; last view remains readable |
| 11 | Error states (reference) | ui-overview mapping | Inline field error, error banner, rate-limit/locked-out |

## Error-to-UI (built)

Follows the `ui-overview` mapping table. Implemented visuals: inline field error (danger border + message under the field), error banner (danger tint + alert icon), rate-limit/locked-out (amber tint). `validation_failed` → inline at field; `conflict` (phone in use) → inline on phone with a Log in link; `locked_out`/`rate_limited` → banner with countdown.

## Notes for the Flutter build

- One config file holds the API base URL: `https://athena-api-ujpl.onrender.com`.
- Put the palette and type into a single theme file; reference tokens, not raw hex, so re-theming is one place.
- **Bangla copy in Figma is placeholder for layout** — founder-authored strings replace the text layers (Bangla copy is founder-authored per project standards).
- Localise from bundled string tables; the client never translates API text (already-localised from the API).
