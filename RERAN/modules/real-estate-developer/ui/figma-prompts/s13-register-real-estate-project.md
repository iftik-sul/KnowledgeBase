---
project: RERAN
module: real-estate-developer
type: reference-sample
status: draft
contains_proposals: true
written_against_specs_on: 2026-08-19
derived_from:
  - "RERAN/modules/real-estate-developer/service-flows/service-13-register-real-estate-project.md"
  - "RERAN/modules/real-estate-developer/ui/screens/projects.md"
  - "RERAN/modules/real-estate-developer/ui/screens/project-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/applications.md"
  - "RERAN/modules/real-estate-developer/ui/components.md"
  - "RERAN/modules/real-estate-developer/ui/figma-prompts/nav-sidebar-landing-screens.md"
  - "RERAN/modules/financial-trust-institutions/ui/figma-prompts/s03-mortgage-registration.md"
tags:
  - real-estate-developer
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in [`../screens/`](../screens/) and [`service-13-register-real-estate-project.md`](../../service-flows/service-13-register-real-estate-project.md); where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Service #13: Registration of Real Estate Project

**Module:** Real Estate Developer (RERAN Group B)
**Screens:** 11, namespaced `S13 – 01` … `S13 – 11`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## Why this doesn't reuse Group C's wizard shape

Group C's `s03-mortgage-registration.md` pack — the reference this one is modelled on — uses one continuous 6-step wizard (Application Info → Service Info → Documents → Validation → Payment → Review & Submit), because that service really is one continuous submission: fill it in, pay, submit, done.

**Service #13 does not have that shape.** Its own sourced workflow has a hard gate in the middle: the developer submits an initial application, RERA accepts or rejects it, and only *after acceptance* can the developer upload units, request a Registrar account, and pay. Forcing that into one 6-step wizard would misrepresent a service where step 5 genuinely cannot happen until RERA acts on step 4. This pack instead uses two trackers:

- A **4-step horizontal wizard** (`S13 – 02` through `S13 – 05`) for the initial application only — Project Information, Survey Information, Documents, Review & Submit.
- The module's own **vertical status timeline** (the same pattern used on `applications.md`'s Application Details screen) for everything from submission onward, since that phase is a sequence of gated stages rather than a form the developer fills in continuously.

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | **Payment sits near the end, after RERA's initial acceptance** | Sourced directly — Section 9 of the service file states this is a genuine payment-timing exception, verified against this service's own row, not inferred. Fee is paid only once the Registrar account request is in, right before the certificate is issued. |
| 2 | **Two separate authorities act at two separate points** | Sourced — Compliance & Escrow Auditor handles the initial accept/reject; the Registrar handles the account-opening step after units are uploaded. Both are shown, not collapsed into one "RERA" actor. |
| 3 | **Unit upload happens through an approved survey company, not a raw file upload** | Sourced ("Developer Uploads Units through Approved Survey Company"). Shown as a company-selection step, not a generic document attach. |
| 4 | **Required documents follow the general project-registration pattern** | The source specifies only "attach requirements," not an itemized list — flagged `contains_proposals: true` in the service file itself, carried through here unchanged. |
| 5 | **Output document not itemized beyond "certificate"** | Source is clear only on the certificate name; this pack shows one output document, matching what's sourced. |
| 6 | **This application continues the same record already shown mid-flow in the nav-sidebar pack** | `APP-2026-0221` / Gwarinpa Heights already appears as "Under Review" in `nav-sidebar-landing-screens.md`'s Applications and Dashboard screens. This pack tells that same application's full story, start to finish — screens here dated after Aug 17, 2026 extend past where the nav pack's snapshot left off. |

---

## Consistent sample data across all screens

