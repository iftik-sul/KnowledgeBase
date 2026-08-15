---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/services-overview.md"
  - "RERAN/modules/individual-user/payments.md"
  - "RERAN/modules/individual-user/ui/README.md"
  - "RERAN/modules/individual-user/ui/components.md"
tags:
  - individual-user
  - ui-spec
  - wizard
---

# Screen: Submit Application (Configurable Wizard)

**Access:** Any authenticated Individual User. Which services are actually selectable depends on the account's own properties, leases, and authorizations — see `navigation.md`'s Access Model — not on a role.

## Purpose

One configurable wizard behind all 41 services that collect their own fields (everything except #30 and #37, which route into this same wizard rather than defining separate forms — see below). The step sequence and field groups shown depend entirely on which of the eleven patterns (`ui/README.md`'s Service × Form Matrix) the selected service belongs to.

## Layout

```
Step Indicator (varies by pattern — see Sections)
↓
Current Step Content
↓
Back / Continue (or Save Draft / Submit on the final step)
```

## Sections — By Pattern

### Pattern A (Search/Lookup) — #1, #2, #3

```
Enter Search Criteria → Review Service Fee → Complete Payment → Submit → View Result
```
No document upload, no multi-step wizard — effectively a single-screen search-and-pay flow. Shortest of the eleven patterns.

### Pattern B (Standard single-applicant) — #4, #17, #18, #20, #22, #41

```
Select/Enter Property → Applicant Details → Transaction-Specific Details →
  Upload Documents → [Payment, if fee-bearing] → Review → Submit
```
#17, #18 skip the Payment step entirely (confirmed no-fee, `payments.md` Category 4). #41 is Trustee-Centre-only per its own source — this pattern documents its *fields*, but #41 has no online submission path at all; see its own service-flow file.

### Pattern C (Two-party with counterparty confirmation) — #5, #6, #8, #9, #10, #11, #14

```
Primary Applicant: Select Property → Enter Counterparty Details →
  Upload Documents → [Payment, if online-upfront] → Review → Submit
↓
Counterparty: Receive Notification → Review Details → [OTP, #6 only] →
  Upload Own Documents (where required) → Confirm or Decline
↓
RERAN Review → Approved → Both Parties Notified
```
This is the only pattern with two distinct user sessions inside one application. The wizard state must persist correctly across both — the counterparty is not filling out a fresh wizard, they're completing a specific pending application. See Counterparty Confirmation Card in `components.md`.

**Channel split, where sourced:** #5, #9–#16 (Pattern C and D both) source a Trustee Centre channel with a different payment timing than the online path documented above — see `payments.md` Category 3. This wizard documents the online path; the Trustee Centre path is an assisted-mode workflow outside this wizard's scope, operated by Group G (not yet documented — see `module-roadmap.md`'s Group G Note).

### Pattern D (Amend/release/terminate existing record) — #7, #12, #13, #15, #16, #19, #21

```
Select Registered [Property/Lease-to-Own/Usufruct/Company] →
  Review Existing Details → Enter Amendment/Release/Termination-Specific Fields →
  [Repeatable Group Entry, #19/#21 only] → Upload Documents →
  [Payment, if fee-bearing] → Review → Submit
```
**#7 is a split service** — Property Information Amendment follows this pattern in full (fee-bearing, online); Owner/Entity Information Amendment is Trustee-Centre-only, no fee, no online wizard path at all (see its own service-flow file's Option 1).

**#19, #21's repeatable group** — a dynamic add/remove list (heirs with their ownership shares for #19; partners for #21), not a fixed field set. Each row needs its own identity and share-percentage fields; the wizard must validate that shares sum correctly before allowing submission, though the exact validation rule (must equal 100%? may be partial?) is **not specified in source** and needs client confirmation before this becomes a hard validation rule rather than a soft warning.

### Pattern E (Tenancy) — #23, #24, #27

```
[Landlord or Tenant, per open-questions.md B1] → Select/Enter Property →
  Enter Counterparty (Landlord or Tenant) Details → Enter Lease Terms →
  Upload Documents →
  [Online:] Payment → Submit
  [Trustee Centre:] Submit → (payment happens at the counter after RERAN review,
    not in this wizard — see Application Details for the "Pay Now" action)
```
The only pattern where the wizard's *first* step is choosing which of two roles the applicant is acting as, per B1's resolution — Landlord remains the primary/default path, Tenant is the documented secondary path.

### Pattern F (Management workspace) — #25

Not a linear wizard. Select a lease (Lease Selector, `components.md`) → view details → choose an action from a list of permitted actions → the chosen action opens whichever pattern actually matches it (most commonly Pattern D's shape, for amendments). Payment is conditional per action, not per the umbrella service — see `payments.md` Category 6.

### Pattern G (Category-conditional) — #26

```
Select Dispute Category (10 sub-types) → Enter Category-Specific Details →
  Upload Category-Specific Documents → [Payment, timing per payments.md Category 2] →
  Submit → Routed to Correct Process → [Hearing/Conciliation, where applicable] →
  Decision
```
The category selector is a hard gate (`validation-rules.md`) — no downstream field renders until a category is chosen. **The ten sub-types' individual field/document sets are not fully specified in this package** — see `ui/README.md`'s Open Items. This section documents the pattern shape, not all ten field sets.

### Pattern H (Power of Attorney) — #29, #30, #42

**#29 (Register):**
```
Select Property → Enter Attorney (Representative) Details → Define Scope of Authority →
  Upload PoA Document → Payment → Review → Submit
```

**#30 (Act on Behalf):** *not a field-collection form.*
```
Select Property Owner (who has granted the representative a PoA) →
  System Validates PoA Status (hard gate — see validation-rules.md) →
  Select Service to Perform → [Wizard re-opens at that service's own pattern,
    with the represented owner's identity substituted for "Applicant"] →
  [Payment, where the selected service requires it] → Submit
```

**#42 (Cancel):** field set unknown — see `ui/README.md`'s Open Items. Provisionally mirrors #29's Select-Property → Enter-Reason → Upload-Document → Submit shape, inverted, but this is inference, not sourced.

### Pattern I (Certificate / statement / valuation) — #31, #32, #33, #34, #35, #28

```
Search/Select Property → Enter Purpose → [Preferred Inspection Date, where sourced] →
  Upload Documents → [Payment — upfront for #31/#32/#34/#35, no fee for #33,
    after-approval for #28] → Submit → [Inspection Scheduled, where required] →
  Report/Certificate Issued
```
**#28's payment step does not appear before submission at all** — it renders only after RERAN approves the valuation, as an action on Application Details, matching #28's corrected Section 9 (`payments.md` Category 2). This is the same after-approval pattern as some of Pattern C/D/E/G's Trustee-Centre paths, but #28 is the one Pattern I service where it's confirmed for the *online* channel too.

### Pattern J (Diaspora / identity) — #36, #37

**#36:**
```
Enter Personal Information → Select Verification Method → Upload ID Documents →
  Complete Biometric Verification → Payment → Submit → Identity Validated
```

**#37:** *routing wrapper.*
```
Confirm #36 Status = Verified (hard gate) → Select Transaction Type →
  [Wizard re-opens at that transaction's own pattern] → Submit
```

### Pattern K (Complaint) — #38, #39

**#38:**
```
Select Complaint Category → Enter Complaint Details (free text) →
  Upload Supporting Evidence → Payment (confirmed required, open-questions.md A7) →
  Submit → Assigned → Investigation → Resolution
```

**#39:** read-only, not a submission wizard — search only, no payment (`open-questions.md` A6). See [my-complaints.md](../screens/my-complaints.md) rather than this wizard.

## Empty State

Not applicable at the wizard level — each pattern's own selector components (Property Selector, Lease Selector) define their own empty states where a prerequisite record doesn't exist yet.

## Reused Components

Property Selector, Lease Selector, Counterparty Confirmation Card, Document Upload, Payment Step, Buttons — all from `components.md`.

## Validation

See `validation-rules.md` in full. The two hard gates worth repeating here since they block wizard progression entirely, not just show a warning: PoA scope validation (Pattern H) and Remote Identity Verification status (Pattern J, #37).

## Access

Every pattern is reachable by every authenticated user; what's actually selectable is constrained by the account's own data (owns no properties → Patterns B/C/D that require selecting one are blocked at the Property Selector step, not at a higher access-control layer). No pattern is gated by a declared role.

## User Flow

```
Services Catalog → Service Details → Submit Application (pattern-appropriate steps) →
  Application Review → [Payment, where upfront] → Submit → Application Details
```

## Notes

* This is the largest design surface in the package and the one most likely to need revision once actual field-level mockups are built — the pattern classification is High confidence (checked service-by-service against source), but the exact step ordering within each pattern is design judgement, not sourced fact, except where a specific payments.md/service-flow file citation is given above.
* Pattern G's ten sub-types and #42's field set are the two genuinely open gaps — see `ui/README.md`.
* The #19/#21 repeatable-group share-validation rule needs a client answer before it can be enforced rather than just displayed as guidance.
