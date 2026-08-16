---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-16
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
  - "RERAN/modules/financial-trust-institutions/payments.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - assisted-mode
---

# Screen: Assisted Service Terminal

**Operated by:** Trustee Centre and Land Department operators (**Group G** — not a Group C role or institution user)

> **Corrected 2026-08-15 — this file had not been touched since it was first written (2026-08-11), through every correction pass this module has had.** Found: two broken links to `service-request.md`, deleted in favour of `screens-unified/submit-application.md`; stale "Group C `file` scope" language that no longer makes sense once Group C's own scopes were retired module-wide; a "settlement" reference to the retired standing-account concept; and — the most consequential gap at the time — no acknowledgment anywhere that this is the exact screen where Services #12 and #18's post-approval counter payment physically happens, a fact this file predated entirely.
>
> **Corrected again 2026-08-16.** The client has since reviewed the #12/#18 post-approval payment timing directly, confirmed it was an artefact of the source's original physical-counter process rather than intentional design, and normalized both services to pay before RERA's decision, the same as #13–#17. The dedicated "Payment at Counter" section this screen gained on 2026-08-15 specifically to handle #12/#18's return-to-pay scenario is folded back into the ordinary counter-payment flow below, since every assisted-mode service now pays at the same point in the visit.

## Purpose

Let a Group G operator run a Group C service on a walk-in customer's behalf, at a counter, exactly as answer C2 establishes: this is the *same online service* accessed in assisted mode, not a separate paper channel or a parallel build. What the operator submits is a normal service request, with an operator and a represented customer attached to it instead of an institution's own filing officer.

## Layout

```
Top Bar
↓
Operator & Customer Context
↓
Service Selection (operator's own transaction scopes only)
↓
Transaction Capture (embeds Submit Application)
↓
Document Capture
↓
Payment at Counter (where the service charges a fee)
↓
Review & Customer Handoff
```

**Corrected 2026-08-16** — this diagram previously showed two separate payment points, one before Transaction Capture and one after Review & Handoff, to accommodate #12/#18's post-decision counter payment. With both services normalized to pay before RERA's decision, every assisted-mode service now pays at the same single point in the visit.

## Sections

### Section 1 — Operator & Customer Context

* Operator identity, verified under registration Flow 7's per-operator transaction scopes. **Corrected 2026-08-15** — previously described this as "not a Group C `file` scope, which belongs to institution staff only." That comparison no longer makes sense: Group C's own scopes, including `file`, are retired module-wide (`navigation.md`) — institution staff don't hold one either any more. The accurate distinction is simpler: this operator is not a Group C institution user at all, and accesses Group C services under Group G's own, separate Flow 7 operator-scope system, which is unaffected by anything that happened to Group C's internal access model.
* Represented customer or institution: NIN/CAC lookup, or entry where the customer has no prior platform record.
* **Authority record** — how the customer authorised this transaction (present in person, Power of Attorney reference, or other basis defined per service). Captured once per session and attached to every request filed in it.

### Section 2 — Service Selection

Filtered to the specific services this operator's Flow 7 scope permits — not the full eighteen. Which services actually route through a counter is service-specific and, per each service's own service-flow document, only sourced for some of the eighteen:

| Service group | Assisted mode sourced? | Payment timing at this counter |
| :---- | :---- | :---- |
| #1–#2 Institutional approval | Not applicable — filed by the institution's own IRM, not at a counter | — |
| #3–#6 Mortgage lifecycle | Yes, alongside the Online Mortgage System | Upfront, before this screen's Transaction Capture step (same gateway as the direct channel) |
| #7 Grant Property Mortgage | Not sourced — row 39 names only the online channel | — |
| #8–#11 Finance lease lifecycle | Yes — Trustee Centre is the only channel these source | Upfront, before Transaction Capture |
| #12–#17 Fund company registration, heirs' sale, company shares sale, title deed update, split ownership, issuance | Yes — Trustee Centre or Land Department, per service | Before RERAN's decision, as part of this same visit |
| #18 Contract cancellation | Yes — Land Department | Before RERAN's decision, as part of this same visit |

This table is a routing summary; the authoritative statement for each service is its own `service-flows/service-NN-*.md` document.

**Corrected 2026-08-16.** This table previously split #12 and #18 out into their own row, "payment after RERAN's decision, in a separate session with the customer." Both are now folded into the same row as #13–#17, since all six services in this cluster pay before RERAN's decision, at the same visit.

### Section 3 — Transaction Capture

