---
project: RERAN
module: financial-trust-institutions
type: reference-sample
status: current
updated: 2026-08-19
contains_proposals: true
written_against_specs_on: 2026-08-17
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/service-03-mortgage-registration.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/submit-application.md"
  - "RERAN/modules/financial-trust-institutions/ui/screens-unified/application-review.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - figma
  - reference
---

> **This is a reference sample, not a specification.** It shows the pattern new Figma prompt packs should follow. The authoritative behaviour spec lives in `../screens/` and `../screens-unified/`; where this pack and a spec disagree, the spec wins. See [README.md](README.md).

# Figma AI Prompt Pack — Service #3: Mortgage Registration

**Module:** Financial & Trust Institutions (RERAN Group C)
**Screens:** 11, namespaced `S3 – 01` … `S3 – 11`
**How to use:** each prompt below is self-contained. Copy one block at a time into Figma AI.

---

## Assumptions baked into these prompts

| # | Assumption | Why |
| :-- | :-- | :-- |
| 1 | Designed as the **institution-portal** channel | Unlike #17, this is the *sourced* primary channel. The Trustee Centre assisted-mode variant is not designed here. |
| 2 | **Payment is upfront — before internal certification and before lodging** | Sourced and corrected throughout the service file. See the doc defect note below. |
| 3 | Tracker reuses the **same 6-step labels** as #17 and the built Application Review | Consistency across services beats per-service tracker shapes. |
| 4 | **Select Property is folded into Step 2 (Service Info)**, not given its own step | The service file lists it as a separate screen, but a 7th tracker step would break consistency with every other service. It appears as a property lookup card at the top of Step 2. |
| 5 | **Validation has no standalone screen** | Auto-passes; surfaces as the Validation Summary card on Review & Submit. |
| 6 | **The filer also certifies the transaction** | Explicitly permitted — certification is unrestricted, including the person who filed it. Showing this demonstrates the unified-access model rather than implying a maker-checker gate that doesn't exist. |
| 7 | Output shown as **Certificate of Title** | Source lists five possible output documents without stating selection criteria (open question 2). One is shown; swap if criteria land. |
| 8 | **No Service #6 dependency indicator anywhere** | Decided 2026-08-16: the real-estate-developer dependency stays entirely invisible on this side. Every prompt below explicitly forbids adding one. |
| 9 | Fee figures reuse your Application Review sample | Real fee is a configuration fact still unresolved. |

> **Doc defect worth fixing in the repo.** `service-03-mortgage-registration.md` §9 states the corrected upfront model in its first paragraph, then the second paragraph still says *"submission is free; the fee is settled only once RERA has approved the transaction."* That contradicts §5, §12, §13, §20 and Business Rule 4, all of which carry the corrected upfront model. Classic drift — the correction landed everywhere except that one paragraph. These prompts follow the upfront model.

**Consistent sample data across all screens** — keep these identical so the screens read as one journey:

- Application ID: `APP-2026-0172`
- Institution: First Bank of Nigeria · `FI-2024-00892` · Commercial Bank
- Institution Reference: `FBN-MTG-2026-0447`
- Acting officer / filer / certifier: Chukwuemeka Okonkwo — Institution Relationship Manager
- Borrower: Adebayo Adesanya · NIN `NGA-29384756` · +234 812 345 6789 · adebayo.adesanya@email.com
- Property: Eko Atlantic City, Victoria Island, Lagos · Residential — Apartment · 185 sqm · `RERA-PROP-2024-04521`
- Mortgage: Loan Amount ₦45,000,000 · Term 20 years · Interest Rate 9.5% · LTV 75% · Deed Reference `MTG-DEED-2026-00318`
- Fees: Service Fee ₦50,000 · Processing Levy ₦5,000 · VAT (7.5%) ₦4,125 · **Total ₦59,125**
- Payment Reference: `PAY-2026-00918`
- Mortgage Registration Number: `MTG-2026-001284`
- Processing time: 20–25 minutes
- Approving authority: RERA — Compliance & Escrow Auditor

---

## S3 – 01 · Service Details

