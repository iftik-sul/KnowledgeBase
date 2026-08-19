---
project: RERAN
module: real-estate-developer
type: reference-sample
status: current
updated: 2026-08-19
contains_proposals: false
derived_from:
  - "RERAN/modules/real-estate-developer/ui/README.md"
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/financial-trust-institutions/ui/figma-prompts/README.md"
tags:
  - real-estate-developer
  - ui-spec
  - figma
  - reference
---

# Figma Prompt Packs — Real Estate Developer

**This folder is new, started 2026-08-19.** It follows the same conventions established in [Group C's figma-prompts folder](../../financial-trust-institutions/ui/figma-prompts/README.md) — read that file first for the full pattern (fixed opening block, one file per service rather than per screen, name-don't-describe component reuse, the simplicity constraint, negative instructions for things the product deliberately lacks, numbered top-to-bottom content, consistent sample data, and an assumptions table at the top of each pack). Everything in that README applies here unchanged; it is not repeated in full in this file.

**These files are samples, not specifications** — same as Group C's. When you need a prompt for a screen not yet covered here, copy the closest existing pack in this folder and adapt it, rather than starting from scratch. Where a pack disagrees with [`../screens/`](../screens/), the screen spec wins.

## What's here so far

| Pack | Contains |
| :---- | :---- |
| [red-sidebar.md](red-sidebar.md) | The `RED-Sidebar` component prompt — RED's persistent left navigation, adapted from Group C's `FI-Sidebar` component spec, with RED's own 12-item nav list (see [navigation.md](../../navigation.md)) |

This is the first entry, not a full pack set. Service-journey prompts (the equivalent of Group C's `s03-mortgage-registration.md`-style packs) and a landing-screens pack (the equivalent of `nav-sidebar-landing-screens.md`) have not been started yet — see [`module-roadmap.md`](../../../../module-roadmap.md) for what's queued next.

## Screen ID conventions

Not yet established for this module — RED has no service-journey packs yet to draw a convention from. When the first service pack is built, follow Group C's `S{n} – NN` / `NAV – NN` pattern (see [Group C's README](../../financial-trust-institutions/ui/figma-prompts/README.md#screen-id-conventions)) unless a reason emerges to diverge.