- Application ID: `APP-2026-0221`
- Company: Crestwood Developments Ltd. · `DEV-2024-00437` · Real Estate License `RERA-DEV-2024-00437`
- Developer Self Registration Username: `crestwood.devportal`
- Filer / acting officer: Adaeze Nwosu — Project Registration Officer
- Project: Gwarinpa Heights · Plot 14, Gwarinpa District, Abuja Municipal Area Council, FCT · Mixed Use · 86 units
- Survey Company: Meridian Geospatial Surveys Ltd. (RERA-approved)
- Survey Reference: `SUR-2026-00812`
- Registrar Account Reference: `REG-ACC-2026-0143`
- Fee: Registration Fee ₦850,000 · Processing Levy ₦15,000 · VAT (7.5%) ₦64,875 · **Total ₦929,875**
- Payment Reference: `PAY-2026-01044`
- Project Approval Certificate Number: `RERA-CERT-PRJ-2026-00341`
- Processing time: 3 business days (the initial audit step; source does not give a combined figure for the full multi-gate journey)
- Initial audit authority: RERA — Compliance & Escrow Auditor
- Account-opening authority: RERA — Registrar

---

## S13 – 01 · Service Details

```
Create a new screen frame named "S13 – 01 Service Details", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 01 Service Details
  - RED-Sidebar       (instance of the existing sidebar component — do not redraw it; active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Details", subtitle "Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, tables, breadcrumbs, section headers, label/value field grids, icons. Do not invent new colours, new type scales, or new card treatments. Match the spacing, corner radius, and white-card-on-grey treatment already used on the Dashboard and Applications screens.

Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Projects / Registration of Real Estate Project

2. Page header row: heading "Registration of Real Estate Project" on the left. On the right, a secondary button "Back to Projects" and a blue primary button "Start Application".

3. Card — "Service Overview". Two-column label/value grid:
   Service Code: #13
   Service Category: Real Estate Development Services
   Processing Time: 3 business days (initial audit step)
   Applicable Fee: ₦850,000 (per RERAN fee schedule)
   Approving Authority: RERA — Compliance & Escrow Auditor (initial review), RERA — Registrar (account opening)
   Payment Timing: Paid after RERA's initial acceptance, before the certificate is issued
   Below the grid, a full-width description paragraph: "Registers a new real estate project with RERA — the foundational step before any unit within it can be sold, leased, or otherwise transacted. Most other Group B services depend on a project already being registered under this service."

4. A single-line inline notice beneath the Service Overview card, using the existing subtle notice style: "This is a multi-stage service. RERA must accept your initial application before you can upload units and request a Registrar account — those steps cannot be completed upfront."

5. Card — "How It Works". Two rows, since this service has two distinct phases:
   Phase 1 row, four numbered steps evenly spaced: 1 Project Information · 2 Survey Information · 3 Documents · 4 Review & Submit
   A short label beneath phase 1: "Your initial application to RERA"
   Phase 2 row, four numbered steps evenly spaced, greyed slightly to show they come later: 5 RERA Review · 6 Upload Units · 7 Registrar Account · 8 Payment & Certificate
   A short label beneath phase 2: "After RERA accepts your application"

6. Card — "What You'll Need". Two columns side by side.
   Left column heading "Required Information", as a simple bulleted list:
     Project name, location, type and number of units
     Approved survey company and survey reference
     Developer Self Registration username
   Right column heading "Required Documents", as a list of rows, each with the document name and a small requirement pill:
     Real Estate License — Required
     Land Title Documents — Required
     Survey Report from Approved Survey Company — Required
     Project Master Plan — Required
     Other Supporting Documents — Optional

7. Card — "Prerequisites". A short vertical list of check-style rows:
   Registered developer company account with a valid real estate license
   Designated Developer Self Registration username
   Project requirements and unit survey data available from an approved survey company

8. Card — "Who Can Apply". Two short label/value rows:
   Applicant: Any of the company's Group B users
   Typical Filer: Project Registration Officer (customary practice, not a restriction — see navigation.md)

9. Bottom-right: blue primary button "Start Application".
```

