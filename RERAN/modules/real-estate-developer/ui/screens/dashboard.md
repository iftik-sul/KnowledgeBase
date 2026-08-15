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

# Screen: Dashboard

**Access:** All four roles — Developer Principal / Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison. Group B does not gate access by role or permission scope; see [navigation.md](../../navigation.md). Role is audit-trail attribution only.

The Dashboard is the landing screen shown immediately after login. Its chrome (sidebar mechanics, top bar title, search) is shared; the Purpose, Layout, section content, Empty State, and Reused Components are role-specific and are documented in full under [Role Variations](#role-variations).

## Purpose

Purpose differs between variants — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Dashboard**
* **Top Bar Title:** Dashboard
* **Search Bar:** Search anything...

Which sidebar menu items are visible, the welcome subtitle, top-bar page actions, and the overall layout diagram differ by role — see [Role Variations](#role-variations).

## Sections

Every numbered section (Welcome Banner, KPI Cards, Quick Actions, and the role-specific tables and feeds below them) differs between variants — see [Role Variations](#role-variations).

## Empty State

Empty state message and actions differ by role — see [Role Variations](#role-variations).

## Reused Components

Differs between variants — see [Role Variations](#role-variations).

## Role Variations

> **Reframed 2026-08-15 — these are content variants, not access restrictions.** Every variant
> below is reachable and actionable by all four roles; none of them is withheld from anyone. What
> the blocks record is that the source material defined this screen more than once, with different
> KPI sets, filters, columns, actions or empty states each time — differences of *content*, not of
> permission. Those are preserved verbatim rather than merged, because collapsing them into one
> screen is a design decision about which variant (or which union of them) is correct, and that is
> the client's call, not a documentation cleanup. **Flagged for review — see
> [../README.md](../README.md#per-role-content-variants-flagged-for-review).**
>
> The role headings below should now be read as *"the variant the source defined under this role's
> heading"*, not *"what this role is allowed to see"*.

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Dashboard**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

### Top Bar Status

**Title:** Dashboard

**Subtitle:** Welcome back, **{Developer Principal Name}**

**Search Bar:** Search anything...

No page-specific actions are displayed in the top bar. It uses the shared **Background \+ HorizontalBorder** component consistent with the rest of the platform.

### Purpose

Provide the Developer Principal / Director with a high-level executive overview of the organization, highlighting business performance, regulatory status, pending actions, and recent activities immediately after login.

### Dashboard Layout

Top Bar  
↓  
Welcome Banner  
↓  
KPI Cards (8)  
↓  
Quick Actions  
↓  
Recent Projects            Applications Status  
↓  
Sales & Escrow Overview    Compliance & Alerts  
↓  
Recent Activity

### Section 1 — Welcome Banner

A compact banner introducing the dashboard.

#### **Left**

* Welcome back, {Developer Principal Name}  
* Company Name  
* Developer Registration Number  
* Verification Badge (Verified / Pending)

#### **Right**

Primary Button

* View Reports

Secondary Button

* View Projects

### Section 2 — KPI Cards

Display 8 KPI cards in a responsive grid.

| KPI | Description |
| ----- | ----- |
| Active Projects | Total ongoing development projects |
| Property Registrations | Total registered properties |
| Pending Applications | Applications awaiting RERA action |
| Approved Applications | Successfully approved applications |
| Active Sales Listings | Properties currently available for sale |
| Active Escrow Cases | Escrow processes currently in progress |
| Compliance Issues | Outstanding regulatory items requiring attention |
| Documents Awaiting Action | Documents requested or pending submission |

Clicking any KPI opens the corresponding module with appropriate filters applied.

### Section 3 — Quick Actions

Large action cards providing shortcuts to frequently monitored areas.

Actions:

* View Projects  
* View Property Registrations  
* Review Sales & Disclosures  
* View Escrow Status  
* Review Applications  
* Generate Reports

Since the Principal / Director is primarily an oversight role, these actions navigate to existing operational modules rather than creating new records.

### Section 4 — Recent Projects

Card/Table showing recently active projects.

Columns

* Project Name  
* Location  
* Current Stage  
* Completion %  
* Registration Status  
* Last Updated  
* Action (View)

Display latest 5 projects with **View All**.

### Section 5 — Applications Overview

Table displaying recent submissions.

Columns

* Reference No.  
* Service  
* Submitted By  
* Submitted Date  
* Current Status  
* Assigned RERA Officer  
* Action

Latest 5 applications.

### Section 6 — Sales & Escrow Overview

Two equal-width summary cards.

#### **Sales Summary**

* Active Listings  
* Units Sold  
* Pending Disclosures  
* Recently Updated Listings

#### **Escrow Summary**

* Active Escrow Accounts  
* Pending Fund Releases  
* Completed Releases  
* Escrow Issues

Each card includes a **View Details** link.

### Section 7 — Compliance & Alerts

Highlight items requiring executive attention.

Examples

* Documents requested by RERA  
* Project inspection scheduled  
* Escrow milestone overdue  
* Pending sales disclosure  
* Application returned for correction  
* Compliance deadline approaching

High-priority items appear first.

### Section 8 — Recent Activity

Timeline showing organizational activity.

Examples

* New project submitted  
* Property registration approved  
* Sales disclosure completed  
* Escrow milestone achieved  
* Document uploaded  
* RERA comment received

Latest 10 activities.

### Empty State

For a newly approved developer with no operational data:

**Message**

> Welcome to the RERA Developer Portal. Your organization is ready to begin managing development projects and regulatory activities.

Primary actions:

* View Company Profile  
* Explore Projects

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

This dashboard is designed for **executive monitoring**, allowing the Developer Principal / Director to understand the organization's overall operational and regulatory status at a glance without performing day-to-day operational tasks.

### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Dashboard**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

### Top Bar Status

**Title:** Dashboard

**Subtitle:** Welcome back, **{Project Registration Officer Name}**

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Register New Project  
* Register Property

### Purpose

Provide the Project Registration Officer with an operational workspace to manage development project registrations, property registrations, regulatory applications, and supporting documents. The dashboard prioritizes tasks requiring action, submission status, and pending responses from RERA.

### Layout

Top Bar  
↓  
Welcome Banner  
↓  
KPI Cards  
↓  
Quick Actions  
↓  
Projects Requiring Attention      Pending Applications  
↓  
Recent Property Registrations     RERA Requests  
↓  
Upcoming Deadlines  
↓  
Recent Activity

### Section 1 — Welcome Banner

#### **Left**

* Welcome back, {Officer Name}  
* Company Name  
* Assigned Department  
* Current Work Queue

#### **Right**

Primary Button

* Register New Project

Secondary Button

* Register Property

### Section 2 — KPI Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Active Projects | Projects assigned to you |
| Draft Projects | Projects not yet submitted |
| Pending Property Registrations | Awaiting submission or review |
| Applications Under Review | Currently with RERA |
| Returned Applications | Require corrections |
| Documents Pending Upload | Missing required documents |
| Due This Week | Tasks approaching deadline |
| Completed This Month | Successfully completed registrations |

Selecting a KPI automatically filters the relevant module.

### Section 3 — Quick Actions

Display shortcut cards.

* Register New Project  
* Register Property  
* Submit Application  
* Upload Documents  
* View Returned Applications  
* Generate Registration Report

### Section 4 — Projects Requiring Attention

Table displaying projects needing immediate action.

#### **Columns**

* Project Name  
* Project ID  
* Current Stage  
* Pending Action  
* Due Date  
* Priority  
* Action

Actions

* Continue Registration  
* View Details

### Section 5 — Pending Applications

Table showing applications currently in progress.

#### **Columns**

* Application ID  
* Application Type  
* Related Project  
* Submitted Date  
* Current Status  
* Days in Process  
* Action

Actions

* View Details

### Section 6 — Recent Property Registrations

Table showing recently created registrations.

#### **Columns**

* Registration Number  
* Property  
* Project  
* Submission Date  
* Status  
* Action

Actions

* View Registration

### Section 7 — RERA Requests

Shows items requiring action from the Project Registration Officer.

Examples

* Additional documents requested  
* Registration returned for correction  
* Technical clarification requested  
* Inspection scheduled  
* Missing information notification

Each request displays:

* Request Type  
* Related Application  
* Requested By  
* Due Date  
* Priority  
* Action

### Section 8 — Upcoming Deadlines

Timeline or task list.

Examples

* Project submission deadline  
* Property registration deadline  
* Document submission deadline  
* Response due to RERA  
* Scheduled inspection

High-priority deadlines appear first.

### Section 9 — Recent Activity

Timeline showing operational activities.

Examples

* Project created  
* Property registered  
* Documents uploaded  
* Application submitted  
* RERA review started  
* Additional information requested  
* Registration approved

Display the latest 10 activities.

### Empty State

For a newly assigned Project Registration Officer:

**Message**

> Welcome to the Project Registration workspace. Start by registering a new development project or adding property registrations to an existing project.

Primary Button

* Register New Project

Secondary Button

* Register Property

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard

├── Register New Project

├── Register Property

├── Submit Application

├── Upload Documents

├── View Returned Applications

└── Open Project Details

### Notes

* This is an **operational dashboard**, unlike the Developer Principal's executive dashboard.  
* The emphasis is on **creating, submitting, tracking, and responding** rather than monitoring.  
* KPI cards and task lists should prioritize actionable work, overdue items, and pending responses from RERA.  
* The primary CTAs (**Register New Project** and **Register Property**) should always remain prominently visible to support the officer's day-to-day workflow. This aligns with the Project Registration Officer's responsibilities of project registration, application submission, document management, and registration tracking.

### Sales & Disclosure Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Dashboard**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

### Top Bar Status

**Title:** Dashboard

**Subtitle:** Welcome back, **{Sales & Disclosure Officer Name}**

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Create Sales Disclosure  
* Record Property Sale

### Purpose

Provide the Sales & Disclosure Officer with an operational workspace for recording property sales, preparing sales disclosures, submitting regulatory information to RERA, tracking disclosure approvals, and responding to compliance requests.

Unlike the Project Registration Officer, whose work centers on project and property registration, this dashboard focuses on **property sales and disclosure compliance**.

### Layout

Top Bar  
↓  
Welcome Banner  
↓  
KPI Cards  
↓  
Quick Actions  
↓  
Sales Requiring Action        Pending Disclosures  
↓  
Recent Property Sales         RERA Requests  
↓  
Upcoming Deadlines  
↓  
Recent Activity

### Section 1 — Welcome Banner

#### **Left**

* Welcome back, {Officer Name}  
* Company Name  
* Assigned Department  
* Current Sales Queue

#### **Right**

Primary Button

* Create Sales Disclosure

Secondary Button

* Record Property Sale

### Section 2 — KPI Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Active Property Listings | Properties currently available for sale |
| Sales Awaiting Disclosure | Sales that still require disclosure |
| Draft Disclosures | Disclosures not yet submitted |
| Submitted Disclosures | Submitted to RERA |
| Returned Disclosures | Require correction |
| Approved Disclosures | Successfully approved |
| Buyer Documents Pending | Buyer documents awaiting upload or verification |
| Due This Week | Sales activities approaching deadline |

Selecting a KPI filters the corresponding records.

### Section 3 — Quick Actions

Display shortcut cards.

* Record Property Sale  
* Create Sales Disclosure  
* Upload Buyer Documents  
* Respond to RERA Query  
* View Returned Disclosures  
* Generate Sales Report

### Section 4 — Sales Requiring Action

Table displaying sales that need attention.

#### **Columns**

* Sale Reference  
* Property  
* Buyer  
* Current Stage  
* Required Action  
* Due Date  
* Priority  
* Action

#### **Actions**

* Continue  
* View Details

### Section 5 — Pending Disclosures

Table showing disclosure submissions currently being processed.

#### **Columns**

* Disclosure ID  
* Property  
* Buyer  
* Submitted Date  
* Current Status  
* Days in Process  
* Action

#### **Actions**

* View Details

### Section 6 — Recent Property Sales

Table showing recently recorded sales.

#### **Columns**

* Sale Reference  
* Property  
* Buyer  
* Sale Date  
* Sale Value  
* Disclosure Status  
* Action

#### **Actions**

* View Sale

### Section 7 — RERA Requests

Display requests requiring action.

Examples:

* Additional buyer information requested  
* Disclosure returned for correction  
* Missing supporting documents  
* Compliance clarification requested  
* Verification scheduled

Each request displays:

* Request Type  
* Related Disclosure  
* Requested By  
* Due Date  
* Priority  
* Action

### Section 8 — Upcoming Deadlines

Display upcoming regulatory deadlines.

Examples

* Submit Sales Disclosure  
* Respond to RERA Query  
* Upload Buyer Documentation  
* Correct Returned Disclosure  
* Compliance Submission

Critical deadlines appear first.

### Section 9 — Recent Activity

Timeline showing operational activities.

Examples

* Property sold  
* Sales disclosure created  
* Buyer documents uploaded  
* Disclosure submitted  
* RERA review started  
* Additional information requested  
* Disclosure approved

Display the latest 10 activities.

### Empty State

For a newly assigned Sales & Disclosure Officer:

**Message**

> Welcome to the Sales & Disclosure workspace. Record your first property sale or create a sales disclosure to begin managing regulatory sales compliance.

Primary Button

* Record Property Sale

Secondary Button

* Create Sales Disclosure

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
├── Record Property Sale  
├── Create Sales Disclosure  
├── Upload Buyer Documents  
├── Respond to RERA Query  
├── View Returned Disclosures  
└── Open Sales Details

### Notes

* This is the **operational dashboard** for the **Sales & Disclosure Officer**.  
* The dashboard prioritizes **sales transactions**, **buyer documentation**, **sales disclosure compliance**, and **returned disclosures**.  
* Returned disclosures and pending RERA requests should always appear at the top of the dashboard.  
* The primary CTAs (**Record Property Sale** and **Create Sales Disclosure**) remain permanently visible to support the officer's daily workflow.  
* The dashboard should surface buyer-document issues early to prevent delays in disclosure approval.

### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Dashboard**  
* **Other Menu Items:** the full shared sidebar — every menu item is visible to every role, see [navigation.md](../../navigation.md).

### Top Bar Status

**Title:** Dashboard

**Subtitle:** Welcome back, **{Escrow Liaison Name}**

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Request Fund Release  
* Register Escrow Account

### Purpose

Provide the Escrow Liaison with an operational workspace for managing escrow accounts, coordinating with financial institutions, monitoring construction milestones, preparing fund release requests, and ensuring compliance with RERA escrow regulations.

Unlike the Project Registration Officer and Sales & Disclosure Officer, this dashboard focuses entirely on **escrow operations, fund management, and milestone-based releases**.

### Layout

Top Bar  
↓  
Welcome Banner  
↓  
KPI Cards  
↓  
Quick Actions  
↓  
Escrow Accounts Requiring Action      Pending Fund Releases  
↓  
Recent Escrow Activities              RERA / Bank Requests  
↓  
Upcoming Milestones & Deadlines  
↓  
Recent Activity

### Section 1 — Welcome Banner

#### **Left**

* Welcome back, {Officer Name}  
* Company Name  
* Assigned Department  
* Current Escrow Portfolio

#### **Right**

Primary Button

* Request Fund Release

Secondary Button

* Register Escrow Account

### Section 2 — KPI Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Active Escrow Accounts | Escrow accounts currently managed |
| Pending Fund Releases | Release requests awaiting submission or approval |
| Milestones Under Review | Construction milestones awaiting verification |
| Funds Released This Month | Successfully released funds |
| Returned Release Requests | Requests requiring correction |
| Pending Bank Actions | Awaiting financial institution response |
| Due This Week | Milestones or releases approaching deadline |
| Completed Escrow Activities | Successfully completed escrow tasks this month |

Selecting a KPI filters the relevant records.

### Section 3 — Quick Actions

Display shortcut cards.

* Register Escrow Account  
* Request Fund Release  
* Upload Escrow Documents  
* Respond to RERA Query  
* View Returned Requests  
* Generate Escrow Report

### Section 4 — Escrow Accounts Requiring Action

Table displaying escrow accounts that need attention.

#### **Columns**

* Escrow ID  
* Project  
* Financial Institution  
* Current Milestone  
* Required Action  
* Due Date  
* Priority  
* Action

#### **Actions**

* Continue  
* View Details

### Section 5 — Pending Fund Releases

Table showing fund release requests currently being processed.

#### **Columns**

* Release Request ID  
* Escrow Account  
* Milestone  
* Requested Amount  
* Current Status  
* Days in Process  
* Action

#### **Actions**

* View Details

### Section 6 — Recent Escrow Activities

Table showing recently completed escrow activities.

#### **Columns**

* Escrow ID  
* Project  
* Activity  
* Amount  
* Date  
* Status  
* Action

#### **Examples**

* Escrow account created  
* Initial deposit received  
* Milestone verified  
* Fund release approved  
* Funds transferred

### Section 7 — RERA / Bank Requests

Display requests requiring action.

Examples

* Additional escrow documents requested  
* Milestone verification clarification  
* Bank confirmation pending  
* Fund release returned for correction  
* Escrow compliance review scheduled

Each request displays:

* Request Type  
* Related Escrow Account  
* Requested By  
* Due Date  
* Priority  
* Action

### Section 8 — Upcoming Milestones & Deadlines

Display upcoming construction milestones and regulatory deadlines.

Examples

* Milestone inspection  
* Submit fund release request  
* Upload engineer's certification  
* Bank confirmation deadline  
* Escrow compliance review  
* Final escrow reconciliation

Critical deadlines appear first.

### Section 9 — Recent Activity

Timeline showing operational activities.

Examples

* Escrow account created  
* Escrow agreement uploaded  
* Initial deposit confirmed  
* Milestone completed  
* Fund release requested  
* Bank verification completed  
* RERA approved fund release  
* Funds transferred  
* Escrow account closed

Display the latest **10 activities**.

### Empty State

For a newly assigned Escrow Liaison:

**Message**

> Welcome to the Escrow Management workspace. Register your first escrow account or begin managing fund releases for an existing development project.

**Primary Button**

* Register Escrow Account

**Secondary Button**

* View Escrow Management

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard

├── Register Escrow Account  
│      ↓  
│  Escrow Details  
│  
├── Request Fund Release  
│      ↓  
│  Escrow Details  
│  
├── View Escrow Account  
│      ↓  
│  Escrow Details  
│  
├── Respond to Request  
│      ↓  
│  Applications  
│  
└── Generate Report  
       ↓  
    Reports

### Notes

* The dashboard should prioritize **operational tasks**, not executive analytics.  
* High-priority alerts (returned requests, pending bank confirmations, overdue milestones, and upcoming fund releases) should always appear at the top.  
* KPI cards should be interactive and filter the corresponding records.  
* Escrow statuses, milestone statuses, and fund release statuses should reuse the platform's existing status badge components for consistency.

## User Flow

The Developer Principal / Director version of this screen has no explicit User Flow section in the source material. The other three roles do; see their blocks under Role Variations above.

## Notes

The Developer Principal / Director version of this screen has no explicit Notes section in the source material — it closes with a single unheaded paragraph, reproduced under its Role Variations block above. The other three roles have a dedicated Notes section; see their blocks under Role Variations above.
