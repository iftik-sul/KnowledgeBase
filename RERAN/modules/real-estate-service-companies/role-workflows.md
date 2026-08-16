---
project: RERAN
module: real-estate-service-companies
type: workflow
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/roles-and-responsibilities.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
  - "RERAN/modules/real-estate-service-companies/navigation.md"
tags:
  - real-estate-service-companies
  - workflow
---

# Real Estate Service Companies Role Workflows

The path any user of a Group D company account takes through the system, from login to logout. This describes the user's route, not the interface — screen-level detail lives in [ui/screens/](ui/screens/), access rules in [navigation.md](navigation.md).

**Proposed.** Group D's roles are described in the source; the post-login journey below is reconstructed from the 26 services this module documents, following the unified-access model from the start (`navigation.md`) rather than describing four separate role-bound journeys that would later need correcting into one.

---

## The Shared Journey

```
Login
↓
View Dashboard
↓
[ Any of the following, in any order, any number of times, by any role: ]

   Jointly Owned Property Administration (#1–#11)
   Register Company for JOP Supervision → Register Owners Association →
     Approve Fees / Manage Escrow / Appoint Auditors, as needed against the
     registered property
   (No fee anywhere in this cluster — see `payments.md` Model 1. No internal
   certification gate and no Account Trustee step — every service routes
   directly from company submission to RERA's Compliance & Escrow Auditor.)

   Licensing (#12–#19)
   Real Estate Licensing Application → Permit / Practice Card services, as needed
   (Services #12–#15: audit/acceptance → pay → receive output. Services #16, #17:
   free, automatic or lightly-reviewed. Service #19: email-only, no portal flow.
   Service #18: not currently wired into this journey — see `navigation.md`'s
   provenance note.)

   Rental (#20–#22)
   Register/Renew Management Contract → Register Tenancy System Users, as needed
   (No fee anywhere in this cluster.)

   Transaction (#23–#24)
   Permit to Sell by Public Auction → Register Property Sold by Auction
   (#23 free; #24 pays, sequenced pay-then-output with no separate audit step
   named — see `payments.md` Model 3.)

   Dispute (#25–#26)
   Primary Suit (Joint Property) → Execution Case, where enforcement is needed
   (Channel-dependent payment timing — Service Center audits before payment;
   online pays near-upfront. See `payments.md` Model 4.)

↓
Track Application Status / Respond to RERAN Information Requests
↓
Retrieve Output Document — pay first where the service requires it (#12–#15,
  #24, #25, #26), or retrieve directly, no payment involved (#1–#11, #16, #17,
  #20–#23)
↓
Logout
```

Every branch is reachable by every logged-in user of the company account. Which branches a given person actually uses is a matter of their role in practice, described below — not a system restriction.

---

## What Each Role Typically Does

### Brokerage Principal

The role with the widest typical service coverage in the module, in practice.

* Company licensing and permits (#12, #13)
* Professional practice card issuance, renewal, cancellation, amendment (#14–#17)
* Training entity accreditation (#19)
* Public auction permit and sale registration (#23, #24)

Sourced directly from the source table's Responsible Role column for every Licensing and Transaction row, confirmed reliable per `open-questions.md` A1.

### Owners'-Association Manager

Typically administers jointly-owned-property matters, in practice.

* Company/property JOP supervision registration (#1)
* Fee approval, employee competence registration (#2, #3)
* Owners' Association registration (#4)
* Escrow account transfer, closure, signatory accreditation (#5–#7)
* Auditor and audit office appointments (#8–#11)

Sourced directly from the source table's Responsible Role column for every Jointly Owned Property row — the cleanest single-role-to-category mapping of any module documented so far.

### Property Management Officer

Typically manages the firm's rental-side registrations, in practice.

* Management contract registration, renewal, and cancellation (#20, #21)
* Tenancy system user registration (#22)

### Company Dispute Filing Officer

Typically files and pursues formal disputes on behalf of managed or jointly-owned properties, in practice.

* Primary suit filing (#25)
* Execution case pursuit (#26)

The smallest responsibility set of the four roles by service count, but not by access — any of the four roles may act on either dispute service under the unified-access model.

---

## Notes

* **No internal certification loop exists anywhere in this module** (`open-questions.md` A5) — unlike Financial & Trust Institutions' mortgage/lease services, no Group D service routes through a company-side maker-checker gate before reaching RERA. Every service goes straight from `Submitted` to RERA review.
* **No Account Trustee step exists in the JOP escrow-adjacent cluster** (`open-questions.md` A3) — despite the "escrow account" terminology in several service names, JOP's escrow services do not mirror Group B/C's Trustee-mediated mechanism. Do not build a Trustee-facing queue for this module unless A3 is revisited.
* **Two services (#6, #19) are email-only**, with no portal-based journey step to describe — the highest count of any module documented so far (every other module has at most one email-only service).
* **Service #18 does not appear in this journey at all**, pending resolution of its Group D vs. Group G provenance question (`open-questions.md` A2, `navigation.md`).
