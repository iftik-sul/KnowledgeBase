---
project: KnowledgeBase
type: standard
status: current
updated: 2026-08-18
tags:
  - standard
  - meta
---

# Documentation Standards

## Purpose

This document defines how documentation is written, named, structured, and versioned across every project in the KnowledgeBase repository.

It exists so that:

- Any document can be located without asking someone where it is.
- Any reader — human or AI — can tell whether a document is current, superseded, or raw input.
- Every derived document can be traced back to what it was written from.
- Documents can be chunked and embedded for semantic search without losing context or citation accuracy.

Projects differ. A regulatory platform and a manufacturing ERP do not partition into the same kind of modules or produce the same kind of documents. This document therefore defines the **shape** that every project follows, and leaves the **vocabulary** to each project.

---

## Scope

| Defined here (applies to every project) | Defined per project in `<PROJECT>/project-standards.md` |
|---|---|
| The `reference/` and `modules/` split | What a "module" means in this project |
| Stage folders and the derivation chain | Which stage folders exist and in what order |
| Frontmatter fields and their meaning | Project-specific `type` values |
| File naming, Markdown rules, size limits | Module abbreviations for document IDs |
| Versioning, status, retirement | Any documented exception to these standards |
| Cross references, source hierarchy, AI guidelines | |

A project without a `project-standards.md` inherits the base vocabulary in this document.

---

## Repository Structure

```
KnowledgeBase/
├── README.md                      # Repository overview and project index
├── documentation-standards.md     # This document
└── <PROJECT>/
    ├── README.md                  # Project overview, status, stack, entry points
    ├── project-standards.md       # This project's module definition and vocabulary
    ├── reference/                 # Inputs — material this project was built from
    │   ├── source-of-truth/       # Supplied by the client, frozen
    │   ├── baseline/              # Written by us, approved by the client, change-controlled
    │   └── discovery/             # Captured by us from meetings and discussion
    └── modules/
        └── <module-name>/
            ├── README.md          # Module index
            └── <stage>/           # Stage folders, declared in project-standards.md
```

One project folder per system. Two systems for two different clients are two projects, even when they are the same kind of software.

Project folder names are UPPERCASE for acronyms (`RERAN`) and PascalCase otherwise (`LoyaltyPoints`).

A project uses whichever `reference/` subfolders it actually has material for. None of the three is mandatory.

---

## Folder Standards

| Folder | Contains | Editable | Authoritative |
|---|---|---|---|
| `reference/source-of-truth/` | Material supplied by the client, converted to Markdown but not rewritten | No | No — provenance only |
| `reference/baseline/` | A specification written by us and approved by the client as the agreed scope | No — changes go through change control | Yes — for scope, not for implementation |
| `reference/discovery/` | Requirements we captured ourselves from meetings and discussion | Yes | No — superseded by module docs |
| `modules/` | Documents written from the inputs, structured for development use | Yes | Yes |
| `<PROJECT>/README.md` | Project overview and index | Yes | Yes |

**Rules:**

1. `source-of-truth/` is read-only once committed. Corrections are never applied to these files; they record what the client actually supplied.
2. `baseline/` is read-only in the same way, but for a different reason. A baseline is the agreed definition of scope, so an untracked edit silently moves the line between delivery and change request. Revisions produce a new version through the project's change-control process; they never overwrite.
3. `discovery/` is editable, because it records our understanding rather than the client's words. When understanding changes, the file changes. Never present a discovery document as something the client wrote.
4. `modules/` is where all interpretation, restructuring, clarification, and consolidation lives. Development works from `modules/` only.
5. A module partitions the project along its natural axis — user groups, functional areas, subsystems, whichever the project declares. Never along document type.
6. Every module folder contains a `README.md` listing its documents and their status.
7. No empty folders. A folder is created when its first document exists.

---

## Input Kinds

Not every project starts with client documents. Some start with a conversation.

