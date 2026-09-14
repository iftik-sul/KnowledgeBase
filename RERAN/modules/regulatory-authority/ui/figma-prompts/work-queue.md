---
project: RERAN
module: regulatory-authority
type: figma-prompt
screen: work-queue
status: draft
updated: 2026-09-14
derived_from:
  - "RERAN/modules/regulatory-authority/ui/screens/work-queue.md"
  - "RERAN/modules/regulatory-authority/ui/status-badges.md"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
reference_frame: "RERAN-Web-App / Financial & Trust Institution / screen #17: Escrow Request Queue (1247:36042)"
tags: [regulatory-authority, figma-prompt, back-office, queue]
---

# Figma build prompt — Work Queue (Group A, Archetype 1: Queue)

Build the Group A back-office **Work Queue** as a pixel-consistent sibling of the existing
**Escrow Request Queue** (node 1247:36042). Reuse that screen's exact region structure, frame
names, and dimensions. Only content and the sidebar change.

## Frame
- Name: `Work Queue — Transaction` · size **1440x927** · desktop · neutral page background token.
- Back-office screen; reachable only by the queue's owning role (MFA required).

## Components to use (real, existing)
- **RA-Sidebar** — NEW component, built as a direct sibling of `FI-Sidebar` / `RED-Sidebar`
  (240x927, identical construction). The sidebar is **role-scoped** (per role-screen-matrix.md section 1):
  - Default persona **Compliance & Escrow Auditor**: Dashboard · **Work Queue (active, count badge)** · Audit Trail.
    (Transaction and Escrow are *in-screen views*, not separate nav items — see Queue-type views.)
  - Licensing variant (**Licensing & Registration Officer**): Dashboard · **Work Queue (active)** · National Practitioner Register · Audit Trail.
- **Button Primary** (+ secondary variant for Export), **Badge** (status), **Avatar**.
- Icons: `Search`, `Chevron Down` (dropdowns), `Warning Circle` (SLA), `Chevron Right`, notification `bell`.
- Everything else (TopBar, cards, table) = composed frames, named as below, matching the reference.

## Layout (mirror 1247:36042)
```
Work Queue 1440x927
├─ RA-Sidebar (240 wide)
└─ MainContent (1200 wide, x=240)
   ├─ TopBar (1200x78)
   │   ├─ HeaderTitles:  Title "Work Queue — Transaction"
   │   │                 Subtitle "Review and decide submitted applications."
   │   └─ HeaderRight:   NotificationBell · VerticalDivider · Avatar + ProfileMetadata
   │                      (name + role "Compliance & Escrow Auditor")
   └─ Workspace (inner width 1136, 32px side padding)
      ├─ Title-And-Actions:  Left title "Transaction Queue"
      │                      Right (optional): "Export" secondary button + a view switcher
      │                      (Transaction / Escrow) for the C&E Auditor persona
      ├─ SummaryGrid:        five SummaryCard (274x127), one row — see KPIs below
      ├─ FiltersRow:         SearchContainer (320) + FilterDropdowns + ResetFilter
      └─ TableSection:       TableHeaderActions ("All Applications" · "Showing 1-8 of 156")
                             QueueTable: TableHeader + TableRow (45) x8
                             Pagination
```

## SummaryGrid — KPI cards (from work-queue.md section 1)
Awaiting Review · Under Review · Information Requested · Decided This Month · **Breaching SLA**.
Each card: label, large count, short context line, icon. The **Breaching SLA** card uses the
warning treatment (`Warning Circle`, red accent). Selecting a card filters the table.

## FiltersRow (section 2)
- Search placeholder: "Search by reference, applicant, or subject…"
- Dropdowns: Originating service · Status · Age / SLA state · Channel (transaction vs escrow — C&E Auditor only).
- Default sort = **SLA urgency** (adopting the confirmed FTI-queue precedent), not recency.

## QueueTable columns (section 3)
Reference · Originating service (e.g. "RED #1 Register Initial Sale") · Applicant ·
Subject (project / property / title / practitioner) · **Status** (`Badge`) · **Age / SLA**
(countdown; amber = approaching, red = breached).
Row click → opens **Application Review**. No decision control lives on this screen.

**Status badge values** (status-badges.md section 1 — do not localise):
`Under Review` · `Information Requested` · `Returned` · `Approved` · `Rejected`.
Proposed colour intent (bind to library tokens in Figma): Under Review = neutral/info ·
Information Requested = attention/amber · Returned = warning/amber · Approved = success/green ·
Rejected = danger/red.

## Queue-type views (one screen, swap columns/content — do not build separate layouts)
- **Transaction** (C&E Auditor) — the default above.
- **Escrow / Trust** (C&E Auditor) — add an **Escrow flag** column (trustee-assessment received);
  only shows items past the FTI trustee gate.
- **Licensing** (Licensing & Registration Officer) — replace the escrow column with **Credential type**;
  sidebar shows the Licensing variant (adds National Practitioner Register).

## Notes / guards
- Breaching SLA is computed against each item's **originating-service** SLA, not one queue-wide timer.
- Auto-approval licensing items do not appear here.
- Status text is owned by status-badges.md section 1 — do not introduce local status words.
