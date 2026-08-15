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

# Screen: Help & Support

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described four designs whose section sets genuinely disagreed: three variants (Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer) had **System Status** and **Feedback & Suggestions** sections and structured regulatory contact as RERA Support Center / Live Chat / Emergency Regulatory Support; the Escrow Liaison variant had neither, and instead had **Training Resources** and **Quick Help Categories** sections the other three lacked. All four are **retired**; this is one screen carrying every section any variant defined.

## Purpose

Give any developer user the knowledge base, support tickets, contact routes, system status and training resources needed to use the module and reach RERA.

## Layout

```
Top Bar
↓
Support Summary Cards
↓
Quick Actions
↓
Search Knowledge Base
↓
Quick Help Categories
↓
Knowledge Base Articles
↓
Support Tickets
↓
System Status
↓
Contact RERA Support
↓
Training Resources
↓
Feedback & Suggestions
```

## Sections

### Section 1 — Support Summary Cards

Open tickets, resolved tickets, average response time, and unread announcements — organization-wide.

### Section 2 — Quick Actions

* Create Support Ticket
* Search Knowledge Base
* Contact RERA Support
* View Training Resources

Absorbed across all four variants; every action is available to every user.

### Section 3 — Search Knowledge Base

Full-text search across help articles.

**Absorbed 2026-08-15** from the Escrow Liaison variant, which was the only one to give search its own section — the other three folded search into their Help Center / Knowledge Base section. Kept as a distinct section, since search is the primary entry point.

### Section 4 — Quick Help Categories

Task-oriented shortcuts into the knowledge base: registering a project, registering a property, recording a sale, filing a disclosure, activating an escrow account, requesting a fund release, uploading documents, responding to a RERA query, making a payment.

**Absorbed 2026-08-15** from the Escrow Liaison variant, the only one to define it, and **extended from escrow-only to every function** — the section's shape is useful across all of them.

### Section 5 — Knowledge Base Articles

Article catalogue, grouped by topic and covering every module function.

**Reconciled 2026-08-15:** the Principal / Director variant called this section **Help Center**; the other three called it **Knowledge Base**. Same content and structure. Kept as **Knowledge Base**, the three-quarters majority and the name used in the Quick Actions of all four.

**Absorbed:** the union of all four variants' article topics — the three operational variants each covered their own domain, and the executive variant covered organization-level topics.

### Section 6 — Support Tickets

Ticket list with reference, subject, category, priority, status, created and last-updated dates, plus Create, View, Reply and Close actions. Present in all four variants with the same structure.

**Organization-wide, not per user.** Previously each variant implied a ticket list scoped to its own role's work.

### Section 7 — System Status

Platform and service availability, plus scheduled maintenance notices.

**Absorbed 2026-08-15** from the three variants that had it. **The Escrow Liaison variant's omission reads as a gap, not a restriction** — service availability is not role-specific information, and there is no reason an escrow user would not need it.

### Section 8 — Contact RERA Support

* **RERA Support Center** — primary contact route, hours and reference numbers.
* **Live Chat** — during support hours.
* **Emergency Regulatory Support** — escalation route for time-critical regulatory matters.
* General contact options — phone, email, office addresses.

**Reconciled 2026-08-15:** three variants structured this as the three named routes above; the Escrow Liaison variant instead listed a flat set of contact options with no equivalent breakdown. Both are kept — the structured routes plus the flat option list, which contained contact details the structured version did not enumerate.

**Naming:** the Principal / Director variant titled this section *Contact Support* and the other three *Contact RERA Support*. Kept as **Contact RERA Support**, the more specific name.

### Section 9 — Training Resources

Guides, walkthroughs, recorded sessions and onboarding material.

**Absorbed 2026-08-15** from the Escrow Liaison variant, the only one to define it. Retained and generalized beyond escrow — training material applies to every function, and the other variants' omission looks like a gap rather than a decision.

### Section 10 — Feedback & Suggestions

Submit product feedback and feature suggestions, with a record of previous submissions.

**Absorbed 2026-08-15** from the three variants that had it. As with System Status, the Escrow Liaison variant's omission reads as a gap.

## Empty State

> No support tickets yet. Search the knowledge base, or create a ticket if you need help from RERA.

**Primary Button** — Create Support Ticket

Applies to Section 6 only; every other section always renders.

## Reused Components

See [components.md](../components.md).

## Validation

1. No section, article, category, contact route or action on this screen is role-gated.
2. Support tickets and feedback submissions are organization-wide, with author attribution from the audit trail.
3. System Status reflects platform availability and is identical for every user.

## User Flow

```
Any screen
↓
Help & Support
├─ Search / Quick Help Category → Knowledge Base Article
├─ Create Support Ticket → ticket flow
├─ Contact RERA Support → contact route
└─ Training Resources → guide or recording
```

## Notes

* **This absorbs, rather than references, all four retired variants.**

* **This screen had the clearest asymmetry in the module.** Three variants shared a section set; the fourth had two sections they lacked (Training Resources, Quick Help Categories) and lacked two they had (System Status, Feedback & Suggestions). Every one of those four sections is kept. Three of the four omissions read as gaps in the source rather than deliberate restrictions — there is no coherent reason an escrow user would not need system status, or a registration user not need training material.

* **Reconciliation — "Help Center" vs "Knowledge Base."** Same section, two names; resolved to Knowledge Base.

* **Reconciliation — "Contact Support" vs "Contact RERA Support."** Resolved to the more specific name, with both the structured contact routes and the flat option list retained.

* **Quick Help Categories and Training Resources were generalized, not just copied.** Both were written escrow-only. Restricting them to escrow on a shared screen would have made them look like leftovers; extending them to every function is the minimal change that keeps them coherent. **Proposed** — the non-escrow entries are extrapolated from the module's other functions, not sourced.

* **What was dropped, and why.** Only the per-role scoping of tickets and article topics, and the duplicate section naming. No section, article topic or contact route was discarded.
