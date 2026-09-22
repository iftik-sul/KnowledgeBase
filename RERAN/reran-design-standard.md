---
project: RERAN
type: skill
scope: figma-build
status: draft
updated: 2026-09-22
description: >
  The RERAN-wide Figma design standard. Read this BEFORE building or prompting ANY screen in ANY module
  (Regulatory Authority, FTI, RED, Individual User, Public Users, Allied Professionals, RESC). It
  defines the platform's shared tokens, components, status vocabulary, geometry, typography, the full
  table and card taxonomies, plus the old-hex→token migration map used to harmonise legacy screens.
  Section A is universal (all modules). Section B is surface-specific (back-office vs applicant portal).
  Section C is per-module specifics. This supersedes the RA-only scope of the former figma-build-rules.md.
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
2. **Use the canonical component; don't hand-build what exists.** Stat cards, top bars, sidebars,
   badges, buttons, inputs, pagination, icons are all components. Compose only what has no component
   (tables, card sections, panels), per A5.
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

## A4. Canonical components (instance these — never hand-build)
> **These are local components on the Regulatory Body (RA) page — not a published team library.** Any
> screen on any page in this file instances them from there; cross-page component use within the file
> works natively (the FTI/RED portal already does this — 21 of its instances point back to RA-page
> components). Reference by name + node ID: the name is the durable anchor, the node ID the precise
> pointer (an ID only goes stale if the component is deleted and rebuilt). `Badge`, `Buttons/Button`,
> the form/identity atoms, and icons are different — they come from the **published UI-kit library**
> (remote components), and are referenced by name only, as before.

- **Stat / KPI card** (RA-page-local, node `1692:528`) — the canonical stat tile: white, `N30` border,
  radius 14, **no icon**, props Label (all-caps `N400`) / Value (`Heading 5` `N900`) / Sublabel
  (`Small/Regular` `N400`). Flex-1 in a row. (Legacy `SummaryCard`/`MetricCard`/hand-built KpiCard are
  retired — instance this one.)
- **Top bar** (`Background+HorizontalBorder`, RA-page-local, node `1692:536`) — 1200×78, white; props
  Title/Subtitle/Name/Role; carries the notification bell + profile block. Never hand-build a "TopBar".
- **Sidebar** (`RA-Sidebar`, RA-page-local, node `1667:43811`, 8 persona variants) — 240×927, white,
  construction: SidebarHeader (78, RERA logo) / SidebarNav (NavItem + one NavItemActive at `blue-600`)
  / SidebarFooter (Sign Out). **One sidebar component per module** (RA-Sidebar, FI-Sidebar,
  RED-Sidebar, …) — same construction, module-specific nav items. No per-item count badges.
- **`Filter Dropdown`** (RA-page-local, node `1724:506`, 105×40) — the canonical table filter trigger.
- **`Search Bar`** (RA-page-local, node `1733:55348`, 180×40) — the canonical table search field.
- **`Pagination`** (RA-page-local, node `1712:376`, 1136×64) — table footer, "Showing 1–N of M",
  32×32 rounded-8 prev/next + active page.
- **`Badge`** (published UI-kit library) — the ONLY status/label asset. Size sm, Icon False; set the
  **Color** prop per the module's status vocabulary (A8). Never hand-build a status pill.
- **`Buttons/Button`** (published UI-kit library) — Hierarchy Primary/Secondary color/Secondary
  gray/Tertiary/Link; Size sm–xl. **⚠ Primary defaults to `Brand/600` purple — override its fill to
  `blue-600` on every instance.**
- **`Buttons/Button destructive`** (published UI-kit library) — same API; its default `Red/600` is
  correct, no override. Reject/delete/dismiss.
- **`Input field`** / **`Textarea input field`** / **`Verification code input field`** / **`Checkbox`**
  / **`Dropdown menu`** / **`Avatar`** (+ label group) (published UI-kit library) — the form + identity
  atoms.
- **Icon library** (published UI-kit library) — the categorized icon frames on the Component library
  page. Pull all icons here.

## A5. Composed patterns (no component — build to spec)
- **Breadcrumb** — real `PathSegment`s (label + 14px `Chevron Right` icon), non-final = `blue-600`
  Medium 13 links, final = `N400` Regular 13 no chevron. **Drill-down screens only** — a top-level
  sidebar destination never gets one.
