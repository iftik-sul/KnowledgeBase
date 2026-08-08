  
**REAL ESTATE REGULATORY AGENCY**

**IN**

**NIGERIA**

**PRODUCT REQUIREMENTS DOCUMENT**

RERA Digital Technology Platform

Developed by Kingscott Technologies Ltd

Version 1.0  ·  May 2026 ·  CONFIDENTIAL

Document Owner: Kingscott Technologies Ltd ·  

Prepared for: Real Estate Regulatory Agencies in the Federal Republic of Nigeria

# **Document Control**

This Product Requirements Document (PRD) is a living specification governing the design, development, and delivery of the RERA in the Nigerian Digital Platform. It is authored and maintained by Kingscott Technologies Ltd. as the technology platform designer and owner.

| Field | Detail | Status |
| :---- | :---- | :---- |
| **Document Title** | RERA in Nigeria Digital Platform  PRD | FINAL DRAFT |
| **Version** | 1.0 | May 2026 |
| **Prepared by** | Kingscott Technologies Limited | Confidential |
| **Stakeholder** | Real Estate Regulatory Agencies (RERA) in the Federal Government of Nigeria | Government |
| **Review Date** | Quarterly \- September 2026 | Scheduled |

**This document is classified CONFIDENTIAL. It is intended solely for authorised personnel of RERA in the Federal Government of Nigeria and Kingscott Technologies Ltd., and its approved subcontractors. Distribution beyond these parties requires written authorisation from Kingscott Technologies Ltd.**

# **1\.   Executive Summary**

Nigeria's real estate sector is the second-largest contributor to GDP among non-oil sectors, yet it operates without a unified, technology-enabled regulatory infrastructure. Informal transactions, unverified practitioners, fraudulent title documents, and unresolved landlord-tenant disputes cost Nigerians hundreds of billions of naira annually and actively deter both domestic and foreign property investment.

The Real Estate Regulatory Agencies in Nigeria (RERAN)  are the statutory regulatory authority of the 36 states and Abuja, FCT, in the Federal Government of Nigeria, and Kingscott Technologies Ltd. is partnering to design, develop, deploy, and maintain a comprehensive digital technology platform (the 'RERAN Platform') to transform how Nigeria regulates its real estate market.

This PRD defines the problem, the target users, their needs, the product's required capabilities, and the success criteria against which the platform will be evaluated. It is the single source of truth for all product decisions throughout the design and engineering lifecycle.

# **2\.   Objective \- The "Why"**

## **2.1   The Problem**

Nigeria's real estate market suffers from several deep structural challenges that the RERAN Digital Platform is specifically designed to resolve:

* **Regulatory Opacity:** There is no single, accessible, verified database of registered properties, licensed developers, or accredited agents. Buyers, sellers, and tenants have no reliable mechanism to verify the legal standing of property or practitioners before transacting.

* **Pervasive Fraud:** Land and property fraud, including forged titles, double sales of the same property, and misrepresentation by unlicensed agents, ranks among the most prevalent financial crimes in Nigeria. The absence of a centralized digital registry creates the conditions for these crimes to thrive.

* **Manual, Inefficient Regulation**: RERAN's current operations rely heavily on paper-based processes, in-person visits, and manual workflows. This creates bottlenecks, compliance gaps, and significant institutional inefficiency. SLA enforcement is effectively impossible without a system to track and manage cases.

* **Unresolved Disputes**: Property disputes between buyers and developers, landlords and tenants, or between competing title claimants frequently go unresolved due to the absence of a formal, accessible, technology-enabled dispute-management system.

* **Revenue Leakage**: Without a digitalised fee collection system, regulatory fees are inconsistently collected and insufficiently tracked, depriving RERAN of the institutional revenue needed to fund effective oversight.

* **Diaspora Exclusion:** Millions of Nigerians in the diaspora wish to invest in domestic real estate but are deterred by the inability to transact, verify, and regulate property interests remotely.

## **2.2   Business Goals**

The RERAN Digital Platform is expected to deliver the following business outcomes for the various regulatory agencies and the Nigerian real estate sector:

1. Establish a single, authoritative national digital registry of all regulated real estate entities, properties, developers, agents, and transactions.

2. Digitize and streamline RERAN's full regulatory workflow from application intake through processing, decision, fee collection, and certificate issuance, reducing average processing time by at least 80%.

