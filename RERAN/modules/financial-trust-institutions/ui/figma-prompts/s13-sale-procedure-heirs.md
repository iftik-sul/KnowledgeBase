---
project: RERAN
module: financial-trust-institutions
type: reference-sample
status: current
updated: 2026-08-19
contains_proposals: true
written_against_specs_on: 2026-08-18
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/service-13-sale-procedure-heirs.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/submit-application.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in `../screens/` and `../screens-unified/`; where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Service #13: Sale Procedure (Heirs)

**Module:** Financial & Trust Institutions (RERAN Group C)
**Screens:** 11, namespaced `S13 – 01` … `S13 – 11`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | Designed as an **institution-portal** flow | Same call as #17. Source row 40 confirms only the Trustee Centre walk-in path; whether a bank-originated channel exists at all is still open. Portal shell chosen for consistency. |
| 2 | **Payment is a step inside the wizard, before submission** | Sourced: the heir pays at the counter *before* RERA's audit. In portal terms that is the same position as #3 and #17 — step 5. |
| 3 | Tracker reuses the **same 6-step labels** | Consistency across all services. |
| 4 | **No internal certification gate** | Unlike #3, this service has a single approval authority (Compliance & Escrow Auditor). Review & Submit goes straight to Submitted. |
| 5 | **Heirs live in Step 1, property and sale in Step 2** | Step 1 is the parties (institution, deceased owner, heirs); Step 2 is the transaction (property, sale, distribution). Matches the source's own screen ordering — Heir Information before Property & Sale Information. |
| 6 | **Select Property folded into Step 2** | Same call as #3 — a 7th tracker step would break consistency. |
| 7 | **Distribution Confirmation and Registration Confirmation kept as separate screens** | The source lists both, and they are genuinely different events: the Trusts Department transfers the money, RERA issues the documents. Merging them into one completion screen is a defensible simplification if you'd rather — say so and I'll rewrite. |
| 8 | Fee figures are **placeholders** | Exact fee is unresolved client data. |

**New component this service needs:** a **repeatable heir block** — an add/remove group where each entry captures one heir's identity, share and bank account. This is the main reason #13 is in the set. `S13 – 02` is the screen that defines it; get it right there and the rest follows.

**Consistent sample data across all screens** — keep these identical so the screens read as one journey:

- Application ID: `APP-2026-0179`
- Institution: First Bank of Nigeria · `FI-2024-00892` · Commercial Bank
- Acting officer: Chukwuemeka Okonkwo — Institution Relationship Manager
- Deceased owner: Late Chief Emeka Nwachukwu · NIN `NGA-11248907` · Date of Death 12 Feb 2026
- Grant of Probate: `PR/LAG/2026/00841`
- Property: 27 Bourdillon Road, Ikoyi, Lagos · Residential — Detached House · 640 sqm · `RERA-PROP-2019-01147`
- Sale: Sale to Third Party · Sale Value **₦185,000,000** · Purchaser Oluwaseun Bakare · NIN `NGA-52901744` · +234 809 332 1178
- **Heirs (3):**
  1. Ngozi Nwachukwu · NIN `NGA-33471290` · +234 802 118 4471 · ngozi.nwachukwu@email.com · **40%** · First Bank of Nigeria · 3041882756 · ₦74,000,000
  2. Chidi Nwachukwu · NIN `NGA-33471318` · +234 805 774 2210 · chidi.nwachukwu@email.com · **30%** · Guaranty Trust Bank · 0124887301 · ₦55,500,000
  3. Amaka Nwachukwu-Bello · NIN `NGA-33471442` · +234 813 209 6654 · amaka.bello@email.com · **30%** · Zenith Bank · 2078441093 · ₦55,500,000
- Fees: Service Fee ₦80,000 · Processing Levy ₦8,000 · VAT (7.5%) ₦6,600 · **Total ₦94,600**
- Payment Reference: `PAY-2026-00931`
- Distribution Reference: `DST-2026-000417`
- Title Deed Number: `TD-2026-004598`
- Processing time: 25–30 minutes
- Approving authority: RERA — Compliance & Escrow Auditor
- Distributing authority: RERA — Trusts Department

---

## S13 – 01 · Service Details

