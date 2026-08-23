---
project: 3i
module: commerce
type: ui-spec
status: current
updated: 2026-08-20
id: 3I-CMR-UI-006
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - waivers
---

# Screen: Waiver Request Form

Satisfies: FR-WAV-01, FR-WAV-07

---

## Purpose

Submit a hardship waiver request — written explanation, optional evidence, and the one profile the waiver will cover.

## Access Gate

Web only. Member session required.

## Fields

- **Written explanation** — required, free text (FR-WAV-01).
- **Evidence files** — optional upload, stored in a private bucket and never CDN-cached once submitted (FR-WAV-07). Accepted formats and size limits per the platform's general file-upload constraints.
- **Covered profile** — required single-select from the account's own active or never-activated profiles, each shown with its [Tier Badge](../components.md#tier-badge). See [validation-rules.md](../validation-rules.md#waiver-covered-profile-selection). Amended in by [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md) — not part of the original FR-WAV-01, but chosen at this exact point in the flow so approval can be immediate and automatic.

## Warning Copy

Before submission, the form states plainly: **if approved, every profile other than the one selected here will be automatically deactivated.** History is preserved and reactivation later is a fresh payment, same as any seat cancellation — but this is a consequence the account holder should see before submitting, not discover after approval. This is the UX check [3I-DEC-025](/3i/decisions/dec-025-waiver-single-profile-cap.md#cost--open-items-introduced-by-this-decision) flagged as worth confirming once this screen existed — this warning is that confirmation point.

## After Submission

Status moves to Pending. No profile is deactivated yet — deactivation happens only at admin approval, not at submission (see [Waiver Admin Review](waiver-admin-review.md)).

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04).