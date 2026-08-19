---
project: RERAN
module: financial-trust-institutions
type: reference-sample
status: current
updated: 2026-08-19
contains_proposals: false
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/README.md"
  - "RERAN/modules/financial-trust-institutions/ui/figma-screen-register.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - figma
  - reference
---

# Figma Prompt Packs — Reference Samples

**These files are samples, not specifications.**

They exist so that new Figma prompts follow the same pattern as the ones already written. When you need prompts for a screen that isn't covered here, copy the closest pack in this folder and adapt it, rather than starting from scratch.

**Do not treat these as the source of truth for how a screen behaves.** That lives in [`../screens/`](../screens/) and [`../screens-unified/`](../screens-unified/). These packs were written against those specs on the dates in their frontmatter, and are not maintained in step with them. Where a pack and a spec disagree, the spec wins — and the pack is simply out of date, which is expected and fine for a sample.

---

## Which sample to copy

Two shapes, two examples. Pick by what you're building, not by which service is closest.

| If you're building | Copy | Why |
| :--- | :--- | :--- |
| A full service journey — wizard steps, payment, review, output documents | [`s03-mortgage-registration.md`](s03-mortgage-registration.md) | The most complete journey. Includes the internal certification gate, so it has two screens the other four don't. |
| A list or queue screen reached from the sidebar | [`nav-sidebar-landing-screens.md`](nav-sidebar-landing-screens.md) | Eleven list screens in one pack, sharing one layout. Shows how a repeated structure is stated once and referenced. |

The other four packs are variations on the first, each carrying one distinct component:

| Pack | Notable for |
| :--- | :--- |
| [`s12-register-real-estate-fund-company.md`](s12-register-real-estate-fund-company.md) | Document-dominant step — extended document table with file metadata |
| [`s13-sale-procedure-heirs.md`](s13-sale-procedure-heirs.md) | Repeatable field group — add/remove heir blocks with a running total |
| [`s15-update-title-deed-information.md`](s15-update-title-deed-information.md) | Conditional field selector — checklist that reveals current/new value pairs |
| [`s17-issue-title-deed.md`](s17-issue-title-deed.md) | The simplest complete journey — a good starting point if `s03` is more than you need |

---

## The pattern

What follows is the pattern these packs share, stated as rules. A new pack should follow all of it.

### 1. One file per service, not per screen

A service journey is 10–11 screens. Splitting that across 11 files makes it unusable — you consume these by copying one block at a time out of a single document. The sidebar pack holds 11 screens for the same reason.

### 2. Every prompt is self-contained

Each prompt block is copied into Figma AI on its own, with nothing before it. That means each block repeats the frame declaration, the layer structure, the component-reuse instruction and the simplicity constraint. The repetition is deliberate — a shared preamble the user has to remember to paste first is a reliability problem.

### 3. Fixed opening

Every prompt opens the same way:

```
Create a new screen frame named "[ID] [Screen Name]", 1440px wide, light grey background.

Layer structure exactly:
- [ID] [Screen Name]
  - FI-Sidebar        (instance of the existing sidebar component — do not redraw it; active nav item = "[Item]")
  - MainContent
    - TopBar          (instance of the existing top bar component — title "[Title]", subtitle "[Subtitle]")
    - Workspace
```

Layer naming is fixed across every screen in the design file and must not vary.

### 4. Name components, don't describe them

The Figma file already holds a component library. A prompt should say *reuse the existing X* and let Figma AI find it — never describe what the component looks like, which produces a near-miss duplicate instead of an instance.

Say this:

> Reuse existing components and styles from this file wherever one already exists — cards, buttons, status pills, tables, breadcrumbs, section headers, label/value grids, icons. Do not invent new colours, new type scales, or new card treatments. Match the spacing, corner radius, and white-card-on-grey treatment already used on the Dashboard and Application Review screens.

Naming two built screens as the reference point matters more than listing component names. It gives Figma AI something concrete to match against.

### 5. State the simplicity constraint every time

> Keep it simple: stacked white cards, one blue primary action, plain two-column label/value grids, no illustrations, no gradients, no decorative graphics.

Without this, Figma AI adds visual interest that the design language doesn't want.

### 6. Use negative instructions for anything the product deliberately lacks

This is the rule that most often gets forgotten, and the one that most often causes rework. Figma AI fills gaps helpfully. If the product deliberately has no such thing, say so explicitly.

Real examples from these packs:

- *"This screen must show NO account balance anywhere. There is no standing account and nothing to fund. Do not add a balance card, a top-up action, or a low-balance warning."*
- *"Every service is available to every user. Do not grey out, lock, hide, or badge any service as restricted."*
- *"Do not add any indicator, badge, notice, or reference relating to developer sales or any downstream service that depends on this record."*
- *"Documents are never uploaded from this screen. Do not add an Upload or Add Document button."*
- *"Do not draw a decorative certificate, seal, border, or watermark — output documents are represented as document records with actions."*

Each of these prevents a specific plausible-but-wrong addition. If a spec says something doesn't exist, the prompt needs to say so out loud.

### 7. Content top to bottom, numbered

The workspace content is a numbered list in the order it appears down the screen. Every card gets a heading, its fields, and its sample values. Tables get their columns named and their rows written out in full. Concrete sample content produces better output than field-name placeholders.

### 8. Sample data is consistent across the whole pack

One set of names, references, dates and amounts, listed once at the top of the pack and used identically in every screen. This is what makes a set of screens read as one journey rather than eleven unrelated mockups. Where a pack sits alongside already-built screens, its data should agree with theirs too — the sidebar pack reuses the Dashboard's exact figures for this reason.

### 9. Assumptions table at the top

Every pack opens with a table of the decisions it makes that aren't sourced — channel assumptions, proposed field lists, merged or dropped screens, placeholder fee amounts. Anyone reading the pack later needs to know which parts are documented fact and which are a position taken to make the design buildable.

---

## Screen ID conventions

| Prefix | Used for | Example |
| :--- | :--- | :--- |
| `S{n} – NN` | Screens belonging to service #n's journey | `S3 – 07` |
| `NAV – NN` | Sidebar landing screens | `NAV – 04` |

Both are separate from the design file's global screen numbering (Dashboard is #1, Application Review is #5). See [`../figma-screen-register.md`](../figma-screen-register.md) for the full inventory and build status.

---

## What these packs cover

Sixty-three screens: eleven sidebar landing screens, and 52 across five services (#3, #12, #13, #15, #17). The five services were chosen for design-pattern coverage rather than business priority, on the expectation that the remaining thirteen services reuse the components these establish.
