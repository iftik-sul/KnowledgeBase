---
project: RERAN
module: regulatory-authority
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-09-18
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a10-executive-signoff-revocation.md"
  - "RERAN/modules/regulatory-authority/ui/screen-archetypes.md"
tags: [regulatory-authority, ui-spec, back-office, governance, decision]
---

# Screen: Sign-off Detail

**Archetype:** 2 — Detail / Decision.
**Access (RBAC-gated):** Director-General / Registrar. MFA required, plus **step-up re-authentication before authorising** (`M-GOV-01`). Navigation is governed by [role-screen-matrix.md](../role-screen-matrix.md).

The executive decision screen (A-10): the DG reviews an escalated matter and its underlying
recommendation, then authorises or declines. Reached by drilling into a row from the
[Sign-off Queue](signoff-queue.md) — so it carries a breadcrumb. On authorise/decline the outcome is
recorded and the matter returns to the originating service to execute.

## Purpose

Present the escalation, the lower tier's recommendation, and the underlying record on one screen, and
capture an accountable executive decision (authorise/decline) with recorded reasons.

## Layout

* **Visible Sidebar:** Back-Office Sidebar (role-scoped)
* **Top Bar Title:** {Reference} — Executive Sign-off
* **Breadcrumb:** Sign-off Queue › {Reference}

```
Top Bar → Breadcrumb → Item Header → Escalation Summary → Underlying Record →
Recommendation → Decision Panel (sticky) → Activity / Audit Trail
```

## Sections

### Section 1 — Item Header

Reference · Matter · Source (A-2 / A-8) · current status (status-badges §3) · age.

### Section 2 — Escalation Summary (read-only)

What is being escalated and by whom — the escalating officer/role, the escalation reason, the date.

### Section 3 — Underlying Record (read-only)

The originating case/record the escalation rests on (e.g. the A-2 licensing decision and practitioner
record for a revocation). Links back to the source item where applicable.

### Section 4 — Recommendation (read-only)

The lower tier's explicit recommendation to the DG (e.g. "Revoke licence LIC-2024-0231").

### Section 5 — Decision Panel (sticky footer) — the core control

Two mutually-exclusive outcomes:

- **Authorise** — signs the instrument / revocation and returns it to the originating service to
  execute (`M-GOV-01`). **Requires step-up re-authentication** before it can be committed.
- **Decline** — returns the matter to the originating tier with reasons (`M-GOV-02`).

A **reason** field is required for Decline and recommended for Authorise; both outcomes write decision
+ actor + reason to the audit trail.

### Section 6 — Activity / Audit Trail (collapsible)

Reverse-chronological record of the escalation and this decision.

## Role Variations / Permissions

- Only the Director-General / Registrar can authorise or decline. No other role reaches this screen.
- **Step-up re-authentication** is mandatory at the point of Authorise (a distinct control from
  session MFA) — surface it as an explicit re-auth step in the Authorise flow.

## Notes

- Revocations and final enforcement cannot execute without authorisation here (A-10 acceptance
  criteria). A Decline must carry recorded reasons.
- Statuses use the config/governance vocabulary (status-badges §3).
