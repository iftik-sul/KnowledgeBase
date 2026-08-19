---
project: RERAN
module: financial-trust-institutions
type: reference-sample
status: current
updated: 2026-08-19
contains_proposals: true
written_against_specs_on: 2026-08-18
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/service-12-register-real-estate-fund-company.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/submit-application.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in `../screens/` and `../screens-unified/`; where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Service #12: Registration of Real Estate Fund Companies

**Module:** Financial & Trust Institutions (RERAN Group C)
**Screens:** 10, namespaced `S12 – 01` … `S12 – 10`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | Designed as an **institution-portal** flow | Same call as #17, #13 and #15. Source row 38 confirms only the Trustee Centre walk-in path; a bank-originated channel remains unconfirmed. |
| 2 | **Payment is a step inside the wizard, before submission** | Normalized by client decision 2026-08-16. Row 38 originally sourced payment *after* RERA's approval; that ordering was confirmed as an artefact of the physical-counter process and retired. This service's own status flow now runs Draft → Payment Pending → Payment Successful → Submitted. |
| 3 | Tracker reuses the **same 6-step labels** | Consistency across all services. |
| 4 | **No internal certification gate** | Single approval authority (Compliance & Escrow Auditor). No corporate account originates this transaction. |
| 5 | **Ownership Certificate and Registration Confirmation merged into one completion screen** | The source lists both, but unlike #13 (where money moves, then documents issue) these are two output documents produced by the same event. One screen with an output-documents table covers both. |
| 6 | **Property / asset reference is conditional** | Source says "where applicable." Built as a yes/no that reveals the reference field, since open question 2 — whether register-of-privileges entry relates to ordinary title registration — is unresolved. |
| 7 | **Beneficial owners stay a document, not a form** | Source captures unit holders as an uploaded list. Deliberately *not* built as a repeatable group like #13's heirs — that would invent structure the source doesn't have. |
| 8 | Fee figures are **placeholders** | Exact fee is unresolved client data. |

**Two open questions this pack does not resolve**, both harmless for UI but worth raising with the client: what qualifies as a "real estate fund company" for these purposes, and whether registration here also requires separate title registration.

**What this service contributes to the library:** the **document-dominant variant** of Pattern A. Where #3 and #17 carry documents as a supporting step, here the documents *are* the substance — six of them, with file metadata. `S12 – 04` is the screen that earns this service its slot.

**Consistent sample data across all screens** — keep these identical so the screens read as one journey:

- Application ID: `APP-2026-0191`
- Institution: First Bank of Nigeria · `FI-2024-00892` · Commercial Bank
- Acting officer: Chukwuemeka Okonkwo — Institution Relationship Manager
- Fund company: Meridian Real Estate Fund PLC · RC `RC-1428907` · incorporated 09 Jun 2022
- Fund type: Closed-End Real Estate Investment Fund
- Authorized representative: Tunde Ogunleye — Fund Manager · NIN `NGA-71039284` · +234 807 665 3319 · tunde.ogunleye@meridianfund.ng
- Nature of privilege: Registered Ownership Interest
- Linked asset: `RERA-PROP-2023-05502` — Meridian Court, 12 Kofo Abayomi Street, Victoria Island, Lagos
- Unit holders on file: 24
- Fees: Service Fee ₦120,000 · Processing Levy ₦12,000 · VAT (7.5%) ₦9,900 · **Total ₦153,900**
- Payment Reference: `PAY-2026-00957`
- Register of Privileges Number: `ROP-2026-000238`
- Ownership Certificate Number: `OC-2026-000238`
- Processing time: 25–30 minutes
- Approving authority: RERA — Compliance & Escrow Auditor

---

## S12 – 01 · Service Details

