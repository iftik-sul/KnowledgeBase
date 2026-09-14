---
project: RERAN
module: regulatory-authority
type: services-overview
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/modules/*/service-flows/"
---

# Group A — Services Overview

Group A has **no service catalogue of its own**. Unlike every other group, it does
not file applications or pay fees. Its "services" are the approval touchpoints of
the work other groups submit: every external service terminates in a Group A
decision, and this document is the register of those touchpoints.

Each row below is one external service (from RED, FTI, RESC, or Individual User),
the Group A role that finishes it, and the sub-system channel that role works in.
For the full submission logic of any service, see the originating module's own
service-flow — this register cross-references, it does not duplicate.

## Coverage

- **114 external services** route to Group A (RED 27 · FTI 18 · RESC 26 · IU 43).
- **105 need a Group A decision**; 9 are automated lookups or wrappers that need none.
- Channel split: Transaction Audit Queue **79** · Escrow / Trust-Account Audit **13**
  · Licensing & Registry **9** · Tribunal & Remote-Litigation **4** · no decision **9**.

`[proposed]` marks a service whose source did not name a Group A role explicitly;
the assignment is a reasoned proposal awaiting client confirmation (see
[open-questions.md](open-questions.md)).

## Register

| Origin | # | Service | Group A role | Sub-system / channel | Processing time |
|---|---|---|---|---|---|
| RED | 1 | Register Initial Sale | Compliance & Escrow Auditor | Transaction Audit Queue | 6 business days |
| RED | 2 | Register Initial Rent-to-Own | Compliance & Escrow Auditor | Transaction Audit Queue | 6 business days |
| RED | 3 | Register Initial Usufruct | Compliance & Escrow Auditor | Transaction Audit Queue | 6 business days |
| RED | 4 | Amend Initial Procedures Data | Compliance & Escrow Auditor | Transaction Audit Queue | 6 business days |
| RED | 5 | Complete Initial Procedures Data | Compliance & Escrow Auditor | Transaction Audit Queue | 6 business days |
| RED | 6 | Register Sale Associated with an Initial Mortgage | Compliance & Escrow Auditor | Transaction Audit Queue | 6 business days |
| RED | 7 | Transfer Registration Fees Between Properties | Compliance & Escrow Auditor | Transaction Audit Queue | 6 business days |
| RED | 8 | Escrow Account Activation | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 20 business hours |
| RED | 9 | Escrow Account Transfer | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 24 working hours |
| RED | 10 | Project Profit Withdrawal | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 29 business hours |
| RED | 11 | Amend the Cap of Administrative, Marketing and VAT Expenses | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 26 business hours |
| RED | 12 | Receive a Payment from the Project's Escrow Account | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 29 business hours |
| RED | 13 | Registration of Real Estate Project | Compliance & Escrow Auditor | Transaction Audit Queue | Project registration: 3 business days |
| RED | 14 | Real Estate Project Cancellation | Compliance & Escrow Auditor | Transaction Audit Queue | 15 minutes |
| RED | 15 | Real Estate Project Sub-division | Compliance & Escrow Auditor | Transaction Audit Queue | 30 minutes |
| RED | 16 | Changing the Name of a Real Estate Project | Compliance & Escrow Auditor | Transaction Audit Queue | 30 minutes |
| RED | 17 | Project Re-registration | Compliance & Escrow Auditor | Transaction Audit Queue | 40 minutes |
| RED | 18 | Settlements Application | Compliance & Escrow Auditor | Transaction Audit Queue | 7 hours 30 minutes |
| RED | 19 | Request Termination of Initial Registration | Compliance & Escrow Auditor | Transaction Audit Queue | 8 hours 30 minutes |
| RED | 20 | Depositing a Mortgage into an Escrow Account | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 26 working hours |
| RED | 21 | Bank Guarantee Cancellation | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 26 business hours |
| RED | 22 | Real Estate Licensing Application | Licensing & Registration Officer | Licensing & Registry | 5 minutes |
| RED | 23 | Accreditation of Training Entities | Licensing & Registration Officer | Licensing & Registry | 4 business days |
| RED | 24 | Registration/Amendment of Real Estate Project Details | Compliance & Escrow Auditor | Transaction Audit Queue | 5 business days |
| RED | 25 | Issuing Map Application | Compliance & Escrow Auditor | Transaction Audit Queue | One business day |
| RED | 26 | Separation or Annexing a Property | Compliance & Escrow Auditor | Transaction Audit Queue | One business day |
| RED | 27 | Requesting a Technical Report for the Project | Compliance & Escrow Auditor | Transaction Audit Queue | 5 business days |
| FTI | 1 | Approval / Renewal of Account Trustee & Auditing Company | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 29 business hours |
| FTI | 2 | Cancellation of Account Trustee & Auditing Company | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 29 business hours |
| FTI | 3 | Mortgage Registration | Compliance & Escrow Auditor | Transaction Audit Queue | 20–25 minutes |
| FTI | 4 | Mortgage Amendment | Compliance & Escrow Auditor | Transaction Audit Queue | 10–15 minutes |
| FTI | 5 | Mortgage Transfer | Compliance & Escrow Auditor | Transaction Audit Queue | 15–20 minutes |
| FTI | 6 | Mortgage Release | Compliance & Escrow Auditor | Transaction Audit Queue | 10–15 minutes |
| FTI | 7 | Grant Property Mortgage | Compliance & Escrow Auditor | Transaction Audit Queue | 15–20 minutes |
| FTI | 8 | Finance Lease Registration | Compliance & Escrow Auditor | Transaction Audit Queue | 30–35 minutes |
| FTI | 9 | Finance Lease Amendment | Compliance & Escrow Auditor | Transaction Audit Queue | 10–15 minutes |
| FTI | 10 | Finance Lease Transfer | Compliance & Escrow Auditor | Transaction Audit Queue | 10–15 minutes |
| FTI | 11 | Finance Lease Release | Compliance & Escrow Auditor | Transaction Audit Queue | 10–15 minutes |
| FTI | 12 | Registration of Real Estate Fund Companies in the Register of Privileges | Compliance & Escrow Auditor | Transaction Audit Queue | 25–30 minutes |
| FTI | 13 | Sale Procedure (Heirs) | Compliance & Escrow Auditor | Transaction Audit Queue | 25–30 minutes |
| FTI | 14 | Company Shares Sale | Compliance & Escrow Auditor | Transaction Audit Queue | 25–30 minutes |
| FTI | 15 | Updating Title Deed Information | Compliance & Escrow Auditor | Transaction Audit Queue | 25 minutes |
| FTI | 16 | Split Ownership | Compliance & Escrow Auditor | Transaction Audit Queue | 25 minutes |
| FTI | 17 | Issuance of Title Deed | Compliance & Escrow Auditor | Transaction Audit Queue | 25 minutes |
| FTI | 18 | Contract Cancellation | Compliance & Escrow Auditor | Transaction Audit Queue | 15 minutes |
| RESC | 1 | Register Company for JOP Administrative Supervision | Compliance & Escrow Auditor | Transaction Audit Queue | 5 minutes |
| RESC | 2 | Approve Service Fees & Utilization Fees | Compliance & Escrow Auditor | Transaction Audit Queue | 25 minutes |
| RESC | 3 | Register JOP-Competent Employees | Compliance & Escrow Auditor | Transaction Audit Queue | 5 minutes |
| RESC | 4 | Register Owners Association | Compliance & Escrow Auditor | Transaction Audit Queue | 25 minutes |
| RESC | 5 | Transfer JOP Escrow Account | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 1 business day |
| RESC | 6 | Request No-Objection Letter to Close Escrow Account [proposed] | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 3 business days |
| RESC | 7 | Accredit Escrow Account Signatories | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 1 business day |
| RESC | 8 | Appoint Financial Auditor | Compliance & Escrow Auditor | Transaction Audit Queue | 1 business day |
| RESC | 9 | Appoint Audit Office for JOP Financial Accounts | Compliance & Escrow Auditor | Transaction Audit Queue | 1 business day |
| RESC | 10 | Appoint Audit Office for JOP Budget Audit | Compliance & Escrow Auditor | Transaction Audit Queue | 1 business day |
| RESC | 11 | Approval / Renewal of Financial Auditing Company [proposed] | Compliance & Escrow Auditor | Escrow / Trust-Account Audit | 8 business days |
| RESC | 12 | Real Estate Licensing Application | Licensing & Registration Officer | Licensing & Registry | 5 minutes |
| RESC | 13 | Real Estate Permit Application | Licensing & Registration Officer | Licensing & Registry | 7 minutes |
| RESC | 14 | Issue Professional Practice Card | Licensing & Registration Officer | Licensing & Registry | 5 minutes |
| RESC | 15 | Renew Professional Practice Card [proposed] | Licensing & Registration Officer | Licensing & Registry | Automatic approval |
| RESC | 16 | Cancel Professional Practice Card | Licensing & Registration Officer | Licensing & Registry | 2 minutes |
| RESC | 17 | Amend Professional Practice Card [proposed] | Licensing & Registration Officer | Licensing & Registry | Automatic approval |
| RESC | 18 | Register Real Estate Evaluation Details Certificate [proposed] | None | — | Immediate |
| RESC | 19 | Accreditation of Training Entities (Real Estate Companies) | Licensing & Registration Officer | Licensing & Registry | 4 business days |
| RESC | 20 | Register/Renew Management Contract | Compliance & Escrow Auditor | Transaction Audit Queue | 1 hour 35 minutes |
| RESC | 21 | Cancel Management Contract [proposed] | None | — | Immediate |
| RESC | 22 | Register Tenancy System User [proposed] | None | — | Immediate |
| RESC | 23 | Permit to Sell by Public Auction [proposed] | Compliance & Escrow Auditor | Transaction Audit Queue | Within two business days |
| RESC | 24 | Register Property Sold by Auction | Compliance & Escrow Auditor | Transaction Audit Queue | 25–30 minutes |
| RESC | 25 | Primary Suit (Joint Property) | Dispute Adjudication Officer | Tribunal & Remote-Litigation | Registration completion: 10 minutes |
| RESC | 26 | Execution Case (Joint Ownership) | Dispute Adjudication Officer | Tribunal & Remote-Litigation | Registration completion: 10 minutes |
| IU | 1 | Verify Developer [proposed] | None | — | Immediate (real-time lookup) |
| IU | 2 | Verify Development Project [proposed] | None | — | Immediate (real-time lookup) |
| IU | 3 | Verify Property [proposed] | None | — | Immediate (real-time lookup) |
| IU | 4 | Register Property Ownership [proposed] | Compliance & Escrow Auditor | Transaction Audit Queue | Subject to RERAN service standards |
| IU | 5 | Transfer Property Ownership | Compliance & Escrow Auditor | Transaction Audit Queue | 25 minutes |
| IU | 6 | Register Property Sale [proposed] | Compliance & Escrow Auditor | Transaction Audit Queue | 25–35 minutes |
| IU | 7 | Update Property Ownership Information | Compliance & Escrow Auditor | Transaction Audit Queue | Owner/entity info amendment |
| IU | 8 | Register Sale of Mortgaged Property | Compliance & Escrow Auditor | Transaction Audit Queue | 15–20 minutes |
| IU | 9 | Register Gift Transfer | Compliance & Escrow Auditor | Transaction Audit Queue | 25–30 minutes |
| IU | 10 | Register Lease-to-Own | Compliance & Escrow Auditor | Transaction Audit Queue | ~25 minutes |
| IU | 11 | Transfer Lease-to-Own | Compliance & Escrow Auditor | Transaction Audit Queue | ~25 minutes |
| IU | 12 | Release Lease-to-Own | Compliance & Escrow Auditor | Transaction Audit Queue | ~25 minutes |
| IU | 13 | Amend Lease-to-Own | Compliance & Escrow Auditor | Transaction Audit Queue | ~25 minutes |
| IU | 14 | Register Usufruct Right | Compliance & Escrow Auditor | Transaction Audit Queue | Max 30 minutes |
| IU | 15 | Amend Usufruct Right | Compliance & Escrow Auditor | Transaction Audit Queue | 10–15 minutes |
| IU | 16 | Terminate Usufruct Right | Compliance & Escrow Auditor | Transaction Audit Queue | 10–15 minutes |
| IU | 17 | Grant Registration | Compliance & Escrow Auditor | Transaction Audit Queue | 25–30 minutes |
| IU | 18 | Grant Completion | Compliance & Escrow Auditor | Transaction Audit Queue | ~25 minutes |
| IU | 19 | Register Heirs Ownership | Compliance & Escrow Auditor | Transaction Audit Queue | 30–40 minutes |
| IU | 20 | Register Community Land | Compliance & Escrow Auditor | Transaction Audit Queue | 30–40 minutes |
| IU | 21 | Register Partners Division | Compliance & Escrow Auditor | Transaction Audit Queue | ~30 minutes |
| IU | 22 | Register Industrial & Commercial Land Ownership | Compliance & Escrow Auditor | Transaction Audit Queue | ~30 minutes |
| IU | 23 | Register Lease | Compliance & Escrow Auditor | Transaction Audit Queue | Via Real Estate Services Trustee |
| IU | 24 | Renew Lease | Compliance & Escrow Auditor | Transaction Audit Queue | Via Real Estate Services Trustee |
| IU | 25 | Manage Lease [proposed] | Compliance & Escrow Auditor | Transaction Audit Queue | Depends on request type |
| IU | 26 | Submit Tenancy Dispute | Dispute Adjudication Officer | Tribunal & Remote-Litigation | Dispute registration |
| IU | 27 | Cancel Tenancy Contract | Compliance & Escrow Auditor | Transaction Audit Queue | Via Real Estate Trustee Services |
| IU | 28 | Request Rental Valuation | Compliance & Escrow Auditor | Transaction Audit Queue | ~20–30 minutes |
| IU | 29 | Register Power of Attorney [proposed] | Compliance & Escrow Auditor | Transaction Audit Queue | Subject to RERAN service standards |
| IU | 30 | Act on Behalf of Property Owner [proposed] | None | — | Depends on selected service |
| IU | 31 | Request Detailed Real Estate Statement | Compliance & Escrow Auditor | Transaction Audit Queue | ~10–15 minutes |
| IU | 32 | Request To Whom It May Concern Certificate | Compliance & Escrow Auditor | Transaction Audit Queue | ~10–15 minutes |
| IU | 33 | Request Property Survey | Compliance & Escrow Auditor | Transaction Audit Queue | ~3–10 working days |
| IU | 34 | Request Property Valuation | Compliance & Escrow Auditor | Transaction Audit Queue | ~3–10 working days |
| IU | 35 | Request Full / Partial Indemnity | Compliance & Escrow Auditor | Transaction Audit Queue | ~10–20 minutes |
| IU | 36 | Remote Identity Verification [proposed] | Compliance & Escrow Auditor | Transaction Audit Queue | Subject to RERAN standards |
| IU | 37 | Remote Property Transactions [proposed] | None | — | Depends on selected transaction |
| IU | 38 | Submit Complaint [proposed] | Dispute Adjudication Officer | Tribunal & Remote-Litigation | Subject to RERAN standards |
| IU | 39 | Track Complaint [proposed] | None | — | Immediate (real-time lookup) |
| IU | 40 | Upload Building Details for Leasing | Compliance & Escrow Auditor | Transaction Audit Queue | One business day |
| IU | 41 | Register Company | Compliance & Escrow Auditor | Transaction Audit Queue | 25–30 minutes |
| IU | 42 | Cancel Power of Attorney | Compliance & Escrow Auditor | Transaction Audit Queue | 20 minutes |
| IU | 43 | Exchange Properties | Compliance & Escrow Auditor | Transaction Audit Queue | 25 minutes |

## Notes

- The escrow / trust-account classification was verified against each service's own
  source (not inferred from the title): it covers operations on a project escrow
  account **and** governance of the escrow apparatus — the approval and cancellation
  of Account Trustees and Auditing Companies (FTI #1, #2; RESC #11). See
  [open-questions.md](open-questions.md) for the one-queue-vs-two-queue decision.
- The full role definitions and responsibilities are in
  [roles-and-responsibilities.md](roles-and-responsibilities.md); this register is
  the by-service view of the same role assignments.
