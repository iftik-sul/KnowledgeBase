---
project: RERAN
module: real-estate-developer
type: reference-sample
status: draft
contains_proposals: true
written_against_specs_on: 2026-08-20
derived_from:
  - "RERAN/modules/real-estate-developer/service-flows/service-01-register-initial-sale.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registrations.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
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

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in [`../screens/`](../screens/) and [`service-01-register-initial-sale.md`](../../service-flows/service-01-register-initial-sale.md); where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Service #1: Register Initial Sale

**Module:** Real Estate Developer (RERAN Group B)
**Screens:** 10, namespaced `S1 – 01` … `S1 – 10`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## Why this one *does* use a single continuous wizard

Unlike Service #13, this service has no mid-flow gate — the source workflow runs straight through: select the unit, fill in sale and purchaser details, attach documents, pay, submit. Payment happens *before* submission, not after a multi-stage approval like #13. That makes this pack's shape closer to Group C's `s03` wizard than to `s13`'s split pattern — one 5-step tracker covers the whole application, and everything after submission is a single RERA review with no internal-certification stage (RED has no maker/checker concept — every application goes straight from the developer to RERA).

**One deliberate deviation from Group C's own step grouping:** Group C's `s03` folds "Select Property" into its second step, since that service is fundamentally about the mortgage, not the unit. This service is fundamentally about selling a specific unit, so **Select Property gets its own first step** here rather than being folded in — the more natural entry point for a sale.

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | **Payment sits before submission**, not after | Sourced directly — Section 9 states this is paid "before RERA's decision," and the workflow places "Select Payment Method" immediately before "Submit Application Online." |
| 2 | **No internal certification stage** | RED has no equivalent to Group C's maker/checker step — any of the four roles files and submits directly to RERA. This pack has no screen matching Group C's `S3 – 09`. |
| 3 | **Output is emailed to the purchaser; an in-app copy for the filer is proposed, not sourced** | The service file flags this explicitly (`contains_proposals: true`) — the source only says the certificate is emailed to the purchaser. This pack shows both, consistent with that flag. |
| 4 | **Required documents follow the general sale-registration pattern** | Not itemized field-by-field in the source; carried through from the service file's own proposal. |
| 5 | **This application continues the same sale already shown in the other two packs** | `APP-2026-0219` / Unit A-120, Banana Island Villas already appears "Approved" in `nav-sidebar-landing-screens.md`'s Applications screen, and the same sale appears as `SALE-2026-0087` on the Sales & Disclosures screen, and as a completed payment (`RCT-2026-0533`, ₦42,000) on Payment History. This pack tells that same sale's full application story. |

---

## Consistent sample data across all screens

- Application ID: `APP-2026-0219`
- Company: Crestwood Developments Ltd. · `DEV-2024-00437`
- Filer / acting officer: Ifeoma Chukwu — Sales & Disclosure Officer
- Project: Banana Island Villas · `PRJ-2026-0014` · Residential
- Unit: A-120 · 2-Bedroom Apartment · 145 sqm
- Purchaser: John Smith · NIN `NGA-58231940` · +234 803 221 7765 · john.smith@example.com
- Sale: Sale Value ₦185,000,000 · Payment Plan: Outright Payment · Agreed Sale Date Aug 3, 2026
- Fee: Registration Fee ₦40,000 · Processing Levy ₦2,000 · **Total ₦42,000**
- Payment Reference: `PAY-2026-00891`
- Provisional Registration e-Certificate Number: `RERA-PROV-2026-00219`
- Processing time: 6 business days
- Approving authority: RERA — Compliance & Escrow Auditor

---

## S1 – 01 · Service Details

