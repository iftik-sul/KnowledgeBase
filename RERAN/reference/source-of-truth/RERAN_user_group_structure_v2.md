**RERA NIGERIA**

**Comprehensive User Group Structure,**  
**Roles, Features & Service Workflows**

**Contents**

[1  Architecture Overview	3](#1-architecture-overview)

[2  User Groups, Roles & Features	4](#2-user-groups,-roles-&-features)

[Group A — Regulatory Authority & Governance	4](#group-a-—-regulatory-authority-&-governance)

[Group B — Real Estate Developers	4](#group-b-—-real-estate-developers)

[Group C — Financial & Trust Institutions	5](#group-c-—-financial-&-trust-institutions)

[Group D — Real Estate Service Companies	5](#group-d-—-real-estate-service-companies)

[Group E — Property Owners & Landlords	6](#group-e-—-property-owners-&-landlords)

[Group F — Tenants & Consumers	6](#group-f-—-tenants-&-consumers)

[Group G — Allied Professionals & Service Trustees	6](#group-g-—-allied-professionals-&-service-trustees)

[Group H — Public & Informational Users	7](#group-h-—-public-&-informational-users)

[3  Detailed Service Workflows	8](#3-detailed-service-workflows)

[Workflow 1: Off-Plan (Initial Sale) Registration	8](#workflow-1:-off-plan-\(initial-sale\)-registration)

[Workflow 2: Mortgage Registration	8](#workflow-2:-mortgage-registration)

[Workflow 3: Tenant Dispute – Amicable Settlement	8](#workflow-3:-tenant-dispute-–-amicable-settlement)

[Workflow 4: Project Survey-Data Registration / Amendment	8](#workflow-4:-project-survey-data-registration-/-amendment)

[Workflow 5: Property Sale Registration (App / Trustee)	9](#workflow-5:-property-sale-registration-\(app-/-trustee\))

[4  Nigerian Design Principles	10](#4-nigerian-design-principles)

# **1  Architecture Overview** {#1-architecture-overview}

This blueprint structures the  platform users into eight integrated groups, each aligned to a distinct service domain drawn from regulated services. Every group resolves into specific operational roles, a defined set of platform sub-systems (features), and end-to-end workflows. The structure expands the group model so that each external actor domain \- developers, financiers, service companies, owners, tenants, allied professionals and the public has a dedicated, self-contained service surface, while the Regulatory Authority retains cross-cutting oversight.

| Grp | User Group | Service Mandate |
| :---- | :---- | :---- |
| **A** | **Regulatory Authority & Governance** | The agency's internal command tier. Holds final authority over policy, licensing approvals, enforcement, escrow oversight, dispute adjudication and the harmonisation demanded by the Land Use Act. |
| **B** | **Real Estate Developers** | Licensed development companies registering projects and off-plan sales, operating escrow accounts and filing construction progress etc. |
| **C** | **Financial & Trust Institutions** | Banks, mortgage institutions, account trustees and auditing bureaux that finance, secure and audit real-estate transactions. |
| **D** | **Real Estate Service Companies** | Brokerage, property-management and jointly-owned-property (estate/strata) management firms operating under licence. |
| **E** | **Property Owners & Landlords** | Individual and corporate property owners transacting title, registering leases and managing title-deed data. |
| **F** | **Tenants & Consumers** | Renters and the property-buying public the protected consumer base empowered to verify, transact and seek redress. |
| **G** | **Allied Professionals & Service Trustees** | Accredited surveyors, valuers, conveyancers and the Real-Estate Service / Registration Trustee centres that act as accredited intermediaries. |
| **H** | **Public & Informational Users** | Unauthenticated and lightly-authenticated users consuming verification, inquiry and awareness services. |

# **2  User Groups, Roles & Features** {#2-user-groups,-roles-&-features}

*Each group below lists its specific roles (with the real-world player and core function), the platform sub-systems it operates, and the source service categories it covers.*

## **Group A — Regulatory Authority & Governance** {#group-a-—-regulatory-authority-&-governance}

*The agency's internal command tier. Holds final authority over policy, licensing approvals, enforcement, escrow oversight, dispute adjudication and the federal–state harmonisation demanded by the Land Use Act.*

| Role | Player | Core Function |
| :---- | :---- | :---- |
| **Director-General / Registrar** | Executive head | Approves policy, signs statutory instruments, authorises licence revocations and final enforcement actions; chairs the governing board interface. |
| **System Super Administrator** | ICT Directorate | Provisions accounts, configures modules and role permissions, manages audit trails, data security and disaster recovery. |
| **Licensing & Registration Officer** | Licensing Directorate | Vets and approves developer, agent, surveyor and company licences; maintains the National Practitioner Register; issues e-licences and NOCs. |
| **Compliance & Escrow Auditor** | Compliance Directorate | Audits project escrow / trust accounts, vets off-plan sale registrations, monitors disclosure obligations, flags and sanctions defaulters. |
| **Inspection & Enforcement Officer** | Field Enforcement Unit | Conducts geo-tagged site inspections, verifies construction milestones, issues stop-work and violation notices, escalates penalties. |
| **Dispute Adjudication Officer** | Real Estate Tribunal Secretariat | Receives suits and complaints, schedules mediation/conciliation, manages remote-litigation sessions, records judgments and assignments. |
| **Revenue & Finance Officer** | Finance Directorate | Configures fee schedules and levies, reconciles gateway settlements, manages penalty collection and remittance to state/federal accounts. |
| **State Liaison Coordinator** | Inter-Governmental Affairs | Synchronises records with State Lands Bureaus and Surveyors-General, resolves jurisdictional conflicts, harmonises C-of-O data. |

**Platform sub-systems (features):** Admin & Configuration Console  ·  Licensing & Registry Engine  ·  Escrow / Trust-Account Audit System  ·  Inspection & Enforcement Module  ·  Tribunal & Remote-Litigation System  ·  Revenue & Settlement Dashboard

**Service coverage:** *Maps to all DEVELOPERS, FINANCIAL INSTITUTIONS oversight, dispute and licensing service categories.*

## **Group B — Real Estate Developers** {#group-b-—-real-estate-developers}

*Licensed development companies registering projects and off-plan sales, operating escrow accounts and filing construction progress the most heavily regulated external group.*

| Role | Player | Core Function |
| :---- | :---- | :---- |
| **Developer Principal / Director** | Authorised signatory | Holds the corporate account, authorises project registrations, escrow drawdowns and completion filings. |
| **Project Registration Officer** | Developer staff | Registers projects and unit inventories, uploads approved plans, submits initial off-plan and rent-to-own sale registrations. |
| **Sales & Disclosure Officer** | Developer staff | Registers initial sales, cancellations and amendments. |
| **Escrow Liaison** | Developer finance staff | Coordinates the trustee/auditor, files escrow statements and milestone-release requests. |

**Platform sub-systems (features):** Developers Portal  ·  Title-Deed & Project-Data Module  ·  Trust-Account (Escrow) System  

**Service coverage:** *Maps to: DEVELOPERS – Development Services (21), Licensing (2), Title-Deed Data Services (4).*

## **Group C — Financial & Trust Institutions** {#group-c-—-financial-&-trust-institutions}

*Banks, mortgage institutions, account trustees and auditing bureaux that finance, secure and audit real-estate transactions.*

| Role | Player | Core Function |
| :---- | :---- | :---- |
| **Mortgage Officer** | Bank lending desk | Registers, modifies and discharges mortgages; submits transactions for departmental audit. |
| **Account Trustee** | Approved escrow trustee | Manages project trust accounts, certifies milestone releases, files audited statements. |
| **Auditing Bureau Officer** | Approved auditor | Audits developer escrow accounts and submits independent compliance reports. |
| **Institution Relationship Manager** | Bank admin | Maintains institutional registration, renews trustee/auditor approvals, manages user provisioning. |

**Platform sub-systems (features):** Online Mortgage System  ·  Trust-Account Approval & Renewal  ·  Transaction Audit Queue

**Service coverage:** *Maps to: FINANCIAL INSTITUTIONS – Development (2), Transaction (15), Title-Deed Data (1).*

## **Group D — Real Estate Service Companies** {#group-d-—-real-estate-service-companies}

*Brokerage, property-management and jointly-owned-property (estate/strata) management firms operating under licence.*

| Role | Player | Core Function |
| :---- | :---- | :---- |
| **Brokerage Principal** | Licensed broker | Holds firm licence, registers agents, oversees listings and transaction logging. |
| **Owners'-Association Manager** | JOP / strata manager | Registers for administrative supervision of jointly owned properties, files service-charge budgets. |
| **Property Management Officer** | Management firm | Registers and renews management contracts, files occupancy and maintenance data. |
| **Company Dispute Filing Officer** | Firm legal staff | Files primary suits and dispute cases relating to managed/joint properties. |

**Platform sub-systems (features):** Owner / JOP System  ·  Tenancy Management System  ·  Brokerage Licensing & Listings  ·  Dispute Filing Portal

**Service coverage:** *Maps to: REAL ESTATE COMPANIES – JOP (11), Disputes (2), Licensing (8), Rental (3), Transaction (2).*

## **Group E — Property Owners & Landlords** {#group-e-—-property-owners-&-landlords}

*Individual and corporate property owners transacting title, registering leases and managing title-deed data.*

| Role | Player | Core Function |
| :---- | :---- | :---- |
| **Property Owner / Seller** | Individual or corporate | Registers sales, grants and transfers; uploads building data for leasing; manages title records. |
| **Landlord** | Lessor | Registers and renews leases, uploads building details, manages tenancy records. |
| **Owner's Representative / PoA Holder** | Appointed agent | Acts under power of attorney for diaspora or absent owners across transaction and title services. |

**Platform sub-systems (features):** Title-Deed & Transaction Module  ·  Tenancy System  ·  Owner Self-Service (App)

**Service coverage:** *Maps to: OWNER – Rental (1), Transaction (12), Title-Deed Data (15).*

## **Group F — Tenants & Consumers** {#group-f-—-tenants-&-consumers}

*Renters and the property-buying public — the protected consumer base empowered to verify, transact and seek redress.*

| Role | Player | Core Function |
| :---- | :---- | :---- |
| **Tenant** | Residential / commercial | Registers and renews leases, files rental disputes, requests amicable settlement. |
| **Property Buyer / Investor** | Domestic purchaser | Verifies developer and project legitimacy, tracks off-plan progress, lodges complaints. |
| **Diaspora Investor** | Nigerian abroad / foreign | Completes remote KYC, verifies remotely, transacts via representative, tracks in multiple currencies. |

**Platform sub-systems (features):** RERA Mobile App  ·  Tenancy System (Tenant)  ·  Dispute & Settlement Portal  ·  Public Verification

**Service coverage:** *Maps to: TENANT – Disputes (10), Rental (3); plus consumer-facing INFORMATIVE services.*

## **Group G — Allied Professionals & Service Trustees** {#group-g-—-allied-professionals-&-service-trustees}

*Accredited surveyors, valuers, conveyancers and the Real-Estate Service / Registration Trustee centres that act as accredited intermediaries.*

| Role | Player | Core Function |
| :---- | :---- | :---- |
| **Survey Company** | ESVARBON-accredited | Prepares and matches project survey data to approved plans, submits to the Survey Department. |
| **Valuer** | Registered valuer | Submits valuations and professional reports for transactions, financing and disputes. |
| **Conveyancer / Legal Practitioner** | Property lawyer | Conducts title verification, lodges documentation, supports due diligence. |
| **Registration / Service Trustee Centre** | Accredited centre | Processes walk-in transactions, registrations and dispute filings on behalf of customers. |

**Platform sub-systems (features):** Survey Submission Module  ·  Trustee-Centre Transaction Terminal  ·  Valuation & Legal Filing

**Service coverage:** *Supports OWNER & FINANCIAL transaction service channels (Trustee Centres, Survey Department).*

## **Group H — Public & Informational Users** {#group-h-—-public-&-informational-users}

*Unauthenticated and lightly-authenticated users consuming verification, inquiry and awareness services.*

| Role | Player | Core Function |
| :---- | :---- | :---- |
| **General Public** | Unregistered | Inquires about property status, verifies licences, browses the public register and awareness content. |
| **Institutional Verifier** | Bank / govt / researcher | Performs bulk or API verification of titles, projects and practitioner standing. |

**Platform sub-systems (features):** Public Register & Verification  ·  Inquiry Services (App / Web / WhatsApp / Call Centre)

**Service coverage:** *Maps to: INFORMATIVE – General (33).*

# **3  Detailed Service Workflows** {#3-detailed-service-workflows}

*Representative end-to-end workflows for the highest-volume service in each major domain. Each follows the lodge → validate → audit → pay → issue pattern that standardises the platform.*

## **Workflow 1: Off-Plan (Initial Sale) Registration** {#workflow-1:-off-plan-(initial-sale)-registration}

**Group:** B — Developers      **Actors:** Developer → Compliance & Escrow Auditor → Purchaser

1. Developer logs in to the Developers Portal and selects ‘Provisional / Initial Sale Registration’.

2. Selects the registered project and unit, fills sale particulars and attaches the signed sale-and-purchase contract and party IDs.

3. System validates that the contract is lodged within the statutory 90-day window and that a valid escrow account exists.

4. Developer selects payment method; seller and purchaser fees plus VAT are computed automatically.

5. Compliance & Escrow Auditor reviews the filing, confirms escrow linkage and approves or returns it.

6. On approval, a provisional registration e-certificate is generated and e-mailed to the purchaser; the unit status updates in the register.

**Output:** Provisional registration e-certificate      **Service time:** 1 business day

## **Workflow 2: Mortgage Registration** {#workflow-2:-mortgage-registration}

**Group:** C — Financial Institutions      **Actors:** Bank Mortgage Officer → Bank Auditor → RERA Transaction Audit

1. Customer assembles mortgage requirements with the bank.

2. Mortgage Officer enters all documents via the Online Mortgage System.

3. The bank's internal auditor reviews and certifies the transaction.

4. Transaction is routed to the RERA Transaction Audit queue for departmental verification.

5. On approval, fees are settled through the payment gateway and an e-receipt issues.

6. Mortgage is registered against the title; confirmation is delivered to the bank and owner.

**Output:** Mortgage registration certificate      **Service time:** Same / next business day

## **Workflow 3: Tenant Dispute – Amicable Settlement** {#workflow-3:-tenant-dispute-–-amicable-settlement}

**Group:** A/F — Disputes      **Actors:** Tenant → Dispute Adjudication Officer → Both Parties

1. Tenant signs in to the Dispute & Settlement Portal (or attends a Service Trustee Centre) and selects ‘Amicable Settlement’.

2. Uploads tenancy contract, evidence and respondent details; system audits completeness.

3. Fees are paid; a conciliation session is scheduled.

4. Parties attend via the Remote-Litigation System; the Adjudication Officer mediates.

5. On agreement, a settlement / assignment document is signed electronically.

6. Executed agreement is issued to both parties and recorded in the case register.

**Output:** Signed settlement / assignment      **Service time:** Per session schedule

## **Workflow 4: Project Survey-Data Registration / Amendment** {#workflow-4:-project-survey-data-registration-/-amendment}

**Group:** B/G — Title Deed      **Actors:** Developer → Survey Company → Survey Department

1. Developer designates an accredited Survey Company in the Title-Deed module.

2. Survey Company prepares project data and matches it to the approved plans.

3. Approval fees are paid and the package is submitted to the Survey Department.

4. Survey Department reviews, verifies coordinates and approves or returns for correction.

5. Approved project data is committed to the title-deed register.

6. Developer is notified and the project record is updated platform-wide.

**Output:** Updated project title-deed record      **Service time:** Multi-day (review-dependent)

## **Workflow 5: Property Sale Registration (App / Trustee)** {#workflow-5:-property-sale-registration-(app-/-trustee)}

**Group:** E — Owners      **Actors:** Seller → Registration Trustee / App → Buyer

1. Seller opens the RERA App (or visits a Registration Trustee Centre) and selects the property.

2. Prepares the transaction, selects the buyer and enters sale particulars.

3. Documents are attached; the trustee/system audits the submission.

4. Both parties confirm; transfer fees are paid via the gateway.

5. Title transfer is executed and the register updated.

6. Sale outputs (e-title / receipt) are delivered to both parties by e-mail and in-app.

**Output:** New title deed / transfer certificate      **Service time:** Same-day (digital channel)

# **4  Nigerian Design Principles** {#4-nigerian-design-principles}

* **Federal–state harmonisation —** A dedicated State Liaison role and data-sync layer reconcile the national register with State Lands Bureaus, since land vests in State Governors under the Land Use Act.

* **C-of-O as core instrument —** Certificate of Occupancy verification and grant registration replace Dubai's Title-Deed primitive throughout the title-data services.

* **Escrow-first developer control —** Off-plan registration is hard-gated on a verified trust account, with independent trustee and auditor roles, to curb abandoned-project fraud.

* **Diaspora enablement —** Remote KYC, power-of-attorney representation and multi-currency tracking are first-class features, reflecting diaspora capital inflows.

* **Multi-channel access —** Every consumer service is reachable via App, web, Trustee Centre, WhatsApp and Call Centre, matching low-bandwidth and walk-in realities.

* **Anti-fraud verification —** Public, instant verification of licences, projects and titles directly counters ‘Omonile’ and fake-developer schemes.