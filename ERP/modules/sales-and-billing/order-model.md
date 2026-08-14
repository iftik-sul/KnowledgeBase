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

Holds: customer, dates, status, delivery, billing, and one or more Order Lines. Only fields genuinely true regardless of what's in the Order live here — an Order can span multiple industry categories, so per-product data does not belong at this level.

## Order Line — the atomic fulfillment unit

Since a single Order can mix categories (e.g., a Woven Label line and a Plastic Bag line in the same Order), the Order itself is not the right scope for per-product data. Each **Order Line** holds: the Item (from the Item Master), ordered qty, rate, amount.

An Order Line's category-specific custom fields are driven by its Item's category, not by the Order as a whole — see [modules/platform/custom-fields-layer.md](/ERP/modules/platform/custom-fields-layer.md). This is what lets one Order mix categories cleanly: a Woven Label line renders Pick/Acc; a Plastic Bag line in the same Order does not.

## Fulfillment: Make vs. Buy, and split fulfillment

Each Order Line is fulfilled by one or more of:

- **Production Order(s)** — manufactured in-house. See [modules/manufacturing/production-model.md](/ERP/modules/manufacturing/production-model.md).
- **Sourcing Order(s)** — bought from a vendor specifically to fulfill this Order Line. See [modules/procurement/sourcing-order.md](/ERP/modules/procurement/sourcing-order.md).

Default fulfillment type comes from the Item Master's `is_manufacturable` flag: items not on the manufactured list are always sourced (no BOM exists for them). Manufacturable items default to a Production Order but can be fully or partially converted to a Sourcing Order — including mid-course, if a production issue arises after work has already started.

An Order Line's **Balance Qty** = Ordered Qty − (sum of qty committed across all its Production Orders and Sourcing Orders combined). This lets one Order Line be split — e.g. 600 units produced in-house and 400 sourced from a vendor to cover a capacity shortfall — without cancelling or recreating the Order Line itself.

## Delivery

- Delivery can happen in multiple installments, each with a Delivery Challan.
- A single Challan can bundle multiple Order Lines from the same parent Order, regardless of whether each line was fulfilled by production, sourcing, or a split of both. Delivery does not care which path supplied the stock, only that it's ready.
- Delivered qty can exceed ordered qty but never be less, at invoice time.
- Supporting-document attachments (e.g., artwork files, approval cards) can be uploaded at the Order level, separate from internally-generated working files. Printing supports "parent document alone" or "parent document + attachments."

## Billing

- One Bill can consolidate multiple fully-delivered Orders for the same customer.
- Once billed, an Order closes (one-to-one bill relationship — cannot appear on another bill).
- Bill is only created after all ordered qty, across every Order Line, is delivered.
- Bill columns: SL No, Job No, Particulars, Challan No, Quantity, Unit Price, Amount.
- The rate-calculation rule (how line amount is derived from qty and rate) is a configurable rule per company/item — see Industry Variations below.

## Multi-currency

Invoices can be billed in a currency different from the company's home currency. Each customer has a default conversion rate, overridable per invoice.

---

## Industry Variations

### Woven Label

- Custom fields, scoped to the **Order Line** (not the whole Order): O/No, Card, File#, Pick/acc, Item Code, PO No, JH SO/NO, ref no, Color Code 1–8, Comments. A Woven Label line within a mixed-category Order carries these; a non-Woven-Label line in the same Order does not.
- Line items: Label Description / Size / Qty / Rate / Amount / File Name / Repit.
- Workflow: Order Line created → File# assigned (digital artwork file) → Card (physical Sample Card made from the artwork file, sent to customer for approval, supports revisions v1, v2, ...).
- Material Requisition ("Yarn Requisition Slip") is created per Production Order fulfilling a Woven Label line; can be submitted before or after the Sample Card.
- **Rate-calculation rule:** `amount = (qty in pcs / 12) × dozen rate`. A Woven Label industry convention, not a platform-wide rule.
- Numbering: Order Number 5-digit numeric; Card No 4-digit numeric; File Name = letter + digits (e.g., "L5568"); Pick/Acc = two numbers separated by a slash (e.g., "1652/72"). One company's chosen config values, not fixed for every Woven Label company.
- The reference deployment operates under two trade names for the same business, same address — an example of the multi-letterhead capability, not a Woven Label industry requirement.

### Packaging

- Multi-category product portfolio (woven/printed labels, stickers/tags, packaging materials, trims, add-ons) — the category that proved the generic Item Master is needed.
- Trade-finance-heavy workflow: introduces Proforma Invoice (PI) and Letter of Credit (LC) as new pipeline concepts not present in the Woven Label category.
  - **LC statuses:** Awaited, Received, Verified, Expiring Soon, Expired.
  - PI List screen designed; PI Create screen deferred (presentation-value sequencing).
- **Open decisions specific to this category:** PI numbering format, PI revision handling, PI-to-Order cardinality (one PI → one Order? one PI → many Orders?).
- Manufactured vs. traded item distinction is handled generically at the platform level (Order Line Make/Buy fork — see above), not as a category-specific concern. Each item in this category's portfolio just needs `is_manufacturable` set correctly on its Item Master record.
