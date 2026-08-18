---
project: 3i
type: standard
status: draft
updated: 2026-08-18
tags:
  - standard
  - meta
---

# 3i Project Standards

This document declares 3i's vocabulary under the repository-wide rules in [/documentation-standards.md](/documentation-standards.md). Where the two differ, the repository standards win.

**Status is `draft`: the module partition is not settled.** Document IDs must not be assigned from the table below until it reaches `current`, because an ID does not change when a file moves.

---

## Input Kinds

3i has no `reference/source-of-truth/`. The client supplied nothing in writing — the entire requirement set was gathered verbally and expanded by us. Creating the folder would breach the repository rule against empty folders and imply evidence that does not exist.

SRD v2.0 is not source of truth and is not discovery either. It is our document, but it is also the fixed, change-controlled baseline that defines scope. It lives in:

```
reference/baseline/
```

Vendor-authored, client-approved, frozen, versioned. Corrections go through §21.3 change control, not through edits. A superseded version keeps `status: superseded` and stays in place.

This category is repository-wide, not a 3i quirk — see `/documentation-standards.md`.

---

## Derivation Chain

```
reference/baseline/  →  modules/  →  ui/
```

The baseline is the parent of every requirement document. Nothing sits above it.

---

## Requirement Numbering

**The SRD's requirement codes are canonical.** Format is `FR-<CODE>-<nn>` — `FR-AUTH-03`, `FR-CHAT-07`, `FR-BILL-02` — and `NFR-<nn>` for non-functional requirements, which are unprefixed and run in a single series to 32.

A requirement number is never reassigned, renumbered, or reused, including after deprecation. When a requirement is split across documents, every resulting file carries the original code.

This matters more here than elsewhere: the SRD is client-facing. A code quoted in a client meeting and a code in this repository must mean the same thing.

Requirements proposed by us with no SRD entry take a `P-nn` number in a project-wide proposed list, exactly as RERAN handles proposed services. They enter the `FR-` series only when the client accepts them and the SRD is revised under §21.3.

### The 19 Requirement Codes

| Code | Area | Count |
| :---- | :---- | ----: |
| AUTH | Registration and authentication | 13 |
| FAM | Family accounts and learner profiles | 10 |
| RBAC | Roles and permissions | 5 |
| INST | Instructor onboarding | 7 |
| CRS | Course catalogue and management | 12 |
| MAT | Course materials and video delivery | 15 |
| BAT | Batches and live sessions | 7 |
| ENR | Enrolment, waitlist and age gating | 7 |
| QB | Question bank | 7 |
| EX | Examinations | 8 |
| CERT | Certificates | 9 |
| BILL | Subscriptions and billing | 8 |
| WAV | Waivers | 9 |
| REF | Refunds | 5 |
| CHAT | Group chat and moderation | 15 |
| NOT | Notifications | 8 |
| CMS | Content management and public site | 7 |
| REP | Reports and exports | 5 |
| LOC | Localisation | 6 |

---

## Modules — NOT YET DECIDED

A module in 3i is a **functional area** owning one or more requirement codes. The code in an ID stays the SRD's; the folder is ours.

The partition below is **proposed and awaiting review**. It is recorded here so the reasoning is not lost, not because it is agreed.

| Proposed module | Owns | FRs |
| :---- | :---- | ----: |
| `identity-and-access` | AUTH, RBAC, FAM | 28 |
| `commerce` | BILL, WAV, REF | 22 |
| `communication` | CHAT, NOT | 23 |
| `materials` | MAT | 15 |
| `assessment` | QB, EX | 15 |
| `learning-delivery` | BAT, ENR | 14 |
| `catalogue` | CRS | 12 |
| `certification` | CERT | 9 |
| `instructors` | INST | 7 |
| `public-site` | CMS | 7 |
| `localisation` | LOC | 6 |
| `reporting` | REP | 5 |
| `platform` | — | 32 NFRs |

Three judgement calls worth reviewing rather than accepting silently:

