---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-010
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - profiles
figma: null
---

# Screen: Guardian Dashboard

Satisfies: FR-FAM-09

---

## Purpose

The Member's overview of every profile on the account — all four states, not just the active ones.

## Content

One card per profile, in any state, using the [Profile State Indicator](../components.md#profile-state-indicator) and [Age Band Badge](../components.md#age-band-badge).

For **active** and **never-activated** profiles: progress, enrolments, attendance, **exam results** — scores and pass/fail, never written answers, settled in review 2026-08-18 — and certificates (FR-FAM-09).

For **inactive (cancelled)** profiles: the same historical data remains visible — cancellation preserves it — with a clear "cancelled" label and a reactivate action leading to seat purchase (`commerce`).

For **deleted** profiles: only surviving certificates are shown, each linking to its public verification page, consistent with FR-FAM-10 and FR-CERT-08. No progress or exam data, because none survives.

## Behaviour

Actions available per card, gated by state:

| State | Available actions |
| :---- | :---- |
| Active | Edit, reset PIN, cancel seat |
| Never activated | Edit, reset PIN, activate (purchase seat), delete |
| Inactive | Reactivate (purchase seat), delete |
| Deleted | None — view certificates only |

**Cancel and Delete are visually and textually distinct actions**, never the same button with different confirmation copy. Cancel preserves everything; Delete is the destructive path detailed in [Profile deletion confirmation](profile-deletion-confirmation.md).

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04). The state indicator's colour coding (if used) must not be colour-only — pair with a text label, since colour-only status is a common accessibility failure and this screen carries safeguarding-relevant state.