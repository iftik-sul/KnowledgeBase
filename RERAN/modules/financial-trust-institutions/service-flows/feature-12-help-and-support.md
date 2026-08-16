---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: extrapolated
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/help-and-support.md"
  - "RERAN/modules/real-estate-developer/service-flows/feature-12-help-and-support.md"
  - "RERAN/modules/financial-trust-institutions/navigation.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - help-support
---

# Feature #12 – Help & Support

**Feature Category:** Shared Platform Features – General Platform

> **Built 2026-08-16, by client decision, superseding the prior `TBD` treatment.** No source material describes this feature; `navigation.md`'s sidebar names it, and no screen existed anywhere in the module (`ui/screens/` and `ui/screens-unified/` both checked directly before this build). Built at Claude's full discretion, by explicit client instruction — structured on real-estate-developer's Help & Support feature, the only complete design of this kind in the project, adapted for an institutional B2B audience rather than individual developers. Every section is a proposed build, not sourced or corrected; flagged as such throughout, matching the honesty standard the rest of this module's genuinely unsourced content already follows.

## 1. Feature Overview

**Help & Support** gives any institution user the knowledge base, support tickets, and RERA contact routes needed to operate the module — scoped to a financial institution's compliance and operations staff, not a general consumer support experience.

## 2. Purpose

Give every institution user access to help resources and RERA contact routes relevant to this module's actual functions, regardless of role.

## 3. Description

Built on the same structural template as real-estate-developer's Help & Support, with two sections deliberately dropped rather than carried over: Training Resources and Feedback & Suggestions. This module's users are professional financial-institution staff operating a compliance-critical system as part of their job, not individual first-time platform users — a full onboarding section reads as consumer-app framing, not institutional software support. Where onboarding material is genuinely needed, a single "Institution Onboarding Guide" link under Knowledge Base Articles covers it without a dedicated section. Sections that plausibly *do* transfer as-is — Contact RERA Support, System Status — are kept close to identical to real-estate-developer's version, since both modules answer to the same regulator.

## 4. Used By

Not tied to any single numbered service — reachable from any screen in the module.

## 5. Prerequisites

* User is logged into a verified institution account.

## 6. Required Information

Search terms for Knowledge Base search; ticket subject/category/priority when creating a support ticket.

## 7. Required Documents

None required; attachments optional on support tickets.

## 8. Service Fee

No fee.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the institution's four Group C roles** — no section, article, contact route, or action is role-gated.

## 11. Expected Processing Time

Knowledge base search and article access are immediate. Support ticket response time is not given a fixed sourced figure — Support Summary Cards display an "average response time" as a reported metric, not a committed SLA.

## 12. Processing Workflow

Any Screen
↓
Open Help & Support
↓
Search Knowledge Base **or** Browse Quick Help Categories **or** Create Support Ticket **or** Contact RERA Support
↓
*(on ticket)* Ticket Created → Institution-Wide Ticket List → Reply / Close

## 13. Application Status Flow

Support Ticket: Open → In Progress → Resolved / Closed. Not otherwise a submission-based feature with a broader application status flow.

## 14. Possible Outcomes

* Knowledge Base Article Found
* Support Ticket Created / Resolved
* RERA Support Contacted

## 15. Output

* Support ticket record, institution-wide, with author attribution from the audit trail

## 16. Related Features

None directly — a standalone resource, reachable from every other screen in the module rather than feeding into or from any specific one.

## 17. UI Screens

* Help & Support

## 18. API Requirements

* Retrieve Knowledge Base Articles / Search
* Retrieve Quick Help Categories
* Create / Retrieve / Reply to / Close Support Tickets
* Retrieve System Status
* Create Audit Log

## 19. Database Entities

* Institution, Institution Staff, User
* Support Ticket, Knowledge Base Article
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can access every section: Knowledge Base, Quick Help Categories, Support Tickets, System Status, Contact RERA Support.
* Support tickets are institution-wide, with author attribution from the audit trail.
* System Status reflects platform availability identically for every user.
* Training Resources and Feedback & Suggestions are deliberately absent — see Notes on why.

## 21. Business Rules

1. No section, article, contact route, or action on this feature is role-gated.
2. Support tickets are institution-wide, not per-user.
3. Quick Help Categories and Knowledge Base articles are scoped to this module's actual functions (mortgage/lease registration, certification, escrow assessment, compliance reporting, staff management), not carried over from real-estate-developer's developer-facing task list.
4. All ticket activity is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. Whether "Emergency Regulatory Support" needs an institution-specific escalation path (e.g. reporting a discovered escrow irregularity), distinct from general emergency support — not addressed by this build.
2. Same adoption question as Feature #1 (Service Requests) — needs client confirmation that this shared-features layer as a whole is wanted.

## Notes

* **Deliberately narrower than real-estate-developer's version, not a lesser copy of it.** Training Resources and Feedback & Suggestions are dropped because this module's audience and use case genuinely differ — not because less effort went into this build. See Feature Overview.
* **Contact RERA Support and System Status are close to identical to real-estate-developer's version by design**, since the same regulator, and plausibly the same platform-wide system status mechanism, underlies both modules.
