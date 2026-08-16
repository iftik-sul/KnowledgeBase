---
project: RERAN
module: real-estate-service-companies
type: navigation
status: draft
updated: 2026-08-16
derived_from:
  - "RERAN/modules/real-estate-service-companies/roles-and-responsibilities.md"
  - "RERAN/modules/real-estate-service-companies/services-overview.md"
  - "RERAN/modules/real-estate-service-companies/open-questions.md"
tags:
  - real-estate-service-companies
  - navigation
  - permissions
---

# Real Estate Service Companies — Navigation & Access

**Unified access, from the start.** Group D does not gate access by role. Every user of a verified Group D company account sees and can act on every screen, action, and service in this module. Role is recorded as audit-trail attribution only. Group D skips the role-permission-matrix phase both Group B and Group C went through before arriving at this same model — see `roles-and-responsibilities.md` and `open-questions.md` C2.

---

## Audit-Trail Principle

Every action in this module is logged with the acting user and the role they held at the time:

```
Action: JOP Escrow Transfer Submitted
Performed by: Adaeze Nwosu
Role at time of action: Owners'-Association Manager

Action: Practice Card Application Certified
Performed by: Tunde Bakare
Role at time of action: Brokerage Principal
```

Role is **attribution only**. It does not filter which menu items are visible, which actions are enabled, or who may act on which record. Any of the four roles — Brokerage Principal, Owners'-Association Manager, Property Management Officer, Company Dispute Filing Officer — may perform any action described in this module.

---

## Company Operations Sidebar

One sidebar, identical for every user of a verified Group D company account, regardless of role:

| Menu | Description |
| :---- | :---- |
| Dashboard | Personalized operational overview |
| Services | Browse and start any of the 26 services |
| Applications | Track and act on submitted applications |
| Jointly Owned Property | Register of properties under the company's JOP administrative supervision |
| Documents | Upload and manage documents |
| Company Profile | Licence status, agents' practice cards, staff roster |
| Notifications | View alerts and system messages |
| Help & Support | Contact RERA support |

**Jointly Owned Property gets its own sidebar item, not folded into Applications.** With 11 of the module's 26 services (42%) concerned with JOP administration, and JOP properties themselves persisting as standing records the company returns to repeatedly (escrow transfers, signatory accreditation, auditor appointments — all filed against the same property over time), a dedicated register follows the same reasoning Financial & Trust Institutions used for Trust Accounts: the underlying object needs its own home, separate from the generic application-tracking list.

Every item is visible and actionable to every role. There is no menu filtering, no role-driven read-only variant of any screen.

**Count badges** appear on items carrying actionable work: Applications and Notifications — institution-wide counts, the same for every user.

---

## Access Rules

1. **Every menu item is reachable by every role.** No rendering distinction between roles.
2. **No maker ≠ checker restriction.** No internal company-side certification gate exists anywhere in Group D (`open-questions.md` A5), so this rule has no practical case to apply to yet — recorded for consistency with Groups B and C's own access-rule documents, in case a future service introduces one.
3. **Expired company licence blocks submission, not access.** Every menu item remains reachable; Services saves drafts but will not submit, and directs the user to Company Profile to renew (Service #12). *(Proposed — the specific blocking behavior mirrors Financial & Trust Institutions' equivalent rule, since Group D's own Service #12 plays the same institutional-standing role Financial & Trust Institutions' Service #1 does; needs client confirmation.)*
4. **No role has a read-only variant of any screen.** Every user sees full detail and full action controls on every record in the module.

---

## Landing After Login

Every role lands on the same [Dashboard](ui/screens/dashboard.md), with identical content and no per-role default view — built this way from the start, not corrected into it later.

---

## Service #18 — Confirmed in Group D, Screen Still Pending

**Corrected 2026-08-16 (client decision, `open-questions.md` A2).** This module's navigation previously excluded Service #18 (Register Real Estate Evaluation Details Certificate) entirely, pending confirmation of whether it belonged to Group D or an undocumented Group G module. The client has confirmed it stays in Group D.

**This section is retained, reframed, rather than deleted — because the underlying reason for the exclusion is only partly resolved.** Service #18's own sourced workflow still describes an evaluation company accepting or rejecting customer requests directly, with no RERA review step named — a structurally different shape from every other Group D service. That's now a UI-design problem, not an ownership question: the service is confirmed to belong here, but it still doesn't fit the shared Services Catalogue → Submit Application → Application Details pattern every other service in this navigation model uses.

**Current state, corrected 2026-08-16 — the Services Catalog correction is done, not pending.** Service #18 is documented (`service-flows/service-18-register-evaluation-details-certificate.md`) and now appears in [Services Catalog](ui/screens/services-catalog.md)'s selectable list, matching every other confirmed-in-scope service. What remains genuinely undone is only the service's own dedicated screen: its atypical accept/reject-by-company workflow has no designed wizard to route into, so selecting it from the catalogue currently leads to a placeholder state, not a functioning application flow.

---

## External Access

**Registration / Service Trustee Centre operators (Group G)** may act on some Group D services in assisted mode, the same way they do for Groups B and C, wherever the source names a Trustee Centre or physical-counter channel. None of Group D's 26 rows sourced a Trustee Centre channel the way several Financial & Trust Institutions and Individual User services did — every Group D service is sourced as either portal-based or email-based (Services #6, #11, #19). **Corrected 2026-08-16** — previously listed only #6 and #19; Service #11 was found during the same-day Phase 6 audit to also be sourced as email-only, its own Section 12 having incorrectly carried a portal-style workflow inherited from a cross-reference to Service #5. **This means Group D likely has no assisted-mode surface at all**, unlike every other documented module. Flagged for client confirmation rather than assumed as a gap — the source's own silence here may be accurate, not a documentation omission.