```
Create a new screen frame named "S3 – 01 Service Details", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 01 Service Details
  - FI-Sidebar        (instance of the existing sidebar component — do not redraw it; active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Service Details", subtitle "Mortgage Registration")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, tables, breadcrumbs, section headers, label/value field grids, icons. Do not invent new colours, new type scales, or new card treatments. Match the spacing, corner radius, and white-card-on-grey treatment already used on the Dashboard and Application Review screens.

Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Services Catalog / Mortgage Registration

2. Page header row: heading "Mortgage Registration" on the left. On the right, a secondary button "Back to Catalog" and a blue primary button "Start Application".

3. Card — "Service Overview". Two-column label/value grid:
   Service Code: #3
   Service Category: Mortgage Services
   Processing Time: 20–25 minutes
   Applicable Fee: ₦50,000 (per RERAN fee schedule)
   Approving Authority: RERA — Compliance & Escrow Auditor
   Payment Timing: Payable upfront, before the application is lodged
   Below the grid, a full-width description paragraph: "Records a new mortgage against a registered property title. The transaction is certified internally by the institution, then audited by RERA before the mortgage record takes effect on the property registry."

4. Card — "How It Works". A single horizontal row of six numbered steps, evenly spaced, each with a number badge and a short label underneath:
   1 Application Info · 2 Service Info · 3 Documents · 4 Validation · 5 Payment · 6 Review & Submit
   Beneath the row, a single grey line: "After submission, the transaction passes internal certification within your institution before it is routed to RERA for audit."

5. Card — "What You'll Need". Two columns side by side.
   Left column heading "Required Information", as a simple bulleted list:
     Institution reference number
     Borrower full name, NIN and contact details
     Property registration number, address and type
     Loan amount, mortgage term and interest rate
     Mortgage deed reference
   Right column heading "Required Documents", as a list of rows, each with the document name and a small requirement pill:
     Existing Certificate of Title — Required
     Mortgage Agreement / Deed of Mortgage — Required
     Loan Offer Letter — Required
     Property Valuation Report — Required
     Government-issued Identification (Borrower) — Required
     Other Supporting Documents — Optional

6. Card — "Prerequisites". A short vertical list of check-style rows:
   The property is registered with RERAN and its title is verified
   The borrower has completed all mortgage requirements with the bank
   The mortgage deed has been executed

7. Card — "Who Can Apply". Two short label/value rows:
   Applicant: Any of the institution's Group C users
   Counterparty: Registered Property Owner granting the mortgage

8. Bottom-right: blue primary button "Start Application".

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 02 · Step 1 — Application Info

```
Create a new screen frame named "S3 – 02 Application Info", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 02 Application Info
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Mortgage Registration")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, section headers. Do not invent new colours, type scales, or card treatments. Match the Application Review screen's spacing and card treatment.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action, no illustrations or decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Mortgage Registration / New Application

2. Page header row: heading "Mortgage Registration" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip (reuse the existing horizontal metadata component), five fields across:
   APPLICATION ID: APP-2026-0172
   SERVICE NAME: Mortgage Registration
   STATUS: Draft (status pill)
   LAST UPDATED: Aug 17, 2026 — 10:04 AM
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
   Below the grid, one editable text input labelled "Institution Reference Number", value "FBN-MTG-2026-0447", with helper text "Your internal reference for this mortgage".

6. Card — "Borrower Information". Editable form, two columns:
   Full Name — text input, value "Adebayo Adesanya"
   National Identification Number (NIN) — text input, value "NGA-29384756"
   Phone Number — text input, value "+234 812 345 6789"
   Email Address — text input, value "adebayo.adesanya@email.com"
   Mark all four as required fields using the existing required-field treatment.

7. Step navigation row at the bottom: secondary button "Back" (disabled) on the left, blue primary button "Continue" on the right.

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 03 · Step 2 — Service Info