3. Provide citizens and investors with the tools to verify, transact, and seek redress through a trusted, accessible digital channel available on the web and mobile.

4. Enable robust enforcement by giving RERAN the data, workflow tools, and audit infrastructure needed to identify, investigate, and act on non-compliant practitioners and fraudulent transactions.

5. Increase RERAN's regulatory fee revenue through mandatory digital payment collection, targeting 70% digital collection in Year 1, 90% in Year 2, and 100% in Year 3\.

6. Position Nigeria's real estate sector as a transparent, investor-friendly market aligned with international best practices, supporting the government's Ease of Doing Business agenda.

7. Create a scalable digital infrastructure that can be extended over time to integrate with other federal systems, including the Corporate Affairs Commission (CAC), Nigeria Revenue Service (NRS), and the National Land Commission (NLC)

# **3\.   Target Audience**

## **3.1   Primary User Groups**

### **3.1.1   Property Owners, Buyers & Tenants**

The largest user group by volume, comprising individual Nigerians and corporate entities that own, buy, sell, or rent real property. This group includes the Nigerian diaspora who wish to invest or manage property interests remotely. They need trustworthy information, straightforward self-service transactions, and an accessible mechanism to seek redress. Digital literacy levels vary significantly; the platform must cater to both sophisticated urban users and first-time digital service users.

### **3.1.2   Property Developers (Residential, Commercial & Mixed-Use)**

Registered developers range from large listed companies such as Mixta Africa and Shelter Afrique affiliates to mid-tier indigenous developers who are required by law to register projects, comply with RERAN's development standards, and maintain current licenses. These users undertake complex, multi-document submissions and need efficient case management and milestone tracking across multiple concurrent projects.

### **3.1.3   Real Estate Agents, Brokers & Valuers**

Individually licensed practitioners must maintain current RERAN professional licenses to operate lawfully. They interact with the platform primarily for license applications, renewals, and profile management. Many operate as sole traders with limited administrative capacity; the platform must be frictionless for this group.

### **3.1.4   RERAN Regulatory Staff**

The internal users of the platform's back-end management system, including: Compliance and Registration Officers who process applications; Dispute Resolution Officers who manage complaints and mediations; Finance Officers responsible for fee assessments and revenue tracking; Senior Managers who oversee departmental workloads and SLA performance; the registrar and director-general who exercise final regulatory authority; and IT/system administrators who manage platform access, configuration, and security.

## **3.2   Secondary / Oversight Audience**

* Federal Ministry of Housing, Urban Development, and Public Infrastructure policy oversight and ministerial reporting.

* Office of the Attorney General / Ministry of Justice legal and enforcement support in complex disputes.

* Nigeria Data Protection Commission (NDPC) compliance oversight for personal data processing.

* Financial institutions and mortgage lenders require title and developer verification.

* Foreign and diaspora investors require remote property verification and transparent market data.

# **4\.   Stakeholder Map**

The following table identifies all key stakeholders, their relationship to the platform, and their level of engagement in the project.

| Stakeholder | Category | Interest / Role in Platform | Engagement Level |
| :---- | :---- | :---- | :---- |
| **Real Estate Regulatory Agencies In Nigeria (RERAN)** | Government  Client | Primary owner and operator of the platform; regulatory mandate and policy authority (PPP) | Decision Maker (PPP) |
| **Federal Ministry of Housing / Works** | Government | Policy oversight; integration with the federal housing registry and national land policy | Approver/Decision Maker |
| **Kingscott Technologies Limited** | Technology Partner | Design, development, integration, deployment, and post-launch maintenance and operation of the platform (PPP) | Delivery Lead |
| **Property Developers** | Regulated Industry | Submit project registrations, track compliance obligations, and access licensing services | Primary End User |
| **Real Estate Agents & Brokers** | Regulated Industry | Apply for and renew professional licences, subject to RERA oversight and enforcement | Primary End User |
| **Property Owners & Buyers** | Private Consumer | Register titles, search public registry, file complaints, verify developers and agents | Primary End User |
| **Nigeria Data Protection Commission (NDPC)** | Regulator | Data compliance oversight; all personal data processing must conform to NDPA 2023 | Compliance Authority |
| **Relevant Financial Institutions** | Financial Sector | Mortgage and transaction processing; potential integration for mortgage data verification | Collaborator |
| **Corporate Affairs Commission (CAC)** | Government Agency | Business registration validation; potential API integration for developer entity verification | Collaborator / Future Integration |

     
**5 User Stories & Use Cases**

