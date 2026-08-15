---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
tags:
  - real-estate-developer
  - ui-spec
  - dashboard
---

# Screen: Dashboard

**Access:** Any of the developer's four Group B roles — identical screen for every user, no role-based variant.

> **Rebuilt 2026-08-15.** This screen previously described four structurally different dashboards, one per role — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison — each with its own KPI set, Quick Actions, work queue and activity feed. Those four designs are **retired, not merged**: this is one screen that absorbs their load-bearing content, reorganized by *function* rather than by role. Follows the same rework Group C's [`dashboard.md`](../../../financial-trust-institutions/ui/screens/dashboard.md) used under issue #50.

## Purpose

Give any developer user, on login, a single view of the organization's work in flight across every function Group B performs — project registration, property registration, sales and disclosures, escrow and fund releases, and regulatory compliance — with quick access to start something new. No section is gated or reshaped by which of the four roles is looking at it; what a user actually focuses on is a matter of their role in practice, not what the screen shows them.

## Layout

```
Top Bar
↓
Welcome Banner
↓
KPI Summary Cards
↓
Quick Actions
↓
Requiring Action
↓
Focus Areas (Projects & Registrations · Sales & Disclosures · Escrow & Fund Releases · Compliance & Standing)
↓
Upcoming Deadlines
↓
Organization Activity
```

## Sections

### Section 1 — Welcome Banner

A compact banner identifying the user and the organization.

**Left**

* Welcome back, {User Name}
* Company Name
* Developer Registration Number
* Verification Badge (Verified / Pending)

**Right**

* Primary Button — **Register New Project**
* Secondary Button — **View Reports**

**Absorbed 2026-08-15.** The company identity block (name, registration number, verification badge) came from the Principal / Director variant only; the other three showed the user's name alone. It applies to every user and is kept for all. The banner buttons are now the same for everyone — see the reconciliation note in [Notes](#notes) on the Principal's navigation-only actions.

### Section 2 — KPI Summary Cards

Organization-wide totals, identical for every user.

| KPI | Description | Absorbed from |
| :---- | :---- | :---- |
| Active Projects | Ongoing development projects, organization-wide | Principal · Registration Officer *(reconciled — see Notes)* |
| Draft Projects | Created, not yet submitted | Registration Officer |
| Property Registrations | Registered properties, organization-wide | Principal |
| Pending Property Registrations | Awaiting submission or review | Registration Officer |
| Applications With RERA | Submitted, under review, or information requested | Principal · Registration Officer *(reconciled)* |
| Returned Applications | Require correction, any type | Registration Officer · Sales & Disclosure Officer · Escrow Liaison *(reconciled)* |
| Approved Applications | Successfully approved | Principal |
| Active Sales Listings | Properties currently available for sale | Principal · Sales & Disclosure Officer *(reconciled)* |
| Sales Awaiting Disclosure | Sales that still require a disclosure filing | Sales & Disclosure Officer |
| Active Escrow Accounts | Escrow accounts under management | Principal · Escrow Liaison *(reconciled — see Notes)* |
| Pending Fund Releases | Release requests awaiting submission or approval | Escrow Liaison |
| Milestones Under Review | Construction milestones awaiting verification | Escrow Liaison |
| Documents Awaiting Action | Requested, missing, or pending submission | Principal · Registration Officer *(reconciled)* |
| Compliance Issues | Outstanding regulatory items requiring attention | Principal |
| Due This Week | Any deadline within seven days, across all functions | Registration Officer · Sales & Disclosure Officer · Escrow Liaison *(reconciled — see Notes)* |
| Completed This Month | Registrations, disclosures and releases completed | Registration Officer · Escrow Liaison *(reconciled)* |

Selecting a card navigates to the relevant list screen, filtered accordingly.

