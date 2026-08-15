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

# Individual User (Groups E+F) — Questions and Proposed Answers

Built the same way Group C's equivalent document was: each question carries a proposed answer to build against unless told otherwise, with a confidence level and what breaks if it's wrong. This module's questions arose from checking all 43 service-flow files individually against the master service table (rows 72–112) before writing `payments.md`, `navigation.md`, and `role-workflows.md` — per the standing instruction to check every service and every role attribution individually rather than trust a pattern from a neighbor.

| Level | Meaning |
| :---- | :---- |
| **Sourced** | The source material answers this directly |
| **High** | A strong inference from the source |
| **Medium** | A reasonable design judgement; a different answer would also be defensible |
| **Client data** | Cannot be reasoned to; only RERA/the client holds the answer |

**Scope note:** post-login functionality only, matching the project-wide scope rule. This document does not resolve the UI/screen-level questions this module will need once UI work starts — those are out of scope for this chat's brief.

---

## A. Roles

### A1. Register Lease (#23) and Renew Lease (#24) — is this a Landlord service or a Tenant service?

**Real conflict, not resolved here — proposed answer: Landlord-initiated, with Tenant confirmation, but flagged for client confirmation because the source itself disagrees with the current documentation.**

Three sources disagree with each other:

1. **The master service table** files row 82 under the source category "TENANT – Real Estate Rental Services" and names **Tenant** as the Responsible Role.
2. **`roles-and-responsibilities.md`'s own responsibility lists** give *both* roles overlapping duties here: Landlord — "Register rental properties, Create and renew lease records"; Tenant — "Register tenancy information, Renew lease records." The worked examples don't resolve it either — Grace (Landlord) "registers each lease agreement... renews tenancy records," which reads as the same action row 82 describes, while Sarah (Tenant)'s worked example is about disputes, not registration.
3. **The current Service #23/#24 files** frame the entire service around the Landlord, with "Property Management Company acting on behalf of the owner" also listed as an eligible applicant — a role that doesn't appear in `roles-and-responsibilities.md`'s six Individual User roles at all (it's a Group D role).

**Reasoning toward a proposed answer:** row 82's own workflow text doesn't name who initiates — "submit docs, enter system and audit, pay, receive contract registration certificate" reads equally well from either party's perspective. But the master table's *category* label ("TENANT – Real Estate Rental Services") most plausibly reflects that the *source jurisdiction's* system had tenants self-register their own leases for rental protection purposes — consistent with Group F's platform sub-system being named "RERA Mobile App, Tenancy (Tenant)" in the Groups & Roles table, versus Group E's "Title-Deed & Transaction, Tenancy System, **Owner Self-Service (App)**." Both groups have a tenancy-adjacent sub-system, which is itself evidence the source intended *both* roles to have some form of tenancy access, not that one is right and one is wrong.

**Proposed:** the Landlord registers and renews the lease (matching the current files and Grace's worked example, and matching that only the Landlord holds the underlying property registration this service modifies), with the Tenant able to *view and confirm* the registered lease but not *initiate* it — the same "confirm, don't initiate" pattern Service #6 (Register Property Sale) already uses for its purchaser side. This resolves the ambiguity without discarding either role's documented responsibilities: Tenant's "register tenancy information" responsibility is read as encompassing tenant-side confirmation, not independent initiation.

**Confidence:** Medium. This is a genuine three-way disagreement between source table, role descriptions, and current documentation, not a case where one source is clearly right. **Flagged for direct client confirmation, same standard as Group C's A4.**

**Affects:** `service-23-register-lease.md` and `service-24-renew-lease.md` Section 4 (add Tenant as confirming party, remove "Property Management Company" or relocate it to a cross-module note); `role-workflows.md` (this document, built assuming the proposed answer above); `roles-and-responsibilities.md`'s Landlord and Tenant responsibility lists (add a cross-reference noting the overlap and how it's resolved, rather than leaving two roles silently claiming the same action).

