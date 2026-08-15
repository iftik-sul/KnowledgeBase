---
project: RERAN
module: individual-user
type: user-group
status: current
updated: 2026-08-15
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - individual-user
  - roles
---

# Individual User Roles & Responsibilities

The **Individual User** module serves natural persons who interact with the RERA platform to buy, own, rent, lease, sell, or manage real estate. Unlike organizational users, an individual may perform multiple roles over time using the same account. The platform grants access to services based on the user's current activities and permissions.

**On the Landlord/Tenant overlap below, resolved 2026-08-15 (`open-questions.md` D1):** the Landlord and Tenant responsibility lists both include lease-related actions — "renew lease records" appears in both. This is not a drafting error and does not need disambiguating. It reflects the same principle stated in the paragraph above and worked out fully in `navigation.md`'s activity-scoped access model: **one account can hold both roles at once, against different properties.** Consider Mike: he rents the flat he lives in (Tenant) but also owns and rents out a separate flat to someone else (Landlord). When Mike renews the lease on his own rented flat, he may do so as Tenant, self-registering the lease he's signed, under the secondary applicant path `open-questions.md` B1 established for Register/Renew Lease. When Mike renews the lease on the flat he rents *out*, he does so as Landlord, the primary applicant on that same service. Same person, same account, same platform session even — two different leases, two different roles. Neither responsibility list is claiming exclusive ownership of "renew lease records"; each is describing what that action looks like when the account is acting in that role for that particular property. Nothing in the source or in this module's design model prevents one person from occupying both roles across their own portfolio, and B1's secondary-applicant resolution for #23/#24 exists precisely to support this.

## 1. Property Owner / Seller

### Purpose

Represents an individual who owns one or more properties and manages ownership records, property transactions, and title-related activities.

### Responsibilities

* Register owned properties  
* Manage property ownership records  
* Initiate property sales and ownership transfers  
* Upload required property documents  
* Track property transaction status  
* Respond to RERA requests during registration or transfer processes

### Practical Example

Ahmed purchases a residential property and registers it with RERA. Three years later, he decides to sell the property. Through the platform, he initiates the ownership transfer, uploads the required documents, pays the applicable fees, and tracks the approval until the title is transferred to the new owner.

## 2. Landlord

### Purpose

Represents an individual who leases or rents out owned properties and manages tenancy-related activities.

### Responsibilities

* Register rental properties  
* Create and renew lease records **for properties they own and let out** — see the note above on how this overlaps, intentionally, with the Tenant role's own renewal responsibility below  
* Manage tenancy information  
* Update rental property details  
* Monitor active rental agreements  
* Participate in tenancy-related services

### Practical Example

Grace owns an apartment building with several tenants. She registers each lease agreement through the platform, renews tenancy records when contracts expire, and updates tenant information whenever new tenants move in.

## 3. Owner's Representative / Power of Attorney (PoA) Holder

### Purpose

Represents an authorized individual acting on behalf of a property owner under a valid Power of Attorney.

### Responsibilities

* Act on behalf of the property owner  
* Submit property-related applications  
* Manage transactions for represented properties  
* Upload supporting authorization documents  
* Track applications and respond to regulatory requests

### Practical Example

David lives in Lagos while his mother lives abroad. She grants him Power of Attorney to manage her properties. David uses the platform to renew leases, submit property applications, and complete ownership transactions on her behalf.

## 4. Tenant

### Purpose

Represents an individual renting residential or commercial property who uses the platform for tenancy services and consumer protection.

### Responsibilities

* Register tenancy information — as the secondary applicant path on Register Lease (#23), self-registering a lease they've signed; see `open-questions.md` B1  
* Renew lease records **for the tenancy they themselves hold** — the same overlap with Landlord's responsibility above, and the same resolution: this is the account acting as Tenant on its own lease, not a conflicting claim over the Landlord's action on a different one  
* Submit rental-related complaints  
* Request dispute resolution  
* Track tenancy applications and dispute cases

### Practical Example

Sarah rents an apartment. After her landlord refuses to return her security deposit, she submits a dispute through the RERA platform, uploads supporting documents, and tracks the resolution process.

## 5. Property Buyer / Investor

### Purpose

Represents an individual purchasing real estate for personal ownership or investment purposes.

### Responsibilities

* Verify registered developers  
* Verify registered projects  
* Review project legitimacy before purchase  
* Monitor off-plan project progress  
* Submit consumer complaints when necessary  
* Track purchase-related applications

### Practical Example

Michael plans to purchase an off-plan apartment. Before making payment, he verifies that the developer and project are registered with RERA, monitors construction progress through the platform, and receives updates until completion.

## 6. Diaspora Investor

### Purpose

Represents a Nigerian living abroad or a foreign individual investing in Nigerian real estate through remote identity verification and online property services.

### Responsibilities

* Complete remote identity verification  
* Purchase and monitor properties from abroad  
* Manage foreign contact information  
* Link an authorized representative when required  
* Track investments remotely  
* Complete transactions without travelling to Nigeria

### Practical Example

Aisha lives in the United Kingdom and purchases an apartment in Abuja. She completes identity verification using her passport, appoints her brother as her authorized representative, monitors construction progress remotely, and receives updates through the platform until the property is completed.

These responsibilities align with the **RERA Nigeria User Group Structure** and **Registration Flows** documents:

* **Property Owner / Seller** – Registers sales, transfers, leasing information, and manages title records.  
* **Landlord** – Registers and renews leases and manages tenancy records.  
* **Owner's Representative / PoA Holder** – Acts under a valid Power of Attorney on behalf of property owners.  
* **Tenant** – Registers leases, renews tenancy, and files rental disputes.  
* **Property Buyer / Investor** – Verifies developers and projects, tracks off-plan progress, and lodges complaints.  
* **Diaspora Investor** – Completes remote KYC, transacts through representatives when needed, and manages investments remotely.