## **5.1   User Story Summary**

The following user stories describe specific scenarios of how target users will interact with the RERAN Digital Platform. Priority is classified as "Must Have" (core scope for launch), "Should Have" (important but deferrable), and "Could Have" (desirable if capacity allows).

| ID | User Role | As a… I want to… | So that… | Priority |
| :---- | :---- | :---- | :---- | :---- |
| US-01 | **Property Owner** | Register my property on the RERA platform without visiting an office | I can get formal title recognition quickly and with a full documentation trail | Must Have |
| US-02 | **Property Developer** | Submit and track new development project registrations | I can remain compliant with RERA regulations and avoid penalties | Must Have |
| US-03 | **Real Estate Agent / Broker** | Apply for and renew my RERA professional license online | I can operate legally without time-consuming physical office visits | Must Have |
| US-04 | **Prospective Buyer / Tenant** | search a verified public registry of licensed developers, agents, and properties | I can make informed decisions and avoid fraud or misrepresentation | Must Have |
| US-05 | **RERAN Compliance Officer** | review and approve or reject registration applications with full case notes | I can maintain a documented, auditable regulatory decision record | Must Have |
| US-06 | **RERAN Senior Manager** | access a live dashboard of all submissions, SLA timelines, and case statuses | I can monitor the agency's regulatory workload and performance | Must Have |
| US-07 | **Property Owner** | File a complaint against a developer or agent through the platform | I can seek a formal resolution without navigating manual processes | Must Have |
| US-08 | **RERAN Dispute Officer** | manage, escalate, and resolve complaints with all supporting documents | I can resolve disputes within mandated timeframes | Must Have |
| US-09 | **System Administrator** | create, suspend, and manage staff roles and access permissions | I can enforce data security and role-appropriate access across the organisation. | Must Have |
| US-10 | **Property Developer** | upload project documentation and track approval milestones | I can maintain compliance across all phases of a development project | Must Have |
| US-11 | **RERAN Finance Officer** | generate fee assessments and track payments for all regulated services | I can reconcile revenue and maintain financial oversight | Must Have |
| US-12 | **Ministerial Oversight Body** | access aggregate regulatory statistics and performance reports | I can evaluate RERAN's regulatory effectiveness and inform policy | Should Have |
| US-13 | **RERAN Auditor** | Review full audit logs of all system actions and decisions | I can detect irregularities and ensure governance compliance | Must Have |
| US-14 | **Property Owner (Diaspora)** | Access the platform fully from outside Nigeria | I can manage my real estate interests remotely | Must Have |
| US-15 | **IT / DevOps Staff** | monitor platform health, uptime, and performance metrics | I can proactively address technical issues and maintain service levels | Must Have |

## **5.2   Detailed Use Cases**

### **Use Case 1: Property Registration (Private Individual / Developer)**

Trigger: A property owner or developer wishes to register a property title or development project.

Steps:

* The user creates an account or logs into the individual portal and selects 'Register a Property.'

* User completes a structured application form and uploads required documents (survey plan, deed of conveyance, building approval, identification).

* The system validates document completeness against a defined checklist and alerts the user to any deficiencies.

* A reference number is generated, and the application is assigned to a RERAN Registration Officer.

* The officer reviews the application, may raise queries (communicated to the applicant via the portal and SMS/email), and then approves, queries, or rejects.

* On approval, the system generates an invoice for the applicable registration fee. The applicant pays online.

* Upon payment confirmation, the system issues a digitally certified registration certificate downloadable from the portal.

Exception: If documents are found fraudulent at any stage, the system flags the case for escalation to the Compliance Enforcement unit.

### **Use Case 2: Professional License Renewal (Agent / Broker)**

Trigger: A licensed real estate agent receives a renewal reminder 90 days before their current license expires.

Steps:

* The agent receives an automated SMS and email notification linking to the renewal portal.

* Agent logs in, reviews pre-populated license details, updates any changed information, and uploads CPD evidence if required.

* The system validates CPD hours and any regulatory standing issues (pending complaints, outstanding fees).

* The agent pays the renewal fee online. The system updates the license status to 'Active' and issues a renewed digital license certificate.