```
Create a new screen frame named "S3 – 03 Service Info", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 03 Service Info
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Mortgage Registration")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, form inputs, dropdowns, search inputs, status pills, inline notices, section headers. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards, plain two-column form layout, one blue primary action, no illustrations, no maps, no property photographs.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Mortgage Registration / New Application

2. Page header row: heading "Mortgage Registration" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields and values as the previous step.

4. Horizontal step progress tracker, six steps, step 1 complete, step 2 active.

5. Card — "Select Property". At the top, a single search input labelled "Property Registration Number" with a small "Search" button beside it, value "RERA-PROP-2024-04521". Beneath it, a selected-result panel using the existing subtle bordered treatment, containing:
   - On the left, a two-column label/value grid:
       Property Registration Number: RERA-PROP-2024-04521
       Property Type: Residential — Apartment
       Property Address: Eko Atlantic City, Victoria Island, Lagos
       Registered Area: 185 sqm
       Registered Owner: Adebayo Adesanya
   - On the right, a small vertical stack of two validation rows, each a green check icon with a short label:
       Property registered with RERAN
       Title verified
   - A text link "Change Property" at the bottom of the panel.

6. Card — "Mortgage Information". Editable form, two columns:
   Loan Amount — text input, value "₦45,000,000"
   Mortgage Term — text input, value "20 years"
   Interest Rate — text input, value "9.5%"
   Loan-to-Value Ratio — text input, value "75%"
   Mortgage Deed Reference — text input, value "MTG-DEED-2026-00318"
   Mortgagee (Institution) — read-only value "First Bank of Nigeria — FI-2024-00892"
   Mark Loan Amount, Mortgage Term, Interest Rate and Mortgage Deed Reference as required.

7. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 04 · Step 3 — Documents

```
Create a new screen frame named "S3 – 04 Documents", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 04 Documents
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Mortgage Registration")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, the document table, requirement pills, status pills, link-style row actions, inline notices. Do not invent new colours, type scales, or card treatments. Match the Supporting Documents table already used on the Application Review screen.

Keep it simple: one table inside one card, no drag-and-drop illustration, no file thumbnails, no decorative graphics.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Mortgage Registration / New Application

2. Page header row: heading "Mortgage Registration" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields and values as the previous steps.

4. Horizontal step progress tracker, six steps, steps 1–2 complete, step 3 active.

5. Card — "Supporting Documents". Under the heading, a small grey counter line: "4 of 5 required documents uploaded". On the right of the card header, a secondary text action "Attach from Documents".
   Table with columns: Document Name · Requirement · Status · Action
     Existing Certificate of Title — Required — Uploaded — View / Replace
     Mortgage Agreement / Deed of Mortgage — Required — Uploaded — View / Replace
     Loan Offer Letter — Required — Uploaded — View / Replace
     Property Valuation Report — Required — Uploaded — View / Replace
     Government-issued Identification (Borrower) — Required — Not Uploaded — Upload
     Other Supporting Documents — Optional — Not Uploaded — Upload
   Use the existing requirement pill style for Required / Optional and the existing status pill style for Uploaded / Not Uploaded.

6. A single-line inline notice beneath the card, using the existing subtle notice style: "The internal certification record is generated by the system at the certification stage and does not need to be uploaded here."

7. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Continue" on the right.

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 05 · Step 5 — Payment

```
Create a new screen frame named "S3 – 05 Payment", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 05 Payment
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "New Application", subtitle "Mortgage Registration")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, the horizontal step progress tracker, the application metadata strip, label/value rows, radio groups, inline notices. Do not invent new colours, type scales, or card treatments. Match the Payment Summary block already used on the Application Review screen.

Keep it simple: two stacked cards, plain radio list for payment method, no card-brand logos, no illustrations.

Workspace content, top to bottom:

1. Breadcrumb: Service Requests / Mortgage Registration / New Application

2. Page header row: heading "Mortgage Registration" on the left, secondary button "Save Draft" on the right.

3. Application metadata strip, same five fields as the previous steps, but STATUS pill now reads "Payment Pending".

4. Horizontal step progress tracker, six steps, steps 1–4 complete (Validation shown as automatically passed), step 5 active.

5. Card — "Fee Breakdown". A simple stacked list of label/amount rows, right-aligned amounts, with a divider before the total:
   Service Fee — ₦50,000
   Processing Levy — ₦5,000
   VAT (7.5%) — ₦4,125
   — divider —
   Total Amount Due — ₦59,125  (larger, bold)
   Beneath the total, one small grey line: "Paid by the institution via the shared platform payment gateway."

6. Card — "Payment Method". A vertical radio group with three plain options, first one selected:
   Card Payment
   Bank Transfer
   USSD
   No logos or brand marks — text labels only, each with a short grey helper line beneath ("Pay with a debit or credit card", "Transfer to a generated account number", "Pay from your mobile phone").

7. A single-line inline notice beneath the cards: "Payment must be completed before this application can be lodged or sent for internal certification."

8. Step navigation row at the bottom: secondary button "Back" on the left, blue primary button "Pay ₦59,125" on the right.

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 06 · Payment Confirmation

```
Create a new screen frame named "S3 – 06 Payment Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 06 Payment Confirmation
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Payment Successful", subtitle "Mortgage Registration")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, the horizontal step progress tracker, label/value rows, success icon treatment. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card, no illustration, no confetti, no large graphics. Use the existing green success colour only for the check icon and the status pill.

