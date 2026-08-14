---
project: ERP
module: sales-and-billing
type: data-model
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Order Model

## Core Order entity

Holds: customer, dates, status, line items, delivery, billing. Industry-specific fields do not live here — see the custom-fields layer in modules/platform/architecture.md (mechanism not yet designed).

## Delivery

- Delivery can happen in multiple installments, each with a Delivery Challan.
- A single Challan can bundle multiple Production Orders/products from the same parent Order.
- Delivered qty can exceed ordered qty but never be less, at invoice time.
- Supporting-document attachments (e.g., artwork files, approval cards) can be uploaded at the Order level, separate from internally-generated working files. Printing supports "parent document alone" or "parent document + attachments."

## Billing

- One Bill can consolidate multiple fully-delivered Orders for the same customer.
- Once billed, an Order closes (one-to-one bill relationship — cannot appear on another bill).
- Bill is only created after all ordered qty is delivered.
- Bill columns: SL No, Job No, Particulars, Challan No, Quantity, Unit Price, Amount.
- The rate-calculation rule (how line amount is derived from qty and rate) is a configurable rule per company/item — see Industry Variations below.

## Multi-currency

Invoices can be billed in a currency different from the company's home currency. Each customer has a default conversion rate, overridable per invoice.

## Manufacturing linkage

One Production Order per product within a parent Order (full detail in modules/manufacturing/production-model.md). Independent status, produced qty, balance qty, priority per Production Order.

---

## Industry Variations

### Woven Label Manufacturing

- Custom Order fields: O/No, Card, File#, Pick/acc, Item Code, PO No, JH SO/NO, ref no, Color Code 1–8, Comments.
- Line items: Label Description / Size / Qty / Rate / Amount / File Name / Repit.
- Workflow: Order created → File# assigned (digital artwork file) → Card (physical Sample Card made from the artwork file, sent to customer for approval, supports revisions v1, v2, ...).
- Material Requisition is called "Yarn Requisition Slip"; can be submitted before or after the Sample Card (parallel, not sequential).
- **Rate-calculation rule:** `amount = (qty in pcs / 12) × dozen rate`. This is this template's convention, not a platform-wide rule.
- Numbering: Order Number 5-digit numeric; Card No 4-digit numeric; File Name = letter + digits (e.g., "L5568"); Pick/Acc = two numbers separated by a slash (e.g., "1652/72").
- Operates under two trade names for the same business (one on Orders, a different one on Bills/Requisitions), same address.

### Circle Packaging

- Broader 17-product portfolio (woven/printed labels, stickers/tags, packaging materials, trims, add-ons) — the case that proved the generic Item Master is needed (see modules/platform/architecture.md).
- Trade-finance-heavy workflow: introduces Proforma Invoice (PI) and Letter of Credit (LC) as new pipeline concepts not present in the Woven Label template.
  - **LC statuses:** Awaited, Received, Verified, Expiring Soon, Expired.
  - PI List screen designed; PI Create screen deferred (presentation-value sequencing).
- **Open decisions specific to this template:** PI numbering format, PI revision handling, PI-to-Order cardinality (one PI → one Order? one PI → many Orders?).
- Manufactured vs. traded item distinction (production vs. procurement) is currently out of scope for this template.
