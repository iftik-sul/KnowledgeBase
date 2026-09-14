---
project: RERAN
module: regulatory-authority
type: reference
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/modules/*/service-flows/"
---

# Group A — Role Directory

This directory answers three questions for each of Group A's eight roles: **what
it is** (a plain description), **what it is responsible for** (its duties), and
**which services it finishes, from which group** (the exact approval mapping).

## How to read this

- Group A finishes work; it never initiates it. "Finishes a service" means Group A
  is the authority that makes the final approve / reject / return decision on an
  application another group filed.
- Only **three of the eight roles finish any current service**. The other five run
  the agency (platform operations, finance, governance, inspection, inter-state
  liaison) but no service in the current catalogue of 114 routes to them for a
  decision. All eight are described here so the picture is complete.
- Service counts: Compliance & Escrow Auditor 92 · Licensing & Registration
  Officer 9 · Dispute Adjudication Officer 4 · no Group A decision 9. Total 114.
- `[proposed]` marks a service whose source did not name a Group A role explicitly;
  the assignment is a reasoned proposal awaiting client confirmation.

---

# Roles that finish services

## 1. Compliance & Escrow Auditor

**Description.** The workhorse of Group A. This is the regulatory officer who reviews
and approves the vast majority of everything filed on the platform — property
registrations, sales, leases, mortgages, financial-institution filings, and every
escrow-account action. Where the platform touches project money or a regulated
property transaction, this role is the gate it passes through. One role carries 81%
of all decisions on the platform.

**Responsibilities.**
- Receive submitted, paid applications into the Transaction Audit Queue.
- Review and audit each application and its documents; verify against the registry
  (developer registered, project valid, unit available, title clean, applicant
  authorised).
- Decide: approve, request additional information, return for correction, or reject.
- Audit project escrow and trust accounts; vet off-plan sale registrations; monitor
  developer disclosure obligations; flag and sanction defaulters.
- On approval, trigger the output (certificate, title deed, map, registry update).
- Record every action to the audit trail.

**Sub-system:** Escrow / Trust-Account Audit System + the general Transaction Audit Queue.

**Services finished (92):**

*From Real Estate Developer (25):*
- #1 Register Initial Sale
- #2 Register Initial Rent-to-Own
- #3 Register Initial Usufruct
- #4 Amend Initial Procedures Data
- #5 Complete Initial Procedures Data
- #6 Register Sale Associated with an Initial Mortgage
- #7 Transfer Registration Fees Between Properties
- #8 Escrow Account Activation *(escrow)*
- #9 Escrow Account Transfer *(escrow)*
- #10 Project Profit Withdrawal *(escrow)*
- #11 Amend the Cap of Admin/Marketing/VAT Expenses *(escrow)*
- #12 Receive a Payment from the Project's Escrow Account *(escrow)*
- #13 Registration of Real Estate Project
- #14 Real Estate Project Cancellation
- #15 Real Estate Project Sub-division
- #16 Changing the Name of a Project
- #17 Project Re-registration
- #18 Settlements Application
- #19 Request Termination of Initial Registration
- #20 Depositing a Mortgage into an Escrow Account *(escrow)*
- #21 Bank Guarantee Cancellation *(escrow)*
- #24 Registration/Amendment of Project Details
- #25 Issuing Map Application
- #26 Separation or Annexing a Property
- #27 Requesting a Technical Report

*From Financial & Trust Institutions (all 18):*
- #1 Approval/Renewal of Account Trustee & Auditing Company *(escrow)*
- #2 Cancellation of Account Trustee & Auditing Company *(escrow)*
- #3 Mortgage Registration
- #4 Mortgage Amendment
- #5 Mortgage Transfer
- #6 Mortgage Release
- #7 Grant Property Mortgage
- #8 Finance Lease Registration
- #9 Finance Lease Amendment
- #10 Finance Lease Transfer
- #11 Finance Lease Release
- #12 Registration of Real Estate Fund Companies
- #13 Sale Procedure (Heirs)
- #14 Company Shares Sale
- #15 Updating Title Deed Information
- #16 Split Ownership
- #17 Issuance of Title Deed
- #18 Contract Cancellation

*From Real Estate Service Companies (14):*
- #1 Register Company for JOP Administrative Supervision
- #2 Approve Service Fees & Utilization Fees
- #3 Register JOP-Competent Employees
- #4 Register Owners Association
- #5 Transfer JOP Escrow Account *(escrow)*
- #6 Request No-Objection Letter to Close Escrow Account *(escrow, proposed)*
- #7 Accredit Escrow Account Signatories *(escrow)*
- #8 Appoint Financial Auditor
- #9 Appoint Audit Office for JOP Financial Accounts
- #10 Appoint Audit Office for JOP Budget Audit
- #11 Approval/Renewal of Financial Auditing Company *(escrow, proposed)*
- #20 Register/Renew Management Contract
- #23 Permit to Sell by Public Auction *(proposed)*
- #24 Register Property Sold by Auction

*From Individual User (35):*
- #4 Register Property Ownership *(proposed)*
- #5 Transfer Property Ownership
- #6 Register Property Sale *(proposed)*
- #7 Update Property Ownership Information
- #8 Register Sale of Mortgaged Property
- #9 Register Gift Transfer
- #10 Register Lease-to-Own
- #11 Transfer Lease-to-Own
- #12 Release Lease-to-Own
- #13 Amend Lease-to-Own
- #14 Register Usufruct Right
- #15 Amend Usufruct Right
- #16 Terminate Usufruct Right
- #17 Grant Registration
- #18 Grant Completion
- #19 Register Heirs Ownership
- #20 Register Community Land
- #21 Register Partners Division
- #22 Register Industrial & Commercial Land Ownership
- #23 Register Lease
- #24 Renew Lease
- #25 Manage Lease *(proposed)*
- #27 Cancel Tenancy Contract
- #28 Request Rental Valuation
- #29 Register Power of Attorney *(proposed)*
- #31 Request Detailed Real Estate Statement
- #32 Request To Whom It May Concern Certificate
- #33 Request Property Survey
- #34 Request Property Valuation
- #35 Request Full/Partial Indemnity
- #36 Remote Identity Verification *(proposed)*
- #40 Upload Building Details for Leasing
- #41 Register Company
- #42 Cancel Power of Attorney
- #43 Exchange Properties

---

## 2. Licensing & Registration Officer

**Description.** The gatekeeper for who is allowed to operate in the sector. This
role vets and approves the licences, permits, professional practice cards, and
training accreditations that developers and service companies need before they can
trade. It maintains the national register of licensed practitioners.

**Responsibilities.**
- Vet and approve developer, agent, surveyor, and company licences and permits.
- Issue, renew, amend, and cancel professional practice cards.
- Accredit training entities.
- Maintain the National Practitioner Register; issue e-licences and no-objection
  certificates.
- Same decision loop as the auditor (approve / request info / return / reject).

**Sub-system:** Licensing & Registry Engine.

**Services finished (9):**

*From Real Estate Developer (2):*
- #22 Real Estate Licensing Application
- #23 Accreditation of Training Entities

*From Real Estate Service Companies (7):*
- #12 Real Estate Licensing Application
- #13 Real Estate Permit Application
- #14 Issue Professional Practice Card
- #15 Renew Professional Practice Card *(proposed)*
- #16 Cancel Professional Practice Card
- #17 Amend Professional Practice Card *(proposed)*
- #19 Accreditation of Training Entities

---

## 3. Dispute Adjudication Officer

**Description.** The tribunal side of Group A. Where the other two roles approve
applications, this role handles conflict — suits, complaints, and disputes between
parties. Its work is not a single approve/reject decision but a multi-step process
of mediation, hearing, and judgment.

**Responsibilities.**
- Receive suits and complaints.
- Schedule and run mediation / conciliation and remote-litigation sessions.
- Record judgments and assignments.
- Manage the case lifecycle from filing to resolution (this is a longer, multi-
  session flow, not the standard decision loop).

**Sub-system:** Tribunal & Remote-Litigation System.

**Services finished (4):**

*From Real Estate Service Companies (2):*
- #25 Primary Suit (Joint Property)
- #26 Execution Case (Joint Ownership)

*From Individual User (2):*
- #26 Submit Tenancy Dispute
- #38 Submit Complaint *(proposed)*

---

# Platform & configuration roles (active, finish no service)

## 4. System Super Administrator

**Description.** The role that runs the platform itself rather than any regulatory
decision. It is the technical administrator of Group A — the only place in RERAN
where real permission control exists. Everyone else's access is attribution-only;
this role configures who can do what within Group A.

**Responsibilities.**
- Provision staff accounts and assign roles.
- Configure modules and role permissions (this role operates the RBAC system).
- Manage the audit trail, data security, and disaster recovery.

**Sub-system:** Admin & Configuration Console.

---

## 5. Revenue & Finance Officer

**Description.** The money-configuration role. Every fee-bearing service on the
platform reads a fee schedule; this role owns that schedule. It also reconciles what
the payment gateway collects against what was owed and manages remittance to
government accounts.

**Responsibilities.**
- Configure fee schedules and levies.
- Reconcile gateway settlements.
- Manage penalty collection and remittance to state/federal accounts.

**Sub-system:** Revenue & Settlement Dashboard.

---

# Oversight & latent roles (real functions, finish no current service)

## 6. Director-General / Registrar

**Description.** The executive head of the authority. This is a governance and
sign-off tier, not a day-to-day processing role — it acts on the exceptional and the
final, not the routine.

**Responsibilities.**
- Approve policy and sign statutory instruments.
- Authorise licence revocations and final enforcement actions.
- Chair the governing-board interface.

**Sub-system:** spans Admin & Configuration and the enforcement/governance layer.

---

## 7. Inspection & Enforcement Officer

**Description.** The physical-world verification and enforcement role. Where the
other roles work on documents, this one works on the ground — confirming that what
was filed matches reality, and acting when it doesn't.

**Responsibilities.**
- Conduct geo-tagged site inspections and verify construction milestones.
- Issue stop-work and violation notices; escalate penalties.
- Perform technical/boundary verification of survey submissions *(proposed home for
  the "Survey Department" work currently mislabelled in some developer service-
  flows).*

**Sub-system:** Inspection & Enforcement Module.

---

## 8. State Liaison Coordinator

**Description.** The federalism role. Nigeria's land system is split across federal
and state authorities; this role keeps the platform's records synchronised with the
state land bureaus and resolves conflicts between jurisdictions. This is also the
role any AGIS-type integration would sit under.

**Responsibilities.**
- Synchronise records with State Lands Bureaus and Surveyors-General.
- Resolve jurisdictional conflicts; harmonise Certificate-of-Occupancy data.
- Coordinate external Surveyor-General verification *(proposed home for the external
  survey-confirmation step seen in AGIS).*

**Sub-system:** cross-cutting (data harmonisation layer).

---

# Services with no Group A decision (9)

These are filed by other groups but need no Group A approval — they are automated
system actions (real-time registry lookups) or wrappers that inherit another
service's decision. No role, no queue.

*Real Estate Service Companies (3):*
- #18 Register Real Estate Evaluation Details Certificate *(auto)*
- #21 Cancel Management Contract *(auto)*
- #22 Register Tenancy System User *(auto)*

*Individual User (6):*
- #1 Verify Developer *(lookup)*
- #2 Verify Development Project *(lookup)*
- #3 Verify Property *(lookup)*
- #30 Act on Behalf of Property Owner *(wrapper)*
- #37 Remote Property Transactions *(wrapper)*
- #39 Track Complaint *(lookup)*

---

# Summary table

| Role | Finishes | Sub-system |
| :--- | :--- | :--- |
| Compliance & Escrow Auditor | 92 services | Escrow/Trust Audit + Transaction Audit Queue |
| Licensing & Registration Officer | 9 services | Licensing & Registry Engine |
| Dispute Adjudication Officer | 4 services | Tribunal & Remote-Litigation |
| System Super Administrator | 0 (runs RBAC) | Admin & Configuration Console |
| Revenue & Finance Officer | 0 (fee engine) | Revenue & Settlement Dashboard |
| Director-General / Registrar | 0 (sign-off) | Governance |
| Inspection & Enforcement Officer | 0 (sub-steps) | Inspection & Enforcement Module |
| State Liaison Coordinator | 0 (data sync) | Harmonisation layer |
