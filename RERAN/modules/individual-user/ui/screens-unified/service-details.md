---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/service-flows/"
  - "RERAN/modules/individual-user/payments.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - catalog
---

# Screen: Service Details

**Access:** Any authenticated Individual User.

## Purpose

Show everything a user needs to know before starting a service's wizard: eligibility, required documents, fee, and timing — pulled directly from that service's own service-flow file, not restated independently (restating risks drifting out of sync the way `services-overview.md` and `module-roadmap.md` already have, twice, in this module's documentation history).

## Layout

```
Service Header (name, category, fee indicator)
↓
Who Can Apply
↓
Prerequisites
↓
Required Documents
↓
Fee & Payment Timing
↓
Expected Processing Time
↓
Start Application
```

## Sections

### Section 1 — Who Can Apply

Read directly from the service-flow file's own Who Can Apply section. Where a service has a resolved secondary-applicant path (#23, #24 — Landlord primary, Tenant secondary per `open-questions.md` B1), both are shown, not just the primary.

### Section 2 — Prerequisites

Read from the service-flow file's Prerequisites section. Where a prerequisite is "own a registered property" or "hold an active PoA," this section links directly to My Properties or Power of Attorney so the user can check before starting rather than discovering the gate mid-wizard.

### Section 3 — Required Documents

Read from the service-flow file's Required Documents list.

### Section 4 — Fee & Payment Timing

**The section most likely to need correction if this package is ever built against a stale copy of the service-flow files.** Must read: whether a fee applies at all (5 services confirmed free: #17, #18, #33, #7's Owner/Entity-Amendment path, plus #40/#42 already unspecified), and if so, when it's collected (upfront vs. after RERAN's decision — see `payments.md` for the full per-service table). Shown here exactly as documented, not summarized as a generic "fees apply."

### Section 5 — Expected Processing Time

Read from the service-flow file's own Expected Processing Time section.

### Section 6 — Start Application

Primary action, opens [Submit Application](submit-application.md) at the pattern appropriate to this service.

## Empty State

If a Prerequisite the account doesn't meet is detected (no registered property, no active PoA), the Start Application button is disabled with an inline message pointing to what's missing, rather than allowing the user into a wizard step they can't complete.

## Reused Components

Buttons.

## Validation

Every field on this screen must trace to the corresponding service-flow file section — no field here should be hand-maintained separately from source, given this module's documented history of exactly that kind of drift.

## Access

No role variation — every service's details are visible to every user, matching the Access Model.

## User Flow

```
Services Catalog → Service Details → Submit Application
                 ↖________________________|  (Back)
```

## Notes

* #40's Service Details page shows the email-based process description instead of a wizard-start button — see `ui/README.md`.
* #30/#37's Service Details pages explain the routing behaviour (validate authority/identity, then choose an underlying service) rather than listing their own document/fee requirements, since they don't have independent ones.