Workspace content, top to bottom:

1. Horizontal step progress tracker, six steps, steps 1–5 complete, step 6 (Review & Submit) shown as next.

2. One centred card, roughly 720px wide, containing in this order:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Payment Successful"
   - Sub-line, centred, grey: "Your payment has been received. You can now complete and submit this application for internal certification."
   - The amount, centred and large: ₦59,125
   - A divider
   - A two-column label/value grid:
       Payment Reference: PAY-2026-00918
       Payment Date: Aug 17, 2026 — 10:19 AM
       Payment Method: Card Payment
       Payment Status: Paid (green status pill)
       Application ID: APP-2026-0172
       Service Name: Mortgage Registration
   - A divider
   - Two buttons, centred side by side: secondary "Download Receipt", blue primary "Continue to Review"

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 07 · Step 6 — Review & Submit

```
Create a new screen frame named "S3 – 07 Review and Submit", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 07 Review and Submit
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Service Requests")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Review", subtitle "Review your application before submission.")
    - Workspace

This screen must follow the existing "Application Review" screen already in this file exactly — same card order, same section header treatment, same inline "Edit" links, same document table, same payment summary block, same validation checklist, same declaration row. Reuse every one of those components and styles. Only the content changes. Do not invent new colours, type scales, or card treatments, and do not restructure the layout.

Workspace content, top to bottom:

1. Breadcrumb: Applications / Application Review

2. Page header row: heading "Application Review" on the left. On the right, secondary button "Save Draft" and blue primary button "Submit for Internal Certification".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0172
   SERVICE NAME: Mortgage Registration
   STATUS: Ready for Review (status pill)
   LAST UPDATED: Aug 17, 2026 — 10:21 AM
   CREATED BY: Chukwuemeka Okonkwo

4. Horizontal step progress tracker, six steps, steps 1–5 complete, step 6 active.

5. Card — "Application Summary". Label/value grid:
   Service Name: Mortgage Registration
   Application Reference: APP-2026-0172
   Application Type: Online Submission
   Created Date: Aug 17, 2026
   Current Status: Ready for Review (pill)
   Submission Fee: ₦59,125
   Payment Status: Paid (green pill)

6. Card — "Institution Information", with an inline "Edit" link in the card header:
   Institution Name: First Bank of Nigeria
   Registration Number: FI-2024-00892
   Institution Type: Commercial Bank
   Institution Reference: FBN-MTG-2026-0447
   Contact Email: operations@firstbanknigeria.com
   Acting Officer: Chukwuemeka Okonkwo — Institution Relationship Manager

7. Card — "Service Information", with an inline "Edit" link:
   Service Name: Mortgage Registration
   Service Category: Mortgage Services
   Service Description: Records a new mortgage against a registered property title, subject to internal certification and RERA audit.
   Processing Time: 20–25 minutes
   Applicable Fee: ₦50,000

8. Card — "Application Details", with an inline "Edit" link. Three sub-groups, each with a small uppercase grey sub-heading and a divider between them:
   BORROWER INFORMATION
     Full Name: Adebayo Adesanya
     National Identification Number: NGA-29384756
     Phone Number: +234 812 345 6789
     Email Address: adebayo.adesanya@email.com
   PROPERTY INFORMATION
     Property Registration Number: RERA-PROP-2024-04521
     Property Type: Residential — Apartment
     Property Address: Eko Atlantic City, Victoria Island, Lagos
     Registered Area: 185 sqm
   MORTGAGE INFORMATION
     Loan Amount: ₦45,000,000
     Mortgage Term: 20 years
     Interest Rate: 9.5%
     Loan-to-Value Ratio: 75%
     Mortgage Deed Reference: MTG-DEED-2026-00318
     Mortgagee: First Bank of Nigeria — FI-2024-00892

9. Card — "Supporting Documents", counter line "6 of 6 documents uploaded", inline action "Manage Documents". Table with columns Document Name · Requirement · Status · Action:
   Existing Certificate of Title — Required — Uploaded — View
   Mortgage Agreement / Deed of Mortgage — Required — Uploaded — View
   Loan Offer Letter — Required — Uploaded — View
   Property Valuation Report — Required — Uploaded — View
   Government-issued Identification (Borrower) — Required — Uploaded — View
   Other Supporting Documents — Optional — Uploaded — View

10. Card — "Payment Summary":
    Service Fee: ₦50,000
    Processing Levy: ₦5,000
    VAT (7.5%): ₦4,125
    Total Amount Paid: ₦59,125 (larger, bold)
    Payment Reference: PAY-2026-00918
    Payment Date: Aug 17, 2026
    Payment Status: Paid (green pill with check)

11. Card — "Validation Summary", with a green sub-line "All checks passed", then a vertical list of green check rows:
    Required information completed
    Required documents provided
    Institution information valid
    Property registered and title verified
    Borrower ownership confirmed
    Duplicate application check passed
    Payment completed
    Below a dotted divider, a green status line: "All Clear — Ready for Internal Certification"

12. Card — "Declaration". A checked checkbox with the text: "I confirm that the information and documents provided in this application are accurate and complete. I understand that providing false or misleading information may result in application rejection, penalties, or regulatory action against the institution."

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 08 · Submitted for Internal Certification

```
Create a new screen frame named "S3 – 08 Submitted for Certification", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 08 Submitted for Certification
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Submitted for Internal Certification", subtitle "Mortgage Registration")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, label/value rows, success icon treatment, numbered list rows. Do not invent new colours, type scales, or card treatments.

