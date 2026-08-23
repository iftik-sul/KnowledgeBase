---
project: 3i
module: localisation
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-LCL-UI-002
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
  - safeguarding
---

# Screen: Exempt String Sign-Off

Satisfies: FR-LOC-02 (via [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md))

---

## Purpose

Manage the five safeguarding-critical strings that never pass through AI translation — human-authored text, with named sign-off required per language before that language goes live for each string.

## Access Gate

Admin only.

## Contents

Exactly five rows, one per exempt string (registration block message, safety contact copy, profile deletion confirmation, filtered-message notice, report-a-message flow copy — listed in full in [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md), not re-listed here). Each expands to five locale columns: English source plus the four translated languages, each with a text field (human-entered, never AI-suggested) and a **Sign Off** action requiring the reviewer's name (see [validation-rules.md](../validation-rules.md#sign-off-gates-exempt-string-visibility)).

**The [Translation Status Indicator](../components.md#translation-status-indicator) here shows sign-off state, not AI-vs-corrected state** — a language cell reads either "Not signed off — falls back to English" or "Signed off by [name], [date]."

## Behaviour

**Editing a signed-off string's text clears that language's sign-off immediately** — the new text is not live in that language until a fresh Sign Off action is taken, even if the edit was trivial. This is deliberate friction, not an oversight: a changed safeguarding string is a changed safeguarding string, regardless of how small the change looks to the person making it.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04), with the same genuine-RTL-preview note as [Admin Translation Management](admin-translation-management.md).