---

## S13 – 02 · Step 1 — Project Information

```
Create a new screen frame named "S13 – 02 Project Information", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 02 Project Information
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, section headers. Do not invent new colours, type scales, or card treatments. Match the Applications screen's spacing and card treatment.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action, no illustrations or decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Projects / Registration of Real Estate Project / New Application

2. Page header row: heading "Registration of Real Estate Project" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, five fields across:
   APPLICATION ID: APP-2026-0221
   SERVICE NAME: Registration of Real Estate Project
   STATUS: Draft (status pill)
   LAST UPDATED: Aug 14, 2026 — 2:10 PM
   CREATED BY: Adaeze Nwosu

4. Horizontal step progress tracker, four steps, step 1 active and steps 2–4 upcoming:
   1. Project Information · 2. Survey Information · 3. Documents · 4. Review & Submit
   A small grey line beneath the tracker: "Steps 5–8 unlock once RERA accepts this application."

5. Card — "Company Information", with a small grey helper line under the heading: "Pre-filled from your company profile". Read-only two-column label/value grid:
   Company Name: Crestwood Developments Ltd.
   Registration Number: DEV-2024-00437
   Real Estate License: RERA-DEV-2024-00437
   Developer Self Registration Username: crestwood.devportal
   Acting Officer: Adaeze Nwosu — Project Registration Officer

6. Card — "Project Information". Editable form, two columns:
   Project Name — text input, value "Gwarinpa Heights"
   Project Location — text input, value "Plot 14, Gwarinpa District, Abuja Municipal Area Council, FCT"
   Project Type — dropdown, value "Mixed Use"
   Number of Units — text input, value "86"
   Mark all four as required fields using the existing required-field treatment.

7. Step navigation row at the bottom: secondary button "Back" (disabled) on the left, blue primary button "Continue" on the right.
```

---

## S13 – 03 · Step 2 — Survey Information

```
Create a new screen frame named "S13 – 03 Survey Information", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 03 Survey Information
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, search inputs. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action, no illustrations, no maps.

Workspace content, top to bottom:

1. Breadcrumb: Projects / Registration of Real Estate Project / New Application

2. Page header row: heading "Registration of Real Estate Project" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous step.

4. Horizontal step progress tracker, four steps, step 1 complete, step 2 active.

5. Card — "Survey Company". A single search/select input labelled "Approved Survey Company", value "Meridian Geospatial Surveys Ltd.", with a small grey helper line: "Only RERA-approved survey companies appear here." Beneath it, a selected-result panel using the existing subtle bordered treatment:
   Survey Company: Meridian Geospatial Surveys Ltd.
   RERA Approval Status: Approved (green status pill)
   Approval Reference: SVY-APPR-2019-0042
   A text link "Change Survey Company" at the bottom of the panel.

6. Card — "Survey Information". Editable form, two columns:
   Survey Reference — text input, value "SUR-2026-00812"
   Survey Date — text input, value "Aug 10, 2026"
   Mark Survey Reference as required.

7. A single-line inline notice beneath the card: "Unit-level data is uploaded later, through this survey company, once RERA has accepted your application — not on this screen."

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S13 – 04 · Step 3 — Documents

```
Create a new screen frame named "S13 – 04 Documents", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 04 Documents
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, the document table, requirement pills, status pills, link-style row actions, inline notices. Do not invent new colours, type scales, or card treatments. Match the Documents screen's table treatment.

Keep it simple: one table inside one card, no drag-and-drop illustration, no file thumbnails, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Projects / Registration of Real Estate Project / New Application

2. Page header row: heading "Registration of Real Estate Project" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps.

4. Horizontal step progress tracker, four steps, steps 1–2 complete, step 3 active.