```
Create a new screen frame named "S13 – 01 Service Details", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 01 Service Details
  - FI-Sidebar        (instance of the existing sidebar component — do not redraw it; active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Details", subtitle "Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, tables, breadcrumbs, section headers, label/value field grids, icons. Do not invent new colours, new type scales, or new card treatments. Match the spacing, corner radius, and white-card-on-grey treatment already used on the Dashboard and Application Review screens.

Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Services Catalog / Sale Procedure (Heirs)

2. Page header row: heading "Sale Procedure (Heirs)" on the left. On the right, a secondary button "Back to Catalog" and a blue primary button "Start Application".

3. Card — "Service Overview". Two-column label/value grid:
   Service Code: #13
   Service Category: Title & Ownership Transaction Services
   Processing Time: 25–30 minutes
   Applicable Fee: ₦80,000 (per RERAN fee schedule)
   Approving Authority: RERA — Compliance & Escrow Auditor
   Payment Timing: Payable before RERA review
   Below the grid, a full-width description paragraph: "Processes the sale of a deceased owner's registered property on behalf of the heirs. On approval, RERA records the ownership change and the Trusts Department transfers each heir's share of the proceeds to their nominated bank account."

4. Card — "How It Works". A single horizontal row of six numbered steps, evenly spaced, each with a number badge and a short label underneath:
   1 Application Info · 2 Service Info · 3 Documents · 4 Validation · 5 Payment · 6 Review & Submit
   Beneath the row, a single grey line: "After RERA approves, the Trusts Department distributes each heir's share before the final documents are issued."

5. Card — "What You'll Need". Two columns side by side.
   Left column heading "Required Information", as a simple bulleted list:
     Property registration number
     Deceased owner's full name and NIN
     Each heir's full name, NIN and contact details
     Each heir's share of the estate
     Each heir's bank account details for distribution
     Sale value, and purchaser details where sold to a third party
   Right column heading "Required Documents", as a list of rows, each with the document name and a small requirement pill:
     Death Certificate of the Deceased Owner — Required
     Grant of Probate / Letters of Administration — Required
     Existing Certificate of Title — Required
     Government-issued Identification (Each Heir) — Required
     Bank Account Confirmation (Each Heir) — Required
     Sale Agreement — Optional
     Other Supporting Documents — Optional

6. Card — "Prerequisites". A short vertical list of check-style rows:
   The property is registered with RERAN under the deceased owner
   Heirship is established by grant of probate or letters of administration
   Each heir's bank account details are available for distribution

7. Card — "Who Can Apply". Two short label/value rows:
   Applicant: Any of the institution's Group C users
   Beneficiaries: Registered heirs of the deceased owner, or their authorized representatives

8. Bottom-right: blue primary button "Start Application".
```

---

## S13 – 02 · Step 1 — Application Info

```
Create a new screen frame named "S13 – 02 Application Info", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 02 Application Info
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, date inputs, section headers, inline notices. Do not invent new colours, type scales, or card treatments. Match the Application Review screen's spacing and card treatment.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action, no illustrations, no avatars, no photographs.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Sale Procedure (Heirs) / New Application

2. Page header row: heading "Sale Procedure (Heirs)" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip (reuse the existing horizontal metadata component), five fields across:
   APPLICATION ID: APP-2026-0179
   SERVICE NAME: Sale Procedure (Heirs)
   STATUS: Draft (status pill)
   LAST UPDATED: Aug 17, 2026 — 11:02 AM
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

6. Card — "Deceased Owner Information". Editable form, two columns:
   Full Name — text input, value "Late Chief Emeka Nwachukwu"
   National Identification Number (NIN) — text input, value "NGA-11248907"
   Date of Death — date input, value "12 Feb 2026"
   Grant of Probate / Administration Number — text input, value "PR/LAG/2026/00841"
   Mark all four as required fields using the existing required-field treatment.

7. Card — "Heirs". This is the important part of this screen — build it as a REPEATABLE FIELD GROUP, and make it a reusable component:

   Card header: heading "Heirs" on the left, and on the right a small grey counter "3 heirs · 100% allocated".

   Beneath the header, three stacked heir blocks. Each block is a light bordered container (not a nested white card — use a subtle border and a slightly recessed background so it reads as a sub-group), containing:
     - A block header row: a small grey uppercase label "HEIR 1", and on the right a small text-only "Remove" action in the existing destructive/muted link style
     - A two-column form:
         Full Name — text input
         National Identification Number (NIN) — text input
         Phone Number — text input
         Email Address — text input
         Share of Estate (%) — text input, narrow
         Bank Name — dropdown
         Account Number — text input
         Account Name — text input
   Values for the three blocks:
     HEIR 1 — Ngozi Nwachukwu · NGA-33471290 · +234 802 118 4471 · ngozi.nwachukwu@email.com · 40 · First Bank of Nigeria · 3041882756 · Ngozi Nwachukwu
     HEIR 2 — Chidi Nwachukwu · NGA-33471318 · +234 805 774 2210 · chidi.nwachukwu@email.com · 30 · Guaranty Trust Bank · 0124887301 · Chidi Nwachukwu
     HEIR 3 — Amaka Nwachukwu-Bello · NGA-33471442 · +234 813 209 6654 · amaka.bello@email.com · 30 · Zenith Bank · 2078441093 · Amaka Nwachukwu-Bello

   Beneath the three blocks, a full-width secondary button with a plus icon: "Add Another Heir".

   Beneath that, a single summary row spanning the card, visually separated by a divider: on the left the label "Total Share Allocated", on the right the value "100%" with a small green check icon beside it.

8. A single-line inline notice beneath the Heirs card, using the existing subtle notice style: "The total share allocated across all heirs must equal 100% before this application can proceed."

9. Step navigation row at the bottom: secondary button "Back" (disabled) on the left, blue primary button "Continue" on the right.
```

