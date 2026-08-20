---
project: RERAN
module: real-estate-developer
type: reference-sample
status: draft
contains_proposals: true
written_against_specs_on: 2026-08-20
derived_from:
  - "RERAN/modules/real-estate-developer/service-flows/service-06-register-mortgage-linked-sale.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registrations.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
  - "RERAN/modules/real-estate-developer/ui/figma-prompts/s1-register-initial-sale.md"
  - "RERAN/modules/real-estate-developer/ui/figma-prompts/nav-sidebar-landing-screens.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/service-03-mortgage-registration.md"
tags:
  - real-estate-developer
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in [`../screens/`](../screens/) and [`service-06-register-mortgage-linked-sale.md`](../../service-flows/service-06-register-mortgage-linked-sale.md); where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Service #6: Register Sale Associated with an Initial Mortgage

**Module:** Real Estate Developer (RERAN Group B)
**Screens:** 11, namespaced `S6 – 01` … `S6 – 11`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## Why this pack shows two outcomes, not one

Every other pack in this folder walks one application from Draft to a completed record. This service is different on purpose — its whole reason for being in the selected five is a **real-time cross-module validation** that most applications through this service will actually fail, at least on a first attempt: the cited mortgage reference is checked against Group C's Mortgage Registration records, in real time, within the same submission request, and must already be `Completed` there. If it isn't, the application is automatically returned — immediately, with no warning beforehand, and after the developer has already paid.

So this pack shows both outcomes:

- **`S6 – 02` through `S6 – 08`** walk the **successful** path — a mortgage that's already `Completed` on Group C's side.
- **`S6 – 09`** is the **automatic-return** outcome — shown as an alternate ending fed by a *different* application, so the contrast is explicit rather than implied. This is the screen the whole pack exists to show.
- **`S6 – 10` and `S6 – 11`** continue the successful path through to registration.

**This alternate application isn't invented for this pack alone.** `APP-2026-0228` — Unit B-204, Lekki Pearl Estate, buyer Blessing Okafor — already appears with status `Returned` in `nav-sidebar-landing-screens.md`'s Applications screen, filed Aug 14 and returned Aug 15. This pack is where that return finally gets explained: the mortgage cited on that application hadn't reached `Completed` status on Group C's side yet.

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | **No pre-submission indication of the mortgage's FTI status, anywhere in the wizard** | Sourced explicitly, decided 2026-08-16 — "no pre-submission warning is shown." Every wizard screen (`S6 – 02` through `S6 – 07`) must not hint at whether the cited mortgage will validate. |
| 2 | **Payment happens before the validation check runs, not after** | Sourced directly — Section 9: "Payment is collected before the mortgage-validation check runs — a developer whose mortgage isn't yet `Completed` will have already paid by the time the real-time check returns a failure." Both outcome screens keep the payment as already-settled. |
| 3 | **The validation itself has no visible "checking..." screen** | Sourced — it's synchronous, resolved within the same request as submission. `S6 – 08` and `S6 – 09` are the two possible *results* of that same instant, not two different steps in a sequence. |
| 4 | **The system-generated return is visually distinguished from a RERA-issued return** | Sourced, Section 13 — the return reason must specifically say "mortgage not yet completed" and distinguish itself from RERA's own manual returns. `S6 – 09` shows this explicitly. |
| 5 | **Required documents follow the general mortgage-linked sale pattern** | Not itemized field-by-field in the source; carried through from the service file's own flagged proposal. |

---

## Consistent sample data — successful path (`S6 – 02` through `S6 – 11`)

- Application ID: `APP-2026-0233`
- Company: Crestwood Developments Ltd. · `DEV-2024-00437`
- Filer / acting officer: Ifeoma Chukwu — Sales & Disclosure Officer
- Project: Lekki Pearl Estate · `PRJ-2026-0019`
- Unit: C-305 · 3-Bedroom Apartment · 168 sqm
- Purchaser: Amaka Eze · NIN `NGA-71059283` · +234 807 552 3391 · amaka.eze@example.com
- Mortgage Institution: First Bank of Nigeria · Mortgage Reference `MTG-2026-002210` · Mortgage Amount ₦38,500,000
- Sale: Sale Value ₦142,500,000 · Agreed Sale Date Aug 15, 2026
- Fee: Registration Fee ₦45,000 · Processing Levy ₦2,500 · **Total ₦47,500**
- Payment Reference: `PAY-2026-01102`
- Mortgage Provisional Registration Certificate Number: `RERA-MTGPROV-2026-00233`