- **Empty state** — centred illustration + one line of `Caption`/`Small` guidance.
- **Info/warning banner** — rounded-12, tinted background (the semantic `*/50` token), icon chip +
  title (`Semi Bold` 13) + description (`Regular` 12).
- **Tables** and **Cards** — the two big composed patterns — have their own full taxonomies in A5a and
  A6 below.

## A5a. TABLES — complete taxonomy (canonical from RA; FTI/RED harmonise to this)
Five table archetypes, all sharing one core row/cell construction. RA tables are canonical and NOT
changed; FTI/RED tables harmonise to match (see A5a.7).

### A5a.0 — Core construction (EVERY table type)
```
Header row  (HORIZONTAL, FILL×HUG ~38–40, gap 12, pad 12/20/12/20)
            NO fill (transparent, inherits white) · N40 bottom-only stroke
            cell text: Caption/Medium 13, N400
Data row × N (HORIZONTAL, FILL×FIXED 48, gap 12, pad 0/20/0/20)
            NO fill · N40 bottom-only stroke · counter-align CENTER
            Col 0 (primary id): Inter Semi Bold 13, blue-600 (link) or N900
            other cols: Inter Regular 13, N900 (or N400 secondary)
            status col: real Badge instance (sm), left-aligned
```
Core rules (all types):
1. **Every cell — header AND data — is `FIXED` width.** Never HUG/FILL. Header and data cell widths
   identical per column. Badge/button cells sit in a FIXED wrapper.
2. **Data row height FIXED 48.** Header row HUG (~38–40).
3. **Row separation = bottom-only `N40` stroke**, not item spacing (spacing 0).
4. **No underline on any table cell text** (`textDecoration: NONE`); the only underline in the app is a
   real hyperlink outside a table.
5. **Column-width formula (always):** `available = rowWidth − (nCols−1)×gap`;
   `colW[i] = floor(available × prop[i]/100)`; remainder → Col 0, so `sum(colW)+gaps = rowWidth`.
   Typical proportions: primary id ~45% · short label ~12% · date ~13% · status ~16% · action ~14%.
6. **Pagination — by table role, not by current row count.** The **primary full-page table** of a
   queue/list/editor screen (Types B, C, D, and standalone E) **always ends with an instance of the
   `Pagination` component (RA page, `1712:376`)** — the real dataset spans many pages even when the
   mock shows only ~8–11 rows. An **embedded sub-table** (a Type-A simple table inside a Dashboard
   section or a detail card — e.g. "Recent Activity", a documents sub-list) has **no pagination**; it
   shows a short fixed set (~5) and uses a "See All" link instead if more exist. Rule of thumb: *if the
   table is the screen's main content it paginates; if it's a widget inside another section it doesn't.*

### A5a.1 — Type A: Simple table
Header + data, no filter, no title, no wrapping card. Sub-section of a screen (dashboard activity,
detail sub-list). *RA ref:* Dashboard "Recent Activity".

### A5a.2 — Type B: Table with filter
Header + data preceded by a Controls block (title + Search Bar + Filter Dropdowns), inside a titled
card. The queue/list workhorse. *RA ref:* Work Queue, Audit Trail, Case Queue, Register, Notifications.
```
Table card (VERTICAL, FILL×HUG, white, N30 border, r12, clipsContent)
├─ Controls (VERTICAL, gap 16, pad 20/20/16/20)
│   ├─ Title row (HORIZONTAL, FILL×HUG) — section title left
│   └─ Filters (HORIZONTAL, gap 12, h40) — Search Bar (`1733:55348`) + Filter Dropdown (`1724:506`) instances
├─ Header row
├─ Data row × N
└─ Pagination (`1712:376`, FILL×HUG)
```