---

## S13 – 03 · Step 2 — Service Info

```
Create a new screen frame named "S13 – 03 Service Info", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 03 Service Info
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, search inputs, radio groups, status pills, tables, inline notices, section headers. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action, no illustrations, no maps, no property photographs.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Sale Procedure (Heirs) / New Application

2. Page header row: heading "Sale Procedure (Heirs)" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields and values as the previous step.

4. Horizontal step progress tracker, six steps, step 1 complete, step 2 active.

5. Card — "Select Property". At the top, a single search input labelled "Property Registration Number" with a small "Search" button beside it, value "RERA-PROP-2019-01147". Beneath it, a selected-result panel using the existing subtle bordered treatment, containing:
   - On the left, a two-column label/value grid:
       Property Registration Number: RERA-PROP-2019-01147
       Property Type: Residential — Detached House
       Property Address: 27 Bourdillon Road, Ikoyi, Lagos
       Registered Area: 640 sqm
       Registered Owner: Late Chief Emeka Nwachukwu
   - On the right, a small vertical stack of two validation rows, each a green check icon with a short label:
       Property registered with RERAN
       Owner record matches deceased owner
   - A text link "Change Property" at the bottom of the panel.

6. Card — "Sale Information". Editable form:
   "Sale Type" as a simple vertical radio group with two options: Sale to Third Party (selected), Transfer Among Heirs.
   Beneath it, a two-column form:
     Sale Value — text input, value "₦185,000,000"
     Date of Sale Agreement — date input, value "04 Aug 2026"
   Then a sub-group with a small uppercase grey sub-heading "PURCHASER INFORMATION" and a grey helper line "Required when the property is sold to a third party":
     Full Name — text input, value "Oluwaseun Bakare"
     National Identification Number (NIN) — text input, value "NGA-52901744"
     Phone Number — text input, value "+234 809 332 1178"
     Email Address — text input, value "oluwaseun.bakare@email.com"

7. Card — "Distribution Preview", with a small grey helper line under the heading: "Calculated from the shares entered in the previous step". A read-only table with columns Heir · Share · Bank · Account Number · Amount:
   Ngozi Nwachukwu — 40% — First Bank of Nigeria — 3041882756 — ₦74,000,000
   Chidi Nwachukwu — 30% — Guaranty Trust Bank — 0124887301 — ₦55,500,000
   Amaka Nwachukwu-Bello — 30% — Zenith Bank — 2078441093 — ₦55,500,000
   A total row beneath a divider: Total — 100% — — — ₦185,000,000 (bold)

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S13 – 04 · Step 3 — Documents

```
Create a new screen frame named "S13 – 04 Documents", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 04 Documents
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, the document table, requirement pills, status pills, link-style row actions, inline notices, small uppercase sub-headings. Do not invent new colours, type scales, or card treatments. Match the Supporting Documents table already used on the Application Review screen.