* The public registry is updated in real time.

Exception: Agents with unresolved complaints or outstanding fees are blocked from renewal until issues are resolved.

### **Use Case 3: Complaint Filing & Resolution (Property Owner)**

Trigger: A property buyer has made payment to a developer for an off-plan property that has not been delivered within the contracted period.

Steps:

* The buyer logs into the citizen portal and selects 'File a Complaint,' choosing the complaint category 'Developer Non-Delivery.

* Buyer uploads supporting documentation (sale agreement, payment receipts, correspondence).

* The complaint is assigned to a RERAN dispute officer. Both parties are notified.

* The developer is given a defined response window (configurable, e.g., 14 days) to submit their position through the portal.

* The Dispute Officer reviews all submissions and can schedule mediation, escalate to legal review, or issue a determination directly.

* Both parties receive automated notifications at each stage. The final determination is documented and published in the applicant's case file.

**6\.   Features & Requirements**

## 

## **6.1   Platform Architecture Overview**

The RERAN Platform shall comprise three integrated layers accessible through web and mobile interfaces:

* Individual & Industry Portal: A public-facing web and mobile application providing self-service access to all RERA-regulated services for property owners, developers, agents, and the general public.

* RERAN Staff Back-Office System: A secure internal management system for RERAN regulatory staff providing application processing, case management, workflow orchestration, and reporting tools.

* Administrative & Integration Layer: System administration, role and access management, API gateway for government system integrations, payment processing, and notification engine.

## **6.2   Functional Requirements**

The table below defines all functional and non-functional requirements. The 'how'  system architecture, technology stack, integration patterns, and UX design is intentionally left to the engineering and design teams within the constraints described.

| ID | Area | Requirement | Priority | User Story |
| :---- | :---- | :---- | :---- | :---- |
| **FR-01** | Property Registration | The platform shall enable property owners and developers to submit property registration applications entirely online, with all required documentation uploaded digitally | Must Have | US-01 |
| **FR-02** | Property Registration | The system shall validate the completeness of submitted documentation against a configurable checklist before acceptance | Must Have | US-01 |
| **FR-03** | Property Registration | Each application shall be assigned a unique reference number, and real-time status tracking shall be available to the applicant | Must Have | US-01, US-10 |
| **FR-04** | Property Registration | RERAN officers shall be able to approve, query, or reject applications with mandatory documented reasoning | Must Have | US-05 |
| **FR-05** | Property Registration | On successful registration, the system shall auto-generate a certified digital title certificate downloadable by the applicant | Must Have | US-01 |
| **FR-06** | Licensing | The system shall support online application, renewal, upgrade, and suspension of licenses for developers, agents, and brokers | Must Have | US-03 |
| **FR-07** | Licensing | The platform shall enforce license expiry tracking and issue automated renewal reminders at 90, 60, and 30 days before expiry | Must Have | US-03 |
| **FR-08** | Licensing | License status (active, suspended, expired) shall be visible in the public registry in real time | Must Have | US-04 |
| **FR-09** | Public Registry | A searchable, publicly accessible registry of all registered properties, licensed developers, and licensed agents shall be available without login | Must Have | US-04 |
| **FR-10** | Registry | Registry search shall support filtering by property type, location, developer, and registration status | Should Have, but Highly Restricted to RERAN Staff | US-04 |
| **FR-11** | Complaints | Property owners and tenants shall be able to file formal complaints through the platform, with document upload support | Must Have | US-07 |
| **FR-12** | Complaints | Each complaint shall be assigned to a RERA Dispute Officer and tracked through defined resolution stages with SLA timers | Must Have | US-08 |
| **FR-13** | Complaints | The system shall support internal escalation workflows and cross-department referrals for complex disputes | Must Have | US-08 |
| **FR-14** | Complaints | Complainants shall receive automated status notifications at every stage change in their case | Must Have | US-07 |
| **FR-15** | Payments | The platform shall integrate a payment gateway supporting card, bank transfer, and USSD payment for all regulatory fees | Must Have | US-11 |
| **FR-16** | Payments | A fee schedule engine shall auto-calculate applicable fees based on application type, property value, and classification | Must Have | US-11 |
| **FR-17** | Payments | Automated payment receipts and tax invoices shall be generated upon successful payment | Must Have | US-11 |
| **FR-18** | Reporting | The system shall provide a live operational dashboard for RERA managers showing application volumes, SLA status, and revenue | Must Have | US-06 |
| **FR-19** | Reporting | Configurable reports shall be exportable in PDF and Excel formats, covering all regulatory service areas | Must Have | US-12 |
| **FR-20** | Reporting | A ministerial-level aggregate dashboard shall present macro sector statistics, including market size, registered entities, and compliance rates | Must Have | US-12 |
| **FR-21** | Access Control | The platform shall implement role-based access control with granular permissions assignable by a system administrator | Must Have | US-09 |
| **FR-22** | Access Control | All user actions (logins, approvals, rejections, data changes) shall be logged in a tamper-evident audit trail | Must Have | US-13 |
| **FR-23** | Access Control | The system shall enforce multi-factor authentication for all RERA staff accounts | Must Have | US-09 |
| **NFR-01** | Performance | Platform uptime shall be not less than 99.5%, excluding scheduled maintenance windows | Must Have | US-15 |
| **NFR-02** | Performance | All citizen-facing pages shall load in under three seconds on a 3G connection | Must Have | US-14 |
| **NFR-03** | Security | All data in transit and at rest shall be encrypted using AES-256 and TLS 1.3 or higher | Must Have | US-09 |
| **NFR-04** | Security | The system shall be compliant with the Nigeria Data Protection Act 2023 (NDPA) and all NDPC guidelines | Must Have | US-09 |
| **NFR-05** | Accessibility | The citizen portal shall support English and Hausa/Igbo/Yoruba language interfaces | Should Have / Future Configuration | US-14 |
| **NFR-06** | Scalability | The architecture shall support horizontal scaling to handle a minimum of 100,000 concurrent users | Must Have | US-15 |
| **NFR-07** | Integration | The platform shall expose a documented API layer for future integration with relevant federal government systems (e.g., CAC, NRS, NLC) | Must Have | US-09 |