## Sample data — the automatic-return alternate ending (`S6 – 09` only)

- Application ID: `APP-2026-0228` *(already referenced as "Returned" in `nav-sidebar-landing-screens.md`)*
- Filer: Ifeoma Chukwu — Sales & Disclosure Officer
- Project / Unit: Lekki Pearl Estate · Unit B-204
- Purchaser: Blessing Okafor
- Sale Value: ₦142,000,000
- Mortgage Institution: First Bank of Nigeria · Mortgage Reference `MTG-2026-002089` · Mortgage Amount ₦95,000,000
- Submitted: Aug 14, 2026 — 11:20 AM · Auto-returned: Aug 14, 2026 — 11:20 AM (same instant — synchronous check)
- Payment Reference: `PAY-2026-01087` (already charged, ₦47,500, before the return)

---

## S6 – 01 · Service Details

```
Create a new screen frame named "S6 – 01 Service Details", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 01 Service Details
  - RED-Sidebar       (instance of the existing sidebar component — do not redraw it; active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Details", subtitle "Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, tables, breadcrumbs, section headers, label/value field grids, icons. Do not invent new colours, new type scales, or new card treatments.

Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Sale Associated with an Initial Mortgage

2. Page header row: heading "Register Sale Associated with an Initial Mortgage" on the left. On the right, a secondary button "Back to Property Registrations" and a blue primary button "Start Application".

3. Card — "Service Overview". Two-column label/value grid:
   Service Code: #6
   Service Category: Real Estate Development Services
   Processing Time: 6 business days (once the cited mortgage validates)
   Applicable Fee: ₦45,000 (per RERAN fee schedule)
   Approving Authority: RERA — Compliance & Escrow Auditor
   Payment Timing: Paid at submission, before RERA's review and before mortgage validation
   Below the grid, a full-width description paragraph: "Registers the provisional sale of a unit where the purchaser is financing the purchase through a mortgage. The cited mortgage is checked in real time against the financing institution's own Mortgage Registration record before this application can proceed."

4. A single-line inline notice beneath the Service Overview card, using the existing subtle notice style, in the amber/warning treatment rather than the neutral one: "The cited mortgage must already be fully registered and approved with the financing institution before this application can proceed. There is no way to check this in advance — the system checks automatically, immediately after you submit and pay."

5. Card — "How It Works". A single horizontal row of five numbered steps, evenly spaced, each with a number badge and a short label underneath:
   1 Select Property · 2 Purchaser & Mortgage Details · 3 Documents · 4 Payment · 5 Review & Submit
   Beneath the row, a single grey line: "Immediately after submission, the system checks the cited mortgage against the financing institution's records. If it isn't fully registered yet, your application is returned automatically — you'll need to resubmit once it is."

6. Card — "What You'll Need". Two columns side by side.
   Left column heading "Required Information", as a simple bulleted list:
     Project reference number and unit identifier
     Purchaser full name, National Identification Number and contact details
     Mortgage institution, reference number and amount
   Right column heading "Required Documents", as a list of rows, each with the document name and a small requirement pill:
     Provisional Sale Agreement — Required
     Mortgage Offer Letter — Required
     Purchaser Government-issued Identification — Required
     Other Supporting Documents — Optional

7. Card — "Prerequisites". A short vertical list of check-style rows, with the last one in the amber/warning treatment rather than the standard neutral one:
   Registered developer company account
   Real estate project already registered with RERA
   Property/unit exists within that project's approved unit list
   Purchaser and mortgage institution identified
   The cited mortgage must already be a Completed record with the financing institution — not merely underway

8. Card — "Who Can Apply". Two short label/value rows:
   Applicant: Any of the company's Group B users
   Typical Filer: Sales & Disclosure Officer (customary practice, not a restriction — see navigation.md)

9. Bottom-right: blue primary button "Start Application".
```

---

## S6 – 02 · Step 1 — Select Property

