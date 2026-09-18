---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a3-adjudicate-dispute.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, back-office, tribunal]
---

# Screen: Case Workspace

**Archetype:** 5 — Case Workspace.
**Access (RBAC-gated):** Dispute Adjudication Officer. MFA required. Navigation (which roles reach this screen) is governed by [role-screen-matrix.md](../role-screen-matrix.md); the roles named here identify who acts on this screen.

The hub for working one dispute case over multiple sessions. This is the one Group A screen
that is not an approve/reject — it is a case worked over time, with sessions, evidence, and
a final judgment. Opened from the [Case Queue](case-queue.md).

## Purpose

Give the officer everything for one case in one place — parties, evidence, the running
session timeline, and the judgment step — and support the case moving through its lifecycle
across several sittings.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** {Case ref} — {matter type}
* **Top Bar meta:** case-lifecycle status badge · parties · next session

```
Top Bar → Case Header → Parties & Evidence → Session Timeline → Judgment / Resolution
```

## Sections

### Section 1 — Case Header

Matter type, parties, filing origin (originating dispute service), current lifecycle status.

### Section 2 — Parties & Evidence

The parties named in the filing and all submitted evidence/documents; the officer can
request further evidence (moves the case to Information Requested).

### Section 3 — Session Timeline

The running record of sessions. The officer can **schedule** a mediation/hearing
(`M-DIS-01`), **conduct** a (remote) session and record its outcome (`M-DIS-02`), and
**request evidence** between sessions (`M-DIS-03`) — the loop from A-3 §12. Each session and
interim note is recorded.

### Section 4 — Judgment / Resolution

Recorded once, closes the case. The officer records a judgment (`M-DIS-04`) or closes the
case another way: dismiss (`M-DIS-05`), record withdrawal (`M-DIS-06`), or refer to another
forum (`M-DIS-07`). Outcome is one of: Resolved · Partially Resolved · Dismissed ·
Withdrawn · Referred (A-3 §14). A recorded judgment/basis is required before close
(`M-BLK-04` blocks closing without one). Modal wording and fields are owned by
[modals.md](../modals.md) §4.

## Role Variations / Permissions

- Dispute Adjudication Officer only. This role can schedule sessions, record session
  outcomes, request evidence, and record the judgment.
- Judgment/close is the officer's equivalent of the Decision Panel — enabled only for this
  role.

## Notes

- Status uses the case lifecycle (status-badges §2). The complaint matter (IU #38) includes
  an investigation phase, handled inside the Session Timeline loop (A-3 §15).
- The case lifecycle must map to each originating service's own applicant-facing status
  (A-3 §13) — a `Proposed` dependency.