Keep it simple: tables inside cards, no drag-and-drop illustration, no file thumbnails, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Sale Procedure (Heirs) / New Application

2. Page header row: heading "Sale Procedure (Heirs)" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields and values as the previous steps.

4. Horizontal step progress tracker, six steps, steps 1–2 complete, step 3 active.

5. Card — "Supporting Documents". Under the heading, a small grey counter line: "7 of 9 required documents uploaded". On the right of the card header, a secondary text action "Attach from Documents".
   Inside the card, two sections separated by a divider, each introduced by a small uppercase grey sub-heading.

   ESTATE DOCUMENTS — table with columns Document Name · Requirement · Status · Action:
     Death Certificate of the Deceased Owner — Required — Uploaded — View / Replace
     Grant of Probate / Letters of Administration — Required — Uploaded — View / Replace
     Existing Certificate of Title — Required — Uploaded — View / Replace
     Sale Agreement — Optional — Uploaded — View / Replace
     Other Supporting Documents — Optional — Not Uploaded — Upload

   PER-HEIR DOCUMENTS — table with columns Heir · Document Name · Requirement · Status · Action:
     Ngozi Nwachukwu — Government-issued Identification — Required — Uploaded — View / Replace
     Ngozi Nwachukwu — Bank Account Confirmation — Required — Uploaded — View / Replace
     Chidi Nwachukwu — Government-issued Identification — Required — Uploaded — View / Replace
     Chidi Nwachukwu — Bank Account Confirmation — Required — Uploaded — View / Replace
     Amaka Nwachukwu-Bello — Government-issued Identification — Required — Not Uploaded — Upload
     Amaka Nwachukwu-Bello — Bank Account Confirmation — Required — Not Uploaded — Upload

   Use the existing requirement pill style for Required / Optional and the existing status pill style for Uploaded / Not Uploaded.

6. A single-line inline notice beneath the card: "Identification and bank account confirmation must be provided for every heir before this application can proceed."

7. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S13 – 05 · Step 5 — Payment

```
Create a new screen frame named "S13 – 05 Payment", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 05 Payment
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, label/value rows, radio groups, inline notices. Do not invent new colours, type scales, or card treatments. Match the Payment Summary block already used on the Application Review screen.

Keep it simple: two stacked cards, plain radio list for payment method, no card-brand logos, no illustrations.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Sale Procedure (Heirs) / New Application

2. Page header row: heading "Sale Procedure (Heirs)" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Pending Payment".

4. Horizontal step progress tracker, six steps, steps 1–4 complete (Validation shown as automatically passed), step 5 active.

5. Card — "Fee Breakdown". A simple stacked list of label/amount rows, right-aligned amounts, with a divider before the total:
   Service Fee — ₦80,000
   Processing Levy — ₦8,000
   VAT (7.5%) — ₦6,600
   — divider —
   Total Amount Due — ₦94,600  (larger, bold)
   Beneath the total, one small grey line: "This is the RERA service fee only. It is separate from the sale proceeds distributed to the heirs."

6. Card — "Payment Method". A vertical radio group with three plain options, first one selected:
   Card Payment
   Bank Transfer
   USSD
   No logos or brand marks — text labels only, each with a short grey helper line beneath ("Pay with a debit or credit card", "Transfer to a generated account number", "Pay from your mobile phone").

7. A single-line inline notice beneath the cards: "Payment must be completed before this application can be submitted for RERA review."

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Pay ₦94,600" on the right.
```

---

## S13 – 06 · Payment Successful

```
Create a new screen frame named "S13 – 06 Payment Successful", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 06 Payment Successful
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment Successful", subtitle "Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, the horizontal step progress tracker, label/value rows, success icon treatment. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card, no illustration, no confetti, no large graphics. Use the existing green success colour only for the check icon and the status pill.

Workspace content, top to bottom:

1. Horizontal step progress tracker, six steps, steps 1–5 complete, step 6 (Review & Submit) shown as next.

2. One centred card, roughly 720px wide, containing in this order:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Payment Successful"
   - Sub-line, centred, grey: "Your payment has been received. You can now complete and submit this application."
   - The amount, centred and large: ₦94,600
   - A divider
   - A two-column label/value grid:
       Payment Reference: PAY-2026-00931
       Payment Date: Aug 17, 2026 — 11:26 AM
       Payment Method: Card Payment
       Payment Status: Paid (green status pill)
       Application ID: APP-2026-0179
       Service Name: Sale Procedure (Heirs)
   - A divider
   - Two buttons, centred side by side: secondary "Download Receipt", blue primary "Continue to Review"
```

