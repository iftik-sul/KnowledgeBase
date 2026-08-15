---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-15
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/ui/screens/dashboard.md"
  - "RERAN/modules/real-estate-developer/ui/screens/applications.md"
  - "RERAN/modules/real-estate-developer/ui/screens/application-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/document-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/reports.md"
  - "RERAN/modules/real-estate-developer/ui/screens/notifications.md"
  - "RERAN/modules/real-estate-developer/ui/screens/help-and-support.md"
  - "RERAN/modules/real-estate-developer/ui/screens/documents.md"
  - "RERAN/modules/real-estate-developer/ui/screens/projects.md"
  - "RERAN/modules/real-estate-developer/ui/screens/project-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registrations.md"
  - "RERAN/modules/real-estate-developer/ui/screens/property-registration-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/sales-and-disclosures.md"
  - "RERAN/modules/real-estate-developer/ui/screens/sales-and-disclosure-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/escrow-management.md"
  - "RERAN/modules/real-estate-developer/ui/screens/escrow-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/fund-release-request.md"
  - "RERAN/modules/real-estate-developer/ui/screens/fund-release-request-details.md"
  - "RERAN/modules/real-estate-developer/ui/screens/company-profile.md"
tags:
  - real-estate-developer
  - ui-spec
  - components
---

# Shared Component Library

UI components reused across screens in this module, gathered from every "Reused Components" list across all 19 screen files (originally 49 role-scoped instances, since merged into 19 unified screens — see [README.md](README.md)). Screen files link here instead of describing a component again.

**Naming is not consistent in the source.** Several components are named differently from screen to screen, or from role to role on the same screen, without any apparent pattern. Where that happens, this file records every name used and picks the most descriptive one as the heading — it does not assume the differently-named mentions are describing different things, but it also doesn't silently erase the inconsistency. Divergences in name or description are called out explicitly rather than smoothed over.

## Layout & Chrome

### Left Sidebar