1. **AUTH, RBAC and FAM merged.** §3 is titled "read this first" and defines Account and Learner as one model. Splitting it across folders would fracture the thing the baseline says governs every other section.
2. **CMS and REP kept apart** despite both being administrative in feel. A public SEO site and admin analytics share no entities. Merging them would create the junk drawer this document warns against.
3. **LOC as its own module** rather than a cross-cutting note. FR-LOC-04 requires full RTL layout mirroring across web and both mobile apps — that needs real UI documentation, not a paragraph in an NFR file.

The delivery phases in §21.1 are **not** a partition. They are temporal, and Hardening is not a subsystem. Documentation is never organised by phase.

---

## Module Folder Shape

```
modules/<module-name>/
├── README.md                    # module index
├── data-model.md                # entities owned by this module
├── requirements/
│   └── <code>-<name>.md
└── ui/
    ├── README.md                # role × screen matrix
    ├── components.md
    ├── validation-rules.md
    └── screens/
        └── <screen-name>.md
```

A module is not required to have every stage.

Entities are documented in the module that **owns** them, once. A module that reads another module's entity links to it rather than restating its fields.

---

## The `ui/` Stage

Screens and requirements cross — a screen such as Checkout or Video Player serves several requirements.

1. **One file per distinct screen.** Never one file per role-screen pair.
2. **Role differences go inside the screen file**, under `## Role Variations`.
3. **Shared logic documented once** and linked — `components.md`, `validation-rules.md`.
4. **`ui/README.md` carries the role × screen matrix**, which is what makes a missing screen visible.
5. **Screens cite the requirement codes they satisfy**, and requirement documents list the screens realising them.
6. **`figma:` frontmatter** records the design generated from a screen file.

### Accessibility

NFR-12 requires WCAG 2.2 Level AA with 4.5:1 contrast. Every screen document states its contrast pairs explicitly. A near-black background carrying navy text shipped once on this project and was caught late — contrast belongs in the specification, where it is reviewable, not in the design tool, where it is discovered.

RTL is not a rendering concern. FR-LOC-04 requires navigation, alignment, icon direction, and progress indicators to mirror for Arabic and Urdu. Every screen document states its RTL behaviour.

---

## Cross-Cutting Documents

Some rules span every module. They are documented **once**, at project root, and linked — never restated, because restated rules go stale silently.

| Document | Why it cannot live in a module |
| :---- | :---- |
| [age-and-safeguarding.md](age-and-safeguarding.md) | Age rules sit in AUTH, FAM, CRS, ENR, CHAT and INST simultaneously |
| [decisions/](decisions/README.md) | The consequential decisions constrain several modules at once |
| [open-questions.md](open-questions.md) | Tracks unresolved items across the whole project |

---

## Additional Document Types

| Type | Purpose |
| :---- | :---- |
| `functional-requirement` | A group of SRD requirements for one module, with acceptance criteria |
| `compliance` | Analysis of a legal or platform-policy constraint and what it forces |
| `integration` | Contract with a third-party service — Stripe, Bunny Stream, SES |

---

## File Naming

| Location | Pattern | Example |
| :---- | :---- | :---- |
| `reference/baseline/` | `srd-v<version>.md` | `srd-v2.0.md` |
| `requirements/` | `<code>-<name>.md` | `chat-moderation.md` |
| `ui/screens/` | `<screen-name>.md` | `checkout.md` |
| `decisions/` | `dec-NNN-<name>.md` | `dec-001-learner-as-unit-of-study.md` |

---

## Decisions

Decision IDs take the form `3I-DEC-NNN`, omitting the module segment of the repository's format. A cross-cutting decision has no single module, and inventing one to satisfy the format would misfile it permanently.

A decision is never edited to reflect a change of mind. A reversed decision gets `status: superseded` and a new file citing it under `supersedes`.

---

## Exceptions

| Exception | Reason |
| :---- | :---- |
| No `reference/source-of-truth/` | The client supplied nothing in writing. Verified 2026-08-18, not assumed. |
| `reference/baseline/` | New input kind — vendor-authored, client-approved, change-controlled. Now repository-wide. |
| Project-root cross-cutting documents | Rules spanning six modules belong in none of them. RERAN sets the precedent with `module-roadmap.md`. |
