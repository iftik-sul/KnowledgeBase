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

   Property Ownership & Registration (#4, #17–#22, #35, #43)
   Select Service → Enter Property/Applicant Details → Upload Documents →
     Pay (upfront, confirmed for #4, #19–#22, #35, #43) →
     Submit → RERAN Review → Approved → Receive Title Documents
   (#17, #18, #33 are the confirmed exception — no fee at all per `open-questions.md` A3.
   #41 is deliberately excluded from this group — corrected 2026-08-15, found in an audit
   pass. It was previously listed here alongside the upfront payers, but #41 is Trustee-
   Centre-only with no online channel at all, and its one channel pays *after* RERAN's
   audit, the opposite of "upfront" — see the Trustee Centre group below, where it now
   belongs.)

   Property Transactions (#5–#16)
   Select Property → Enter Counterparty Details → Upload Documents →
     [Online:] Pay → Submit → RERAN Review → Approved → Receive Documents
     [Trustee Centre, where sourced:] Submit → RERAN Audits → Pay → Receive Documents
   (The Trustee Centre branch is sourced for #9–#16; #5 has it too but with a different
   sequence — pay *before* the combined audit-and-approval step, not after an isolated
   audit — see `payments.md` Category 3. #7 splits into two components with different fee
   treatment — see `payments.md` Category 4. #6's counterparty pays nothing — corrected
   2026-08-15, a documentation duplication that previously showed both parties paying;
   only the primary applicant pays in this group.)

   Trustee-Centre-only services, no online channel at all (#41)
   Visit Trustee Centre → Submit Documents → RERAN Enters & Audits → Pay → Receive Output
   (Added 2026-08-15, moved from the upfront group above. #41's own file documents no
   in-app submission path — see `payments.md` Category 2, which correctly notes #41's
   file needed no Section 9 fix because it never made the "before submission" claim in
   the first place; the correction here is to this document's own grouping, not to #41's
   file.)

   Tenancy (#23–#28, #40)
   Select Service → Enter Lease/Tenant Details → Upload Documents →
     [Online:] Pay → Submit
     [Trustee Centre:] Submit → RERAN Audits → Pay → Receive Certificate
   (#23, #24, #26 document the Trustee-Centre order correctly, and their Section 9 boilerplate
   has been corrected to match, per `open-questions.md` A1. #27 was restructured to document
   both channels explicitly, both fee-bearing on the counter channel's timing, per client
   confirmation (A5). #28 sources payment *after* RERAN's approval, not before, per A4 — now
   corrected. #40 has no fee at all — already correctly documented. #25 is fee-conditional,
   not upfront-or-after — see `payments.md` Category 6.)

   Power of Attorney (#29, #30, #42)
   Register (#29): Select Property → Enter Attorney Details → Define Scope → Pay → Submit
   Act on Behalf (#30): Select Property Owner → System Validates PoA → Select Service →
     [Wizard re-opens at that service's own pattern and payment rule] → Submit
   Cancel (#42): Visit Customer Centre → Submit Documents → RERAN Reviews
   (#30 has no independent fee of its own — corrected 2026-08-15, `payments.md` Category 9 —
   it inherits whichever fee and timing rule the selected service uses, which could be any
   of the groups above. #42's fee, output document, and completion criteria are not specified
   in source at all — the thinnest-specified service in the module, already flagged as such
   in its own file.)

   Property Information & Certificates (#31–#35)
   Search Property → Enter Request Details → Pay → Submit → Receive Document
   (#33 is the confirmed no-fee exception among this group — see A3. #28 belongs to Tenancy
   above, not here, despite being a certificate/valuation request in shape — its Who Can Apply
   spans Property Owner, Landlord, and Tenant, and `ui/README.md`'s Pattern I list groups it
   with the other certificate services for field shape even though its category placement is
   Tenancy Services.)

   Diaspora (#36–#37)
   Verify Identity (#36): Enter Personal Info → Upload ID → Biometric Check → Pay → Submit
   Remote Transaction (#37): Confirm #36 Complete → Select Transaction Type → [routes into
     the relevant service above, e.g. #5, #6, #23]
   (#37 is a routing layer over other services, not a separate transaction type of its own —
   its payment timing therefore inherits whatever the underlying selected service uses, same
   as #30 above — see `payments.md` Category 9.)

   Consumer Protection (#38–#39)
   Submit Complaint (#38): Select Category → Enter Details → Upload Evidence →
     Pay → Submit → RERAN Investigates → Resolution
   (Confirmed by client, A7 — the fee stands as originally documented; deters frivolous
   complaints.)
   Track Complaint (#39): Search → View Status (free, per `open-questions.md` A6 — the
     payment gate has been removed)

↓
Track Application Status (Feature #2, free) / Respond to Information Requests (Feature #3, free)
↓
Retrieve Output Document — pay-then-retrieve, retrieve-then-pay-at-counter, or retrieve
  directly with no payment, depending on which category above the service falls into
  (see `payments.md` for the full per-service breakdown — this module does not have a
  single uniform answer to "when does payment happen," unlike what a first read of the
  original Section 9 boilerplate across all 43 files would have suggested)
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

* Register and renew leases (#23, #24), as the **primary applicant**. The master table attributes row 82 to *Tenant*, not Landlord, and this module's own role-description text gives both roles overlapping "register/renew lease" language — a genuine conflict, resolved (not silently) by keeping Landlord primary and adding Tenant as a documented secondary applicant path in both files. See `open-questions.md` B1 for the full reasoning and the conflict check performed before adopting this resolution.
* Manage active leases (#25)
* Upload building details for leasing (#40) — the only service in the module specified in source as an off-platform, email-based process rather than an in-app form; already correctly documented that way in #40's own file.

**Sourced vs. extrapolated:** #23/#24 and #40 are sourced (rows 82, 85); #25 is extrapolated.

### Owner's Representative / PoA Holder

* Act on behalf of a property owner within the scope of a registered Power of Attorney (#30)

**Sourced vs. extrapolated — checked directly, not previously stated anywhere in this module (`open-questions.md` B5):** this role **never appears as a Responsible Role in any of the 41 sourced master-table rows for Groups E and F.** Its only direct documented service (#30) is extrapolated. It has a secondary, derivative presence — "Authorized Representative acting under a valid Power of Attorney" appears as an alternate applicant in nearly every sourced service's Who Can Apply section — but that presence is never the row's primary sourced actor. This role's entire standalone documentation rests on `roles-and-responsibilities.md`'s own worked example (David) and the extrapolated #29/#30, not on the master service table.

### Tenant

* Register/renew leases (#23, #24) as a **documented secondary applicant** alongside Landlord — see `open-questions.md` B1. The master table's own attribution of row 82 to Tenant is the reason this path exists at all, even though Landlord remains the primary applicant as currently designed.
* Cancel a tenancy contract (#27), jointly with Landlord
* Submit and pursue tenancy disputes (#26) — the module's clearest sourced role attribution: all ten consolidated dispute rows (72–81) name Tenant as the Responsible Role without exception
* Request rental valuation (#28), alongside Property Owner, Landlord, and prospective tenants

**Sourced vs. extrapolated:** #26's ten source rows are unambiguously sourced and unambiguously Tenant. #27's role attribution (Tenant, per row 83) is consistent with the file's current dual Landlord/Tenant framing. #28 (row 84) is sourced but its Who Can Apply list is broader than "Tenant" alone.

### Property Buyer / Investor

* Verify developers, projects, and properties before purchase (#1–#3)
* Participate as purchaser in Register Property Sale (#6)
* Diaspora-adjacent purchase flows via #37 where relevant

**Sourced vs. extrapolated — checked directly, not previously stated anywhere in this module (`open-questions.md` B4):** like Owner's Representative/PoA Holder above, this role **never appears as a Responsible Role in the sourced master-table rows.** Its documented service list is drawn almost entirely from the 11 extrapolated services (#1–#3 specifically). #6 is the one point of contact with a sourced row, and even there the master table's role column names Property Owner/Seller for the row, with "Purchaser" appearing only in the file's own workflow narrative, not the source's Responsible Role field. **The purchaser's own workflow no longer includes a payment step** — corrected 2026-08-15; the purchaser's role in #6 is confirmation and document upload only, matching #6's own corrected file.

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
