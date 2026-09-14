---
project: RERAN
module: regulatory-authority
type: figma-prompt
screen: application-review
status: draft
updated: 2026-09-14
derived_from:
  - "RERAN/modules/regulatory-authority/ui/screens/application-review.md"
  - "RERAN/modules/regulatory-authority/ui/validation-rules.md"
  - "RERAN/modules/regulatory-authority/ui/status-badges.md"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
reference_frame: "RERAN-Web-App / Financial & Trust Institution / screen #5: Application Review (1179:35755) — reuse card shell + ValidationSummaryCard; replace submit-footer with Decision Panel"
tags: [regulatory-authority, figma-prompt, back-office, decision]
---

# Figma build prompt — Application Review (Group A, Archetype 2: Detail / Decision)

The highest-leverage screen in the platform (A-1 routes 92 services through it). Reuse the
card-based shell of the existing **Application Review** (node 1179:35755) — TopBar, breadcrumb,
header chips, and the `Card -> CardHeader -> DetailsGrid -> GridRow` field pattern — but this is a
**reviewer decision** screen: fields are read-only, and the applicant's Declaration/submit footer
is replaced by a **Decision Panel**.

## Frame
- Name: `Application Review` · **1440x927** (body taller, scrolls) · reached from Work Queue (MFA).

## Components to use (real, existing)
- **RA-Sidebar** — role-scoped (per role-screen-matrix.md section 1); C&E Auditor persona:
  Dashboard · **Work Queue (active)** · Audit Trail. (This screen is reached from the queue, not a
  top-level nav item — "Work Queue" stays active.)
- **Button Primary** (Approve) + variants for the other three outcomes (secondary / danger).
- **Badge** (status), **Checkbox** (mark-seen / flag on documents), **Avatar**.
- Icons: `arrow-left` (back), `Chevron Right` (breadcrumb), `Action Eye Visible` (view doc),
  `Check` + `Warning Circle` (registry check pass/attention), `File`/`Folder` (documents).
- Cards, tables, and the Decision Panel = composed frames named as below.

## Layout (reuse 1179:35755 shell; new right rail + footer)
```
Application Review 1440x927
├─ RA-Sidebar (240)
└─ MainContent (1200)
   ├─ TopBar (78): Title "{Reference} — {Originating service}"
   │               meta: status Badge · SLA state · applicant
   │               HeaderRight: BackButton "Back to Work Queue" · NotificationBell · Avatar
   └─ Workspace
      ├─ Breadcrumb:  Work Queue > Application Review
      ├─ ItemHeader (HeaderRow of HeaderField chips):
      │     Applicant · Subject · Originating service · Expected output · SLA
      ├─ Two-column body
      │   ├─ LEFT (main)
      │   │   ├─ Application Panel  — "Application Summary" AppInfoCard + cards
      │   │   │     (CardHeader + DetailsGrid + GridRow; Subsections: Applicant Info,
      │   │   │      Property/Project Info, service-specific fields). READ-ONLY, no Edit links.
      │   │   └─ Documents Panel   — SupportingDocumentsCard -> Table (TableHeader + TableRow 41):
      │   │         name · type · uploaded · status; row actions: view inline (Action Eye Visible),
      │   │         mark seen / flag (Checkbox).
      │   └─ RIGHT (rail)
      │       ├─ Registry Checks Panel — adapt ValidationSummaryCard: rows of live checks, each with
      │       │     a pass/attention indicator (Check / Warning Circle + Badge) and a StatusIndicator
      │       │     summary ("All Clear" / "N items need attention").
      │       │     Checks (A-1 section 7): developer · project · unit · title · applicant validity & consistency.
      │       │     Licensing items: replace with a single Practitioner-Register check.
      │       └─ Escrow panels (ESCROW ITEMS ONLY):
      │             "Trustee Assessment" card (FTI trustee's uploaded assessment) +
      │             "Escrow Account" card (account state; mortgage-linked -> live FTI mortgage
      │              status must read `Completed`).
      ├─ Decision Panel (STICKY FOOTER) — the core control
      │     Four mutually-exclusive outcomes:
      │        Approve (Button Primary) · Request Additional Information · Return · Reject
      │     Reason field: optional for Approve; REQUIRED for the other three (show required marker
      │     + block submit until filled). On Approve -> triggers the originating service's output.
      │     Every outcome writes decision + actor + reason to the audit trail.
      └─ Activity / Audit Trail (collapsible): reverse-chronological — actor, role, action, time, reason.
```

## Status badge values (status-badges.md section 1 — do not localise)
`Under Review` · `Information Requested` · `Returned` · `Approved` · `Rejected`.
Proposed colour intent (bind to library tokens in Figma): Under Review = neutral/info ·
Information Requested = attention/amber · Returned = warning/amber · Approved = success/green ·
Rejected = danger/red.

## Role variations (section Role Variations)
- **Compliance & Escrow Auditor** — escrow panels render only for escrow items, only for this role.
- **Licensing & Registration Officer** — Practitioner-Register check in place of property registry
  checks; no escrow panels.
- Decision Panel is **enabled only for the item's primary decision role**; view-only roles see it disabled.

## Guards (validation-rules.md / A-1)
- Reason mandatory on Request Info / Return / Reject.
- Escrow items cannot be decided until the trustee assessment is present.
- A mortgage-registration approval flips the mortgage to `Completed` for RED #6's live check.
- Status vocabulary from status-badges.md section 1 — do not localise.

## Genuinely new vs the reference frame (flag for the builder)
1. **RA-Sidebar** — new sibling component (see work-queue.md prompt).
2. **Registry Checks Panel** — adapted from ValidationSummaryCard (checks instead of validations).
3. **Decision Panel** — new reviewer control replacing the applicant's Declaration + submit footer.
