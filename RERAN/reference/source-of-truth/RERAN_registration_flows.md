**RERA NIGERIA**  
Real Estate Regulatory Agency

**Registration (Sign-Up) Flows**  
**& Acceptance Criteria by Role**

Onboarding specification for all roles across the eight user groups

*Nine registration archetypes · 28 roles · NIMC / BVN / CAC / ESVARBON verification*

**Contents**

[1  Overview	3](#1-overview)

[2  Registration Flows by Role	4](#2-registration-flows-by-role)

[Flow 1 — Individual Consumer	4](#flow-1-—-individual-consumer)

[Flow 2 — Diaspora Investor	4](#flow-2-—-diaspora-investor)

[Flow 3 — Licensed Agent / Broker (Individual)	5](#flow-3-—-licensed-agent-/-broker-\(individual\))

[Flow 4 — Company / Corporate Entity	5](#flow-4-—-company-/-corporate-entity)

[Flow 5 — Delegated Company Staff	6](#flow-5-—-delegated-company-staff)

[Flow 6 — Allied Professional (Individual)	7](#flow-6-—-allied-professional-\(individual\))

[Flow 7 — Accredited Service / Registration Trustee Centre	7](#flow-7-—-accredited-service-/-registration-trustee-centre)

[Flow 8 — Regulator / Admin & Staff Accounts	8](#flow-8-—-regulator-/-admin-&-staff-accounts)

[Flow 9 — Public & Institutional Verifier	8](#flow-9-—-public-&-institutional-verifier)

[3  Role-to-Flow Mapping	10](#3.-role-to-flow-mapping)

[4  Profile Management (Post-Registration)	11](#4.-profile-management-\(post-registration\))

# **1  Overview** {#1-overview}

All users begin by creating an account via the web portal or the RERA mobile app, because the platform serves twenty-eight distinct roles across eight user groups, the sign-up experience is organized into nine registration archetypes, each a self-contained flow with its own steps and acceptance criteria. A role inherits the archetype that matches how it onboards: a natural person, a diaspora user, a licensed individual, a company, delegated company staff, an allied professional, an accredited centre, an internal regulator, or a public/institutional verifier.

All flows are on a shared set of Nigerian identity and accreditation primitives, summarised below.

| Primitive | Role in onboarding |
| :---- | :---- |
| **NIN / NIMC (NVS API)** | Primary individual identity verification for all natural persons. |
| **BVN** | Alternative or supplementary identity/financial verification. |
| **International Passport** | Identity route for diaspora and foreign users, with liveness/selfie match. |
| **CAC via NIBSS-CAC API** | Company verification and auto-population of director/address data. |
| **ESVARBON** | Accreditation check for surveyors and valuers. |
| **RERA Practitioner Register** | License validation for agents, brokers, and firms. |
| **2FA (SMS / Authenticator)** | Mandatory second factor for all account types. |
| **Enterprise SSO** | Authentication path for internal regulator/staff accounts. |
| **NDPA 2023 consent** | Data-protection consent captured at sign-up and API onboarding. |

# **2  Registration Flows by Role** {#2-registration-flows-by-role}

## **Flow 1 — Individual Consumer** {#flow-1-—-individual-consumer}

**Groups E, F**    

**Applies to:** 

- Property Owner / Seller (individual)

- Landlord (individual) 

- Tenant 

- Property Buyer / Investor

- Owner's Representative / PoA Holder

The baseline self-service flow for natural persons transacting on their own behalf. Completed entirely via the web or the RERA mobile app.

1. **Role Selection:** The user selects an initial intent (own/buy/rent), which provisions the matching consumer role and dashboard.

2. **Provide Personal Info:** full name, date of birth, residential address, email, and mobile number.

3. **Identity Verification:** Enter National Identity Number (NIN); the system calls the NIMC Verification Service (NVS) API to confirm identity, with a BVN check as an alternative or supplementary lookup.

4. **Set Credentials:** Choose a username and password; enable 2FA via SMS or authenticator app.

5. **Profile Setup (KYC):** upload a government ID (NIN slip/card) and a passport photograph; optionally add a utility bill for address proof.

6. **Email / SMS Confirmation:** The system sends a verification code to email and phone; the user confirms to activate the account.

| Acceptance Criteria Sign-up cannot be completed without a valid NIN (or international passport for diaspora). Identity must be verified via NIMC/NVS or BVN lookup before activation. Email and mobile number must each be unique in the system. On success, the account is created with the relevant consumer role and a unique user ID, which will be a phone number. |
| :---- |

## **Flow 2 — Diaspora Investor** {#flow-2-—-diaspora-investor}

**Group F (and E via representation)**    

**Applies to:** 

- Diaspora Investor

- Owner's Representative / PoA Holder (foreign-based)

A variant of the individual flow for Nigerians and foreign nationals based abroad, accommodating international identity documents and remote KYC.

1. **Provide Personal Info:** full name, date of birth, foreign address, email, and an international mobile number (non-Nigerian numbers accepted).

2. **Identity Verification:** Provide NIN where held; otherwise, authenticate via international passport. Passport data is checked, and a liveness/selfie match is performed for remote KYC.

3. **Set Credentials:** choose a username and password; 2FA via an authenticator app (preferred where SMS is unreliable internationally).

4. **Profile Setup (KYC):** upload passport bio-data page and passport photograph; optionally upload proof of foreign residence. \- **This won’t be necessary anymore because the passport number has been collected. The automated system would get to this as well.**

5. **Representative Linkage (optional):** Nominate a local owner's representative / PoA holder and upload the notarized power of attorney.

6. **Email / SMS Confirmation:** Confirm via emailed code; activate the account with multi-currency tracking enabled.

| Acceptance Criteria A valid NIN or international passport is mandatory; the passport route requires a successful liveness/selfie match. Where a representative is nominated, a valid, notarized PoA must be attached before transactional rights are granted. Email and mobile (international format permitted) must be unique. On success, the account is created with the Diaspora Investor role and multi-currency features enabled. |
| :---- |

## **Flow 3 — Licensed Agent / Broker (Individual)** {#flow-3-—-licensed-agent-/-broker-(individual)}

**Group D**    

**Applies to:** 

- Individual licensed brokers signing up under their own RERA practitioner license

For individual real estate practitioners. Builds on the individual flow and adds professional license verification.

1. **Personal Info:** As in the Individual flow (name, DOB, address, email, and mobile).

2. **Professional Credentials:** Enter the RERA practitioner license (or provisional certificate) number and upload the license document; if expired, the renewal flow is offered inline.

3. **Identity Verification:** Verify identity via NIMC/NVS (NIN) or BVN.

4. **Set Credentials:** Choose login details, enable 2FA, and confirm contact details.

5. **Email / SMS Confirmation:** Confirm the verification code to activate.

| Acceptance Criteria The applicant must hold a valid RERA license or provisional certificate; the license number is checked against the Practitioner Register. Identity must be verified via NIMC or BVN. On success, the agent role is assigned, and license validity (and expiry) is recorded on the profile. |
| :---- |

## **Flow 4 — Company / Corporate Entity** {#flow-4-—-company-/-corporate-entity}

**Groups B, C, D, G**    

**Applies to:** 

- Developer Principal / Director 

- Brokerage Principal (firm) 

- Owners' Association Manager 

- Property Management Officer 

- Survey Company 

- Institution Relationship Manager (onboarding the firm)

The corporate onboarding flow for any registered company. A verified company entity is created first; staff roles are then provisioned beneath it (Flow 5).

1. **Company Details:** enter the company name and CAC registration (RC) number; upload the Certificate of Incorporation. The system uses the NIBSS-CAC API to verify the RC number and auto-populate official company data (registered address, directors).

2. **Authorized User Info:** enter the company representative's details (name, NIN, email, and mobile) and verify their identity via the NIMC API.

3. **Sector Credentials:** Attach the sector-specific accreditation, e.g., ESVARBON registration (Survey Company), banking/CBN license (Financial Institution), or RERA firm license (Brokerage/Management) where applicable.

4. **Credentials & Documents:** Set login details; upload a company letterhead and a board resolution authorizing portal use.

5. **Email / SMS Confirmation:** Complete the verification flow for the representative.

| Acceptance Criteria The CAC (RC) number must be valid and active; company data is auto-populated via the CAC lookup. The representative's identity must be verified and must match the directors/authorized signatories on the CAC record. Required sector accreditation, where the role demands it, must be attached and valid. On creation, the account receives its corporate role and is set to pending admin approval where policy requires it (e.g., developer, financial institution). |
| :---- |

## **Flow 5 — Delegated Company Staff** {#flow-5-—-delegated-company-staff}

**Groups B, C, D**    

**Applies to:** 

- Project Registration Officer 

- Sales & Disclosure Officer 

- Escrow Liaison 

- Mortgage Officer 

- Account Trustee

-  Auditing Bureau Officer 

- Company Dispute Filing Officer

Operational staff do not self-register independently; they are invited and provisioned by their company's authorised representative under the verified corporate account (Flow 4).

1. **Invitation:** The company representative invites the staff member by email from the corporate dashboard and pre-assigns the intended role.

2. **Identity Verification:** The invitee verifies their own identity via NIMC/NVS (NIN) or BVN on first sign-in.

3. **Set Credentials:** The invitee sets a password and enables 2FA.

4. **Scope Confirmation:** The representative confirms the staff member's permission scope (e.g., escrow filing only); the account inherits the company's verified standing.

5. **Activation:** on confirmation, the delegated role is activated under the parent company entity.

| Acceptance Criteria Staff accounts can only be created under an already-verified corporate entity. The invitee's identity must be independently verified via NIMC or BVN. Permission scope must be explicitly set by the authorised representative before activation. On success, the delegated role is bound to the parent company and appears in its user roster. |
| :---- |

## **Flow 6 — Allied Professional (Individual)** {#flow-6-—-allied-professional-(individual)}

**Group G**    

**Applies to:** 

- Valuer 

- Conveyancer / Legal Practitioner

For accredited individual professionals who file specialist outputs (valuations, legal documentation). Combines the individual flow with professional-body verification*.*

1. **Personal Info:** as in the Individual flow.

2. **Professional Body Verification:** Enter the registration number for the relevant body, ESVARBON (valuers),, or the Nigerian Bar Association/Supreme Court enrollment (legal practitioners), and upload the practicing certificate.

3. **Identity Verification:** Verify via NIMC/NVS or BVN.

4. **Set Credentials:** set login details; enable 2FA.

5. **Email / SMS Confirmation:** Confirm to activate.

| Acceptance Criteria A valid, current professional registration (ESVARBON or legal enrollment) must be supplied and is checked against the issuing body's records where an API is available. Identity must be verified via NIMC or BVN. On success, the professional role is assigned, and the credential type and expiry are recorded. |
| :---- |

## **Flow 7 — Accredited Service / Registration Trustee Centre** {#flow-7-—-accredited-service-/-registration-trustee-centre}

**Group G**    

**Applies to:** 

- Registration / Service Trustee Centre

Accredited centers that transact on behalf of walk-in customers. Onboarded as a supervised corporate entity with elevated, audited operator accounts.

1. **Center Registration:** complete the company flow (Flow 4\) with the CAC entity and upload the RERA accreditation/appointment letter for the center.

2. **Premises & Coverage:** Register the physical center address(es) and service coverage area for state-level routing.

3. **Operator Provisioning:** Provision individual operator accounts (each NIMC-verified) under the center, with per-operator transaction scopes.

4. **Security Onboarding:** Enforce 2FA for all operators and register the center's static IP / device whitelist for audit.

5. **Activation: The** RERA Licensing & Registration Officer reviews and approves the center before it can transact.

| Acceptance Criteria The center must hold a valid RERA accreditation/appointment letter in addition to an active CAC entity. Every operator account must be individually NIMC/BVN-verified and 2FA-enabled. The center is inactive until approved by a RERA Licensing & Registration Officer. On approval, the center receives trustee-operator privileges with full transaction audit logging. |
| :---- |

## **Flow 8 — Regulator / Admin & Staff Accounts** {#flow-8-—-regulator-/-admin-&-staff-accounts}

**Group A**    

**Applies to:** 

- Director-General / Registrar 

- System Super Administrator

- Licensing & Registration Officer 

- Compliance & Escrow Auditor

- Inspection & Enforcement Officer

- Dispute Adjudication Officer

- Revenue & Finance Officer

- Liaison Coordinator

Regulator and staff accounts are never self-registered through the public portal. They are created internally by an IT administrator or via HR directory import and authenticated through enterprise SSO.

1. **Internal Provisioning:** The system super administrator (or an HR directory import) creates the account; public self-registration is not permitted.

2. **Identity & Role Assignment:** The staff member's identity is confirmed against HR records, and a specific role is assigned at creation (e.g., registrar, auditor, IT admin).

3. **Authentication Setup:** The account is bound to enterprise SSO with mandatory 2FA.

4. **Permission Scoping:** Module and directorate permissions are applied per the role–feature matrix.

5. **Activation & Audit:** The account is activated and entered into the privileged-access audit log.

| Acceptance Criteria Admin/staff accounts must be created internally; self-registration through the public portal is blocked. Each account is bound to enterprise SSO with enforced 2FA. A role and permission scope must be assigned at creation; no account is activated without one. All privileged accounts are recorded in the audit log upon activation. |
| :---- |

## **Flow 9 — Public & Institutional Verifier** {#flow-9-—-public-&-institutional-verifier}

**Group H**    

**Applies to:** 

- General Public (unregistered) 

- Institutional Verifier

*Lightweight access for verification and inquiry. Most public services need no account; institutional verifiers register for higher-volume or API access.*

1. **General Public:** no account required for public-register lookups, license checks, and awareness content; an optional light account (email \+ phone OTP) saves searches and complaint references.

2. **Institutional Verifier—Entity Details:** complete the company flow (Flow 4\) and indicate the verification use case (lender due diligence, government, or research).

3. **Access Tier Request:** request API credentials or a bulk-verification quota; accept the data-use and privacy terms (NDPA 2023).

4. **Credentials & Keys:** set login details and enable 2FA; the system issues scoped, rate-limited API keys.

5. **Activation:** standard public access is immediate; API/bulk access is activated after a compliance check.

| Acceptance Criteria Public read-only verification requires no registration; any optional account uses email \+ phone OTP only. Institutional verifiers must complete CAC-verified company onboarding and accept NDPA 2023 data-use terms. API keys are scoped, rate-limited, and revocable; bulk access requires a passed compliance check. On success, the verifier role is assigned an access tier, and a usage quota is recorded. |
| :---- |

# **3\. Role-to-Flow Mapping** {#3.-role-to-flow-mapping}

*Quick reference mapping every role in the user-group structure to its registration archetype.*

| Grp | Role | Registration Flow |
| ----- | :---- | :---- |
| **A** | Director-General / Registrar | Flow 8 — Regulator / Admin |
| **A** | System Super Administrator | Flow 8 — Regulator / Admin |
| **A** | Licensing & Registration Officer | Flow 8 — Regulator / Admin |
| **A** | Compliance & Escrow Auditor | Flow 8 — Regulator / Admin |
| **A** | Inspection & Enforcement Officer | Flow 8 — Regulator / Admin |
| **A** | Dispute Adjudication Officer | Flow 8 — Regulator / Admin |
| **A** | Revenue & Finance Officer | Flow 8 — Regulator / Admin |
| **A** | State Liaison Coordinator | Flow 8 — Regulator / Admin |
| **B** | Developer Principal / Director | Flow 4 — Company |
| **B** | Project Registration Officer | Flow 5 — Delegated Staff |
| **B** | Sales & Disclosure Officer | Flow 5 — Delegated Staff |
| **B** | Escrow Liaison | Flow 5 — Delegated Staff |
| **C** | Mortgage Officer | Flow 5 — Delegated Staff |
| **C** | Account Trustee | Flow 5 — Delegated Staff |
| **C** | Auditing Bureau Officer | Flow 5 — Delegated Staff |
| **C** | Institution Relationship Manager | Flow 4 — Company |
| **D** | Brokerage Principal (firm) | Flow 4 — Company |
| **D** | Brokerage Principal (individual) | Flow 3 — Licensed Agent |
| **D** | Owners' Association Manager | Flow 4 — Company |
| **D** | Property Management Officer | Flow 4 — Company |
| **D** | Company Dispute Filing Officer | Flow 5 — Delegated Staff |
| **E** | Property Owner / Seller | Flow 1 — Individual |
| **E** | Landlord | Flow 1 — Individual |
| **E** | Owner's Representative / PoA Holder | Flow 1 / Flow 2 (if abroad) |
| **F** | Tenant | Flow 1 — Individual |
| **F** | Property Buyer / Investor | Flow 1 — Individual |
| **F** | Diaspora Investor | Flow 2 — Diaspora |
| **G** | Survey Company | Flow 4 — Company |
| **G** | Valuer | Flow 6 — Allied Professional |
| **G** | Conveyancer / Legal Practitioner | Flow 6 — Allied Professional |
| **G** | Registration / Service Trustee Centre | Flow 7 — Trustee Centre |
| **H** | General Public | Flow 9 — Public / Verifier |
| **H** | Institutional Verifier | Flow 9 — Public / Verifier |

# **4\. Profile Management (Post-Registration)** {#4.-profile-management-(post-registration)}

After activation, users maintain their profiles in a secure dashboard scoped to their role:

* **Individuals & Consumers:** Edit contact information, add supplementary ID (utility bill for address proof), link owned or rented properties, and manage complaint references.

* **Diaspora Investors:** Update foreign address and currency preferences, manage the linked representative, and refresh the power of attorney.

* **Developers & Companies:** Manage the company profile, update CAC documents on re-incorporation, designate project managers, and add or revoke delegated staff.

* **Financial & Trust Institutions:** Renew trustee/auditor approvals, manage user provisioning, and update CBN/banking credentials.

* **Agents, Valuers & Conveyancers:** Update licensing details, upload continuing-education or practicing certificates, and manage office addresses.

* **Trustee Centers:** Manage operator rosters, premises, and device whitelists, subject to audit.

* **Regulator / Staff:** Profile changes are governed internally; role and permission changes are made by the system super administrator and logged.

| Grp | Role | Registration Flow | Category |
| ----- | :---- | :---- | :---- |
| **A** | Director-General / Registrar | Flow 8 — Regulator / Admin | EMPLOYEE TAB |
| **A** | System Super Administrator | Flow 8 — Regulator / Admin | EMPLOYEE TAB |
| **A** | Licensing & Registration Officer | Flow 8 — Regulator / Admin | EMPLOYEE TAB |
| **A** | Compliance & Escrow Auditor | Flow 8 — Regulator / Admin | EMPLOYEE TAB |
| **A** | Inspection & Enforcement Officer | Flow 8 — Regulator / Admin | EMPLOYEE TAB |
| **A** | Dispute Adjudication Officer | Flow 8 — Regulator / Admin | EMPLOYEE TAB |
| **A** | Revenue & Finance Officer | Flow 8 — Regulator / Admin | EMPLOYEE TAB |
| **A** | State Liaison Coordinator | Flow 8 — Regulator / Admin | EMPLOYEE TAB |
| **B** | Developer Principal / Director | Flow 4 — Company | BUSINESS  TAB |
| **B** | Project Registration Officer | Flow 5 — Delegated Staff | BUSINESS  TAB |
| **B** | Sales & Disclosure Officer | Flow 5 — Delegated Staff | BUSINESS  TAB |
| **B** | Escrow Liaison | Flow 5 — Delegated Staff | BUSINESS  TAB |
| **C** | Mortgage Officer | Flow 5 — Delegated Staff | BUSINESS  TAB |
| **C** | Account Trustee | Flow 5 — Delegated Staff | BUSINESS  TAB |
| **C** | Auditing Bureau Officer | Flow 5 — Delegated Staff | BUSINESS TAB |
| **C** | Institution Relationship Manager | Flow 4 — Company | BROKERAGE  TAB |
| **D** | Brokerage Principal (firm) | Flow 4 — Company | BROKERAGE  TAB |
| **D** | Brokerage Principal (individual) | Flow 3 — Licensed Agent | BROKERAGE  TAB |
| **D** | Owners' Association Manager | Flow 4 — Company | BUSINESS  TAB |
| **D** | Property Management Officer | Flow 4 — Company | BROKERAGE  TAB |
| **D** | Company Dispute Filing Officer | Flow 5 — Delegated Staff | BUSINESS  TAB |
| **E** | Property Owner / Seller | Flow 1 — Individual | INDIVIDUAL TAB |
| **E** | Landlord | Flow 1 — Individual | INDIVIDUAL TAB |
| **E** | Owner's Representative / PoA Holder | Flow 1 / Flow 2 (if abroad) | INDIVIDUAL TAB |
| **F** | Tenant | Flow 1 — Individual | INDIVIDUAL TAB |
| **F** | Property Buyer / Investor | Flow 1 — Individual | INDIVIDUAL TAB |
| **F** | Diaspora Investor | Flow 2 — Diaspora | INDIVIDUAL TAB |
| **G** | Survey Company | Flow 4 — Company | BUSINESS  TAB |
| **G** | Valuer | Flow 6 — Allied Professional | BUSINESS  TAB |
| **G** | Conveyancer / Legal Practitioner | Flow 6 — Allied Professional | BUSINESS  TAB |
| **G** | Registration / Service Trustee Centre | Flow 7 — Trustee Centre | BUSINESS  TAB |
| **H** | General Public | Flow 9 — Public / Verifier |  |
| **H** | Institutional Verifier | Flow 9 — Public / Verifier |  |

# 