## **6.3   Key Feature Modules**

### **Module 1: Property & Project Registration**

* Online registration for freehold, leasehold, and off-plan properties.

* Developer project registration covering all residential, commercial, and mixed-use developments requiring RERAN approval.

* Document management with configurable checklists per registration category.

* Automated title certificate generation with QR code verification.

### **Module 2: Licensing & Accreditation**

* End-to-end digital lifecycle for developer, agent, broker, and valuer licenses.

* Automated expiry tracking, multi-stage renewal reminders, and bulk renewal processing.

* Integration hooks for background verification (CAC entity status, court records).

### **Module 3: Public Registry & Market Information**

* Publicly searchable registry of all licensed entities and registered properties.

* Market data dashboard showing registration volumes, transaction trends, and sector statistics (anonymized).

* QR and reference code verification tools for instant status lookup via mobile.

### **Module 4: Complaints, Disputes & Enforcement**

* Structured multi-category complaint submission with document attachment.

* Case lifecycle management from filing through investigation, mediation, determination, and closure.

* Automated SLA timers with escalation triggers and management alerts on breach.

* Enforcement action recording (suspensions, license revocations, referrals to prosecution).

### **Module 5: Payments & Revenue Management**

* Integrated payment gateway supporting Paystack / Flutterwave / Interswitch and USSD.

* Configurable fee schedule engine based on property type, value band, and service category.

* Automated receipt generation, payment reconciliation reports, and revenue analytics.

### **Module 6: Staff Workflow & Case Management**

* Queue management and workload assignment tools for all RERAN processing teams.

* SLA tracker with color-coded dashboards surfacing at-risk and breached cases.

* Internal communication tools (notes, queries to applicants, and interdepartmental referrals).

* Decision documentation with mandatory reasoning fields for all approvals and rejections.

### **Module 7: Reporting, Analytics & Oversight**

* Real-time operational dashboard for RERAN management with KPI widgets.

* Configurable scheduled reports for ministerial and management review.

* Export functionality in PDF and Excel for all major report types.

* Aggregate sector statistics portal for public and ministerial audiences.

### **Module 8: Administration, Security & Audit**

* Role-based access control with granular permission management by the system administrator.

* Tamper-evident, immutable audit trail logging all system actions and decisions.

* Multi-factor authentication mandatory for all staff accounts.

* Compliance controls for the Nigeria Data Protection Act 2023 (NDPA) and NDPC guidelines.

