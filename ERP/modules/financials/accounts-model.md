---
project: ERP
module: financials
type: data-model
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Accounts Model

Three ledgers auto-post to a central General Ledger:

1. **Daily Cash / petty cash** — continuous rolling, never resets, opening = prior day's closing. A per-individual Loan Ledger runs in parallel. Expense categories are user-definable ("Particulars").
2. **Customer Receivables**
3. **Vendor Payments**

Plus:

- Manual Journal Entry (sequential Journal No, date, reference/narration, balanced debit/credit lines).
- Financial Reports: Trial Balance, P&L, Balance Sheet, Job Profitability.
- Bank Account Management with reconciliation.
- Aging Reports.
- Financial Year Closing.
- Audit Trail.

## Out of scope

Fixed Assets/Depreciation, Budgeting/Forecasting, Cost Accounting/Cost Centers.
