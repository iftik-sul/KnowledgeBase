---
project: RERAN
module: financial-trust-institutions
type: reference-sample
status: current
updated: 2026-08-19
contains_proposals: true
written_against_specs_on: 2026-08-18
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/service-15-update-title-deed-information.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/submit-application.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in `../screens/` and `../screens-unified/`; where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Service #15: Updating Title Deed Information

**Module:** Financial & Trust Institutions (RERAN Group C)
**Screens:** 10, namespaced `S15 – 01` … `S15 – 10`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | Designed as an **institution-portal** flow | Same call as #17 and #13. Source row 42 confirms only the Trustees Centre / Land Department walk-in path; a bank-originated channel remains unconfirmed. |
| 2 | **Payment is a step inside the wizard, before submission** | Sourced: row 42 puts "pay fees, get receipt" at step 4, before "review and approval" at step 5. |
| 3 | Tracker reuses the **same 6-step labels** | Consistency across all services. |
| 4 | **No internal certification gate** | Single approval authority (Compliance & Escrow Auditor). |
| 5 | **Select Property folded into Step 2**, with Update Details beneath it | Same call as #3 and #13. Step 2 is the Pattern C screen. |
| 6 | **The updatable-field list is proposed, not sourced** — see below | Open question 1 in the service file: source never says which fields this service covers. |
| 7 | **The updated deed keeps its number and gains a version** | Open question 2: source doesn't say whether a new certificate is issued or the record is amended. Proposing amend-with-version, since the service explicitly does not transfer ownership. |
| 8 | Fee figures are **placeholders** | Exact fee is unresolved client data. |

### Proposed updatable fields (assumption 6)

The service's own boundary is the constraint: it corrects particulars **without transferring ownership or creating an encumbrance**. Everything below stays inside that line.

**Owner particulars** — Owner Full Name · Owner National Identification Number · Owner Phone Number · Owner Email Address · Correspondence Address

**Property particulars** — Property Address · Property Type · Registered Area · Plot / Parcel Number · Survey Plan Reference

