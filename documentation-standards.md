---
project: KnowledgeBase
type: standard
status: current
updated: 2026-08-09
tags:
  - standard
  - meta
---

# Documentation Standards

## Purpose

This document defines how documentation is written, named, structured, and versioned in the KnowledgeBase repository.

It exists so that:

- Any document can be located without asking someone where it is.
- Any reader — human or AI — can tell whether a document is current, superseded, or raw client input.
- Every derived document can be traced back to the client material it came from.
- Documents can be chunked and embedded for semantic search without losing context or citation accuracy.

These standards are binding for all projects in this repository. Where a project needs an exception, the exception is documented in that project's `README.md` with a reason.

---

## Repository Structure

```
KnowledgeBase/
├── README.md                      # Repository overview and project index
├── documentation-standards.md     # This document
└── <PROJECT>/
    ├── README.md                  # Project overview, status, stack, entry points
    ├── modules/                   # Authoritative, curated documentation
    │   └── <module-name>/
    │       └── <document>.md
    └── reference/
        └── source-of-truth/       # Unmodified client-supplied material
            └── <client-document>.md
```

Every project folder follows this shape. Additional folders (`decisions/`, `api/`, `architecture/`) may be added at the project root when needed, but `modules/` and `reference/` are mandatory.

Project folder names are UPPERCASE for acronyms (`RERAN`) and PascalCase otherwise (`LoyaltyPoints`).

---

## Folder Standards

| Folder | Contains | Editable | Authoritative |
|---|---|---|---|
| `reference/source-of-truth/` | Files received from the client, converted to Markdown but not rewritten | No | No — provenance only |
| `modules/` | Documents written from source material, structured for development use | Yes | Yes |
| `<PROJECT>/README.md` | Project overview and index | Yes | Yes |

**Rules:**

1. `source-of-truth/` is read-only once committed. Corrections are never applied to these files; they record what the client actually supplied.
2. `modules/` is where all interpretation, restructuring, clarification, and consolidation lives. Development works from `modules/` only.
3. A module folder maps to a real system boundary — a user group, a subsystem, or a bounded domain (`individual-user`, `real-estate-developer`). Not to a document type.
4. Every module folder contains a `README.md` listing its documents and their status.
5. No empty folders. A folder is created when its first document exists.

---

## File Naming Convention

**Format:** `kebab-case.md` — lowercase, hyphen-separated, no spaces, no underscores.

The folder path already carries the project and module, so filenames do not repeat them.

| Correct | Incorrect |
|---|---|
| `service-flows.md` | `RERAN_ individual user_service_flows.md` |
| `registration-flows.md` | `RERAN_registration_flows.md` |
| `user-group-structure.md` | `RERAN user group structure v2.md` |

**Exception — `source-of-truth/`:** client files keep a version suffix, since multiple versions coexist by design:

```
prd-v1.0.md
service-flows-v2.md
```

If the client's original filename carries meaning, preserve it in the `original_filename` frontmatter field rather than in the filename itself.

---

## Markdown Standards

1. **One `# H1` per file**, matching the document title. All other headings descend from it without skipping levels.
2. **Headings are chunk boundaries.** Each `##` section should stand alone well enough to be read out of context, because that is how the retrieval layer will serve it.
3. **One topic per file.** Target under 50 KB. A file past that is a folder waiting to be split — split by service, flow, or entity, not by arbitrary length.
4. **Tables for structured data** (fields, statuses, roles, permissions). Prose for rules and rationale.
5. **Fenced code blocks with a language tag** for schemas, payloads, and examples.
6. **Explicit terms over pronouns.** Write "the developer submits the application," not "they submit it" — a chunk retrieved in isolation has no antecedent.
7. **No screenshots as the only source of a rule.** If an image carries information, transcribe it into text beneath the image.
8. **Define acronyms on first use in each file**, not once per project.

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
  - reference/source-of-truth/prd-v1.0.md
```

**Required additionally in `source-of-truth/` files:**

```yaml
received: 2026-07-22
original_filename: RERAN Service Flows (Final) v2.docx
```

**Optional:**

```yaml
id: RERAN-IU-FLOW-001
tags: [flow, individual-user]
supersedes: modules/individual-user/service-flows-v1.md
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
| `derived_from` | List of repo-relative paths | Which source material this was written from |
| `received` | `YYYY-MM-DD` | When the client supplied this file |

`derived_from` is the field that makes traceability work. When a client sends a new version of a source document, every module document citing the old path is a re-sync candidate — findable with a single search.

---

## Document Types

