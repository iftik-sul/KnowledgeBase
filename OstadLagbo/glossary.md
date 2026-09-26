---
project: OstadLagbo
type: glossary
status: current
updated: 2026-09-24
id: OL-GLS-001
owner: Iftikher
---

# Glossary

Canonical definitions for terms used throughout the OstadLagbo knowledge base. If a document's usage conflicts with this page, this page wins; raise the conflict as a documentation fix.

## People and roles

| Term | Definition |
|---|---|
| **Ostad** (ওস্তাদ) | A teacher/expert account holder; the supply side. Verified, discoverable, and reviewed. |
| **Shagred** (শাগরেদ) | A learner account holder; the demand side. Never publicly discoverable. |
| **Guest** | A visitor with no account. Can browse the map, search, and view public Ostad profiles; cannot contact, favorite, or report. |
| **Admin** | A manually provisioned dashboard operator. Currently the founder; single full-permission tier in MVP. |
| **Guardian** | An adult Shagred account holder acting on behalf of a minor learner. The account, chat, and arrangement legally belong to the adult (18+ gate, REG-03). |
| **AI development agent** | The builder of the platform; held to this knowledge base as its specification (stakeholder S-10, risk R-11). |

## Core objects

| Term | Definition |
|---|---|
| **Offer** | A free-text message a Shagred sends an Ostad proposing contact. States: pending → accepted / declined / expired (7 days) / withdrawn. |
| **Connection** | An *accepted* offer. The platform's success unit — the anchor for chat, rating eligibility, phone/email reveal, and Ostad history. Persists anonymized; never vanishes. |
| **Verified badge** | Shown on an Ostad's public profile once identity verification has passed and the profile is admin-approved. Not an endorsement of skill or character (ToS §2). |
| **Profile completion %** | A computed score reflecting how much of the optional profile content an Ostad has filled in. |
| **Pause** (visibility pause) | An Ostad-controlled toggle that removes them from discovery and blocks new offers while preserving existing chats and pending offers already received (OSP-11). |
| **Key field** | Legal names, identity documents, skills, or profile photo (CL-021) — after approval, a change to any of them publishes only when an admin approves the revision carrying it, while the last approved version stays public (OSP-10). |
| **Profile revision** | The single pending record of an approved Ostad's key-field changes (OSP-DM): edited, then submitted for review, locked while under review, and published, returned, or discarded by the verdict. Unsubmitted revisions are discarded after 90 days of inactivity. Initial approval uses the profile's own status, not a revision. |
| **Skill category** | A fixed, admin-managed, bilingual group (e.g., Guitar / গিটার) that Ostads select and Shagreds filter by; the specific skill is free text within it. Seeded from OL-SKC-001. |
| **Seed data** | Reference data loaded before any user exists — skill categories and the administrative-area dataset — founder-approved under change control. |

## Trust and safety

| Term | Definition |
|---|---|
| **Report** | A user-filed flag against a profile, message, review, or reply, routed to the admin reports queue with a category and detail. |
| **Block** | A user action that freezes chat, severs profile visibility, and prevents new offers between two accounts in both directions. Defined once (RNT-DM) and checked everywhere, never copied. Hidden from the blocked party within their own account's view; public content remains public to anyone logged out. |
| **Suspension** | An admin action freezing an account (login succeeds only into a restricted session showing a notice screen; Ostad pins removed; chats frozen). Reversible. |
| **Termination** | An admin action banning an account (CL-019): it stays suspended for a 30-day appeal window — during which appeal is its only write path — then purges under the banned-account retention exception so the person cannot re-register. Reversed only by a successful appeal (reinstatement). |
| **Appeal** | A support ticket of category `appeal`, the single action a suspended or terminated account may take (SUP-04), with its three supporting operations (attachment upload, push-token registration, language/logout). |
| **Restricted session** | The session a suspended account receives at login — valid only for the appeal and its supporting operations; refused by every direct Supabase channel. |
| **Legal hold** | A flag suspending scheduled data purging on a specific account or record while an investigation, report, or legal matter is active. |
| **Anonymization** | When a Shagred's account purges, their ratings and connections persist with identity replaced by "Former Shagred" (via `anonymized` flags on those records and captured display-name snapshots); the profile itself purges. |
| **Tombstone** | The minimal row a purged account leaves behind (id, role, purge date, and — if banned — the banned-exception data), so records that reference the account stay valid. |