The persistent navigation sidebar shown on every operational screen (referred to in each screen's own Layout section as the "Developer Operational Sidebar"). **Corrected 2026-08-15:** the sidebar is no longer role-scoped — one identical menu is shown to all four roles, with only the *active* item varying by screen. See [../navigation.md](../navigation.md).. Named "Left Sidebar" in 46 of the 49 Reused Components lists that mention it.

**Naming divergence:** three lists — the Escrow Liaison's variants of [help-and-support.md](screens/help-and-support.md), [notifications.md](screens/notifications.md), and [reports.md](screens/reports.md) — name it "Developer Operational Sidebar" directly instead of "Left Sidebar." Same component; the Escrow Liaison's Reused Components lists on those three screens consistently use the specific instance name rather than the generic component name used everywhere else.

### Top Bar

The page header: title, subtitle, search bar, and page-specific actions, built on a shared background/border treatment referenced across nearly every screen as "the shared Background + HorizontalBorder component."

**Naming divergence, not just cosmetic:** appears as "Top Bar" (bare, mostly on the Principal / Director variants — 15 mentions), "Top Bar (Background + HorizontalBorder)" (21 mentions), "Top Bar (**Background + HorizontalBorder**)" (bold variant, 8 mentions), and with a missing space — "Top Bar (Background +HorizontalBorder)" / "Top Bar (**Background +HorizontalBorder**)" — in 2 mentions (both on operational-role variants of [application-details.md](screens/application-details.md) and [escrow-management.md](screens/escrow-management.md); likely typos rather than a deliberate distinct styling, but preserved as written since this batch's rules don't permit silently "fixing" source wording). The same three Escrow Liaison lists noted under Left Sidebar above list "Background + HorizontalBorder" as if it were a **separate** component from "Top Bar," rather than a styling note on the Top Bar entry — a real structural inconsistency, not just a wording one.

### Search Bar

The top-bar search input, captioned "Search anything...". **Resolved 2026-08-15 — "Search Bar".** One retired variant of [dashboard.md](screens/dashboard.md) called it "Search Component"; every other mention across every screen called it "Search Bar". Resolved to the majority name. The escrow screens previously carried their own placeholder text in their variant blocks; the rebuilt [escrow-management.md](screens/escrow-management.md) and [escrow-details.md](screens/escrow-details.md) use the shared caption, with domain-specific searching handled by their own Filters sections instead of by placeholder wording.

## Data Display

### KPI Cards

Summary metric cards, typically 6–8 per screen, shown near the top of list screens and detail-screen headers. Consistently named "KPI Cards" across all 36 mentions — the most consistently-named component in the whole library.

### Data Table

Tabular list of records with sortable/filterable columns. Named "Data Table" (18 mentions) and "Data Tables" (18 mentions, plural) in roughly equal measure, with no discernible pattern (varies by screen, not by role) — purely a singular/plural inconsistency, not a meaning difference.

### Information Cards

Two-column (or multi-field) read-only information display, used throughout detail screens for things like "Basic Information," "Property Information," "Financial Institution Information." Consistently named across all 17 mentions.

### Analytics Cards

A card presenting 2–4 rollup metrics together (e.g. "Sales Performance," "Compliance Summary"), distinct from the single-metric KPI Cards above.

**Resolved 2026-08-15 — "Analytics Cards".** Most screens (7 mentions) used "Analytics Cards"; [reports.md](screens/reports.md)'s operational variants (3 mentions) used "Analytics Widgets" for the same card. Resolved to the majority name, now referenced from the rebuilt [reports.md](screens/reports.md).

### Status Badges

The colour-coded status indicator shown on records throughout the module. **See [status-badges.md](status-badges.md) for the full status vocabulary** — that file also documents the significant conflicts found between roles' status lists. Named consistently as "Status Badges" in all 48 mentions, the most common component in the library after Left Sidebar.

### Document Viewer

An embedded, in-page preview of a document (zoom, rotate, page navigation, download), used on read-only detail screens.

**Resolved 2026-08-15 — "Embedded Document Viewer".** The Principal / Director variants said "Document Viewer" (3 mentions); the operational variants on [document-details.md](screens/document-details.md) said "Embedded Document Viewer" (4 mentions). This was previously recorded as *probably* the same component, inferred from the identical feature list (zoom, rotate, page navigation, full screen, download) but not confirmed from the Reused Components lists themselves. With the screens rebuilt as single unified screens, one name is required — and the identical feature lists confirm the inference. Resolved to the longer, more descriptive name.

### Version History Table

A table of every previously uploaded version of a document.

**Resolved 2026-08-15 — "Version History Table".** The Principal variant of [document-details.md](screens/document-details.md) called it "Version History Component" (1 mention); the three operational variants plus [fund-release-request-details.md](screens/fund-release-request-details.md) called it "Version History Table" (3 mentions). Same component; resolved to the majority name now that the variants are merged.

### Document List

A list/table of documents linked to a record, distinct from the full [documents.md](screens/documents.md) screen itself. 3 mentions, consistently named ([company-profile.md](screens/company-profile.md), [escrow-details.md](screens/escrow-details.md)).

## Timelines & Progress

Two visually similar but functionally distinct components are both loosely called "timeline" across the source. They are kept separate here because conflating them would lose the distinction between a chronological event log and a linear stage tracker — exactly the kind of meaning-changing merge this batch's rules prohibit.

### Activity Timeline

A **chronological, vertical log of past events** on a record (e.g. "Document uploaded → Verification requested → Verification completed"), always described as showing the latest activity first.

**Naming divergence:** called "Activity Timeline" on detail screens (7 mentions — [application-details.md](screens/application-details.md), [document-details.md](screens/document-details.md), [fund-release-request.md](screens/fund-release-request.md)); plain "Timeline" on several detail/creation screens (16 mentions — the single most overloaded name in this library, also used loosely elsewhere); "Timeline Widget" on list/dashboard screens showing a rolled-up activity feed rather than one record's history (4 mentions — [dashboard.md](screens/dashboard.md), [applications.md](screens/applications.md), [documents.md](screens/documents.md), [notifications.md](screens/notifications.md)); and "Audit Timeline" once, on [company-profile.md](screens/company-profile.md).

### Progress Tracker

A **horizontal, linear stage tracker** showing where a record sits in a fixed pipeline (e.g. "Draft → Submitted → Under Review → Approved"), with the current stage highlighted and completed stages marked.

**Naming divergence:** "Progress Tracker" on most operational form/detail screens (10 mentions); "Progress Timeline" once, on [escrow-details.md](screens/escrow-details.md)'s Developer Principal / Director variant; "Workflow Timeline" once, on [application-details.md](screens/application-details.md)'s Developer Principal / Director variant (that screen's "Approval Workflow" section). Both single-occurrence names are functionally the same component as "Progress Tracker" based on the section content they label, but neither screen's Reused Components list uses the more common name.

## Actions & Navigation

### Buttons

Generic action buttons (Primary/Secondary throughout). Consistently named across all 39 mentions.

### Pagination

Rows-per-page, previous/next, and page-number controls at the bottom of a table. Consistently named across all 20 mentions.

### Filter Bar

The row of filter controls (search, dropdowns, date range, reset) above a data table.

**Naming divergence:** "Filter Bar" on 20 mentions across most screens; "Filter Panel" on 4 mentions, all from the Escrow Liaison's minimalist Reused Components lists ([escrow-management.md](screens/escrow-management.md), [documents.md](screens/documents.md)'s Escrow variant, [help-and-support.md](screens/help-and-support.md) and [notifications.md](screens/notifications.md)'s Escrow variants).

### Quick Action Cards

Shortcut cards on a Dashboard or list screen linking to common next actions (e.g. "Register New Project," "Create Sales Disclosure").

**Naming divergence:** "Quick Action Cards" on 6 mentions (the operational roles' Dashboard variants, [help-and-support.md](screens/help-and-support.md)); "Action Cards" once, on [dashboard.md](screens/dashboard.md)'s Developer Principal / Director variant, describing the same "Section 3 — Quick Actions" pattern under a shorter name.

### Task Cards / Task List

A card- or list-style summary of pending, actionable work items (distinct from a full Data Table of records) — e.g. Dashboard's "Projects Requiring Attention" for operational roles.

**Resolved 2026-08-15 — "Task Cards", with one open question.** "Task Cards" (3 mentions) and "Task List" (2 mentions) both described a "requires action" summary. The rebuilt screens use **Task Cards** on [dashboard.md](screens/dashboard.md)'s Requiring Action section and a **Data Table** on [applications.md](screens/applications.md)'s and [documents.md](screens/documents.md)'s Pending Actions / Pending Verification sections, since those carry per-row columns the dashboard's does not.

**Still open:** whether the source intended a card grid and a list as two distinct visual patterns, or was simply inconsistent. The rebuild picked by context rather than resolving the underlying question — flagged for the client.

### Information Tabs

The tab navigation used on the Escrow Liaison's detail screens (Overview / Fund Releases / Milestones / Documents / Activity Log, etc.) in place of stacked sections.

**Naming divergence:** "Information Tabs" on 3 mentions ([application-details.md](screens/application-details.md), [document-details.md](screens/document-details.md), [fund-release-request-details.md](screens/fund-release-request-details.md), all Escrow Liaison variants); "Tabs" once, on [escrow-details.md](screens/escrow-details.md)'s Escrow Liaison variant.

### Confirmation Dialogs

Modal confirmation prompts. **Updated 2026-08-15:** previously mentioned only on Escrow Liaison variants (5 mentions), and flagged as plausibly a source oversight since no other variant listed it even on screens with similarly consequential actions. With the variants merged, the component now applies wherever a destructive or irreversible action exists — delete a draft, resubmit, close a ticket, restore a document version — on any rebuilt screen. **Proposed**: the extension beyond the escrow screens follows the component's own definition rather than any source statement.

### Overflow Action Menu

A "more actions" overflow menu on table rows, mentioned once, on [escrow-management.md](screens/escrow-management.md)'s Escrow Liaison variant (its Escrow Accounts Table's Row Actions use an overflow menu for secondary actions rather than listing them inline).

## Forms & Inputs

### Editable Form Components

Grouped, editable form fields on creation/edit screens.

**Naming divergence:** "Editable Form Components" on 5 mentions ([application-details.md](screens/application-details.md), [document-details.md](screens/document-details.md), [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md)); "Form Components" on 2 mentions ([project-details.md](screens/project-details.md), [property-registration-details.md](screens/property-registration-details.md)); "Form Sections" once, on [fund-release-request.md](screens/fund-release-request.md).

### File Upload Component

A document upload widget with replace/preview/delete actions, backing every screen's "Supporting Documents" / "Required Documents" section.

**Resolved 2026-08-15 — "File Upload Component", the widget, over a Data Table.** "File Upload Component" appeared on 8 mentions; "Document Upload Table" on 2, both Escrow Liaison forms. Every screen's Supporting Documents section describes the identical pattern regardless of the name used: a table with Document / Status / Uploaded On / Version / Action columns and Upload / Replace / Preview / Delete row actions. The rebuilt screens document that as a **File Upload Component** (the control) rendering above a **Data Table** (the list), which is what both names were describing from different ends. No behaviour changed.

### Validation Panel

The Passed/Warning/Error display driving a Validation Summary section. **See [validation-rules.md](validation-rules.md) for the shared validation mechanism and rules.** Consistently named "Validation Panel" across all 9 mentions.

## Communication

### Communication Thread

A chronological, conversational message log between the developer and RERA (or a financial institution).

**Naming divergence:** "Communication Thread" on 7 mentions; "Conversation Component" once, on [application-details.md](screens/application-details.md)'s Registration Officer variant.

### Empty State

The message-and-CTA pattern shown when a list or record has no content yet.

**Naming divergence:** "Empty State" on 37 mentions, the near-universal name; "Empty State Component" once, on [dashboard.md](screens/dashboard.md)'s Developer Principal / Director variant.

## Alerts & Notifications

### Alert Cards

Dashboard-level alert cards for items needing executive attention, mentioned once, on [dashboard.md](screens/dashboard.md)'s Developer Principal / Director variant ("Section 7 — Compliance & Alerts").

### Alert Panel

A dedicated sidebar of alerts and reminders. Backs the "Right Sidebar — Alerts & Reminders" section of [escrow-details.md](screens/escrow-details.md), which remains its only usage in the module. **Retained through the 2026-08-15 rebuild**: it was defined in only one of that screen's two retired variants, and dropping single-sourced content would have orphaned this component.

**Possible naming divergence, not resolved:** "Alert Cards" (Dashboard, Principal) and "Alert Panel" (Escrow Details, Escrow Liaison) might be the same underlying alerting component used in two different layouts (a card grid vs. a sidebar panel), or they might be unrelated. Each is mentioned only once in the entire source, so there isn't enough information to say either way — recorded separately rather than merged on a guess.

### Notification Cards / Notification List

The rendering of an individual notification.

**Resolved 2026-08-15 — "Data Table" plus "Priority Alert Cards".** Three variants of [notifications.md](screens/notifications.md) listed "Notification Cards"; the Escrow Liaison's listed "Notification List" plus a separate "Priority Alert Cards" entry. The rebuilt screen renders the main feed as a **Data Table** (matching every other list screen in the module, and carrying more per row than a card) and the Priority Notifications section as **Priority Alert Cards**. The Escrow Liaison variant's two-component split turned out to be the more accurate description of what the screen needs; the card-only framing is retired.

### Priority Indicators

A small badge/marker for a notification's priority level (Critical/High/Medium/Low), mentioned on the Registration Officer's and Sales & Disclosure Officer's variants of [notifications.md](screens/notifications.md) (2 mentions).

### Notification Settings Dialog

A modal for configuring notification preferences, mentioned once, on the Escrow Liaison's variant of [notifications.md](screens/notifications.md).

## Screen-Specific Cards (single or narrow occurrence)

These appeared under exactly one screen's Reused Components list (or narrow variants of one screen). Included per this batch's "one definition per component, gathered from every mention" instruction, even though — unlike everything above — none of these currently repeat across *different* screens. A future screen that needs the same pattern should reuse the definition here rather than re-describing it.

* **Welcome Banner** — the greeting banner at the top of [dashboard.md](screens/dashboard.md) (4 mentions — one per role, all on the same screen).
* **Office Cards** — [company-profile.md](screens/company-profile.md)'s Office Locations section.
* **Contact Cards** — [help-and-support.md](screens/help-and-support.md)'s Escrow Liaison variant, for its Contact Options section.
* **Ticket Table** — [help-and-support.md](screens/help-and-support.md)'s Escrow Liaison variant, for its Support Tickets section (other roles' variants render the same section as a Data Table instead — see the Data Table entry above; not merged, since this is the only role that names it separately).
* **Knowledge Base Cards** — [help-and-support.md](screens/help-and-support.md), 3 mentions (Principal, Registration Officer, Sales & Disclosure Officer).
* **Knowledge Base List** — [help-and-support.md](screens/help-and-support.md)'s Escrow Liaison variant — likely this role's name for the same pattern as Knowledge Base Cards above, following the same "List" vs. "Cards" naming split seen in Notification Cards / Notification List.
* **Category Cards** / **Report Category Cards** — [reports.md](screens/reports.md)'s Report Categories section; the Principal's variant says "Category Cards" (1 mention), the three operational roles say "Report Category Cards" (3 mentions).
* **System Status Widget** — [help-and-support.md](screens/help-and-support.md), 3 mentions (Principal, Registration Officer, Sales & Disclosure Officer only — the Escrow Liaison's variant of this screen has no System Status section at all, so no equivalent component).
* **Export Button** / **Generate Report Button** — [reports.md](screens/reports.md)'s Principal variant.
* **Export Dialog** / **Schedule Report Dialog** — [reports.md](screens/reports.md)'s Escrow Liaison variant — plausibly the same actions as Export Button/Generate Report Button above, presented as dialogs instead of direct buttons; not merged, since "button" and "dialog" describe genuinely different interaction patterns and the source doesn't confirm they're interchangeable.
* **Summary Card** — [escrow-details.md](screens/escrow-details.md)'s Escrow Liaison variant, the single card at the top of its tabbed layout consolidating key escrow figures.
* **Detail Cards** — [fund-release-request-details.md](screens/fund-release-request-details.md).