Keep it simple: one centred confirmation card plus one short "what happens next" card. No illustration, no large graphics.

Workspace content, top to bottom:

1. One centred card, roughly 720px wide:
   - A single green circular check icon, centred, modest in size
   - Heading, centred: "Submitted for Internal Certification"
   - Sub-line, centred, grey: "This transaction is now waiting to be certified within your institution before it is routed to RERA."
   - The reference, centred and large: APP-2026-0172
   - A divider
   - A two-column label/value grid:
       Service Name: Mortgage Registration
       Status: Pending Internal Certification (status pill)
       Submitted On: Aug 17, 2026 — 10:23 AM
       Submitted By: Chukwuemeka Okonkwo
       Total Amount Paid: ₦59,125
       Expected Processing Time: 20–25 minutes

2. Card — "What Happens Next". Three numbered rows, each with a number badge, a short bold label and one grey line beneath:
   1  Internal Certification — Any user in your institution, including you, can certify or return this transaction. The acting user is recorded in the audit trail.
   2  RERA Audit — Once certified, the transaction is routed to RERA's Transaction Audit queue for review.
   3  Registration Complete — On approval, the mortgage is recorded on the registry and the output documents are emailed to the borrower.

3. Two buttons, centred side by side beneath the cards: secondary "View Application", blue primary "Go to Internal Certification".

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 09 · Internal Certification — Review Transaction