```
Create a new screen frame named "S1 – 01 Service Details", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 01 Service Details
  - RED-Sidebar       (instance of the existing sidebar component — do not redraw it; active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Details", subtitle "Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, tables, breadcrumbs, section headers, label/value field grids, icons. Do not invent new colours, new type scales, or new card treatments. Match the spacing, corner radius, and white-card-on-grey treatment already used on the Dashboard and Applications screens.

Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Initial Sale

2. Page header row: heading "Register Initial Sale" on the left. On the right, a secondary button "Back to Property Registrations" and a blue primary button "Start Application".

3. Card — "Service Overview". Two-column label/value grid:
   Service Code: #1
   Service Category: Real Estate Development Services
   Processing Time: 6 business days
   Applicable Fee: ₦40,000 (per RERAN fee schedule)
   Approving Authority: RERA — Compliance & Escrow Auditor
   Payment Timing: Paid at submission, before RERA's review
   Below the grid, a full-width description paragraph: "Registers the provisional sale of a unit within a registered project — the first regulatory record that a specific unit has been sold to a purchaser, ahead of full title transfer."

4. Card — "How It Works". A single horizontal row of five numbered steps, evenly spaced, each with a number badge and a short label underneath:
   1 Select Property · 2 Sale & Purchaser Details · 3 Documents · 4 Payment · 5 Review & Submit
   Beneath the row, a single grey line: "Once submitted, RERA reviews the application directly — there is no internal certification stage in this module."

5. Card — "What You'll Need". Two columns side by side.
   Left column heading "Required Information", as a simple bulleted list:
     Project reference number and unit identifier
     Purchaser full name, National Identification Number and contact details
     Sale value, payment plan and agreed sale date
   Right column heading "Required Documents", as a list of rows, each with the document name and a small requirement pill:
     Provisional Sale Agreement — Required
     Purchaser Government-issued Identification — Required
     Proof of Initial Payment — Required
     Other Supporting Documents — Optional

6. Card — "Prerequisites". A short vertical list of check-style rows:
   Registered developer company account
   Real estate project already registered with RERA
   Property/unit exists within that project's approved unit list
   Purchaser identified

7. Card — "Who Can Apply". Two short label/value rows:
   Applicant: Any of the company's Group B users
   Typical Filer: Sales & Disclosure Officer (customary practice, not a restriction — see navigation.md)

8. Bottom-right: blue primary button "Start Application".
```

---

## S1 – 02 · Step 1 — Select Property

```
Create a new screen frame named "S1 – 02 Select Property", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 02 Select Property
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, search inputs, section headers. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, one search-and-select card, one blue primary action. No illustrations, no floor plans, no property photographs.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Initial Sale / New Application

2. Page header row: heading "Register Initial Sale" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, five fields across:
   APPLICATION ID: APP-2026-0219
   SERVICE NAME: Register Initial Sale
   STATUS: Draft (status pill)
   LAST UPDATED: Aug 9, 2026 — 1:15 PM
   CREATED BY: Ifeoma Chukwu

4. Horizontal step progress tracker, five steps, step 1 active and steps 2–5 upcoming:
   1. Select Property · 2. Sale & Purchaser Details · 3. Documents · 4. Payment · 5. Review & Submit

5. Card — "Select Project". A single search/select input labelled "Project Reference Number", value "PRJ-2026-0014 — Banana Island Villas". A small grey helper line beneath: "Only registered projects appear here."

6. Card — "Select Unit". At the top, a search input labelled "Unit Identifier", value "A-120". Beneath it, a selected-result panel using the existing subtle bordered treatment:
   Unit Identifier: A-120
   Unit Type: 2-Bedroom Apartment
   Unit Specifications: 145 sqm
   Availability: Available for Sale (green status pill)
   A text link "Change Unit" at the bottom of the panel.

7. Step navigation row at the bottom: secondary button "Back" (disabled) on the left, blue primary button "Continue" on the right.
```

---

## S1 – 03 · Step 2 — Sale & Purchaser Details

```
Create a new screen frame named "S1 – 03 Sale and Purchaser Details", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 03 Sale and Purchaser Details
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action. No illustrations.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Initial Sale / New Application

2. Page header row: heading "Register Initial Sale" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous step.

4. Horizontal step progress tracker, five steps, step 1 complete, step 2 active.

5. Card — "Selected Unit", read-only summary strip: "PRJ-2026-0014 — Banana Island Villas · Unit A-120 · 2-Bedroom Apartment, 145 sqm", with a text link "Change" on the right.

6. Card — "Purchaser Information". Editable form, two columns:
   Full Name — text input, value "John Smith"
   National Identification Number (NIN) — text input, value "NGA-58231940"
   Phone Number — text input, value "+234 803 221 7765"
   Email Address — text input, value "john.smith@example.com"
   Mark all four as required fields using the existing required-field treatment.

7. Card — "Sale Information". Editable form, two columns:
   Sale Value — text input, value "₦185,000,000"
   Payment Plan / Terms — dropdown, value "Outright Payment"
   Agreed Sale Date — text input, value "Aug 3, 2026"
   Mark all three as required.

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S1 – 04 · Step 3 — Documents

```
Create a new screen frame named "S1 – 04 Documents", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 04 Documents
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, the document table, requirement pills, status pills, link-style row actions, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: one table inside one card, no drag-and-drop illustration, no file thumbnails.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Initial Sale / New Application