```
Create a new screen frame named "S6 – 02 Select Property", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 02 Select Property
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, search inputs. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, one search-and-select card, one blue primary action. No illustrations, no floor plans.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Sale Associated with an Initial Mortgage / New Application

2. Page header row: heading "Register Sale Associated with an Initial Mortgage" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, five fields across:
   APPLICATION ID: APP-2026-0233
   SERVICE NAME: Register Sale Associated with an Initial Mortgage
   STATUS: Draft (status pill)
   LAST UPDATED: Aug 18, 2026 — 4:40 PM
   CREATED BY: Ifeoma Chukwu

4. Horizontal step progress tracker, five steps, step 1 active and steps 2–5 upcoming:
   1. Select Property · 2. Purchaser & Mortgage Details · 3. Documents · 4. Payment · 5. Review & Submit

5. Card — "Select Project". A single search/select input labelled "Project Reference Number", value "PRJ-2026-0019 — Lekki Pearl Estate".

6. Card — "Select Unit". At the top, a search input labelled "Unit Identifier", value "C-305". Beneath it, a selected-result panel using the existing subtle bordered treatment:
   Unit Identifier: C-305
   Unit Type: 3-Bedroom Apartment
   Unit Specifications: 168 sqm
   Availability: Available for Sale (green status pill)
   A text link "Change Unit" at the bottom of the panel.

7. Step navigation row at the bottom: secondary button "Back" (disabled) on the left, blue primary button "Continue" on the right.

Do not add any indication of the cited mortgage's validation status anywhere on this screen — that check happens only after submission on S6 – 08 or S6 – 09.
```

---

## S6 – 03 · Step 2 — Purchaser & Mortgage Details

```
Create a new screen frame named "S6 – 03 Purchaser and Mortgage Details", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 03 Purchaser and Mortgage Details
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Sale Associated with an Initial Mortgage / New Application

2. Page header row: heading "Register Sale Associated with an Initial Mortgage" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous step.

4. Horizontal step progress tracker, five steps, step 1 complete, step 2 active.

5. Card — "Selected Unit", read-only summary strip: "PRJ-2026-0019 — Lekki Pearl Estate · Unit C-305 · 3-Bedroom Apartment, 168 sqm", with a text link "Change" on the right.

6. Card — "Purchaser Information". Editable form, two columns:
   Full Name — text input, value "Amaka Eze"
   National Identification Number (NIN) — text input, value "NGA-71059283"
   Phone Number — text input, value "+234 807 552 3391"
   Email Address — text input, value "amaka.eze@example.com"
   Mark all four as required.

7. Card — "Mortgage Information". Editable form, two columns:
   Mortgage Institution — dropdown, value "First Bank of Nigeria"
   Mortgage Reference Number — text input, value "MTG-2026-002210"
   Mortgage Amount — text input, value "₦38,500,000"
   Mark all three as required. Beneath the form, a small grey helper line: "Enter the reference exactly as issued by the mortgage institution." Do NOT add any check icon, validation status, or "verify" button beside these fields — the mortgage is not checked until after this application is submitted and paid.

8. Card — "Sale Information". Editable form, two columns:
   Sale Value — text input, value "₦142,500,000"
   Agreed Sale Date — text input, value "Aug 15, 2026"
   Mark both as required.

9. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S6 – 04 · Step 3 — Documents

```
Create a new screen frame named "S6 – 04 Documents", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 04 Documents
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, the document table, requirement pills, status pills. Do not invent new colours, type scales, or card treatments.

Keep it simple: one table inside one card. No drag-and-drop illustration.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Sale Associated with an Initial Mortgage / New Application

2. Page header row: heading "Register Sale Associated with an Initial Mortgage" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps.

4. Horizontal step progress tracker, five steps, steps 1–2 complete, step 3 active.

5. Card — "Supporting Documents". Under the heading, a small grey counter line: "3 of 3 required documents uploaded". On the right of the card header, a secondary text action "Attach from Documents".
   Table with columns: Document Name · Requirement · Status · Action
     Provisional Sale Agreement — Required — Uploaded — View / Replace
     Mortgage Offer Letter — Required — Uploaded — View / Replace
     Purchaser Government-issued Identification — Required — Uploaded — View / Replace
     Other Supporting Documents — Optional — Not Uploaded — Upload

6. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S6 – 05 · Step 4 — Payment

```
Create a new screen frame named "S6 – 05 Payment", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 05 Payment
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, label/value rows, radio groups, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: two stacked cards, plain radio list for payment method.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Sale Associated with an Initial Mortgage / New Application

2. Page header row: heading "Register Sale Associated with an Initial Mortgage" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Payment Pending".

4. Horizontal step progress tracker, five steps, steps 1–3 complete, step 4 active.

5. Card — "Fee Breakdown". A simple stacked list of label/amount rows, right-aligned amounts, with a divider before the total:
   Registration Fee — ₦45,000
   Processing Levy — ₦2,500
   — divider —
   Total Amount Due — ₦47,500  (larger, bold)

6. Card — "Payment Method". A vertical radio group with three plain options, first one selected: Card Payment · Bank Transfer · USSD, each with a short grey helper line beneath.

7. A single-line inline notice beneath the cards, in the amber/warning treatment: "Payment is collected before your mortgage reference is checked. If the cited mortgage isn't yet fully registered with the financing institution, your application will still be returned after this payment is made."

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Pay ₦47,500" on the right.
```

