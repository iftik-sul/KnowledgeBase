---
project: RERAN
module: individual-user
type: decision
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/individual-user/roles-and-responsibilities.md"
  - "RERAN/modules/individual-user/services-overview.md"
  - "RERAN/modules/individual-user/payments.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_prd_v1.0.md"
tags:
  - individual-user
  - open-questions
  - decisions
  - client
---

# Individual User — Questions and Proposed Answers

Fifteen questions arose from checking all 43 service-flow files individually against their sourced rows (`RERAN_service_flows_v2.md` rows 72–112) and against `roles-and-responsibilities.md`'s own worked examples, per the standing instruction not to accept the master table's role column, or a service file's stated position, at face value. Each carries a **proposed answer** to build against, per the standing preference for proposed positions over deferring to the client.

**How to read this:** each answer states a recommendation, the reasoning, confidence, and what breaks if it's wrong. Confidence follows the same scale used in Group C's `open-questions.md`:

| Level | Meaning |
| :---- | :---- |
| **Sourced** | The source material answers this directly |
| **High** | A strong inference, or the only option that survives contact with the source |
| **Medium** | A reasonable design judgement; a different answer would also be defensible |
| **Client data** | Cannot be reasoned to; only RERA holds the answer |

**Scope note:** post-login functionality only, matching the rest of this project.

---

## A. Payment Timing

### A1. Should the Section-9 boilerplate be corrected for #23, #24, #26, and #41?

