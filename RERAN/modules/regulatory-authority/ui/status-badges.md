---
project: RERAN
module: regulatory-authority
type: ui-status-badges
status: draft
contains_proposals: true
updated: 2026-09-12
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/"
tags:
  - regulatory-authority
  - ui-spec
  - status-badges
---

# Group A — Status Badges

The status vocabularies the back-office screens display. Group A drives the **decision
half** of every originating service's status flow, so its badges must match the shared
platform vocabulary — the originating modules' status displays read the same words (see
A-1 §13). This file is the single source for badge wording and grouping; screens
reference it rather than defining status inline.

## 1. Shared decision statuses (A-1, A-2 — the 92 + 9 services)

Used by the Work Queue and Application Review screens. **Do not localise these words.**

| Badge | Meaning | Group |
| :-- | :-- | :-- |
| Under Review | Item is in the queue / being reviewed | active |
| Information Requested | Queried back to the applicant; re-enters on response | active |
| Returned | Sent back for correction | active |
| Approved | Decided; output issued | terminal (positive) |
| Rejected | Decided; terminal | terminal (negative) |

## 2. Case lifecycle statuses (A-3 — dispute)

Used by the Case Queue and Case Workspace. A case lifecycle, distinct from §1.

| Badge | Meaning |
| :-- | :-- |
| Filed | Received, not yet assigned |
| Assigned | With a Dispute Adjudication Officer |
| Scheduled | Mediation/hearing scheduled |
| In Session | A session is under way |
| Information Requested | Evidence/info requested between sessions |
| Under Deliberation | Awaiting judgment |
| Judgment Recorded | Judgment entered |
| Closed | Resolved / partially resolved / referred |
| Dismissed | Terminal — closed without substantive judgment |
| Withdrawn | Terminal — filing party withdrew |

## 3. Config / platform statuses

| Screen | Badges |
| :-- | :-- |
| Fee Schedule Editor (A-4) | Draft · Published · Archived |
| Reconciliation (A-5) | Open · Balanced · Discrepant; remittances Pending · Remitted |
| Admin Console (A-6) | Invited · Active · Suspended · Deactivated |

## 4. Latent statuses (A-7–A-10)

Defined in each latent service-flow; not built yet. Inspection: Requested · Scheduled ·
Completed · Cancelled. Enforcement: Draft · Issued · Escalated · Resolved. Harmonisation:
Open · Reconciled · Conflicted. Sign-off: Pending Sign-off · Authorised · Declined.

> **Proposed** — colour mapping (which badge group maps to which design-token colour) is
> deferred to the Figma thread, where badges reconcile to the real component library.