- **Client-supplied material** → `reference/source-of-truth/`. Frozen, versioned by the client's own version numbers, never edited.
- **A specification we wrote and the client approved** → `reference/baseline/`. Frozen, versioned by us, revised only through change control.
- **Our own requirement capture** → `reference/discovery/`. Meeting notes, requirement summaries, and understandings written up after discussion. Edited freely as understanding sharpens.

The distinction matters because a frozen folder full of our own reconstructions is a rule nobody can follow. Keeping them apart means `source-of-truth/` stays trustworthy as evidence, and `discovery/` stays honest about being our interpretation.

### Why `baseline/` exists separately

An engagement where the client supplies nothing written still produces a document that governs delivery. That document fits neither of the other two folders.

It is not source of truth: we wrote it, and filing our own reasoning as client evidence would let us cite ourselves as proof of what was asked for. That is exactly the confusion the source-of-truth rule prevents.

It is not discovery either: discovery is editable and explicitly never a final word, whereas a baseline defines what is in scope, carries acceptance criteria, and is the thing a change request is measured against. Filing it somewhere labelled non-authoritative would be wrong in the opposite direction.

**The test is authorship and standing together.** Client wrote it → `source-of-truth/`. We wrote it and the client agreed to it as scope → `baseline/`. We wrote it and it is our current understanding → `discovery/`.

A project may hold all three. Where a baseline was derived from client material, its `derived_from` cites that material.

### Approval

A baseline document records how it was approved, in the `approval` frontmatter field:

| Value | Meaning |
|---|---|
| `written` | The client confirmed the baseline in writing. Cite the document under `derived_from` or store it in `source-of-truth/` |
| `verbal` | Agreed in conversation only |
| `pending` | Issued, not yet agreed |

`verbal` and `pending` are recorded rather than hidden. A baseline is the instrument a change request is measured against, so whether it is actually agreed is a fact the repository should state plainly instead of leaving to assumption.

All three are inputs. None is authoritative for **how** the system is built — that is always `modules/`.

---

## Stage Folders and the Derivation Chain

Documentation is produced in stages, each derived from the one before. A project declares its own chain in `project-standards.md`. Three examples:

```
RERAN:  source-of-truth  →  service-flows/  →  ui/
ERP:    discovery        →  process-flows/  →  ui/
3i:     baseline         →  requirements/   →  ui/
```

Stage folders live inside a module. Their names are the project's own; the ordering is what matters.

**`derived_from` cites the immediate parent in the chain, not the ultimate origin.** A UI document cites the flow document it was written from; that flow document cites the input material. This keeps the chain traversable in both directions: when an input changes, you find the flows that cite it, and from those the UI documents that cite them.

Citing everything back to the original source in every file defeats the purpose — a query that returns every file returns no information.

---

## File Naming Convention

**Format:** `kebab-case.md` — lowercase, hyphen-separated, no spaces, no underscores.

The folder path already carries the project, module, and stage, so filenames do not repeat them.

| Correct | Incorrect |
|---|---|
| `register-property-sale.md` | `RERAN_ individual user_service_flows.md` |
| `payment.md` | `RERAN_real_estate_developer_ui.md` |

Where a project numbers its documents for ordering, the number leads: `service-06-register-property-sale.md`.

**Exception — `source-of-truth/` and `baseline/`:** files in both keep a version suffix, since multiple versions coexist by design (`prd-v1.0.md`, `service-flows-v2.md`, `srd-v2.0.md`). If the client's original filename carries meaning, preserve it in the `original_filename` frontmatter field rather than in the filename.

---

## Markdown Standards

1. **One `# H1` per file**, matching the document title. All other headings descend from it without skipping levels.
2. **Headings are chunk boundaries.** Each `##` section should stand alone well enough to be read out of context, because that is how the retrieval layer will serve it.
3. **One topic per file.** Target under 50 KB. A file past that is a folder waiting to be split.
4. **Tables for structured data** (fields, statuses, roles, permissions). Prose for rules and rationale.
5. **Fenced code blocks with a language tag** for schemas, payloads, and examples.
6. **Explicit terms over pronouns.** Write "the developer submits the application," not "they submit it" — a chunk retrieved in isolation has no antecedent.
7. **No screenshots as the only source of a rule.** If an image carries information, transcribe it into text beneath the image.
8. **Define acronyms on first use in each file**, not once per project.