**Deliberately excluded**, because they'd be a different service: the identity of the registered owner (that's a transfer), ownership shares (Split Ownership, #16), and any mortgage or encumbrance record (#3–#6).

Worth putting to the client as a proposal rather than an open question — it's a short list and the boundary is defensible from the service's own description.

**New component this service needs:** a **conditional field selector** — a checklist of updatable fields where each ticked field reveals a Current Value / New Value pair. `S15 – 03` defines it. This is the only Pattern C service in the module, so nothing else will build this component.

**Consistent sample data across all screens** — keep these identical so the screens read as one journey:

- Application ID: `APP-2026-0184`
- Institution: First Bank of Nigeria · `FI-2024-00892` · Commercial Bank
- Acting officer: Chukwuemeka Okonkwo — Institution Relationship Manager
- Registered owner: Halima Yusuf · NIN `NGA-60218473`
- Property: Plot 8, Gana Street, Maitama, Abuja · Residential — Detached House · 510 sqm · `RERA-PROP-2021-03356`
- Existing Title Deed: `TD-2021-002917` · issued 14 Mar 2021
- **Two fields being updated:**
  - Owner Full Name — `Halima Yusuf` → `Halima Yusuf-Danjuma`
  - Owner Phone Number — `+234 803 552 1140` → `+234 806 774 9218`
- Reason for update: Legal name change following marriage
- Supporting evidence: Marriage Certificate (`MC/ABJ/2026/04417`)
- Fees: Service Fee ₦16,000 · Processing Levy ₦1,600 · VAT (7.5%) ₦1,320 · **Total ₦18,920**
- Payment Reference: `PAY-2026-00944`
- Updated deed: `TD-2021-002917` · **Version 2** · issued 17 Aug 2026
- Processing time: 25 minutes
- Approving authority: RERA — Compliance & Escrow Auditor

---

## S15 – 01 · Service Details

```
Create a new screen frame named "S15 – 01 Service Details", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 01 Service Details
  - FI-Sidebar        (instance of the existing sidebar component — do not redraw it; active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Details", subtitle "Updating Title Deed Information")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, tables, breadcrumbs, section headers, label/value field grids, icons. Do not invent new colours, new type scales, or new card treatments. Match the spacing, corner radius, and white-card-on-grey treatment already used on the Dashboard and Application Review screens.

Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Services Catalog / Updating Title Deed Information

2. Page header row: heading "Updating Title Deed Information" on the left. On the right, a secondary button "Back to Catalog" and a blue primary button "Start Application".

3. Card — "Service Overview". Two-column label/value grid:
   Service Code: #15
   Service Category: Title & Ownership Transaction Services
   Processing Time: 25 minutes
   Applicable Fee: ₦16,000 (per RERAN fee schedule)
   Approving Authority: RERA — Compliance & Escrow Auditor
   Payment Timing: Payable before RERA review
   Below the grid, a full-width description paragraph: "Corrects or updates information recorded on an existing title deed — for example a legal name change or a correction to recorded particulars. This service does not transfer ownership and does not create a mortgage or other encumbrance."

4. Card — "How It Works". A single horizontal row of six numbered steps, evenly spaced, each with a number badge and a short label underneath:
   1 Application Info · 2 Service Info · 3 Documents · 4 Validation · 5 Payment · 6 Review & Submit
   Beneath the row, a single grey line: "On approval, the title deed record is amended and an updated electronic certificate is emailed to the registered owner."

5. Card — "What Can Be Updated". Two columns side by side, each a simple bulleted list.
   Left column heading "Owner Particulars":
     Owner Full Name
     Owner National Identification Number
     Owner Phone Number
     Owner Email Address
     Correspondence Address
   Right column heading "Property Particulars":
     Property Address
     Property Type
     Registered Area
     Plot / Parcel Number
     Survey Plan Reference
   Beneath both columns, spanning the full card width and separated by a divider, a short grey paragraph: "Not available through this service — transferring ownership to a different person, changing ownership shares, or adding or removing a mortgage. These require a separate service."

6. Card — "What You'll Need". Two columns side by side.
   Left column heading "Required Information", as a simple bulleted list:
     Property registration number
     The field or fields to be updated
     The current recorded value and the requested new value
     Reason for the update
   Right column heading "Required Documents", as a list of rows, each with the document name and a small requirement pill:
     Existing Certificate of Title — Required
     Evidence Supporting the Update — Required
     Government-issued Identification (Owner) — Required
     Other Supporting Documents — Optional

7. Card — "Who Can Apply". Two short label/value rows:
   Applicant: Any of the institution's Group C users
   Customer: Registered Property Owner, or Authorized Representative

8. Bottom-right: blue primary button "Start Application".
```

---

## S15 – 02 · Step 1 — Application Info

```
Create a new screen frame named "S15 – 02 Application Info", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 02 Application Info
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Updating Title Deed Information")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, section headers. Do not invent new colours, type scales, or card treatments. Match the Application Review screen's spacing and card treatment.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action, no illustrations or decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Updating Title Deed Information / New Application

2. Page header row: heading "Updating Title Deed Information" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip (reuse the existing horizontal metadata component), five fields across:
   APPLICATION ID: APP-2026-0184
   SERVICE NAME: Updating Title Deed Information
   STATUS: Draft (status pill)
   LAST UPDATED: Aug 17, 2026 — 2:14 PM
   CREATED BY: Chukwuemeka Okonkwo

4. Horizontal step progress tracker, six steps, step 1 active and steps 2–6 upcoming:
   1. Application Info · 2. Service Info · 3. Documents · 4. Validation · 5. Payment · 6. Review & Submit

5. Card — "Institution Information", with a small grey helper line under the heading: "Pre-filled from your institution profile". Read-only two-column label/value grid, not editable inputs:
   Institution Name: First Bank of Nigeria
   Registration Number: FI-2024-00892
   Institution Type: Commercial Bank
   Contact Email: operations@firstbanknigeria.com
   Contact Phone: +234 1 905 7000
   Acting Officer: Chukwuemeka Okonkwo — Institution Relationship Manager

6. Card — "Requestor Information". Editable form, two columns:
   Requestor Type — dropdown, value "Registered Property Owner" (other option: Authorized Representative)
   Full Name — text input, value "Halima Yusuf"
   National Identification Number (NIN) — text input, value "NGA-60218473"
   Phone Number — text input, value "+234 803 552 1140"
   Email Address — text input, value "halima.yusuf@email.com"
   Mark Full Name, NIN, Phone Number and Email Address as required fields using the existing required-field treatment.
   Beneath the form, one small grey line: "Enter the requestor's details as currently recorded. Any changes to these details are made in the next step."

7. Step navigation row at the bottom: secondary button "Back" (disabled) on the left, blue primary button "Continue" on the right.
```

---

## S15 – 03 · Step 2 — Service Info

```
Create a new screen frame named "S15 – 03 Service Info", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 03 Service Info
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Updating Title Deed Information")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, search inputs, checkboxes, text areas, status pills, inline notices, section headers, small uppercase sub-headings. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, one blue primary action, no illustrations, no maps, no property photographs.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Updating Title Deed Information / New Application

2. Page header row: heading "Updating Title Deed Information" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields and values as the previous step.

4. Horizontal step progress tracker, six steps, step 1 complete, step 2 active.

5. Card — "Select Property". At the top, a single search input labelled "Property Registration Number" with a small "Search" button beside it, value "RERA-PROP-2021-03356". Beneath it, a selected-result panel using the existing subtle bordered treatment, containing:
   - On the left, a two-column label/value grid:
       Property Registration Number: RERA-PROP-2021-03356
       Title Deed Number: TD-2021-002917
       Property Type: Residential — Detached House
       Property Address: Plot 8, Gana Street, Maitama, Abuja
       Registered Area: 510 sqm
       Registered Owner: Halima Yusuf
   - On the right, a small vertical stack of two validation rows, each a green check icon with a short label:
       Property registered with RERAN
       Requestor matches registered owner
   - A text link "Change Property" at the bottom of the panel.

6. Card — "Select Fields to Update". This is the important part of this screen — build it as a CONDITIONAL FIELD SELECTOR, and make it a reusable component.

   Card header: heading "Select Fields to Update" on the left, and on the right a small grey counter "2 fields selected".

   Beneath the header, a checklist in two columns, each column introduced by a small uppercase grey sub-heading. Every row is a plain checkbox with a label — no values shown at this stage:
     OWNER PARTICULARS
       Owner Full Name  (CHECKED)
       Owner National Identification Number
       Owner Phone Number  (CHECKED)
       Owner Email Address
       Correspondence Address
     PROPERTY PARTICULARS
       Property Address
       Property Type
       Registered Area
       Plot / Parcel Number
       Survey Plan Reference

7. Card — "Changes to Apply", with a small grey helper line under the heading: "One entry appears here for each field selected above". Inside the card, one block per selected field. Each block is a light bordered container (not a nested white card — use a subtle border and a slightly recessed background so it reads as a sub-group), containing:
     - A block header row: the field name in bold on the left, and on the right a small text-only "Remove" action in the existing muted link style
     - A two-column row beneath it:
         Current Recorded Value — READ-ONLY, shown as a label with a plain value, not an input, with a subtle "locked" or muted treatment
         Requested New Value — an editable text input

   Block 1 — Owner Full Name
     Current Recorded Value: Halima Yusuf
     Requested New Value: Halima Yusuf-Danjuma

   Block 2 — Owner Phone Number
     Current Recorded Value: +234 803 552 1140
     Requested New Value: +234 806 774 9218

   Beneath the blocks, separated by a divider, a full-width text area labelled "Reason for Update", marked required, with the value: "Legal name change following marriage. Supporting marriage certificate MC/ABJ/2026/04417 attached."

8. A single-line inline notice beneath the cards, using the existing subtle notice style: "This service updates recorded particulars only. It does not transfer ownership or change ownership shares."

9. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S15 – 04 · Step 3 — Documents

```
Create a new screen frame named "S15 – 04 Documents", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 04 Documents
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Updating Title Deed Information")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, the document table, requirement pills, status pills, link-style row actions, inline notices. Do not invent new colours, type scales, or card treatments. Match the Supporting Documents table already used on the Application Review screen.

Keep it simple: one table inside one card, no drag-and-drop illustration, no file thumbnails, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Updating Title Deed Information / New Application

2. Page header row: heading "Updating Title Deed Information" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields and values as the previous steps.

4. Horizontal step progress tracker, six steps, steps 1–2 complete, step 3 active.

5. Card — "Supporting Documents". Under the heading, a small grey counter line: "3 of 3 required documents uploaded". On the right of the card header, a secondary text action "Attach from Documents".
   Table with columns: Document Name · Requirement · Status · Action
     Existing Certificate of Title — Required — Uploaded — View / Replace
     Evidence Supporting the Update (Marriage Certificate) — Required — Uploaded — View / Replace
     Government-issued Identification (Owner) — Required — Uploaded — View / Replace
     Other Supporting Documents — Optional — Not Uploaded — Upload
   Use the existing requirement pill style for Required / Optional and the existing status pill style for Uploaded / Not Uploaded.

6. A single-line inline notice beneath the card: "Every field being updated must be supported by evidence. RERA may return the application if the evidence does not substantiate the requested change."

7. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S15 – 05 · Step 5 — Payment

```
Create a new screen frame named "S15 – 05 Payment", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 05 Payment
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Updating Title Deed Information")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, label/value rows, radio groups, inline notices. Do not invent new colours, type scales, or card treatments. Match the Payment Summary block already used on the Application Review screen.

Keep it simple: two stacked cards, plain radio list for payment method, no card-brand logos, no illustrations.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Updating Title Deed Information / New Application

2. Page header row: heading "Updating Title Deed Information" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Pending Payment".

4. Horizontal step progress tracker, six steps, steps 1–4 complete (Validation shown as automatically passed), step 5 active.

5. Card — "Fee Breakdown". A simple stacked list of label/amount rows, right-aligned amounts, with a divider before the total:
   Service Fee — ₦16,000
   Processing Levy — ₦1,600
   VAT (7.5%) — ₦1,320
   — divider —
   Total Amount Due — ₦18,920  (larger, bold)
   Beneath the total, one small grey line: "A single fee applies regardless of how many fields are being updated."

6. Card — "Payment Method". A vertical radio group with three plain options, first one selected:
   Card Payment
   Bank Transfer
   USSD
   No logos or brand marks — text labels only, each with a short grey helper line beneath ("Pay with a debit or credit card", "Transfer to a generated account number", "Pay from your mobile phone").

7. A single-line inline notice beneath the cards: "Payment must be completed before this application can be submitted for RERA review."

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Pay ₦18,920" on the right.
```

---

## S15 – 06 · Payment Successful

```
Create a new screen frame named "S15 – 06 Payment Successful", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 06 Payment Successful
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment Successful", subtitle "Updating Title Deed Information")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, the horizontal step progress tracker, label/value rows, success icon treatment. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card, no illustration, no confetti, no large graphics. Use the existing green success colour only for the check icon and the status pill.

Workspace content, top to bottom:

1. Horizontal step progress tracker, six steps, steps 1–5 complete, step 6 (Review & Submit) shown as next.

2. One centred card, roughly 720px wide, containing in this order:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Payment Successful"
   - Sub-line, centred, grey: "Your payment has been received. You can now complete and submit this application."
   - The amount, centred and large: ₦18,920
   - A divider
   - A two-column label/value grid:
       Payment Reference: PAY-2026-00944
       Payment Date: Aug 17, 2026 — 2:38 PM
       Payment Method: Card Payment
       Payment Status: Paid (green status pill)
       Application ID: APP-2026-0184
       Service Name: Updating Title Deed Information
   - A divider
   - Two buttons, centred side by side: secondary "Download Receipt", blue primary "Continue to Review"
```

---

## S15 – 07 · Step 6 — Review & Submit

```
Create a new screen frame named "S15 – 07 Review and Submit", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 07 Review and Submit
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Review", subtitle "Review your application before submission.")
    - Workspace

This screen must follow the existing "Application Review" screen already in this file exactly — same card order, same section header treatment, same inline "Edit" links, same document table, same payment summary block, same validation checklist, same declaration row. Reuse every one of those components and styles. Only the content changes. Do not invent new colours, type scales, or card treatments, and do not restructure the layout.

Workspace content, top to bottom:

1. Breadcrumb: Applications / Application Review

2. Page header row: heading "Application Review" on the left. On the right, secondary button "Save Draft" and blue primary button "Submit Application".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0184
   SERVICE NAME: Updating Title Deed Information
   STATUS: Ready for Review (status pill)
   LAST UPDATED: Aug 17, 2026 — 2:40 PM
   CREATED BY: Chukwuemeka Okonkwo

4. Horizontal step progress tracker, six steps, steps 1–5 complete, step 6 active.

5. Card — "Application Summary". Label/value grid:
   Service Name: Updating Title Deed Information
   Application Reference: APP-2026-0184
   Application Type: Online Submission
   Created Date: Aug 17, 2026
   Current Status: Ready for Review (pill)
   Submission Fee: ₦18,920
   Payment Status: Paid (green pill)

6. Card — "Institution Information", with an inline "Edit" link in the card header:
   Institution Name: First Bank of Nigeria
   Registration Number: FI-2024-00892
   Institution Type: Commercial Bank
   Contact Email: operations@firstbanknigeria.com
   Contact Phone: +234 1 905 7000
   Acting Officer: Chukwuemeka Okonkwo — Institution Relationship Manager

7. Card — "Service Information", with an inline "Edit" link:
   Service Name: Updating Title Deed Information
   Service Category: Title & Ownership Transaction Services
   Service Description: Corrects or updates information recorded on an existing title deed, without transferring ownership or creating an encumbrance.
   Processing Time: 25 minutes
   Applicable Fee: ₦16,000

8. Card — "Application Details", with an inline "Edit" link. Three sub-groups, each with a small uppercase grey sub-heading and a divider between them:
   REQUESTOR
     Requestor Type: Registered Property Owner
     Full Name: Halima Yusuf
     National Identification Number: NGA-60218473
     Phone Number: +234 803 552 1140
     Email Address: halima.yusuf@email.com
   PROPERTY AND TITLE DEED
     Property Registration Number: RERA-PROP-2021-03356
     Title Deed Number: TD-2021-002917
     Property Type: Residential — Detached House
     Property Address: Plot 8, Gana Street, Maitama, Abuja
     Registered Area: 510 sqm
   REQUESTED CHANGES
     Render this sub-group as a read-only table, not as label/value pairs. Columns: Field · Current Recorded Value · Requested New Value
       Owner Full Name — Halima Yusuf — Halima Yusuf-Danjuma
       Owner Phone Number — +234 803 552 1140 — +234 806 774 9218
     Beneath the table, a full-width row: Reason for Update — "Legal name change following marriage. Supporting marriage certificate MC/ABJ/2026/04417 attached."

9. Card — "Supporting Documents", counter line "4 of 4 documents uploaded", inline action "Manage Documents". Table with columns Document Name · Requirement · Status · Action, all rows Uploaded, action "View":
   Existing Certificate of Title — Required
   Evidence Supporting the Update (Marriage Certificate) — Required
   Government-issued Identification (Owner) — Required
   Other Supporting Documents — Optional

10. Card — "Payment Summary":
    Service Fee: ₦16,000
    Processing Levy: ₦1,600
    VAT (7.5%): ₦1,320
    Total Amount Paid: ₦18,920 (larger, bold)
    Payment Reference: PAY-2026-00944
    Payment Date: Aug 17, 2026
    Payment Status: Paid (green pill with check)

11. Card — "Validation Summary", with a green sub-line "All checks passed", then a vertical list of green check rows:
    Required information completed
    Required documents provided
    Institution information valid
    Property registered with RERAN
    Requestor matches registered owner
    Supporting evidence provided for every field
    Duplicate application check passed
    Payment completed
    Below a dotted divider, a green status line: "All Clear — Ready for Submission"

12. Card — "Declaration". A checked checkbox with the text: "I confirm that the information and documents provided in this application are accurate and complete. I understand that providing false or misleading information may result in application rejection, penalties, or regulatory action against the institution."
```

---

## S15 – 08 · Application Submitted

```
Create a new screen frame named "S15 – 08 Application Submitted", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 08 Application Submitted
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Submitted", subtitle "Updating Title Deed Information")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, success icon treatment, numbered list rows. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card plus one short "what happens next" card. No illustration, no large graphics.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Application Submitted"
   - Sub-line, centred, grey: "Your application has been submitted to RERA for review."
   - The reference, centred and large: APP-2026-0184
   - A divider
   - A two-column label/value grid:
       Service Name: Updating Title Deed Information
       Status: Submitted (status pill)
       Submitted On: Aug 17, 2026 — 2:42 PM
       Submitted By: Chukwuemeka Okonkwo
       Fields Being Updated: 2
       Title Deed Number: TD-2021-002917
       Expected Processing Time: 25 minutes
       Reviewing Authority: RERA — Compliance & Escrow Auditor

2. Card — "What Happens Next". Three numbered rows, each with a number badge, a short bold label and one grey line beneath:
   1  RERA Review — The Compliance & Escrow Auditor checks the requested changes against the supporting evidence.
   2  Record Amended — On approval, the title deed record is updated with the new values.
   3  Updated Deed Issued — A link to the updated electronic title deed is emailed to the registered owner.

3. Two buttons, centred side by side beneath the cards: secondary "Back to Dashboard", blue primary "View Application".
```

---

## S15 – 09 · Application Details

```
Create a new screen frame named "S15 – 09 Application Details", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 09 Application Details
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Details", subtitle "APP-2026-0184 — Updating Title Deed Information")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, tables, document tables, the activity feed row pattern from the Dashboard. Do not invent new colours, type scales, or card treatments.

Keep it simple: a single stacked column of cards, no tabs, no side panel, no charts.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0184

2. Page header row: heading "APP-2026-0184" with the status pill "Under Review" beside it on the left. On the right, secondary button "Download Summary" and secondary button "Withdraw Application".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0184
   SERVICE NAME: Updating Title Deed Information
   STATUS: Under Review (pill)
   SUBMITTED ON: Aug 17, 2026 — 2:42 PM
   CREATED BY: Chukwuemeka Okonkwo

4. Card — "Application Status". A simple vertical timeline, one row per stage, each with a small circular marker on a connecting line, the stage name, a timestamp and the actor. Completed stages use the filled marker, the current stage uses the active marker, future stages use an empty outlined marker:
   Draft — Aug 17, 2026, 2:14 PM — Chukwuemeka Okonkwo  (complete)
   Payment Successful — Aug 17, 2026, 2:38 PM — ₦18,920, PAY-2026-00944  (complete)
   Submitted — Aug 17, 2026, 2:42 PM — Chukwuemeka Okonkwo  (complete)
   Under Review — Aug 17, 2026, 2:45 PM — RERA, Compliance & Escrow Auditor  (current)
   Approved — Pending  (future)
   Completed — Pending  (future)

5. Card — "Requested Changes". A read-only table with columns Field · Current Recorded Value · Requested New Value · Status:
   Owner Full Name — Halima Yusuf — Halima Yusuf-Danjuma — Pending Review (status pill)
   Owner Phone Number — +234 803 552 1140 — +234 806 774 9218 — Pending Review (status pill)
   Beneath the table, a full-width row separated by a divider: Reason for Update — "Legal name change following marriage. Supporting marriage certificate MC/ABJ/2026/04417 attached."

6. Card — "Property & Title Deed". Read-only label/value grid:
   Property Registration Number: RERA-PROP-2021-03356
   Title Deed Number: TD-2021-002917
   Deed Issue Date: 14 Mar 2021
   Property Type: Residential — Detached House
   Property Address: Plot 8, Gana Street, Maitama, Abuja
   Registered Area: 510 sqm
   Registered Owner: Halima Yusuf

7. Card — "Supporting Documents". Table with columns Document Name · Requirement · Status · Action, four rows, all Uploaded, action "View" — same list as the Review & Submit screen.

8. Card — "Payment". Label/value rows:
   Total Amount Paid: ₦18,920
   Payment Reference: PAY-2026-00944
   Payment Date: Aug 17, 2026
   Payment Method: Card Payment
   Payment Status: Paid (green pill)
   Inline text action on the right of the card header: "Download Receipt"

9. Card — "Activity Log", with a "View All" link in the header. Use the Dashboard's activity feed row pattern — event description on the left, actor and relative timestamp right-aligned:
   Application under review by RERA — RERA (Compliance & Escrow Auditor) — 3 minutes ago
   Application submitted — Chukwuemeka Okonkwo (Institution Relationship Manager) — 6 minutes ago
   Payment completed — ₦18,920 — Chukwuemeka Okonkwo (Institution Relationship Manager) — 10 minutes ago
   Documents attached — 4 files — Chukwuemeka Okonkwo (Institution Relationship Manager) — 18 minutes ago
   Update fields selected — 2 fields — Chukwuemeka Okonkwo (Institution Relationship Manager) — 24 minutes ago
   Application created — Chukwuemeka Okonkwo (Institution Relationship Manager) — 34 minutes ago
```

---

## S15 – 10 · Updated Title Deed

```
Create a new screen frame named "S15 – 10 Updated Title Deed", 1440px wide, light grey background.

Layer structure exactly:
- S15 – 10 Updated Title Deed
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Title Deed Updated", subtitle "APP-2026-0184 — Updating Title Deed Information")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, tables, document table rows, success icon treatment, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. Do not draw a decorative certificate, seal, border, or watermark — the deed is represented as a document record with actions, not as a rendered certificate graphic.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0184 / Updated Title Deed

2. Page header row: heading "APP-2026-0184" with the status pill "Completed" beside it on the left. On the right, secondary button "View Application" and blue primary button "Download Title Deed".

3. A success notice card, full width, using the existing subtle success treatment: a green check icon on the left, then bold text "Title Deed Information Updated" and a grey line beneath: "Approved by RERA on Aug 17, 2026. A link to the updated electronic title deed has been emailed to the registered owner."

4. Card — "Changes Applied". A read-only table with columns Field · Previous Value · Updated Value · Status:
   Owner Full Name — Halima Yusuf — Halima Yusuf-Danjuma — Applied (green status pill)
   Owner Phone Number — +234 803 552 1140 — +234 806 774 9218 — Applied (green status pill)

5. Card — "Updated Title Deed Record". Two-column label/value grid:
   Title Deed Number: TD-2021-002917
   Version: 2
   Updated On: Aug 17, 2026
   Original Issue Date: 14 Mar 2021
   Deed Status: Active (green status pill)
   Issuing Authority: RERA — Compliance & Escrow Auditor
   Registered Owner: Halima Yusuf-Danjuma
   Owner Identification: NGA-60218473
   Property Registration Number: RERA-PROP-2021-03356
   Property Type: Residential — Detached House
   Property Address: Plot 8, Gana Street, Maitama, Abuja  (full width row)
   Registered Area: 510 sqm

6. Card — "Output Documents". A document table, same styling as the supporting-documents table, with columns Document Name · Type · Issued · Action:
   Electronic Title Deed Certificate — TD-2021-002917-V2.pdf — Title Deed — Aug 17, 2026 — View / Download / Email Copy
   Payment Receipt — PAY-2026-00944.pdf — Receipt — Aug 17, 2026 — View / Download

7. Card — "Application Record". Read-only label/value grid:
   Application Reference: APP-2026-0184
   Service Name: Updating Title Deed Information
   Submitted On: Aug 17, 2026 — 2:42 PM
   Approved On: Aug 17, 2026 — 3:05 PM
   Completed On: Aug 17, 2026 — 3:05 PM
   Fields Updated: 2
   Total Amount Paid: ₦18,920
   Filed By: Chukwuemeka Okonkwo — Institution Relationship Manager

8. Bottom-right: blue primary button "Download Title Deed".
```