5. Card — "Supporting Documents". Under the heading, a small grey counter line: "3 of 4 required documents uploaded". On the right of the card header, a secondary text action "Attach from Documents".
   Table with columns: Document Name · Requirement · Status · Action
     Real Estate License — Required — Uploaded — View / Replace
     Land Title Documents — Required — Uploaded — View / Replace
     Survey Report from Approved Survey Company — Required — Uploaded — View / Replace
     Project Master Plan — Required — Not Uploaded — Upload
     Other Supporting Documents — Optional — Not Uploaded — Upload
   Use the existing requirement pill style for Required / Optional and the existing status pill style for Uploaded / Not Uploaded.

6. A single-line inline notice beneath the card: "Unit survey data is uploaded separately, after RERA accepts this application — see Step 6."

7. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S13 – 05 · Step 4 — Review & Submit

```
Create a new screen frame named "S13 – 05 Review and Submit", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 05 Review and Submit
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Review Application", subtitle "Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, inline "Edit" links, the Validation Panel, a declaration checkbox row. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, one blue primary action at the top and bottom. No illustrations.

IMPORTANT: this screen submits the INITIAL application only — there is no payment step here, and no mention of a fee amount. Payment happens much later, after RERA accepts this application and the Registrar account is requested (see S13 – 10). Do not add a payment summary card to this screen.

Workspace content, top to bottom:

1. Breadcrumb: Projects / Registration of Real Estate Project / New Application

2. Page header row: heading "Review Application" on the left. On the right, secondary button "Save Draft" and blue primary button "Submit Application".

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Ready for Review".

4. Horizontal step progress tracker, four steps, steps 1–3 complete, step 4 active.

5. Card — "Project Information", with an inline "Edit" link in the card header:
   Project Name: Gwarinpa Heights
   Project Location: Plot 14, Gwarinpa District, Abuja Municipal Area Council, FCT
   Project Type: Mixed Use
   Number of Units: 86

6. Card — "Survey Information", with an inline "Edit" link:
   Survey Company: Meridian Geospatial Surveys Ltd.
   Survey Reference: SUR-2026-00812
   Survey Date: Aug 10, 2026

7. Card — "Supporting Documents", counter line "4 of 4 required documents uploaded", inline action "Manage Documents". Table with columns Document Name · Requirement · Status · Action:
   Real Estate License — Required — Uploaded — View
   Land Title Documents — Required — Uploaded — View
   Survey Report from Approved Survey Company — Required — Uploaded — View
   Project Master Plan — Required — Uploaded — View

8. Card — "Validation Summary", with a green sub-line "All checks passed", then a vertical list of green check rows:
   Required project information completed
   Required documents provided
   Real estate license valid
   Survey company is RERA-approved
   No duplicate project name found
   Below a dotted divider, a green status line: "All Clear — Ready to Submit"

9. Card — "Declaration". A checked checkbox with the text: "I confirm that the information and documents provided in this application are accurate and complete. I understand that providing false or misleading information may result in application rejection, penalties, or regulatory action against the company."

10. Bottom-right: blue primary button "Submit Application".
```

---

## S13 – 06 · Application Submitted

```
Create a new screen frame named "S13 – 06 Application Submitted", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 06 Application Submitted
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Submitted", subtitle "Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, success icon treatment, numbered list rows. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card plus one short "what happens next" card. No illustration, no large graphics.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Application Submitted"
   - Sub-line, centred, grey: "Your project registration application has been sent to RERA for initial review."
   - The reference, centred and large: APP-2026-0221
   - A divider
   - A two-column label/value grid:
       Service Name: Registration of Real Estate Project
       Status: Under Review (status pill)
       Submitted On: Aug 15, 2026 — 9:42 AM
       Submitted By: Adaeze Nwosu
       Expected Review Time: 3 business days

2. Card — "What Happens Next". Four numbered rows, each with a number badge, a short bold label and one grey line beneath:
   1  RERA Review — RERA's Compliance & Escrow Auditor reviews this application and either accepts or rejects it.
   2  Upload Units — Once accepted, upload the project's units through your approved survey company.
   3  Registrar Account — Submit a request to open a Registrar account for this project.
   4  Payment & Certificate — Pay the registration fee, then your Real Estate Project Approval Certificate is issued.

3. Two buttons, centred side by side beneath the cards: secondary "View Application", blue primary "Back to Projects".
```