```
Create a new screen frame named "S12 – 01 Service Details", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 01 Service Details
  - FI-Sidebar        (instance of the existing sidebar component — do not redraw it; active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Details", subtitle "Registration of Real Estate Fund Companies")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, tables, breadcrumbs, section headers, label/value field grids, icons. Do not invent new colours, new type scales, or new card treatments. Match the spacing, corner radius, and white-card-on-grey treatment already used on the Dashboard and Application Review screens.

Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Services Catalog / Registration of Real Estate Fund Companies

2. Page header row: heading "Registration of Real Estate Fund Companies" on the left. On the right, a secondary button "Back to Catalog" and a blue primary button "Start Application".

3. Card — "Service Overview". Two-column label/value grid:
   Service Code: #12
   Service Category: Title & Ownership Transaction Services
   Processing Time: 25–30 minutes
   Applicable Fee: ₦120,000 (per RERAN fee schedule)
   Approving Authority: RERA — Compliance & Escrow Auditor
   Payment Timing: Payable before RERA review
   Below the grid, a full-width description paragraph: "Records a real estate fund company's ownership interest in the register of privileges — an ownership register distinct from ordinary property title. On approval, RERA issues an ownership certificate and assigns a register of privileges registration number."

4. Card — "How It Works". A single horizontal row of six numbered steps, evenly spaced, each with a number badge and a short label underneath:
   1 Application Info · 2 Service Info · 3 Documents · 4 Validation · 5 Payment · 6 Review & Submit

5. Card — "What You'll Need". Two columns side by side.
   Left column heading "Required Information", as a simple bulleted list:
     Fund company legal name
     Certificate of incorporation number
     Authorized representative details
     Nature of the privilege or interest being registered
     Property or asset reference, where applicable
   Right column heading "Required Documents", as a list of rows, each with the document name and a small requirement pill:
     Certificate of Incorporation — Required
     Trust Deed / Fund Constitution — Required
     Register of Privileges Application Form — Required
     List of Unit Holders / Beneficial Owners — Required
     Government-issued Identification (Authorized Representative) — Required
     Other Supporting Documents — Optional

6. Card — "Prerequisites". A short vertical list of check-style rows:
   The fund company is validly constituted
   The fund company's interest is capable of registration in the register of privileges
   All supporting documents are available

7. Card — "What You'll Receive". A short vertical list of three rows, each with a small document icon and a one-line label:
   E-Ownership Certificate in the name of the fund
   Register of Privileges Registration Number document
   Payment receipt

8. Card — "Who Can Apply". Two short label/value rows:
   Applicant: Any of the institution's Group C users
   Customer: The real estate fund company's authorized representative

9. Bottom-right: blue primary button "Start Application".
```

---

## S12 – 02 · Step 1 — Application Info

```
Create a new screen frame named "S12 – 02 Application Info", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 02 Application Info
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Registration of Real Estate Fund Companies")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, date inputs, section headers. Do not invent new colours, type scales, or card treatments. Match the Application Review screen's spacing and card treatment.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action, no illustrations, no company logos, no avatars.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Registration of Real Estate Fund Companies / New Application

2. Page header row: heading "Registration of Real Estate Fund Companies" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip (reuse the existing horizontal metadata component), five fields across:
   APPLICATION ID: APP-2026-0191
   SERVICE NAME: Registration of Real Estate Fund Companies
   STATUS: Draft (status pill)
   LAST UPDATED: Aug 17, 2026 — 4:06 PM
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

6. Card — "Fund Company Information". Editable form, two columns:
   Fund Company Legal Name — text input, value "Meridian Real Estate Fund PLC"
   Certificate of Incorporation Number — text input, value "RC-1428907"
   Date of Incorporation — date input, value "09 Jun 2022"
   Fund Type — dropdown, value "Closed-End Real Estate Investment Fund"
   Registered Office Address — text input spanning both columns, value "12 Kofo Abayomi Street, Victoria Island, Lagos"
   Mark Fund Company Legal Name, Certificate of Incorporation Number and Fund Type as required fields using the existing required-field treatment.

7. Card — "Authorized Representative". Editable form, two columns:
   Full Name — text input, value "Tunde Ogunleye"
   Position — text input, value "Fund Manager"
   National Identification Number (NIN) — text input, value "NGA-71039284"
   Phone Number — text input, value "+234 807 665 3319"
   Email Address — text input, value "tunde.ogunleye@meridianfund.ng"
   Mark Full Name, Position, NIN, Phone Number and Email Address as required.

8. Step navigation row at the bottom: secondary button "Back" (disabled) on the left, blue primary button "Continue" on the right.
```

