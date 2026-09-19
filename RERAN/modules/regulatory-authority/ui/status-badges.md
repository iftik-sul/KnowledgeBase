---
project: RERAN
module: regulatory-authority
type: ui-status-badges
status: draft
contains_proposals: true
updated: 2026-09-18
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/"
tags:
  - regulatory-authority
  - ui-spec
  - status-badges
---

# Regulatory Authority — Status Badges

The status vocabularies the back-office screens display. The Regulatory Authority drives
the **decision half** of every originating service's status flow, so its badges must
match the shared platform vocabulary — the originating modules' status displays read the
same words (see A-1 §13). This file is the single source for badge wording and grouping;
screens reference it rather than defining status inline.

**Badge Color** columns below name the `Badge` component's Color prop (from the Component
library) each status maps to — confirmed against the real component during the Figma build.
The `Badge` palette is: Gray · Blue · Sky · Indigo · Purple · Pink · Rose · Orange · Brand ·
Success · Warning · Error · Slate.

## 1. Shared decision statuses (A-1, A-2 — the 92 + 9 services)

Used by the Work Queue and Application Review screens. **Do not localise these words.**

| Badge | Meaning | Group | Badge Color |
| :-- | :-- | :-- | :-- |
| Under Review | Item is in the queue / being reviewed | active | Blue |
| Information Requested | Queried back to the applicant; re-enters on response | active | Warning |
| Returned | Sent back for correction | active | Warning |
| Approved | Decided; output issued | terminal (positive) | Success |
| Rejected | Decided; terminal | terminal (negative) | Error |

## 2. Case lifecycle statuses (A-3 — dispute)

Used by the Case Queue and Case Workspace. A case lifecycle, distinct from §1.

| Badge | Meaning | Badge Color |
| :-- | :-- | :-- |
| Filed | Received, not yet assigned | Gray |
| Assigned | With a Dispute Adjudication Officer | Blue |
| Scheduled | Mediation/hearing scheduled | Sky |
| In Session | A session is under way | Orange |
| Information Requested | Evidence/info requested between sessions | Warning |
| Under Deliberation | Awaiting judgment | Purple |
| Judgment Recorded | Judgment entered | Success |
| Closed | Resolved / partially resolved / referred | Success |
| Dismissed | Terminal — closed without substantive judgment | Error |
| Withdrawn | Terminal — filing party withdrew | Gray |

## 3. Config / platform statuses

| Screen | Badge (Color) |
| :-- | :-- |
| Fee Schedule Editor (A-4) | Draft (Gray) · Published (Success) · Archived (Slate) |
| Reconciliation (A-5) | Open (Blue) · Balanced (Success) · Discrepant (Error); remittances Pending (Warning) · Remitted (Success) |
| Admin Console (A-6) | Invited (Blue) · Active (Success) · Suspended (Warning) · Deactivated (Error) |

## 4. Field & governance statuses (A-7 to A-10)

| Service | Badge (Color) | Screens |
| :-- | :-- | :-- |
| Inspection (A-7) | Requested (Blue) · Scheduled (Sky) · Completed (Success) · Cancelled (Gray) | **Specced** — inspection-queue, inspection-capture, inspection-report |
| Sign-off (A-10) | Pending Sign-off (Warning) · Authorised (Success) · Declined (Error) | **Specced** — signoff-queue, signoff-detail |
| Enforcement (A-8) | Draft (Gray) · Issued (Blue) · Escalated (Warning) · Resolved (Success) | Deferred |
| Harmonisation (A-9) | Open (Blue) · Reconciled (Success) · Conflicted (Error) | Deferred |

## 5. Document review statuses

Used by the Document Review detail screen (a document row's status within Application Review).

| Badge | Meaning | Badge Color |
| :-- | :-- | :-- |
| Pending | Not yet reviewed — the default a document starts at | Warning |
| Verified | Reviewed and accepted | Success |
| Rejected | Reviewed and rejected (reason required) | Error |

## Notes

- **Colour mappings are confirmed against the real `Badge` component** during the Figma build.
  Where a build surfaces a new status not listed here, add it with its Color and note the screen.
- The deferred vocabularies (Enforcement A-8, Harmonisation A-9) carry proposed colours so their
  screens need no rework if/when activated; no screens currently use them.
- The escrow queue's **Escrow Flag** (trustee-assessment gate, not a decision status) uses:
  Received (Success) · Awaiting Trustee (Warning). It is a per-item flag, separate from the §1
  decision status shown alongside it.
