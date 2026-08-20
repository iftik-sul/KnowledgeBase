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

## The five selected services are now all built

See the original selection reasoning in [module-roadmap.md](../../../../module-roadmap.md) — chosen for pattern coverage, not business priority: the full fee-timing spectrum (before / after / dual-stage / none), the full complexity range (4 fields to a 10-state multi-department flow), creation vs. amendment, a conditional-output pattern, and one genuine live cross-module dependency.

## What's here

| Pack | Contains |
| :---- | :---- |
| [red-sidebar.md](red-sidebar.md) | The `RED-Sidebar` component prompt — RED's persistent left navigation, adapted from Group C's `FI-Sidebar` component spec, with RED's own 12-item nav list (see [navigation.md](../../navigation.md)). Built and confirmed in Figma, 2026-08-19. |
| [nav-sidebar-landing-screens.md](nav-sidebar-landing-screens.md) | Twelve landing screens, one per sidebar item — `NAV – 01` through `NAV – 12`. Includes Dashboard, unlike Group C's equivalent pack, since nothing in RED had been built in Figma yet when this pack was written. `contains_proposals: true` — sample data invented for this pack, deliberately kept consistent with Group C's own built sample data. |
| [s13-register-real-estate-project.md](s13-register-real-estate-project.md) | Eleven screens — `S13 – 01` through `S13 – 11`. Fee paid after decision, longest status flow in the module (10 states), a hard RERA-acceptance gate mid-flow. Does **not** copy Group C's `s03` single-wizard shape — splits into a 4-step wizard for the initial application plus the module's vertical status timeline for everything after submission. Continues `APP-2026-0221`, Gwarinpa Heights, already shown mid-flow in `nav-sidebar-landing-screens.md`. `contains_proposals: true`. |
| [s1-register-initial-sale.md](s1-register-initial-sale.md) | Ten screens — `S1 – 01` through `S1 – 10`. Fee paid before decision, single continuous 5-step wizard, no internal-certification stage. Continues `APP-2026-0219` / Unit A-120, Banana Island Villas. `contains_proposals: true`. |
| [s6-register-mortgage-linked-sale.md](s6-register-mortgage-linked-sale.md) | Eleven screens — `S6 – 01` through `S6 – 11`. The genuine live cross-module dependency. Shows **two outcomes**: a successful path where the cited mortgage is already `Completed` on Group C's side, and `S6 – 09`, the automatic, immediate return when it isn't — reusing `APP-2026-0228`, already shown "Returned" in `nav-sidebar-landing-screens.md`. `contains_proposals: true`. |
| [s24-register-amend-project-details.md](s24-register-amend-project-details.md) | Eleven screens — `S24 – 01` through `S24 – 11`. The only pack with two genuinely separate payment stages and a conditional output determined by the project's completion status. The first **amend** pattern here — `S24 – 02` opens pre-filled, not blank. Shows both outputs: `S24 – 10` (Banana Island Villas → Electronic Map) and `S24 – 11` (Apo Green Residences, already established as completed → Title Deed). `contains_proposals: true`. |
| [s16-rename-real-estate-project.md](s16-rename-real-estate-project.md) | Four screens — `S16 – 01` through `S16 – 04`. The simplest baseline: no fee, 4 fields, 30-minute processing, no multi-gate workflow. Deliberately a quarter the size of every other pack — no step tracker (genuinely one step), no payment screens (no fee), and the whole journey resolves same-day. Renames `PRJ-2026-0019`, Lekki Pearl Estate, to "Lekki Pearl Residences." `contains_proposals: true`. |

## Screen ID conventions

**Established 2026-08-19**, following Group C's `S{n} – NN` / `NAV – NN` pattern directly (see [Group C's README](../../financial-trust-institutions/ui/figma-prompts/README.md#screen-id-conventions)):

| Prefix | Used for | Example |
| :---- | :---- | :---- |
| `NAV – NN` | Sidebar landing screens | `NAV – 06` (Applications) |
| `S{n} – NN` | Screens belonging to service #n's journey | `S16 – 02` (Service #16's single form screen) |

Both are separate from the design file's own global screen numbering, same as Group C's convention.
