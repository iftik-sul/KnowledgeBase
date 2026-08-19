---
project: RERAN
module: financial-trust-institutions
type: reference-sample
status: current
updated: 2026-08-19
contains_proposals: true
written_against_specs_on: 2026-08-18
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/applications.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/internal-certification-queue.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/escrow-request-queue.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/trust-accounts.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/compliance-reports.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/payment-history.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/documents.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/institution-profile.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/notifications.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens/help-and-support.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/services-catalog.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in `../screens/` and `../screens-unified/`; where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Sidebar Landing Screens

**Module:** Financial & Trust Institutions (RERAN Group C)
**Screens:** 11, namespaced `NAV – 01` … `NAV – 11`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## What this covers

The first screen a user lands on after clicking each sidebar item. Dashboard is already built (screen #1), so eleven of the twelve nav items need a landing screen.

| Sidebar item | Landing screen | Prompt |
| :--- | :--- | :--- |
| Dashboard | Dashboard | *already built* |
| Service Requests | Services Catalog | `NAV – 01` |
| Applications | Applications | `NAV – 02` |
| Internal Certification | Internal Certification Queue | `NAV – 03` |
| Escrow Requests | Escrow Request Queue | `NAV – 04` |
| Trust Accounts | Trust Accounts | `NAV – 05` |
| Compliance Reports | Compliance Reports | `NAV – 06` |
| Payment History | Payment History | `NAV – 07` |
| Documents | Documents | `NAV – 08` |
| Institution Profile | Institution Profile | `NAV – 09` |
| Notifications | Notifications | `NAV – 10` |
| Help & Support | Help & Support | `NAV – 11` |

**Two of these close loops on work already done.** `NAV – 01` is what the five `S* – 01` Service Details screens breadcrumb back to, and `NAV – 03` is what `S3 – 09` opens from. Both currently point at screens that don't exist in Figma. Worth building first.

---

## Shared structure

Nine of the eleven follow one shape: **Institution Context Header → Summary Cards → Filters → Table → Pagination**. Build `NAV – 02` first and the rest will inherit its layout cleanly.

The two exceptions are `NAV – 09` Institution Profile (no context header — the page *is* the institution's standing) and `NAV – 11` Help & Support (no table at all).

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | **List state only, no detail panel open** | Trust Accounts, Documents and Payment History each specify a detail panel that opens alongside the table. These prompts show the default list state. The panels are follow-up screens. |
| 2 | **All data is institution-wide, never role-filtered** | The unified-access model. No screen hides rows, greys actions, or shows "not available to your role." |
| 3 | **Sample data matches the built Dashboard exactly** | Every count, reference and name below is taken from the Dashboard screen so the whole set reads as one coherent system. |
| 4 | **Payment timing is pay-before-decision everywhere** | See the doc defect note below. |
| 5 | **Empty states are not drawn as separate screens** | Each spec defines one, but eleven extra empty-state frames is disproportionate. Add them per screen later if wanted. |

> **Doc defect worth fixing.** `institution-profile.md` (dated 2026-08-15) still states in Section 1 and again in its Notes that Services #12 and #18 pay *after* RERA's decision, calling them "the two exceptions to the module's general pattern." The 2026-08-16 client normalization retired that exception — `payment-history.md`, `notifications.md`, `services-catalog.md` and `applications.md` were all corrected, but this file wasn't. A non-propagation drift. `NAV – 09` follows the corrected model.

---

## Shared sample data

Taken from the built Dashboard. Keep identical across all eleven screens.

- **Institution:** First Bank of Nigeria · `FI-2024-00892` · Trustee & Auditor Approval · Renewal Due · expires in 47 days (15 Dec 2026)
- **Logged-in user:** Chukwuemeka Okonkwo — Institution Relationship Manager
- **Staff:** Amara Okafor (Mortgage Officer) · Musa Ibrahim (Account Trustee) · Ngozi Adeyemi (Auditing Bureau Officer) · Chukwuemeka Okonkwo (Institution Relationship Manager) · 14 on roster, 2 invited
- **Applications:** Draft 6 · Pending Internal Certification 4 · With RERA 18 · Completed This Month 11
- **Application refs:** `APP-2026-0161` `APP-2026-0158` `APP-2026-0156` `APP-2026-0149` `APP-2026-0143` `APP-2026-0142` `APP-2026-0138` `APP-2026-0131`
- **Escrow:** Awaiting Assessment 7 · Under Trustee Assessment 5 · Breaching SLA 2 · oldest `ESC-2026-0087` Banana Island Villas Trust, 9 days
- **Trust accounts:** 42 under management · 3 statements overdue · 1 flagged (Victoria Gardens Trust)
- **Compliance:** Reports Due 3 · Overdue 1 · Open Findings 5

---

## NAV – 01 · Services Catalog

```
Create a new screen frame named "NAV – 01 Services Catalog", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 01 Services Catalog
  - FI-Sidebar        (instance of the existing sidebar component — do not redraw it; active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Requests", subtitle "Browse and start any RERA service.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, badges, search inputs, filter bars, section headers, icons. Do not invent new colours, type scales, or card treatments. Match the white-card-on-grey treatment used on the Dashboard.

Keep it simple: stacked white cards, one blue primary action, no illustrations, no gradients, no service icons or artwork.

Workspace content, top to bottom:

1. Full-width search input with a magnifier icon, placeholder "Search by service name or number...".

2. A row of five category cards, evenly spaced. Each card shows a category name, a service-count line, and nothing else — no icons, no descriptions:
   Institutional Approval Services — 2 services
   Mortgage Services — 5 services
   Finance Lease Services — 4 services
   Title & Ownership Transaction Services — 6 services
   Contract Services — 1 service
   Show the third card (Title & Ownership) in a selected state, using the existing selected-card treatment.

3. Card — "Recently Used". A single horizontal row of four compact tiles, each showing a service number and name only:
   #3 Mortgage Registration · #13 Sale Procedure (Heirs) · #8 Finance Lease Registration · #17 Issuance of Title Deed

4. Card — "All Services". Card header: heading "All Services" on the left with a small grey counter "18 services"; on the right a filter bar with three dropdowns — Category · Fee Timing · Assisted Mode.
   Beneath the header, a table with columns: Service · Description · Fee Timing · SLA · Assisted Mode
   Each Service cell shows the number and name together (e.g. "#3 Mortgage Registration"). Description is one short line. Fee Timing is a small badge. Assisted Mode is a small badge or an em-dash where unavailable.

     #1 Approval / Renewal — Approve or renew the institution's trustee and auditor standing — Pay upfront — 30 days — —
     #2 Cancellation — Cancel the institution's trustee and auditor approval — FREE — 30 days — —
     #3 Mortgage Registration — Record a new mortgage against a registered title — Pay upfront — 20–25 min — Assisted
     #4 Mortgage Amendment — Amend the terms of a registered mortgage — Pay upfront — 20–25 min — Assisted
     #5 Mortgage Transfer — Transfer a registered mortgage to another institution — Pay upfront — 20–25 min — Assisted
     #6 Mortgage Release — Release a mortgage from a registered title — Pay upfront — 20–25 min — Assisted
     #7 Grant Property Mortgage — Grant a mortgage over a registered property — Pay upfront — 20–25 min — Assisted
     #8 Finance Lease Registration — Register a new finance lease — Pay upfront — 20–25 min — Assisted
     #9 Finance Lease Amendment — Amend a registered finance lease — Pay upfront — 20–25 min — Assisted
     #10 Finance Lease Transfer — Transfer a registered finance lease — Pay upfront — 20–25 min — Assisted
     #11 Finance Lease Release — Release a registered finance lease — Pay upfront — 20–25 min — Assisted
     #12 Fund Company Registration — Register a fund company in the register of privileges — Pay at counter — 25–30 min — Assisted
     #13 Sale Procedure (Heirs) — Sell a deceased owner's property and distribute proceeds — Pay at counter — 25–30 min — Assisted
     #14 Company Shares Sale — Register the sale of shares in a property-holding company — Pay at counter — 25–30 min — Assisted
     #15 Update Title Deed Information — Correct or update recorded title deed particulars — Pay at counter — 25 min — Assisted
     #16 Split Ownership — Split a registered property into separate ownerships — Pay at counter — 25–30 min — Assisted
     #17 Issuance of Title Deed — Issue an electronic title deed certificate — Pay at counter — 25 min — Assisted
     #18 Contract Cancellation — Cancel a registered contract — Pay at counter — 25–30 min — Assisted

   Give the "FREE" badge on service #2 a visually distinct treatment from the two paid badges — it is the only service in the catalogue with no fee at all, and that must be unmistakable rather than read as a missing value.

   Each row's Service cell is a link, and each row carries a right-aligned "Start" text action.
```

---

## NAV – 02 · Applications

```
Create a new screen frame named "NAV – 02 Applications", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 02 Applications
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Applications", subtitle "Every service request across the institution.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — the institution context header, metric cards, filter bars, data tables, status pills, pagination, buttons. Do not invent new colours, type scales, or card treatments. Match the Dashboard's metric card and data table treatment exactly.

Keep it simple: one context header, one row of metric cards, one filter bar, one table. No charts, no illustrations, no side panel.

This screen establishes the layout that most other list screens in this module reuse — build it carefully.

Workspace content, top to bottom:

1. Institution context header card, full width: on the left "First Bank of Nigeria" with a sub-line "Trustee & Auditor Approval FI-2024-00892"; on the right an amber "Renewal Due" status pill above the line "Expires in 47 days (15 Dec 2026)", then a blue primary button "New Service Request".

2. A row of five metric cards, evenly spaced, each with a label, a large figure, and a short grey caption:
   Draft — 6 — Started, not yet submitted
   Pending Internal Certification — 4 — Awaiting certify or return
   Submitted / Under Review — 18 — With RERA
   Information Requested — 3 — RERA has raised a query
   Completed This Month — 11 — Settled and issued

3. Filter bar, full width: a search input with placeholder "Search by reference, service, property or party...", followed by dropdowns — Service · Status · Gate · Origination · Filed By · Date Range · SLA State · Sort By. Show "Sort By: Most recent" as the selected value.

4. Card — "Applications". Card header: heading on the left with a grey counter "42 applications"; on the right a secondary text action "Export Selected".
   Table with columns: Reference · Service · Filed By · Represented Party · Origination · Gate · Status · Submitted · SLA · Action
   Reference cells are blue links. Status uses the existing status pill. SLA shows a countdown, amber when approaching and red when breached. Action is a light-blue "Open" button, matching the Dashboard's table.

     APP-2026-0161 — #3 Mortgage Registration — Amara Okafor — Adebayo Adesanya — Direct — RERA Review — Under Review — Aug 17, 2026 — 18 min left — Open
     APP-2026-0158 — #8 Finance Lease Registration — Musa Ibrahim — Chidinma Eze — Direct — RERA Review — Under Review — Aug 17, 2026 — 12 min left — Open
     APP-2026-0156 — #3 Mortgage Registration — Amara Okafor — Folake Adeyinka — Direct — RERA Review — Information Requested — Aug 14, 2026 — Breached — Open
     APP-2026-0149 — #16 Split Ownership — Chukwuemeka Okonkwo — Ibrahim Sanusi — Assisted — RERA Review — Returned for Correction — Aug 15, 2026 — Breached — Open
     APP-2026-0143 — #8 Finance Lease Registration — Musa Ibrahim — Kelechi Obi — Direct — Internal Certification — Pending Internal Certification — Aug 16, 2026 — 1 day — Open
     APP-2026-0142 — #6 Mortgage Release — Amara Okafor — Yetunde Bakare — Direct — Completed — Completed — Aug 16, 2026 — — — Open
     APP-2026-0138 — #5 Mortgage Transfer — Amara Okafor — Suleiman Bello — Direct — Internal Certification — Pending Internal Certification — Aug 17, 2026 — 6 hours — Open
     APP-2026-0131 — #13 Sale Procedure (Heirs) — Ngozi Adeyemi — Nwachukwu Estate — Assisted — RERA Review — Returned for Correction — Aug 17, 2026 — 4 hours — Open

5. Pagination row beneath the table, right-aligned: "Showing 1–8 of 42" with page controls.
```

---

## NAV – 03 · Internal Certification Queue

```
Create a new screen frame named "NAV – 03 Internal Certification Queue", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 03 Internal Certification Queue
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Internal Certification")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Internal Certification", subtitle "Records awaiting certification before RERA submission.")
    - Workspace

Reuse the layout and every component established on the Applications screen — institution context header, metric cards, filter bar, data table, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Applications, fewer columns. No charts, no illustrations, no bulk decision controls.

Workspace content, top to bottom:

1. Institution context header card, full width: "First Bank of Nigeria" with sub-line "Trustee & Auditor Approval FI-2024-00892"; on the right an amber "Renewal Due" pill above "Expires in 47 days (15 Dec 2026)".

2. A row of four metric cards:
   Awaiting Certification — 4 — Institution-wide
   Certified This Month — 27 — Actioned by you
   Returned This Month — 3 — Sent back by you
   Oldest Waiting — 2 days — Longest-waiting record

3. Filter bar: search input with placeholder "Search by reference, service, filer or party...", followed by dropdowns — Service · Filed By · Age · Sort By. Show "Sort By: Oldest first" as the selected value.

4. Card — "Awaiting Certification". Card header: heading on the left with a grey counter "4 records".
   Table with columns: Reference · Service · Filed By · Represented Party · Submitted · Age · Status · Action
   Reference cells are blue links. Status pill reads "Pending Internal Certification" on every row. Action is a light-blue "Review" button.

     APP-2026-0143 — #8 Finance Lease Registration — Musa Ibrahim — Kelechi Obi — Aug 16, 2026 — 2 days — Pending Internal Certification — Review
     APP-2026-0147 — #4 Mortgage Amendment — Amara Okafor — Halima Yusuf — Aug 17, 2026 — 1 day — Pending Internal Certification — Review
     APP-2026-0138 — #5 Mortgage Transfer — Amara Okafor — Suleiman Bello — Aug 17, 2026 — 6 hours — Pending Internal Certification — Review
     APP-2026-0152 — #3 Mortgage Registration — Chukwuemeka Okonkwo — Adaeze Nwosu — Aug 17, 2026 — 3 hours — Pending Internal Certification — Review

   Give the last row's Filed By cell a small grey "You" label beside the name — any user may certify a record they filed themselves, and the queue does not hide it.

5. A single-line inline notice beneath the table, using the existing subtle notice style: "Certification is a per-record decision made on the record itself. There is no bulk certify action."

6. Pagination row beneath the table, right-aligned: "Showing 1–4 of 4".
```

---

## NAV – 04 · Escrow Request Queue

```
Create a new screen frame named "NAV – 04 Escrow Request Queue", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 04 Escrow Request Queue
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Escrow Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Escrow Requests", subtitle "Assess and certify developer escrow requests before regulatory audit.")
    - Workspace

Reuse the layout and every component established on the Applications screen — institution context header, metric cards, filter bar, data table, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Applications. No charts, no illustrations, no bulk decision controls. This table is wider than the others — let it scroll horizontally rather than shrinking the type.

Workspace content, top to bottom:

1. Institution context header card, full width, same as the Applications screen.

2. A row of six metric cards:
   Awaiting Assessment — 7 — Received, not yet opened
   Under Assessment — 5 — Open with this institution
   Information Requested — 2 — Queried back to the developer
   Certified This Month — 19 — Forwarded to RERA
   Breaching SLA — 2 — Past the response window
   Trust Accounts Managed — 42 — Under trusteeship
   Give the "Breaching SLA" card an error treatment on its figure, matching the existing error colour.

3. Filter bar: search input with placeholder "Search by request ID, project, developer or account...", followed by dropdowns — Request Type · Status · Trust Account · Developer · SLA State · Received Date · Sort By. Show "Sort By: SLA urgency" as the selected value.

4. Card — "Escrow Requests". Card header: heading on the left with a grey counter "14 requests"; on the right two secondary text actions "Export Selected" and "Generate Queue Report".
   Table with columns: Request ID · Type · Project · Developer · Trust Account · Requested Amount · Available Balance · Milestone · Received · SLA Remaining · Status · Action
   Request ID cells are blue links. Action is a light-blue "Assess" button. SLA Remaining is amber when approaching and red when breached.

     ESC-2026-0087 — Payment Release — Banana Island Villas — Crestwood Developments — TRA-0041 — ₦85,000,000 — ₦210,400,000 — Structural completion — Aug 8, 2026 — Breached — Awaiting Assessment — Assess
     ESC-2026-0091 — Profit Withdrawal — Victoria Gardens — Kingsfield Properties — TRA-0017 — ₦40,000,000 — ₦38,200,000 — — — Aug 12, 2026 — Breached — Awaiting Assessment — Assess
     ESC-2026-0094 — Payment Release — Lekki Pearl Estate — Crestwood Developments — TRA-0029 — ₦62,500,000 — ₦148,900,000 — Roofing complete — Aug 15, 2026 — 4 hours — Under Assessment — Assess
     ESC-2026-0096 — Account Activation — Ikoyi Heights — Northgate Realty — TRA-0055 — — — — — — — Aug 16, 2026 — 11 hours — Awaiting Assessment — Assess
     ESC-2026-0098 — Mortgage Deposit — Maitama Court — Silverline Homes — TRA-0033 — ₦120,000,000 — ₦305,700,000 — — — Aug 17, 2026 — 1 day — Under Assessment — Assess
     ESC-2026-0099 — Bank Guarantee Cancellation — Lekki Pearl Estate — Crestwood Developments — TRA-0029 — — — ₦148,900,000 — — — Aug 17, 2026 — 1 day — Awaiting Assessment — Assess

   On the ESC-2026-0091 row, show the Available Balance in the error colour — the requested amount exceeds it, and that must be visible before the row is opened.

5. Pagination row beneath the table, right-aligned: "Showing 1–6 of 14".
```

---

## NAV – 05 · Trust Accounts

```
Create a new screen frame named "NAV – 05 Trust Accounts", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 05 Trust Accounts
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Trust Accounts")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Trust Accounts", subtitle "Accounts under this institution's trusteeship.")
    - Workspace

Reuse the layout and every component established on the Applications screen — institution context header, metric cards, filter bar, data table, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Applications. No charts, no balance graphs, no illustrations. Show the default list state only — not the account detail panel.

Workspace content, top to bottom:

1. Institution context header card, full width, same as the Applications screen.

2. A row of six metric cards:
   Active Accounts — 36 — Operating normally
   Pending Activation — 2 — Registered, not yet active
   Statement Overdue — 3 — Periodic statement not filed
   Under Audit — 1 — Open audit engagement
   Flagged — 1 — Irregularity raised
   Suspended — 0 — Frozen by RERA
   Give "Statement Overdue" a warning treatment and "Flagged" an error treatment on their figures.

3. Filter bar: search input with placeholder "Search by account reference, project or developer...", followed by dropdowns — Status · Project · Developer · Statement Filing State · Sort By. Show "Sort By: Statement due date" as the selected value.

4. Card — "Trust Accounts". Card header: heading on the left with a grey counter "42 accounts"; on the right a secondary text action "Export Selected".
   Table with columns: Account Reference · Project · Developer · Current Balance · Statement Filed · Statement Due · Status · Open Findings · Action
   Account Reference cells are blue links. Open Findings shows a count, or an em-dash where zero, and links out. Action is a light-blue "View" button.

     TRA-0017 — Victoria Gardens — Kingsfield Properties — ₦38,200,000 — 12 May 2026 — 12 Aug 2026 — Flagged — 3 — View
     TRA-0022 — Ikeja Grove — Northgate Realty — ₦91,750,000 — 04 May 2026 — 04 Aug 2026 — Statement Overdue — — — View
     TRA-0041 — Banana Island Villas — Crestwood Developments — ₦210,400,000 — 28 Jun 2026 — 28 Sep 2026 — Under Audit — 2 — View
     TRA-0029 — Lekki Pearl Estate — Crestwood Developments — ₦148,900,000 — 15 Jul 2026 — 15 Oct 2026 — Active — — — View
     TRA-0033 — Maitama Court — Silverline Homes — ₦305,700,000 — 22 Jul 2026 — 22 Oct 2026 — Active — — — View
     TRA-0055 — Ikoyi Heights — Northgate Realty — — — — — — — Pending Activation — — — View

   Show the Statement Due dates for TRA-0017 and TRA-0022 in the error colour — both are past due.

5. Pagination row beneath the table, right-aligned: "Showing 1–6 of 42".
```

---

## NAV – 06 · Compliance Reports

```
Create a new screen frame named "NAV – 06 Compliance Reports", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 06 Compliance Reports
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Compliance Reports")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Compliance Reports", subtitle "Prepare independent compliance reports and record escrow audit findings.")
    - Workspace

Reuse the layout and every component established on the Applications screen — institution context header, metric cards, filter bar, data table, status pills, pagination — plus the existing tab component. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Applications, with a two-tab switch above the table. No charts, no illustrations.

Workspace content, top to bottom:

1. Institution context header card, full width: "First Bank of Nigeria" with sub-line "Trustee & Auditor Approval FI-2024-00892"; on the right an amber "Renewal Due" pill above "Expires in 47 days (15 Dec 2026)", then a secondary button "Raise Finding" and a blue primary button "New Compliance Report".

2. A row of five metric cards:
   Reports Due — 3 — Filing date this period
   Overdue — 1 — Past filing date
   Accounts Statement Overdue — 3 — Trust account statements outstanding
   Open Findings — 5 — Raised, not yet resolved
   Escalated to RERA — 1 — Referred for regulatory attention
   Give "Overdue" an error treatment on its figure.

3. A two-tab switch: "Reports" (active) and "Findings", using the existing tab component.

4. Filter bar: search input with placeholder "Search by report reference, trust account or project...", followed by dropdowns — Report Type · Period · Status · Sort By.

5. Card — "Reports". Card header: heading on the left with a grey counter "12 reports".
   Table with columns: Report Reference · Report Type · Period Covered — Scope · Prepared By · Filing Deadline · Submitted · Status · Action
   Report Reference cells are blue links. Action is a light-blue "Open" button.

     CR-2026-0044 — Periodic escrow audit — Q2 2026 — 12 accounts — Ngozi Adeyemi — 31 Jul 2026 — — — Overdue — Open
     CR-2026-0051 — Trust account statement — Jul 2026 — TRA-0017 — Ngozi Adeyemi — 31 Aug 2026 — — — Draft — Open
     CR-2026-0049 — Periodic escrow audit — Q2 2026 — 8 accounts — Ngozi Adeyemi — 31 Aug 2026 — 14 Aug 2026 — Under RERA Review — Open
     CR-2026-0043 — Ad hoc compliance report — Jun 2026 — TRA-0041 — Musa Ibrahim — 30 Jun 2026 — 27 Jun 2026 — Accepted — Open
     CR-2026-0038 — Periodic escrow audit — Q1 2026 — 11 accounts — Ngozi Adeyemi — 30 Apr 2026 — 24 Apr 2026 — Returned — Open

   Show the CR-2026-0044 filing deadline in the error colour.

6. Pagination row beneath the table, right-aligned: "Showing 1–5 of 12".
```

---

## NAV – 07 · Payment History

```
Create a new screen frame named "NAV – 07 Payment History", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 07 Payment History
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Payment History")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment History", subtitle "Every payment made by the institution, by transaction.")
    - Workspace

Reuse the layout and every component established on the Applications screen — institution context header, metric cards, filter bar, data table, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: same shape as Applications. Show the default list state only — not the receipt detail panel.

IMPORTANT: this screen must show NO account balance anywhere. There is no standing account and nothing to fund — every figure here is a fact about a transaction that already happened. Do not add a balance card, a top-up action, or a low-balance warning.

Workspace content, top to bottom:

1. Institution context header card, full width, same as the Applications screen but with no primary button.

2. A row of four metric cards:
   Paid This Month — ₦2,847,300 — Successful payments
   Payments Failed — 2 — Retryable
   Refunds Requested — 1 — Under review
   Refunds Completed This Month — 3 — ₦184,500

3. Filter bar: search input with placeholder "Search by application, receipt or reference...", followed by dropdowns — Service · Status · Payer · Date Range · Amount Range · Sort By. Show "Sort By: Most recent" as the selected value.

4. Card — "Payments". Card header: heading on the left with a grey counter "68 payments"; on the right a secondary text action "Export Selected".
   Table with columns: Receipt Reference · Application · Service · Payer · Amount · Method · Paid · Status · Action
   Receipt and Application cells are blue links. Action shows two inline text links, "View Receipt" and "View Application".

     PAY-2026-00957 — APP-2026-0191 — #12 Fund Company Registration — Customer — ₦153,900 — Card — Aug 17, 2026, 4:31 PM — Successful — View Receipt / View Application
     PAY-2026-00944 — APP-2026-0184 — #15 Update Title Deed Information — Customer — ₦18,920 — Card — Aug 17, 2026, 2:38 PM — Successful — View Receipt / View Application
     PAY-2026-00931 — APP-2026-0179 — #13 Sale Procedure (Heirs) — Customer — ₦94,600 — Bank Transfer — Aug 17, 2026, 11:26 AM — Successful — View Receipt / View Application
     PAY-2026-00918 — APP-2026-0172 — #3 Mortgage Registration — Institution — ₦59,125 — Card — Aug 17, 2026, 10:19 AM — Successful — View Receipt / View Application
     PAY-2026-00912 — APP-2026-0167 — #17 Issuance of Title Deed — Customer — ₦23,650 — Card — Aug 17, 2026, 9:24 AM — Successful — View Receipt / View Application
     PAY-2026-00905 — APP-2026-0163 — #8 Finance Lease Registration — Institution — ₦47,300 — Card — Aug 16, 2026, 3:12 PM — Failed — View Application
     PAY-2026-00898 — APP-2026-0159 — #5 Mortgage Transfer — Institution — ₦59,125 — USSD — Aug 16, 2026, 11:04 AM — Refund Requested — View Receipt / View Application

   The Failed row shows only "View Application" — there is no receipt for a payment that did not settle.

5. Pagination row beneath the table, right-aligned: "Showing 1–7 of 68".
```

---

## NAV – 08 · Documents

```
Create a new screen frame named "NAV – 08 Documents", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 08 Documents
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Documents")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Documents", subtitle "Every file attached across the institution.")
    - Workspace

Reuse the layout and every component established on the Applications screen — institution context header, filter bar, data table, status pills, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: no metric cards on this screen — it goes straight from the context header to the filters. Show the default list state only, not the preview panel. No file thumbnails, no folder tree, no illustrations.

IMPORTANT: there is no Upload button anywhere on this screen. Documents are added from within an application, an escrow assessment or a compliance report — this repository is where they are found afterward.

Workspace content, top to bottom:

1. Institution context header card, full width, same as the Applications screen but with no primary button.

2. Filter bar: search input with placeholder "Search by document name, application, service or uploader...", followed by dropdowns — Document Type · Linked To · Status · Uploaded By · Date Range · Sort By. Show "Sort By: Most recent" as the selected value.

3. Card — "Documents". Card header: heading on the left with a grey counter "1,284 documents"; on the right a secondary text action "Export Selected".
   Table with columns: Document Name · Type · Linked To · Version · Uploaded By · Uploaded · Status · Action
   Document Name cells are blue links. Linked To shows a reference, with a small grey "+1" style indicator where a document is attached to more than one record. Action is a light-blue "Preview" button.

     meridian-trust-deed.pdf — Trust Deed — APP-2026-0191 — v1 — Chukwuemeka Okonkwo — Aug 17, 2026 — Uploaded — Preview
     meridian-unit-holders-24.xlsx — Beneficial Owners List — APP-2026-0191 — v2 — Chukwuemeka Okonkwo — Aug 17, 2026 — Uploaded — Preview
     halima-marriage-certificate.pdf — Supporting Evidence — APP-2026-0184 — v1 — Chukwuemeka Okonkwo — Aug 17, 2026 — Uploaded — Preview
     nwachukwu-grant-of-probate.pdf — Probate / Administration — APP-2026-0179 — v1 — Ngozi Adeyemi — Aug 17, 2026 — Uploaded — Preview
     adesanya-certificate-of-title.pdf — Certificate of Title — APP-2026-0172, +1 — v1 — Amara Okafor — Aug 17, 2026 — Referenced Elsewhere — Preview
     adesanya-valuation-report.pdf — Valuation Report — APP-2026-0172 — v1 — Amara Okafor — Aug 17, 2026 — Uploaded — Preview
     tra-0017-statement-q2.pdf — Trust Account Statement — CR-2026-0051 — v1 — Musa Ibrahim — 12 May 2026 — Uploaded — Preview
     tra-0017-statement-q1.pdf — Trust Account Statement — CR-2026-0038 — v1 — Musa Ibrahim — 24 Apr 2026 — Superseded — Preview

   Give the "Superseded" status pill a muted treatment, distinct from "Uploaded" and "Referenced Elsewhere".

4. Pagination row beneath the table, right-aligned: "Showing 1–8 of 1,284".
```

---

## NAV – 09 · Institution Profile

```
Create a new screen frame named "NAV – 09 Institution Profile", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 09 Institution Profile
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Institution Profile")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Institution Profile", subtitle "Approval standing and staff roster.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value grids, data tables, tabs, section headers. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards with a two-tab switch. No charts, no illustrations, no org chart, no avatars.

IMPORTANT: this screen does NOT use the institution context header — the page's own Institution Standing card is that same information, shown as the subject of the page rather than a strip above it. Do not add both.

Workspace content, top to bottom:

1. Card — "Institution Standing". Inside the card:
   - A header row: "First Bank of Nigeria" as a large heading on the left, with an amber "Renewal Due" status pill beside it. On the right, a secondary button "Cancel Approval", a secondary button "Cancel Contract", and a blue primary button "Renew Approval".
   - Beneath, a two-column label/value grid:
       Institution Type: Commercial Bank
       Registration Reference: FI-2024-00892
       Standing: Account Trustee & Approved Auditing Company
       Approval Granted: 15 Dec 2024
       Approval Expires: 15 Dec 2026
       Time Remaining: 47 days
   - Show "47 days" in the warning colour — it is inside the 60-day window.

2. A two-tab switch: "Staff Records" (active) and "Approval History", using the existing tab component.

3. Card — "Staff Records". Card header: heading on the left with a grey counter "14 on roster · 2 invited"; on the right a blue primary button "Invite Staff Member".
   Table with columns: Name · Email · Role · Status · Added · Action
   Action is a text-only "Remove" link in the existing muted destructive style.

     Chukwuemeka Okonkwo — c.okonkwo@firstbanknigeria.com — Institution Relationship Manager — Active — 15 Dec 2024 — Remove
     Amara Okafor — a.okafor@firstbanknigeria.com — Mortgage Officer — Active — 08 Jan 2025 — Remove
     Musa Ibrahim — m.ibrahim@firstbanknigeria.com — Account Trustee — Active — 08 Jan 2025 — Remove
     Ngozi Adeyemi — n.adeyemi@firstbanknigeria.com — Auditing Bureau Officer — Active — 22 Feb 2025 — Remove
     Bisi Afolabi — b.afolabi@firstbanknigeria.com — Mortgage Officer — Active — 14 Mar 2026 — Remove
     Tobi Adewale — t.adewale@firstbanknigeria.com — Account Trustee — Invited — 12 Aug 2026 — Remove

   Beneath the table, a single-line inline notice using the existing subtle notice style: "Every staff member has identical system access. Role is recorded for audit-trail attribution and does not restrict what a user can do."

4. Pagination row beneath the table, right-aligned: "Showing 1–6 of 16".
```

---

## NAV – 10 · Notifications

```
Create a new screen frame named "NAV – 10 Notifications", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 10 Notifications
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Notifications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Notifications", subtitle "Alerts across the institution.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, filter chips, the activity feed row pattern from the Dashboard, pagination. Do not invent new colours, type scales, or card treatments.

Keep it simple: one priority banner, one row of filter chips, one list. No illustrations, no icons per notification beyond a small priority dot.

Workspace content, top to bottom:

1. A single full-width priority alert banner, using the existing warning treatment: a warning icon on the left, then bold text "Institutional approval expires in 47 days" and a grey line beneath "Renewal must be filed before 15 Dec 2026 to avoid a lapse in standing." On the right, a secondary button "Renew Approval".

2. A row of filter chips, left-aligned: All (selected) · Unread · Approval Outcomes · Information Requested · Approval Expiry · Escrow Routing · Reporting Obligation · Certification Waiting. On the right of the same row, a secondary text action "Mark All Read".

3. Card — "Notifications". A vertical list, one row per notification. Each row has: a small coloured priority dot on the far left (red for error, amber for warning, blue for info), then the category as a small grey uppercase label above a one-line message, then the related record reference as a blue link, and a right-aligned relative timestamp. Unread rows have the message text in bold.

     ERROR · Information Requested — RERA has raised a query on your mortgage registration — APP-2026-0156 — 5 hours ago  (unread)
     WARNING · Escrow Routing — Escrow request ESC-2026-0087 has breached its response window — ESC-2026-0087 — 9 days ago  (unread)
     WARNING · Reporting Obligation — Q2 periodic escrow audit is overdue — CR-2026-0044 — 18 days ago  (unread)
     WARNING · Approval Expiry — Institutional approval expires in 47 days — Institution Profile — 1 day ago  (unread)
     INFO · Approval Outcomes — Mortgage release completed and documents issued — APP-2026-0142 — 1 day ago
     WARNING · Certification Waiting — A record has waited 2 days for internal certification — APP-2026-0143 — 2 days ago
     INFO · Escrow Routing — New escrow request received from Crestwood Developments — ESC-2026-0099 — 2 days ago
     INFO · Approval Outcomes — Finance lease registration certified internally — APP-2026-0158 — 3 days ago
     ERROR · Approval Outcomes — Split ownership application returned for correction — APP-2026-0149 — 4 days ago

4. Pagination row beneath the list, right-aligned: "Showing 1–9 of 34".
```

---

## NAV – 11 · Help & Support

```
Create a new screen frame named "NAV – 11 Help and Support", 1440px wide, light grey background.

Layer structure exactly:
- NAV – 11 Help and Support
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Help & Support")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Help & Support", subtitle "Knowledge base, support tickets and RERA contact routes.")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, metric cards, search inputs, data tables, the quick actions tile pattern from the Dashboard. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. No illustrations, no hero image, no chat bubble graphic, no video thumbnails.

Workspace content, top to bottom:

1. A row of four metric cards:
   Open Tickets — 2 — Institution-wide
   Resolved This Month — 7 — Closed by RERA support
   Average Response Time — 4 hours — Current period
   Unread Announcements — 1 — From RERA

2. Card — "Search the Knowledge Base". A single large full-width search input with a magnifier icon, placeholder "Search help articles...". Nothing else in this card.

3. Card — "Quick Help". A grid of seven compact tiles, each a short text label only, no icons:
   Registering a mortgage · Certifying an escrow request · Filing a compliance report · Renewing institutional approval · Managing staff records · Responding to an information request · Resubmitting a returned application

4. Card — "Knowledge Base Articles". Card header: heading on the left, a "View All" link on the right. A simple two-column list of article titles grouped under small uppercase grey sub-headings:
   MORTGAGE & FINANCE LEASE — Registering a mortgage against a verified title · Amending a registered mortgage · Releasing a mortgage on sale
   ESCROW & TRUST ACCOUNTS — Assessing a developer escrow request · Filing a periodic trust account statement · What makes an account flagged
   COMPLIANCE & REPORTING — Preparing a periodic escrow audit · Raising and escalating a finding
   INSTITUTION & STAFF — Renewing institutional approval · Adding and removing staff

5. Card — "Support Tickets". Card header: heading on the left with a grey counter "2 open"; on the right a blue primary button "Create Support Ticket".
   Table with columns: Reference · Subject · Category · Priority · Status · Created · Last Updated · Action
   Reference cells are blue links. Action is a light-blue "View" button.

     TKT-2026-0412 — Escrow request stuck in Under Assessment — Escrow — High — Open — Aug 16, 2026 — 4 hours ago — View
     TKT-2026-0408 — Clarification on compliance report template — Reporting — Normal — Under Response — Aug 14, 2026 — 1 day ago — View
     TKT-2026-0391 — Staff invitation email not received — Account — Normal — Resolved — Aug 09, 2026 — 5 days ago — View

6. Card — "System Status". A vertical list of four rows, each with a small green dot, a service name, and a right-aligned status label:
   Platform — Operational
   Payment Gateway — Operational
   Document Storage — Operational
   RERA Submission Service — Operational
   Beneath the list, separated by a divider, one grey line: "Scheduled maintenance: 24 Aug 2026, 01:00–03:00 WAT."

7. Card — "Contact RERA Support". A two-column layout:
   Left column, under a small uppercase grey sub-heading "SUPPORT CHANNELS":
     RERA Support Centre — Mon–Fri, 8:00 AM – 6:00 PM WAT — +234 1 448 7700
     Live Chat — Available during support hours
     Email — institutions@rera.gov.ng
   Right column, under a small uppercase grey sub-heading "EMERGENCY REGULATORY SUPPORT":
     For time-critical regulatory matters, including discovered escrow irregularities requiring urgent attention.
     +234 1 448 7799 — 24 hours
   Beneath both columns, a secondary button "Contact RERA Support".
```