### A5a.3 — Type C: Table with title-action button
Like B (or simple) but the title row carries a right-aligned action button (`Buttons/Button` — "New
Fee Entry", "Invite Staff"). *RA ref:* Fee Schedule "Fee Entries", Admin Console "Staff". Title-action
button and a filters row can coexist.

### A5a.4 — Type D: Table with row actions
Each data row ends with an action control in a **FIXED rightmost action cell** (never HUG). **Every
row-action button uses ONE style: the borderless text-link.** No bordered buttons, no filled buttons
in table rows — ever.

**The one row-action style:** `Buttons/Button`, **Hierarchy = Link color**, **Size sm** — borderless,
no fill, text only.
- **Normal action** ("Review", "View", "Open", "Edit", "Manage") → **`blue-600` text**.
- **Destructive action** ("Delete", "Revoke", "Deactivate") → same borderless text-link, but
  **`Red/600` text** (`Buttons/Button destructive`, Link hierarchy — no fill, red text).

Rules:
- **One pattern for all row actions** — always the borderless text-link. Never a bordered
  (Secondary-gray) or filled (Primary) button inside a table row.
- Colour carries the meaning: `blue-600` for normal, `Red/600` for destructive. Nothing else changes.
- Size is always **sm**. The action cell is FIXED width (~110–120), the text-link left- or
  centre-aligned in it consistently down the column.
- A row may also have **no button** — the whole row is click-to-open instead (e.g. Practitioner
  Register rows open Entry Detail on row click). That's valid; don't add a redundant "View" link.
- *RA ref:* Application Review "Review" per document row (the canonical borderless text-link).

### A5a.5 — Type E: Bare table wrapped in a card
A Type-A simple table given its own container (white, `N30` border, r12, clipsContent) when standalone.
The wrapper Types B/C use, minus the Controls block.

### A5a.6 — NOT tables
FTI/RED `OverviewCard`/`InstitutionCard`/`ApplicantCard`/`ServiceCard`/`AppDetailsCard`/`SuccessCard`/
`ConfirmationCard` are **key/value summary cards** (the nested double-card, A6 Type 3), not tables —
harmonise them as cards.

### A5a.7 — FTI/RED table harmonisation gaps
| Aspect | RA canonical | FTI/RED current | Fix |
| :-- | :-- | :-- | :-- |
| Outer container | white, `N30` border, r12 | often bare | wrap in Type-E card (fill+`N30`+r12) |
| **Header fill** | **transparent** | **`N20` grey bar** | **remove header fill** |
| Header bottom stroke | `N40` | `N40` ✓ | keep |
| **Data row height** | **48** | **46** | set to **48** |
| **Cell sizing** | **all FIXED** | Col 0 FILL, Badge HUG | make every cell FIXED (A5a.0 r5) |
| Col 0 weight | Semi Bold 13 | sometimes Regular | Col 0 = Semi Bold |
| Cell underline | none | occasional | remove (`NONE`) |

## A6. CARDS — complete taxonomy (canonical from RA)
Five card types; the "single card" and "double nested card" are Types 1 and 3.

### Type 1 — Section card (the single card, base of everything)
**White, `N30 #EBEDF0` border, radius 12, padding 20/24**, VERTICAL gap 16, FILL×HUG. Most common card.
```
Section card
├─ Title (Body/Medium 16, N900)  [+ inline Badge right, if it carries status]
├─ ... content ...
└─ [optional] Footer — N30 top-border + action links (16px icon + Caption/Medium 13, blue-600)
```
Variants: title-only · title + inline status Badge · title + footer links · header+metadata (pad 16).

### Type 2 — Field-group sub-card
Inner unit of a nested double-card (also standalone inside any card). **`N20 #F5F6F7` fill, NO border,
radius 8, padding 16, gap 8.** The N20 fill is the separator — never border it.
```
Field-group card (VERTICAL, N20, r8, no border, pad 16, gap 8)
├─ Subsection label (Caption/Medium 13, N900)
└─ Fields row (HORIZONTAL, gap 24) → field × N (VERTICAL, gap 2)
    ├─ Label (Small/Regular 12, N400)
    └─ Value (Caption/Medium 13, N900)
```

### Type 3 — Nested double-card (single card + field-group sub-cards)
A Type-1 Section card whose content is one or more Type-2 sub-cards. White-outer / N20-inner contrast
is the point. *RA ref:* Application Summary, Parties & Case Details, Entry Details. FTI/RED
`OverviewCard`/`InstitutionCard`/`SuccessCard` map here.

### Type 4 — Table card
A Type-1 card wrapping a table (A5a Types B/C/E). White, `N30`/`N40` border, r12, clipsContent.

### Type 5 — Stat / KPI card (component)
The metric tile — a component. **White, `N30` border, radius 14** (note 14, not 12), no icon. Props
Label (all-caps `N400`) / Value (`Heading 5` `N900`) / Sublabel (`Small/Regular` `N400`), flex-1.
Retired: `SummaryCard`, `MetricCard`, hand-built `KpiCard`.

### Card rules (all types)
1. **Radius:** 12 (section/table/outer) · **8** (field-group sub-cards, inputs) · **14** (stat card).
2. **Border:** `N30` on white cards; **none** on `N20` sub-cards (fill separates); `N40` ok on table
   cards/inputs.
3. **Nesting = fill contrast:** white outer → `N20` inner. Never white-on-white or a second inner
   border.
4. **Padding:** section 20/24 · sub-card 16 · header/metadata 16.
5. **Title:** `Body/Medium` 16 `N900`; inline status = real Badge, right-aligned.
6. **Footer (optional):** `N30` top-border + action links (16px icon + `Caption/Medium` 13 `blue-600`).

### FTI/RED card harmonisation
FTI/RED cards map onto these types (mostly Type 1 or 3). Harmonise: white fill, `N30` border (not
`#E4E7EC`), radius 12; group fields into Type-2 `N20`/r8/no-border sub-cards; a grey `#F4F5F7`/`#E4E7EC`
body → `N20` if a sub-card, else white + `N30`.

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
Same tokens/components/status/geometry/tables/cards as A. **But** the "N20 workspace backdrop" and
"breadcrumb only on drill-down" back-office rules do NOT force onto portal flow screens — a portal step
screen has its own layout (stepper, form, payment). Apply A's tokens/components/status/geometry/tables/
cards; don't impose B1's back-office shell rules where they don't fit.

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
  (design lives in Figma, not prompt files). **RA tables and cards are the canonical reference for
  A5a/A6 — never changed; other modules harmonise to them.** The 6 RA-page-local components (A4) are
  instanced cross-page by every other module; nothing here needs a published library.

## C2. FTI + RED (the "Financial & Real Estate" portal page)
- **Two module families share one page** — FTI (institution services) and RED (developer services),
  each with its own sidebar (`FI-Sidebar`, `RED-Sidebar`). Naming: spaced/capitalised ("NAV – 03 …")
  and hyphenated ("nav-03-…") variants both appear.
- Status vocabularies: `financial-trust-institutions/ui/status-badges.md` (Application, Escrow Request,
  Trust Account, Institutional Approval) — the source for the treatment→Colour mapping, adopted
  platform-wide.
- **Harmonised to this standard in Sept 2026:** KPI cards → shared card component; TopBar → shared top
  bar; both sidebars → RA construction; ~636 status pills → Badge (818 instances); all 113 frames →
  1440×927; ~1,700 off-token colours → tokens (via A9's map). Fully token-compliant. **Tables and cards
  still to be harmonised to A5a/A6** (remove grey table-header fills, 46→48 rows, all-FIXED cells;
  cards → white/`N30`/r12 with `N20` sub-cards).

## C3. Other modules (Individual User, Public Users, Allied Professionals, RESC)
Bind to Section A + the relevant Section B surface. Each has (or needs) its own `status-badges.md` with
a Treatment column; map to Badge Colours via A8. Where a legacy screen shows off-token colour, apply
A9; tables/cards → A5a/A6. No module-specific components beyond its own sidebar unless confirmed on canvas.

---

## Do / Don't (platform-wide)
- ✅ Instance the canonical RA-page-local components (A4, by name + node ID) and the published UI-kit
  components (by name); bind to A1 tokens; mirror a built reference; Badge for every status (Color by
  A8); override Primary buttons to `blue-600`; 1440×927; Nigerian data; build tables/cards to the
  A5a/A6 taxonomies (all-FIXED cells, 48px rows, no table header fill; white/`N30`/r12 cards with
  `N20` sub-cards); row-action buttons are the ONE borderless text-link style (blue-600 normal,
  Red/600 destructive); the main table paginates, an embedded sub-table doesn't; verify against Figma.
- ❌ Raw hex; hand-built pills/cards/sidebars/top bars; grey table-header bars; 46px rows; HUG/FILL
  cells; underlined cell text; a Primary button left purple or as a table row action; a bordered/filled
  button as a row action; a Badge showing "Label"; a breadcrumb on a top-level screen; Liberation Mono;
  off-927 heights; inventing status words; forcing back-office shell rules onto portal flow screens;
  pushing to GitHub without approval.
