---
project: RERAN
type: skill
scope: figma-build
status: draft
updated: 2026-09-21
description: >
  The RERAN-wide Figma design standard. Read this BEFORE building or prompting ANY screen in ANY module
  (Regulatory Authority, FTI, RED, Individual User, Public Users, Allied Professionals, RESC). It
  defines the platform's shared tokens, components, status vocabulary, geometry, and typography, plus
  the old-hex→token migration map used to harmonise legacy screens. Section A is universal (all
  modules). Section B is surface-specific (back-office vs applicant portal). Section C is per-module
  specifics. This supersedes the RA-only scope of the former figma-build-rules.md.
authorities:
  - "Each module's ui/status-badges.md — the status vocabulary for that module"
  - "regulatory-authority/ui/role-screen-matrix.md, validation-rules.md — RA nav + guards"
  - "Figma: RERAN-Web-App (vBSCiJLpyP8KLCTsmySVrS) — the design system + built screens (ground truth)"
tags: [reran, figma, skill, design-system, standard, platform-wide]
---

# RERAN — Platform Design Standard (Figma)

RERAN is one Figma file (`vBSCiJLpyP8KLCTsmySVrS`, "RERAN-Web-App") holding every module: the
Regulatory Authority (RA) back-office, the FTI and RED applicant-facing portals, Individual User,
Public Users, Allied Professionals, and RESC. Historically each module was built at a different time
and drifted apart (different colours, hand-built pills, different sidebars). This document is the
**one shared standard** every module binds to, so new work starts on-standard and never needs the
harmonisation pass again.

**How to read this:** Section A is **universal** — it holds for every screen in every module. Section
B splits the two **surface types** (back-office vs portal), because some rules differ. Section C notes
**per-module** specifics. When building any screen: apply A always, the relevant B, then C.

---

# SECTION A — UNIVERSAL (every module, every screen)

## A0. Golden rules
1. **Bind to tokens/components, never raw hex or hand-built substitutes.** Use A1's tokens and A4's
   components.
2. **Use the shared component; don't hand-build what exists.** Stat cards, top bars, sidebars, badges,
   buttons, inputs, pagination, icons are all components. Compose only what has no component (tables,
   card sections, panels), per A5.
3. **Adapt, don't reinvent.** Every new screen has a close sibling already built — mirror its structure,
   change only content.
4. **Don't invent content.** Status words come from the module's `status-badges.md`; RA nav/guards from
   `role-screen-matrix.md` / `validation-rules.md`.
5. **Verify against the Figma file, not memory.** This doc is a snapshot; the file is ground truth.
6. **All sample data is Nigerian.** Names, companies, addresses, phones, currency (₦/NGN), institutions,
   locations — always Nigerian, never "Acme Corp"/"John Smith"/US addresses.

## A1. Colour tokens (the ONLY colours allowed)
| Token | Hex | Role |
| :-- | :-- | :-- |
| `N900` | `#091E42` | primary text, headings |
| `N400` | `#505F79` | secondary/muted text, placeholders |
| `N40` | `#DFE2E6` | input/table borders, dividers |
| `N30` | `#EBEDF0` | card borders, chips |
| `N20` | `#F5F6F7` | subtle fills, back-office workspace background |
| `blue-600` | `#006FE8` | primary, links, active nav |
| `blue-700` | `#0057B5` | hover/pressed |
| `Blue/50` | `#EFF6FF` | Badge Blue / info-tint background |
| `green-700` | `#258D3F` | success text/icon |
| `Green/50` | `#F0FDF4` | Badge Success / success-tint background |
| `orange-700` | `#B56A00` | warning text/icon |
| `Yellow/50` | `#FEFCE8` | Badge Warning / warning-tint background |
| `Red/600` | `#DC2626` | error/destructive text, the named red |
| error-tint | `#FEF3F2` | Badge Error background |
| `Background/primary` | `#FFFFFF` | surfaces — sidebars, top bars, cards |
| `Brand/600` | `#7F56D9` | ⚠ the kit `Buttons/Button` Primary default (purple) — ALWAYS override to `blue-600` |

**No other colours.** Any hex not in this table is drift and must map to the nearest token (see A9).

## A2. Typography
Inter throughout; the logo lockup is IBM Plex Sans Bold 14. Styles: `Body Large/Medium` 18/27 ·
`Body/Medium` 16/24 · `Heading 5` Semibold 24 (stat value) · `Footnote/Medium` 14/20 (buttons, input
labels) · `Caption/Medium` 13/20 (table cells, nav, filters) · `Caption/Regular` 13/20 · `Small/Regular`
12/18 (subtitles, field labels, stat label/sublabel). No other fonts — no Liberation Mono (an
HTML-import artifact); convert any to Inter.

## A3. Geometry
Every screen frame is **1440 × 927**, fixed. Never auto/hug, never a stray 917/932/etc. Content taller
than 927 scrolls inside the frame (the frame is a viewport window, not a fit-to-content box) — resize
the outer frame to 927, never squash the content. Sidebar and any full-height element span the full 927.