---

## S12 – 03 · Step 2 — Service Info

```
Create a new screen frame named "S12 – 03 Service Info", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 03 Service Info
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Registration of Real Estate Fund Companies")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, search inputs, radio groups, text areas, status pills, inline notices, section headers. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action, no illustrations, no maps, no property photographs.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Registration of Real Estate Fund Companies / New Application

2. Page header row: heading "Registration of Real Estate Fund Companies" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields and values as the previous step.

4. Horizontal step progress tracker, six steps, step 1 complete, step 2 active.

5. Card — "Service Information", read-only label/value grid, two columns:
   Service Name: Registration of Real Estate Fund Companies
   Service Category: Title & Ownership Transaction Services
   Processing Time: 25–30 minutes
   Applicable Fee: ₦120,000
   Full-width row — Service Description: "Records a real estate fund company's ownership interest in the register of privileges, distinct from ordinary property title registration."

6. Card — "Registration Details". Editable form:
   Nature of the Privilege / Interest — dropdown, value "Registered Ownership Interest", marked required
   Beneath it, a full-width text area labelled "Description of the Interest", marked required, with the value: "Registered ownership interest held by the fund over the Meridian Court development, to be recorded in the register of privileges."

7. Card — "Linked Asset". Inside the card:
   - "Is this interest linked to a registered property or asset?" as a simple horizontal radio group with two options: Yes (selected), No.
   - Beneath it, revealed by the Yes selection, a search input labelled "Property or Asset Reference" with a small "Search" button beside it, value "RERA-PROP-2023-05502", followed by a selected-result panel using the existing subtle bordered treatment:
       Property Registration Number: RERA-PROP-2023-05502
       Asset Name: Meridian Court
       Property Type: Commercial — Mixed Use
       Address: 12 Kofo Abayomi Street, Victoria Island, Lagos
     with a text link "Change Asset" at the bottom of the panel.
   - A small grey line beneath the panel: "Leave this as No where the privilege is not tied to a specific registered asset."

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S12 – 04 · Step 3 — Documents

```
Create a new screen frame named "S12 – 04 Documents", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 04 Documents
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Registration of Real Estate Fund Companies")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, the document table, requirement pills, status pills, link-style row actions, inline notices. Do not invent new colours, type scales, or card treatments. Match the Supporting Documents table already used on the Application Review screen, extending it with the extra file-metadata columns described below.

Keep it simple: one table inside one card. No drag-and-drop illustration, no file thumbnails, no preview panes, no decorative graphics — this screen is document-heavy, so the table carries it.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Registration of Real Estate Fund Companies / New Application

2. Page header row: heading "Registration of Real Estate Fund Companies" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields and values as the previous steps.

4. Horizontal step progress tracker, six steps, steps 1–2 complete, step 3 active.

5. Card — "Supporting Documents". Under the heading, a small grey counter line: "4 of 5 required documents uploaded". On the right of the card header, a secondary text action "Attach from Documents".
   Table with columns: Document Name · Requirement · File · Uploaded · Status · Action
     Certificate of Incorporation — Required — meridian-certificate-of-incorporation.pdf (1.2 MB) — Aug 17, 2026 — Uploaded — View / Replace
     Trust Deed / Fund Constitution — Required — meridian-trust-deed.pdf (4.8 MB) — Aug 17, 2026 — Uploaded — View / Replace
     Register of Privileges Application Form — Required — rop-application-form-signed.pdf (860 KB) — Aug 17, 2026 — Uploaded — View / Replace
     List of Unit Holders / Beneficial Owners — Required — meridian-unit-holders-24.xlsx (312 KB) — Aug 17, 2026 — Uploaded — View / Replace
     Government-issued Identification (Authorized Representative) — Required — — — Not Uploaded — Upload
     Other Supporting Documents — Optional — — — Not Uploaded — Upload
   Use the existing requirement pill style for Required / Optional and the existing status pill style for Uploaded / Not Uploaded. Leave the File and Uploaded cells empty for rows not yet uploaded.