---

## S6 – 06 · Payment Confirmation

```
Create a new screen frame named "S6 – 06 Payment Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 06 Payment Confirmation
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment Successful", subtitle "Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, the horizontal step progress tracker, label/value rows, success icon treatment. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card. Use the existing green success colour only for the check icon and the status pill.

Workspace content, top to bottom:

1. Horizontal step progress tracker, five steps, steps 1–4 complete, step 5 (Review & Submit) shown as next.

2. One centred card, roughly 720px wide, containing in this order:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Payment Successful"
   - Sub-line, centred, grey: "Your payment has been received. You can now review and submit this application to RERA."
   - The amount, centred and large: ₦47,500
   - A divider
   - A two-column label/value grid:
       Payment Reference: PAY-2026-01102
       Payment Date: Aug 19, 2026 — 9:12 AM
       Payment Method: Card Payment
       Payment Status: Paid (green status pill)
       Application ID: APP-2026-0233
       Service Name: Register Sale Associated with an Initial Mortgage
   - A divider
   - Two buttons, centred side by side: secondary "Download Receipt", blue primary "Continue to Review"
```

---

## S6 – 07 · Step 5 — Review & Submit

```
Create a new screen frame named "S6 – 07 Review and Submit", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 07 Review and Submit
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Property Registrations")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Review Application", subtitle "Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, inline "Edit" links, the Validation Panel, a declaration checkbox row. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, one blue primary action at the top and bottom.

IMPORTANT: the Validation Summary on this screen checks the application's own completeness only — required fields, required documents, unit availability. It does NOT check or mention the mortgage's status with the financing institution. That check has not happened yet and nothing on this screen should suggest otherwise.

Workspace content, top to bottom:

1. Breadcrumb: Property Registrations / Register Sale Associated with an Initial Mortgage / New Application

2. Page header row: heading "Review Application" on the left. On the right, secondary button "Save Draft" and blue primary button "Submit Application".

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Ready for Review".

4. Horizontal step progress tracker, five steps, steps 1–4 complete, step 5 active.

5. Card — "Property Information", with an inline "Edit" link:
   Project: Lekki Pearl Estate — PRJ-2026-0019
   Unit Identifier: C-305
   Unit Type: 3-Bedroom Apartment

6. Card — "Purchaser Information", with an inline "Edit" link:
   Full Name: Amaka Eze
   National Identification Number: NGA-71059283
   Phone Number: +234 807 552 3391
   Email Address: amaka.eze@example.com

7. Card — "Mortgage Information", with an inline "Edit" link:
   Mortgage Institution: First Bank of Nigeria
   Mortgage Reference Number: MTG-2026-002210
   Mortgage Amount: ₦38,500,000

8. Card — "Sale Information", with an inline "Edit" link:
   Sale Value: ₦142,500,000
   Agreed Sale Date: Aug 15, 2026

9. Card — "Supporting Documents", counter line "3 of 3 required documents uploaded". Table with columns Document Name · Requirement · Status · Action, three Required rows, all Uploaded, action "View".

10. Card — "Payment Summary": Registration Fee ₦45,000 · Processing Levy ₦2,500 · Total Amount Paid ₦47,500 (larger, bold) · Payment Reference PAY-2026-01102 · Payment Date Aug 19, 2026 · Payment Status Paid (green pill).

11. Card — "Validation Summary", with a green sub-line "All checks passed", then a vertical list of green check rows:
    Required purchaser and sale information completed
    Required documents provided
    Unit belongs to a registered project and is available for sale
    Payment completed
    Below the list, a small grey line, NOT in the green success styling: "Mortgage reference will be validated against the financing institution's records after submission."

12. Card — "Declaration". A checked checkbox with the standard accuracy declaration text.

13. Bottom-right: blue primary button "Submit Application".
```

---

## S6 – 08 · Application Submitted — Mortgage Validated