The same [Submit Application](../screens-unified/submit-application.md) form, embedded rather than re-specified — see that screen's Institution & Party Information section, which already accounts for an assisted-mode block. This terminal does not maintain a second copy of the eighteen services' field groups. **Corrected 2026-08-15** — previously linked to `service-request.md`, deleted in favour of Submit Application (issue #50).

### Section 4 — Payment at Counter

Where the selected service charges a fee (every service except #1, #2, and #7's unsourced channel — see Section 2), the operator processes payment before submitting for review: for #3–#11, via the same shared platform gateway the direct channel uses; for #12–#18, collected directly at the counter as part of this same visit. In every case, payment happens before the transaction is submitted for RERAN's decision — there is no service left where the operator submits first and returns to collect payment afterward.

**Corrected 2026-08-16 — this section replaces the previous "Section 3a — Payment at Counter."** That section documented a genuinely different, more complex flow for #12/#18: submit without payment, wait for RERAN's decision, then bring the customer back (or otherwise reach them) to collect payment before the output could be issued — with the open question of what happens if the customer never returns. That flow, and the open question that came with it, are both retired: the client has normalized #12/#18 to the same before-decision payment pattern every other counter-paid service already used, so there is no return-to-pay scenario left on this screen to document.

### Section 5 — Document Capture

Upload, scan, or photograph-and-attach for a walk-in customer without their own prior digital documents. Same [components.md](../components.md#document-uploader) as the direct-filing path; the difference is capture method, not validation.

### Section 6 — Review & Customer Handoff

* Summary of what was entered, shown to the customer before submission.
* **Customer acknowledgement** — a recorded confirmation that the customer reviewed and agrees with what was filed on their behalf. Distinct from the Authority record in Section 1: authority establishes the operator *can* act; acknowledgement confirms the customer saw *what* was filed.
* Submission reference and next-step summary (what happens at the internal certification / RERAN gate, in plain terms, since the customer will not have platform access to check status themselves in the way an institution's own filer does).

**Corrected 2026-08-16** — this section previously told the customer, for #12/#18 specifically, that they'd need to return to pay once approved. That instruction is removed: payment is already collected by the time a customer reaches this step, for every service.

## Empty State

Not applicable in the ordinary sense — this is a transaction workspace, not a list. Before an operator selects a service:

**Message**

> Select a service to begin. Only services within your assigned transaction scope are shown.

## Reused Components

See [components.md](../components.md). Uses Top Bar, Document Uploader, Information Cards, Buttons. Does **not** use the Institution Operations Sidebar — this operator is not a Group C institution user and has no institution context to show.

## Validation

See [validation-rules.md](../validation-rules.md). Specific to this screen:

1. Service Selection shows only services within the operator's Flow 7 transaction scope; a service outside it is not rendered, matching the platform-wide rule that an unavailable action is omitted, not disabled.
2. Customer acknowledgement is mandatory before submission — a request cannot be filed in assisted mode without it, since there is no other record that the represented customer saw what was submitted on their behalf.
3. Requests filed here carry the same validation as direct submissions ([Submit Application](../screens-unified/submit-application.md#validation)) — assisted mode does not relax any field, document, or property/party reference check.
4. **Corrected 2026-08-16** — this rule previously required the embedded Submit Application step to skip its payment step for #12/#18 specifically and instead flag a return-to-pay requirement. That special case is removed: every service's payment step behaves identically here as on the direct channel — collected before submission, where the service charges a fee at all.

## Role Variations

None — this screen has one operating context (a Group G operator acting for a walk-in customer), not several roles to differentiate between. Where the issue's screen template calls for Role Variations, this section states that plainly rather than inventing distinctions between a Trustee Centre operator and a Land Department operator that the source does not draw; both hold the same kind of per-operator transaction scope under the same registration flow, differing only in which physical location and which services they're scoped to.

## User Flow

```
Operator Login (Group G)
↓
Assisted Service Terminal
↓
Operator & Customer Context → Service Selection → Transaction Capture →
  Payment at Counter (where fee-bearing) → Document Capture → Review & Handoff
↓
Submission Reference (customer copy)
```

Post-submission tracking (internal certification, RERAN review, output) proceeds exactly as it would for a directly-filed request — see [application-details.md](application-details.md) — but the represented customer, not the operator, is the party who would eventually receive the output document, per each service's own delivery mechanism (typically email, per the source workflow text).

**Corrected 2026-08-16** — this flow previously ended with a note that #12/#18's customer would need to return once approved for the operator to collect payment. That step is removed along with the rest of the return-to-pay scenario.

## Notes

* **This screen belongs to Group G, not Group C.** It is documented in this module only because it operates Group C services on Group G's behalf, per answer C2. When Group G's own interfaces are written, this file moves there and this module's [README.md](../README.md) and [navigation.md](../../navigation.md) link out to it rather than owning it — both already say so; this rewrite does not change that intent, only the screen's depth.
* **Which services route through a counter at all is not fully sourced.** Service #7 (Grant Property Mortgage) is the one mortgage-lifecycle service with no Trustee Centre variant in source — see that service's own Open Questions for why this is flagged rather than assumed to be an omission.
* **This screen's #12/#18 handling is worth recording in full, since it changed direction twice in two days.** A 2026-08-15 correction found #12/#18's genuinely-then-sourced post-approval counter payment and built a dedicated flow, section, and open question around it — the most consequential fix that pass made to this file. A second correction, 2026-08-16, removes that same dedicated handling — not because the 2026-08-15 read of the source was wrong, but because the client has since decided to build #12/#18 differently from what the source described, normalizing their payment timing to match every other counter-paid service.
* Operator transaction scopes and their provisioning (registration Flow 7) are out of this module's scope note (post-login functionality only within Group C); this screen documents the Group C-facing side of that access, not Flow 7 itself.
