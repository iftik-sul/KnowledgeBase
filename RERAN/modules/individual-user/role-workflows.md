---
project: RERAN
module: individual-user
type: workflow
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/roles-and-responsibilities.md"
  - "RERAN/modules/individual-user/open-questions.md"
  - "RERAN/modules/individual-user/navigation.md"
  - "RERAN/modules/individual-user/payments.md"
tags:
  - individual-user
  - workflow
---

# Individual User Role Workflows

The path a natural person takes through the platform, from login to logout, across the module's 43 services. As established in `navigation.md`, this is **not** six separate role-gated journeys the way a corporate account's roles might be — one account can act as any combination of these six roles depending on what it currently owns, leases, or holds authorization over. What follows is one shared journey, with a per-role section afterward describing what each role *typically* does and — new in this document, not previously stated anywhere in the module — **how much of that typical behaviour is actually sourced versus extrapolated** (see `open-questions.md` B4/B5).

---

## The Shared Journey

```
Login
↓
View Dashboard
↓
[ Any of the following, depending on what the account currently owns/holds/leases: ]

   Verification (#1–#3)
   Select Service → Enter Search Criteria → Pay → Submit → View Result
   (Upfront payment, confirmed — no counter-channel alternative sourced for any of these three.)

   Property Ownership & Registration (#4, #17–#22, #35, #41, #43)
   Select Service → Enter Property/Applicant Details → Upload Documents →
     Pay (upfront, confirmed for #4, #19–#22, #35, #41, #43) →
     Submit → RERAN Review → Approved → Receive Title Documents
   (#17, #18, #33 are the confirmed exception — no fee at all per `open-questions.md` A3;
   #41 additionally sources a Trustee-Centre-only channel where payment happens *after*
   RERAN's audit, not before — see `payments.md` Category 2.)

   Property Transactions (#5–#16)
   Select Property → Enter Counterparty Details → Upload Documents →
     [Online:] Pay → Submit → RERAN Review → Approved → Receive Documents
     [Trustee Centre, where sourced:] Submit → RERAN Audits → Pay → Receive Documents
   (The Trustee Centre branch is sourced for all of #5, #9–#16 but only fully documented in
   this module's files for a subset — see `payments.md` Category 3 and `open-questions.md` A2.
   #7 splits into two components with different fee treatment — see `payments.md` Category 4.)

   Tenancy (#23–#28, #40)
   Select Service → Enter Lease/Tenant Details → Upload Documents →
     [Online:] Pay → Submit
     [Trustee Centre:] Submit → RERAN Audits → Pay → Receive Certificate
   (#23, #24, #26 already document the Trustee-Centre order correctly in their own workflow
   sections — only their Section 9 boilerplate needs correcting, per `open-questions.md` A1.
   #28 sources payment *after* RERAN's approval, not before, per A4. #40 has no fee at all —
   already correctly documented. #25 is fee-conditional, not upfront-or-after — see
   `payments.md` Category 6.)

   Power of Attorney (#29, #30, #42)
   Register (#29): Select Property → Enter Attorney Details → Define Scope → Pay → Submit
   Act on Behalf (#30): Select Property Owner → System Validates PoA → Select Service →
     Pay (where the selected service requires it) → Submit
   Cancel (#42): Visit Customer Centre → Submit Documents → RERAN Reviews
   (#42's fee, output document, and completion criteria are not specified in source at all —
   the thinnest-specified service in the module, already flagged as such in its own file.)

   Property Information & Certificates (#31–#35)
   Search Property → Enter Request Details → Pay → Submit → Receive Document
   (#33 is the confirmed no-fee exception among this group — see A3.)

   Diaspora (#36–#37)
   Verify Identity (#36): Enter Personal Info → Upload ID → Biometric Check → Pay → Submit
   Remote Transaction (#37): Confirm #36 Complete → Select Transaction Type → [routes into
     the relevant service above, e.g. #5, #6, #23]
   (#37 is a routing layer over other services, not a separate transaction type of its own —
   its payment timing therefore inherits whatever the underlying selected service uses.)

   Consumer Protection (#38–#39)
   Submit Complaint (#38): Select Category → Enter Details → Upload Evidence →
     [Pay, pending `open-questions.md` A7] → Submit → RERAN Investigates → Resolution
   Track Complaint (#39): Search → View Status (free, per `open-questions.md` A6 — payment
     gate should be removed)

↓
Track Application Status (Feature #2, free) / Respond to Information Requests (Feature #3, free)
↓
Retrieve Output Document — pay-then-retrieve, retrieve-then-pay-at-counter, or retrieve
  directly with no payment, depending on which category above the service falls into
  (see `payments.md` for the full per-service breakdown — this module does not have a
  single uniform answer to "when does payment happen," unlike what a first read of the
  Section 9 boilerplate across all 43 files would suggest)
↓
Logout
```

---

## What Each Role Typically Does

### Property Owner / Seller

The module's default/fallback role — the master table's Responsible Role column names this role for the overwhelming majority of Group E's 28 sourced rows (checked directly in `open-questions.md` B2, and found to be a substantively accurate attribution, not a coarse default the way Group C's equivalent column was).