**Yes — this isn't really a question, it's a bug.** Three of these four files (#23, #24, #26) already document the correct payment order in their own Processing Workflow section; only their Section 9 header claim is wrong. #41 already has both parts correct. This is the same two-sections-of-the-same-file-disagreeing pattern in three places, not three separate design questions.

**Confidence:** Sourced. The correct order is already written down in each file; it just needs to be copied into the section that currently contradicts it.

**Affects:** `payments.md` Category 2; Section 9 of service-flow files #23, #24, #26.

### A2. Do #5 and #9–#16 need a documented Trustee Centre payment channel?

**Proposed: yes, for #9–#16; #5 needs its existing Option 1 reordered rather than a channel added.**

#9–#16 either have no counter-channel path documented at all (#9) or inherit row 86's "-V" Trustee Centre pattern by explicit source cross-reference ("same as sale registration") without that pattern ever being written into the files (#10–#16). Since Service #6 (which row 86 directly sources) already documents both an online path and implies the Trustee Centre alternative exists, the sibling services #10–#16 dropping that second channel looks like an oversight in extending #6's template to its neighbours, not a deliberate simplification.

#5 is different: it already has an Option 1 (Customer Center) section, but that section's step order doesn't match row 106's actual sequence — payment there was written to look like the "pay after audit" pattern common to rows 88–95, when row 106's own wording is "...pay, transaction audited and approved" (one combined post-payment step, not an audit gate before payment). This isn't a missing channel, it's a misremembered one.

**Confidence:** Medium-high. The channel-inheritance logic is sourced (services-overview.md's own note that #10–#16 come from "-V: Same as sale registration"); the specific fix each file needs is a judgement call about how literally to extend that inheritance.

**If wrong:** if the online-only model for #9–#16 is an intentional platform redesign rather than an oversight, no fix is needed there — but #5 still needs its Option 1 reordered regardless, since that reading doesn't rescue #5's internal sequence.

**Affects:** `payments.md` Category 3; Processing Workflow sections of #5, #9–#16.

### A3. Do #17, #18, #33, and #7's Owner/Entity-Amendment component actually carry no fee?

**Proposed: yes, no fee — matching the standard Group C used for its own Service #2.**

None of the four sourced rows involved (98, 99, 111, 107) contain a payment step anywhere in their workflow description, and in three of the four cases (#17, #18, #7-component) the row sits directly beside sibling rows in the same source cluster that *do* name a "pay" step at the equivalent point in an otherwise near-identical workflow shape — the same contrast-with-neighbours reasoning that made Group C confident #2 was a genuine no-fee case rather than an omission.

**Confidence:** High for #17/#18 (both flanked by fee-bearing siblings #19–#22 in the same Title & Land Registration cluster). Medium for #33 (Request Property Survey) and the #7 Owner/Entity component, since neither sits in as tight a same-shape cluster to contrast against.

**If wrong:** four services gain a checkout step that currently doesn't exist in their documentation; low build cost either way since the payment UI pattern is shared platform-wide.

**Affects:** `payments.md` Category 4; Section 8/9 of #17, #18, #33; #7's Section 8/9 split into two components.

### A4. Does #28's payment timing move to after RERA's decision?

**Yes — this is sourced, not inferred.** Row 84 states outright: *"Pay fees after approval."* There is no ambiguity to resolve.

**Confidence:** Sourced.

**Affects:** `payments.md` Category 2; #28's Section 9 and Processing Workflow.

### A5. Is the online path for #27 (Cancel Tenancy Contract) genuinely fee-free?

**Proposed: treat as an open question requiring client input, not resolved here.** Row 83's online sub-channel lists no payment step at all, while its counter sub-channel does. Two readings are equally defensible: RERAN made online self-service cancellation free as an incentive (matching the platform's general push toward online channels per Group C's C2 finding), or the source simply omitted a step present in practice. Nothing in the source or in this module's other services settles which.

**Confidence:** Client data. Genuinely unknown either way.

**Affects:** `payments.md` Category 5; #27's Section 9.

### A6. Should #39 (Track Complaint) charge a fee to view status?

**No.** Feature #2 (Track Application Status), which #39 functionally specialises, is explicit that tracking is free once an application is submitted — a principle this module already applies to every other trackable service. #39 currently contradicts its own platform's shared feature for no sourced reason (it's extrapolated, so there's no row to defend the fee).

**Confidence:** High. This isn't a source dispute; it's an internal-consistency fix against a rule the module has already committed to elsewhere.

**Affects:** `payments.md` Category 7; #39's Section 8/9, Processing Workflow (removing the payment gate before "Retrieve Complaint Details").

### A7. Should #38 (Submit Complaint) carry a fee at all?

**Genuinely open — no proposed resolution.** Unlike A6, there's a real argument on both sides: RERAN may want a nominal fee to deter frivolous complaints (the same logic that justifies court filing fees), or Group F's stated purpose as a consumer-protection group may argue for a free filing channel, especially since #26 (Submit Tenancy Dispute) already exists as the fee-bearing formal-adjudication path for disputes that need one. Because #38 is extrapolated with no source row either way, and because the two readings lead to materially different UX (a paywall in front of every complaint vs. none), this is flagged for the client rather than defaulted.

**Confidence:** Client data.

**Affects:** `payments.md` Category 8; #38's Section 8/9 if the fee is removed.

---

## B. Role Attribution

### B1. Is Register Lease / Renew Lease (#23/#24) a Landlord service or a Tenant service?

**Genuine conflict, not silently resolved. Proposed: Landlord as primary applicant, matching the files as currently written — but flagged, not asserted with full confidence.**

The master table's Responsible Role column for row 82 says **Tenant**. Both service-flow files (#23, #24) frame the entire workflow around the **Landlord** — "Registered Property Owner (Landlord)" as the primary applicant, with the tenant appearing only as a data field, not a workflow participant. `roles-and-responsibilities.md` doesn't settle this cleanly either: the Landlord's responsibilities list includes "Create and renew lease records," and Grace's worked example has her registering and renewing leases directly — but the Tenant's responsibilities list *also* includes "Register tenancy information" and "Renew lease records," verbatim overlapping language.

Three readings are possible: (a) the master table's role column reflects which *source category heading* the row sits under ("TENANT – Real Estate Rental Services") rather than a considered per-service actor assignment — the same kind of coarse, category-level default Group C's A4 found in its own role column, just manifesting through the category grouping instead of the column itself this time; (b) both roles genuinely can initiate registration (a landlord registering a lease they're renting out, or a tenant self-registering a lease they've signed for their own protection, especially plausible given RERAN's consumer-protection mandate), meaning this should be a joint/either-party service like #6's seller/purchaser model rather than single-actor; or (c) the files are simply wrong and Tenant is the primary actor.

**Recommendation:** keep Landlord as the current primary applicant (matches the worked-example precedent and the practical real-world convention that whoever holds the property registers the tenancy against it), but add Tenant as a secondary path — a tenant-initiated self-registration option — rather than treating the master table's Tenant attribution as simply incorrect. This mirrors reading (b) rather than picking (a) or (c) outright.

**Confidence:** Medium. Unlike Group C's A4 (which the client resolved directly), this hasn't been put to the client yet, and the roles-and-responsibilities.md ambiguity means the "safe" default choice isn't as clear-cut as it looked before checking.

**If wrong:** if the client confirms Tenant is the sole intended actor, #23/#24 need a substantial rewrite (currently Landlord-only in every field, form, and business rule) rather than an additive fix.

**Affects:** `roles-and-responsibilities.md`'s Landlord/Tenant responsibility lists (currently genuinely overlapping, which is itself worth flagging to the client rather than living with); #23 and #24's Who Can Apply, Required Information, and Processing Workflow sections; `role-workflows.md`.

### B2. Is the master table's "Property Owner/Seller" default for rows 85–112 as unreliable as Group C's role column turned out to be?

**Checked directly — proposed answer: no, it holds up, unlike Group C's case.** Group C's A4 found the source's role column assigned the Mortgage Officer to services with no plausible connection to mortgage lending (heirs' sales, title-deed issuance) — a genuine mismatch between the assigned role and the transaction's substance. Checking the equivalent pattern here: rows 96–105 (Heirs Ownership, Community Land, Partners Division, Industrial/Commercial Land, Indemnity, Exchange) are all uniformly attributed to Property Owner/Seller, and in every one of these cases the applicant genuinely *is* someone establishing or exercising an ownership-adjacent claim over the property — an heir becoming the new owner-of-record, a community's authorized representative registering title, a co-owner dividing joint ownership. Unlike Group C's Mortgage Officer being assigned services with no lending nexus, "Property Owner/Seller" for these rows describes the applicant's substantive relationship to the transaction, not a coarse category default.

The one row this reasoning doesn't cleanly cover is **row 97 (PoA cancellation)** — but on reflection that also holds: only the original grantor (the Property Owner) has legal standing to revoke a Power of Attorney they issued, so Property Owner/Seller is the only role that makes sense there too.

**Confidence:** High, as a check performed rather than an assumption relied on. Genuinely different conclusion from Group C's A4 despite superficially similar-looking master-table uniformity — worth recording precisely because it would have been easy to pattern-match "uniform role column = same problem as Group C" without checking.

**Affects:** No document changes — this confirms the current attribution across #5, #7 (property-info component), #17–#22, #35, #41–#43 is sound and needs no correction.

### B3. Do the applicant categories named in individual service files (Legal Heir, Community Representative, Financial Institution, Property Management Company) need to become new platform roles?

**Proposed: no — three of the four are status descriptions within an existing role, one is a genuine cross-module error needing removal.**

- **Legal Heir / Court-appointed Administrator (#19):** describes the applicant's *status entering* the transaction — the outcome of #19 is precisely that this person becomes the registered Property Owner/Seller of record. Not a new role; a precondition on who may currently invoke the Property Owner/Seller role for this specific service.
- **Community Representative / Leader (#20):** same pattern — acting on behalf of a collective ownership structure, but the resulting registration still vests in an owner-type entity. Not a new role.
- **Financial Institution (#34, as a requester of a valuation):** this is Group C reaching into an Individual User service as a *requester*, not Group C acting as a Group C role inside this module. Worth a one-line clarifying note in #34 rather than a role change.
- **Property Management Company (#23, #24, #25):** this one is a genuine problem, not a status description. "Property Management Company" is Group D's **Property Management Officer** role (`real-estate-service-companies` module), not an Individual User concept at all. Its presence in #23/#24/#25's Who Can Apply sections looks like cross-module leakage, possibly copied from Group D material during drafting. **Recommend removing it** from all three files, leaving "Authorized Property Representative" (which is already a legitimate Individual User concept, covering PoA holders and similar) to cover delegated management without implying a Group D corporate actor can act as an Individual User.

**Confidence:** High on the Property Management Company removal (a clear cross-module category error, the same kind of mistake Group C's A1 corrected for "internal auditor" vs. "Auditing Bureau Officer"). Medium on treating the other three as status descriptions rather than needing their own role entries — a defensible design choice, not a certainty.

**Affects:** #23, #24, #25's Who Can Apply sections (remove Property Management Company); no change needed to `roles-and-responsibilities.md`'s six-role list.

### B4. How much of Property Buyer/Investor's and Diaspora Investor's documented behaviour actually traces to source, versus extrapolation?

**Checked, not previously flagged: almost none of it traces to a master-table row.** Across all 41 sourced rows for Groups E and F (72–112), the Responsible Role column names only three values: Property Owner/Seller, Landlord, and Tenant. **Property Buyer/Investor and Diaspora Investor never appear as a Responsible Role in the source table at all.** Their entire documented presence in this module rests on the 11 extrapolated services — #1–#3 (verification, tied to Buyer/Investor by role-description inference) and #36–#37 (diaspora, tied to Diaspora Investor the same way).

This isn't necessarily wrong — `services-overview.md` already discloses the sourced/extrapolated split at the service level — but it hasn't previously been stated at the *role* level: two of the module's six roles are almost entirely a documentation team's inference from role-description prose (roles-and-responsibilities.md's own "Purpose" paragraphs), not a role the source's own workflow table ever assigns a service to.

**Confidence:** Sourced, as a factual observation about what is and isn't in the master table. Not a problem to fix — a provenance note worth surfacing so nobody later treats Buyer/Investor's or Diaspora Investor's service list as more source-grounded than it is.

**Affects:** `role-workflows.md` — this note belongs in each of those two roles' sections, matching how Group C's A4 answer documents provenance directly in the affected role sections rather than only in this file.

### B5. Same question for Owner's Representative / PoA Holder.

**Same finding.** This role never appears as a Responsible Role in the sourced master-table rows either. Its documented service list (#29, #30) is entirely extrapolated. It also appears constantly as a *secondary* applicant category — "Authorized Representative acting under a valid Power of Attorney" — sprinkled through nearly every sourced service's Who Can Apply section, which gives it more textual presence in the module than #4's role-column tally alone would suggest, but that presence is all secondary/derivative, never a row's primary Responsible Role.

**Confidence:** Sourced, same basis as B4.

**Affects:** `role-workflows.md`.

---

## C. Payment Artefacts and Mechanisms

### C1. Does Service #6's Wallet Account reference apply module-wide?

**Open — flagged, not resolved.** Row 86's purchaser workflow names "pay via Wallet Account" as the payment step. No other service-flow file in this module mentions a wallet. Two readings: the wallet is #6's own purchaser-specific mechanism (property purchase being the highest-value, most naturally wallet-suited transaction in the module), or it's the intended default payment method for the whole module and every other file's generic "Complete Payment" step should be understood to mean the wallet unless stated otherwise. This also connects to Group C's still-open B2 question about whether the wallet primitive (P-22) is shared build across modules.

**Confidence:** Client data.

**Affects:** `payments.md`'s Settlement Mechanism section; potentially every service's Payment UI screens once `ui/` work begins.

### C2. Does "Fee Balance" mean the same thing here as it meant in Group C's now-retired model?

**Proposed: no — it can't, because the standing-account structure it described in Group C never existed for individual users in the first place.** Group C's B9 found "Fee Balance" was evidence of a since-retired standing pre-funded account. Individual User has no institutional account structure of any kind — there's no entity here analogous to a bank's settlement account. The term most plausibly denotes an amount-due or amount-paid line on a single transaction's receipt.

**Confidence:** Medium-high. The retired-account reading is confidently ruled out (there's nothing here for it to describe); the "single-transaction balance line" reading is the most natural remaining one but isn't independently confirmed by source.

**Affects:** `payments.md`'s Payment Artefacts section; no service-flow file changes needed unless the client's answer changes what the receipt UI should show.

---

## Summary

| Area | Questions | Proposed / Resolved | Genuinely open (client data) |
| :---- | :---: | :---: | :---: |
| A. Payment Timing | 7 | 5 | 2 (A5, A7) |
| B. Role Attribution | 5 | 5 | 0 |
| C. Payment Artefacts | 2 | 1 | 1 (C1) |
| **Total** | **14** | **11** | **3** |

### The client-facing list

1. **A5** — is #27's online cancellation path genuinely fee-free, or was a fee step omitted from the source?
2. **A7** — should Submit Complaint (#38) carry a fee at all, given Group F's consumer-protection purpose?
3. **C1** — is Service #6's Wallet Account the module's default payment method, or specific to that one purchaser flow?

Everything else above carries a proposed position to build against, consistent with the standing instruction to propose rather than default to "needs client input" wherever the source or the module's own internal consistency gives a defensible answer.
