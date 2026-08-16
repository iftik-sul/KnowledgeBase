---
project: RERAN
module: real-estate-service-companies
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-developer/service-flows/feature-12-help-and-support.md"
  - "RERAN/modules/financial-trust-institutions/service-flows/feature-12-help-and-support.md"
tags:
  - real-estate-service-companies
  - ui-spec
  - help-support
---

# Screen: Help & Support

**Access:** Any of the company's four Group D roles — identical screen for every user.

> **Not sourced — built at Claude's discretion, matching the pattern already established for Financial & Trust Institutions' equivalent screen.** No source material describes this feature; `navigation.md`'s sidebar names it. Structured on Financial & Trust Institutions' Help & Support (itself adapted from Real Estate Developer's), scoped for Group D's brokerage/JOP/property-management audience rather than either of those.

## Purpose

Give every company user the knowledge base, support tickets, and RERA contact routes needed to operate the module.

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
Contact RERA Support
```

## Sections

### Section 1 — Support Summary Cards

Open tickets, resolved tickets, average response time — company-wide.

### Section 2 — Quick Actions

* Create Support Ticket · Search Knowledge Base · Contact RERA Support

### Section 3 — Quick Help Categories

Task-oriented shortcuts, scoped to this module's actual functions: registering JOP supervision, registering an owners' association, licensing and permits, practice cards, management contracts, tenancy system users, auction permits, and filing a dispute.

### Section 4 — Knowledge Base Articles

Article catalogue, grouped by the five service categories.

### Section 5 — Support Tickets

Ticket list with reference, subject, category, priority, status, dates, and Create / View / Reply / Close actions. Company-wide, not per user.

### Section 6 — Contact RERA Support

RERA Support Center, Live Chat, Emergency Regulatory Support — following the pattern established for Groups B and C, since the same regulator and plausibly the same platform-wide support mechanism underlies all three.

## Empty State

**Message**

> No support tickets yet. Search the knowledge base, or create a ticket if you need help from RERA.

**Primary Button:** Create Support Ticket

## Reused Components

Company Operations Sidebar, Top Bar, Buttons.

## Validation

1. No section, article, or contact route is role-gated.
2. Support tickets are company-wide, with author attribution from the audit trail.

## Access

Identical for all four roles.

## User Flow

```
Any Screen
↓
Help & Support
├─ Search / Quick Help Category → Knowledge Base Article
├─ Create Support Ticket → ticket flow
└─ Contact RERA Support → contact route
```

## Notes

* **Deliberately narrower than Real Estate Developer's version, matching Financial & Trust Institutions' precedent, not a lesser copy of either.** Training Resources and Feedback & Suggestions are omitted — this module's professional B2B audience (brokerages, JOP managers, property management firms) reads closer to Financial & Trust Institutions' institutional audience than Real Estate Developer's.