```
Create a new screen frame named "S3 – 09 Internal Certification Review", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 09 Internal Certification Review
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Internal Certification")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Internal Certification", subtitle "APP-2026-0172 — Mortgage Registration")
    - Workspace

This is the detail screen reached from the existing Internal Certification Queue — do not redesign the queue list itself.

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, text areas, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: a single stacked column of read-only summary cards, then one decision card at the bottom. No tabs, no side-by-side comparison panel, no charts.

Workspace content, top to bottom:

1. Breadcrumb: Internal Certification / APP-2026-0172

2. Page header row: heading "APP-2026-0172" with the status pill "Pending Internal Certification" beside it on the left. On the right, a secondary button "Return to Filer" and a blue primary button "Certify Transaction".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0172
   SERVICE NAME: Mortgage Registration
   STATUS: Pending Internal Certification (pill)
   FILED ON: Aug 17, 2026 — 10:23 AM
   FILED BY: Chukwuemeka Okonkwo — Institution Relationship Manager

4. A single-line inline notice using the existing subtle notice style: "Any user in this institution may certify this transaction, including the person who filed it. Your name and role will be recorded in the audit trail."

5. Card — "Transaction Summary". Read-only label/value grid, three sub-groups separated by dividers with small uppercase grey sub-headings:
   BORROWER
     Full Name: Adebayo Adesanya
     National Identification Number: NGA-29384756
     Phone Number: +234 812 345 6789
     Email Address: adebayo.adesanya@email.com
   PROPERTY
     Property Registration Number: RERA-PROP-2024-04521
     Property Type: Residential — Apartment
     Property Address: Eko Atlantic City, Victoria Island, Lagos
     Registered Area: 185 sqm
   MORTGAGE
     Loan Amount: ₦45,000,000
     Mortgage Term: 20 years
     Interest Rate: 9.5%
     Loan-to-Value Ratio: 75%
     Mortgage Deed Reference: MTG-DEED-2026-00318
     Institution Reference: FBN-MTG-2026-0447

6. Card — "Supporting Documents". Table with columns Document Name · Requirement · Status · Action, six rows, all Uploaded, action "View":
   Existing Certificate of Title, Mortgage Agreement / Deed of Mortgage, Loan Offer Letter, Property Valuation Report, Government-issued Identification (Borrower) — all Required; Other Supporting Documents — Optional.

7. Card — "Payment". Label/value rows:
   Total Amount Paid: ₦59,125
   Payment Reference: PAY-2026-00918
   Payment Date: Aug 17, 2026
   Payment Status: Paid (green pill)

8. Card — "Certification Decision". Inside the card:
   - A text area labelled "Certification Notes", with helper text "Required when returning a transaction to the filer", left empty
   - Beneath it, a row of two buttons aligned right: secondary "Return to Filer", blue primary "Certify Transaction"
   - A small grey line under the buttons: "Certifying routes this transaction to RERA's Transaction Audit queue."

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 10 · Application Details

```
Create a new screen frame named "S3 – 10 Application Details", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 10 Application Details
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Application Details", subtitle "APP-2026-0172 — Mortgage Registration")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, the application metadata strip, label/value grids, document tables, the activity feed row pattern from the Dashboard. Do not invent new colours, type scales, or card treatments.

Keep it simple: a single stacked column of cards, no tabs, no side panel, no charts.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0172

2. Page header row: heading "APP-2026-0172" with the status pill "Under Review" beside it on the left. On the right, secondary button "Download Summary" and secondary button "Withdraw Application".

3. Application metadata strip:
   APPLICATION ID: APP-2026-0172
   SERVICE NAME: Mortgage Registration
   STATUS: Under Review (pill)
   SUBMITTED ON: Aug 17, 2026 — 10:31 AM
   CREATED BY: Chukwuemeka Okonkwo

4. Card — "Application Status". A simple vertical timeline, one row per stage, each with a small circular marker on a connecting line, the stage name, a timestamp and the actor. Completed stages use the filled marker, the current stage uses the active marker, future stages use an empty outlined marker:
   Draft — Aug 17, 2026, 10:04 AM — Chukwuemeka Okonkwo  (complete)
   Payment Successful — Aug 17, 2026, 10:19 AM — ₦59,125, PAY-2026-00918  (complete)
   Pending Internal Certification — Aug 17, 2026, 10:23 AM — Chukwuemeka Okonkwo  (complete)
   Certified Internally — Aug 17, 2026, 10:29 AM — Chukwuemeka Okonkwo (Institution Relationship Manager)  (complete)
   Submitted — Aug 17, 2026, 10:31 AM — Routed to RERA Transaction Audit  (complete)
   Under Review — Aug 17, 2026, 10:33 AM — RERA, Compliance & Escrow Auditor  (current)
   Approved — Pending  (future)
   Completed — Pending  (future)

5. Card — "Transaction Details". Read-only label/value grid, three sub-groups separated by dividers with small uppercase grey sub-headings — BORROWER, PROPERTY, MORTGAGE — using the same fields and values as the Transaction Summary card on the Internal Certification screen.

6. Card — "Supporting Documents". Table with columns Document Name · Requirement · Status · Action, six rows, all Uploaded, action "View".