```
Create a new screen frame named "S6 – 08 Application Submitted Validated", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 08 Application Submitted Validated
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Submitted", subtitle "Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, success icon treatment, numbered list rows.

Keep it simple: one centred confirmation card plus one short "what happens next" card.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Application Submitted and Mortgage Validated"
   - Sub-line, centred, grey: "Your cited mortgage was verified as Completed with First Bank of Nigeria. This application has been sent to RERA for review."
   - The reference, centred and large: APP-2026-0233
   - A divider
   - A two-column label/value grid:
       Service Name: Register Sale Associated with an Initial Mortgage
       Status: Under Review (status pill)
       Submitted On: Aug 19, 2026 — 9:24 AM
       Submitted By: Ifeoma Chukwu
       Mortgage Reference: MTG-2026-002210 (Verified, green pill)
       Expected Review Time: 6 business days

2. Card — "What Happens Next". Two numbered rows:
   1  RERA Review — RERA's Compliance & Escrow Auditor reviews the application. Any of your company's users may track it, including you.
   2  Registration — On approval, a Mortgage Provisional Registration Certificate and an Electronic Map are issued.

3. Two buttons, centred side by side: secondary "View Application", blue primary "Back to Property Registrations".
```

---

## S6 – 09 · Alternate Outcome — Application Automatically Returned

```
Create a new screen frame named "S6 – 09 Application Automatically Returned", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 09 Application Automatically Returned
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Returned", subtitle "Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, an error/warning icon treatment, numbered list rows.

Keep it simple: one centred outcome card, using the existing warning/error treatment rather than the green success treatment. No illustration.

THIS IS A DIFFERENT APPLICATION FROM S6 – 08. It uses the alternate sample data (APP-2026-0228, Unit B-204, Blessing Okafor) to show what happens when the cited mortgage is NOT yet Completed on the financing institution's side. This is not a follow-up to S6 – 08 — it is a separate, contrasting scenario, reached the same way but ending differently.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single amber/warning circular icon (not the green check), centred, modest in size
   - Heading, centred: "Application Automatically Returned"
   - Sub-line, centred, grey: "The mortgage cited on this application has not yet completed registration with the financing institution. Your payment has already been processed."
   - The reference, centred and large: APP-2026-0228
   - A divider
   - A two-column label/value grid:
       Service Name: Register Sale Associated with an Initial Mortgage
       Status: Returned (amber/warning status pill — NOT the same red used for RERA rejections)
       Submitted On: Aug 14, 2026 — 11:20 AM
       Returned On: Aug 14, 2026 — 11:20 AM
       Return Reason: System-generated — mortgage not yet Completed (small distinct label, visually different from a RERA-issued return reason)
       Mortgage Institution: First Bank of Nigeria
       Mortgage Reference: MTG-2026-002089
       Total Amount Paid: ₦47,500 (unaffected by this return)

2. A single-line inline notice, using the existing subtle notice style: "This is a system check, not a RERA decision. Once First Bank of Nigeria completes this mortgage's own registration, you can resubmit this application as a new submission — there is no automatic retry."

3. Card — "What You Can Do". Two numbered rows:
   1  Check Mortgage Status — Confirm with First Bank of Nigeria that the mortgage referenced above has reached Completed status on their side.
   2  Resubmit — Once confirmed, file this application again as a fresh submission. Your previously uploaded documents can be reused.

4. Two buttons, centred side by side: secondary "View Application", blue primary "Start New Application".
```

---

## S6 – 10 · Application Details — Under Review