2. Page header row: heading "Register Initial Sale" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps.

4. Horizontal step progress tracker, five steps, steps 1–2 complete, step 3 active.

5. Card — "Supporting Documents". Under the heading, a small grey counter line: "2 of 3 required documents uploaded". On the right of the card header, a secondary text action "Attach from Documents".
   Table with columns: Document Name · Requirement · Status · Action
     Provisional Sale Agreement — Required — Uploaded — View / Replace
     Purchaser Government-issued Identification — Required — Uploaded — View / Replace
     Proof of Initial Payment — Required — Not Uploaded — Upload
     Other Supporting Documents — Optional — Not Uploaded — Upload
   Use the existing requirement pill style for Required / Optional and the existing status pill style for Uploaded / Not Uploaded.

6. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S1 – 05 · Step 4 — Payment

```
Create a new screen frame named "S1 – 05 Payment", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 05 Payment
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, label/value rows, radio groups, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: two stacked cards, plain radio list for payment method, no card-brand logos, no illustrations.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Initial Sale / New Application

2. Page header row: heading "Register Initial Sale" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Payment Pending".

4. Horizontal step progress tracker, five steps, steps 1–3 complete, step 4 active.

5. Card — "Fee Breakdown". A simple stacked list of label/amount rows, right-aligned amounts, with a divider before the total:
   Registration Fee — ₦40,000
   Processing Levy — ₦2,000
   — divider —
   Total Amount Due — ₦42,000  (larger, bold)
   Beneath the total, one small grey line: "Paid by the company via the shared platform payment gateway."

6. Card — "Payment Method". A vertical radio group with three plain options, first one selected:
   Card Payment
   Bank Transfer
   USSD
   No logos or brand marks — text labels only, each with a short grey helper line beneath ("Pay with a debit or credit card", "Transfer to a generated account number", "Pay from your mobile phone").

7. A single-line inline notice beneath the cards: "Payment must be completed before this application can be submitted for review."

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Pay ₦42,000" on the right.
```

---

## S1 – 06 · Payment Confirmation

```
Create a new screen frame named "S1 – 06 Payment Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 06 Payment Confirmation
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment Successful", subtitle "Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, the horizontal step progress tracker, label/value rows, success icon treatment. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card, no illustration, no large graphics. Use the existing green success colour only for the check icon and the status pill.

Workspace content, top to bottom:

1. Horizontal step progress tracker, five steps, steps 1–4 complete, step 5 (Review & Submit) shown as next.

2. One centred card, roughly 720px wide, containing in this order:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Payment Successful"
   - Sub-line, centred, grey: "Your payment has been received. You can now review and submit this application to RERA."
   - The amount, centred and large: ₦42,000
   - A divider
   - A two-column label/value grid:
       Payment Reference: PAY-2026-00891
       Payment Date: Aug 10, 2026 — 2:47 PM
       Payment Method: Card Payment
       Payment Status: Paid (green status pill)
       Application ID: APP-2026-0219
       Service Name: Register Initial Sale
   - A divider
   - Two buttons, centred side by side: secondary "Download Receipt", blue primary "Continue to Review"
```

---

## S1 – 07 · Step 5 — Review & Submit

