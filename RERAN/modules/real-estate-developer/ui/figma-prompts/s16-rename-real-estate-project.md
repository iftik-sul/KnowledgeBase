---
project: RERAN
module: real-estate-developer
type: reference-sample
status: draft
contains_proposals: true
written_against_specs_on: 2026-08-20
derived_from:
  - "RERAN/modules/real-estate-developer/service-flows/service-16-rename-real-estate-project.md"
  - "RERAN/modules/real-estate-developer/ui/screens/project-details.md"
  - "RERAN/modules/real-estate-developer/ui/figma-prompts/s13-register-real-estate-project.md"
  - "RERAN/modules/real-estate-developer/ui/figma-prompts/nav-sidebar-landing-screens.md"
tags:
  - real-estate-developer
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in [`../screens/`](../screens/) and [`service-16-rename-real-estate-project.md`](../../service-flows/service-16-rename-real-estate-project.md); where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Service #16: Changing the Name of a Real Estate Project

**Module:** Real Estate Developer (RERAN Group B)
**Screens:** 4, namespaced `S16 – 01` … `S16 – 04`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## Why this pack is a quarter the size of the other four

This is the deliberate floor of the set. Four fields, no fee, 30-minute processing, a five-state status flow — the simplest service in the entire module, picked specifically to contrast against `s13`'s ten-state multi-gate journey and `s24`'s two-payment amendment. Everything in this pack follows directly from that:

- **No horizontal step tracker anywhere.** Every other pack in this folder has one, because every other service genuinely has multiple stages to move through before submission. This one doesn't — putting a 1-of-1 tracker on a single-screen form would manufacture complexity that isn't there.
- **No payment screen, no payment confirmation, no fee breakdown.** Sourced directly — this service has no RERA fee at all.
- **One form screen, not three or four.** Name, reason, and an optional supporting document all fit on one screen, because that's genuinely all the source asks for.
- **The whole journey from submission to output happens same-day** — the source's own 30-minute processing time is short enough that this pack's dates and times reflect that literally, unlike every other pack's multi-day timelines.

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | **Supporting document is optional, not required** | Sourced — the service file lists "Board Resolution or Equivalent Authorization... (where applicable)," conditioned rather than mandatory, and flags the whole document list as `contains_proposals: true`. |
| 2 | **This is shown as a standalone service request, not reached only from Project Details** | Both are valid entry points per the service file's own UI Screens list (Project Details, Application Submitted); this pack shows the Service Details / Start Application route, consistent with every other pack in the folder. |
| 3 | **Project Name field is disabled elsewhere in the module while this or Service #24 amends it** | Not sourced — a reasonable UI safeguard against the confirmed overlap between the two services, flagged as proposed. |

---

## Consistent sample data across all screens

- Application ID: `APP-2026-0249`
- Company: Crestwood Developments Ltd. · `DEV-2024-00437`
- Filer / acting officer: Adaeze Nwosu — Project Registration Officer
- Project: `PRJ-2026-0019` · Current Name: "Lekki Pearl Estate" · Proposed New Name: "Lekki Pearl Residences"
- Reason: "Rebranding to align with updated marketing materials and reflect the project's residential-only unit mix."
- Updated Real Estate Project Approval Certificate Number: `RERA-CERT-PRJ-2026-00298` (revised)
- Processing time: 30 minutes
- Approving authority: RERA — Compliance & Escrow Auditor

---

## S16 – 01 · Service Details

```
Create a new screen frame named "S16 – 01 Service Details", 1440px wide, light grey background.

Layer structure exactly:
- S16 – 01 Service Details
  - RED-Sidebar       (instance of the existing sidebar component — do not redraw it; active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Details", subtitle "Changing the Name of a Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, breadcrumbs, section headers, label/value field grids. Do not invent new colours, new type scales, or new card treatments.

Keep it simple: stacked white cards, one blue primary action, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Projects / Changing the Name of a Real Estate Project

2. Page header row: heading "Changing the Name of a Real Estate Project" on the left. On the right, a secondary button "Back to Projects" and a blue primary button "Start Application".

3. Card — "Service Overview". Two-column label/value grid:
   Service Code: #16
   Service Category: Real Estate Development Services
   Processing Time: 30 minutes
   Applicable Fee: None — no RERA fee applies to this service
   Approving Authority: RERA — Compliance & Escrow Auditor
   Payment Timing: Not applicable — no fee is charged
   Below the grid, a full-width description paragraph: "Renames a registered project — for example following a rebrand — without affecting its underlying registration or unit set."

4. A single-line inline notice beneath the Service Overview card, using the existing subtle notice style: "A name change may also be submitted through the broader Register/Amend Project Details service if it accompanies other changes. Neither route is required over the other — use whichever fits what you're changing."

5. Card — "What You'll Need". A simple bulleted list, no two-column split needed — this service is small enough for one column:
   Project reference number
   Proposed new project name
   Reason for the name change
   Board resolution or equivalent authorization, if your organization requires one for this kind of change (optional)

6. Card — "Prerequisites". A short vertical list of check-style rows:
   An existing registered project
   A proposed new project name

7. Card — "Who Can Apply". Two short label/value rows:
   Applicant: Any of the company's Group B users
   Typical Filer: Project Registration Officer (customary practice, not a restriction — see navigation.md)

8. Bottom-right: blue primary button "Start Application".
```

