---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-09
derived_from:
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

UI components reused across screens in this module, gathered from every "Reused Components" list across all 19 screen files (49 role-scoped instances in total). Screen files link here instead of describing a component again.

**Naming is not consistent in the source.** Several components are named differently from screen to screen, or from role to role on the same screen, without any apparent pattern. Where that happens, this file records every name used and picks the most descriptive one as the heading — it does not assume the differently-named mentions are describing different things, but it also doesn't silently erase the inconsistency. Divergences in name or description are called out explicitly rather than smoothed over.

## Layout & Chrome

### Left Sidebar

The persistent navigation sidebar shown on every operational screen (referred to in each screen's own Layout section as the "Developer Operational Sidebar," with role-scoped visible/active menu items). Named "Left Sidebar" in 46 of the 49 Reused Components lists that mention it.

**Naming divergence:** three lists — the Escrow Liaison's variants of [help-and-support.md](screens/help-and-support.md), [notifications.md](screens/notifications.md), and [reports.md](screens/reports.md) — name it "Developer Operational Sidebar" directly instead of "Left Sidebar." Same component; the Escrow Liaison's Reused Components lists on those three screens consistently use the specific instance name rather than the generic component name used everywhere else.

### Top Bar

The page header: title, subtitle, search bar, and page-specific actions, built on a shared background/border treatment referenced across nearly every screen as "the shared Background + HorizontalBorder component."

**Naming divergence, not just cosmetic:** appears as "Top Bar" (bare, mostly on Principal's read-only screens — 15 mentions), "Top Bar (Background + HorizontalBorder)" (21 mentions), "Top Bar (**Background + HorizontalBorder**)" (bold variant, 8 mentions), and with a missing space — "Top Bar (Background +HorizontalBorder)" / "Top Bar (**Background +HorizontalBorder**)" — in 2 mentions (both on operational-role variants of [application-details.md](screens/application-details.md) and [escrow-management.md](screens/escrow-management.md); likely typos rather than a deliberate distinct styling, but preserved as written since this batch's rules don't permit silently "fixing" source wording). The same three Escrow Liaison lists noted under Left Sidebar above list "Background + HorizontalBorder" as if it were a **separate** component from "Top Bar," rather than a styling note on the Top Bar entry — a real structural inconsistency, not just a wording one.

### Search Bar

The top-bar search input, generally captioned "Search anything..." (though [escrow-management.md](screens/escrow-management.md) and [escrow-details.md](screens/escrow-details.md) use role-specific placeholder text instead — see those screens' Role Variations for the exact wording). Named "Search Bar" in every mention except one: [dashboard.md](screens/dashboard.md)'s Developer Principal / Director variant calls it "Search Component" instead, even though every other screen — including that same Dashboard's other three role variants — calls it "Search Bar."

## Data Display

### KPI Cards

Summary metric cards, typically 6–8 per screen, shown near the top of list screens and detail-screen headers. Consistently named "KPI Cards" across all 36 mentions — the most consistently-named component in the whole library.

### Data Table

Tabular list of records with sortable/filterable columns. Named "Data Table" (18 mentions) and "Data Tables" (18 mentions, plural) in roughly equal measure, with no discernible pattern (varies by screen, not by role) — purely a singular/plural inconsistency, not a meaning difference.

### Information Cards

Two-column (or multi-field) read-only information display, used throughout detail screens for things like "Basic Information," "Property Information," "Financial Institution Information." Consistently named across all 17 mentions.

### Analytics Cards

A card presenting 2–4 rollup metrics together (e.g. "Sales Performance," "Compliance Summary"), distinct from the single-metric KPI Cards above.

**Naming divergence:** most screens ([applications.md](screens/applications.md), [documents.md](screens/documents.md), [sales-and-disclosures.md](screens/sales-and-disclosures.md), [property-registrations.md](screens/property-registrations.md), [escrow-management.md](screens/escrow-management.md) — 7 mentions) call this "Analytics Cards"; [reports.md](screens/reports.md) (3 mentions, all operational-role variants) calls the same kind of card "Analytics Widgets" instead.

### Status Badges

The colour-coded status indicator shown on records throughout the module. **See [status-badges.md](status-badges.md) for the full status vocabulary** — that file also documents the significant conflicts found between roles' status lists. Named consistently as "Status Badges" in all 48 mentions, the most common component in the library after Left Sidebar.

### Document Viewer

An embedded, in-page preview of a document (zoom, rotate, page navigation, download), used on read-only detail screens.

**Naming divergence:** the Developer Principal / Director's variants say "Document Viewer" (3 mentions — [application-details.md](screens/application-details.md), [escrow-details.md](screens/escrow-details.md)); the operational roles' equivalents on [document-details.md](screens/document-details.md) all say "Embedded Document Viewer" instead (4 mentions). Likely the same component with the Principal's screens using a shortened name, since the underlying feature list (zoom, rotate, page navigation, full screen, download) is identical wherever it's spelled out in full in the screen body — but the Reused Components lists themselves never spell that out, so this is inferred, not confirmed from the component list alone.

### Version History Table

A table of every previously uploaded version of a document.

**Naming divergence:** [document-details.md](screens/document-details.md)'s Principal variant calls it "Version History Component" (1 mention); the three operational-role variants of the same screen, plus [fund-release-request-details.md](screens/fund-release-request-details.md), call it "Version History Table" (3 mentions).

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

**⚠ Possible conflict, not fully resolved:** "Task Cards" (3 mentions — [applications.md](screens/applications.md), [documents.md](screens/documents.md), both operational-role variants) and "Task List" (2 mentions — [dashboard.md](screens/dashboard.md)'s Registration Officer and Sales & Disclosure Officer variants) are presented together here because they describe the same kind of "requires action" summary, but the source never clarifies whether "Task Cards" and "Task List" are the same visual pattern (a list vs. a card grid) or genuinely different presentations of the same data. Not merged into a single unqualified name; both are recorded.

### Information Tabs

The tab navigation used on the Escrow Liaison's detail screens (Overview / Fund Releases / Milestones / Documents / Activity Log, etc.) in place of stacked sections.

**Naming divergence:** "Information Tabs" on 3 mentions ([application-details.md](screens/application-details.md), [document-details.md](screens/document-details.md), [fund-release-request-details.md](screens/fund-release-request-details.md), all Escrow Liaison variants); "Tabs" once, on [escrow-details.md](screens/escrow-details.md)'s Escrow Liaison variant.

### Confirmation Dialogs

Modal confirmation prompts, mentioned only on Escrow Liaison operational screens (5 mentions — [applications.md](screens/applications.md), [document-details.md](screens/document-details.md), [documents.md](screens/documents.md), [fund-release-request-details.md](screens/fund-release-request-details.md)). No other role's Reused Components lists mention this component at all, even on screens with similarly consequential actions (e.g. submitting an application) — plausibly an oversight in the source rather than a deliberate role restriction, but not assumed either way here.

### Overflow Action Menu

A "more actions" overflow menu on table rows, mentioned once, on [escrow-management.md](screens/escrow-management.md)'s Escrow Liaison variant (its Escrow Accounts Table's Row Actions use an overflow menu for secondary actions rather than listing them inline).

## Forms & Inputs

### Editable Form Components

Grouped, editable form fields on creation/edit screens.

**Naming divergence:** "Editable Form Components" on 5 mentions ([application-details.md](screens/application-details.md), [document-details.md](screens/document-details.md), [sales-and-disclosure-details.md](screens/sales-and-disclosure-details.md)); "Form Components" on 2 mentions ([project-details.md](screens/project-details.md), [property-registration-details.md](screens/property-registration-details.md)); "Form Sections" once, on [fund-release-request.md](screens/fund-release-request.md).

### File Upload Component

A document upload widget with replace/preview/delete actions, backing every screen's "Supporting Documents" / "Required Documents" section.

**Possible naming divergence, reported not resolved:** "File Upload Component" on 8 mentions across most operational form screens; "Document Upload Table" on 2 mentions, both on Escrow Liaison forms ([application-details.md](screens/application-details.md), [fund-release-request.md](screens/fund-release-request.md)). Every screen's actual Supporting Documents section — regardless of which name its Reused Components list uses — describes the identical pattern: a table with Document/Status/Uploaded On/Version/Action columns and Upload/Replace/Preview/Delete row actions. It's plausible "Document Upload Table" and "File Upload Component" are two names for that exact same pattern; it's also plausible the Escrow Liaison's forms present upload as a table-first UI while other roles' forms present it as a discrete upload widget with a table underneath. The source doesn't say which, so both names are kept rather than collapsed into one.

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

A dedicated sidebar of alerts and reminders, mentioned once, on [escrow-details.md](screens/escrow-details.md)'s Escrow Liaison variant (backing that screen's unique "Right Sidebar — Alerts & Reminders" section — see that file's Role Variations).

**Possible naming divergence, not resolved:** "Alert Cards" (Dashboard, Principal) and "Alert Panel" (Escrow Details, Escrow Liaison) might be the same underlying alerting component used in two different layouts (a card grid vs. a sidebar panel), or they might be unrelated. Each is mentioned only once in the entire source, so there isn't enough information to say either way — recorded separately rather than merged on a guess.

### Notification Cards / Notification List

The rendering of an individual notification.

**Naming divergence:** "Notification Cards" on 3 mentions (Developer Principal / Director, Registration Officer, Sales & Disclosure Officer variants of [notifications.md](screens/notifications.md)); the Escrow Liaison's variant of the same screen instead lists "Notification List" (implying a denser list rendering rather than cards) plus a separate "Priority Alert Cards" entry that the other three roles don't call out independently (they fold priority notifications into the same Notification Cards component, backed by a separate "Priority Indicators" badge — see below).

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