---

## S13 – 07 · Step 6 — Review & Submit

```
Create a new screen frame named "S13 – 07 Review and Submit", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 07 Review and Submit
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Review", subtitle "Review your application before submission.")
    - Workspace

This screen must follow the existing "Application Review" screen already in this file exactly — same card order, same section header treatment, same inline "Edit" links, same document table, same payment summary block, same validation checklist, same declaration row. Reuse every one of those components and styles. Only the content changes. Do not invent new colours, type scales, or card treatments, and do not restructure the layout.

Workspace content, top to bottom:

1. Breadcrumb: Applications / Application Review

2. Page header row: heading "Application Review" on the left. On the right, secondary button "Save Draft" and blue primary button "Submit Application".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0179
   SERVICE NAME: Sale Procedure (Heirs)
   STATUS: Ready for Review (status pill)
   LAST UPDATED: Aug 17, 2026 — 11:28 AM
   CREATED BY: Chukwuemeka Okonkwo

4. Horizontal step progress tracker, six steps, steps 1–5 complete, step 6 active.

5. Card — "Application Summary". Label/value grid:
   Service Name: Sale Procedure (Heirs)
   Application Reference: APP-2026-0179
   Application Type: Online Submission
   Created Date: Aug 17, 2026
   Current Status: Ready for Review (pill)
   Submission Fee: ₦94,600
   Payment Status: Paid (green pill)

6. Card — "Institution Information", with an inline "Edit" link in the card header:
   Institution Name: First Bank of Nigeria
   Registration Number: FI-2024-00892
   Institution Type: Commercial Bank
   Contact Email: operations@firstbanknigeria.com
   Contact Phone: +234 1 905 7000
   Acting Officer: Chukwuemeka Okonkwo — Institution Relationship Manager

7. Card — "Service Information", with an inline "Edit" link:
   Service Name: Sale Procedure (Heirs)
   Service Category: Title & Ownership Transaction Services
   Service Description: Processes the sale of a deceased owner's registered property on behalf of the heirs, with each heir's share distributed to their nominated bank account.
   Processing Time: 25–30 minutes
   Applicable Fee: ₦80,000

8. Card — "Application Details", with an inline "Edit" link. Four sub-groups, each with a small uppercase grey sub-heading and a divider between them:
   DECEASED OWNER
     Full Name: Late Chief Emeka Nwachukwu
     National Identification Number: NGA-11248907
     Date of Death: 12 Feb 2026
     Grant of Probate Number: PR/LAG/2026/00841
   PROPERTY INFORMATION
     Property Registration Number: RERA-PROP-2019-01147
     Property Type: Residential — Detached House
     Property Address: 27 Bourdillon Road, Ikoyi, Lagos
     Registered Area: 640 sqm
   SALE INFORMATION
     Sale Type: Sale to Third Party
     Sale Value: ₦185,000,000
     Date of Sale Agreement: 04 Aug 2026
     Purchaser: Oluwaseun Bakare — NGA-52901744
     Purchaser Contact: +234 809 332 1178
   HEIRS AND DISTRIBUTION
     Render this sub-group as a read-only table, not as label/value pairs. Columns: Heir · NIN · Share · Bank · Account Number · Amount
       Ngozi Nwachukwu — NGA-33471290 — 40% — First Bank of Nigeria — 3041882756 — ₦74,000,000
       Chidi Nwachukwu — NGA-33471318 — 30% — Guaranty Trust Bank — 0124887301 — ₦55,500,000
       Amaka Nwachukwu-Bello — NGA-33471442 — 30% — Zenith Bank — 2078441093 — ₦55,500,000
     Total row beneath a divider: Total — — 100% — — — ₦185,000,000 (bold)

9. Card — "Supporting Documents", counter line "9 of 9 documents uploaded", inline action "Manage Documents". Table with columns Document Name · Requirement · Status · Action, all rows Uploaded, action "View":
   Death Certificate of the Deceased Owner — Required
   Grant of Probate / Letters of Administration — Required
   Existing Certificate of Title — Required
   Sale Agreement — Optional
   Government-issued Identification (Ngozi Nwachukwu) — Required
   Bank Account Confirmation (Ngozi Nwachukwu) — Required
   Government-issued Identification (Chidi Nwachukwu) — Required
   Bank Account Confirmation (Chidi Nwachukwu) — Required
   Government-issued Identification (Amaka Nwachukwu-Bello) — Required
   Bank Account Confirmation (Amaka Nwachukwu-Bello) — Required

10. Card — "Payment Summary":
    Service Fee: ₦80,000
    Processing Levy: ₦8,000
    VAT (7.5%): ₦6,600
    Total Amount Paid: ₦94,600 (larger, bold)
    Payment Reference: PAY-2026-00931
    Payment Date: Aug 17, 2026
    Payment Status: Paid (green pill with check)

11. Card — "Validation Summary", with a green sub-line "All checks passed", then a vertical list of green check rows:
    Required information completed
    Required documents provided
    Institution information valid
    Heirship documentation validated
    Property registered under deceased owner
    Heir shares total 100%
    Bank account details provided for every heir
    Duplicate application check passed
    Payment completed
    Below a dotted divider, a green status line: "All Clear — Ready for Submission"

12. Card — "Declaration". A checked checkbox with the text: "I confirm that the information and documents provided in this application are accurate and complete. I understand that providing false or misleading information may result in application rejection, penalties, or regulatory action against the institution."
```

