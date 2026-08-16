---
project: 3i
type: standard
status: draft
updated: 2026-08-16
tags:
  - standard
  - meta
---

# 3i Project Standards

This document declares 3i's vocabulary under the repository-wide rules in [/documentation-standards.md](/documentation-standards.md). Where the two differ, the repository standards win; this document only fills in what they leave to each project.

**Status is `draft`.** The module partition below is proposed, not confirmed. Everything downstream — document IDs, folder paths, cross references — depends on it, so it is marked draft until reviewed. Do not assign document IDs from this table before it reaches `current`.

---

## What a Module Means Here

RERAN partitions by user group, because a regulatory platform's natural seam is the stakeholder. 3i does not have that seam: a single learner touches catalogue, delivery, assessment, and certification in one sitting, and a guardian touches billing and communication on that same learner's behalf. Partitioning by user group would put the same subsystem in four folders.

**A module in 3i is a functional area** — a subsystem with its own entities, its own rules, and a boundary that a developer can hold in their head.

| Module folder | Covers | Abbrev. | Status |
| :---- | :---- | :---: | :---- |
| `identity-and-access` | Registration, authentication, age gating, guardian accounts, learner profiles, RBAC | IDA | Not started |
| `catalogue` | Courses, subjects, curriculum structure, enrolment | CAT | Not started |
| `learning-delivery` | Lessons, video delivery, materials, progress tracking | LDL | Not started |
| `assessment` | Question bank, quizzes, examinations, grading | ASM | Not started |
| `certification` | Certificate issuance, verification, retention | CRT | Not started |
| `communication` | Chat rooms, guardian participation, moderation, notifications | COM | Not started |
| `billing` | Subscriptions, seats, checkout, waivers, invoicing | BIL | Not started |
| `administration` | Admin console, operational reporting, institute configuration | ADM | Not started |
| `platform` | Cross-cutting architecture, infrastructure, integrations, NFRs | PLT | Not started |

Abbreviations are for document IDs (`3I-IDA-REQ-001`). The project prefix in an ID is `3I`, uppercase, even though the folder name is `3i`.

`platform` is deliberately last and deliberately thin. It holds only what genuinely belongs to no single functional area — deployment topology, shared NFRs, third-party integration contracts. It is not a drawer for anything hard to place. A document that could live in a real module belongs in that module.

### Status Vocabulary

The status column describes which stages of the derivation chain a module has reached, not how complete any one stage is. A module whose files exist but are thin placeholders is described as *drafted*, not *complete*.

---

## Stage Folders

3i's derivation chain:

```
reference/discovery/  →  requirements/  →  ui/
```

3i has no `reference/source-of-truth/` at present. The client did not supply written specifications; requirements were captured by us through structured clarification rounds and consolidated into an SRD. Under the repository standard on input kinds, that material is discovery, not source of truth — it records our interpretation, not the client's words. If the institute later supplies written material of its own, `source-of-truth/` is created then.

```
modules/<module-name>/
├── README.md                    # module index
├── data-model.md                # entities owned by this module
├── requirements/
│   └── fr-NNN-<name>.md
└── ui/
    ├── README.md                # role × screen matrix
    ├── components.md
    ├── validation-rules.md
    └── screens/
        └── <screen-name>.md
```

A module is not required to have every stage.

### `data-model.md`

Entities are documented in the module that **owns** them, once. A module that reads another module's entity links to it rather than restating its fields. Where ownership is genuinely shared, the entity is documented in the module that writes it, and the reading module records the read in its own `data-model.md` with a link.

---

## The `ui/` Stage

The same many-to-many rule that governs RERAN's UI stage applies here: screens and requirements cross, and a screen such as Video Player or Checkout appears under several requirements.

**Rules:**

1. **One file per distinct screen**, in `ui/screens/`. Never one file per role-screen pair.
2. **Role differences go inside the screen file**, under a `## Role Variations` section. A dashboard that differs for learner, guardian, instructor, and admin is one file with four variations.
3. **Shared logic is documented once** and linked — `components.md`, `validation-rules.md`.
4. **`ui/README.md` carries the role × screen matrix.** This is the index that makes a missing screen visible.
5. **Screens link back to the requirements they satisfy**, and requirement documents list the screens that realise them.
6. **`figma:` frontmatter** on a screen file records the design generated from it.

### Accessibility

Every screen document states its colour contrast pairs explicitly. This is not decoration: a near-black background carrying navy text shipped once on this project and was caught late. Contrast belongs in the specification, where it can be reviewed, not in the design tool, where it is discovered.

---

## Additional Document Types

Beyond the base types in the repository standards, 3i uses:

| Type | Purpose |
| :---- | :---- |
| `functional-requirement` | A group of numbered SRD requirements for one module, with acceptance criteria |
| `compliance` | Analysis of a legal or platform-policy constraint and what it forces |
| `integration` | Contract with a third-party service — Stripe, Bunny Stream, SES |
| `delivery-phase` | One phase of the nine-phase delivery sequence |

---

## File Naming

| Location | Pattern | Example |
| :---- | :---- | :---- |
| `requirements/` | `fr-NNN-<name>.md` | `fr-042-guardian-chat-participation.md` |
| `ui/screens/` | `<screen-name>.md` | `checkout.md` |
| `decisions/` | `dec-NNN-<name>.md` | `dec-001-learner-as-unit-of-study.md` |
| module root | `<document-name>.md` | `data-model.md` |

---

## Requirement Numbering

**SRD v2.0's numbers are canonical.** A requirement's number is assigned by the SRD and is never reassigned, renumbered, or reused — including after a requirement is deprecated. When a requirement is split across module documents, every resulting file carries the original number.

Where a requirement is proposed by us and has no SRD entry, it takes a `P-NN` number in a project-wide proposed list, exactly as RERAN handles proposed services. It enters the `FR-NNN` series only when the client accepts it and the SRD is revised.

This matters more here than the equivalent rule does elsewhere, because the SRD is a client-facing artefact. A requirement number quoted in a client meeting and a requirement number in this repository must mean the same thing.

---

## The `decisions/` Folder

3i keeps a project-root `decisions/` folder holding one file per recorded decision, indexed by [decisions/README.md](decisions/README.md).

Decisions live at project root rather than inside modules because the consequential ones cross module boundaries — the guardian-account model constrains identity, communication, and billing simultaneously. Filing such a decision under one module would hide it from the other two.

Decision IDs take the form `3I-DEC-NNN`, omitting the module segment of the repository's `<PROJECT>-<MODULE>-<TYPE>-<NNN>` format. A cross-cutting decision has no single module, and inventing one to satisfy the format would misfile the decision permanently — an ID does not change when a file moves, which is the whole point of having one.

A decision file records context, the decision, and its consequences. It is never edited to reflect a change of mind: a reversed decision gets `status: superseded` and a new file that cites it under `supersedes`. The reasoning that was wrong is as useful as the reasoning that was right.

---

## Exceptions

| Exception | Reason |
| :---- | :---- |
| No `reference/source-of-truth/` folder | The client supplied no written specifications. Creating the folder empty would breach the repository rule against empty folders and imply evidence that does not exist. |
| Project-root `decisions/` folder | The repository structure defines `reference/` and `modules/` only. Cross-cutting decisions belong to no single module; RERAN sets the precedent for project-root documents with `module-roadmap.md`. |