6. A single-line inline notice beneath the card, using the existing subtle notice style: "The list of unit holders must be current as at the date of application. RERA may return the application where the list does not reconcile with the fund constitution."

7. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.
```

---

## S12 – 05 · Step 5 — Payment

```
Create a new screen frame named "S12 – 05 Payment", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 05 Payment
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Registration of Real Estate Fund Companies")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, label/value rows, radio groups, inline notices. Do not invent new colours, type scales, or card treatments. Match the Payment Summary block already used on the Application Review screen.

Keep it simple: two stacked cards, plain radio list for payment method, no card-brand logos, no illustrations.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Registration of Real Estate Fund Companies / New Application

2. Page header row: heading "Registration of Real Estate Fund Companies" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Payment Pending".

4. Horizontal step progress tracker, six steps, steps 1–4 complete (Validation shown as automatically passed), step 5 active.

5. Card — "Fee Breakdown". A simple stacked list of label/amount rows, right-aligned amounts, with a divider before the total:
   Service Fee — ₦120,000
   Processing Levy — ₦12,000
   VAT (7.5%) — ₦9,900
   — divider —
   Total Amount Due — ₦153,900  (larger, bold)
   Beneath the total, one small grey line: "Payable by the fund company. An e-receipt is issued once payment clears."

6. Card — "Payment Method". A vertical radio group with three plain options, first one selected:
   Card Payment
   Bank Transfer
   USSD
   No logos or brand marks — text labels only, each with a short grey helper line beneath ("Pay with a debit or credit card", "Transfer to a generated account number", "Pay from your mobile phone").

7. A single-line inline notice beneath the cards: "Payment must be completed before this application can be submitted for RERA review."

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Pay ₦153,900" on the right.
```

---

## S12 – 06 · Payment Successful

```
Create a new screen frame named "S12 – 06 Payment Successful", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 06 Payment Successful
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment Successful", subtitle "Registration of Real Estate Fund Companies")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, the horizontal step progress tracker, label/value rows, success icon treatment. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card, no illustration, no confetti, no large graphics. Use the existing green success colour only for the check icon and the status pill.

Workspace content, top to bottom:

1. Horizontal step progress tracker, six steps, steps 1–5 complete, step 6 (Review & Submit) shown as next.

2. One centred card, roughly 720px wide, containing in this order:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Payment Successful"
   - Sub-line, centred, grey: "Your payment has been received and an e-receipt issued. You can now complete and submit this application."
   - The amount, centred and large: ₦153,900
   - A divider
   - A two-column label/value grid:
       Payment Reference: PAY-2026-00957
       Payment Date: Aug 17, 2026 — 4:31 PM
       Payment Method: Card Payment
       Payment Status: Paid (green status pill)
       Application ID: APP-2026-0191
       Paid By: Meridian Real Estate Fund PLC
   - A divider
   - Two buttons, centred side by side: secondary "Download e-Receipt", blue primary "Continue to Review"
```

---

## S12 – 07 · Step 6 — Review & Submit

```
Create a new screen frame named "S12 – 07 Review and Submit", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 07 Review and Submit
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Review", subtitle "Review your application before submission.")
    - Workspace

This screen must follow the existing "Application Review" screen already in this file exactly — same card order, same section header treatment, same inline "Edit" links, same document table, same payment summary block, same validation checklist, same declaration row. Reuse every one of those components and styles. Only the content changes. Do not invent new colours, type scales, or card treatments, and do not restructure the layout.

Workspace content, top to bottom:

1. Breadcrumb: Applications / Application Review

2. Page header row: heading "Application Review" on the left. On the right, secondary button "Save Draft" and blue primary button "Submit Application".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0191
   SERVICE NAME: Registration of Real Estate Fund Companies
   STATUS: Ready for Review (status pill)
   LAST UPDATED: Aug 17, 2026 — 4:33 PM
   CREATED BY: Chukwuemeka Okonkwo

4. Horizontal step progress tracker, six steps, steps 1–5 complete, step 6 active.

5. Card — "Application Summary". Label/value grid:
   Service Name: Registration of Real Estate Fund Companies
   Application Reference: APP-2026-0191
   Application Type: Online Submission
   Created Date: Aug 17, 2026
   Current Status: Ready for Review (pill)
   Submission Fee: ₦153,900
   Payment Status: Paid (green pill)

6. Card — "Institution Information", with an inline "Edit" link in the card header:
   Institution Name: First Bank of Nigeria
   Registration Number: FI-2024-00892
   Institution Type: Commercial Bank
   Contact Email: operations@firstbanknigeria.com
   Contact Phone: +234 1 905 7000
   Acting Officer: Chukwuemeka Okonkwo — Institution Relationship Manager

7. Card — "Service Information", with an inline "Edit" link:
   Service Name: Registration of Real Estate Fund Companies
   Service Category: Title & Ownership Transaction Services
   Service Description: Records a real estate fund company's ownership interest in the register of privileges.
   Processing Time: 25–30 minutes
   Applicable Fee: ₦120,000

8. Card — "Application Details", with an inline "Edit" link. Three sub-groups, each with a small uppercase grey sub-heading and a divider between them:
   FUND COMPANY
     Legal Name: Meridian Real Estate Fund PLC
     Certificate of Incorporation Number: RC-1428907
     Date of Incorporation: 09 Jun 2022
     Fund Type: Closed-End Real Estate Investment Fund
     Registered Office Address: 12 Kofo Abayomi Street, Victoria Island, Lagos
   AUTHORIZED REPRESENTATIVE
     Full Name: Tunde Ogunleye
     Position: Fund Manager
     National Identification Number: NGA-71039284
     Phone Number: +234 807 665 3319
     Email Address: tunde.ogunleye@meridianfund.ng
   REGISTRATION DETAILS
     Nature of the Privilege / Interest: Registered Ownership Interest
     Linked Asset: Yes
     Property or Asset Reference: RERA-PROP-2023-05502 — Meridian Court
     Asset Address: 12 Kofo Abayomi Street, Victoria Island, Lagos
     Unit Holders on File: 24
     Description of the Interest (full width): "Registered ownership interest held by the fund over the Meridian Court development, to be recorded in the register of privileges."

9. Card — "Supporting Documents", counter line "6 of 6 documents uploaded", inline action "Manage Documents". Table with columns Document Name · Requirement · File · Status · Action, all rows Uploaded, action "View":
   Certificate of Incorporation — Required — meridian-certificate-of-incorporation.pdf
   Trust Deed / Fund Constitution — Required — meridian-trust-deed.pdf
   Register of Privileges Application Form — Required — rop-application-form-signed.pdf
   List of Unit Holders / Beneficial Owners — Required — meridian-unit-holders-24.xlsx
   Government-issued Identification (Authorized Representative) — Required — tunde-ogunleye-id.pdf
   Other Supporting Documents — Optional — meridian-board-resolution.pdf

10. Card — "Payment Summary":
    Service Fee: ₦120,000
    Processing Levy: ₦12,000
    VAT (7.5%): ₦9,900
    Total Amount Paid: ₦153,900 (larger, bold)
    Payment Reference: PAY-2026-00957
    Payment Date: Aug 17, 2026
    Payment Status: Paid (green pill with check)

11. Card — "Validation Summary", with a green sub-line "All checks passed", then a vertical list of green check rows:
    Required information completed
    Required documents provided
    Institution information valid
    Fund company constitution validated
    Authorized representative verified
    Linked asset record matched
    Duplicate application check passed
    Payment completed
    Below a dotted divider, a green status line: "All Clear — Ready for Submission"

