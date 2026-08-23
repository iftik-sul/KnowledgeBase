---
project: 3i
module: localisation
type: ui-spec
status: current
updated: 2026-08-23
id: 3I-LCL-UI-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - ui
  - admin
---

# Screen: Admin Translation Management

Satisfies: FR-LOC-01, FR-LOC-02

---

## Purpose

Admin browses, searches, and corrects AI-generated translations for every non-exempt static UI string.

## Access Gate

Admin only.

## Contents

A searchable list of `TranslationString`s (by key or category), each expandable to show the English source alongside all four AI-generated locale values, with the [Translation Status Indicator](../components.md#translation-status-indicator) per locale. Editing any locale's text saves immediately — live the instant the admin confirms, per the confirmed no-approval-queue workflow.

**Exempt strings do not appear on this screen** — they have their own dedicated flow entirely, since editing them here would bypass the sign-off gate that makes them exempt in the first place. See [Exempt String Sign-Off](exempt-string-signoff.md).

## Behaviour

A correction sets `aiGenerated = false` on that specific `TranslationValue` — the other three locales' values for the same string are untouched, since correcting one language's translation says nothing about whether the others are also wrong.

## Role Variations

Admin only.

## Contrast and RTL

Standard, 4.5:1 (NFR-12). Full RTL mirroring where the admin panel supports it (FR-LOC-04) — including, notably, this screen's own preview of Arabic/Urdu text, which should render genuinely RTL in the editor, not just store RTL text inside an LTR-rendered input.