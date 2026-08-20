---
project: RERAN
module: real-estate-developer
type: reference-sample
status: draft
contains_proposals: true
written_against_specs_on: 2026-08-20
derived_from:
  - "RERAN/modules/real-estate-developer/service-flows/service-24-register-amend-project-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/project-details.md"
  - "RERAN/modules/real-estate-developer/ui/figma-prompts/s13-register-real-estate-project.md"
  - "RERAN/modules/real-estate-developer/ui/figma-prompts/nav-sidebar-landing-screens.md"
tags:
  - real-estate-developer
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in [`../screens/`](../screens/) and [`service-24-register-amend-project-details.md`](../../service-flows/service-24-register-amend-project-details.md); where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Service #24: Registration/Amendment of Real Estate Project Details

**Module:** Real Estate Developer (RERAN Group B)
**Screens:** 11, namespaced `S24 – 01` … `S24 – 11`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## What makes this one different from the other four packs

Two things, and neither appears anywhere else in this folder:

1. **Two separate payment stages, not one.** Sourced directly, Section 9: an *application approval fee* paid before the Survey Department reviews the amendment, and a second *approval fee in the real estate records* paid after RERA approves, before the output is issued. `S24 – 04`/`S24 – 05` are the first payment; `S24 – 09` is the second, much later, after a full review cycle has already happened in between. These are not framed as one fee shown twice — they are genuinely two transactions, with two different receipts.

2. **The output depends on the project's own completion status**, decided automatically, not chosen by the developer: a completed project gets an **Electronic Certificate of Title / Title Deed**; an incomplete one gets an **Electronic Map**. Like Service #6's pack, this one shows two endings — `S24 – 10` is the main path (Banana Island Villas, still under construction, so it gets the Map), and `S24 – 11` is an alternate ending showing the Title Deed outcome, using a project that's actually complete.