12. Card — "Declaration". A checked checkbox with the text: "I confirm that the information and documents provided in this application are accurate and complete. I understand that providing false or misleading information may result in application rejection, penalties, or regulatory action against the institution."
```

---

## S12 – 08 · Application Submitted

```
Create a new screen frame named "S12 – 08 Application Submitted", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 08 Application Submitted
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Submitted", subtitle "Registration of Real Estate Fund Companies")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, success icon treatment, numbered list rows. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card plus one short "what happens next" card. No illustration, no large graphics.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Application Submitted"
   - Sub-line, centred, grey: "Your application has been submitted to RERA for review."
   - The reference, centred and large: APP-2026-0191
   - A divider
   - A two-column label/value grid:
       Service Name: Registration of Real Estate Fund Companies
       Status: Submitted (status pill)
       Submitted On: Aug 17, 2026 — 4:35 PM
       Submitted By: Chukwuemeka Okonkwo
       Fund Company: Meridian Real Estate Fund PLC
       Total Amount Paid: ₦153,900
       Expected Processing Time: 25–30 minutes
       Reviewing Authority: RERA — Compliance & Escrow Auditor

2. Card — "What Happens Next". Three numbered rows, each with a number badge, a short bold label and one grey line beneath:
   1  RERA Review — The Compliance & Escrow Auditor validates the fund constitution and supporting documents.
   2  Register Entry — On approval, the fund company's interest is recorded in the register of privileges and a registration number is assigned.
   3  Certificate Issued — The ownership certificate and registration number document are emailed to the authorized representative.

3. Two buttons, centred side by side beneath the cards: secondary "Back to Dashboard", blue primary "View Application".
```

---

## S12 – 09 · Application Details

```
Create a new screen frame named "S12 – 09 Application Details", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 09 Application Details
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Details", subtitle "APP-2026-0191 — Registration of Real Estate Fund Companies")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, the activity feed row pattern from the Dashboard. Do not invent new colours, type scales, or card treatments.

Keep it simple: a single stacked column of cards, no tabs, no side panel, no charts.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0191

2. Page header row: heading "APP-2026-0191" with the status pill "Under Review" beside it on the left. On the right, secondary button "Download Summary" and secondary button "Withdraw Application".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0191
   SERVICE NAME: Registration of Real Estate Fund Companies
   STATUS: Under Review (pill)
   SUBMITTED ON: Aug 17, 2026 — 4:35 PM
   CREATED BY: Chukwuemeka Okonkwo

4. Card — "Application Status". A simple vertical timeline, one row per stage, each with a small circular marker on a connecting line, the stage name, a timestamp and the actor. Completed stages use the filled marker, the current stage uses the active marker, future stages use an empty outlined marker:
   Draft — Aug 17, 2026, 4:06 PM — Chukwuemeka Okonkwo  (complete)
   Payment Successful — Aug 17, 2026, 4:31 PM — ₦153,900, PAY-2026-00957  (complete)
   Submitted — Aug 17, 2026, 4:35 PM — Chukwuemeka Okonkwo  (complete)
   Under Review — Aug 17, 2026, 4:38 PM — RERA, Compliance & Escrow Auditor  (current)
   Approved — Pending  (future)
   Completed — Pending  (future)

5. Card — "Fund Company & Registration". Read-only label/value grid, three sub-groups separated by dividers with small uppercase grey sub-headings — FUND COMPANY, AUTHORIZED REPRESENTATIVE, REGISTRATION DETAILS — using the same fields and values as the corresponding sub-groups on the Review & Submit screen.

6. Card — "Supporting Documents". Table with columns Document Name · Requirement · File · Status · Action, six rows, all Uploaded, action "View" — same list as the Review & Submit screen.