`type` must be one of:

| Type | Purpose |
|---|---|
| `overview` | Project or module summary and index |
| `prd` | Product requirements |
| `service-flow` | Step-by-step flow for a service or transaction |
| `registration-flow` | Onboarding and registration sequences |
| `user-group` | Roles, permissions, and user group structure |
| `data-model` | Entities, fields, relationships |
| `api` | Endpoint contracts |
| `architecture` | System design and infrastructure |
| `decision` | A recorded decision with context and consequences |
| `meeting-note` | Dated record of a discussion |
| `glossary` | Domain terminology |
| `standard` | Meta-documentation such as this file |

New types are added to this table before first use, not invented ad hoc.

---

## Versioning

**Git is the version history.** Filenames are not a changelog.

| Case | Handling |
|---|---|
| Editing a module document | Edit in place, bump `updated`, commit with a descriptive message |
| Client sends a revised document | Add as a new file with the client's version suffix; set the previous file's `status: superseded` |
| A module document is replaced by a restructured one | New file sets `supersedes:`; old file sets `status: superseded` |
| A feature is dropped | `status: deprecated`, file stays for history |

Never delete a document that has been committed. Status changes are how things retire, because deleted files disappear from search while their conclusions are still cited elsewhere.

**Commit messages:** `<project>: <what changed>` — for example, `RERAN: split individual-user service flows into per-service files`.

---

## Document IDs

Optional but recommended for anything that will be referenced from a ticket, a spec, or another document.

**Format:** `<PROJECT>-<MODULE>-<TYPE>-<NNN>`

```
RERAN-IU-FLOW-001
RERAN-RED-FLOW-014
RERAN-CORE-DM-003
```

Module abbreviations are declared in the project `README.md` (`IU` = individual-user, `RED` = real-estate-developer). Numbers are assigned sequentially within a project-module-type combination and are never reused, even after deprecation.

An ID, once assigned, does not change when the file is renamed or moved. That is the point of having one.

---

## Cross References

Link with **repo-relative paths** from the repository root, so links survive both GitHub rendering and local editors:

```markdown
See [Individual User Service Flows](/RERAN/modules/individual-user/service-flows.md).
```

**Rules:**

1. Link to a heading anchor when referring to a specific rule, not just the file.
2. Never duplicate content across files to avoid a link. Duplicated content diverges; links do not.
3. When a module document depends on a rule defined elsewhere, link it rather than restating it — restated rules become stale silently.
4. Reference source material through `derived_from` frontmatter, not through inline links in the body.

---

## Source Hierarchy

When two documents disagree, resolve in this order:

1. **`modules/` with `status: current`** — authoritative for all development work.
2. **`reference/source-of-truth/` with `status: current`** — authoritative for what the client requested, but not for how it is built.
3. **Anything with `status: superseded` or `deprecated`** — historical only, never a basis for implementation.

**The working rule:** if a module document contradicts a client source document, that is a flag, not a fallback. It means either the source was interpreted deliberately — in which case the reasoning belongs in the module document — or the module drifted and needs correcting. Do not silently prefer one; record the resolution.

Material outside this repository — chat threads, email, verbal agreements, meeting recordings — has no standing until it is written into a document here.

---

## AI Guidelines

This repository is intended to be consumed by AI assistants through indexing, retrieval, and MCP integration. The following applies to both how documents are written and how tools should treat them.

**For retrieval and indexing:**

1. Index both `modules/` and `source-of-truth/`, but answer from `modules/`. Source documents are provenance, cited only when the question is specifically about what the client asked for.
2. Filter on `status`. Never answer from `superseded` or `deprecated` content without labelling it as historical.
3. Chunk on heading boundaries. Attach `project`, `module`, `type`, and file path to every chunk so citations resolve to a location, not just a document.
4. Prefer smaller, well-scoped files over large ones. This is the reason for the 50 KB guidance in Markdown Standards.

**For assistants generating or editing documentation:**

1. Write new documents into `modules/`. Never write into `source-of-truth/`.
2. Populate complete frontmatter, including `derived_from`, on every new module document.
3. When a request cannot be answered from repository content, say so rather than inferring. An invented business rule that reads plausibly is worse than a gap.
4. Cite the file path for every substantive claim drawn from the repository.
5. When restructuring, preserve every rule from the original. Restructuring changes organization, never content — content changes are a separate, deliberate commit.

**For assistants writing code from this repository:**

Implement against `modules/`. If a needed detail is missing there, check `source-of-truth/` and, if the detail exists, raise it as a documentation gap before writing the code.