---

## S13 – 08 · Application Submitted

```
Create a new screen frame named "S13 – 08 Application Submitted", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 08 Application Submitted
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Submitted", subtitle "Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, success icon treatment, numbered list rows. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card plus one short "what happens next" card. No illustration, no large graphics.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Application Submitted"
   - Sub-line, centred, grey: "Your application has been submitted to RERA for review."
   - The reference, centred and large: APP-2026-0179
   - A divider
   - A two-column label/value grid:
       Service Name: Sale Procedure (Heirs)
       Status: Submitted (status pill)
       Submitted On: Aug 17, 2026 — 11:30 AM
       Submitted By: Chukwuemeka Okonkwo
       Heirs: 3
       Total Distribution: ₦185,000,000
       Expected Processing Time: 25–30 minutes
       Reviewing Authority: RERA — Compliance & Escrow Auditor

2. Card — "What Happens Next". Three numbered rows, each with a number badge, a short bold label and one grey line beneath:
   1  RERA Review — The Compliance & Escrow Auditor validates the heirship documentation and the sale details.
   2  Distribution of Proceeds — On approval, the RERA Trusts Department transfers each heir's share to their nominated bank account.
   3  Registration Complete — The ownership change is recorded and the Certificate of Title, Title Deed and Map are emailed to the heirs.

3. Two buttons, centred side by side beneath the cards: secondary "Back to Dashboard", blue primary "View Application".
```

---

## S13 – 09 · Application Details

