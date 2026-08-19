---
project: RERAN
module: real-estate-developer
type: reference-sample
status: draft
contains_proposals: true
written_against_specs_on: 2026-08-19
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/dashboard.md"
  - "RERAN/modules/real-estate-developer/ui/screens/projects.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registrations.md"
  - "RERAN/modules/real-estate-developer/ui/screens/sales-and-disclosures.md"
  - "RERAN/modules/real-estate-developer/ui/screens/escrow-management.md"
  - "RERAN/modules/real-estate-developer/ui/screens/applications.md"
  - "RERAN/modules/real-estate-developer/ui/screens/payment-history.md"
  - "RERAN/modules/real-estate-developer/ui/screens/documents.md"
  - "RERAN/modules/real-estate-developer/ui/screens/reports.md"
  - "RERAN/modules/real-estate-developer/ui/screens/company-profile.md"
  - "RERAN/modules/real-estate-developer/ui/screens/notifications.md"
  - "RERAN/modules/real-estate-developer/ui/screens/help-and-support.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/financial-trust-institutions/ui/figma-prompts/nav-sidebar-landing-screens.md"
tags:
  - real-estate-developer
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in [`../screens/`](../screens/); where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Sidebar Landing Screens

**Module:** Real Estate Developer (RERAN Group B)
**Screens:** 12, namespaced `NAV – 01` … `NAV – 12`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## What this covers

The first screen a user lands on after clicking each sidebar item.

| Sidebar item | Landing screen | Prompt |
| :--- | :--- | :--- |
| Dashboard | Dashboard | `NAV – 01` |
| Projects | Projects | `NAV – 02` |
| Property Registrations | Property Registrations | `NAV – 03` |
| Sales & Disclosures | Sales & Disclosures | `NAV – 04` |
| Escrow Management | Escrow Management | `NAV – 05` |
| Applications | Applications | `NAV – 06` |
| Payment History | Payment History | `NAV – 07` |
| Documents | Documents | `NAV – 08` |
| Reports | Reports | `NAV – 09` |
| Company Profile | Company Profile | `NAV – 10` |
| Notifications | Notifications | `NAV – 11` |
| Help & Support | Help & Support | `NAV – 12` |

**Deviation from Group C's pack, deliberate:** Group C's equivalent pack skips Dashboard because it was already built as screen #1 before that pack existed. Nothing in RED has been built yet except the `RED-Sidebar` component itself — so Dashboard is included here as `NAV – 01`, not held back.

---

## Shared structure

Nine of the twelve follow one shape: **Top Bar → Summary Cards → Filters & Search → Table → [a domain-specific insights section] → Pagination**. Build `NAV – 06` (Applications) first — it's the screen this module's own [`components.md`](../components.md) treats as the template every other list screen follows — and the rest inherit its layout cleanly.

Three exceptions don't follow this shape: `NAV – 01` Dashboard (its own multi-section layout, no single table), `NAV – 10` Company Profile (no context header strip — the page's own Institution Standing card, here "Company Standing," *is* that information, shown as the subject of the page), and `NAV – 12` Help & Support (no table at all).

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | **List state only, no detail panel open** | Projects, Property Registrations, Sales & Disclosures, Escrow Management, Documents and Payment History each link out to a `-details.md` screen. These prompts show the default list state; the detail screens are follow-up prompts, not built here. |
| 2 | **All data is organization-wide, never role-filtered** | The unified-access model (`navigation.md`, confirmed 2026-08-15). No screen hides rows, greys actions, or shows "not available to your role." |
| 3 | **Sample data is invented for this pack, not drawn from a built screen** | Unlike Group C's pack, RED has no built Dashboard to draw consistent figures from. A full data set is invented once below and held identical across all twelve screens instead. |
| 4 | **Sample data deliberately overlaps Group C's own pack where the two modules describe the same real-world records** | Crestwood Developments, Banana Island Villas, Lekki Pearl Estate, and escrow accounts `TRA-0041` / `TRA-0029` all appear in Group C's built `escrow-request-queue.md` sample data. Reusing them here — from RED's own side of the same transactions — makes the platform read as one coherent system across modules rather than two unrelated demos. Everything else is newly invented for this pack. |
| 5 | **Payment timing genuinely varies by service, not assumed uniform** | Unlike Group C's pack (which flagged a since-corrected assumption that timing was uniform everywhere), RED's Payment Timing column reflects the real per-service split confirmed in PR #59's audit — before-decision, after-decision, and one dual-stage service, each shown in the sample data. |
| 6 | **Empty states are not drawn as separate screens** | Each spec defines one; twelve extra empty-state frames is disproportionate. Add them per screen later if wanted. |

---

## Shared sample data

Invented for this pack (Assumption 3), held identical across all twelve screens.