# **7\.   Success Metrics**

The following Key Performance Indicators (KPIs) define what success looks like for the RERA Digital Platform. These metrics will be reviewed at the cadence specified and reported to RERA management and Kingscott's project leadership.

| \# | Metric | Definition | Target | Review Cadence |
| :---- | :---- | :---- | :---- | :---- |
| **1** | **Platform Adoption Rate** | % of eligible regulated entities registered on the platform within 12 months of launch | ≥ 60% Year 1 / ≥ 85% Year 2 | Quarterly |
| **2** | **Application Processing Time** | Average calendar days from submission to final decision (registration/licensing) | ≤ 10 working days | Monthly |
| **3** | **SLA Compliance Rate** | % of applications processed within mandated SLA timelines | ≥ 90% | Monthly |
| **4** | **Complaint Resolution Rate** | % of filed complaints fully resolved within 30 calendar days | ≥ 80% | Monthly |
| **5** | **System Uptime** | Platform availability excluding scheduled maintenance | ≥ 99.5% | Weekly |
| **6** | **Digital Revenue Collection** | % of RERAN regulatory fees collected through the platform (vs. cash/manual) | ≥ 70% Year 1 / ≥ 90% Year 2 | Quarterly |
| **7** | **User Satisfaction Score** | Individual satisfaction rating post-transaction (CSAT / NPS surveys) | NPS ≥ \+30 | Quarterly |
| **8** | **Data Accuracy Rate** | % of registry records passing automated data integrity validation checks | ≥ 95% | Monthly |
| **9** | **Staff Efficiency Gain** | Reduction in average staff hours per application vs. pre-platform baseline | ≥ 40% reduction | 6-Monthly |
| **10** | **Fraud / Duplicate Incidents** | Number of verified fraudulent registrations or duplicate title attempts detected and blocked | Zero undetected / \< 0.5% flagged | Monthly |

***Baseline measurements for processing time, SLA compliance, and staff efficiency will be captured during Phase 1 discovery (Months 1–2) through structured assessment of RERAN's current manual workflows. Targets above will be recalibrated if the baseline differs materially from the assumptions used in this document.***

# **8\.   Indicative Delivery Roadmap**

The following phased delivery roadmap reflects the sequencing of features based on criticality, dependency, and regulatory priority. Detailed sprint planning and milestone dates will be established during Phase 1 discovery.

| Phase | Timeline | Scope | Status |
| :---- | :---- | :---- | :---- |
| **Phase 1** | Week 1-2 | Discovery, system architecture, UI/UX design, infrastructure setup, and RERAN staff onboarding. Core registration and licensing modules developed and tested. | In Planning |
| **Phase 2** | Week 3-4 | Complaints module, payment gateway integration, public registry portal, audit trail, dashboard, and reporting. | Planned |
| **Phase 3** | Week 5-6 | API layer, ministerial reporting, multi-language support, security audit, user acceptance testing, and go-live. | Planned |
| **Phase 4** | Week 7-8 | Performance optimization, integration with federal systems (CAC, NRS), expanded analytics, and mobile app. | Planned |

# **9\.   Assumptions & Constraints**

## **9.1   Assumptions**

* RERAN will provide timely access to relevant existing data sets, regulatory frameworks, fee schedules, and legacy records required to populate the platform at launch.

* RERAN PPP Product Owner designate (Kingscott Technologies Ltd.) will liaise with authorities to make product decisions and approve deliverables at each phase gate.

* A reliable cloud hosting environment compliant with Nigeria's data sovereignty requirements will be procured and made available by the infrastructure mobilisation milestone.

* All RERAN staff required to use the platform will undergo structured onboarding and training before go-live.

* Legal authority for mandatory digital registration and fee collection will be formally confirmed by RERAN's legal team before the payment module is activated in production.

## **9.2   Constraints**

* All personal data processing must comply with the Nigeria Data Protection Act 2023 (NDPA) and all applicable NDPC guidelines. No personal data shall be transferred to servers outside Nigeria without appropriate safeguards.

* The platform must be accessible on low-bandwidth connections common in secondary Nigerian cities (target: functional on 3G connections).

* Security architecture must be compliant with relevant federal government ICT security guidelines (NITDA).

* The system must be designed for operational resilience, including graceful degradation, given the variable power and internet infrastructure in parts of Nigeria.

