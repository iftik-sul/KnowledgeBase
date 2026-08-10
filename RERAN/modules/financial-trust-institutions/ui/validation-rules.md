---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
updated: 2026-08-11
contains_proposals: true
derived_from:
  - "RERAN/modules/financial-trust-institutions/service-flows/"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - ui-spec
---

# Validation Rules

**Proposed** — field-level rules are absent from the source.

## Submission

* Validate required information, service-specific documents and relevant property/institution reference.
* Confirm filer authority and, for assisted mode, the operator’s transaction scope.
* Flag duplicate active requests for the same instrument and action.

## Certification and Settlement

* Where enabled, delegated certifier scope must certify or return before RERAN submission.
* A return requires a reason and preserves the record.
* An approved request must have sufficient standing-account balance; output release is blocked until settlement.
* An approved-but-unsettled request expires after 30 calendar days.
