---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-15
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - real-estate-developer
  - ui-spec
---

# Screen: Application Details

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described four designs: an overview (Developer Principal / Director) and three operational workspaces (Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison) scoped to different application types, each with its own Validation Summary check set. All four are **retired**; this is one screen absorbing the load-bearing content of each.

## Purpose

The detail view of a single regulatory application, opened from [Applications](applications.md). Covers the application record, its related project, property or escrow account, its documents, its approval workflow and regulatory correspondence — with the controls to edit, validate, respond, correct and resubmit. Any user may do any of it, for any application type.

## Layout

```
Top Bar
↓
Application Header
↓
Application Summary Cards
↓
Approval Progress
↓
Application Information
↓
Related Records (Project · Property · Buyer · Escrow — by application type)
↓
Supporting Documents
↓
Validation Summary
↓
RERA Queries & Review History
↓
Activity Timeline
```

## Sections

### Section 1 — Application Header

Application ID, application type, current status badge, submission date, assigned RERA unit.

**Actions:** **Edit** · **Validate** · **Submit** · **Respond to Query** · **Resubmit** · **Download Approval**

Governed by application status. **Reconciled 2026-08-15:** the overview variant's header carried view actions only — an access restriction, now retired.

### Section 2 — Application Summary Cards

Absorbed from the overview variant, the only one to define them: days in review, documents submitted versus required, open queries, and elapsed time against the service SLA.

### Section 3 — Approval Progress

Stage tracker for the application's regulatory journey.

**Reconciled 2026-08-15:** the overview variant called this *Approval Workflow* and rendered it as a read-only record of stages passed; the three operational variants called it *Approval Progress* and rendered it as a live tracker. Same content, one of them static because that variant could not act. Kept as the live tracker.

### Section 4 — Application Information

The application's own fields — reference, service, submission channel, fee status and payment reference where the service charges one, SLA and expected decision date.

**Payment reference note:** where the application's service carries a RERA fee, that fee is paid per transaction through the shared platform payment gateway. Payment timing differs by service — some before RERA's decision, some after, and one service in two stages. See the relevant [service flow](../../service-flows/) for the specific service rather than assuming a uniform order.

### Section 5 — Related Records

**Absorbed 2026-08-15** by unioning what the four variants each showed for their own domain:

* **Related Project & Property** — from the overview and Registration Officer variants.
* **Property & Buyer Information** — from the Sales & Disclosure Officer variant, including buyer classification and additional purchasers.
* **Related Escrow Account** — from the Escrow Liaison variant, including the account, milestone and release the application concerns. *(Project escrow account — not RERA fees.)*
* **Applicant Information** — from the overview variant: who filed, and the role they held at the time.
* **Related Records** — from the overview variant: other applications and records linked to this one.

Groups render according to **application type**, not according to who is looking. An escrow application shows the escrow group; a sales disclosure shows buyer information. This is the same conditional-rendering principle as [applications.md](applications.md)'s domain columns.

### Section 6 — Supporting Documents

Required-document checklist and table, with Upload / Replace / Preview / Resubmit actions governed by document status.

**Reconciled 2026-08-15:** the overview variant's *Submitted Documents* listed filed documents with view/download only; the three operational variants' *Supporting Documents* added the checklist and upload controls. The operational version is the superset and is kept.

### Section 7 — Validation Summary

Automatic pre-submission checks, displayed as Passed / Warning / Error, with the submit action disabled until all mandatory checks pass.

**This section now applies to every user.** It existed in the three operational variants only; the overview variant had none, because it could not submit. That was an access restriction, not a property of the screen.

**Reconciliation — the three operational variants' check lists differed and are now merged by application type.** [validation-rules.md](../validation-rules.md) recorded that all three shared the same mechanism and the same first checks, but diverged in their specific items. Those checks are the actual business rule, so none was dropped: the shared checks apply to every application, and the domain-specific checks apply to the application types that need them. See [validation-rules.md](../validation-rules.md) for the consolidated set.

### Section 8 — RERA Queries & Review History

**Absorbed 2026-08-15** by combining two sections the variants held apart:

* **RERA Queries** *(three operational variants)* — open queries with Respond and Upload actions.
* **RERA Review History** *(overview variant)* — the closed record of review rounds, reviewers, decisions and remarks.

The same correspondence at two points in its life, split only because one variant could act on it and the others could only read it. Open queries first, resolved history below.

### Section 9 — Activity Timeline

Chronological record of everything that has happened to this application, including every status change, document action and payment event. Each entry shows who acted and what role they held at the time ([navigation.md](../../navigation.md#audit-trail-principle)).

**Reconciled 2026-08-15:** the three operational variants had both a *Communication History* and an *Activity Timeline*; the overview variant had only the timeline. Communication entries are a subset of activity, so they are merged into one timeline with a correspondence filter rather than kept as two lists that partly restate each other.

## Empty State

> This application has no submitted documents yet. Upload the required documents to move it forward.

**Primary Button** — Upload Documents

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

## Validation

1. No section, field, action or card on this screen is role-gated. What a user can do depends on the application's status, never on who they are.
2. Fields become read-only after submission unless RERA returns the application — a lifecycle rule applying to every user equally.
3. Once approved, the application becomes read-only. Also a lifecycle rule.
4. Validation Summary checks are defined in [validation-rules.md](../validation-rules.md) and are not restated here.
5. Related Records groups render by application type, never by role.

## User Flow

```
Applications
↓
Application Details
├─ Edit / Validate / Submit → the service flow
├─ Respond to Query → response flow
├─ Document row → Document Details
└─ Related Record link → Project / Property / Escrow Details
```

## Notes

* **This absorbs, rather than references, all four retired variants.**

* **The three operational variants were one design scoped three ways**, exactly as on [applications.md](applications.md) — same section order, same Validation Summary mechanism, same query and communication sections, differing in their Related Records group and their specific validation checks. Both of those differences are now driven by application type rather than by role.

* **The Validation Summary was the substantive merge decision, twice over.** First, it applies to everyone now, since every user can submit. Second, the three variants' check lists genuinely differed, and [validation-rules.md](../validation-rules.md) had explicitly warned against normalizing them because "the checks are the actual business rule." They are therefore merged **by application type**, not flattened — every check survives, attached to the applications it governs.

* **What was dropped, and why.** Only the view-only header actions, the static rendering of Approval Progress, the per-domain scoping, and the duplicate Communication History list. Nothing representing distinct work was discarded — the overview variant's Application Summary Cards, Applicant Information, Related Records and RERA Review History all survive, as do each operational variant's domain groups, validation checks and query controls.