```
Create a new screen frame named "S13 – 09 Application Details", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 09 Application Details
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Details", subtitle "APP-2026-0179 — Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, tables, document tables, the activity feed row pattern from the Dashboard. Do not invent new colours, type scales, or card treatments.

Keep it simple: a single stacked column of cards, no tabs, no side panel, no charts.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0179

2. Page header row: heading "APP-2026-0179" with the status pill "Under Review" beside it on the left. On the right, secondary button "Download Summary" and secondary button "Withdraw Application".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0179
   SERVICE NAME: Sale Procedure (Heirs)
   STATUS: Under Review (pill)
   SUBMITTED ON: Aug 17, 2026 — 11:30 AM
   CREATED BY: Chukwuemeka Okonkwo

4. Card — "Application Status". A simple vertical timeline, one row per stage, each with a small circular marker on a connecting line, the stage name, a timestamp and the actor. Completed stages use the filled marker, the current stage uses the active marker, future stages use an empty outlined marker:
   Draft — Aug 17, 2026, 11:02 AM — Chukwuemeka Okonkwo  (complete)
   Payment Successful — Aug 17, 2026, 11:26 AM — ₦94,600, PAY-2026-00931  (complete)
   Submitted — Aug 17, 2026, 11:30 AM — Chukwuemeka Okonkwo  (complete)
   Under Review — Aug 17, 2026, 11:33 AM — RERA, Compliance & Escrow Auditor  (current)
   Approved — Pending  (future)
   Distribution of Proceeds — Pending — RERA Trusts Department  (future)
   Completed — Pending  (future)

5. Card — "Estate & Sale Details". Read-only label/value grid, three sub-groups separated by dividers with small uppercase grey sub-headings — DECEASED OWNER, PROPERTY, SALE — using the same fields and values as the corresponding sub-groups on the Review & Submit screen.

6. Card — "Heirs & Distribution". Read-only table with columns Heir · NIN · Share · Bank · Account Number · Amount · Status:
   Ngozi Nwachukwu — NGA-33471290 — 40% — First Bank of Nigeria — 3041882756 — ₦74,000,000 — Pending (status pill)
   Chidi Nwachukwu — NGA-33471318 — 30% — Guaranty Trust Bank — 0124887301 — ₦55,500,000 — Pending (status pill)
   Amaka Nwachukwu-Bello — NGA-33471442 — 30% — Zenith Bank — 2078441093 — ₦55,500,000 — Pending (status pill)
   Total row beneath a divider: Total — — 100% — — — ₦185,000,000 (bold)

7. Card — "Supporting Documents". Table with columns Document Name · Requirement · Status · Action, ten rows, all Uploaded, action "View" — same list as the Review & Submit screen.

8. Card — "Payment". Label/value rows:
   Total Amount Paid: ₦94,600
   Payment Reference: PAY-2026-00931
   Payment Date: Aug 17, 2026
   Payment Method: Card Payment
   Payment Status: Paid (green pill)
   Inline text action on the right of the card header: "Download Receipt"

9. Card — "Activity Log", with a "View All" link in the header. Use the Dashboard's activity feed row pattern — event description on the left, actor and relative timestamp right-aligned:
   Application under review by RERA — RERA (Compliance & Escrow Auditor) — 3 minutes ago
   Application submitted — Chukwuemeka Okonkwo (Institution Relationship Manager) — 6 minutes ago
   Payment completed — ₦94,600 — Chukwuemeka Okonkwo (Institution Relationship Manager) — 10 minutes ago
   Documents attached — 10 files — Chukwuemeka Okonkwo (Institution Relationship Manager) — 18 minutes ago
   Heir details entered — 3 heirs — Chukwuemeka Okonkwo (Institution Relationship Manager) — 28 minutes ago
   Application created — Chukwuemeka Okonkwo (Institution Relationship Manager) — 34 minutes ago
```

---

## S13 – 10 · Distribution Confirmation

```
Create a new screen frame named "S13 – 10 Distribution Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 10 Distribution Confirmation
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Distribution Confirmation", subtitle "APP-2026-0179 — Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, tables, success icon treatment, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, one table as the centrepiece. No charts, no pie graphs, no illustrations — the distribution is shown as a table, not as a visualisation.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0179 / Distribution

2. Page header row: heading "APP-2026-0179" with the status pill "Approved" beside it on the left. On the right, secondary button "View Application" and blue primary button "Download Distribution Statement".

3. A success notice card, full width, using the existing subtle success treatment: a green check icon on the left, then bold text "Heirs' Shares Distributed" and a grey line beneath: "The RERA Trusts Department transferred each heir's share on Aug 17, 2026. Confirmation has been emailed to every heir."

4. Card — "Distribution Summary". Two-column label/value grid:
   Distribution Reference: DST-2026-000417
   Distribution Date: Aug 17, 2026 — 12:04 PM
   Executing Authority: RERA — Trusts Department
   Total Distributed: ₦185,000,000
   Number of Heirs: 3
   Distribution Status: Completed (green status pill)

5. Card — "Heir Transfers". A table with columns Heir · Share · Bank · Account Number · Amount · Transfer Reference · Status:
   Ngozi Nwachukwu — 40% — First Bank of Nigeria — 3041882756 — ₦74,000,000 — TRF-2026-118204 — Transferred (green pill)
   Chidi Nwachukwu — 30% — Guaranty Trust Bank — 0124887301 — ₦55,500,000 — TRF-2026-118205 — Transferred (green pill)
   Amaka Nwachukwu-Bello — 30% — Zenith Bank — 2078441093 — ₦55,500,000 — TRF-2026-118206 — Transferred (green pill)
   Total row beneath a divider: Total — 100% — — — ₦185,000,000 — — (bold)

6. Card — "Sale Record". Read-only label/value grid:
   Property Registration Number: RERA-PROP-2019-01147
   Property Address: 27 Bourdillon Road, Ikoyi, Lagos
   Deceased Owner: Late Chief Emeka Nwachukwu
   Sale Type: Sale to Third Party
   Purchaser: Oluwaseun Bakare — NGA-52901744
   Sale Value: ₦185,000,000

7. A single-line inline notice beneath the cards: "Title registration completes once the ownership change is recorded. The final documents will be issued shortly."

8. Bottom-right: blue primary button "Download Distribution Statement".
```