* Register, transfer, and sell property (#4–#9)
* All lease-to-own and usufruct lifecycle services (#10–#16)
* All Title & Land Registration services (#17–#22, #43) — including acting as the receiving party in Heirs Ownership (#19) and Community Land (#20) registrations, where the applicant's status as heir or community representative is a precondition for *becoming* this role for that transaction, not a separate role (`open-questions.md` B3)
* Register and cancel Power of Attorney over their own property (#29, #42)
* Request certificates and statements (#31–#35)
* Register a company in connection with property holdings (#41)

**Sourced vs. extrapolated:** the most source-grounded role in the module. Every service above traces to an explicit master-table row except #4 itself (extrapolated, per `services-overview.md`).

### Landlord

* Register and renew leases (#23, #24) — **flagged, not settled.** The master table attributes row 82 to *Tenant*, not Landlord; this module's own role-description text gives both roles overlapping "register/renew lease" language. Documented here as Landlord per the current service-flow files' framing, with the conflict and a proposed joint-access resolution recorded in `open-questions.md` B1. Treat this bullet as provisional until that question is confirmed.
* Manage active leases (#25)
* Upload building details for leasing (#40) — the only service in the module specified in source as an off-platform, email-based process rather than an in-app form; already correctly documented that way in #40's own file.

**Sourced vs. extrapolated:** #23/#24 and #40 are sourced (rows 82, 85); #25 is extrapolated.

### Owner's Representative / PoA Holder

* Act on behalf of a property owner within the scope of a registered Power of Attorney (#30)

**Sourced vs. extrapolated — checked directly, not previously stated anywhere in this module (`open-questions.md` B5):** this role **never appears as a Responsible Role in any of the 41 sourced master-table rows for Groups E and F.** Its only direct documented service (#30) is extrapolated. It has a secondary, derivative presence — "Authorized Representative acting under a valid Power of Attorney" appears as an alternate applicant in nearly every sourced service's Who Can Apply section — but that presence is never the row's primary sourced actor. This role's entire standalone documentation rests on `roles-and-responsibilities.md`'s own worked example (David) and the extrapolated #29/#30, not on the master service table.

### Tenant

* Register/renew leases as an alternate or joint actor with Landlord — see the B1 flag above
* Cancel a tenancy contract (#27), jointly with Landlord
* Submit and pursue tenancy disputes (#26) — the module's clearest sourced role attribution: all ten consolidated dispute rows (72–81) name Tenant as the Responsible Role without exception
* Request rental valuation (#28), alongside Property Owner, Landlord, and prospective tenants

**Sourced vs. extrapolated:** #26's ten source rows are unambiguously sourced and unambiguously Tenant. #27's role attribution (Tenant, per row 83) is consistent with the file's current dual Landlord/Tenant framing. #28 (row 84) is sourced but its Who Can Apply list is broader than "Tenant" alone.

### Property Buyer / Investor

* Verify developers, projects, and properties before purchase (#1–#3)
* Participate as purchaser in Register Property Sale (#6)
* Diaspora-adjacent purchase flows via #37 where relevant

**Sourced vs. extrapolated — checked directly, not previously stated anywhere in this module (`open-questions.md` B4):** like Owner's Representative/PoA Holder above, this role **never appears as a Responsible Role in the sourced master-table rows.** Its documented service list is drawn almost entirely from the 11 extrapolated services (#1–#3 specifically). #6 is the one point of contact with a sourced row, and even there the master table's role column names Property Owner/Seller for the row, with "Purchaser" appearing only in the file's own workflow narrative (the purchaser's 16-step sub-flow), not the source's Responsible Role field.

### Diaspora Investor

* Remote identity verification (#36)
* Remote property transactions (#37), routing into whichever underlying service (#5, #6, #23, etc.) the transaction actually is

**Sourced vs. extrapolated:** entirely extrapolated, same finding as Property Buyer/Investor and for the same reason — #36/#37 are both in the 11-service extrapolated list, and this role never appears as a Responsible Role in any of rows 72–112.

---

## Provenance Summary — New Finding, Not Previously Documented

Of the module's six roles, **three (Property Owner/Seller, Landlord, Tenant) are the only ones the master service table ever directly names as a Responsible Role.** The other three (Owner's Representative/PoA Holder, Property Buyer/Investor, Diaspora Investor) exist in this module's documentation entirely through `services-overview.md`'s 11 extrapolated services and `roles-and-responsibilities.md`'s own worked-example prose — never through the source workbook's own workflow table.

This isn't a defect — `services-overview.md` already discloses the sourced/extrapolated split at the *service* level, and extrapolating from role-description text is the explicit, sanctioned method this project uses to fill gaps in incomplete client material. But it hadn't previously been stated at the *role* level, and it matters for how much weight the client should be asked to put on any future correction to those three roles' responsibilities: there's no master-table row to check a proposed correction against, unlike Property Owner/Seller, Landlord, or Tenant, where the source gives a check the documentation team can verify against directly.

## Superseded By This Document

Nothing — this is the first `role-workflows.md` this module has had.