- **Company:** Crestwood Developments Ltd. · `DEV-2024-00437` · RERA License Status: Active · expires 15 Nov 2027
- **Logged-in user:** Adaeze Nwosu — Project Registration Officer *(the same name `navigation.md`'s own Audit-Trail Principle example uses)*
- **Staff:** Oluwaseun Bankole (Developer Principal / Director) · Adaeze Nwosu (Project Registration Officer) · Ifeoma Chukwu (Sales & Disclosure Officer) · Tunde Adebayo (Escrow Liaison) · 9 on roster, 1 invited
- **Projects:** `PRJ-2026-0014` Banana Island Villas, Lagos, Residential, Active, Construction, 62% · `PRJ-2026-0019` Lekki Pearl Estate, Lagos, Residential, Active, Construction, 78% · `PRJ-2026-0022` Gwarinpa Heights, Abuja, Mixed Use, Under Review, Planning, 8%
- **Property registrations:** `REG-2026-0301` Unit A-120, Banana Island Villas, Apartment, Approved · `REG-2026-0308` Unit B-204, Lekki Pearl Estate, Apartment, Under Review · `REG-2026-0312` Retail Unit R-02, Gwarinpa Heights, Commercial, Draft
- **Sales:** `SALE-2026-0087` Unit A-120, Banana Island Villas, buyer John Smith, Sold, Disclosure Approved · `SALE-2026-0091` Unit B-204, Lekki Pearl Estate, buyer Blessing Okafor, Reserved, Disclosure Draft · `SALE-2026-0079` Unit A-118, Banana Island Villas, buyer Emeka Nwachukwu, Completed, Disclosure Approved
- **Escrow accounts:** `ESC-RED-0041` Banana Island Villas, First Bank of Nigeria, account `TRA-0041`, balance ₦210,400,000, milestone Structural completion, Active · `ESC-RED-0029` Lekki Pearl Estate, First Bank of Nigeria, account `TRA-0029`, balance ₦148,900,000, milestone Roofing complete, Active
- **Fund releases:** `FR-2026-0087` Banana Island Villas, ₦85,000,000, Structural completion, requested 8 Aug 2026, Trustee Review · `FR-2026-0094` Lekki Pearl Estate, ₦62,500,000, Roofing complete, requested 15 Aug 2026, Submitted
- **Applications:** `APP-2026-0221` #13 Register Real Estate Project (Gwarinpa Heights, Under Review) · `APP-2026-0219` #1 Register Initial Sale (Unit A-120, Approved) · `APP-2026-0217` #8 Activate Escrow Account (Banana Island Villas, Approved) · `APP-2026-0224` #12 Receive Escrow Payment (Banana Island Villas, Under Review) · `APP-2026-0226` #21 Cancel Bank Guarantee (Lekki Pearl Estate, Information Requested) · `APP-2026-0228` #6 Register Mortgage-Linked Sale (Unit B-204, Returned) · `APP-2026-0189` #24 Register/Amend Project Details (Banana Island Villas, Approved) · `APP-2026-0201` #17 Re-Register Real Estate Project (Apo Green Residences, an older completed project, Approved)
- **Payments:** see `NAV – 07` for the full table — drawn from the applications above plus a few older ones for variety.

---

## NAV – 01 · Dashboard

```
Create a new screen frame named "NAV – 01 Dashboard", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 01 Dashboard
  - RED-Sidebar       (instance of the existing sidebar component — do not redraw it; active nav item = "Dashboard")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Dashboard", subtitle "")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, badges, data tables, section headers, icons. Do not invent new colours, type scales, or card treatments. This is the first screen built in this file — establish the white-card-on-grey treatment here; every later screen in this pack matches it.

Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Welcome Banner, full width. Left side: "Welcome back, Adaeze Nwosu", then "Crestwood Developments Ltd." on its own line, then "DEV-2024-00437" in grey, then a green "Verified" badge. Right side: a blue primary button "Register New Project" and a secondary button "View Reports".

2. A grid of KPI Summary Cards, two rows of eight, each card a label, a large figure, and nothing else:
   Row 1: Active Projects — 2 · Draft Projects — 1 · Property Registrations — 18 · Pending Property Registrations — 4 · Applications With RERA — 3 · Returned Applications — 1 · Approved Applications — 4 · Active Sales Listings — 5
   Row 2: Sales Awaiting Disclosure — 2 · Active Escrow Accounts — 2 · Pending Fund Releases — 2 · Milestones Under Review — 2 · Documents Awaiting Action — 3 · Compliance Issues — 1 · Due This Week — 5 · Completed This Month — 6

3. Card — "Quick Actions". Three columns under small uppercase grey sub-headings:
   CREATE — Register New Project · Register Property · Record Property Sale · Create Sales Disclosure · Register Escrow Account · Request Fund Release · Submit Application
   RESPOND — Upload Documents · Upload Buyer Documents · Upload Escrow Documents · Respond to RERA Query · View Returned Items
   REVIEW — View Projects · View Property Registrations · Review Sales & Disclosures · View Escrow Status · Review Applications · Generate Reports

4. Card — "Requiring Action". A short prioritized list, not a table — four rows, each with a small coloured priority dot, the record reference as a link, one line describing what's waiting, and a right-aligned "waiting X" duration:
   APP-2026-0226 — #21 Cancel Bank Guarantee — RERA has requested information — waiting 1 day
   APP-2026-0228 — #6 Register Mortgage-Linked Sale — Returned for correction — waiting 4 hours
   FR-2026-0087 — Fund release for Banana Island Villas — Awaiting Trustee Review response — waiting 9 days
   REG-2026-0312 — Retail Unit R-02 registration — Draft, not yet submitted — waiting 3 days

5. A row of four Focus Area cards, each with a small heading, three or four summary lines, and a "View all" link at the bottom:
   "Projects & Registrations" — Active 2 · Draft 1 · Under Review 1 · Approved 4 (registrations) — links to Projects
   "Sales & Disclosures" — Active Listings 5 · Units Sold 12 · Pending Disclosures 2 · Buyer Documents Pending 1 — links to Sales & Disclosures
   "Escrow & Fund Releases" — Active Accounts 2 · Pending Releases 2 · Completed Releases 7 — with a highlighted sub-line "Oldest pending: FR-2026-0087, 9 days" — links to Escrow Management
   "Compliance & Standing" — Compliance Issues 1 · Open RERA Requests 2 · License Status: Active — links to Applications, Documents and Company Profile

6. Card — "Upcoming Deadlines". A simple list, four rows, each a date, a short description, and a small priority badge:
   Aug 18, 2026 — Respond to bank guarantee cancellation query (APP-2026-0226) — High
   Aug 20, 2026 — Trust account statement due (TRA-0029) — Medium
   Aug 22, 2026 — Structural milestone re-inspection (Banana Island Villas) — Medium
   Aug 25, 2026 — Gwarinpa Heights survey document expires — Low

7. Card — "Organization Activity". A compact activity feed, five rows, each showing who acted, what role they held, what happened, and a relative timestamp:
   Adaeze Nwosu (Project Registration Officer) — Submitted Gwarinpa Heights for registration — 2 days ago
   Ifeoma Chukwu (Sales & Disclosure Officer) — Filed sales disclosure for Unit A-120 — 3 days ago
   Tunde Adebayo (Escrow Liaison) — Requested fund release for Banana Island Villas — 9 days ago
   Oluwaseun Bankole (Developer Principal / Director) — Reviewed Q2 organizational report — 4 days ago
   Tunde Adebayo (Escrow Liaison) — Uploaded bank confirmation letter for Lekki Pearl Estate — 5 days ago

Every card, action, and Focus Area is visible to every user — this module has no role-based gating anywhere. Do not add a role switcher or "assigned to you" scoping to any list on this screen.
```

---

## NAV – 02 · Projects

```
Create a new screen frame named "NAV – 02 Projects", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 02 Projects
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Projects", subtitle "Register, track and monitor the organization's development projects.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — summary cards, filter bars, data tables, status pills, pagination, buttons. Do not invent new colours, type scales, or card treatments. Match the treatment established on the Dashboard.

Keep it simple: one row of summary cards, one filter bar, one table, one insights card. No charts, no illustrations.

Workspace content, top to bottom:

1. A row of ten summary cards (allow two rows of five if a single row is too tight), each a label, a figure, and nothing else:
   Total Projects — 3 · Draft Projects — 0 · Submitted Projects — 1 · Under Review — 1 · Information Requested — 0 · Returned Projects — 0 · Approved Projects — 2 · Active Projects — 2 · Suspended Projects — 0 · Completed Projects — 0

2. Filter bar, full width: search input placeholder "Search project...", followed by dropdowns — Project Status · Development Type · Location · Registration Stage · Date Range. Show "Registration Stage: All" as the selected value on the fourth dropdown.

3. Card — "Projects". Card header: heading on the left with a grey counter "3 projects"; on the right a secondary text action "Export Selected" and "Download Summary", and a blue primary button "Register New Project".
   Table with columns: Project ID · Project Name · Development Type · Location · Current Status · Development Stage · Progress · Last Updated · Action
   Project ID cells are blue links. Progress shows a small horizontal progress bar with a percentage. Action is a light-blue "View" button.

     PRJ-2026-0014 — Banana Island Villas — Residential — Lagos — Active — Construction — 62% — Aug 16, 2026 — View
     PRJ-2026-0019 — Lekki Pearl Estate — Residential — Lagos — Active — Construction — 78% — Aug 15, 2026 — View
     PRJ-2026-0022 — Gwarinpa Heights — Mixed Use — Abuja — Under Review — Planning — 8% — Aug 17, 2026 — View

   Give PRJ-2026-0022's Current Status pill the "Under Review" treatment, distinct from the "Active" pill on the other two rows.

4. Card — "Portfolio Insights". Two side-by-side sub-cards:
   "Project Distribution" — a simple horizontal bar breakdown by development stage: Planning 1 · Construction 2 · Completed 0. And by type: Residential 2 · Mixed Use 1.
   "Organizational Performance" — three lines: Average Progress Across Active Projects: 70% · Projects On Schedule: 2 of 2 · This Quarter: 1 new project registered.
   Beneath both, a text link "View full reports →".

5. Pagination row beneath the table, right-aligned: "Showing 1–3 of 3".
```

---

## NAV – 03 · Property Registrations

```
Create a new screen frame named "NAV – 03 Property Registrations", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 03 Property Registrations
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Property Registrations", subtitle "Register properties and units, and track their regulatory status.")
    - Workspace

Reuse the layout and every component established on the Projects screen — summary cards, filter bar, data table, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Projects. No charts, no illustrations.

Workspace content, top to bottom:

1. A row of summary cards: Total Registrations — 12 · Draft Registrations — 2 · Submitted — 3 · Under Review — 2 · Information Requested — 1 · Returned — 0 · Approved — 4 · Rejected — 0 · Registered This Month — 3

2. Filter bar, full width: search input placeholder "Search property...", followed by dropdowns — Project · Property Type · Registration Status · Date Range.

3. Card — "Property Registrations". Card header: heading on the left with a grey counter "12 registrations"; on the right "Export Selected", "Download Registration Summary", and a blue primary button "Register New Property".
   Table with columns: Registration No. · Property ID · Property Name / Unit · Project · Property Type · Submitted Date · Current Status · Last Updated · Action
   Registration No. cells are blue links. Action is a light-blue "View" button.

     REG-2026-0301 — PROP-00301 — Unit A-120 — Banana Island Villas — Apartment — Aug 4, 2026 — Approved — Aug 12, 2026 — View
     REG-2026-0308 — PROP-00308 — Unit B-204 — Lekki Pearl Estate — Apartment — Aug 13, 2026 — Under Review — Aug 15, 2026 — View
     REG-2026-0312 — PROP-00312 — Retail Unit R-02 — Gwarinpa Heights — Commercial — — — Draft — Aug 17, 2026 — View

   REG-2026-0312's Submitted Date cell is empty — a draft has not been submitted yet. Give its Current Status pill the "Draft" treatment, distinct from "Approved" and "Under Review".

4. Card — "Registration Insights". Two side-by-side sub-cards:
   "Registration Performance" — Approval Rate: 92% · Average Approval Time: 7 days · Registrations This Quarter: 5 · Pending Reviews: 3.
   "Registration Distribution" — Residential 9 · Commercial 2 · Mixed Use 1 · Industrial 0.

5. Pagination row beneath the table, right-aligned: "Showing 1–3 of 12".
```

---

## NAV – 04 · Sales & Disclosures

```
Create a new screen frame named "NAV – 04 Sales and Disclosures", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 04 Sales and Disclosures
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Sales & Disclosures")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Sales & Disclosures", subtitle "Record property sales and file the disclosures RERA requires for each.")
    - Workspace

Reuse the layout and every component established on the Projects screen — summary cards, filter bar, data table, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Projects. Two page actions instead of one. No charts, no illustrations.

Workspace content, top to bottom:

1. A row of summary cards: Total Sales — 12 · Draft Sales — 1 · Active Listings — 5 · Sales Awaiting Disclosure — 2 · Draft Disclosures — 1 · Submitted Disclosures — 4 · Under Review — 1 · Returned Disclosures — 0 · Approved Disclosures — 6 · Total Sales Value — ₦1,840,000,000 · This Month's Sales — 2

2. Filter bar, full width: search input placeholder "Search property or buyer...", followed by dropdowns — Project · Property Type · Sales Status · Disclosure Status · Date Range.

3. Card — "Sales & Disclosures". Card header: heading on the left with a grey counter "12 sales"; on the right "Export Selected", "Download Summary", a secondary button "Record Property Sale", and a blue primary button "Create Sales Disclosure".
   Table with columns: Sale Reference · Property · Project · Buyer · Sale Date · Sale Value · Current Status · Current Stage · Disclosure Status · Last Updated · Action
   Sale Reference cells are blue links. Two separate status pills appear per row — Current Status and Disclosure Status — using visually distinct pill colours so the two axes read as separate values, not one. Action is a light-blue "View" button.

     SALE-2026-0087 — Unit A-120 — Banana Island Villas — John Smith — Aug 3, 2026 — ₦185,000,000 — Sold — Documentation — Approved — Aug 12, 2026 — View
     SALE-2026-0091 — Unit B-204 — Lekki Pearl Estate — Blessing Okafor — Aug 12, 2026 — ₦142,000,000 — Reserved — Disclosure Preparation — Draft — Aug 14, 2026 — View
     SALE-2026-0079 — Unit A-118 — Banana Island Villas — Emeka Nwachukwu — Jul 2, 2026 — ₦179,500,000 — Completed — Closed — Approved — Jul 20, 2026 — View

4. Card — "Sales Analytics". Two side-by-side sub-cards:
   "Sales Performance" — Sales This Month: 2 · Sales This Quarter: 6 · Average Sale Value: ₦168,700,000 · Total Revenue: ₦1,840,000,000.
   "Disclosure Compliance" — Compliance Rate: 94% · Pending Disclosures: 2 · Average Approval Time: 5 days · Returned Cases: 0.

5. Pagination row beneath the table, right-aligned: "Showing 1–3 of 12".
```

---

## NAV – 05 · Escrow Management

```
Create a new screen frame named "NAV – 05 Escrow Management", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 05 Escrow Management
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Escrow Management")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Escrow Management", subtitle "Monitor project escrow accounts and manage milestone-based fund releases.")
    - Workspace

Reuse the layout and every component established on the Projects screen — summary cards, filter bar, data table, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Projects. Two page actions. No charts, no illustrations.

IMPORTANT: the balances on this screen are the developer's own project escrow account — a real, regulated product feature — not a RERA-fee account. Do not add any note, badge, or warning implying these balances relate to RERA service fees; that is a fully separate mechanism covered on the Payment History screen.

Workspace content, top to bottom:

1. A row of eight summary cards: Active Escrow Accounts — 2 · Total Escrow Balance — ₦359,300,000 · Pending Fund Releases — 2 · Released Funds — ₦412,000,000 · Pending Milestones — 2 · Completed Milestones — 5 · Escrow Compliance — 96% · Financial Institutions — 1

2. Search and filter row: search input placeholder "Search by Escrow ID, project, financial institution or account number...", followed by dropdowns — Escrow Status (All · Pending Registration · Active · Suspended · Closed) · Fund Release Status (All · No Request · Pending Approval · Under Review · Approved · Released · Returned · Rejected) · Project · Financial Institution · Date Range. Show "Sort by: Recently Updated" as the selected sort value.

3. Card — "Escrow Accounts". Card header: heading on the left with a grey counter "2 accounts"; on the right "Export Selected", "Generate Summary Report", a secondary button "Register Escrow Account", and a blue primary button "Request Fund Release".
   Table with columns: Escrow ID · Project · Financial Institution · Escrow Account Number · Escrow Balance · Current Milestone · Last Fund Release · Escrow Status · Release Status · Last Updated · Action
   Escrow ID cells are blue links. Action is a light-blue "View" button.

     ESC-RED-0041 — Banana Island Villas — First Bank of Nigeria — TRA-0041 — ₦210,400,000 — Structural completion — — — Active — Trustee Review — Aug 16, 2026 — View
     ESC-RED-0029 — Lekki Pearl Estate — First Bank of Nigeria — TRA-0029 — ₦148,900,000 — Roofing complete — ₦38,000,000 (Foundation) — Active — Submitted — Aug 15, 2026 — View

4. Card — "Fund Release Overview". Table with columns: Milestone · Planned Date · Actual Date · Release Amount · Status
     Structural completion (Banana Island Villas) — Aug 5, 2026 — — — ₦85,000,000 — Trustee Review
     Roofing complete (Lekki Pearl Estate) — Aug 12, 2026 — — — ₦62,500,000 — Submitted
     Foundation (Lekki Pearl Estate) — Jun 10, 2026 — Jun 14, 2026 — ₦38,000,000 — Released

5. Card — "Escrow Analytics". Two side-by-side sub-cards:
   "Financial Summary" — Total Escrow Value: ₦359,300,000 · Released This Month: ₦0 · Pending Release Value: ₦147,500,000 · Average Release Time: 12 days.
   "Compliance Summary" — Milestones On Schedule: 4 of 5 · Delayed Milestones: 1 · Pending Reviews: 2 · Compliance Score: 96%.

6. Pagination row beneath the Escrow Accounts table, right-aligned: "Showing 1–2 of 2".
```

---

## NAV – 06 · Applications

```
Create a new screen frame named "NAV – 06 Applications", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 06 Applications
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Applications", subtitle "Track, manage and respond to every regulatory application your organization has submitted to RERA.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — summary cards, filter bars, data tables, status pills, pagination, buttons. Do not invent new colours, type scales, or card treatments. Match the treatment established on the Dashboard and Projects screens.

Keep it simple: one row of summary cards, one filter bar, one table, one pending-actions table, one analytics card, one activity feed. No charts, no illustrations.

This screen establishes the layout every other list screen in this pack reuses — build it carefully.

Workspace content, top to bottom:

1. A row of ten summary cards: Total Applications — 8 · Draft Applications — 0 · Submitted — 1 · Under Review — 2 · Information Requested — 1 · Returned — 1 · Approved — 4 · Rejected — 0 · Due This Week — 2 · Average Approval Time — 9 days

2. Filter bar, full width: search input placeholder "Search anything...", followed by dropdowns — Application Type (registration · property · sales disclosure · escrow · licensing · title deed) · Project · Property · Status · Assigned RERA Unit · Date Range.

3. Card — "Applications". Card header: heading on the left with a grey counter "8 applications"; on the right a blue primary button "Submit New Application".
   Table with columns: Application ID · Application Type · Related Project · Related Property · Buyer · Submitted By · Submitted Date · Current Status · Assigned RERA Unit · Last Updated · Action
   Application ID cells are blue links. Submitted By shows the person's name with a small grey role label beneath it (e.g. "Adaeze Nwosu" / "Project Registration Officer"). Action varies by status — Draft rows show "Continue"; Submitted/Under Review show "View Details"; Information Requested shows "Respond"; Returned shows "Correct Issues"; Approved shows "View Details".

     APP-2026-0221 — #13 Register Real Estate Project — Gwarinpa Heights — — — Adaeze Nwosu / Project Registration Officer — Aug 15, 2026 — Under Review — Project Registration Unit — Aug 17, 2026 — View Details
     APP-2026-0219 — #1 Register Initial Sale — — — Unit A-120 — — Ifeoma Chukwu / Sales & Disclosure Officer — Aug 10, 2026 — Approved — Sales Registry Unit — Aug 12, 2026 — View Details
     APP-2026-0217 — #8 Activate Escrow Account — Banana Island Villas — — — — Tunde Adebayo / Escrow Liaison — Aug 5, 2026 — Approved — Escrow Compliance Unit — Aug 9, 2026 — View Details
     APP-2026-0224 — #12 Receive Escrow Payment — Banana Island Villas — — — — Tunde Adebayo / Escrow Liaison — Aug 8, 2026 — Under Review — Escrow Compliance Unit — Aug 17, 2026 — View Details
     APP-2026-0226 — #21 Cancel Bank Guarantee — Lekki Pearl Estate — — — — Tunde Adebayo / Escrow Liaison — Aug 16, 2026 — Information Requested — Escrow Compliance Unit — Aug 17, 2026 — Respond
     APP-2026-0228 — #6 Register Mortgage-Linked Sale — — — Unit B-204 — Blessing Okafor — Ifeoma Chukwu / Sales & Disclosure Officer — Aug 14, 2026 — Returned — Sales Registry Unit — Aug 15, 2026 — Correct Issues
     APP-2026-0189 — #24 Register/Amend Project Details — Banana Island Villas — — — — Adaeze Nwosu / Project Registration Officer — Jul 20, 2026 — Approved — Project Registration Unit — Jul 29, 2026 — View Details
     APP-2026-0201 — #17 Re-Register Real Estate Project — Apo Green Residences — — — — Oluwaseun Bankole / Developer Principal / Director — Jun 2, 2026 — Approved — Project Registration Unit — Jun 20, 2026 — View Details

   Give the APP-2026-0226 row's SLA-relevant cell (Last Updated) an amber highlight — it has been awaiting a developer response for 1 day.

4. Card — "Pending Actions". Table with columns: Application · Required Action · Due Date · Priority · Action
     APP-2026-0226 — Respond to RERA query — Aug 19, 2026 — High — Respond
     APP-2026-0228 — Correct and resubmit — Aug 22, 2026 — Medium — Correct Issues

5. Card — "Application Analytics". Two side-by-side sub-cards:
   "Approval Performance" — Approval Rate: 88% · Average Processing Duration: 9 days · Applications This Quarter: 14.
   "Volume by Status" — a simple horizontal bar breakdown: Under Review 2 · Approved 4 · Information Requested 1 · Returned 1.

6. Card — "Recent Regulatory Activities". Activity feed, four rows: submission, decision, information request, resubmission events, most recent first, each with actor, role, action and timestamp.

7. Pagination row beneath the Applications table, right-aligned: "Showing 1–8 of 8".
```

---

## NAV – 07 · Payment History

```
Create a new screen frame named "NAV – 07 Payment History", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 07 Payment History
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Payment History")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment History", subtitle "Every RERA service fee paid by the company, by transaction.")
    - Workspace

Reuse the layout and every component established on the Applications screen — summary cards, filter bar, data table, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Applications. Show the default list state only — not the receipt detail panel.

IMPORTANT: this screen must show NO account balance anywhere. There is no standing account and nothing to fund — every figure here is a fact about a transaction that already happened. Do not add a balance card, a top-up action, or a low-balance warning.

Workspace content, top to bottom:

1. A row of four summary cards: Paid This Month — ₦80,500 — Successful payments · Payments Failed — 1 — Retryable from originating application · Refunds Requested — 1 — Under review · Refunds Completed This Month — 2 — ₦33,500

2. Filter bar, full width: search input placeholder "Search by application, receipt or reference...", followed by dropdowns — Service · Status (Successful · Failed · Refund Requested · Refunded) · Payment Timing (Before Decision · After Decision · Dual-Stage) · Date Range · Amount Range. Show "Sort by: Most recent" as the selected value.

3. Card — "Payments". Card header: heading on the left with a grey counter "7 payments"; on the right a secondary text action "Export Selected".
   Table with columns: Receipt Reference · Application Reference · Service · Timing · Amount · Method · Paid · Status · Action
   Receipt and Application cells are blue links. Action shows two inline text links, "View Receipt" and "View Application" — except on the Failed row, which shows only "View Application", since there is no receipt for a payment that did not settle.

     RCT-2026-0533 — APP-2026-0219 — #1 Register Initial Sale — Before Decision — ₦42,000 — Card — Aug 10, 2026, 3:14 PM — Successful — View Receipt / View Application
     RCT-2026-0529 — APP-2026-0228 — #6 Register Mortgage-Linked Sale — Before Decision — ₦38,500 — Bank Transfer — Aug 14, 2026, 10:02 AM — Successful — View Receipt / View Application
     RCT-2026-0518 — APP-2026-0201 — #17 Re-Register Real Estate Project — After Decision — ₦58,000 — Bank Transfer — Jun 20, 2026, 1:47 PM — Successful — View Receipt / View Application
     RCT-2026-0506 — APP-2026-0189 — #24 Register/Amend Project Details — Dual-Stage · Stage 2 — ₦45,000 — Card — Jul 29, 2026, 4:12 PM — Successful — View Receipt / View Application
     RCT-2026-0505 — APP-2026-0189 — #24 Register/Amend Project Details — Dual-Stage · Stage 1 — ₦20,000 — Card — Jul 21, 2026, 9:30 AM — Successful — View Receipt / View Application
     RCT-2026-0498 — APP-2026-0176 — #19 Terminate Initial Registration — Before Decision — ₦15,000 — Card — Jun 3, 2026, 11:20 AM — Failed — View Application
     RCT-2026-0490 — APP-2026-0154 — #22 Real Estate Licensing Application — After Decision — ₦125,000 — Card — May 28, 2026, 2:05 PM — Refund Requested — View Receipt / View Application

   The two RCT-2026-0505 / RCT-2026-0506 rows both reference the same Application Reference (APP-2026-0189) — that application's service, #24, is the one dual-stage service in the module, and pays in two separate transactions. Do not merge them into one row.

4. Pagination row beneath the table, right-aligned: "Showing 1–7 of 7".
```

---

## NAV – 08 · Documents

```
Create a new screen frame named "NAV – 08 Documents", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 08 Documents
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Documents")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Documents", subtitle "Upload, organize and manage every document the organization files with RERA.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — summary cards, filter bars, data tables, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Applications, plus one extra card for category groups. Show the default list state only, not the preview panel. No file thumbnails, no folder tree, no illustrations.

Workspace content, top to bottom:

1. A row of eight summary cards: Total Documents — 214 · Draft Documents — 6 · Pending Verification — 9 · Verified Documents — 178 · Returned Documents — 3 · Rejected Documents — 1 · Missing Required Documents — 4 · Expiring Soon — 5

2. Filter bar, full width: search input placeholder "Search document...", followed by dropdowns — Category · Project · Property · Application · Buyer · Disclosure · Escrow Account · Fund Release · Financial Institution · Verification Status · Expiry Status · Uploaded By · Upload Date Range. Fitting all these in one row will overflow — wrap the dropdowns onto a second line beneath the search input if needed.

3. Card — "Document Categories". Five small labelled groups, shown as compact pill lists rather than a table:
   ORGANIZATION — Company Documents · Regulatory Certificates · Licenses & Permits · Legal Agreements · Financial Documents · Compliance Documents
   PROJECT & REGISTRATION — Project Documents · Property Registration Documents · Technical Documents · Survey Documents · Building Approval Documents · Environmental Documents
   SALES & DISCLOSURE — Sales Agreements · Buyer Identification · Proof of Payment · Mortgage Documents · Corporate Buyer Documents · Power of Attorney · Disclosure Forms
   ESCROW — Escrow Agreement · Bank Confirmation Letter · Engineer Progress Certificate · Quantity Surveyor Report · Construction Progress Report · Site Inspection Report · Fund Release Documents
   OTHER — Supporting Documents · Other

4. Card — "Documents". Card header: heading on the left with a grey counter "214 documents"; on the right a blue primary button "Upload Documents".
   Table with columns: Document Name · Category · Linked Record · Financial Institution · Uploaded By · Upload Date · Verification Status · Expiry Date · Action
   Document Name cells are blue links. Action is a light-blue "Preview" button.

     banana-island-structural-cert.pdf — Engineer Progress Certificate — ESC-RED-0041 — First Bank of Nigeria — Tunde Adebayo — Aug 14, 2026 — Verified — — Preview
     a-120-sale-agreement.pdf — Sales Agreements — SALE-2026-0087 — — Ifeoma Chukwu — Aug 3, 2026 — Verified — — Preview
     gwarinpa-heights-survey-plan.pdf — Survey Documents — PRJ-2026-0022 — — Adaeze Nwosu — Aug 15, 2026 — Pending Verification — — Preview
     bank-guarantee-lekki-pearl.pdf — Bank Confirmation Letter — APP-2026-0226 — First Bank of Nigeria — Tunde Adebayo — Aug 16, 2026 — Information Requested — — Preview
     b-204-buyer-id-blessing-okafor.pdf — Buyer Identification — SALE-2026-0091 — — Ifeoma Chukwu — Aug 12, 2026 — Verified — — Preview
     crestwood-rera-license.pdf — Licenses & Permits — Company Profile — — Oluwaseun Bankole — 15 Nov 2024 — Verified — 15 Nov 2027 — Preview
     gwarinpa-heights-environmental-approval.pdf — Environmental Documents — PRJ-2026-0022 — — Adaeze Nwosu — Aug 10, 2026 — Expiring Soon — 1 Sep 2026 — Preview

   Give the "Expiring Soon" row's Expiry Date an amber highlight, and "Information Requested" a distinct pill treatment from "Verified" and "Pending Verification".

5. Pagination row beneath the table, right-aligned: "Showing 1–7 of 214".
```

---

## NAV – 09 · Reports

```
Create a new screen frame named "NAV – 09 Reports", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 09 Reports
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Reports")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Reports", subtitle "Generate, schedule and download reports across every function.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — summary cards, category card grids, data tables, filter bars, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. No charts beyond what's described below, no illustrations.

Workspace content, top to bottom:

1. A row of four summary cards: Reports Generated This Month — 9 · Scheduled Reports Active — 2 · Saved Report Definitions — 6 · Most-Used Report — "Project Registration Status"

2. Card — "Report Categories". Seven small labelled groups, each report name a plain text link:
   PROJECT REPORTS — Project Progress · Project Completion · Construction Milestones · Development Performance · Project Registration Status · Project Approval Progress · Returned Projects · Registration Timeline
   PROPERTY REPORTS — Property Registrations · Registration Status · Property Inventory · Property Availability · Registration Progress · Approved Properties · Returned Registrations
   SALES & DISCLOSURE REPORTS — Sales Performance · Buyer Statistics · Sales Trends · Disclosure Compliance · Property Sales Register · Sales Value Analysis · Monthly Sales Summary · Disclosure Status Report · Buyer Verification Status
   ESCROW REPORTS — Escrow Balances · Fund Releases · Milestone Progress · Financial Institution Summary · Escrow Account Summary · Active Escrow Accounts · Escrow Status Report
   APPLICATION & REGULATORY REPORTS — Applications · Approval Performance · Processing Time · Compliance Overview · Submitted Applications · Pending Reviews · Registration Compliance · RERA Query Response Time
   DOCUMENT REPORTS — Document Verification · Repository Summary · Missing Documents · Pending Verification · Returned Documents · Expiring Documents
   FINANCIAL REPORTS — Revenue · Escrow Funds · Sales Value · Payment Summary · Property Sales Value · Payment Status Summary

3. Card — "Saved Reports". Table with columns: Report Name · Category · Last Run · Action (Run · Edit · Duplicate · Schedule · Delete, shown as an overflow menu)
     Project Registration Status — Project Reports — Aug 17, 2026 — ⋯
     Monthly Sales Summary — Sales & Disclosure Reports — Aug 1, 2026 — ⋯
     Escrow Status Report — Escrow Reports — Aug 15, 2026 — ⋯

4. Card — "Recent Generated Reports". Table with columns: Report Name · Category · Generated By · Generated — Status
     Q2 Organizational Performance — Executive — Oluwaseun Bankole — Aug 16, 2026 — Completed
     Project Registration Status — Project Reports — Adaeze Nwosu — Aug 17, 2026 — Completed
     Payment Status Summary — Financial Reports — Tunde Adebayo — Aug 10, 2026 — Completed

5. Card — "Scheduled Reports". Table with columns: Report Name · Frequency · Recipients · Next Run · Action (Pause · Edit · Delete)
     Monthly Sales Summary — Monthly — Ifeoma Chukwu, Oluwaseun Bankole — Sep 1, 2026 — ⋯
     Escrow Status Report — Weekly — Tunde Adebayo — Aug 22, 2026 — ⋯

6. Card — "Insights". Two side-by-side sub-cards:
   "Organization Performance" — Overall Approval Rate: 89% · Average Processing Time: 8.4 days · Projects On Schedule: 2 of 3.
   "Operational Insights" — Outstanding Tasks: 3 · Due This Week: 5 · Validation Error Patterns: none flagged this period.
```

---

## NAV – 10 · Company Profile

```
Create a new screen frame named "NAV – 10 Company Profile", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 10 Company Profile
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Company Profile")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Company Profile", subtitle "Manage your organization's registration details, licenses, authorized representatives, and corporate information.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value grids, data tables, section headers. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. No charts, no illustrations, no org chart, no avatars.

IMPORTANT: this screen does NOT use the summary-card-plus-filter-bar layout every other list screen in this pack uses. There is no context header strip — the Company Header and Company Standing information below is the subject of the page, not a strip above it.

Workspace content, top to bottom:

1. Company Header row: left side, the company logo, "Crestwood Developments Ltd." as a large heading, "DEV-2024-00437" beneath it, and a green "Active" status badge. Right side: Organization Type "Limited Liability Company", Member Since "15 Nov 2024", Last Profile Updated "Aug 16, 2026".

2. A row of six summary cards: RERA License Status — Active · Active Projects — 2 · Registered Properties — 12 · Active Escrow Accounts — 2 · Authorized Representatives — 4 · Compliance Score — 96%

3. Card — "Basic Company Information". Two-column label/value grid, two sub-groups side by side:
   ORGANIZATION DETAILS — Company Name: Crestwood Developments Ltd. · Registration Number: DEV-2024-00437 · Company Type: Limited Liability Company · Tax Identification Number: TIN-88213047 · Date of Incorporation: 3 Feb 2018 · Country of Registration: Nigeria
   CONTACT INFORMATION — Official Email: info@crestwooddevelopments.ng · Phone Number: +234 1 280 3312 · Website: www.crestwooddevelopments.ng · Customer Support Contact: support@crestwooddevelopments.ng

4. Card — "RERA Registration". Two-column grid: Developer Registration Number: DEV-2024-00437 · Registration Date: 15 Nov 2024 · License Number: RERA-DEV-2024-00437 · License Status: Active · Expiry Date: 15 Nov 2027 · Renewal Status: Not Due · Assigned RERA Office: Lagos Regional Office

5. Card — "Corporate Information". Two-column grid: Legal Entity Name: Crestwood Developments Limited · Parent Company: — · Business Category: Real Estate Development · Share Capital: ₦500,000,000 · Number of Employees: 62 · Primary Business Activity: Residential and mixed-use property development

6. Card — "Authorized Representatives". Card header: heading on the left with a grey counter "4 representatives". Table with columns: Name · Position · Role · Authorization Status · Appointment Date · Action
     Oluwaseun Bankole — Managing Director — Developer Principal / Director — Active — 15 Nov 2024 — View Details
     Adaeze Nwosu — Registrations Manager — Project Registration Officer — Active — 15 Nov 2024 — View Details
     Ifeoma Chukwu — Sales Manager — Sales & Disclosure Officer — Active — 8 Jan 2025 — View Details
     Tunde Adebayo — Finance & Escrow Manager — Escrow Liaison — Active — 8 Jan 2025 — View Details

7. Card — "Office Locations". Four small cards in a row, each with: Office Name, Office Type, Address, City, State, Contact Number, Office Manager:
     Head Office — Head Office — 14 Adeola Odeku Street — Lagos — Lagos State — +234 1 280 3312 — Oluwaseun Bankole
     Banana Island Project Office — Project Office — Plot 22, Banana Island — Lagos — Lagos State — +234 1 280 3319 — Adaeze Nwosu

8. Card — "Banking & Escrow Information". Two sub-groups:
   BANKING INFORMATION — Primary Bank: First Bank of Nigeria · Account Name: Crestwood Developments Ltd. · Account Number: •••• 4471 · SWIFT Code: FBNINGLA
   ESCROW INFORMATION — Linked Financial Institutions: First Bank of Nigeria · Active Escrow Accounts: 2 · Total Escrow Value: ₦359,300,000 · Latest Escrow Activity: Fund release requested, Aug 15, 2026
   Beneath, a secondary button "View Escrow Management".

9. Card — "Company Documents". Table with columns: Document · Category · Verification Status · Expiry Date · Action
     Certificate of Incorporation — Certificate of Incorporation — Verified — — View
     RERA Developer License — RERA License — Verified — 15 Nov 2027 — View
     Tax Clearance Certificate — Tax Certificate — Verified — 31 Dec 2026 — View

10. Card — "Organization Settings". Two-column grid: Organization Time Zone: WAT (UTC+1) · Default Language: English · Notification Preferences: Email + In-App · Preferred Communication Method: Email · Report Delivery Preference: Monthly, by Email · Default Currency: NGN (₦)
    Beneath, a single-line inline notice using the existing subtle notice style: "Every representative has identical system access. Role is recorded for audit-trail attribution and does not restrict what a user can do."

11. Card — "Audit Information". Two-column grid: Profile Created On: 15 Nov 2024 · Created By: Oluwaseun Bankole · Last Updated: Aug 16, 2026 · Last Updated By: Adaeze Nwosu
    Beneath, a secondary button "View Complete Audit History".

Page-level actions, top right of the Top Bar: secondary buttons "Edit Company Profile", "Download Company Profile", "View Audit Log".
```

---

## NAV – 11 · Notifications

```
Create a new screen frame named "NAV – 11 Notifications", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 11 Notifications
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Notifications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Notifications", subtitle "Alerts across the organization.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, filter chips, the activity-row pattern from the Dashboard, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: one row of summary cards, one row of filter chips, one priority section, one list. No illustrations, no icons per notification beyond a small priority dot.

Workspace content, top to bottom:

1. A row of seven summary cards: Total Notifications — 34 · Unread — 6 · High Priority — 3 · Action Required — 4 · Due This Week — 5 · Read — 26 · Archived — 2

2. A row of filter chips, left-aligned: All (selected) · Unread · Regulatory · Project & Registration · Sales & Disclosure · Escrow · Documents & System. On the right of the same row, a secondary text action "Mark All Read".

3. Card — "Priority Notifications". Two rows, each with a small coloured priority dot, bold title text, one grey line of detail, and a primary + secondary action:
     Information Requested — Bank guarantee cancellation query on APP-2026-0226 — "RERA has requested supporting documentation" — Respond / View Application
     Milestone Overdue — Structural completion re-inspection for Banana Island Villas is 2 days overdue — "Schedule re-inspection to avoid delaying the pending fund release" — Schedule Inspection / View Escrow Account

4. Card — "Notifications". A table, one row per notification, columns: Notification · Type · Related Record · Priority · Received · Status · Action
     Bank guarantee query received — Regulatory · Information Requested — APP-2026-0226 — High — 1 day ago — Unread — Open
     Mortgage-linked sale returned for correction — Project & Registration — APP-2026-0228 — High — 2 days ago — Unread — Open
     Fund release awaiting Trustee Review — Escrow — FR-2026-0087 — Medium — 9 days ago — Unread — Open
     Sales disclosure approved — Sales & Disclosure — SALE-2026-0087 — Low — 3 days ago — Read — Open
     Gwarinpa Heights environmental approval expiring — Documents & System — PRJ-2026-0022 — Medium — 4 days ago — Unread — Open
     Escrow account activated — Escrow — ESC-RED-0041 — Low — 12 days ago — Read — Open
     Payment confirmation — Register Initial Sale fee — Documents & System — APP-2026-0219 — Low — 7 days ago — Read — Open
     Scheduled maintenance notice — Documents & System — — — Low — 1 day ago — Unread — Open

5. Card — "Upcoming Deadlines". List, three rows, each a date, description, and a small priority badge:
   Aug 19, 2026 — Respond to bank guarantee cancellation query — High
   Aug 20, 2026 — Trust account statement due (TRA-0029) — Medium
   Aug 22, 2026 — Structural milestone re-inspection — Medium

6. Card — "Pinned Announcements". One row: "Scheduled maintenance: 24 Aug 2026, 01:00–03:00 WAT" with a small grey pin icon.

7. Pagination row beneath the Notifications table, right-aligned: "Showing 1–8 of 34".
```

---

## NAV – 12 · Help & Support

```
Create a new screen frame named "NAV – 12 Help and Support", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 12 Help and Support
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Help & Support")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Help & Support", subtitle "Knowledge base, support tickets, training resources and RERA contact routes.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, summary cards, search inputs, data tables, the quick-actions tile pattern from the Dashboard. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. No illustrations, no hero image, no chat bubble graphic, no video thumbnails.

Workspace content, top to bottom:

1. A row of four summary cards: Open Tickets — 2 · Resolved This Month — 5 · Average Response Time — 6 hours · Unread Announcements — 1

2. Card — "Quick Actions". Four items in a row, each a short text label: Create Support Ticket · Search Knowledge Base · Contact RERA Support · View Training Resources

3. Card — "Search the Knowledge Base". A single large full-width search input with a magnifier icon, placeholder "Search help articles...". Nothing else in this card.

4. Card — "Quick Help". A grid of nine compact tiles, each a short text label only, no icons:
   Registering a project · Registering a property · Recording a sale · Filing a disclosure · Activating an escrow account · Requesting a fund release · Uploading documents · Responding to a RERA query · Making a payment

5. Card — "Knowledge Base Articles". Card header: heading on the left, a "View All" link on the right. A two-column list of article titles grouped under small uppercase grey sub-headings:
   PROJECTS & REGISTRATIONS — Registering a new development project · Correcting a returned property registration · Understanding project status stages
   SALES & DISCLOSURES — Recording a property sale · Filing a sales disclosure · Uploading buyer identification documents
   ESCROW & FUND RELEASES — Registering a project escrow account · Requesting a milestone-based fund release · What triggers a Trustee Review
   PAYMENTS & COMPLIANCE — Understanding when a service fee is due · Responding to a RERA information request · Renewing developer registration

6. Card — "Support Tickets". Card header: heading on the left with a grey counter "2 open"; on the right a blue primary button "Create Support Ticket".
   Table with columns: Reference · Subject · Category · Priority · Status · Created · Last Updated · Action
     TKT-2026-0244 — Fund release stuck in Trustee Review — Escrow — High — Open — Aug 15, 2026 — 9 hours ago — View
     TKT-2026-0239 — Question about dual-stage payment for Service #24 — Payments — Normal — Under Response — Aug 12, 2026 — 1 day ago — View
     TKT-2026-0221 — Staff invitation email not received — Account — Normal — Resolved — Aug 4, 2026 — 6 days ago — View

7. Card — "System Status". A vertical list of four rows, each with a small green dot, a service name, and a right-aligned status label:
   Platform — Operational
   Payment Gateway — Operational
   Document Storage — Operational
   RERA Submission Service — Operational
   Beneath, separated by a divider: "Scheduled maintenance: 24 Aug 2026, 01:00–03:00 WAT."

8. Card — "Contact RERA Support". Two-column layout:
   Left, under "SUPPORT CHANNELS" — RERA Support Centre: Mon–Fri, 8:00 AM – 6:00 PM WAT, +234 1 448 7700 · Live Chat: Available during support hours · Email: developers@rera.gov.ng
   Right, under "EMERGENCY REGULATORY SUPPORT" — For time-critical regulatory matters, including an escrow irregularity requiring urgent attention — +234 1 448 7799, 24 hours
   Beneath both columns, a secondary button "Contact RERA Support".

9. Card — "Training Resources". Three compact cards: "Getting Started with the Developer Portal" (Guide) · "Escrow & Fund Release Walkthrough" (Recorded Session) · "Filing Your First Sales Disclosure" (Guide)

10. Card — "Feedback & Suggestions". A single-line text input with placeholder "Share feedback or suggest a feature...", a blue primary button "Submit", and beneath it a short list of two previous submissions with a status pill each (Under Review · Implemented).
```