---

## S13 – 11 · Registration Confirmation

```
Create a new screen frame named "S13 – 11 Registration Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S13 – 11 Registration Confirmation
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Registration Complete", subtitle "APP-2026-0179 — Sale Procedure (Heirs)")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, tables, document table rows, success icon treatment, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. Do not draw a decorative certificate, seal, border, watermark, or map graphic — the output documents are represented as document records with actions, not as rendered artefacts.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0179 / Registration Confirmation

2. Page header row: heading "APP-2026-0179" with the status pill "Completed" beside it on the left. On the right, secondary button "View Application" and blue primary button "Download Documents".

3. A success notice card, full width, using the existing subtle success treatment: a green check icon on the left, then bold text "Sale Registered and Proceeds Distributed" and a grey line beneath: "Approved by RERA on Aug 17, 2026. Ownership has been transferred on the registry and the output documents have been emailed to all heirs and the purchaser."

4. Card — "Registration Record". Two-column label/value grid:
   Title Deed Number: TD-2026-004598
   Registration Date: Aug 17, 2026
   Registry Status: Active (green status pill)
   Approving Authority: RERA — Compliance & Escrow Auditor
   Property Registration Number: RERA-PROP-2019-01147
   Property Type: Residential — Detached House
   Property Address: 27 Bourdillon Road, Ikoyi, Lagos  (full width row)
   Registered Area: 640 sqm
   Previous Owner: Late Chief Emeka Nwachukwu (Deceased)
   New Registered Owner: Oluwaseun Bakare — NGA-52901744
   Sale Value: ₦185,000,000

5. Card — "Distribution", with an inline text action "View Distribution Statement" in the card header. A compact table with columns Heir · Share · Amount · Status:
   Ngozi Nwachukwu — 40% — ₦74,000,000 — Transferred (green pill)
   Chidi Nwachukwu — 30% — ₦55,500,000 — Transferred (green pill)
   Amaka Nwachukwu-Bello — 30% — ₦55,500,000 — Transferred (green pill)
   Total row beneath a divider: Total — 100% — ₦185,000,000 (bold)

6. Card — "Output Documents". A document table, same styling as the supporting-documents table, with columns Document Name · Type · Issued · Action:
   Certificate of Title — TD-2026-004598.pdf — Title Document — Aug 17, 2026 — View / Download / Email Copy
   Title Deed — TD-2026-004598-DEED.pdf — Title Document — Aug 17, 2026 — View / Download / Email Copy
   Property Map — RERA-PROP-2019-01147-MAP.pdf — Map — Aug 17, 2026 — View / Download
   Payment Receipt — PAY-2026-00931.pdf — Receipt — Aug 17, 2026 — View / Download
   Distribution Statement — DST-2026-000417.pdf — Statement — Aug 17, 2026 — View / Download

7. Card — "Application Record". Read-only label/value grid:
   Application Reference: APP-2026-0179
   Service Name: Sale Procedure (Heirs)
   Submitted On: Aug 17, 2026 — 11:30 AM
   Approved On: Aug 17, 2026 — 11:58 AM
   Distributed On: Aug 17, 2026 — 12:04 PM
   Completed On: Aug 17, 2026 — 12:09 PM
   Total Amount Paid: ₦94,600
   Filed By: Chukwuemeka Okonkwo — Institution Relationship Manager

8. Bottom-right: blue primary button "Download Documents".
```
