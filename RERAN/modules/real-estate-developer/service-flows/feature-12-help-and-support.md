---
project: RERAN
module: real-estate-developer
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/ui/screens/help-and-support.md"
tags:
  - real-estate-developer
  - shared-feature
  - help-support
---

# Feature #12 – Help & Support

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

**Help & Support** gives any developer user the knowledge base, support tickets, contact routes to RERA, system status, and training resources needed to use the module. Unlike financial-trust-institutions' equivalent feature, this one has a fully built screen — the source described four variants with genuinely disagreeing section sets, all merged into one.

## 2. Purpose

Give every developer user access to the full set of help resources and RERA contact routes, regardless of role, rather than the narrower subset any one prior role-based design happened to expose.

## 3. Description

Rebuilt 2026-08-15 from four designs whose section sets genuinely disagreed — three variants had System Status and Feedback & Suggestions but lacked Training Resources and Quick Help Categories; the fourth (Escrow Liaison) had exactly the reverse. All four sections are kept; the three omissions read as gaps in the source rather than deliberate restrictions, since there's no coherent reason an escrow user wouldn't need system status, or a registration user training material. Quick Help Categories and Training Resources, both escrow-only in source, are generalized to cover every module function — flagged as extrapolated, not sourced, for the non-escrow entries specifically.

## 4. Used By

Not tied to any single numbered service — reachable from any screen in the module.

## 5. Prerequisites

* User is logged into a registered developer company account.

## 6. Required Information

Search terms for Knowledge Base search; ticket subject/category/priority when creating a support ticket.

## 7. Required Documents

None required; attachments optional on support tickets.

## 8. Service Fee

No fee.

## 9. Payment Required

**No.**

## 10. Processing Authority

**Any of the developer's four Group B roles** — no section, article, contact route, or action is role-gated.

## 11. Expected Processing Time

Knowledge base search and article access are immediate. Support ticket response time is not given a fixed sourced figure — Support Summary Cards display an "average response time" as a reported metric, not a committed SLA.

## 12. Processing Workflow

Any Screen
↓
Open Help & Support
↓
Search Knowledge Base **or** Browse Quick Help Categories **or** Create Support Ticket **or** Contact RERA Support **or** View Training Resources
↓
*(on ticket)* Ticket Created → Organization-Wide Ticket List → Reply / Close

## 13. Application Status Flow

Support Ticket: Open → In Progress → Resolved / Closed. Not otherwise a submission-based feature with a broader application status flow.

## 14. Possible Outcomes

* Knowledge Base Article Found
* Support Ticket Created / Resolved
* RERA Support Contacted

## 15. Output

* Support ticket record, organization-wide, with author attribution from the audit trail
* Feedback/suggestion submission record

## 16. Related Features

None directly — this feature is a standalone resource, reachable from every other screen in the module rather than feeding into or from any specific one.

## 17. UI Screens

* Help & Support

## 18. API Requirements

* Retrieve Knowledge Base Articles / Search
* Retrieve Quick Help Categories, Training Resources
* Create / Retrieve / Reply to / Close Support Tickets
* Retrieve System Status
* Submit Feedback
* Create Audit Log

## 19. Database Entities

* Developer Company, User
* Support Ticket, Knowledge Base Article
* Feedback Submission
* Audit Log

## 20. Acceptance Criteria

* Any of the developer's four Group B roles can access every section: Knowledge Base, Quick Help Categories, Support Tickets, System Status, Contact RERA Support, Training Resources, Feedback & Suggestions.
* Support tickets and feedback submissions are organization-wide, with author attribution from the audit trail.
* System Status reflects platform availability identically for every user.

## 21. Business Rules

1. No section, article, contact route, or action on this feature is role-gated.
2. Support tickets and feedback are organization-wide, not per-user.
3. Quick Help Categories and Training Resources cover every module function, not escrow alone — the non-escrow entries are extrapolated, not sourced.
4. All ticket and feedback activity is permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. The non-escrow entries in Quick Help Categories and Training Resources are extrapolated from the module's other functions, not sourced — needs client confirmation of the actual content.
2. Same adoption question as Feature #1 — needs client confirmation.
