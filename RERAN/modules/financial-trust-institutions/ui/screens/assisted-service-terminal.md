---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-15
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

> **Corrected 2026-08-15 — this file had not been touched since it was first written (2026-08-11), through every correction pass this module has had.** Found: two broken links to `service-request.md`, deleted in favour of `screens-unified/submit-application.md`; stale "Group C `file` scope" language that no longer makes sense once Group C's own scopes were retired module-wide; a "settlement" reference to the retired standing-account concept; and — the most consequential gap — no acknowledgment anywhere that this is the exact screen where Services #12 and #18's post-approval counter payment physically happens, a fact this file predates entirely. All fixed below.

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
[Payment at Counter, where sourced before RERAN's decision]
↓
Review & Customer Handoff
↓
[Payment at Counter, where sourced after RERAN's decision — separate operator session]
```

**Corrected 2026-08-15** — payment is now shown explicitly in this diagram, in both its possible positions, since this screen is where the counter payment for every assisted-mode service actually happens — see Section 3a below.

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
| #12 Fund company registration | Yes — Trustee Centre | **After RERAN's decision** — this operator collects payment once approval comes back, in a separate session with the customer |
| #13–#14 Heirs' sale, company shares sale | Yes — Trustee Centre | Before RERAN's decision, as part of this same visit |
| #15–#17 Title deed update, split ownership, issuance | Yes — Trustee Centre or Land Department, per service | Before RERAN's decision, as part of this same visit |
| #18 Contract cancellation | Yes — Land Department | **After RERAN's decision** — same as #12 |

This table is a routing summary; the authoritative statement for each service is its own `service-flows/service-NN-*.md` document. **Payment Timing column added 2026-08-15** — this table previously said nothing about when payment happens relative to RERAN's decision, even though every row on it is a service where the operator, not a digital checkout, is who actually collects the payment.

### Section 3 — Transaction Capture

The same [Submit Application](../screens-unified/submit-application.md) form, embedded rather than re-specified — see that screen's Institution & Party Information section, which already accounts for an assisted-mode block. This terminal does not maintain a second copy of the eighteen services' field groups. **Corrected 2026-08-15** — previously linked to `service-request.md`, deleted in favour of Submit Application (issue #50).

### Section 3a — Payment at Counter

**Added 2026-08-15.** Not previously specified anywhere on this screen, despite every assisted-mode service in Section 2's table charging a fee collected here.

* **For #3–#11 (upfront services):** the operator processes payment via the same shared platform gateway the direct channel uses, before Transaction Capture proceeds — functionally identical to an institution user's own checkout, just entered by the operator on the customer's behalf.
* **For #13–#17:** the operator collects payment at the counter as part of this same visit, before submitting for RERAN's review.
* **For #12 and #18:** the operator submits the transaction *without* collecting payment, and RERAN's decision is awaited. **Once approved, the customer must return to the counter (or the operator must otherwise reach them) for the operator to collect payment before the output can be issued.** What happens if the customer doesn't return — no expiry, no escalation, no alternative payment channel — is not addressed by any source document or client decision. This is the same open item flagged in `payments.md`'s and `validation-rules.md`'s To Confirm sections, and it lands specifically on this screen and this operator, which hadn't been documented anywhere until now.

### Section 4 — Document Capture

Upload, scan, or photograph-and-attach for a walk-in customer without their own prior digital documents. Same [components.md](../components.md#document-uploader) as the direct-filing path; the difference is capture method, not validation.

### Section 5 — Review & Customer Handoff

* Summary of what was entered, shown to the customer before submission.
* **Customer acknowledgement** — a recorded confirmation that the customer reviewed and agrees with what was filed on their behalf. Distinct from the Authority record in Section 1: authority establishes the operator *can* act; acknowledgement confirms the customer saw *what* was filed.
* Submission reference and next-step summary (what happens at the internal certification / RERAN gate, in plain terms, since the customer will not have platform access to check status themselves in the way an institution's own filer does). **For #12/#18, this summary should explicitly tell the customer they'll need to return to pay once approved** — see Section 3a.

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
3. Requests filed here carry the same validation as direct submissions ([Submit Application](../screens-unified/submit-application.md#validation)) — assisted mode does not relax any field, document, or property/party reference check. **Corrected 2026-08-15** — previously linked to `service-request.md`, deleted.
4. **Added 2026-08-15.** For #12/#18, this screen must not allow the operator to submit the transaction as though payment were being collected now — the Submit Application step embedded here (Section 3) needs to correctly skip its payment step for these two services, the same way it does for the direct channel, and instead flag the return-to-collect-payment requirement per Section 3a.

## Role Variations

None — this screen has one operating context (a Group G operator acting for a walk-in customer), not several roles to differentiate between. Where the issue's screen template calls for Role Variations, this section states that plainly rather than inventing distinctions between a Trustee Centre operator and a Land Department operator that the source does not draw; both hold the same kind of per-operator transaction scope under the same registration flow, differing only in which physical location and which services they're scoped to.

## User Flow

```
Operator Login (Group G)
↓
Assisted Service Terminal
↓
Operator & Customer Context → Service Selection → Transaction Capture →
  [Payment, before decision — #3–#11, #13–#17] → Document Capture → Review & Handoff
↓
Submission Reference (customer copy)
↓
(for #12, #18 only) Customer returns once approved → operator collects payment at counter
```

Post-submission tracking (internal certification, RERAN review, output) proceeds exactly as it would for a directly-filed request — see [application-details.md](application-details.md) — but the represented customer, not the operator, is the party who would eventually receive the output document, per each service's own delivery mechanism (typically email, per the source workflow text). **Corrected 2026-08-15** — "settlement" removed from this list; there is no settlement stage anywhere in Group C, and #12/#18's genuine post-approval payment step is now specified in Section 3a rather than gestured at with a retired term.

## Notes

* **This screen belongs to Group G, not Group C.** It is documented in this module only because it operates Group C services on Group G's behalf, per answer C2. When Group G's own interfaces are written, this file moves there and this module's [README.md](../README.md) and [navigation.md](../../navigation.md) link out to it rather than owning it — both already say so; this rewrite does not change that intent, only the screen's depth.
* **Which services route through a counter at all is not fully sourced.** Service #7 (Grant Property Mortgage) is the one mortgage-lifecycle service with no Trustee Centre variant in source — see that service's own Open Questions for why this is flagged rather than assumed to be an omission.
* **#12/#18's return-to-pay gap is the same unresolved item flagged in `payments.md`, `validation-rules.md`, and `payment-history.md`** — this screen is simply where it becomes concrete: an actual operator, at an actual counter, waiting to collect a payment that may or may not be returned for. Whichever document eventually resolves this (an expiry rule, an escalation, an alternative remote-payment option) should update this screen's Section 3a alongside it.
* Operator transaction scopes and their provisioning (registration Flow 7) are out of this module's scope note (post-login functionality only within Group C); this screen documents the Group C-facing side of that access, not Flow 7 itself.