---

## S13 – 07 · Application Details — Under Review

```
Create a new screen frame named "S13 – 07 Application Details Under Review", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 07 Application Details Under Review
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Details", subtitle "APP-2026-0221 — Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, the vertical status timeline pattern. Do not invent new colours, type scales, or card treatments.

Keep it simple: a single stacked column of cards, no tabs, no side panel, no charts.

This screen shows the SAME application as S13 – 06, at a later point — RERA is still reviewing it, none of the later stages have happened yet.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0221

2. Page header row: heading "APP-2026-0221" with the status pill "Under Review" beside it on the left. On the right, secondary button "Download Summary".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0221
   SERVICE NAME: Registration of Real Estate Project
   STATUS: Under Review (pill)
   SUBMITTED ON: Aug 15, 2026 — 9:42 AM
   CREATED BY: Adaeze Nwosu

4. Card — "Application Status". A vertical timeline, one row per stage, each with a small circular marker on a connecting line, the stage name, a timestamp and the actor. Completed stages use the filled marker, the current stage uses the active marker, future stages use an empty outlined marker:
   Draft — Aug 14, 2026, 2:10 PM — Adaeze Nwosu  (complete)
   Submitted — Aug 15, 2026, 9:42 AM — Adaeze Nwosu  (complete)
   Under Review — Aug 15, 2026, 9:45 AM — RERA, Compliance & Escrow Auditor  (current)
   Accepted — Pending  (future)
   Units Uploaded — Pending  (future)
   Registrar Account Requested — Pending  (future)
   Payment Successful — Pending  (future)
   Registered — Pending  (future)

5. Card — "Project Information". Read-only label/value grid:
   Project Name: Gwarinpa Heights
   Project Location: Plot 14, Gwarinpa District, Abuja Municipal Area Council, FCT
   Project Type: Mixed Use
   Number of Units: 86

6. Card — "Survey Information". Read-only label/value grid:
   Survey Company: Meridian Geospatial Surveys Ltd.
   Survey Reference: SUR-2026-00812
   Survey Date: Aug 10, 2026

7. Card — "Supporting Documents". Table with columns Document Name · Requirement · Status · Action, four rows, all Uploaded, action "View":
   Real Estate License, Land Title Documents, Survey Report from Approved Survey Company, Project Master Plan — all Required.

8. A single-line inline notice beneath the documents card, using the existing subtle notice style: "Once RERA accepts this application, an 'Upload Units' action will appear here."
```

---

## S13 – 08 · Upload Units

```
Create a new screen frame named "S13 – 08 Upload Units", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 08 Upload Units
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Upload Units", subtitle "APP-2026-0221 — Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, data tables, inline notices, the File Upload Component. Do not invent new colours, type scales, or card treatments.

Keep it simple: one status card, one upload card, one table. No illustrations, no floor-plan graphics.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0221 / Upload Units

2. Page header row: heading "Upload Units" with the status pill "Accepted" beside it on the left. On the right, a blue primary button "Submit Unit Data".

3. A success notice card, full width, using the existing subtle success treatment: a green check icon on the left, then bold text "Application Accepted by RERA" and a grey line beneath: "Accepted on Aug 18, 2026. You may now upload the project's units through your approved survey company."

4. Application metadata strip:
   APPLICATION ID: APP-2026-0221
   SERVICE NAME: Registration of Real Estate Project
   STATUS: Accepted (pill)
   ACCEPTED ON: Aug 18, 2026 — 11:15 AM

5. Card — "Unit Data Source". Read-only panel:
   Survey Company: Meridian Geospatial Surveys Ltd. (RERA-approved)
   Survey Reference: SUR-2026-00812
   A single-line inline notice beneath: "Unit data must come through this survey company. Self-reported unit data is not accepted."
   Beneath the notice, a File Upload Component labelled "Unit Survey Data File", showing an uploaded state: "gwarinpa-heights-unit-schedule.xlsx — Uploaded Aug 18, 2026" with a "Replace" action.

6. Card — "Unit Summary". A small table, columns Unit Type · Count · Status:
     2-Bedroom Apartment — 34 — Ready
     3-Bedroom Apartment — 28 — Ready
     Retail Unit — 12 — Ready
     Office Suite — 12 — Ready
   Beneath the table, a total row: "86 units total"

7. Bottom-right: blue primary button "Submit Unit Data".
```

