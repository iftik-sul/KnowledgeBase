---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
  - "RERAN/reference/source-of-truth/RERAN_registration_flows.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - assisted-mode
---

# Screen: Assisted Service Terminal

**Operated by:** Trustee Centre and Land Department operators (**Group G** — not a Group C role, holds no Group C permission scope)

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
Transaction Capture (embeds Service Request)
↓
Document Capture
↓
Review & Customer Handoff
```

## Sections

### Section 1 — Operator & Customer Context

* Operator identity, verified under registration Flow 7's per-operator transaction scopes — not a Group C `file` scope, which belongs to institution staff only.
* Represented customer or institution: NIN/CAC lookup, or entry where the customer has no prior platform record.
* **Authority record** — how the customer authorised this transaction (present in person, Power of Attorney reference, or other basis defined per service). Captured once per session and attached to every request filed in it.

### Section 2 — Service Selection

Filtered to the specific services this operator's Flow 7 scope permits — not the full eighteen. Which services actually route through a counter is service-specific and, per each service's own service-flow document, only sourced for some of the eighteen:

| Service group | Assisted mode sourced? |
| :---- | :---- |
| #1–#2 Institutional approval | Not applicable — filed by the institution's own IRM, not at a counter |
| #3–#6 Mortgage lifecycle | Yes, alongside the Online Mortgage System |
| #7 Grant Property Mortgage | Not sourced — row 39 names only the online channel |
| #8–#11 Finance lease lifecycle | Yes — Trustee Centre is the only channel these source |
| #12 Fund company registration | Yes — Trustee Centre |
| #13–#14 Heirs' sale, company shares sale | Yes — Trustee Centre |
| #15–#17 Title deed update, split ownership, issuance | Yes — Trustee Centre or Land Department, per service |
| #18 Contract cancellation | Yes — Land Department |

This table is a routing summary; the authoritative statement for each service is its own `service-flows/service-NN-*.md` document.

### Section 3 — Transaction Capture

The same [service-request.md](service-request.md) form, embedded rather than re-specified — see that screen's Applicant & Representation section, which already accounts for an assisted-mode block. This terminal does not maintain a second copy of the eighteen services' field groups.

### Section 4 — Document Capture

Upload, scan, or photograph-and-attach for a walk-in customer without their own prior digital documents. Same [components.md](../components.md#document-uploader) as the direct-filing path; the difference is capture method, not validation.

### Section 5 — Review & Customer Handoff

* Summary of what was entered, shown to the customer before submission.
* **Customer acknowledgement** — a recorded confirmation that the customer reviewed and agrees with what was filed on their behalf. Distinct from the Authority record in Section 1: authority establishes the operator *can* act; acknowledgement confirms the customer saw *what* was filed.
* Submission reference and next-step summary (what happens at the internal certification / RERAN gate, in plain terms, since the customer will not have platform access to check status themselves in the way an institution's own filer does).

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
3. Requests filed here carry the same validation as direct submissions ([service-request.md](service-request.md#validation)) — assisted mode does not relax any field, document, or property/party reference check.

## Role Variations

None — this screen has one operating context (a Group G operator acting for a walk-in customer), not several roles to differentiate between. Where the issue's screen template calls for Role Variations, this section states that plainly rather than inventing distinctions between a Trustee Centre operator and a Land Department operator that the source does not draw; both hold the same kind of per-operator transaction scope under the same registration flow, differing only in which physical location and which services they're scoped to.

## User Flow

```
Operator Login (Group G)
↓
Assisted Service Terminal
↓
Operator & Customer Context → Service Selection → Transaction Capture → Document Capture → Review & Handoff
↓
Submission Reference (customer copy)
```

Post-submission tracking (internal certification, RERAN review, settlement, output) proceeds exactly as it would for a directly-filed request — see [application-details.md](application-details.md) — but the represented customer, not the operator, is the party who would eventually receive the output document, per each service's own delivery mechanism (typically email, per the source workflow text).

## Notes

* **This screen belongs to Group G, not Group C.** It is documented in this module only because it operates Group C services on Group G's behalf, per answer C2. When Group G's own interfaces are written, this file moves there and this module's [README.md](../README.md) and [navigation.md](../../navigation.md) link out to it rather than owning it — both already say so; this rewrite does not change that intent, only the screen's depth.
* **Which services route through a counter at all is not fully sourced.** Service #7 (Grant Property Mortgage) is the one mortgage-lifecycle service with no Trustee Centre variant in source — see that service's own Open Questions for why this is flagged rather than assumed to be an omission.
* Operator transaction scopes and their provisioning (registration Flow 7) are out of this module's scope note (post-login functionality only within Group C); this screen documents the Group C-facing side of that access, not Flow 7 itself.
