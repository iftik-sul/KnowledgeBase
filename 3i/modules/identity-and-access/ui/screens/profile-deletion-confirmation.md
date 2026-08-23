---
project: 3i
module: identity-and-access
type: ui-spec
status: current
updated: 2026-08-18
id: 3I-IDA-UI-011
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - profiles
  - safeguarding
figma: null
---

# Screen: Profile Deletion Confirmation

Satisfies: FR-FAM-10

---

## Purpose

The confirmation step before a profile is permanently deleted. Reached only from [Guardian dashboard](guardian-dashboard.md), never as a direct action.

## Content

**This screen's copy is in the exempt safeguarding string set** — [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md). It must state plainly, in two clearly separated lists, what is destroyed and what survives:

**Destroyed:** progress, enrolments, exam results, chat message content (tombstoned — [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md)).

**Survives:** issued certificates, remaining publicly verifiable (FR-FAM-10, FR-CERT-08); the moderation record of any reports or actions on the profile's messages, though the message content itself is gone.

This must **not** be conflated with cancellation. If the Member arrived here by mistake looking for the cancel action, the screen should offer a clear path back to [Guardian dashboard](guardian-dashboard.md) rather than assuming intent.

## Behaviour

Requires explicit confirmation — typing the profile's display name, or an equivalent deliberate action, not a single click. This is the platform's one truly irreversible action against a child's records and should be harder to trigger by accident than cancellation is.

On confirmation: progress, enrolments and exam results are removed; chat messages are tombstoned per [3I-DEC-016](/3i/decisions/dec-016-deletion-removes-content-retains-record.md); certificates remain, unaffected.

## Role Variations

Member only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring (FR-LOC-04). This screen cannot ship in a given language until that language's safeguarding string sign-off is complete, per [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md).