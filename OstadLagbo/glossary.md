---
project: OstadLagbo
type: glossary
status: current
updated: 2026-09-12
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

## Core objects

| Term | Definition |
|---|---|
| **Offer** | A free-text message a Shagred sends an Ostad proposing contact. States: pending → accepted / declined / expired (7 days) / withdrawn. |
| **Connection** | An *accepted* offer. The platform's success unit — the anchor for chat, rating eligibility, phone/email reveal, and Ostad history. |
| **Verified badge** | Shown on an Ostad's public profile once identity verification has passed and the profile is admin-approved. Not an endorsement of skill or character (ToS §2). |
| **Profile completion %** | A computed score reflecting how much of the optional profile content an Ostad has filled in. |
| **Pause** (visibility pause) | An Ostad-controlled toggle that removes them from discovery and blocks new offers while preserving existing chats and pending offers already received (OSP-11). |
| **Key field** | Legal names, identity documents, or skills — editing one returns the profile to admin review while the last approved version stays public (OSP-10). |
| **Profile revision** | The approved/pending snapshot mechanism that makes the "public never sees unapproved edits" rule structural, not just a UI behavior. |

## Trust and safety

| Term | Definition |
|---|---|
| **Report** | A user-filed flag against a profile, message, review, or reply, routed to the admin reports queue with a category and detail. |
| **Block** | A user action that freezes chat, severs profile visibility, and prevents new offers between two accounts in both directions. |
| **Suspension** | An admin action freezing an account (login blocked beyond a notice screen; Ostad pins removed; chats frozen). Reversible. |
| **Legal hold** | A flag suspending scheduled data purging on a specific account or record while an investigation, report, or legal matter is active. |
| **Connection anonymization** | When a Shagred deletes their account, their reviews and Ostad-history entries persist with identity replaced by "Former Shagred," never removed. |

## Governance and process terms

| Term | Definition |
|---|---|
| **Baseline** | The founder-approved, change-controlled MVP scope document (`reference/baseline/`). Revised only by issuing a new version file; never edited in place. |
| **Change log** | The append-only record of every approved scope change (`CL-NNN`), each pending absorption into the next baseline version. |
| **Requirements** | Per-module documents (`REQ`) stating what the system must do, with numbered items and acceptance criteria, derived from the baseline. |
| **Data model** | Per-module documents (`DM`) defining entities, fields, and relationships, derived from requirements. Logical, not backend-specific. |
| **Slice** | A build-sequence unit (`OL-BLD-001`) — a set of requirements that, once built, leaves the product usable at a defined gate. |
| **MVP-core** | The product at the end of Slice 3: registration through offers, connections, and chat. The first "real product" milestone. |
| **MVP-complete** | The product at the end of Slice 5: everything in approved scope, including analytics, support, and insights. The public-launch milestone. |
| **Scope freeze** | The rule, effective once baseline v1.2 is cut, that new ideas during build are logged for a future version rather than implemented mid-build. |

## Module abbreviations

`REG` registration-and-verification · `OSP` ostad-profile · `SGP` shagred-profile · `MAP` map-discovery · `OFR` contact-and-offers · `ADM` admin-review · `RNT` ratings-and-trust · `SUP` support

## Document ID prefixes

`OL-CHR` charter · `OL-STK` stakeholder register · `OL-RSK` risk register · `OL-CHG` change log · `OL-RET` retention policy · `OL-PRV` privacy policy · `OL-TOS` terms of service · `OL-INC` incident response · `OL-BLD` build sequence · `OL-NFR` non-functional requirements · `OL-DM` data model · `OL-GLS` glossary · `OL-<MODULE>-REQ` module requirements · `OL-<MODULE>-DM` module data model

## External context

| Term | Definition |
|---|---|
| **PDPA 2026** | Bangladesh's Personal Data Protection Act, in force April 2026 — governs consent, retention disclosure, erasure rights, and breach notification for this platform. |
| **NID** | National ID card — the primary accepted identity document for Ostad verification, alongside passport and driving licence (CL-017). |
