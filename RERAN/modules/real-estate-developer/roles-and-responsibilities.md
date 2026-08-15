---
project: RERAN
module: real-estate-developer
type: user-group
status: current
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
tags:
  - real-estate-developer
  - roles
---

# Real Estate Developer Roles & Responsibilities

## 1. Developer Principal / Director

### Who are they?

The senior executive or owner of the real estate development company. They oversee the entire business but usually do not perform day-to-day operational work.

### Main Responsibilities

* Monitor all development projects  
* Review project registrations  
* Monitor property sales  
* Review escrow status  
* Track regulatory compliance  
* Make business decisions  
* Represent the company before RERA  
* Review organizational reports  
* Monitor company performance

### Practical Example

Imagine **ABC Developers Ltd.** is constructing a 500-unit housing estate.

The Developer Principal:

* Checks that the project registration has been submitted.  
* Reviews how many units have been approved by RERA.  
* Sees that 150 apartments have been sold.  
* Notices an escrow payment is delayed.  
* Reviews reports before attending a meeting with investors.  
* Decides whether to start a new development project.

They are asking questions like:

> "Are all our projects progressing properly?"

rather than

> "Let me upload this document."

## 2. Project Registration Officer

### Who are they?

The employee responsible for handling all registrations and regulatory submissions to RERA.

### Main Responsibilities

* Register new development projects  
* Register properties  
* Upload required documents  
* Submit applications  
* Respond to RERA requests  
* Track approval progress  
* Generate registration reports

### Practical Example

ABC Developers starts a new apartment project.

The Project Registration Officer:

1. Creates the new project in the RERA portal.  
2. Enters project details.  
3. Uploads:  
   * Building plans  
   * Environmental approvals  
   * Land title  
4. Submits the application.  
5. Later receives a request from RERA:  
   "Please upload the updated survey plan."  
6. Uploads the revised document.  
7. Monitors the application until it is approved.

This role spends most of the day inside the registration and applications modules.

## 3. Sales & Disclosure Officer

### Who are they?

The employee responsible for property sales records and ensuring all legally required disclosures are submitted to RERA.

### Main Responsibilities

* Manage property listings  
* Record property sales  
* Submit sales disclosures  
* Maintain buyer information  
* Update property status  
* Ensure sales comply with regulations  
* Generate sales reports

### Practical Example

Apartment A-120 is sold to **John Smith**.

The Sales & Disclosure Officer:

1. Marks Apartment A-120 as Sold.  
2. Enters:  
   * Buyer name  
   * Sale price  
   * Sale date  
3. Uploads the sale agreement.  
4. Submits the required disclosure to RERA.  
5. Tracks whether RERA approves the disclosure.

They make sure every property sale is properly recorded and reported.

> **Confirmed 2026-08-15 (issue #37).** Eight service-flow files — #1 (Register Initial Sale), #2 (Register Initial Rent-to-Own), #3 (Register Initial Usufruct), #4 (Amend Initial Procedures Data), #5 (Complete Initial Procedures Data), #6 (Register Mortgage-Linked Sale), #7 (Transfer Registration Fees), and #19 (Terminate Initial Registration) — previously attributed "typically filed by" to the Project Registration Officer, inherited from an old UI screen's role-gated sidebar scoping rather than checked against this section. All eight are corrected to Sales & Disclosure Officer, matching this role's worked example above and the master service table's own Responsible Role column. This section itself needed no correction — the "How They Work Together" table below already had it right; the service-flow files had drifted from it.

## 4. Escrow Liaison

### Who are they?

The employee responsible for coordinating escrow-related activities between the developer, the financial institution, and RERA.

### Main Responsibilities

* Monitor escrow accounts  
* Coordinate with banks  
* Submit escrow documents  
* Track construction milestones  
* Monitor fund releases  
* Resolve escrow-related issues  
* Generate escrow reports

### Practical Example

The developer has completed the building foundation and is eligible for the first escrow fund release.

The Escrow Liaison:

1. Confirms the construction milestone has been completed.  
2. Uploads supporting evidence.  
3. Coordinates with the escrow bank.  
4. Tracks the release request.  
5. Monitors when the bank releases the funds.  
6. Updates management on the escrow status.

They ensure construction payments are released according to approved milestones.

> **Confirmed 2026-08-15 (issue #37).** Seven service-flow files — #8 through #12, #20, and #21 — carried the same disagreement in the other direction: the master service table's Responsible Role column says Sales & Disclosure Officer for all seven, not Escrow Liaison, but the actual work matches this section's Escrow Liaison description directly. All seven files now flag the table's disagreement explicitly rather than presenting the Escrow Liaison attribution as uncontested fact.

## How They Work Together

**Descriptive, not access-restrictive — corrected 2026-08-15.** The table below shows who *typically* handles each stage in practice, not who is *permitted* to. Group B does not gate access by role: all four roles have identical access to every screen and action, and any of them may perform any stage's actions. See [navigation.md](navigation.md) for the unified access model. This table previously read as an assignment of each stage to one role; it is now a description of customary division of labour, useful for understanding the audit trail rather than for determining permissions.

Let's follow a real project from start to finish:

| Stage | Typically handled by |
| :---- | :---- |
| Company decides to build a new estate | **Developer Principal / Director** |
| Register the new project with RERA | **Project Registration Officer** |
| Upload project documents and respond to RERA queries | **Project Registration Officer** |
| Start selling completed units | **Sales & Disclosure Officer** |
| Record each sale and submit disclosures | **Sales & Disclosure Officer** |
| Manage escrow account and milestone-based fund releases | **Escrow Liaison** |
| Monitor the overall progress, compliance, sales, and financial status | **Developer Principal / Director** |

Any of these stages may be carried out by any role — a Principal / Director may file a registration directly, an Escrow Liaison may record a sale, and the officer who files a record may also act on it later. Whoever performs the action, the audit trail records their name and the role they held at the time.

In short, each role's customary focus is:

* **Developer Principal / Director** → Runs the business and makes strategic decisions.  
* **Project Registration Officer** → Registers projects and manages regulatory applications.  
* **Sales & Disclosure Officer** → Handles property sales and mandatory disclosures.  
* **Escrow Liaison** → Coordinates escrow accounts and construction fund releases.
