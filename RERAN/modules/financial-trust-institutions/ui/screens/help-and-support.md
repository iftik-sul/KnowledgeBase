---
project: RERAN
module: financial-trust-institutions
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/help-and-support.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
tags:
  - financial-trust-institutions
  - ui-spec
  - help-support
---

# Screen: Help & Support

**Access:** Any of the institution's four Group C roles — unified access, not scope-gated, consistent with every other screen in this module.

> **Built 2026-08-16, by client decision.** No source material describes this screen; `navigation.md`'s sidebar names it, and nothing else in the module does. Built at Claude's full discretion, by explicit client instruction, structured on real-estate-developer's Help & Support screen — the one place in the project with a genuinely complete design for this kind of screen — adapted for an institutional, B2B financial-services audience rather than individual developers. Every section below is a proposed build, not a sourced or corrected one; flagged throughout rather than presented as settled.

## Purpose

Give any institution user the knowledge base, support tickets, contact routes to RERA, and system status needed to operate the module — scoped to what a financial institution's compliance and operations staff actually need, not a general consumer support experience.

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
```

**Deliberately narrower than real-estate-developer's version** — no Training Resources or Feedback & Suggestions sections. See Notes for why.

## Sections

### Section 1 — Support Summary Cards

Open tickets, resolved tickets, average response time, unread announcements — institution-wide.

### Section 2 — Quick Actions

* Create Support Ticket
* Search Knowledge Base
* Contact RERA Support

Available to every user; none conditional on role.

### Section 3 — Search Knowledge Base

Full-text search across help articles, as its own section rather than folded into Knowledge Base Articles — matching real-estate-developer's Escrow Liaison variant, the only one to give search this prominence.

### Section 4 — Quick Help Categories

Task-oriented shortcuts into the knowledge base, scoped to this module's actual functions rather than developer-facing tasks:

* Registering a mortgage
* Certifying an escrow request
* Filing a compliance report
* Renewing institutional approval
* Managing staff records
* Responding to an information request
* Resubmitting a returned application

**Proposed** — not sourced; built by analogy with real-estate-developer's Quick Help Categories, replacing every developer-facing task with the equivalent institution-facing one.

### Section 5 — Knowledge Base Articles

Article catalogue, grouped by this module's own functions: mortgage and finance-lease registration, internal certification, escrow assessment, trust account maintenance, compliance reporting, institutional approval and renewal, staff management.

### Section 6 — Support Tickets

Ticket list — reference, subject, category, priority, status, created and last-updated dates — with Create, View, Reply and Close actions. **Institution-wide, not per-user**, matching the unified-access pattern used everywhere else in this module.

### Section 7 — System Status

Platform and service availability, plus scheduled maintenance notices — identical for every user.

### Section 8 — Contact RERA Support

* **RERA Support Center** — primary contact route, hours and reference numbers.
* **Live Chat** — during support hours.
* **Emergency Regulatory Support** — escalation route for time-critical regulatory matters (e.g. an escrow irregularity requiring urgent RERA attention).
* General contact options — phone, email, office addresses.

Structured identically to real-estate-developer's version — the regulator is the same across both modules, so the contact routes plausibly are too. **Proposed**, not independently sourced for this module.

## Empty State

**Message**

> No support tickets yet. Search the knowledge base, or create a ticket if you need help from RERA.

**Primary Button** — Create Support Ticket

Applies to Section 6 only; every other section always renders.

## Reused Components

See [components.md](../components.md).

## Validation

1. No section, article, category, contact route, or action on this screen is role-gated.
2. Support tickets are institution-wide, with author attribution from the audit trail.
3. System Status reflects platform availability and is identical for every user.

## User Flow

```
Any screen
↓
Help & Support
↓
├─ Search / Quick Help Category → Knowledge Base Article
├─ Create Support Ticket → ticket flow
└─ Contact RERA Support → contact route
```

## Notes

* **Two sections from real-estate-developer's version are deliberately not carried over: Training Resources and Feedback & Suggestions.** Real-estate-developer's audience includes individual developer-company staff who may be first-time platform users; this module's users are professional financial-institution staff operating a compliance-critical system as part of their job. A full Training Resources section reads as consumer-app onboarding, not institutional software support — if onboarding material is needed, a single "Institution Onboarding Guide" link under Knowledge Base Articles covers it without a dedicated section. Feedback & Suggestions is a lower-value feature for a B2B compliance tool than for a consumer-facing app, where product feedback loops matter more; dropped rather than included at reduced weight.
* **This is a genuinely different scope decision from real-estate-developer's build**, not a copy with renamed labels — the two modules' Help & Support screens should diverge exactly where their audiences and use cases diverge, and converge where they don't (Contact RERA Support, System Status, Support Tickets), since the underlying regulator relationship is the same.
* Whether "Emergency Regulatory Support" needs institution-specific escalation paths (e.g. a direct line for reporting a discovered escrow irregularity, distinct from general emergency support) is not addressed here — flagged for future consideration, not resolved.