## A4. Shared components (instance these — never hand-build)
- **Stat / KPI card** — the canonical stat tile: white, `N30` border, radius 14, **no icon**, props
  Label (all-caps `N400`) / Value (`Heading 5` `N900`) / Sublabel (`Small/Regular` `N400`). Flex-1 in a
  row. (Legacy `SummaryCard`/`MetricCard`/hand-built KpiCard are retired — instance the shared card.)
- **Top bar** (`Background+HorizontalBorder`) — 1200×78, white; props Title/Subtitle/Name/Role; carries
  the notification bell + profile block. Never hand-build a "TopBar" frame.
- **Sidebar** — 240×927, white, construction: SidebarHeader (78, RERA logo) / SidebarNav
  (NavItem + one NavItemActive at `blue-600`) / SidebarFooter (Sign Out). **One sidebar component per
  module** (RA-Sidebar, FI-Sidebar, RED-Sidebar, …) — same construction, module-specific nav items. No
  per-item count badges.
- **`Badge`** — the ONLY status/label asset. Size sm, Icon False; set the **Color** prop per the
  module's status vocabulary (A8). Never hand-build a status pill.
- **`Buttons/Button`** — Hierarchy Primary/Secondary color/Secondary gray/Tertiary/Link; Size sm–xl.
  **⚠ Primary defaults to `Brand/600` purple — override its fill to `blue-600` on every instance.**
- **`Buttons/Button destructive`** — same API; its default `Red/600` is correct, no override. Reject/
  delete/dismiss.
- **`Input field`** / **`Textarea input field`** / **`Verification code input field`** / **`Checkbox`**
  / **`Dropdown menu`** / **`Avatar`** (+ label group) — the form + identity atoms.
- **`Pagination`** — table footer, "Showing 1–N of M", 32×32 rounded-8 prev/next + active page.
- **Icon library** — the categorized icon frames on the Component library page. Pull all icons here.

## A5. Composed patterns (no component — build to spec)
- **Card** — white, `N30` border, radius 12, px-24 py-20; title `Body/Medium` `N900` (+ inline Badge if
  it carries status); optional footer: `N30` top border + action links (16px icon + `Caption/Medium` 13
  `blue-600`).
- **Nested double-card** — for grouped read-only fields: outer Card; inside, field-group sub-cards
  filled `N20`, radius 8, no border, padding 16 — group label (`Semi Bold` 13 `N900`) then field pairs
  (label `Small/Regular` 12 `N400` over value 13 `N900`).
- **Table row** — padding 12, gap 16, bottom border `N40`, cells 13 (`N900`/`N400`); reference/ID cell =
  `blue-600` Semibold underlined link; status cell = real Badge. Bare or wrapped in a titled card —
  consistent within a screen.
- **Breadcrumb** — real `PathSegment`s (label + 14px `Chevron Right` icon), non-final = `blue-600`
  Medium 13 links, final = `N400` Regular 13 no chevron. **Drill-down screens only** — a top-level
  sidebar destination never gets one.
- **Empty state** — centred illustration + one line of `Caption`/`Small` guidance.
- **Info/warning banner** — rounded-12, tinted background (the semantic `*/50` token), icon chip +
  title (`Semi Bold` 13) + description (`Regular` 12).

## A8. Status = Badge, colour by treatment
Every status is a `Badge` (Size sm, Icon False) with its **Color** set. Each module's `status-badges.md`
defines its status words and a **Treatment** (Neutral/Info/Warning/Error/Success). Map treatment → Badge
Color once, platform-wide:
| Treatment | Badge Color |
| :-- | :-- |
| Neutral | Gray |
| Info | Blue |
| Warning | Warning |
| Error | Error |
| Success | Success |
So: any positive/done state → Success · in-progress/info → Blue · needs-attention → Warning · failure/
blocking → Error · neutral/inactive → Gray. Same status word = same Colour on every screen, always.

## A9. Legacy → token migration map (use when harmonising ANY drifted screen)
Legacy screens use an older Ant/Tailwind-ish palette. Remap each to its token. **The role decides the
target** (a green as text → `green-700`; the same green as a fill → `Green/50`).
**Neutrals:** `#7A8699`/`#667085`/`#4A5568` → `N400` · `#E4E7EC`/`#E2E8F0` → `N40` · `#EAEDF0` → `N30` ·
`#F4F5F7`/`#F8FAFC`/`#F2F4F7`/`#FAFAFA`/`#F8F9FA` → `N20`.
**Greens:** `#12B76A`/`#28A745`/`#22C55E`/`#10B981`/`#047857` (text) → `green-700`; `#ECFDF3`/`#E6FFED`/
`#D1FADF` (fill) → `Green/50`.
**Reds:** `#D92D20`/`#F5222D`/`#F04438` (text) → `Red/600`; `#FEE4E2`/`#FFF1F0`/`#FFF0F0` (fill) →
error-tint `#FEF3F2`.
**Ambers:** `#B76E12`/`#D97706`/`#F79009`/`#C2410C`/`#D46B08`/`#7F5F00` (text) → `orange-700`;
`#FFFBEB`/`#FFFAEB`/`#FFE0B2`/`#FEF3C7`/`#FFE58F`/`#FFF9E6`/`#FFFBE6` (fill) → `Yellow/50`.
**Blues:** `#004E9C`/`#004085`/`#0052B3`/`#0057B5` (text) → `blue-600`/`blue-700`; `#E6F2FF`/`#E3F2FD`/
`#D0E7FF`/`#F0F7FF`/`#F4F9FF` (fill) → `Blue/50`.
This map was applied to harmonise the FTI/RED portal (Financial & Real Estate page) in Sept 2026 —
~1,700 uses remapped to zero drift. Reuse it verbatim for any future legacy screen.