# **10\.   Key Risks & Mitigations**

| Risk | Potential Impact | Mitigation |
| :---- | :---- | :---- |
| **Low RERAN staff digital adoption** | Underutilisation of the system; continued manual processes | Dedicated change management programme; staged rollout; on-site training and super-user designation |
| **Data migration complexity (legacy records)** | Delays to go-live; incomplete registry at launch | Early discovery sprint; data cleansing strategy; phased migration with manual fallback |
| **Regulatory legal framework gaps** | Features blocked or delayed pending legal authorisation | Legal advisory engagement in Phase 1; phased feature activation aligned to legal confirmations |
| **Payment gateway integration issues** | Revenue collection delays; poor user experience | Early procurement; parallel testing of multiple providers (Paystack, Flutterwave, Interswitch) |
| **Cybersecurity threats/data breach** | Reputational damage; regulatory liability; loss of public trust | Third-party penetration testing; NDPA-compliant architecture; incident response plan |
| **Connectivity limitations in the user base** | Low adoption in rural/secondary markets | USSD / SMS fallback for critical notifications and payments; mobile-first responsive design |
| **Stakeholder alignment (RERAN / Ministry)** | Scope creep, conflicting requirements, and approval delays | Formal governance framework; regular steering committee; RACI-defined decision rights |

# **11\.   Out of Scope  Version 1.0**

The following items are explicitly excluded from the Version 1.0 platform scope and are candidates for future phases:

* Integration with state-level land registries (each state operates its own land administration system under the Land Use Act; federal-state integration requires separate bilateral agreements). Vs 1.0

* Automated AI-powered title fraud detection (planned for Phase 3/4 once sufficient transaction data exists).

* Direct e-conveyancing or in-platform property transaction processing (this PRD covers regulatory registration, not conveyancing).

* Native mobile applications for iOS and Android (a responsive web application is in scope for v1.0 as well as native apps deliverable).

* Integration with international anti-money laundering (AML) or cross-border investor verification systems.

# **12\.   Glossary**

| Term | Definition |
| :---- | :---- |
| **RERAN** | Real estate regulatory agencies in Nigeria at the state levels are the statutory bodies responsible for regulating the Nigerian real estate sector. |
| **PRD** | Product Requirements Document: a specification defining the 'what' and 'why' of a product, without prescribing the 'how.' |
| **Kingscott** | Kingscott Technologies Ltd, the technology in a private-public partnership with RERAN, will design, build, maintain and operate the platform. |
| **NDPA 2023** | The Nigeria Data Protection Act 2023 is the principal federal legislation governing personal data processing in Nigeria. |
| **NDPC** | Nigeria Data Protection Commission, the regulatory authority responsible for enforcing the NDPA 2023\. |
| **CAC** | The Corporate Affairs Commission is the federal agency responsible for business registration in Nigeria. |
| **NRS** | Nigeria Revenue Service, the federal tax authority. |
| **NLC** | The National Land Commission is the federal body responsible for national land policy. |
| **SLA** | A Service Level Agreement is a defined standard for processing time or service delivery within which RERAN staff must complete regulatory tasks. |
| **KYC** | Know Your Customer identity verification processes are applied to individuals and entities transacting on the platform. |
| **RBAC** | Role-Based Access Control is a security model that restricts system access based on the user's organizational role. |
| **API** | An application programming interface is a standardized interface allowing the RERAN Platform to exchange data with other government or financial systems. |
| **MFA** | Multi-Factor Authentication is a security mechanism requiring users to verify identity through two or more independent factors. |
| **CPD** | Continuing Professional Development: ongoing training requirements applicable to licensed real estate practitioners. |
| **USSD** | Unstructured Supplementary Service Data is a mobile communication protocol enabling menu-based services on basic mobile handsets without internet access. |

# **13\.   Document Sign-Off**

This product requirements document is subject to formal review and sign-off by the authorized persons at Kingscott Technologies Ltd. before engineering work commences. Sign-off constitutes acceptance of the scope, objectives, user stories, requirements, and success metrics as defined herein.

| Role | Name | Signature | Date |
| :---- | :---- | :---- | :---- |
| **CEO / Project Lead, Kingscott** |  | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_ |
| **Legal Counsel/Secretary** |  | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \_\_\_\_\_\_\_\_\_\_\_\_ |

