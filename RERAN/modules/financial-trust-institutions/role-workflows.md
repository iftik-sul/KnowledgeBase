---
project: RERAN
module: financial-trust-institutions
type: workflow
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/roles-and-responsibilities.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
tags:
  - financial-trust-institutions
  - workflow
---

# Financial & Trust Institutions Role Workflows

The path any user of a Group C institution account takes through the system, from login to logout. This describes the user's route, not the interface — screen-level detail lives in [ui/screens/](ui/screens/), access rules in [navigation.md](navigation.md).

**Proposed.** Group C's roles are described in the source; the post-login journey below is not — it is reconstructed from the services and screens this module documents.

**Confirmed 2026-08-14: access is unified, not role-gated.** Any of the four roles can perform any action in this module — service requests, internal certification, escrow requests, compliance reporting, settlement, staff records. Because of that, this document no longer describes four separate role-bound journeys. What follows is **one shared journey** covering the full range of actions available in the module. The per-role notes after it describe what each role *typically* does in practice — useful for context and for reading the audit trail — but they are **descriptive, not access-restrictive**: nothing stops a Mortgage Officer from certifying a record, or an Auditing Bureau Officer from filing a service request.

**Extended 2026-08-15.** `open-questions.md` A4 confirms the same principle for service ownership specifically, not just screen access: no service in the module is role-specific, for any of the 18 services. This was a client decision, not a re-derivation — an earlier position that assigned title & ownership transactions to the Mortgage Officer by default is superseded, and the per-role notes below have been corrected accordingly (see the Mortgage Officer section).

**Also 2026-08-15, twice.** `open-questions.md` B11 changes the payment timing for Service #1 (now upfront, not after RERA's decision) and confirms Service #2 carries no fee at all. A second pass, later the same day, found the Shared Journey's own #18 branch — and the diagram's complete absence of a branch for Services #12–#17 — needed the same fuller per-service check that fixed `payments.md`: **#18 (and #12) source RERA's decision *before* the counter payment**, which the diagram previously didn't show, making it read as if payment followed submission directly.

---

## The Shared Journey

```
Login
↓
View Dashboard
↓
[ Any of the following, in any order, any number of times, by any role: ]

   Service Request (mortgage / finance-lease lifecycle, #3–#11)
   Start Service Request → Select Service & Property → Enter Transaction Particulars →
     Attach Supporting Documents → Pay (shared platform gateway, upfront) →
     Submit to Internal Certification
   (Corrected 2026-08-14 — payment is now upfront, part of this branch, not a later separate
   step; see `open-questions.md` B1.)

   Title & Ownership Transaction (#12–#17)
   Start Service Request → Select Service & Property/Instrument → Enter Transaction Particulars →
     Attach Supporting Documents →
     #13–#17: Pay at Trustee Centre / Land Department counter → Submit to RERAN Review
     #12: Submit to RERAN Review → RERAN Decides → Pay at Trustee Centre Counter
   (Added 2026-08-15, second pass — this branch didn't previously exist in this diagram at all.
   #13–#17 pay before RERAN's decision, matching the general pattern; #12 is the one title &
   ownership service that pays after, alongside #18 below. See `payments.md` for the full
   per-service sourcing.)

   Internal Certification
   Open Internal Certification Queue → Review Request & Attached Documents →
     Certify → routes to RERAN Transaction Audit
     or Return → back to the filer with mandatory reason
   (No maker ≠ checker restriction: the acting user may certify a record they themselves filed.
   Applies only to #3–#11 — sourced two-gate pattern; #1, #2, #12–#18 route straight to RERAN.)

   Escrow Request (routed from Group B)
   Open Escrow Request Queue → Assess Solvency & Milestone Evidence →
     Upload Supporting Assessment → Certify, Return, or Request Information →
     Forward to RERAN Escrow Audit → Execute Approved Transfer

   Institutional Standing (#1, #2, #18)
   Review Approval Standing & Expiry →
     #1 (Approval/Renewal): Pay (shared platform gateway, upfront) → Submit Application
     #2 (Cancellation): Submit Application (no fee — nothing to pay)
     #18 (Contract Cancellation): Submit Application → RERAN Decides → Pay at Point of Service
   (Corrected 2026-08-15, twice. First pass: #1 previously paid after RERA's decision; it now
   pays upfront, the same pattern as #3–#11. #2 is confirmed to carry no fee at all, not merely
   unspecified in source. Second pass: #18's branch previously read "Submit Application → Pay
   at Point of Service," omitting RERAN's decision entirely and reading as if payment follows
   submission directly — it doesn't. #18 sources RERAN deciding first, then payment, the same
   order as #12 above. See `open-questions.md` B11 and `payments.md`.)

   Compliance Reporting
   Review Reporting Obligations → Examine Trust Accounts & Statements → Raise Findings →
     Prepare Compliance Report → Submit to RERAN → Escalate Material Findings

   Trust Account Register
   Maintain Trust Account Register & File Periodic Statements

   Staff Records
   Manage Staff Records (contact/attribution details only — there are no scopes left to provision)

↓
Track Application Status / Respond to RERAN Information Requests
↓
Retrieve Output Document — pay first, then retrieve (#1, #3–#11, #13–#17), RERAN decides then
  pay then retrieve (#12, #18), or retrieve directly, no payment involved (#2)
↓
Logout
```