> **This is a superset, deliberately.** Every KPI that represented real distinct work in any of the four retired variants is present. Nothing was dropped for being "someone else's metric," because there is no longer anyone else — all four roles now do all four kinds of work. Where two variants defined the same metric differently, the reconciliation is recorded in [Notes](#notes) rather than resolved silently.

### Section 3 — Quick Actions

Shortcut cards. **All actions are available to every user. None is conditional on role.**

**Create**

* Register New Project
* Register Property
* Record Property Sale
* Create Sales Disclosure
* Register Escrow Account
* Request Fund Release
* Submit Application

**Respond**

* Upload Documents
* Upload Buyer Documents
* Upload Escrow Documents
* Respond to RERA Query
* View Returned Items

**Review**

* View Projects
* View Property Registrations
* Review Sales & Disclosures
* View Escrow Status
* Review Applications
* Generate Reports

### Section 4 — Requiring Action

A short, prioritized list — not a full table — of records where something is waiting on a developer user, across every function: a project needing correction, a sale awaiting its disclosure, an escrow release blocked on documents, an application returned by RERA, a document RERA has requested.

Each row shows the record reference, what kind of work it is, what is waiting, and how long it has been waiting. Empty when there is nothing to act on, and renders no placeholder card in that case.

**Absorbed 2026-08-15** from the four retired variants' separate work queues — "Projects Requiring Attention" (Registration Officer), "Sales Requiring Action" (Sales & Disclosure Officer), "Escrow Accounts Requiring Action" (Escrow Liaison) and "Compliance & Alerts" (Principal). One list, sorted by urgency across all four kinds of work, rather than four lists a user has to know to look at.

### Section 5 — Focus Areas

**Absorbed 2026-08-15** from the four retired role dashboards' most load-bearing sections — condensed summary cards per function, each linking out to its own full screen rather than duplicating that screen's detail here.

**Projects & Registrations**

* Project counts by status: Active, Draft, Under Review, Approved.
* Property registration counts: Pending, Submitted, Registered.
* Recent Projects — most recently updated, with status. *(From the Principal's "Recent Projects" and the Registration Officer's "Recent Property Registrations".)*
* Links to [projects.md](projects.md) and [property-registrations.md](property-registrations.md).

**Sales & Disclosures**

* Sales summary: Active Listings, Units Sold, Pending Disclosures, Recently Updated Listings. *(The Principal's "Sales Summary" card, retained intact.)*
* Disclosure counts by status: Draft, Submitted, Returned, Approved. *(The Sales & Disclosure Officer's KPI breakdown, condensed.)*
* Buyer Documents Pending — awaiting upload or verification.
* Links to [sales-and-disclosures.md](sales-and-disclosures.md).

**Escrow & Fund Releases**

* Escrow summary: Active Escrow Accounts, Pending Fund Releases, Completed Releases, Escrow Issues. *(The Principal's "Escrow Summary" card, retained intact.)*
* **Oldest Pending Release** — the release request that has waited longest, as a call-to-action card, since the failure mode is a request ageing quietly rather than being hard to find. **Proposed** — not in any source variant; added for the same reason Group C's dashboard added "Oldest Awaiting Assessment."
* Pending Bank Actions — awaiting financial institution response. *(Escrow Liaison.)*
* Links to [escrow-management.md](escrow-management.md).
* **Note:** these are the developer's **project escrow account** figures — a regulated holding account and a real product feature, unrelated to how RERA service fees are paid. See [escrow-management.md](escrow-management.md).

**Compliance & Standing**

* Compliance Issues — count and nearest-severity summary. *(Principal.)*
* RERA Requests — open requests for documents, clarification, or correction, with due dates. *(Absorbed from the identical "RERA Requests" section that appeared in the Registration Officer, Sales & Disclosure Officer and Escrow Liaison variants — three near-identical copies, now one.)*
* Organization standing: verification status and registration validity.
* Links to [applications.md](applications.md), [documents.md](documents.md) and [company-profile.md](company-profile.md).

Every Focus Area is visible to every user, regardless of role. In practice a given user will likely check the areas relevant to what they typically do — but nothing on this screen enforces that as a restriction, and there is no per-role variant of which Focus Areas render.

### Section 6 — Upcoming Deadlines

A timeline or task list of approaching obligations across all functions: project and registration submission deadlines, document submission deadlines, responses due to RERA, scheduled inspections, and escrow milestone dates. High-priority items first.

**Absorbed 2026-08-15** from the "Upcoming Deadlines" sections that appeared separately in three variants, each listing only its own function's deadlines.

### Section 7 — Organization Activity

A compact activity feed: projects submitted, registrations approved, disclosures completed, escrow milestones achieved, documents uploaded, RERA comments received — most recent first, latest 10.

Organization-wide, not filtered to the viewer's own actions, matching the audit-trail-attribution model ([navigation.md](../../navigation.md#audit-trail-principle)) — every row shows who performed the action and what role they held at the time.

## Empty State

**Message**

> Welcome to the RERA Developer Portal. Your organization is ready to begin managing development projects and regulatory activities.

**Primary Button** — Register New Project
**Secondary Button** — View Company Profile

Applies to a newly approved developer with no operational data. Section 4 has its own empty state and simply does not render when nothing is waiting; the rest of the dashboard always renders, since Focus Area summaries and the activity feed stay meaningful even with nothing urgently pending.

**Reconciled 2026-08-15:** the four variants each had a different empty state addressed to their own role ("Welcome to the Project Registration workspace…", "…Sales workspace…", and so on). The organization-level message from the Principal's variant is the one that survives, since the screen is no longer addressed to a role.

## Reused Components

See [components.md](../components.md) for definitions of every component used on this screen — Left Sidebar, Top Bar, Welcome Banner, KPI Cards, Quick Action Cards, Task Cards, Data Table, Status Badges, Timeline Widget, Buttons, Empty State.

## Validation

1. **No card, action, list item, or Focus Area on this screen is role-gated.** What each user sees differs only by what work exists at the organization, never by who they are.
2. **Every Focus Area figure must match its source screen's own figures exactly.** This dashboard has no independent data source and must not drift from [projects.md](projects.md), [property-registrations.md](property-registrations.md), [sales-and-disclosures.md](sales-and-disclosures.md), [escrow-management.md](escrow-management.md), [applications.md](applications.md) or [documents.md](documents.md).
3. **KPI definitions are defined once here and reused.** Where a metric also appears in a Focus Area breakdown, it is the same figure shown at a different grain, never an independently computed one.
4. Status vocabulary comes from [status-badges.md](../status-badges.md); this screen defines no status of its own.

## User Flow

```
Login
↓
Dashboard
├─ Quick Action → the relevant create or list screen
├─ KPI Card / Focus Area link → filtered list screen
├─ Requiring Action row → the record's detail screen
├─ Upcoming Deadline row → the record it concerns
└─ Activity Feed row → the record it concerns
```

## Notes

* **This absorbs, rather than references, the four retired role dashboards.** The Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer and Escrow Liaison sections are gone as separate variants. Their load-bearing pieces — KPI sets, work queues, function summaries, RERA request lists, deadlines and activity feeds — are now sections and Focus Area cards on one screen, visible to everyone.

* **Reconciliation — "Active Projects" meant two different things.** The Principal's variant defined it as "Total ongoing development projects"; the Registration Officer's as "Projects assigned to you." These are not the same metric. Resolved to **organization-wide**, because per-user assignment scoping was an artifact of the retired access model — there is no longer any sense in which a project belongs to one user's view. The same reconciliation applies to every other KPI the Registration Officer's variant scoped with "assigned to you."

* **Reconciliation — "Active Escrow Cases" vs "Active Escrow Accounts."** The Principal's variant said *Cases*, the Escrow Liaison's said *Accounts*, both defined as escrow processes currently in progress. Kept as **Active Escrow Accounts**, matching [escrow-management.md](escrow-management.md) and the service flows, which consistently treat the escrow *account* as the record. "Case" is not used anywhere else in the module.

* **Reconciliation — "Due This Week" appeared three times with three scopes.** The Registration Officer's counted tasks, the Sales & Disclosure Officer's counted sales activities, the Escrow Liaison's counted milestones and releases. Merged into **one cross-function count** of any deadline within seven days. Three separate cards would now double-count the same week for the same user.

* **Reconciliation — "Pending Applications" vs "Applications Under Review."** The Principal's card counted applications "awaiting RERA action"; the Registration Officer's counted those "currently with RERA." Same population, different label. Kept as **Applications With RERA**, matching the status vocabulary in [status-badges.md](../status-badges.md).

* **The Principal's navigation-only Quick Actions are retired, not preserved as a variant.** That variant explained its actions navigate rather than create "since the Principal / Director is primarily an oversight role." That was a permission statement in everything but name. Every user now gets the full create-and-navigate set; a Principal who only ever navigates is exercising a habit, not a constraint.

* **Three near-identical "RERA Requests" sections became one.** The Registration Officer, Sales & Disclosure Officer and Escrow Liaison variants each defined this section with the same fields (Request Type, Related Application, Requested By, Due Date, Priority, Action) and differed only in their example rows. Consolidated into the Compliance & Standing Focus Area; no field was lost.

* **What was dropped, and why.** Only the per-role *framing* — welcome text addressed to a role, "assigned to you" scoping, the oversight-role rationale, and duplicate copies of identical sections. No KPI, section, column, action or empty-state message that represented distinct work was discarded. Where a variant was the sole source of something (the Principal's company identity block and Sales/Escrow summary cards; the Escrow Liaison's Pending Bank Actions and Milestones Under Review; the Sales & Disclosure Officer's disclosure status breakdown and Buyer Documents Pending), it is carried forward.

* **Proposed, not sourced:** the Oldest Pending Release card, the three-way grouping of Quick Actions (Create / Respond / Review), and how many rows a Focus Area summary shows before linking out. Reasonable defaults, flagged as such.

* This screen does not redesign project registration, sales disclosure, escrow management or reporting themselves — those remain their own screens, unchanged by this rework. This screen only summarizes and links to them.
