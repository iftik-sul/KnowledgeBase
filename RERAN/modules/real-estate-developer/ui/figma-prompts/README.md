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
| [nav-sidebar-landing-screens.md](nav-sidebar-landing-screens.md) | Twelve landing screens, one per sidebar item — `NAV – 01` through `NAV – 12`. Includes Dashboard, unlike Group C's equivalent pack, since nothing in RED had been built in Figma yet when this pack was written. `contains_proposals: true` — sample data invented for this pack, deliberately kept consistent with Group C's own built sample data. |
| [s13-register-real-estate-project.md](s13-register-real-estate-project.md) | Eleven screens covering Service #13's full application journey — `S13 – 01` through `S13 – 11`. First of the five services selected for full UI design. Does **not** copy Group C's `s03` single-wizard shape — #13's own sourced workflow has a hard RERA-acceptance gate mid-flow, so this pack splits into a 4-step wizard for the initial application plus the module's vertical status timeline for everything after submission. Continues `APP-2026-0221`, Gwarinpa Heights, already shown mid-flow in `nav-sidebar-landing-screens.md`. `contains_proposals: true`. |
| [s1-register-initial-sale.md](s1-register-initial-sale.md) | Ten screens covering Service #1's full application journey — `S1 – 01` through `S1 – 10`. Second of the five. Single continuous 5-step wizard, since #1's own workflow has no mid-flow gate — payment sits before submission, and RERA reviews directly with no internal-certification stage. Continues `APP-2026-0219` / Unit A-120, Banana Island Villas. `contains_proposals: true`. |
| [s6-register-mortgage-linked-sale.md](s6-register-mortgage-linked-sale.md) | Eleven screens covering Service #6's full application journey — `S6 – 01` through `S6 – 11`. Third of the five, and the one with a genuine live cross-module dependency. Shows **two outcomes**: a successful path where the cited mortgage is already `Completed` on Group C's side, and `S6 – 09`, an alternate ending showing the automatic, immediate return when it isn't. The alternate-return scenario reuses `APP-2026-0228` (Unit B-204, Lekki Pearl Estate), already shown "Returned" in `nav-sidebar-landing-screens.md`. `contains_proposals: true`. |
| [s24-register-amend-project-details.md](s24-register-amend-project-details.md) | Eleven screens covering Service #24's full application journey — `S24 – 01` through `S24 – 11`. Fourth of the five, and the only pack with two genuinely separate payment stages (application approval fee before Survey Department review, approval fee in the real estate records after RERA approval) plus a conditional output determined automatically by the project's completion status, not chosen by the developer. Also the first **amend** pattern in this folder — `S24 – 02` opens pre-filled with the project's existing data via a Current-vs-Updated comparison, unlike every other pack's blank starting form. Shows both possible outputs: `S24 – 10` (Banana Island Villas, not completed → Electronic Map) and `S24 – 11`, an alternate ending on Apo Green Residences (completed → Title Deed), already established as "an older completed project" in `nav-sidebar-landing-screens.md`'s Payment History. `contains_proposals: true`. |

One more service-journey pack remains from the selected five: **#16** (Rename Real Estate Project — the simplest baseline).

## Screen ID conventions

**Established 2026-08-19**, following Group C's `S{n} – NN` / `NAV – NN` pattern directly (see [Group C's README](../../financial-trust-institutions/ui/figma-prompts/README.md#screen-id-conventions)):

| Prefix | Used for | Example |
| :---- | :---- | :---- |
| `NAV – NN` | Sidebar landing screens | `NAV – 06` (Applications) |
| `S{n} – NN` | Screens belonging to service #n's journey | `S24 – 09` (Service #24's second, post-approval fee) |

Both are separate from the design file's own global screen numbering, same as Group C's convention.
