---
project: RERAN
module: real-estate-developer
type: reference-sample
status: current
updated: 2026-08-20
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

**These files are samples, not specifications** — same as Group C's. When you need a prompt for a screen not yet covered here, copy the closest existing pack in this folder and adapt it, rather than starting from scratch. Where a pack disagrees with [`../screens/`](../screens/) or a service's own file in [`../../service-flows/`](../../service-flows/), the spec wins.

## What's here

| Pack | Contains |
| :---- | :---- |
| [red-sidebar.md](red-sidebar.md) | The `RED-Sidebar` component prompt — RED's persistent left navigation, adapted from Group C's `FI-Sidebar` component spec, with RED's own 12-item nav list (see [navigation.md](../../navigation.md)). Built and confirmed in Figma, 2026-08-19. |
| [nav-sidebar-landing-screens.md](nav-sidebar-landing-screens.md) | Twelve landing screens, one per sidebar item — `NAV – 01` through `NAV – 12`. Includes Dashboard, unlike Group C's equivalent pack, since nothing in RED had been built in Figma yet when this pack was written. `contains_proposals: true` — sample data is invented for this pack, though deliberately kept consistent with records already in Group C's own built sample data (Crestwood Developments, Banana Island Villas, Lekki Pearl Estate) where the two modules describe the same real-world transactions. |
| [s13-register-real-estate-project.md](s13-register-real-estate-project.md) | Eleven screens covering Service #13's full application journey — `S13 – 01` through `S13 – 11`. First of the five services selected for full UI design. Does **not** copy Group C's `s03` single-wizard shape — #13's own sourced workflow has a hard RERA-acceptance gate mid-flow, so this pack splits into a 4-step wizard for the initial application plus the module's vertical status timeline for everything after submission. Continues `APP-2026-0221`, Gwarinpa Heights, already shown mid-flow in `nav-sidebar-landing-screens.md`, carried through to completion. `contains_proposals: true`. |
| [s1-register-initial-sale.md](s1-register-initial-sale.md) | Ten screens covering Service #1's full application journey — `S1 – 01` through `S1 – 10`. Second of the five. Unlike `s13`, this one **does** use a single continuous 5-step wizard, since #1's own workflow has no mid-flow gate — payment sits before submission, and RERA reviews directly with no internal-certification stage (this module has no maker/checker concept at all). One deliberate step-grouping choice worth knowing: Select Property gets its own dedicated first step rather than being folded into step 2 the way Group C's `s03` folds its own property lookup — this service is fundamentally about the unit being sold. Continues `APP-2026-0219` / Unit A-120, Banana Island Villas, already shown "Approved" in `nav-sidebar-landing-screens.md`'s Applications screen, as `SALE-2026-0087` on Sales & Disclosures, and as a completed ₦42,000 payment on Payment History — all three packs now describe the same transaction consistently. `contains_proposals: true`. |

Three more service-journey packs remain from the selected five: **#6** (Register Mortgage-Linked Sale — the live cross-module validation against Group C's Mortgage Registration), **#24** (Register/Amend Project Details — the dual-stage payment), **#16** (Rename Real Estate Project — the simplest baseline).

## Screen ID conventions

**Established 2026-08-19**, following Group C's `S{n} – NN` / `NAV – NN` pattern directly (see [Group C's README](../../financial-trust-institutions/ui/figma-prompts/README.md#screen-id-conventions)):

| Prefix | Used for | Example |
| :---- | :---- | :---- |
| `NAV – NN` | Sidebar landing screens | `NAV – 06` (Applications) |
| `S{n} – NN` | Screens belonging to service #n's journey | `S1 – 07` (Service #1's Review & Submit step) |

Both are separate from the design file's own global screen numbering, same as Group C's convention.