7. Card — "Payment". Label/value rows:
   Total Amount Paid: ₦153,900
   Payment Reference: PAY-2026-00957
   Payment Date: Aug 17, 2026
   Payment Method: Card Payment
   Payment Status: Paid (green pill)
   Inline text action on the right of the card header: "Download e-Receipt"

8. Card — "Activity Log", with a "View All" link in the header. Use the Dashboard's activity feed row pattern — event description on the left, actor and relative timestamp right-aligned:
   Application under review by RERA — RERA (Compliance & Escrow Auditor) — 3 minutes ago
   Application submitted — Chukwuemeka Okonkwo (Institution Relationship Manager) — 6 minutes ago
   Payment completed — ₦153,900 — Chukwuemeka Okonkwo (Institution Relationship Manager) — 10 minutes ago
   Documents attached — 6 files — Chukwuemeka Okonkwo (Institution Relationship Manager) — 19 minutes ago
   Fund company details entered — Chukwuemeka Okonkwo (Institution Relationship Manager) — 28 minutes ago
   Application created — Chukwuemeka Okonkwo (Institution Relationship Manager) — 35 minutes ago
```

---

## S12 – 10 · Registration Confirmation

```
Create a new screen frame named "S12 – 10 Registration Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S12 – 10 Registration Confirmation
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Registration Complete", subtitle "APP-2026-0191 — Registration of Real Estate Fund Companies")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, document table rows, success icon treatment, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. Do not draw a decorative certificate, seal, border, or watermark — the certificate and registration document are represented as document records with actions, not as rendered artefacts.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0191 / Registration Confirmation

2. Page header row: heading "APP-2026-0191" with the status pill "Completed" beside it on the left. On the right, secondary button "View Application" and blue primary button "Download Documents".

3. A success notice card, full width, using the existing subtle success treatment: a green check icon on the left, then bold text "Registered in the Register of Privileges" and a grey line beneath: "Approved by RERA on Aug 17, 2026. The ownership certificate and registration number document have been emailed to tunde.ogunleye@meridianfund.ng."

4. Card — "Register of Privileges Entry". Two-column label/value grid:
   Register of Privileges Number: ROP-2026-000238
   Registration Date: Aug 17, 2026
   Entry Status: Active (green status pill)
   Approving Authority: RERA — Compliance & Escrow Auditor
   Fund Company: Meridian Real Estate Fund PLC
   Certificate of Incorporation Number: RC-1428907
   Nature of the Privilege / Interest: Registered Ownership Interest
   Linked Asset: RERA-PROP-2023-05502 — Meridian Court
   Asset Address: 12 Kofo Abayomi Street, Victoria Island, Lagos  (full width row)
   Authorized Representative: Tunde Ogunleye — Fund Manager

5. Card — "Ownership Certificate". Two-column label/value grid:
   Certificate Number: OC-2026-000238
   Issue Date: Aug 17, 2026
   Issued To: Meridian Real Estate Fund PLC
   Certificate Status: Active (green status pill)

6. Card — "Output Documents". A document table, same styling as the supporting-documents table, with columns Document Name · Type · Issued · Action:
   E-Ownership Certificate — OC-2026-000238.pdf — Ownership Certificate — Aug 17, 2026 — View / Download / Email Copy
   Register of Privileges Registration Document — ROP-2026-000238.pdf — Registration Record — Aug 17, 2026 — View / Download / Email Copy
   Payment e-Receipt — PAY-2026-00957.pdf — Receipt — Aug 17, 2026 — View / Download

7. Card — "Application Record". Read-only label/value grid:
   Application Reference: APP-2026-0191
   Service Name: Registration of Real Estate Fund Companies
   Submitted On: Aug 17, 2026 — 4:35 PM
   Approved On: Aug 17, 2026 — 5:02 PM
   Completed On: Aug 17, 2026 — 5:02 PM
   Total Amount Paid: ₦153,900
   Filed By: Chukwuemeka Okonkwo — Institution Relationship Manager

8. Bottom-right: blue primary button "Download Documents".
```