7. Card — "Payment". Label/value rows:
   Total Amount Paid: ₦59,125
   Payment Reference: PAY-2026-00918
   Payment Date: Aug 17, 2026
   Payment Method: Card Payment
   Payment Status: Paid (green pill)
   Inline text action on the right of the card header: "Download Receipt"

8. Card — "Activity Log", with a "View All" link in the header. Use the Dashboard's activity feed row pattern — event description on the left, actor and relative timestamp right-aligned:
   Application under review by RERA — RERA (Compliance & Escrow Auditor) — 4 minutes ago
   Transaction routed to RERA Transaction Audit — System — 6 minutes ago
   Certified internally — Chukwuemeka Okonkwo (Institution Relationship Manager) — 8 minutes ago
   Submitted for internal certification — Chukwuemeka Okonkwo (Institution Relationship Manager) — 14 minutes ago
   Payment completed — ₦59,125 — Chukwuemeka Okonkwo (Institution Relationship Manager) — 18 minutes ago
   Documents attached — 6 files — Chukwuemeka Okonkwo (Institution Relationship Manager) — 25 minutes ago
   Application created — Chukwuemeka Okonkwo (Institution Relationship Manager) — 33 minutes ago

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```

---

## S3 – 11 · Registration Confirmation

```
Create a new screen frame named "S3 – 11 Registration Confirmation", 1440px wide, light grey background.

Layer structure exactly:
- S3 – 11 Registration Confirmation
  - FI-Sidebar        (instance of the existing sidebar component — active nav item = "Applications")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "Mortgage Registered", subtitle "APP-2026-0172 — Mortgage Registration")
    - Workspace

Reuse existing components and styles from this file wherever one already exists — cards, buttons, breadcrumbs, status pills, label/value grids, document table rows, success icon treatment, inline notices. Do not invent new colours, type scales, or card treatments.

Keep it simple: stacked white cards. Do not draw a decorative certificate, seal, border, or watermark — the output documents are represented as document records with actions, not as rendered certificate graphics.

Workspace content, top to bottom:

1. Breadcrumb: Applications / APP-2026-0172 / Registration Confirmation

2. Page header row: heading "APP-2026-0172" with the status pill "Completed" beside it on the left. On the right, secondary button "View Application" and blue primary button "Download Documents".

3. A success notice card, full width, using the existing subtle success treatment: a green check icon on the left, then bold text "Mortgage Successfully Registered" and a grey line beneath: "Approved by RERA on Aug 17, 2026. The mortgage is now recorded on the property registry and the output documents have been emailed to adebayo.adesanya@email.com."

4. Card — "Mortgage Record". Two-column label/value grid:
   Mortgage Registration Number: MTG-2026-001284
   Registration Date: Aug 17, 2026
   Registry Status: Active (green status pill)
   Approving Authority: RERA — Compliance & Escrow Auditor
   Mortgagee: First Bank of Nigeria — FI-2024-00892
   Mortgagor (Borrower): Adebayo Adesanya
   Property Registration Number: RERA-PROP-2024-04521
   Property Type: Residential — Apartment
   Property Address: Eko Atlantic City, Victoria Island, Lagos  (full width row)
   Loan Amount: ₦45,000,000
   Mortgage Term: 20 years
   Interest Rate: 9.5%
   Mortgage Deed Reference: MTG-DEED-2026-00318

5. Card — "Output Documents". A document table, same styling as the supporting-documents table, with columns Document Name · Type · Issued · Action:
   Certificate of Title — MTG-2026-001284.pdf — Title Document — Aug 17, 2026 — View / Download / Email Copy
   Payment Receipt — PAY-2026-00918.pdf — Receipt — Aug 17, 2026 — View / Download

6. Card — "Application Record". Read-only label/value grid:
   Application Reference: APP-2026-0172
   Service Name: Mortgage Registration
   Submitted On: Aug 17, 2026 — 10:31 AM
   Certified Internally By: Chukwuemeka Okonkwo — Institution Relationship Manager
   Approved On: Aug 17, 2026 — 10:54 AM
   Completed On: Aug 17, 2026 — 10:54 AM
   Total Amount Paid: ₦59,125
   Filed By: Chukwuemeka Okonkwo — Institution Relationship Manager

7. Bottom-right: blue primary button "Download Documents".

Do not add any indicator, badge, notice, or reference relating to developer sales, linked sales, or any downstream service that depends on this record.
```
