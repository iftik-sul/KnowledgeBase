---
project: 3i
type: standard
status: current
updated: 2026-08-24
tags:
  - design-system
  - ui
  - cross-cutting
---

# Design System

**This is the authoritative source for visual tokens — color, type, spacing, radius, elevation — across every screen in every module.** Module `ui/` documents link here rather than restating values. See [documentation-standards.md](/documentation-standards.md) on why a restated rule goes stale silently.

Derived from a Figma audit of the initial design exploration (5 main screens: landing, course catalogue, course detail, lesson player). The visual language — palette, type pairing, card and lesson-player layout logic — is retained. Specific token values below were corrected against NFR-12 (4.5:1 contrast, hard requirement) and project needs before being adopted as the system of record. The 30 auxiliary auth/profile screens from that same Figma file are **not** part of this system — they were built against a pre-DEC-023 account model and are excluded entirely.

---

## 1. Color Tokens

### Brand

| Token | Hex | Usage |
| :---- | :---- | :---- |
| `navy-900` | `#0C1F33` | Darkest text, primary body text on light backgrounds, text-on-fill for green/gold |
| `navy-800` | `#12304E` | Dark surfaces — headers, hero banners, lesson player top bar, video viewport |
| `gold-500` | `#B8912F` | Accent only — kickers, star icons, "Advanced" badge fill, quiz-row accent. **Never used as a text color on light backgrounds** (fails contrast); used as a *fill* with `navy-900` text on top |

### Green (success / primary action)

| Token | Hex | Usage |
| :---- | :---- | :---- |
| `green-600` | `#22A146` | **Fill only** — primary buttons, progress bar fill, "Enrolled" badge background, active-state icons. Text placed on this fill must be `navy-900`, never white |
| `green-700` | `#157A34` | **Text only** — links ("Learn More"), active tab label, any place green appears as text color on a light background |
| `green-50` | `#EBF7ED` | Light tint background (confirmations, profile picker) |
| `green-600 @ 10%` | `#22A146` at 10% | Subtle tint — sidebar active-item background |

### Neutral / Text

| Token | Hex | Usage |
| :---- | :---- | :---- |
| `navy-900` | `#0C1F33` | H1–H3 display text (source file had this duplicated as `slate-900` — same value, standardised on one name) |
| `slate-600` | `#475569` | **Standard secondary text** — meta, captions, timestamps, placeholder, inactive tab text. Replaces `slate-500` as the default |
| `slate-500` | `#64748B` | Decorative/non-critical use only (e.g. text at 18px+ semibold or larger, which only needs 3:1) — not the default secondary-text token |
| `white` | `#FFFFFF` | Text/icons on `navy-800`/`navy-900` dark surfaces only |
| `white @ 70%` | `#FFFFFF` at 70% | Subdued text on dark surfaces (dashboard sidebar, lesson player meta) |

### Background / Surface

| Token | Hex | Usage |
| :---- | :---- | :---- |
| `cream-50` | `#FBF9F4` | Primary page background |
| `cream-100` | `#F9F6F0` | Secondary/blocked-state background |
| `white` | `#FFFFFF` | Cards, header bar, inputs, sidebar |
| `navy-800` | `#12304E` | Dark section surfaces |

### Border

| Token | Hex | Usage |
| :---- | :---- | :---- |
| `border-light` | `#E3E8EF` | Card outlines, dividers, section separators |

### Link / Interactive

