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

This folder follows the same conventions established in [Group C's figma-prompts folder](../../financial-trust-institutions/ui/figma-prompts/README.md) — read that file first for the full pattern (fixed opening block, one file per service or per shared-screen-set, name-don't-describe component reuse, the simplicity constraint, negative instructions for things the product deliberately lacks, numbered top-to-bottom content, consistent sample data, and an assumptions table at the top of each pack). Everything in that README applies here unchanged; it is not repeated in full in this file.

**These files are samples, not specifications** — same as Group C's. When you need a prompt for a screen not yet covered here, copy the closest existing pack in this folder and adapt it, rather than starting from scratch. Where a pack disagrees with [`../screens/`](../screens/), the screen spec wins.

## What's here

| Pack | Contains |
| :---- | :---- |
| [red-sidebar.md](red-sidebar.md) | The `RED-Sidebar` component prompt — RED's persistent left navigation, adapted from Group C's `FI-Sidebar` component spec, with RED's own 12-item nav list (see [navigation.md](../../navigation.md)). Built and confirmed in Figma, 2026-08-19. |
| [nav-sidebar-landing-screens.md](nav-sidebar-landing-screens.md) | Twelve landing screens, one per sidebar item — `NAV – 01` through `NAV – 12`. Unlike Group C's equivalent pack, this one includes Dashboard, since nothing in RED had been built in Figma yet when this pack was written. `contains_proposals: true` — the sample data is invented for this pack (RED had no built screen yet to draw consistent figures from), though it's deliberately kept consistent with records that already appear in Group C's own built sample data (Crestwood Developments, Banana Island Villas, Lekki Pearl Estate) where the two modules describe the same real-world transactions. |

Service-journey prompts (the equivalent of Group C's `s03-mortgage-registration.md`-style packs, covering a full multi-step service flow rather than a landing screen) haven't been started yet — see [`module-roadmap.md`](../../../../module-roadmap.md) for what's queued next.

## Screen ID conventions

**Established 2026-08-19**, following Group C's `S{n} – NN` / `NAV – NN` pattern directly (see [Group C's README](../../financial-trust-institutions/ui/figma-prompts/README.md#screen-id-conventions)):

| Prefix | Used for | Example |
| :---- | :---- | :---- |
| `NAV – NN` | Sidebar landing screens | `NAV – 06` (Applications) |
| `S{n} – NN` | Screens belonging to service #n's journey | not yet used — reserved for the first service-journey pack |

Both are separate from the design file's own global screen numbering, same as Group C's convention.