### A2. The master table's role column looks like a category-level default, not a per-service judgement — same finding as Group C's A4

**Confirmed pattern, not yet a client decision — flagged the same way Group C flagged A4 before its client resolution.**

Twenty-six of the twenty-seven Group E rows (86–112, excluding row 85) name **Property Owner / Seller** as the Responsible Role — including heirs' ownership registration, community land registration, partners division, industrial/commercial land ownership, property surveys, valuations, and certificate requests, none of which obviously belong to a "seller" specifically. This is the same shape Group C's A4 found: a source column giving one role the overwhelming majority of a group's services regardless of whether the underlying transaction fits that role's description.

Unlike Group C, this module's current service-flow files mostly **already correct for this** — most files list "Joint Property Owner," "Authorized Representative acting under a valid Power of Attorney," and similar broadened applicant sets in their own Section 4, rather than repeating the master table's narrow column verbatim. That's the right instinct and shouldn't be undone. What it hasn't done is **name applicant categories that don't map to any of the six roles in `roles-and-responsibilities.md` at all** — see A3 below.

**Confidence:** High that the master table's role column is a coarse default here too, by direct analogy with Group C's confirmed A4. **Proposed:** treat the six roles in `roles-and-responsibilities.md` as attribution categories applied per-service by the service-flow files' own Section 4 (already largely done), not by the master table's role column — i.e., no correction needed to the *files*, but `roles-and-responsibilities.md` and `role-workflows.md` should say explicitly that the master table's role column is not the authority for this module, the same way Group C's navigation.md now says role is "attribution only." Not yet put to the client; recommend bundling with A1 above since both concern the same underlying question of how much weight the master table's role column deserves in this module.

### A3. Some services name applicants that aren't any of the six documented roles

**Real gap, not resolved here.**

Two examples found during the per-service check:

* **Service #19 (Register Heirs Ownership)** lists "Legal Heir recognized under applicable law" and "Court-appointed Administrator or Executor" as eligible applicants. Neither is a role in `roles-and-responsibilities.md`. An heir may well *become* a Property Owner/Seller once ownership is registered, but at the point of filing this application, they are not yet one — the role that would cover them doesn't exist yet in the six-role list.
* **Service #20 (Register Community Land)** lists "Community Leader" and "Authorized Community Committee Member" as eligible applicants — again, no matching role.

**Proposed:** rather than inventing two new individual-user roles for what are edge-case applicant categories (an heir mid-succession, a community representative), treat these as **temporary or special-capacity personas layered on top of the existing six roles** — e.g., a person acting as "Legal Heir" for the purposes of Service #19 is, functionally, exercising a subset of Property Owner/Seller's eventual responsibilities before that status is confirmed. This avoids a role-count increase for what may be two genuinely narrow cases, but is a documentation judgement, not something the source resolves.

**Confidence:** Medium. **Flagged for client input** on whether these deserve their own role entries in `roles-and-responsibilities.md` or should be handled as described above.

**Affects:** `roles-and-responsibilities.md` (if the client wants dedicated entries); `role-workflows.md` (currently built treating these as capacity-limited extensions of Property Owner/Seller, per the proposal above).

---

## B. Payments

All payment findings are detailed in `payments.md`. This section records the decisions needed to close them, in the same format Group C used.

### B1. Should the five no-fee services (#17, #18, #33, and #7's Owner/Entity Information Amendment component) be built as genuinely free?