---

## S13 – 09 · Registrar Account Request

```
Create a new screen frame named "S13 – 09 Registrar Account Request", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 09 Registrar Account Request
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Registrar Account Request", subtitle "APP-2026-0221 — Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: one status card, one summary card, one confirmation panel. No illustrations.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0221 / Registrar Account Request

2. Page header row: heading "Registrar Account Request" with the status pill "Units Uploaded" beside it on the left. On the right, a blue primary button "Request Registrar Account".

3. A success notice card, full width: a green check icon on the left, bold text "86 Units Successfully Uploaded" and a grey line beneath: "Uploaded on Aug 19, 2026 via Meridian Geospatial Surveys Ltd. You can now request a Registrar account to open this project's official record."

4. Application metadata strip:
   APPLICATION ID: APP-2026-0221
   SERVICE NAME: Registration of Real Estate Project
   STATUS: Units Uploaded (pill)
   UNITS UPLOADED ON: Aug 19, 2026 — 3:20 PM

5. Card — "Project Summary". Read-only label/value grid:
   Project Name: Gwarinpa Heights
   Project Location: Plot 14, Gwarinpa District, Abuja Municipal Area Council, FCT
   Project Type: Mixed Use
   Total Units: 86
   Survey Company: Meridian Geospatial Surveys Ltd.
   Real Estate License: RERA-DEV-2024-00437

6. Card — "Registrar Account Request". A short explanation line: "Requesting a Registrar account opens this project's official record with RERA. This is required before the registration fee can be paid." Beneath it, a single confirmation checkbox: "I confirm the project and unit information above is accurate, and request that a Registrar account be opened for this project."

7. Bottom-right: blue primary button "Request Registrar Account".
```

---

## S13 – 10 · Payment

```
Create a new screen frame named "S13 – 10 Payment", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 10 Payment
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment", subtitle "APP-2026-0221 — Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value rows, radio groups, inline notices. Do not invent new colours, type scales, or card treatments. Match the Payment History screen's fee-breakdown treatment.

Keep it simple: two stacked cards, plain radio list for payment method, no card-brand logos, no illustrations.

IMPORTANT: this is the only point in the whole journey where a fee is shown. Do not add any fee amount, payment card, or payment call-to-action to any earlier screen in this pack.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0221 / Payment

2. Page header row: heading "Payment" with the status pill "Registrar Account Requested" beside it on the left.

3. Application metadata strip:
   APPLICATION ID: APP-2026-0221
   SERVICE NAME: Registration of Real Estate Project
   STATUS: Payment Pending (pill)
   REGISTRAR ACCOUNT REFERENCE: REG-ACC-2026-0143

4. Card — "Fee Breakdown". A simple stacked list of label/amount rows, right-aligned amounts, with a divider before the total:
   Registration Fee — ₦850,000
   Processing Levy — ₦15,000
   VAT (7.5%) — ₦64,875
   — divider —
   Total Amount Due — ₦929,875  (larger, bold)
   Beneath the total, one small grey line: "Paid by the company via the shared platform payment gateway."

5. Card — "Payment Method". A vertical radio group with three plain options, first one selected:
   Card Payment
   Bank Transfer
   USSD
   No logos or brand marks — text labels only, each with a short grey helper line beneath ("Pay with a debit or credit card", "Transfer to a generated account number", "Pay from your mobile phone").

6. A single-line inline notice beneath the cards: "Your Real Estate Project Approval Certificate is issued once this payment is confirmed."

7. Bottom-right: blue primary button "Pay ₦929,875".
```