## A10. Verification discipline
`get_metadata` for sizes · `get_variable_defs` / `get_design_context` for tokens+structure · navigate
by node IDs (the page-list call is unreliable — has hidden whole pages) · after any KB push,
`get_file_contents` to confirm it landed and still exists · read design as data, not images (base64
screenshots render blank here).

---

# SECTION B — SURFACE-SPECIFIC (two kinds of screen)

RERAN has two surfaces. Universal Section A holds for both; these differ.

## B1. Back-office (RA)
Staff decision/admin screens. **Workspace fill = `N20 #F5F6F7`** (sidebar/top bar/cards stay white — the
N20 backdrop gives white cards contrast). Fixed 1440×927. Breadcrumb only on drill-down screens.
Archetypes: Queue (KPI row → filters → table → pagination), Detail/Decision (breadcrumb → item header →
two-column body → sticky decision panel), Dashboard, Editor/Config.

## B2. Applicant portal (FTI, RED, Individual User, …)
Public/applicant-facing multi-step flows (Application Info → Service Info → Documents → Payment →
Review → Submit → Details → Confirmation) plus nav screens (catalog, queues, profile, notifications).
Same tokens/components/status/geometry as A. **But** the "N20 workspace backdrop" and "breadcrumb only
on drill-down" back-office rules do NOT force onto portal flow screens — a portal step screen has its
own layout (stepper, form, payment). Apply A's tokens/components/status/geometry; don't impose B1's
back-office shell rules where they don't fit.

---

# SECTION C — PER-MODULE SPECIFICS

## C1. Regulatory Authority (RA)
- Sidebar: **`RA-Sidebar`**, prop `Persona` — 8 variants (Compliance & Escrow Auditor, Licensing &
  Registration Officer, Dispute Adjudication Officer, Revenue & Finance Officer, System Super
  Administrator, Director-General / Registrar, Inspection & Enforcement Officer, State Liaison
  Coordinator).
- Status vocabularies: `regulatory-authority/ui/status-badges.md` §1–§5 (decision, case lifecycle,
  config, field/governance, document review) — all with confirmed Badge Colours.
- Nav/visibility: `role-screen-matrix.md`. Guards/step-up: `validation-rules.md`.
- RA is the only module where RBAC genuinely gates access; the only place `figma-prompts/` was removed
  (design lives in Figma, not prompt files).

## C2. FTI + RED (the "Financial & Real Estate" portal page)
- **Two module families share one page** — FTI (institution services) and RED (developer services),
  each with its own sidebar (`FI-Sidebar`, `RED-Sidebar`). Naming: spaced/capitalised ("NAV – 03 …")
  and hyphenated ("nav-03-…") variants both appear.
- Status vocabularies: `financial-trust-institutions/ui/status-badges.md` (Application, Escrow Request,
  Trust Account, Institutional Approval) — the source for the treatment→Colour mapping, adopted
  platform-wide.
- **Harmonised to this standard in Sept 2026:** KPI cards → shared card component; TopBar → shared top
  bar; both sidebars → RA construction; ~636 status pills → Badge (818 instances); all 113 frames →
  1440×927; ~1,700 off-token colours → tokens (via A9's map). Fully token-compliant.

## C3. Other modules (Individual User, Public Users, Allied Professionals, RESC)
Bind to Section A + the relevant Section B surface. Each has (or needs) its own `status-badges.md` with
a Treatment column; map to Badge Colours via A8. Where a legacy screen shows off-token colour, apply
A9. No module-specific components beyond its own sidebar unless a real need is confirmed on canvas.

---

## Do / Don't (platform-wide)
- ✅ Instance the shared components; bind to A1 tokens; mirror a built reference; Badge for every status
  (Color by A8); override Primary buttons to `blue-600`; 1440×927; Nigerian data; verify against Figma.
- ❌ Raw hex; hand-built pills/cards/sidebars/top bars; a Primary button left purple; a Badge showing
  "Label"; a breadcrumb on a top-level screen; Liberation Mono; off-927 heights; inventing status words;
  forcing back-office shell rules onto portal flow screens; pushing to GitHub without approval.