A `source-of-truth/` or `baseline/` document may exceed the 50 KB target. Those files are frozen artefacts and are never split, because splitting would change what was supplied or agreed.

---

## Metadata Standard

Every `.md` file opens with YAML frontmatter.

**Required in all files:**

```yaml
---
project: RERAN
type: service-flow
status: current
updated: 2026-08-09
---
```

**Required additionally in `modules/` files:**

```yaml
module: individual-user
derived_from:
  - reference/source-of-truth/service-flows-v2.md
```

**Required additionally in `source-of-truth/` files:**

```yaml
received: 2026-07-22
original_filename: RERAN Service Flows (Final) v2.docx
```

**Required additionally in `baseline/` files:**

```yaml
version: "2.0"
approval: verbal
approved: 2026-08-04
```

**Optional:**

```yaml
id: RERAN-IU-FLOW-001
tags: [flow, individual-user]
supersedes: modules/individual-user/service-flows/register-sale-v1.md
figma: https://figma.com/file/...
owner: Iftikher
```

**Field definitions:**

| Field | Values | Meaning |
|---|---|---|
| `project` | Project folder name | Which project this belongs to |
| `module` | Module folder name | Which module this belongs to |
| `type` | See Document Types | What kind of document this is |
| `status` | `current`, `draft`, `superseded`, `deprecated` | Whether this can be relied on |
| `updated` | `YYYY-MM-DD` | Last meaningful content change |
| `derived_from` | Repo-relative paths | The immediate parent(s) this was written from |
| `received` | `YYYY-MM-DD` | When the client supplied this file |
| `version` | String | The baseline's own version number |
| `approval` | `written`, `verbal`, `pending` | How the client agreed to this baseline |
| `approved` | `YYYY-MM-DD` | When approval was given. Omit when `pending` |
| `figma` | URL | Design generated from this specification |

---

## Document Types

Every project may use these base types:

| Type | Purpose |
|---|---|
| `overview` | Project or module summary and index |
| `standard` | Meta-documentation such as this file |
| `baseline` | An approved specification defining agreed scope |
| `requirements` | What the system must do |
| `ui-spec` | Screen or interface specification |
| `data-model` | Entities, fields, relationships |
| `api` | Endpoint contracts |
| `architecture` | System design and infrastructure |
| `decision` | A recorded decision with context and consequences |
| `meeting-note` | Dated record of a discussion |
| `glossary` | Domain terminology |

Projects declare additional types in their `project-standards.md` — RERAN adds `service-flow`, `registration-flow`, and `user-group`; an ERP might add `process-flow`. New types are declared before first use, not invented ad hoc.

---

## Versioning

**Git is the version history.** Filenames are not a changelog.

| Case | Handling |
|---|---|
| Editing a module document | Edit in place, bump `updated`, commit with a descriptive message |
| Client sends a revised document | Add as a new file with the client's version suffix; set the previous file's `status: superseded` |
| A baseline is revised through change control | Add as a new file with the next version suffix; set the previous file's `status: superseded`. Never edit in place |
| A module document is replaced by a restructured one | New file sets `supersedes:`; old file sets `status: superseded` |
| A feature is dropped | `status: deprecated`, file stays for history |

Never delete a document that has been committed. Status changes are how things retire, because deleted files disappear from search while their conclusions are still cited elsewhere.

**Commit messages:** `<project>: <what changed>` — for example, `RERAN: split individual-user service flows into per-service files`.

---

## Document IDs

Optional but recommended for anything referenced from a ticket, a spec, or another document.

**Format:** `<PROJECT>-<MODULE>-<TYPE>-<NNN>` — for example, `RERAN-IU-FLOW-001`.