---

## S13 – 11 · Registration Confirmation

```
Create a new screen frame named "S13 – 11 Registration Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 11 Registration Confirmation
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Project Registered", subtitle "APP-2026-0221 — Registration of Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, document table rows, success icon treatment, the vertical status timeline. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. Do not draw a decorative certificate, seal, border, or watermark — the output document is represented as a document record with actions, not as a rendered certificate graphic.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0221 / Registration Confirmation

2. Page header row: heading "APP-2026-0221" with the status pill "Registered" beside it on the left. On the right, secondary button "View Project" and blue primary button "Download Certificate".

3. A success notice card, full width, using the existing subtle success treatment: a green check icon on the left, then bold text "Project Successfully Registered" and a grey line beneath: "Approved on Aug 21, 2026. Gwarinpa Heights is now a registered real estate project — property registrations, sales, and escrow activity can proceed under it."

4. Card — "Application Status". The same vertical timeline as S13 – 07, now with every stage marked complete:
   Draft — Aug 14, 2026, 2:10 PM — Adaeze Nwosu  (complete)
   Submitted — Aug 15, 2026, 9:42 AM — Adaeze Nwosu  (complete)
   Under Review — Aug 15, 2026, 9:45 AM — RERA, Compliance & Escrow Auditor  (complete)
   Accepted — Aug 18, 2026, 11:15 AM — RERA, Compliance & Escrow Auditor  (complete)
   Units Uploaded — Aug 19, 2026, 3:20 PM — Adaeze Nwosu  (complete)
   Registrar Account Requested — Aug 19, 2026, 3:31 PM — Adaeze Nwosu, REG-ACC-2026-0143  (complete)
   Payment Successful — Aug 20, 2026, 10:05 AM — ₦929,875, PAY-2026-01044  (complete)
   Registered — Aug 21, 2026, 4:12 PM — RERA, Registrar  (complete)

5. Card — "Project Record". Two-column label/value grid:
   Project Reference Number: PRJ-2026-0022
   Project Approval Certificate Number: RERA-CERT-PRJ-2026-00341
   Registration Date: Aug 21, 2026
   Registrar Account Reference: REG-ACC-2026-0143
   Real Estate License: RERA-DEV-2024-00437
   Project Name: Gwarinpa Heights
   Project Location: Plot 14, Gwarinpa District, Abuja Municipal Area Council, FCT  (full width row)
   Project Type: Mixed Use
   Total Units: 86
   Survey Company: Meridian Geospatial Surveys Ltd.

6. Card — "Output Documents". A document table with columns Document Name · Type · Issued · Action:
   Real Estate Project Approval Certificate — RERA-CERT-PRJ-2026-00341.pdf — Approval Certificate — Aug 21, 2026 — View / Download
   Payment Receipt — PAY-2026-01044.pdf — Receipt — Aug 20, 2026 — View / Download

7. Card — "Application Record". Read-only label/value grid:
   Application Reference: APP-2026-0221
   Service Name: Registration of Real Estate Project
   Submitted On: Aug 15, 2026 — 9:42 AM
   Accepted On: Aug 18, 2026 — 11:15 AM
   Registered On: Aug 21, 2026 — 4:12 PM
   Total Amount Paid: ₦929,875
   Filed By: Adaeze Nwosu — Project Registration Officer

8. Bottom-right: blue primary button "Download Certificate".
```