---

## S16 – 02 · Name Change Request

```
Create a new screen frame named "S16 – 02 Name Change Request", 1440px wide, light grey background.

Layer structure exactly:
- S16 – 02 Name Change Request
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Change Project Name", subtitle "PRJ-2026-0019 — Lekki Pearl Estate")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, form inputs, the application metadata strip, the File Upload Component, a declaration checkbox row.

Keep it simple: ONE card holding the whole form, plus one declaration card. No step tracker — this is a single-screen application, not a multi-step wizard. No illustrations.

IMPORTANT: do not add a horizontal step progress tracker to this screen. Every other service pack in this file uses one; this service genuinely has only one step, and adding a tracker here would misrepresent how simple it is.

Workspace content, top to bottom:

1. Breadcrumb: Projects / PRJ-2026-0019 — Lekki Pearl Estate / Change Project Name

2. Page header row: heading "Change Project Name" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, five fields across:
   APPLICATION ID: APP-2026-0249
   SERVICE NAME: Changing the Name of a Real Estate Project
   STATUS: Draft (status pill)
   LAST UPDATED: Aug 19, 2026 — 9:58 AM
   CREATED BY: Adaeze Nwosu

4. Card — "Name Change Details". A single form, one column, generously spaced since there are only a few fields:
   Project Reference Number — read-only value "PRJ-2026-0019"
   Current Project Name — read-only value "Lekki Pearl Estate"
   Proposed New Project Name — editable text input, value "Lekki Pearl Residences", marked required
   Reason for Name Change — text area, value "Rebranding to align with updated marketing materials and reflect the project's residential-only unit mix.", marked required
   Beneath the form, a File Upload Component labelled "Board Resolution or Equivalent Authorization (optional)", shown empty with an "Upload" action and a small grey helper line: "Only needed if your organization requires formal authorization for this kind of change."

5. Card — "Declaration". A checked checkbox with the text: "I confirm that this name change does not affect the project's registration, unit set, or any active applications against it, and that the information provided is accurate."

6. Bottom-right: blue primary button "Submit Application". No "Continue" button — this is the final step.
```

---

## S16 – 03 · Application Submitted

```
Create a new screen frame named "S16 – 03 Application Submitted", 1440px wide, light grey background.

Layer structure exactly:
- S16 – 03 Application Submitted
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Submitted", subtitle "Changing the Name of a Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, success icon treatment.

Keep it simple: one centred confirmation card. No "what happens next" card needed — there's only one remaining step, and it happens in minutes.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Application Submitted"
   - Sub-line, centred, grey: "Your name change request has been sent to RERA. This service is typically decided within 30 minutes — no payment or additional steps are required."
   - The reference, centred and large: APP-2026-0249
   - A divider
   - A two-column label/value grid:
       Service Name: Changing the Name of a Real Estate Project
       Status: Under Review (status pill)
       Submitted On: Aug 19, 2026 — 10:00 AM
       Submitted By: Adaeze Nwosu
       Expected Decision Time: 30 minutes

2. Two buttons, centred side by side: secondary "View Application", blue primary "Back to Projects".
```

---

## S16 – 04 · Name Change Confirmation

```
Create a new screen frame named "S16 – 04 Name Change Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S16 – 04 Name Change Confirmation
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Project Renamed", subtitle "APP-2026-0249 — Changing the Name of a Real Estate Project")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, document table rows, success icon treatment.

Keep it simple: stacked white cards. Do not draw a decorative certificate graphic — the output is a document record with actions.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0249 / Name Change Confirmation

2. Page header row: heading "APP-2026-0249" with the status pill "Renamed" beside it on the left. On the right, secondary button "View Project" and blue primary button "Download Certificate".

3. A success notice card, full width: a green check icon, bold text "Project Name Successfully Changed" and a grey line beneath: "Approved by RERA on Aug 19, 2026 — decided in 28 minutes. Lekki Pearl Estate is now officially Lekki Pearl Residences."

4. Card — "Project Record". Two-column label/value grid:
   Project Reference Number: PRJ-2026-0019
   Previous Name: Lekki Pearl Estate
   New Name: Lekki Pearl Residences
   Name Changed On: Aug 19, 2026
   Registration Number, Unit Set and Development Stage: Unaffected by this change

5. Card — "Output Documents". A document table with columns Document Name · Type · Issued · Action:
   Updated Real Estate Project Approval Certificate — RERA-CERT-PRJ-2026-00298.pdf — Approval Certificate (Revised) — Aug 19, 2026 — View / Download

6. Card — "Application Record". Application Reference APP-2026-0249 · Submitted On Aug 19, 2026 — 10:00 AM · Approved On Aug 19, 2026 — 10:28 AM · Filed By Adaeze Nwosu — Project Registration Officer.

7. Bottom-right: blue primary button "Download Certificate".
```