## Architecture terms

| Term | Definition |
|---|---|
| **Policy layer** | The single centralized module, in the Render API, that enforces every relationship- and state-based access rule (who may see a Shagred profile, read a chat, receive an offer). Row-level security in the database mirrors it as a second line of defense (ADR-001). |
| **Predicate** | An access or state rule evaluated at query time against live data (discoverability, visibility, thread writability, revision review state), never stored as a flag that can go stale (Data Model Overview convention). |
| **Opacity rule** | An API refusal caused only by a block returns `not_found`, indistinguishable from nonexistence, so a block is never revealed to the blocked party (OL-API-001). |
| **ADR** | Architecture Decision Record (`decisions/`): an immutable record of a technical decision, its alternatives, and its consequences; changed only by a superseding ADR. ADR-001 fixes the platform stack; ADR-002 the analytics store; ADR-003 the implementation stack and the spec/code repository split; ADR-004 the authentication authority and token model. |
| **Three-tier** | ADR-001's architecture: Supabase for data services, Render for the API and policy layer, Vercel for the admin dashboard and public website. |
| **Upload ticket** | A short-lived signed URL the API issues for one file of one declared purpose; media never passes through the API body (OL-API-001). |

## Governance and process terms

| Term | Definition |
|---|---|
| **Baseline** | A founder-approved, change-controlled specification in `reference/baseline/` — the MVP scope (`OL-BAS`) and seed data (`OL-SKC`). Revised only by issuing a new version file; never edited in place. |
| **Change log** | The append-only record of every approved scope change (`CL-NNN`), each pending absorption into the next baseline version. |
| **Requirements** | Per-module documents (`REQ`) stating what the system must do, with numbered items and acceptance criteria, derived from the baseline. |
| **Data model** | Per-module documents (`DM`) defining entities, fields, and relationships, derived from requirements. Logical, not backend-specific. |
| **API document** | Per-module documents (`API`) defining the endpoint contracts between the apps and the Render API, derived from requirements and citing the data models. |
| **Slice** | A build-sequence unit (`OL-BLD-001`) — a set of requirements that, once built, leaves the product usable at a defined gate. |
| **MVP-core** | The product at the end of Slice 3: registration through offers, connections, and chat. The first "real product" milestone. |
| **MVP-complete** | The product at the end of Slice 5: everything in approved scope, including analytics, support, and insights. The public-launch milestone. |
| **Scope freeze** | The rule, effective once baseline v1.2 is cut, that new ideas during build are logged for a future version rather than implemented mid-build. |
| **Adversarial review** | The practice, applied to every data model and api document, of critiquing a draft against its requirements and sibling documents before approval. |

## Module abbreviations

`REG` registration-and-verification · `OSP` ostad-profile · `SGP` shagred-profile · `MAP` map-discovery · `OFR` contact-and-offers · `ADM` admin-review · `RNT` ratings-and-trust · `SUP` support

## Document ID prefixes

`OL-CHR` charter · `OL-STK` stakeholder register · `OL-RSK` risk register · `OL-CHG` change log · `OL-RET` retention policy · `OL-PRV` privacy policy · `OL-TOS` terms of service · `OL-INC` incident response · `OL-BLD` build sequence · `OL-NFR` non-functional requirements · `OL-DM` data model overview · `OL-API` api overview · `OL-UI` UI layer (overview, design foundations, public website) · `OL-GLS` glossary · `OL-BAS` MVP scope baseline · `OL-SKC` skill-category seed data · `OL-DEC` architecture decision record · `OL-<MODULE>-REQ` module requirements · `OL-<MODULE>-DM` module data model · `OL-<MODULE>-API` module api · `OL-<MODULE>-UI` module ui

## External context

| Term | Definition |
|---|---|
| **PDPA 2026** | Bangladesh's Personal Data Protection Act, in force April 2026 — governs consent, retention disclosure, erasure rights, cross-border transfer, and breach notification for this platform. |
| **NID** | National ID card — the primary accepted identity document for Ostad verification, alongside passport and driving licence (CL-017). |
