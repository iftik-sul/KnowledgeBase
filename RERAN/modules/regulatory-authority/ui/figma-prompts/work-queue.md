---
project: RERAN
module: regulatory-authority
type: figma-prompt
screen: work-queue
status: draft
updated: 2026-09-14
derived_from:
  - "RERAN/modules/regulatory-authority/ui/screens/work-queue.md"
  - "RERAN/modules/regulatory-authority/ui/figma-prompts/app-shell.md"
  - "RERAN/modules/regulatory-authority/ui/status-badges.md"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
  - "RERAN/modules/regulatory-authority/ui/figma-prompts/library-assets.md"
reference_frame: "RERAN-Web-App / Financial & Trust Institution / screen #17: Escrow Request Queue (1247:36042)"
tags: [regulatory-authority, figma-prompt, back-office, queue]
---

# Figma build prompt — Work Queue (Group A, Archetype 1: Queue)

Build the Group A back-office **Work Queue** as a pixel-consistent sibling of the existing
**Escrow Request Queue** (node 1247:36042). Reuse that screen's exact region structure, frame
names, and dimensions. Only content and the sidebar nav change.

> **Shell:** build the sidebar + top bar per [`app-shell.md`](app-shell.md) — the shared shell
> extracted from the live FI-Sidebar (1247:36043) + TopBar (1247:36117). RA-Sidebar = a duplicate
> of FI-Sidebar with Group A nav items. Only the screen-specific content below changes.

## Frame
- Name: `Work Queue — Transaction` · size **1440x927** · desktop · surface `#FFFFFF`.
- Back-office screen; reachable only by the queue's owning role (MFA required).

## Shell specifics (rest of the shell = app-shell.md)
- **Sidebar:** RA-Sidebar, **active item: Work Queue**. Persona **Compliance & Escrow Auditor**
  nav: Dashboard · Work Queue (active) · Audit Trail · Notifications · Help & Support.
  Licensing variant (Licensing & Registration Officer) adds National Practitioner Register.
- **Top Bar:** `Background+HorizontalBorder` component — override Title "Work Queue — Transaction",
  Subtitle "Review and decide submitted applications.", profile role "Compliance & Escrow Auditor".
  The component's global search stays (it's distinct from the FiltersRow search below).

## Components to use (real, existing)
Colours, buttons, and badges bind to **library-assets.md** (Foundation tokens + components).
- App shell per app-shell.md · **Button Primary** (+ secondary for Export) · **Badge** (status) · **Avatar**.
- Icons: `Search`, `Chevron Down` (dropdowns), `Warning Circle` (SLA), `Chevron Right`.
- TopBar, cards, table = composed frames, named as below, matching the reference.

## Layout (mirror 1247:36042)
```
Work Queue 1440x927
├─ RA-Sidebar (240 wide)          ← app-shell.md
└─ MainContent (1200 wide, x=240)
   ├─ TopBar (1200x78)            ← Background+HorizontalBorder component (app-shell.md)
   └─ Workspace (inner width 1136, 32px side padding)
      ├─ Title-And-Actions:  Left title "Transaction Queue"
      │                      Right (optional): "Export" secondary button + a view switcher
      │                      (Transaction / Escrow) for the C&E Auditor persona
      ├─ SummaryCard grid:   five SummaryCard (~214x127) in one row — see KPIs below
      │                      (reference uses 274-wide at 4/row; narrow to ~214 so five fit 1136)
      ├─ FiltersRow:         SearchContainer (320) + FilterDropdowns + ResetFilter
      └─ TableSection:       TableHeaderActions ("All Applications" · "Showing 1-8 of 156")
                             QueueTable: TableHeader + TableRow (45) x8
                             Pagination
```

## SummaryGrid — KPI cards (from work-queue.md section 1)
Awaiting Review · Under Review · Information Requested · Decided This Month · **Breaching SLA**.
Selecting a card filters the table.

**SummaryCard construction** (verified from the live card): rounded-12, bg `#FFFFFF`, border `#DFE2E6`
with a **4px LEFT accent border** in the card's status colour (grey default; red for **Breaching SLA**).
- Top row: label (Inter Semi Bold **11**, UPPERCASE, `#505F79`, +0.5 tracking) + a 40x40 icon chip
  (bg `#E5F2FF` light blue, rounded-8, 20px icon).
- Below: value (Inter Medium **20**/30, `#091E42`) + sublabel (Inter Regular **12**, `#505F79`).

## FiltersRow (section 2)
- Search placeholder: "Search by reference, applicant, or subject…"
- Dropdowns: Originating service · Status · Age / SLA state · Channel (transaction vs escrow — C&E Auditor only).
- Default sort = **SLA urgency** (adopting the confirmed FTI-queue precedent), not recency.

## QueueTable columns (section 3)
Reference · Originating service (e.g. "RED #1 Register Initial Sale") · Applicant ·
Subject (project / property / title / practitioner) · **Status** (`Badge`) · **Age / SLA**
(countdown; amber = approaching, red = breached).
Row click -> opens **Application Review**. No decision control lives on this screen.

**TableRow construction** (verified from the live table): p-12, gap-16, border-bottom `#DFE2E6`, ~45 tall.
The **Reference** cell is a **blue underlined link** (`#006FE8`, Inter Semi Bold 13); other cells are
Inter 13 (`#091E42` primary / `#505F79` secondary) with fixed column widths and the Subject column
flex-growing. The **Status** cell is a pill (below).

**Status badge** — the live back-office table **hand-builds the status pill** (it does NOT use the
`Badge` component): rounded-full, px-10 py-4, Inter Medium **11**, soft background + dark text.
Values (status-badges.md section 1 — do not localise): `Under Review` · `Information Requested` ·
`Returned` · `Approved` · `Rejected`.
- **Confirmed pair:** Information Requested = bg `#FFFAEB` / text `#B54708` (amber).
- **Proposed (same pill pattern; confirm each hue from the library):** Under Review = blue ·
  Returned = orange · Approved = green · Rejected = red.
For Group A, either reuse the `Badge` component *if its variants match this pill*, or replicate the pill styling.
(Preferred: use the library `Badge` component with the Foundation mapping in library-assets.md.)

## Queue-type views (one screen, swap columns/content — do not build separate layouts)
- **Transaction** (C&E Auditor) — the default above.
- **Escrow / Trust** (C&E Auditor) — add an **Escrow flag** column (trustee-assessment received);
  only shows items past the FTI trustee gate.
- **Licensing** (Licensing & Registration Officer) — replace escrow column with **Credential type**;
  sidebar shows the Licensing variant (adds National Practitioner Register).

## Notes / guards
- The reference **FI-Sidebar has no per-item count badges** (the FTI screen spec mentioned one, but the
  built sidebar omits it). RA-Sidebar omits them too, to stay consistent; adding queue counts would be a
  platform-wide change across FI/RED/RA sidebars.
- Breaching SLA is computed against each item's **originating-service** SLA, not one queue-wide timer.
- Auto-approval licensing items do not appear here.
- Status text is owned by status-badges.md section 1 — do not introduce local status words.