```
Create a new screen frame named "S1 – 07 Review and Submit", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 07 Review and Submit
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Review Application", subtitle "Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, inline "Edit" links, the Validation Panel, a declaration checkbox row. Do not invent new colours, type scales, or card treatments. Match the Applications screen's card treatment.

Keep it simple: stacked white cards, one blue primary action at the top and bottom. No illustrations.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Initial Sale / New Application

2. Page header row: heading "Review Application" on the left. On the right, secondary button "Save Draft" and blue primary button "Submit Application".

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Ready for Review".

4. Horizontal step progress tracker, five steps, steps 1–4 complete, step 5 active.

5. Card — "Property Information", with an inline "Edit" link in the card header:
   Project: Banana Island Villas — PRJ-2026-0014
   Unit Identifier: A-120
   Unit Type: 2-Bedroom Apartment
   Unit Specifications: 145 sqm

6. Card — "Purchaser Information", with an inline "Edit" link:
   Full Name: John Smith
   National Identification Number: NGA-58231940
   Phone Number: +234 803 221 7765
   Email Address: john.smith@example.com

7. Card — "Sale Information", with an inline "Edit" link:
   Sale Value: ₦185,000,000
   Payment Plan / Terms: Outright Payment
   Agreed Sale Date: Aug 3, 2026

8. Card — "Supporting Documents", counter line "3 of 3 required documents uploaded", inline action "Manage Documents". Table with columns Document Name · Requirement · Status · Action:
   Provisional Sale Agreement — Required — Uploaded — View
   Purchaser Government-issued Identification — Required — Uploaded — View
   Proof of Initial Payment — Required — Uploaded — View

9. Card — "Payment Summary":
   Registration Fee: ₦40,000
   Processing Levy: ₦2,000
   Total Amount Paid: ₦42,000 (larger, bold)
   Payment Reference: PAY-2026-00891
   Payment Date: Aug 10, 2026
   Payment Status: Paid (green pill with check)

10. Card — "Validation Summary", with a green sub-line "All checks passed", then a vertical list of green check rows:
    Required purchaser and sale information completed
    Required documents provided
    Unit belongs to a registered project
    Unit available for sale
    Payment completed
    Below a dotted divider, a green status line: "All Clear — Ready to Submit"

11. Card — "Declaration". A checked checkbox with the text: "I confirm that the information and documents provided in this application are accurate and complete. I understand that providing false or misleading information may result in application rejection, penalties, or regulatory action against the company."

12. Bottom-right: blue primary button "Submit Application".
```

---

## S1 – 08 · Application Submitted

```
Create a new screen frame named "S1 – 08 Application Submitted", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 08 Application Submitted
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Submitted", subtitle "Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, success icon treatment, numbered list rows. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card plus one short "what happens next" card. No illustration, no large graphics.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Application Submitted"
   - Sub-line, centred, grey: "Your sale registration application has been sent to RERA for review."
   - The reference, centred and large: APP-2026-0219
   - A divider
   - A two-column label/value grid:
       Service Name: Register Initial Sale
       Status: Under Review (status pill)
       Submitted On: Aug 10, 2026 — 3:02 PM
       Submitted By: Ifeoma Chukwu
       Expected Review Time: 6 business days
       Total Amount Paid: ₦42,000

2. Card — "What Happens Next". Two numbered rows, each with a number badge, a short bold label and one grey line beneath:
   1  RERA Review — RERA's Compliance & Escrow Auditor reviews this application. There is no internal certification stage in this module — any of your company's users may track and act on this application, including you.
   2  Provisional Registration — On approval, a Provisional Registration e-Certificate is issued and emailed to the purchaser.

3. Two buttons, centred side by side beneath the cards: secondary "View Application", blue primary "Back to Property Registrations".
```

---

## S1 – 09 · Application Details — Under Review

```
Create a new screen frame named "S1 – 09 Application Details Under Review", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 09 Application Details Under Review
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Details", subtitle "APP-2026-0219 — Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, the vertical status timeline pattern, the activity feed row pattern from the Dashboard. Do not invent new colours, type scales, or card treatments.

Keep it simple: a single stacked column of cards, no tabs, no side panel, no charts.

This screen shows the SAME application as S1 – 08, at a later point — RERA is still reviewing it.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0219

2. Page header row: heading "APP-2026-0219" with the status pill "Under Review" beside it on the left. On the right, secondary button "Download Summary" and secondary button "Withdraw Application".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0219
   SERVICE NAME: Register Initial Sale
   STATUS: Under Review (pill)
   SUBMITTED ON: Aug 10, 2026 — 3:02 PM
   CREATED BY: Ifeoma Chukwu

4. Card — "Application Status". A vertical timeline, one row per stage, each with a small circular marker on a connecting line, the stage name, a timestamp and the actor. Completed stages use the filled marker, the current stage uses the active marker, future stages use an empty outlined marker:
   Draft — Aug 9, 2026, 1:15 PM — Ifeoma Chukwu  (complete)
   Payment Successful — Aug 10, 2026, 2:47 PM — ₦42,000, PAY-2026-00891  (complete)
   Submitted — Aug 10, 2026, 3:02 PM — Ifeoma Chukwu  (complete)
   Under Review — Aug 10, 2026, 3:05 PM — RERA, Compliance & Escrow Auditor  (current)
   Approved — Pending  (future)
   Registered — Pending  (future)

5. Card — "Property Information". Read-only label/value grid:
   Project: Banana Island Villas — PRJ-2026-0014
   Unit Identifier: A-120
   Unit Type: 2-Bedroom Apartment
   Unit Specifications: 145 sqm

6. Card — "Purchaser Information". Read-only label/value grid:
   Full Name: John Smith
   National Identification Number: NGA-58231940
   Phone Number: +234 803 221 7765
   Email Address: john.smith@example.com

7. Card — "Sale Information". Read-only label/value grid:
   Sale Value: ₦185,000,000
   Payment Plan / Terms: Outright Payment
   Agreed Sale Date: Aug 3, 2026

8. Card — "Supporting Documents". Table with columns Document Name · Requirement · Status · Action, three rows, all Uploaded, action "View".

9. Card — "Payment". Label/value rows:
   Total Amount Paid: ₦42,000
   Payment Reference: PAY-2026-00891
   Payment Date: Aug 10, 2026
   Payment Status: Paid (green pill)

10. Card — "Activity Log". Use the Dashboard's activity feed row pattern — event description on the left, actor and relative timestamp right-aligned:
    Application under review by RERA — RERA (Compliance & Escrow Auditor) — 3 minutes ago
    Submitted for review — Ifeoma Chukwu — 6 minutes ago
    Payment completed — ₦42,000 — Ifeoma Chukwu — 21 minutes ago
    Documents attached — 3 files — Ifeoma Chukwu — 40 minutes ago
    Application created — Ifeoma Chukwu — 1 hour ago
```