```
Create a new screen frame named "S6 – 10 Application Details Under Review", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 10 Application Details Under Review
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Details", subtitle "APP-2026-0233 — Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, the vertical status timeline pattern.

Keep it simple: a single stacked column of cards.

This continues the SUCCESSFUL path (S6 – 08's application), now further along.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0233

2. Page header row: heading "APP-2026-0233" with the status pill "Under Review" beside it on the left. On the right, secondary button "Download Summary".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0233
   SERVICE NAME: Register Sale Associated with an Initial Mortgage
   STATUS: Under Review (pill)
   SUBMITTED ON: Aug 19, 2026 — 9:24 AM
   CREATED BY: Ifeoma Chukwu

4. Card — "Application Status". A vertical timeline, one row per stage:
   Draft — Aug 18, 2026, 4:40 PM — Ifeoma Chukwu  (complete)
   Payment Successful — Aug 19, 2026, 9:12 AM — ₦47,500, PAY-2026-01102  (complete)
   Submitted — Aug 19, 2026, 9:24 AM — Ifeoma Chukwu  (complete)
   Mortgage Reference Validated — Aug 19, 2026, 9:24 AM — MTG-2026-002210 confirmed Completed with First Bank of Nigeria  (complete, shown with a small green check rather than the standard filled marker, to distinguish it as an automated check rather than a human stage)
   Under Review — Aug 19, 2026, 9:25 AM — RERA, Compliance & Escrow Auditor  (current)
   Approved — Pending  (future)
   Registered — Pending  (future)

5. Card — "Property Information". Read-only: Project: Lekki Pearl Estate — PRJ-2026-0019 · Unit Identifier: C-305 · Unit Type: 3-Bedroom Apartment.

6. Card — "Purchaser Information". Read-only: Full Name Amaka Eze · NIN NGA-71059283 · Phone +234 807 552 3391 · Email amaka.eze@example.com.

7. Card — "Mortgage Information". Read-only: Mortgage Institution First Bank of Nigeria · Mortgage Reference MTG-2026-002210 (Verified, green pill) · Mortgage Amount ₦38,500,000.

8. Card — "Sale Information". Read-only: Sale Value ₦142,500,000 · Agreed Sale Date Aug 15, 2026.

9. Card — "Supporting Documents". Table, three Required rows, all Uploaded.

10. Card — "Payment". Total Amount Paid ₦47,500 · Payment Reference PAY-2026-01102 · Payment Status Paid (green pill).
```

---

## S6 – 11 · Registration Confirmation

```
Create a new screen frame named "S6 – 11 Registration Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S6 – 11 Registration Confirmation
  - RED-Sidebar       (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Sale Registered", subtitle "APP-2026-0233 — Register Sale Associated with an Initial Mortgage")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, document table rows, success icon treatment, the vertical status timeline.

Keep it simple: stacked white cards. Do not draw a decorative certificate or map graphic — output documents are represented as document records with actions.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0233 / Registration Confirmation

2. Page header row: heading "APP-2026-0233" with the status pill "Registered" beside it on the left. On the right, secondary button "View Property Registration" and blue primary button "Download Documents".

3. A success notice card, full width: a green check icon, bold text "Mortgage-Linked Sale Successfully Registered" and a grey line beneath: "Approved by RERA on Aug 21, 2026. Both output documents are ready below."

4. Card — "Application Status". The same vertical timeline as S6 – 10, now with every stage complete, plus two additional rows:
   Draft — Aug 18, 2026, 4:40 PM — Ifeoma Chukwu  (complete)
   Payment Successful — Aug 19, 2026, 9:12 AM — ₦47,500, PAY-2026-01102  (complete)
   Submitted — Aug 19, 2026, 9:24 AM — Ifeoma Chukwu  (complete)
   Mortgage Reference Validated — Aug 19, 2026, 9:24 AM — MTG-2026-002210 confirmed Completed  (complete)
   Under Review — Aug 19, 2026, 9:25 AM — RERA, Compliance & Escrow Auditor  (complete)
   Approved — Aug 21, 2026, 10:18 AM — RERA, Compliance & Escrow Auditor  (complete)
   Registered — Aug 21, 2026, 10:19 AM — Both output documents issued  (complete)

5. Card — "Sale Record". Two-column label/value grid:
   Mortgage Provisional Registration Certificate Number: RERA-MTGPROV-2026-00233
   Registration Date: Aug 21, 2026
   Project: Lekki Pearl Estate — PRJ-2026-0019
   Unit Identifier: C-305
   Purchaser: Amaka Eze
   Sale Value: ₦142,500,000
   Mortgage Institution: First Bank of Nigeria
   Mortgage Reference: MTG-2026-002210

6. Card — "Output Documents". A document table with columns Document Name · Type · Issued · Action:
   Mortgage Provisional Registration Certificate — RERA-MTGPROV-2026-00233.pdf — Registration Certificate — Aug 21, 2026 — View / Download / Email Copy
   Electronic Map — EMAP-2026-00233.pdf — Electronic Map — Aug 21, 2026 — View / Download
   Payment Receipt — PAY-2026-01102.pdf — Receipt — Aug 19, 2026 — View / Download
   Beneath the table, a small grey line: "This service issues two output documents, unlike a standard sale registration — a certificate and an electronic map."

7. Card — "Application Record". Application Reference APP-2026-0233 · Submitted On Aug 19, 2026 · Approved On Aug 21, 2026 · Total Amount Paid ₦47,500 · Filed By Ifeoma Chukwu — Sales & Disclosure Officer.

8. Bottom-right: blue primary button "Download Documents".
```
