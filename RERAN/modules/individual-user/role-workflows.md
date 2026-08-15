---
project: RERAN
module: individual-user
type: workflow
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/individual-user/roles-and-responsibilities.md"
  - "RERAN/modules/individual-user/navigation.md"
  - "RERAN/modules/individual-user/payments.md"
  - "RERAN/modules/individual-user/open-questions.md"
tags:
  - individual-user
  - workflow
---

# Individual User Role Workflows

The path a person takes through the platform, from login to logout, for each of this module's six roles. This describes the user's route, not the interface — screen-level detail will live in `ui/screens/` once that work starts (explicitly out of scope for this document, per this chat's brief).

**A note on payment timing before reading any journey below:** every payment step in this document reflects the timing established in `payments.md` — including the Model B (pay-after-audit-before-decision), Model C (pay-after-decision), and no-fee cases — **not** the currently-published Section 9 line in the individual service-flow files, which `open-questions.md` B2 documents as wrong for at least fifteen of them. Once that correction pass happens, this document will already be consistent with it; until then, this document and the 43 service files will disagree with each other on exactly the items B2 lists, and the service files are the ones that need to change.

**A second note on structure:** because one account can hold several roles at once (`roles-and-responsibilities.md`'s central principle for this module), the six sections below are not mutually exclusive journeys the way Group C's four roles were before its unified-access decision. They describe what a person *typically* does when acting in that capacity, and a single session may move between several of them without any mode switch — consistent with `navigation.md`'s "one sidebar, content scoped by relationship" model.

---

## Property Owner / Seller

The role with the largest service surface in this module — Section A2 of `open-questions.md` notes the master table defaults nearly every Group E row to this role, and while several of those defaults are too coarse to trust as-is, ownership and transaction services genuinely do cluster here more than anywhere else.

```
Login
↓
View Dashboard (role summary shows properties owned, in-progress applications)
↓
[ Any of the following, in any order: ]

   Verification (before any transaction, #1–#3)
   Verify Developer / Verify Development Project / Verify Property →
     Pay upfront → View Result

   Ownership Establishment & Transfer (#4–#9, #41, #43)
   Register Property Ownership → Pay upfront → Submit → RERAN Review → Approved
   Transfer Property Ownership → Pay upfront (online) — Trustee Centre channel pays
     after audit, see `payments.md` — → Submit → Approved → Certificate Issued
   Register Property Sale (#6) → two-sided: Seller initiates and pays (App channel,
     upfront) or Trustee Centre channel (pays after audit) → Purchaser confirms and
     pays their side via Wallet Account or gateway → RERAN Review → Approved
     (Register Property Sale does not itself transfer ownership — Business Rule 8
     of that service requires a separate Transfer Property Ownership application
     afterward)
   Register Sale of Mortgaged Property (#8) → coordinates with Mortgage Institution
     for the Mortgage Release Letter (cross-module dependency on Financial & Trust
     Institutions Service #6) → Pay upfront → RERAN Review → Approved
   Register Gift Transfer (#9) → Trustee Centre only, sourced; pays after audit
     (`payments.md` flags the current file's online-first framing as unsourced —
     see `open-questions.md` B2) → Recipient confirms → Approved
   Register Company (#41) → Trustee Centre only, no online path sourced → pays
     after audit → Reference number issued by email

   Lease-to-Own & Usufruct Lifecycle (#10–#16)
   Register / Transfer / Release / Amend Lease-to-Own, Register / Amend / Terminate
     Usufruct Right → each follows Service #6's two-channel pattern by source
     cross-reference (App: pay upfront; Trustee Centre: pay after audit — see
     `payments.md`'s channel-split section, currently undocumented in these seven
     files) → counterparty confirms where applicable → RERAN Review → Approved

   Title & Land Registration (#17–#22)
   Grant Registration → Grant Completion (no fee, both — see `payments.md`)
   Register Heirs Ownership / Community Land / Partners Division / Industrial &
     Commercial Land Ownership → pay before RERAN's final audit/approval →
     Approved → Title Documents Issued

   Update & Amend Ownership Records (#7)
   Update Property Ownership Information → two distinct branches: Owner/Entity
     Information Amendment (no fee, Trustee Centre only) or Property Information
     Amendment (fee, online upfront / Trustee Centre after audit) — see
     `payments.md`

   Power of Attorney — as Grantor (#29, #42)
   Register Power of Attorney → Pay upfront → Approved → Attorney gains scoped
     access to Act on Behalf of Property Owner (#30)
   Cancel Power of Attorney → thinly sourced (`service-42`'s own file flags this),
     no fee documented → Submitted → *(source ends before a documented outcome)*

   Property Certificates (#31–#35)
   Request Detailed Real Estate Statement / To Whom It May Concern Certificate →
     pay before request processed (online); Trustee Centre channel pays after the
     identity check, per `payments.md` (lower confidence than the audit-gated
     services above)
   Request Property Survey (#33) → no fee sourced → multi-day field process →
     Report Issued
   Request Property Valuation (#34) → pay upfront, sourced explicitly for the
     online channel → multi-day process → Report Issued
   Request Full / Partial Indemnity (#35) → pay before final audit → Certificate
     Issued

↓
Track Application Status (Feature #2, free) / Respond to Information Requests
  (Feature #3, free) / Resubmit Returned Applications (Feature #4, free)
↓
Retrieve Output Document — timing depends on which payment model applied to the
  specific service used (see `payments.md`) — pay-then-retrieve for most title
  and ownership services; retrieve-then-be-invoiced does not occur anywhere in
  this module's sourced services except where flagged as an open question
↓
Logout
```

---

## Landlord

Second-largest surface, and the role at the center of `open-questions.md` A1's unresolved conflict with Tenant over lease registration/renewal.

```
Login
↓
View Dashboard (role summary shows active leases as landlord)
↓
[ Any of the following: ]

   Building Intake (#40)
   Upload Building Details for Leasing → email-based, off-platform intake, no fee
     sourced → RERA staff review and approve → building available for lease
     registration

   Lease Lifecycle (#23, #24, #25)
   Register Lease → per `open-questions.md` A1 (proposed, not confirmed): Landlord
     initiates, Tenant confirms → Trustee Centre channel pays after initial audit,
     before certificate issuance (matches the file's own Option 1 workflow); Online
     channel pays at submission → Certificate Issued
   Renew Lease → same proposed initiator split and same payment-timing pattern as
     Register Lease
   Manage Lease → ongoing workspace; fee only for actions that carry one
     (Section 9's conditional-fee model, already correctly documented)

   Tenancy Termination (#27)
   Cancel Tenancy Contract → Trustee Centre channel pays after audit; Online/App
     channel's own source shows no payment step at all (`payments.md` flags this
     as unresolved, not yet reflected in the current file) → Cancellation
     Confirmed

   Valuation (#28)
   Request Rental Valuation → **pays only after RERAN's approval** (Model C, the
     single clearest payment-timing finding in this module) → Report Issued

   Disputes, as respondent (#26)
   Submit Tenancy Dispute → available to Landlord as well as Tenant (Section 4 of
     the current file already lists both) → pays after initial audit, before the
     hearing/conciliation stage (matches the file's own Option 1 workflow) →
     Resolution / Judgment Issued

↓
Track Application Status / Respond to Information Requests
↓
Logout
```

---

## Owner's Representative / Power of Attorney Holder

The only role in this module whose entire journey is gated by another person's account state before it can begin at all.

```
Login
↓
Select "Act on Behalf of Property Owner" (#30)
↓
System Validates the Registered Power of Attorney (#29) — checks it is active,
  unexpired, unrevoked, and that the requested service falls within its scope
↓
[ If validation fails: Authorization Failed — journey ends here, no service
  proceeds. This is the one hard gate in this module comparable to Group C's
  approval-expiry gate for Service #1. ]
↓
[ If validation succeeds: ]
Select Represented Property Owner → Select Property → Select the Underlying
  Service (any service the Property Owner or Landlord roles could themselves
  perform, per Section 3's "same legal effect as if performed directly by the
  property owner" business rule) → the underlying service's own payment timing
  applies unchanged — Act on Behalf of Property Owner does not introduce a
  separate payment model, it inherits whichever one the selected service uses
↓
RERAN Review → Approved → Output delivered, attributed to both the represented
  owner and the acting representative (Business Rule 8 of Service #30 requires
  this dual attribution be recorded in every transaction)
↓
Logout
```

**Note on David's worked example** (`roles-and-responsibilities.md`): "renews leases, submits property applications, and completes ownership transactions on his mother's behalf" maps directly onto this journey — Renew Lease, Register Property Ownership-family services, and Transfer Property Ownership are all reachable through this single gated entry point, not as separate PoA-specific services.

---

## Tenant

Smallest sourced service surface of the six roles, and the role at the center of `open-questions.md` A1.

```
Login
↓
View Dashboard (role summary shows active tenancies)
↓
[ Any of the following: ]

   Lease Confirmation (#23, #24) — pending A1's resolution
   Confirm Registered Lease / Confirm Renewed Lease → tentative role under the
     proposed A1 answer: confirms, does not initiate — see the Landlord section
     above and `open-questions.md` A1 for the unresolved three-way conflict this
     rests on

   Rental Valuation (#28)
   Request Rental Valuation → available to Tenant as well as Landlord/Owner
     (Section 4 already lists both) → pays only after approval (Model C)

   Disputes (#26) — the role's primary sourced activity
   Submit Tenancy Dispute → covers all ten consolidated dispute types (Dispute
     Case, Preliminary Suit, Appeal, Grievance, Petition to Reconsider, Order on
     a Petition, Offer & Deposit, Performance Order, Grievance Against
     Performance Order, Execution Case) → pays after initial audit, before the
     hearing/conciliation/session stage in every one of the ten source rows
     (72–81) — this is the most consistently-sourced payment pattern found
     anywhere in this module, all ten rows share the identical shape
   → Assigned → Attend Hearing/Conciliation (where applicable) → Resolution /
     Judgment Issued

↓
Track Application Status / Respond to Information Requests
↓
Logout
```

**Note on Sarah's worked example**: "submits a dispute... uploads supporting documents, and tracks the resolution process" maps directly onto the Submit Tenancy Dispute journey above and nothing else — the worked example itself doesn't touch lease registration, which is part of why A1 is a genuine ambiguity rather than something resolvable from the worked examples alone.

---

## Property Buyer / Investor

```
Login
↓
View Dashboard
↓
[ Any of the following, typically in this order for a first-time purchase: ]

   Pre-Purchase Verification (#1–#3)
   Verify Developer → Verify Development Project → Verify Property → each pays
     upfront, real-time lookup, no channel split sourced

   Purchase Participation (#6)
   Receive Booking Reference from Seller → Enter Booking Reference → Verify OTP →
     Review & Accept Property Details → Pay (App: at submission, via Wallet
     Account per row 86 — see `payments.md`'s Settlement Mechanisms section) →
     Submit Response → RERAN Review → Approved

   Post-Purchase Follow-Through
   Transfer Property Ownership (#5) → the buyer becomes a Property Owner/Seller
     from this point forward; Register Sale of Mortgaged Property (#8) if the
     purchase involves clearing a seller's existing mortgage first

   Complaints (#38, #39)
   Submit Complaint → pays upfront in the current files, though `open-questions.md`
     B3 flags this as a design decision worth reconsidering, not a sourced
     requirement → Track Complaint → **currently charges a fee to track, which
     `open-questions.md` B3 flags as inconsistent with Feature #2's free tracking
     for every other application type — proposed for correction, not yet
     resolved**

↓
Track Application Status
↓
Logout
```

**Note on Michael's worked example**: "verifies that the developer and project are registered... monitors construction progress... receives updates until completion" — the "monitors construction progress" step doesn't map to any sourced service in this module; it's closest to Group B's project-status services, which this role would need to reach cross-module (not documented as a gap here since it belongs to a different module's scope, but worth flagging as a thin spot in this role's own documented journey).

---

## Diaspora Investor

```
Login
↓
Complete Remote Identity Verification (#36) — pays upfront, gates every other
  remote-specific action, unlike any other role's Section 5 prerequisite in this
  module (see `navigation.md`'s Diaspora Access section)
↓
[ Once verified: ]

   Remote Property Transactions (#37)
   Select Transaction Type → any transaction another role could perform in
     person, executed remotely → pays upfront → RERAN Review → Approved

   Representative Delegation
   Register Power of Attorney (#29), naming a local representative → the
     representative then operates under the Owner's Representative / PoA Holder
     journey above on the diaspora investor's behalf — this is the primary
     mechanism `roles-and-responsibilities.md`'s Aisha worked example describes
     ("appoints her brother as her authorized representative")

   Everything else available to Property Owner/Seller, Landlord, or Buyer/
   Investor, once verified, executed through the Remote Property Transactions
   gateway rather than those roles' own direct entry points

↓
Track Application Status (remotely, no location dependency sourced)
↓
Logout
```

---

## What's Confirmed vs. Proposed in This Document

Every payment-timing claim above is sourced to `payments.md`, which is itself sourced per-service to the master table rows cited there. The role-initiator claims for Register/Renew Lease are explicitly flagged as pending `open-questions.md` A1, not confirmed. The Tenant-as-confirming-party pattern for lease services is a proposal built to be internally consistent with A1's proposed answer, not a separate independent finding — if A1 resolves differently, this document's Tenant and Landlord sections both need revision, not just one of them.