---

## S1 – 10 · Registration Confirmation

```
Create a new screen frame named "S1 – 10 Registration Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S1 – 10 Registration Confirmation
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Sale Registered", subtitle "APP-2026-0219 — Register Initial Sale")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, document table rows, success icon treatment, the vertical status timeline. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. Do not draw a decorative certificate, seal, border, or watermark — the output document is represented as a document record with actions, not as a rendered certificate graphic.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0219 / Registration Confirmation

2. Page header row: heading "APP-2026-0219" with the status pill "Registered" beside it on the left. On the right, secondary button "View Property Registration" and blue primary button "Download Certificate".

3. A success notice card, full width, using the existing subtle success treatment: a green check icon on the left, then bold text "Provisional Sale Successfully Registered" and a grey line beneath: "Approved by RERA on Aug 12, 2026. The Provisional Registration e-Certificate has been emailed to john.smith@example.com."

4. Card — "Application Status". The same vertical timeline as S1 – 09, now with every stage marked complete:
   Draft — Aug 9, 2026, 1:15 PM — Ifeoma Chukwu  (complete)
   Payment Successful — Aug 10, 2026, 2:47 PM — ₦42,000, PAY-2026-00891  (complete)
   Submitted — Aug 10, 2026, 3:02 PM — Ifeoma Chukwu  (complete)
   Under Review — Aug 10, 2026, 3:05 PM — RERA, Compliance & Escrow Auditor  (complete)
   Approved — Aug 12, 2026, 9:40 AM — RERA, Compliance & Escrow Auditor  (complete)
   Registered — Aug 12, 2026, 9:41 AM — Provisional Registration e-Certificate issued  (complete)

5. Card — "Sale Record". Two-column label/value grid:
   Provisional Registration e-Certificate Number: RERA-PROV-2026-00219
   Registration Date: Aug 12, 2026
   Project: Banana Island Villas — PRJ-2026-0014
   Unit Identifier: A-120
   Unit Type: 2-Bedroom Apartment
   Purchaser: John Smith
   Sale Value: ₦185,000,000
   Agreed Sale Date: Aug 3, 2026

6. Card — "Output Documents". A document table with columns Document Name · Type · Issued · Action:
   Provisional Registration e-Certificate — RERA-PROV-2026-00219.pdf — Registration Certificate — Aug 12, 2026 — View / Download / Email Copy
   Payment Receipt — PAY-2026-00891.pdf — Receipt — Aug 10, 2026 — View / Download
   Beneath the table, a small grey line: "The e-certificate is emailed to the purchaser directly. This copy is retained in-app for your own records."

7. Card — "Application Record". Read-only label/value grid:
   Application Reference: APP-2026-0219
   Service Name: Register Initial Sale
   Submitted On: Aug 10, 2026 — 3:02 PM
   Approved On: Aug 12, 2026 — 9:40 AM
   Total Amount Paid: ₦42,000
   Filed By: Ifeoma Chukwu — Sales & Disclosure Officer

8. Bottom-right: blue primary button "Download Certificate".
```