**Proposed: yes**, on the same basis as Group C's confirmed Service #2 — see `payments.md`'s "No-Fee Services" section for the full evidence. Every one of these rows is silent on payment in a source document that is otherwise consistently explicit about fees. Two sibling services (#40, #42) already correctly document themselves as free using this exact reasoning.

**Confidence:** Medium-high. **Flagged for client confirmation**, same standard as Group C's B11 needed a direct answer rather than an inference.

**Affects:** `service-17-grant-registration.md`, `service-18-grant-completion.md`, `service-33-request-property-survey.md`, and `service-07-update-property-ownership-information.md` Sections 8–9 (Owner/Entity Information Amendment branch only — the Property Information Amendment branch remains fee-bearing per row 112).

### B2. Should the systemic Section 9 defect across Services #1–#39 be corrected as one dedicated pass?

**Proposed: yes**, and recommended as the very next piece of work on this module, before UI work starts — because every UI screen for payment steps will otherwise be built against a wrong assumption in 15+ of the 39 files. Full itemized list, by service:

| Service | Current Section 9 claim | What the source/file's own workflow actually shows | Fix needed |
| :---- | :---- | :---- | :---- |
| #5 – Transfer Property Ownership | Pay before submission | Row 106 + the file's own Option 1 workflow both show pay **after** audit | Correct Section 9 to match Option 1; Option 1 itself is already right |
| #7 – Update Property Ownership Info (Owner/Entity branch) | Pay before submission | Row 107 — no fee at all | See B1 above |
| #9 – Register Gift Transfer | Pay before submission | Row 88 (only sourced channel) — pay **after** audit | Add a Trustee Centre option matching source order, or flag the online flow as an unsourced platform extension |
| #10–#16 – Lease-to-Own / Usufruct family (7 files) | Pay before submission | Row 86 pattern inherited by cross-reference — Trustee Centre channel pays after audit | Same as #9 |
| #17 – Grant Registration | Pay before submission | Row 98 — no fee | See B1 |
| #18 – Grant Completion | Pay before submission | Row 99 — no fee | See B1 |
| #23 – Register Lease | Pay before submission | Row 82 + file's own Option 1 — pay **after** initial audit, before hearing/decision | Correct Section 9 to match Option 1 |
| #24 – Renew Lease | Pay before submission | Same as #23 | Same fix |
| #26 – Submit Tenancy Dispute | Pay before dispute submission | Rows 72–81 + file's own Option 1 — pay **after** initial audit, before hearing | Correct Section 9 to match Option 1 |
| #27 – Cancel Tenancy Contract | Pay before submission | Row 83 — Trustee Centre pays after audit; Online channel shows no fee step at all | Needs a two-channel rewrite, not a one-line fix — see `payments.md`'s channel-split section |
| #28 – Request Rental Valuation | Pay before submission | Row 84 — explicit: "Pay fees **after approval**" | Highest-confidence, cleanest fix in the set |
| #31 – Detailed Real Estate Statement | Pay before request processed | Row 109 — in-person channel pays after the identity check/audit step | Lower confidence than #28; identity verification may not be a substantive "decision" the way audit is elsewhere |
| #32 – To Whom It May Concern Certificate | Pay before certificate generated | Row 108 — same shape as #31 | Same caveat |
| #33 – Request Property Survey | Pay before request processed | Row 111 — no fee at all | See B1 |
| #38, #39 – Submit/Track Complaint | Pay before submission/tracking | No source row (extrapolated) — see B3 below for whether a fee should exist at all | Depends on B3's resolution |

**Confidence:** Sourced for #5, #9, #10–#16, #17, #18, #23, #24, #26, #28, #33 (the row itself is unambiguous). Medium for #27, #31, #32 (real conflicts found, but the "decision" being paid around is less clearly substantive than elsewhere).

**Not done in this pass** — this chat's brief was the analysis layer (`payments.md`, `open-questions.md`, `navigation.md`, `role-workflows.md`), not the 43 service-flow files themselves. Recommend a dedicated correction pass, the same way Group C's UI reconciliation ran as its own tracked issue (#50) rather than folding into the payment-model correction that motivated it.

### B3. Should Submit Complaint (#38) and Track Complaint (#39) carry a fee at all?

**Proposed: no — make both free, or at minimum make #39 free.**

Neither service has a source row; both are fully extrapolated, meaning "Payment Required: Yes" in both files is a platform design decision, not something the source specifies. Two things argue against that design decision:

1. **Consumer-protection complaint mechanisms are typically free to encourage reporting.** A fee to report a developer, agent, or transaction problem to the regulator is an unusual design choice for a *consumer protection* category of service, and nothing in the PRD's stated anti-fraud and consumer-protection goals suggests RERA wants to charge for intake.
2. **#39 duplicates a feature that is explicitly sourced as free.** `feature-02-track-application-status.md` states outright: "No additional fee. Application tracking is included as part of the submitted service." Service #39 performs the identical function — status lookup by reference number — for one specific application type (complaints) and charges for it. There's no source or design rationale distinguishing why tracking a complaint should cost money when tracking every other application type doesn't.

**Confidence:** Medium on #38 (a fee isn't unreasonable per se — Group C's own consumer-facing services aren't free), **High on #39** (the internal inconsistency with Feature #2 is hard to justify either way).

**Flagged for client confirmation** — this is a policy/design question, not a documentation-accuracy one, since no source contradicts the current files.

**Affects:** `service-38-submit-complaint.md`, `service-39-track-complaint.md` Sections 8–9; `payments.md`'s Model D no-fee list (would need #39, and possibly #38, added if confirmed).

### B4. Should the Trustee Centre / Online payment-timing split be documented as two sub-flows per affected service?

Not proposed here — see `payments.md`'s "Trustee Centre / Online channel split" section for the full evidence and reasoning. This is flagged as a workflow-design decision, not resolved with a recommendation, because it materially changes seven files' structure rather than correcting a single line, and because it echoes Group C's C2 question (should a counter-only channel get built as a genuinely separate flow, or treated as an assisted mode of the same underlying service) closely enough that the same answer might apply here without needing independent re-derivation.

**Proposed, tentatively, by analogy with Group C's confirmed C2:** treat the Trustee Centre as an assisted-mode channel of the same service, not a second service — meaning these seven files need their Trustee Centre payment-timing added as an annotated alternate path, not a structurally separate flow. **Confidence:** Medium — C2's reasoning transfers well (same anti-in-person-visit PRD goals apply to Groups E+F as to Group C), but hasn't been independently confirmed for this module.

---

## C. Service Structure

### C1. Does the Wallet Account referenced at row 86 belong to this module?

**Yes — this module is the actual sourced home of `proposed-services.md` P-22**, not just a user of a platform-wide primitive. See `payments.md`'s Settlement Mechanisms section for the full reasoning. This isn't a question requiring an answer so much as a correction that should propagate: `proposed-services.md` P-22 already notes row 86 as its evidence but doesn't say which module that row belongs to (it's filed under the platform-wide Tier 4 list, not attributed to Individual User specifically).

**Confidence:** Sourced on the row; Medium on the P-22 identity claim (see `payments.md`).

**Affects:** `proposed-services.md` P-22's entry could note Individual User Service #6 as its concrete source, strengthening the case for building it early — not changed in this pass since `proposed-services.md` belongs to a different scope than this module's own documents, but worth flagging to whoever next touches that file.

---

## Summary

| Area | Questions | Proposed | Needs client confirmation |
| :---- | :---: | :---: | :---: |
| A. Roles | 3 | 3 | 3 (A1, A2 bundled with A1, A3) |
| B. Payments | 4 | 3 with a proposed direction | 4 (all) |
| C. Service structure | 1 | 1 | 0 (informational) |
| **Total** | **8** | **7** | **7** |

Unlike Group C's open-questions.md at its current state, **none of these are resolved yet** — this is the first pass through this module's analysis layer, not a multi-round audit. The single highest-priority item for a follow-up pass is **B2** (the Section 9 correction sweep across #1–#39), since `navigation.md` and `role-workflows.md` in this same delivery already had to make a judgement call about which payment-timing claim to trust (the file's own Option 1 workflow where one exists, the master table row otherwise) rather than the files' Section 9 line — meaning the four documents delivered in this chat are already internally consistent with the *correct* payment timing, not the currently-published Section 9 text. That gap between what this module's four new documents say and what the 43 existing service-flow files say should be closed before UI work starts, or the UI will be built against whichever one a given screen author happens to open first.