Everything else about this service is an **amend**, not a **create** — Step 1 opens with the project's existing data already filled in, editable, rather than a blank form. That's a genuinely different interaction from every other pack in this folder, all of which start from nothing.

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | **Survey Department review sits between the two payment stages, as its own visible stage** | Sourced, corrected 2026-08-16 in the service file itself — this step was previously missing from three of the file's own sections and had to be added back in. Shown here as a distinct status on the timeline, not folded into "Under Review." |
| 2 | **Who pays the first fee is shown as the developer, via the shared gateway** | The source row attributes the transmission — possibly the payment — to the survey company rather than the developer; the service file flags this explicitly as unresolved. This pack follows the only payment route this module has (developer, via the gateway) and is proposed, not sourced. |
| 3 | **Project Name is shown as an editable field but left unchanged in the worked example** | The service file confirms a name change may be submitted through this service (the overlap with Service #16), so the field must exist — but changing it isn't the point of this particular walkthrough. |
| 4 | **Required documents follow the general pattern** | Not itemized in the source; carried through from the service file's own flagged proposal. |
| 5 | **The alternate ending reuses a project that's genuinely complete, not a hypothetical one** | Apo Green Residences already exists in this module's sample data (`nav-sidebar-landing-screens.md`'s Payment History, "an older completed project") — reused here rather than inventing a new project just to demonstrate the branch. |

---

## Consistent sample data — main path (`S24 – 02` through `S24 – 10`)

- Application ID: `APP-2026-0241`
- Company: Crestwood Developments Ltd. · `DEV-2024-00437`
- Filer / acting officer: Adaeze Nwosu — Project Registration Officer
- Project being amended: Banana Island Villas · `PRJ-2026-0014` · Residential · **Completion Status: Not Completed** (Construction, 62%)
- Amendment: Number of Units — was 62, updated to **68** · Project Location refined to "Plot 7, Banana Island, Ikoyi, Lagos" · Project Name — unchanged, "Banana Island Villas"
- Survey Company confirming the amendment: Meridian Geospatial Surveys Ltd. (RERA-approved) · Survey Reference `SUR-2026-00847`
- Stage 1 — Application Approval Fee: ₦25,000 + Processing Levy ₦1,500 = **₦26,500** · Payment Reference `PAY-2026-01130`
- Stage 2 — Approval Fee in the Real Estate Records: ₦60,000 + Processing Levy ₦3,000 = **₦63,000** · Payment Reference `PAY-2026-01158`
- Output: Electronic Map `EMAP-2026-00241`

## Sample data — alternate ending (`S24 – 11` only)

- Application ID: `APP-2026-0210`
- Project: Apo Green Residences · Ibadan, Oyo State · Residential · **Completion Status: Completed**
- Amendment: corrected unit specification data following a post-completion survey
- Filed Jul 5, 2026 · Approved Jul 12, 2026 · Issued Jul 15, 2026
- Output: Electronic Certificate of Title `RERA-COT-2026-00210`

---

## S24 – 01 · Service Details

```
Create a new screen frame named "S24 – 01 Service Details", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 01 Service Details
  - RED-Sidebar       (instance of the existing sidebar component — do not redraw it; active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Details", subtitle "Registration/Amendment of Real Estate Project Details")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, tables, breadcrumbs, section headers, label/value field grids, icons. Do not invent new colours, new type scales, or new card treatments.

Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Projects / Registration/Amendment of Real Estate Project Details

2. Page header row: heading "Registration/Amendment of Real Estate Project Details" on the left. On the right, a secondary button "Back to Projects" and a blue primary button "Start Application".

3. Card — "Service Overview". Two-column label/value grid:
   Service Code: #24
   Service Category: Title Deed Data Services
   Processing Time: 5 business days
   Applicable Fee: Two stages — ₦25,000 before Survey Department review, ₦60,000 after RERA approval
   Approving Authority: RERA — Survey Department (initial review), RERA — Compliance & Escrow Auditor (final decision)
   Payment Timing: Two separate payments — one before review, one after approval
   Below the grid, a full-width description paragraph: "Keeps a project's Title Deed data record current as project details change. The output depends on the project's completion status: a completed project receives a Title Deed, an incomplete one receives an Electronic Map."

4. A single-line inline notice beneath the Service Overview card, using the existing subtle notice style: "This service charges two separate fees at two different points in the process — not one fee shown twice. You'll pay again after RERA approves, before your output document is issued."

5. Card — "How It Works". A single horizontal row of four numbered steps, evenly spaced, each with a number badge and a short label underneath:
   1 Project Details · 2 Documents · 3 Application Approval Fee · 4 Review & Submit
   Beneath the row, a single grey line: "After submission, the Survey Department confirms your updated data before RERA makes its final decision. A second fee is charged after approval, before your output document is issued."

6. Card — "What You'll Need". Two columns side by side.
   Left column heading "Required Information", as a simple bulleted list:
     Project reference number
     Updated project detail fields — this may include the project name
     Project completion status
   Right column heading "Required Documents", as a list of rows, each with the document name and a small requirement pill:
     Supporting Evidence for the Updated Details — Required
     Other Supporting Documents — Optional

7. Card — "Prerequisites". A short vertical list of check-style rows:
   An existing registered project
   Updated project detail data to register or amend

8. Card — "Who Can Apply". Two short label/value rows:
   Applicant: Any of the company's Group B users
   Typical Filer: Project Registration Officer (customary practice, not a restriction — see navigation.md)

9. A single-line inline notice, using the existing subtle notice style: "A project name change can be submitted here, or through the narrower, no-fee Rename Project service. Neither route is required over the other."

10. Bottom-right: blue primary button "Start Application".
```

---

## S24 – 02 · Step 1 — Project Details

```
Create a new screen frame named "S24 – 02 Project Details", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 02 Project Details
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Amend Project Details", subtitle "PRJ-2026-0014 — Banana Island Villas")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, section headers. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action.

IMPORTANT: unlike every other service pack in this folder, this form opens PRE-FILLED with the project's existing data, not blank. This is an amendment, not a new registration.

Workspace content, top to bottom:

1. Breadcrumb: Projects / PRJ-2026-0014 — Banana Island Villas / Amend Project Details

2. Page header row: heading "Amend Project Details" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, five fields across:
   APPLICATION ID: APP-2026-0241
   SERVICE NAME: Registration/Amendment of Real Estate Project Details
   STATUS: Draft (status pill)
   LAST UPDATED: Aug 17, 2026 — 10:50 AM
   CREATED BY: Adaeze Nwosu

4. Horizontal step progress tracker, four steps, step 1 active and steps 2–4 upcoming:
   1. Project Details · 2. Documents · 3. Application Approval Fee · 4. Review & Submit

5. Card — "Project Being Amended", read-only summary strip: "PRJ-2026-0014 — Banana Island Villas · Residential · Not Completed (Construction, 62%)".

6. Card — "Current vs. Updated Details". A two-column comparison layout, with a small grey "Current" heading over the left column and "Updated" over the right, for each field:
   Project Name — Current: "Banana Island Villas" (read-only) — Updated: editable text input, value "Banana Island Villas" (unchanged)
   Number of Units — Current: "62" (read-only) — Updated: editable text input, value "68"
   Project Location — Current: "Banana Island, Lagos" (read-only) — Updated: editable text input, value "Plot 7, Banana Island, Ikoyi, Lagos"
   Beneath the comparison, a small grey helper line: "Only fields you change will be reflected in the amendment. Project Name may be changed here — see the note on the Service Details screen."

7. Card — "Reason for Amendment". A text area, value "Unit count increased following final architectural approval; location detail refined to plot-level precision for Title Deed accuracy."

8. Step navigation row at the bottom: secondary button "Back" (disabled) on the left, blue primary button "Continue" on the right.
```

---

## S24 – 03 · Step 2 — Documents

```
Create a new screen frame named "S24 – 03 Documents", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 03 Documents
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Amend Project Details", subtitle "PRJ-2026-0014 — Banana Island Villas")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, the document table, requirement pills, status pills. Do not invent new colours, type scales, or card treatments.

Keep it simple: one table inside one card.

Workspace content, top to bottom:

1. Breadcrumb: Projects / PRJ-2026-0014 — Banana Island Villas / Amend Project Details

2. Page header row: heading "Amend Project Details" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous step.

4. Horizontal step progress tracker, four steps, step 1 complete, step 2 active.

5. Card — "Supporting Documents". Under the heading, a small grey counter line: "1 of 1 required documents uploaded". On the right of the card header, a secondary text action "Attach from Documents".
   Table with columns: Document Name · Requirement · Status · Action
     Supporting Evidence for the Updated Details — Required — Uploaded — View / Replace
     Other Supporting Documents — Optional — Not Uploaded — Upload

6. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S24 – 04 · Step 3 — Application Approval Fee

```
Create a new screen frame named "S24 – 04 Application Approval Fee", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 04 Application Approval Fee
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Amend Project Details", subtitle "PRJ-2026-0014 — Banana Island Villas")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, label/value rows, radio groups, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: two stacked cards, plain radio list for payment method.

IMPORTANT: label this card clearly as the FIRST of two fees. The card heading and the fee label must both say "Application Approval Fee" — not just "Fee" or "Payment" — since a second, different-sized fee comes much later in this same application, after approval.

Workspace content, top to bottom:

1. Breadcrumb: Projects / PRJ-2026-0014 — Banana Island Villas / Amend Project Details

2. Page header row: heading "Amend Project Details" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Application Fee Pending".

4. Horizontal step progress tracker, four steps, steps 1–2 complete, step 3 active.

5. Card — "Application Approval Fee (1 of 2)". A simple stacked list of label/amount rows, right-aligned amounts, with a divider before the total:
   Application Approval Fee — ₦25,000
   Processing Levy — ₦1,500
   — divider —
   Total Amount Due Now — ₦26,500  (larger, bold)
   Beneath the total, a small grey line: "This fee sends your amendment to the Survey Department for review. A second, separate fee will be charged after RERA approves, before your output document is issued."

6. Card — "Payment Method". A vertical radio group with three plain options, first one selected: Card Payment · Bank Transfer · USSD, each with a short grey helper line beneath.

7. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Pay ₦26,500" on the right.
```

---

## S24 – 05 · Payment Confirmation — Stage 1

```
Create a new screen frame named "S24 – 05 Payment Confirmation Stage 1", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 05 Payment Confirmation Stage 1
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment Successful", subtitle "Amend Project Details")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, the horizontal step progress tracker, label/value rows, success icon treatment.

Keep it simple: one centred confirmation card.

Workspace content, top to bottom:

1. Horizontal step progress tracker, four steps, steps 1–3 complete, step 4 (Review & Submit) shown as next.

2. One centred card, roughly 720px wide, containing in this order:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Application Approval Fee Paid"
   - Sub-line, centred, grey: "This is the first of two fees for this application. You can now review and submit your amendment."
   - The amount, centred and large: ₦26,500
   - A divider
   - A two-column label/value grid:
       Payment Reference: PAY-2026-01130
       Payment Date: Aug 18, 2026 — 9:05 AM
       Payment Method: Card Payment
       Payment Status: Paid (green status pill)
       Application ID: APP-2026-0241
       Fee Stage: 1 of 2 — Application Approval Fee
   - A divider
   - Two buttons, centred side by side: secondary "Download Receipt", blue primary "Continue to Review"
```

---

## S24 – 06 · Step 4 — Review & Submit

```
Create a new screen frame named "S24 – 06 Review and Submit", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 06 Review and Submit
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Projects")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Review Application", subtitle "Amend Project Details")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, inline "Edit" links, the Validation Panel, a declaration checkbox row.

Keep it simple: stacked white cards, one blue primary action at the top and bottom.

Workspace content, top to bottom:

1. Breadcrumb: Projects / PRJ-2026-0014 — Banana Island Villas / Amend Project Details

2. Page header row: heading "Review Application" on the left. On the right, secondary button "Save Draft" and blue primary button "Submit for Survey Department Review".

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Ready for Review".

4. Horizontal step progress tracker, four steps, steps 1–3 complete, step 4 active.

5. Card — "Amended Details", with an inline "Edit" link. Same "Current vs. Updated" comparison layout as Step 1:
   Project Name — Current: "Banana Island Villas" — Updated: "Banana Island Villas" (unchanged)
   Number of Units — Current: "62" — Updated: "68"
   Project Location — Current: "Banana Island, Lagos" — Updated: "Plot 7, Banana Island, Ikoyi, Lagos"

6. Card — "Reason for Amendment": "Unit count increased following final architectural approval; location detail refined to plot-level precision for Title Deed accuracy."

7. Card — "Supporting Documents", counter line "1 of 1 required documents uploaded". Table with one Required row, Uploaded, action "View".

8. Card — "Payment Summary (Stage 1 of 2)": Application Approval Fee ₦25,000 · Processing Levy ₦1,500 · Total Paid ₦26,500 (larger, bold) · Payment Reference PAY-2026-01130 · Payment Status Paid (green pill). Beneath, a small grey line: "The second fee is charged after RERA approves this amendment — see Step 3 of what happens next."

9. Card — "Validation Summary", with a green sub-line "All checks passed", then a vertical list of green check rows:
   Required amendment fields completed
   Required documents provided
   Project exists and is registered
   First-stage payment completed
   Below a dotted divider, a green status line: "All Clear — Ready to Submit"

10. Card — "Declaration". A checked checkbox with the standard accuracy declaration text.

11. Bottom-right: blue primary button "Submit for Survey Department Review".
```

---

## S24 – 07 · Application Submitted — Survey Department Review

```
Create a new screen frame named "S24 – 07 Submitted for Survey Review", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 07 Submitted for Survey Review
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Submitted for Survey Department Review", subtitle "Amend Project Details")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, success icon treatment, numbered list rows.

Keep it simple: one centred confirmation card plus one short "what happens next" card.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Submitted for Survey Department Review"
   - Sub-line, centred, grey: "Your amendment is first confirmed by the Survey Department before RERA makes a final decision."
   - The reference, centred and large: APP-2026-0241
   - A divider
   - A two-column label/value grid:
       Service Name: Registration/Amendment of Real Estate Project Details
       Status: Survey Department Review (status pill)
       Submitted On: Aug 18, 2026 — 9:20 AM
       Submitted By: Adaeze Nwosu
       Stage 1 Fee Paid: ₦26,500

2. Card — "What Happens Next". Three numbered rows, each with a number badge, a short bold label and one grey line beneath:
   1  Survey Department Confirms Data — Reviews the updated details against survey records.
   2  RERA Review — RERA's Compliance & Escrow Auditor makes the final decision.
   3  Second Fee & Output — After approval, a second fee is charged, then your Electronic Certificate of Title or Electronic Map is issued, depending on the project's completion status.

3. Two buttons, centred side by side: secondary "View Application", blue primary "Back to Projects".
```

---

## S24 – 08 · Application Details — Under Review

```
Create a new screen frame named "S24 – 08 Application Details Under Review", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 08 Application Details Under Review
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Details", subtitle "APP-2026-0241 — Amend Project Details")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, the vertical status timeline pattern.

Keep it simple: a single stacked column of cards.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0241

2. Page header row: heading "APP-2026-0241" with the status pill "Under Review" beside it on the left. On the right, secondary button "Download Summary".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0241
   SERVICE NAME: Registration/Amendment of Real Estate Project Details
   STATUS: Under Review (pill)
   SUBMITTED ON: Aug 18, 2026 — 9:20 AM
   CREATED BY: Adaeze Nwosu

4. Card — "Application Status". A vertical timeline, one row per stage, each with a small circular marker on a connecting line:
   Draft — Aug 17, 2026, 10:50 AM — Adaeze Nwosu  (complete)
   Application Fee Paid — Aug 18, 2026, 9:05 AM — ₦26,500, PAY-2026-01130  (complete)
   Submitted — Aug 18, 2026, 9:20 AM — Adaeze Nwosu  (complete)
   Survey Department Review — Aug 18, 2026, 2:40 PM — Confirmed via Meridian Geospatial Surveys Ltd., SUR-2026-00847  (complete)
   Under Review — Aug 19, 2026, 8:10 AM — RERA, Compliance & Escrow Auditor  (current)
   Approved — Pending  (future)
   Approval Fee Pending — Pending  (future)
   Issued — Pending  (future)

5. Card — "Amended Details". Read-only comparison, same "Current vs. Updated" layout: Project Name (unchanged), Number of Units (62 → 68), Project Location (updated to plot-level detail).

6. Card — "Survey Confirmation". Read-only: Survey Company Meridian Geospatial Surveys Ltd. · Survey Reference SUR-2026-00847 · Confirmed Aug 18, 2026.

7. Card — "Supporting Documents". Table, one Required row, Uploaded.

8. Card — "Payment (Stage 1 of 2)". Total Paid ₦26,500 · Payment Reference PAY-2026-01130 · Payment Status Paid (green pill). Beneath, a grey line: "Stage 2 fee will appear here once RERA approves."
```

---

## S24 – 09 · Approval Fee — Stage 2

```
Create a new screen frame named "S24 – 09 Approval Fee Stage 2", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 09 Approval Fee Stage 2
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Approval Fee", subtitle "APP-2026-0241 — Amend Project Details")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value rows, radio groups, inline notices.

Keep it simple: one status card, one fee card, one payment method card.

IMPORTANT: this screen appears DAYS after S24 – 04's payment, on a different visit — this is not the same fee shown again. Label it clearly as "2 of 2" and make the amount visibly different (₦63,000 here vs. ₦26,500 earlier).

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0241 / Approval Fee

2. Page header row: heading "Approval Fee" with the status pill "Approved" beside it on the left.

3. A success notice card, full width: a green check icon on the left, bold text "Amendment Approved by RERA" and a grey line beneath: "Approved on Aug 21, 2026. Pay the approval fee in the real estate records to receive your output document."

4. Application metadata strip:
   APPLICATION ID: APP-2026-0241
   SERVICE NAME: Registration/Amendment of Real Estate Project Details
   STATUS: Approval Fee Pending (pill)
   APPROVED ON: Aug 21, 2026 — 11:30 AM

5. Card — "Approval Fee in the Real Estate Records (2 of 2)". A simple stacked list of label/amount rows, right-aligned amounts, with a divider before the total:
   Approval Fee in the Real Estate Records — ₦60,000
   Processing Levy — ₦3,000
   — divider —
   Total Amount Due Now — ₦63,000  (larger, bold)
   Beneath the total, a small grey line: "This is the second and final fee for this application. Your output document is issued once this payment is confirmed."

6. Card — "Payment Method". A vertical radio group with three plain options, first one selected: Card Payment · Bank Transfer · USSD.

7. Bottom-right: blue primary button "Pay ₦63,000".
```

---

## S24 – 10 · Registration Confirmation — Electronic Map

```
Create a new screen frame named "S24 – 10 Registration Confirmation Electronic Map", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 10 Registration Confirmation Electronic Map
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Amendment Complete", subtitle "APP-2026-0241 — Amend Project Details")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, document table rows, success icon treatment, the vertical status timeline.

Keep it simple: stacked white cards. Do not draw a decorative map graphic — the output is represented as a document record with actions.

IMPORTANT: this project (Banana Island Villas) is NOT completed — its output is an Electronic Map, not a Title Deed. Do not show a Certificate of Title on this screen.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0241 / Registration Confirmation

2. Page header row: heading "APP-2026-0241" with the status pill "Issued" beside it on the left. On the right, secondary button "View Project" and blue primary button "Download Map".

3. A success notice card, full width: a green check icon, bold text "Project Details Amendment Complete" and a grey line beneath: "Both fees are paid and your Electronic Map has been issued. Banana Island Villas is not yet a completed project, so a Map — not a Title Deed — is the correct output here."

4. Card — "Application Status". The same vertical timeline as S24 – 08, now with every stage complete, plus two additional rows:
   Draft — Aug 17, 2026, 10:50 AM — Adaeze Nwosu  (complete)
   Application Fee Paid — Aug 18, 2026, 9:05 AM — ₦26,500, PAY-2026-01130  (complete)
   Submitted — Aug 18, 2026, 9:20 AM — Adaeze Nwosu  (complete)
   Survey Department Review — Aug 18, 2026, 2:40 PM — Confirmed  (complete)
   Under Review — Aug 19, 2026, 8:10 AM — RERA, Compliance & Escrow Auditor  (complete)
   Approved — Aug 21, 2026, 11:30 AM — RERA, Compliance & Escrow Auditor  (complete)
   Approval Fee Paid — Aug 21, 2026, 11:52 AM — ₦63,000, PAY-2026-01158  (complete)
   Issued — Aug 22, 2026, 9:15 AM — Electronic Map issued  (complete)

5. Card — "Amended Project Record". Two-column label/value grid:
   Project: Banana Island Villas — PRJ-2026-0014
   Completion Status: Not Completed
   Output Document Type: Electronic Map (determined automatically by completion status)
   Number of Units: 68 (was 62)
   Project Location: Plot 7, Banana Island, Ikoyi, Lagos

6. Card — "Output Documents". A document table with columns Document Name · Type · Issued · Action:
   Electronic Map — EMAP-2026-00241.pdf — Electronic Map — Aug 22, 2026 — View / Download
   Payment Receipt (Stage 1) — PAY-2026-01130.pdf — Receipt — Aug 18, 2026 — View / Download
   Payment Receipt (Stage 2) — PAY-2026-01158.pdf — Receipt — Aug 21, 2026 — View / Download

7. Card — "Application Record". Application Reference APP-2026-0241 · Submitted On Aug 18, 2026 · Approved On Aug 21, 2026 · Total Amount Paid Across Both Stages: ₦89,500 · Filed By Adaeze Nwosu — Project Registration Officer.

8. Bottom-right: blue primary button "Download Map".
```

---

## S24 – 11 · Alternate Outcome — Electronic Certificate of Title

```
Create a new screen frame named "S24 – 11 Alternate Outcome Certificate of Title", 1440px wide, light grey background.

Layer structure exactly:
- S24 – 11 Alternate Outcome Certificate of Title
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Amendment Complete", subtitle "APP-2026-0210 — Amend Project Details")
    - Workspace

Reuse the exact same card structure and styles as S24 – 10.

THIS IS A DIFFERENT APPLICATION, ON A DIFFERENT PROJECT, FROM S24 – 10 — shown to demonstrate the OTHER possible output. Apo Green Residences IS a completed project, so this application produces a Title Deed instead of a Map. This is not a sequel to S24 – 10; it's an alternate scenario reached the same way but ending differently, because the underlying project's completion status differs.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0210 / Registration Confirmation

2. Page header row: heading "APP-2026-0210" with the status pill "Issued" beside it on the left. On the right, secondary button "View Project" and blue primary button "Download Certificate".

3. A success notice card, full width: a green check icon, bold text "Project Details Amendment Complete" and a grey line beneath: "Both fees are paid and your Electronic Certificate of Title has been issued. Apo Green Residences is a completed project, so a Title Deed — not a Map — is the correct output here. This is the same service as APP-2026-0241, producing the other possible output."

4. Card — "Application Status". A vertical timeline, all stages complete:
   Draft — Jul 4, 2026 — Adaeze Nwosu  (complete)
   Application Fee Paid — Jul 5, 2026 — ₦25,000 + levy  (complete)
   Submitted — Jul 5, 2026 — Adaeze Nwosu  (complete)
   Survey Department Review — Jul 6, 2026 — Confirmed  (complete)
   Under Review — Jul 8, 2026 — RERA, Compliance & Escrow Auditor  (complete)
   Approved — Jul 12, 2026 — RERA, Compliance & Escrow Auditor  (complete)
   Approval Fee Paid — Jul 12, 2026 — ₦60,000 + levy  (complete)
   Issued — Jul 15, 2026 — Electronic Certificate of Title issued  (complete)

5. Card — "Amended Project Record". Two-column label/value grid:
   Project: Apo Green Residences
   Location: Ibadan, Oyo State
   Completion Status: Completed
   Output Document Type: Electronic Certificate of Title / Title Deed (determined automatically by completion status)
   Amendment: Corrected unit specification data following a post-completion survey

6. Card — "Output Documents". A document table with columns Document Name · Type · Issued · Action:
   Electronic Certificate of Title — RERA-COT-2026-00210.pdf — Title Deed — Jul 15, 2026 — View / Download
   Payment Receipt (Stage 1) — Jul 5, 2026 — View / Download
   Payment Receipt (Stage 2) — Jul 12, 2026 — View / Download

7. Bottom-right: blue primary button "Download Certificate".
```
