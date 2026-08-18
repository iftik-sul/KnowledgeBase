---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-014
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
  - safeguarding
---

# Screen: Admin — DOB Correction

Satisfies: FR-FAM-07

---

## Purpose

The **only** path by which a learner profile's date of birth can change after creation. Every other surface in the platform treats it as absent, not editable — see [validation-rules.md](../validation-rules.md#date-of-birth).

## Content

Lookup for the target profile, current date of birth, new date of birth, required reason.

## Behaviour

**This is the single highest-leverage safeguarding control surface in the module**, precisely because everywhere else treats the field as immutable. A correction here can change a profile's chat access (FR-FAM-08), catalogue visibility (FR-CRS-10), and enrolment eligibility (FR-ENR-03) all at once, silently, from the learner's perspective — they simply find themselves able or unable to do things they could not before.

On save: age-derived state recalculates everywhere that reads date of birth — chat access, catalogue filtering, age band badge. If the correction changes chat eligibility (e.g. corrects an 11-year-old's DOB to reveal they are actually 13), that change should be visible to the guardian, not merely take effect invisibly at next login.

The reason is recorded permanently and should appear in the admin audit log (NFR-09), given the surface's leverage.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04).