| Token | Hex | Usage |
| :---- | :---- | :---- |
| `blue-600` | `#2563BA` | Hyperlink text (non-CTA links) |
| `blue-700` | `#2D6CDF` | **Dual role, confirmed deliberate:** focus ring stroke (inputs, PIN pad) **and** the checked/selected-state fill for checkboxes and selectable pills (e.g. Filter Panel's checkboxes and age-band pills). White text/checkmark on this fill clears 4.5:1. Confirmed 2026-08-24 rather than left as an unreviewed drift — see Filter Panel's build in `catalogue/components.md`. `green-600` remains the token for primary actions (buttons); `blue-700` covers focus **and** selection, not primary action |

### Semantic

| Token | Hex | Usage |
| :---- | :---- | :---- |
| `error-600` | `#DC2626` | **Error text** — validation messages, destructive-action labels |
| `error-500` | `#EF4444` | Error **icons and borders only** (non-text elements need 3:1, not 4.5:1) |
| `error-500 @ 8%` | `#EF4444` at 8% | Error tint background |

### Contrast Rule (binding — NFR-12)

Every text/background pairing on this project must clear **4.5:1**, no exceptions carved out for large or bold text. The pairings above are pre-verified using WCAG relative-luminance contrast, not visual estimation. **Any new pairing introduced on a future screen must be checked before it ships** — this is the kind of small, high-repetition choice (see the PIN Pad note in each module's `components.md`) that's easy to miss in review and costly once shipped across every screen that reuses it.

The corrections against the original Figma export:

| Pairing | Original | Ratio | Fix |
| :---- | :---- | ----: | :---- |
| Button/badge text on `green-600` fill | White text | 3.36:1 | `navy-900` text |
| "Advanced" badge on `gold-500` fill | White text | 2.95:1 | `navy-900` text |
| Green used as link/tab text | `green-600` | 3.36:1 | `green-700` (text-only token) |
| Error text | `error-500` | 3.76:1 | `error-600` (text-only token) |
| Secondary/meta text | `slate-500` on cream | 4.52:1 | `slate-600` (real margin, 7.20:1) |

---

## 2. Typography

### Font Families

| Role | Family | Weights used |
| :---- | :---- | :---- |
| Display / Headings | **Marcellus** | Regular only |
| Body / UI | **Figtree** | Regular, Medium, SemiBold, Bold, Italic |

No other family is used. The source Figma file had 8 stray nodes on Inter — corrected to Figtree; not part of this system.

### Arabic / Urdu — Open Decision, Not Yet Resolved

**Neither Marcellus nor Figtree supports Arabic or Urdu glyphs.** FR-LOC-04 requires full RTL layout mirroring for both languages, so this blocks any non-English screen from being designed, not just launched. Recommendation, pending sign-off:

| Language | Heading face | Body face |
| :---- | :---- | :---- |
| Arabic | `Noto Naskh Arabic` | `Noto Sans Arabic` |
| Urdu | `Noto Nastaliq Urdu` | `Noto Nastaliq Urdu` |

Arabic and Urdu are **not** the same typographic decision — Urdu readers expect Nastaliq script; rendering Urdu in a Naskh face reads as foreign. This needs a decision recorded (candidate for a `3I-DEC-0XX`), not a silent default.

### Type Scale

All line-heights below are explicit — the source file left roughly half the scale as "auto," which resolves differently across the Next.js (browser) and Flutter (native) rendering engines this project targets on both platforms. Values are proposed defaults; flag if any need adjusting against the original Figma intent.

| Role | Family | Weight | Size | Line Height | Notes |
| :---- | :---- | :---- | ----: | ----: | :---- |
| Display XL | Marcellus | Regular | 72px | 80px | Hero decorative only |
| H1 | Marcellus | Regular | 56px | 64px | Page hero titles |
| H1-stat | Marcellus | Regular | 56px | 64px | Large stat numbers |
| H2 | Marcellus | Regular | 48px | 56px | Section hero |
| H2-number | Marcellus | Regular | 48px | 56px | Numbered sequence ("01", "02") |
| H3 | Marcellus | Regular | 40px | 48px | Section headings |
| H4 | Marcellus | Regular | 32px | 40px | Instructor name, profile headings |
| H4-form | Marcellus | Regular | 32px | 38px (120%) | Auth form titles |
| H5 | Marcellus | Regular | 28px | 36px | Sub-sections |
| H5-stat | Marcellus | Regular | 28px | 36px | Stat numbers |
| H5-form | Marcellus | Regular | 28px | 34px (120%) | Mobile form titles |
| H6 | Marcellus | Regular | 24px | 32px | Tertiary/mobile headings |
| Subtitle | Marcellus | Regular | 22px | 28px | Greeting text |
| Card Title | Marcellus | Regular | 18px | 24px | Course card titles |
| Card Title-alt | Marcellus | Regular | 22px | 28px | Category card titles |
| Logo | Marcellus | Regular | 20px | 24px | Brand wordmark, 0.8px tracking |
| Body L | Figtree | Regular | 18px | 26px | Long-form intro paragraphs |
| Body | Figtree | Regular | 16px | 24px | Standard body copy |
| Body S | Figtree | Regular | 15px | 22px | Card descriptions, testimonials |
| Body XS | Figtree | Regular | 14px | 20px | Instructor bios |
| Caption | Figtree | Regular | 13px | 18px | Meta info |
| Caption S | Figtree | Regular | 12px | 16px | Dashboard date labels |
| Caption XS | Figtree | Regular | 10px | 14px | Live-class instructor lines |
| Micro | Figtree | Regular | 9px | 12px | Certificate micro-copy |
| Nav Link | Figtree | Medium | 15px | 20px | Top nav items |
| Nav Active | Figtree | SemiBold | 15px | 20px | Active/CTA nav |
| Button Label | Figtree | SemiBold | 13–15px | 20px | Button text |
| Form Label | Figtree | SemiBold | 16px | 20px | Input labels |
| Badge Label | Figtree | Bold | 11px | 16px | Level tags — UPPERCASE |
| Kicker | Figtree | Bold | 12px | 16px | Section kickers — UPPERCASE, 1.5% tracking |
| Kicker SM | Figtree | Bold | 13px | 18px | Filter group labels — UPPERCASE, 1% tracking |
| Sidebar Label | Figtree | Medium | 14px | 20px | Dashboard sidebar items |
| Link Text | Figtree | SemiBold | 14px | 20px | Underlined text links |
| Tab Label | Figtree | Regular / SemiBold | 15px | 20px | Inactive `slate-600` / active `green-700` |
| Module Active | Figtree | Bold | 12px | 16px | "MODULE 3 • ACTIVE" |
| Breadcrumb | Figtree | Regular | 14px | 20px | Masthead breadcrumb |

---

## 3. Spacing

**4px base unit**, scale: `4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 96`. No changes from the source audit — this was already clean.

### Page-Level Layout

| Property | Value |
| :---- | :---- |
| Frame width | 1440px (desktop) / 390px (mobile) |
| Max content width | 1200px |
| Page horizontal margin | 120px each side |
| Header height | 80px (main), 64px (lesson player) |
| Auth card | 480px wide (desktop) / full-width, 24px padding (mobile) |

**Tablet breakpoint (768/1024px): not defined.** Open flag — needs a deliberate decision (fluid between breakpoints vs. dedicated tablet layout) rather than staying a silent gap.

---

## 4. Corner Radius

Consolidated from 11 raw values in the source file to 6 tokens:

| Token | Value | Usage |
| :---- | :---- | :---- |
| `radius-xs` | 4px | Compact frames, progress bar inner fill |
| `radius-sm` | 6px | Checkboxes, small interactive elements |
| `radius-md` | 8px | **Default** — buttons, inputs, cards, search bars |
| `radius-lg` | 12px | Cards — course, stat, review |
| `radius-xl` | 16px | Larger pill-style containers |
| `radius-full` | 9999px | Pills, fully-rounded pagination, avatar/portrait circles |

---

## 5. Elevation

Shadow color unified on `navy-900` (`rgba(12,31,51,…)`) across every level — the source had `shadow-lg` on a different base (`navy-800`), corrected here.

| Token | Spec | Usage |
| :---- | :---- | :---- |
| `shadow-sm` | `0 4px 12px rgba(12,31,51,0.02)` | Profile tiles, subtle card lift |
| `shadow-md` | `0 4px 24px rgba(12,31,51,0.03)` | Auth cards, form cards |
| `shadow-lg` | `0 8px 24px rgba(12,31,51,0.10)` | Sticky right rail, certificate mockup |
| `shadow-xl` | `0 12px 32px rgba(12,31,51,0.09)` | Modal overlays (PIN entry) |

---

## 6. Touch Targets

Not specified in the source file. Added given the platform's youngest users are five years old:

| Token | Value | Applies to |
| :---- | :---- | :---- |
| `touch-target-min` | 44px | All standard interactive elements — buttons, nav items, checkboxes |
| `touch-target-child` | 56px | Elements a learner (not a guardian) interacts with directly — PIN pad digits, profile-picker tiles |

This is additional to, not a replacement for, the PIN Pad's own "large touch targets" note in each module's `components.md`.

---

## 7. Iconography

**Feather Icons**, outline style, 1.5–2px stroke, no fills. Color follows context: `slate-600` (inactive), `navy-800` (dark-surface stroke), `green-600` (active/success fill contexts), `gold-500` (accent), `white` (on dark surfaces).

| Size | Usage |
| :---- | :---- |
| 12×12 | Compact star ratings, small check-circles |
| 14×14 | Standard inline icons, chevrons |
| 16×16 | Sidebar icons, play/check circles |
| 18×18 | Nav icons, video player controls |
| 20×20 | Search, notification bell |
| 24×24 | Large feature icons |

---

## 8. Componentisation Status

**Updated 2026-08-24.** The source Figma file originally had zero componentisation — every element was a raw frame. That is no longer the current state of the working file: `identity-and-access` (PIN Pad, Age Band Badge, Profile State Indicator, Account Menu), `commerce` (Itemised Total, Tier Badge, Stripe-Hosted Redirect Button), and `catalogue` (Course Card, Filter Panel) have all had their shared components built as real Figma main components/component sets, confirmed against spec before being reused across screens. Any component built from here forward should follow the same pattern: main component or component set, never a raw frame, checked against its module's `components.md` before screens start consuming it as an instance.

A proper **Figma Color Styles library**, generated directly from §1's tokens, was added 2026-08-24 so every future component/screen prompt references a named style rather than a hex value retyped from this document each time — see §10.

---

## 9. Known Gaps — Not Yet Designed

Carried forward from the source audit, unresolved:

- **States**: hover, active/pressed, disabled, focus, and loading are undesigned for nearly every interactive component (buttons, inputs, tabs, cards, pagination).
- **Empty states**: no enrolled courses, empty search results, no certificates, no upcoming classes.
- **Error states**: form validation, network failure, 404, payment/enrollment failure.
- **Loading states**: skeletons, spinners, buffering indicators.
- **Tablet breakpoint**: see §3.

None of these block adopting the token set above — they block specific screens that use them, and should be resolved screen-by-screen as those screens get built.

---

## 10. Figma Color Styles Library

A saved Figma Color Style exists for every token in §1, named to match the token names in this document exactly (e.g. a style literally named `navy-900`, not "Dark Blue" or similar). This closes the gap where every prompt kit up to 2026-08-24 retyped hex values from this table by hand — a real, if so-far-uneventful, drift risk every time this document and a prompt's Block A could silently disagree.

**Going forward, prompt kits should reference style names, not hex values,** wherever the Figma AI tooling in use can consume a named style directly. Where a prompt must still state a hex value explicitly (e.g. for tooling that can't reference styles), it must match this table exactly — this document remains the source of truth either way.