**Corrected 2026-08-15, twice.** This closing step previously read "pay first, then retrieve (#3–#11, #12–#18) or confirm settlement, then retrieve (#1–#2, paid after approval)," reflecting the pre-B11 model where #1–#2 still paid after RERA's decision. A first pass fixed #1/#2 but collapsed #12–#18 into one "pay first, then retrieve" group, which is accurate for #13–#17 but not for #12/#18, where RERAN's decision precedes payment rather than the reverse. The line above now distinguishes all three timings.

Every branch is reachable by every logged-in user of the institution account. Which branches a given person actually uses is a matter of their role in practice, described below — not a system restriction.

---

## What Each Role Typically Does

### Mortgage Officer

The highest-volume role in the module, in practice.

* Mortgage lifecycle — registration, amendment, transfer, release (#3–#7)
* Finance lease lifecycle — registration, amendment, transfer, release (#8–#11)

**Corrected 2026-08-15** — this section previously also listed "Fund company registration (#12)" and "Title and ownership transactions where bank-originated (#13–#17)" as typical Mortgage Officer work. That attribution came from A4's earlier per-service re-derivation, which the client has since rejected outright (`open-questions.md` A4, confirmed 2026-08-15) — no service is role-specific, and the source never actually supported Mortgage Officer as the typical actor for #12–#17 either; that re-derivation was itself flagged as contested before the client's decision resolved it. The two bullets are removed rather than reworded, since there's no sourced or confirmed basis for attributing #12–#17 to this role even as a "typical practice" description — see each of `service-12` through `service-17`'s own Open Questions section for what, if anything, remains genuinely unresolved about who originates those transactions in practice.

### Institution Relationship Manager

Typically maintains the institution's standing and its people, in practice.

* Institutional approval and renewal (#1)
* Approval cancellation (#2)
* Contract cancellation (#18)
* Payment of the approval/renewal fee, upfront, before the application is lodged (#1 only). **Corrected 2026-08-15** — previously "Payment of approval/renewal fees after RERA's decision (#1–#2 only)"; `open-questions.md` B11 moves #1's payment upfront, the same as Services #3–#11, and confirms #2 carries no fee at all — there is nothing for this bullet to describe for #2 any more. Note that #18 (also typically this role's work) still pays after RERA's decision — see the Shared Journey above — this bullet describes #1's payment specifically, not a module-wide pattern. *(Also corrected 2026-08-14 — before that, this bullet read "Settlement account funding and settlement"; there is no standing account left to fund, see B1.)*
* Staff records and institution-wide oversight — no longer "permission scopes" to provision, since scopes are retired; see the note below
* Institution-wide oversight of outcomes

### Account Trustee

Typically works inbound escrow requests from the developer module.

* Account activation, account transfer, profit withdrawal, payment release, mortgage deposit and bank guarantee cancellation — all routed from Group B
* Milestone certification
* Trust account register maintenance and periodic audited statements

Answer A2 confirms from source rows 8–12 that this work happens inside the platform — the Trustee studies capability, uploads documents and sends them on — not externally with an outcome recorded afterwards. The SLA governing the assessment step is confirmed by answer A6 (client decision, 2026-08-15): the source's two-number reading (waiting time vs. delivery time) is correct, and no new SLA figure is needed. This is descriptive of typical practice, not an access restriction: under the unified model, any of the four roles can act on an escrow request.

### Auditing Bureau Officer

Typically provides independent assurance over trust accounts under the institution's trusteeship.

* Independent compliance reporting to RERAN
* Escrow audit of developer trust accounts
* Findings and escalation

**This role's definition was corrected once already**, per answer A1 (see [roles-and-responsibilities.md](roles-and-responsibilities.md) for the full history) — to remove internal certification of Mortgage Officer filings from its responsibilities, on the grounds that certification was a `certify` scope, not this role. That correction is itself now superseded by the 2026-08-14 unified-access decision: there is no `certify` scope any more, only an action any of the four roles may take, attributed by role in the audit trail. The practical upshot for this role is unchanged (it typically doesn't certify Mortgage Officer filings) — but the *reason* is different: not because it lacks a scope, but because certification isn't gated by role or scope at all, for anyone.

---

## Superseded By This Document

Until 2026-08-14, this document described four fully separate role journeys, plus a "Scope-Driven Variations" section in which holding the `certify`, `settlement`, or `admin` permission scope inserted extra steps into a person's journey, and a user's route forked depending on whether they held `certify` for the specific record they were looking at. That forking model is retired along with the scopes themselves. See [navigation.md](navigation.md) for the confirmed unified-access model this document now follows.