Module abbreviations are declared in `project-standards.md`. Numbers are assigned sequentially within a project-module-type combination and are never reused, even after deprecation. An ID, once assigned, does not change when the file is renamed or moved. That is the point of having one.

A document belonging to no single module — a cross-cutting rule or a project-wide decision — omits the module segment: `3I-DEC-001`. Inventing a module to satisfy the format would misfile it permanently.

---

## Cross References

Link with **repo-relative paths** from the repository root, so links survive both GitHub rendering and local editors:

```markdown
See [Register Property Sale](/RERAN/modules/individual-user/service-flows/service-06-register-property-sale.md).
```

**Rules:**

1. Link to a heading anchor when referring to a specific rule, not just the file.
2. Never duplicate content across files to avoid a link. Duplicated content diverges; links do not.
3. When a document depends on a rule defined elsewhere, link it rather than restating it — restated rules become stale silently.
4. Reference input material through `derived_from` frontmatter, not through inline links in the body.
5. Where a shared artefact is used by many documents — a UI screen used across many flows — document it once and link both ways: the flow lists the screens it uses, the screen lists the flows that use it.

---

## Source Hierarchy

When two documents disagree, resolve in this order:

1. **`modules/` with `status: current`** — authoritative for all development work.
2. **`reference/baseline/` with `status: current`** — authoritative for what is in scope and what acceptance means, but not for how it is built.
3. **`reference/source-of-truth/` with `status: current`** — authoritative for what the client requested.
4. **`reference/discovery/`** — our own capture; useful context, never a final word.
5. **Anything with `status: superseded` or `deprecated`** — historical only, never a basis for implementation.

A baseline sits above source-of-truth because it is later and agreed: it records what was settled, where source-of-truth records what was originally asked. Where the two conflict on scope, the baseline governs and the conflict is worth recording, since it usually means a request was consciously dropped or changed.

**The working rule:** if a module document contradicts a client source document, that is a flag, not a fallback. It means either the source was interpreted deliberately — in which case the reasoning belongs in the module document — or the module drifted and needs correcting. Do not silently prefer one; record the resolution.

A module document that contradicts the **baseline** is a different matter. That is scope drift, and it is resolved through change control rather than by editing either document.

Material outside this repository — chat threads, email, verbal agreements, meeting recordings — has no standing until it is written into a document here.

---

## AI Guidelines

This repository is intended to be consumed by AI assistants through indexing, retrieval, and MCP integration.

**For retrieval and indexing:**

1. Index `reference/` and `modules/`, but answer from `modules/`. Input documents are provenance, cited only when the question is specifically about what was originally supplied, agreed, or discussed.
2. Filter on `status`. Never answer from `superseded` or `deprecated` content without labelling it as historical.
3. Chunk on heading boundaries. Attach `project`, `module`, `type`, and file path to every chunk so citations resolve to a location, not just a document.
4. Prefer smaller, well-scoped files over large ones. This is the reason for the 50 KB guidance in Markdown Standards.
5. Questions about scope — whether something is included, what acceptance requires — are answered from `baseline/` where one exists, not from `modules/`.

**For assistants generating or editing documentation:**

1. Write new documents into `modules/`. Never write into `source-of-truth/` or `baseline/`.
2. Populate complete frontmatter, including `derived_from` citing the immediate parent stage.
3. Read the project's `project-standards.md` before creating files in that project.
4. When a request cannot be answered from repository content, say so rather than inferring. An invented business rule that reads plausibly is worse than a gap.
5. Cite the file path for every substantive claim drawn from the repository.
6. When restructuring, preserve every rule from the original. Restructuring changes organization, never content — content changes are a separate, deliberate commit.
7. Never file a document we wrote under `source-of-truth/`, however closely it reflects what the client wants. If it needs to be frozen and it is ours, it is a baseline.

**For assistants writing code from this repository:**

Implement against `modules/`. If a needed detail is missing there, check `reference/` and, if the detail exists, raise it as a documentation gap before writing the code.
