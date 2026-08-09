---
project: RERAN
module: real-estate-developer
type: ui-spec
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/real-estate-developer/ui-design/RERAN_real_estate_developer_ui.md"
tags:
  - real-estate-developer
  - ui-spec
---

# Screen: Notifications

**Roles:** Principal · Registration Officer · Sales & Disclosure Officer · Escrow Liaison

A centralized communication hub consolidating notifications relevant to the viewing role. The Developer Principal / Director sees organization-wide notifications across every module; the three operational roles (Registration Officer, Sales & Disclosure Officer, Escrow Liaison) each see notifications scoped to their own domain, organized around a dedicated Priority Notifications section that the Principal's version does not have.

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Notifications**
* **Top Bar Title:** Notifications
* **Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

Which sidebar menu items are visible, the subtitle, and the layout diagram differ by role — see [Role Variations](#role-variations). The layout diagram is identical for the Registration Officer, Sales & Disclosure Officer, and Escrow Liaison (Notification Summary Cards → Filters → **Priority Notifications** → Notifications List → Upcoming Deadlines → Recent System Announcements); the Principal's differs both in content (no Priority Notifications or Upcoming Deadlines) and in ending with a Pagination step.

## Sections

Every section (Notification Summary Cards, Filters, the notification types/priority vocabulary, Priority Notifications, the Notifications List, Upcoming Deadlines, Pinned Announcements / Recent System Announcements) is role-specific — see [Role Variations](#role-variations). Only the Principal's version has an explicit **Pagination** section; the other three roles do not paginate the notifications list.

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations). Only the Escrow Liaison's version specifies an **Illustration** (a Notification Bell) alongside the message; the other three roles specify text only.

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Notifications**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * Sales & Disclosures  
  * Escrow Management  
  * Applications  
  * Documents  
  * Reports  
  * Company Profile  
  * **Notifications (Active)**  
  * Help & Support

### Top Bar Status

**Title:** Notifications

**Subtitle:** Stay informed about regulatory updates, application progress, compliance reminders, and organization activities.

**Search Bar:** Search anything...

**Page Actions (Right Side):**

* Mark All as Read  
* Notification Settings

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a centralized communication hub where all notifications from RERA, financial institutions, internal teams, and the platform are consolidated. This screen helps executives stay informed about important events requiring awareness or action.

### Layout

Top Bar  
↓  
Notification Summary Cards  
↓  
Filters  
↓  
Notifications List  
↓  
Pinned Announcements  
↓  
Recent Activities  
↓  
Pagination

### Section 1 — Notification Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| Total Notifications | All notifications received |
| Unread | Notifications not yet viewed |
| High Priority | Critical notifications |
| Action Required | Items requiring organizational action |
| Announcements | Official RERA communications |
| This Week | Notifications received this week |

Selecting a KPI filters the notification list.

### Section 2 — Filters

Located above the notification list.

#### **Components**

* Search Notifications  
* Notification Type  
* Priority  
* Status  
* Source  
* Date Range  
* Reset Filters

### Notification Types

* Applications  
* Projects  
* Property Registration  
* Sales Disclosure  
* Escrow  
* Documents  
* Company Profile  
* Compliance  
* License  
* Payment  
* Announcement  
* System

### Priority Levels

* Critical  
* High  
* Medium  
* Low

### Status

See [status-badges.md](../status-badges.md#notification-status).

### Section 3 — Notifications List

Each notification is displayed as a card.

Each card contains:

#### **Header**

* Notification Icon  
* Notification Title  
* Priority Badge  
* Time Received

#### **Body**

* Short Description  
* Related Module  
* Related Reference Number *(if applicable)*

#### **Footer**

* View Details  
* Mark as Read

Unread notifications are visually highlighted.

### Section 4 — Pinned Announcements

Displays important organization-wide announcements.

Examples

* New RERA Regulation  
* Scheduled Platform Maintenance  
* New Compliance Requirement  
* Policy Update  
* Holiday Notice

Each announcement displays:

* Title  
* Summary  
* Published Date  
* Effective Date

Button

* Read Full Announcement

### Section 5 — Recent Activities

Timeline showing significant recent events.

Examples

* Project Approved  
* Property Registration Completed  
* Escrow Fund Released  
* License Renewal Due  
* Compliance Certificate Issued  
* Sales Disclosure Approved  
* Document Verification Completed

Each activity displays:

* Activity  
* Date & Time  
* Current Status  
* Related Module

Selecting an activity opens the related record.

### Empty State

If there are no notifications:

**Message**

> You're all caught up\! There are no new notifications at this time.

Primary Button

* Go to Dashboard

### Pagination

Bottom of the page.

Components

* Rows per page  
* Previous  
* Next  
* Page Number  
* Total Records

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Notifications

├── Read Notification

├── View Related Record

├── Mark as Read

└── Open Announcement

### Notes

* This is the **central communication hub** for the **Developer Principal / Director**.  
* Notifications are aggregated from every module in the platform, ensuring executives do not need to monitor each module individually.  
* High-priority and action-required notifications should remain pinned at the top until acknowledged.  
* Every notification should include deep links to the relevant module (Project, Property Registration, Escrow, Application, Document, etc.) to reduce navigation time.  
* Read/unread status is tracked per user and synchronized across devices.

### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Notifications**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * Applications  
  * Documents  
  * Reports  
  * **Notifications (Active)**  
  * Help & Support

### Top Bar Status

**Title:** Notifications

**Subtitle:** Stay informed about project registrations, regulatory updates, document reviews, and upcoming deadlines.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Mark All as Read  
* Notification Settings

### Purpose

Provide the Project Registration Officer with a centralized notification center for monitoring all operational events related to projects, property registrations, applications, documents, and communications from RERA. The page prioritizes actionable notifications so officers can respond promptly and maintain compliance with regulatory timelines.

### Layout

Top Bar  
↓  
Notification Summary Cards  
↓  
Filters  
↓  
Priority Notifications  
↓  
Notifications List  
↓  
Upcoming Deadlines  
↓  
Recent System Announcements

### Section 1 — Notification Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Notifications | All notifications |
| Unread | Notifications not yet viewed |
| High Priority | Urgent notifications |
| RERA Requests | Information or action requests |
| Returned Items | Returned projects, registrations, or applications |
| Upcoming Deadlines | Due within the next 7 days |
| Document Reviews | Document verification updates |
| Completed Today | Notifications resolved today |

Selecting a KPI filters the notification list.

### Section 2 — Filters

Allow officers to quickly locate specific notifications.

#### **Components**

* Search Notifications  
* Notification Type  
* Priority  
* Status (Read / Unread)  
* Related Module  
* Date Range  
* Reset Filters

#### **Notification Types**

* Project Registration  
* Property Registration  
* Application  
* Document  
* Inspection  
* Deadline Reminder  
* RERA Announcement  
* System Notification

#### **Priority Levels**

* Critical  
* High  
* Medium  
* Low

### Section 3 — Priority Notifications

Display important notifications requiring immediate action.

Examples:

* Additional information requested by RERA  
* Project returned for correction  
* Property registration returned  
* Application approaching deadline  
* Missing mandatory documents  
* Scheduled inspection tomorrow

Each notification displays:

* Priority Indicator  
* Notification Title  
* Related Record  
* Due Date  
* Time Received

Primary Action

* Resolve Now

Secondary Action

* View Details

### Section 4 — Notifications List

Chronological list of notifications.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Notification | Title |
| Module | Related module |
| Reference | Project / Property / Application ID |
| Date & Time | Received |
| Status | Read / Unread |
| Priority | Priority level |
| Action | Open |

#### **Notification Actions**

* View Details  
* Mark as Read  
* Mark as Unread  
* Archive *(where permitted)*

### Section 5 — Upcoming Deadlines

Display all upcoming regulatory deadlines.

#### **Columns**

| Deadline | Related Record | Due Date | Days Remaining | Action |
| :---: | :---: | :---: | :---: | :---: |

Examples

* Submit Project Registration  
* Respond to RERA Query  
* Upload Missing Documents  
* Property Registration Submission  
* Inspection Preparation

High-priority deadlines appear first.

### Section 6 — Recent System Announcements

Display organization-wide and RERA announcements.

Examples

* Planned platform maintenance  
* New registration guidelines  
* Updated document requirements  
* Regulatory policy changes  
* Service availability updates

Each announcement displays:

* Announcement Title  
* Published Date  
* Category  
* Read More

### Empty State

#### **Message**

> You're all caught up\! There are no new notifications requiring your attention.

Primary Button

* Go to Dashboard

Secondary Button

* View Projects

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Notifications

├── View Notification

├── Open Related Project

├── Open Property Registration

├── Open Application

├── Open Document

├── Mark as Read

└── Configure Notification Settings

### Notes

* This is the **central operational notification hub** for the **Project Registration Officer**.  
* Notifications should automatically prioritize **Critical** and **High Priority** items, followed by approaching deadlines.  
* Selecting a notification should navigate directly to the related **Project**, **Property Registration**, **Application**, or **Document**.  
* Notifications should update in real time whenever RERA requests information, changes an application status, verifies documents, schedules inspections, or publishes important announcements.  
* Read/unread status should synchronize across all devices for the logged-in user.

### Sales & Disclosure Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Notifications**  
* **Other Menu Items:**  
  * Dashboard  
  * Sales & Disclosures  
  * Applications  
  * Documents  
  * Reports  
  * **Notifications (Active)**  
  * Help & Support

### Top Bar Status

**Title:** Notifications

**Subtitle:** Stay informed about sales disclosures, buyer verification, regulatory reviews, and compliance deadlines.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Mark All as Read  
* Notification Settings

### Purpose

Provide the Sales & Disclosure Officer with a centralized notification center for monitoring every operational event related to property sales, disclosure applications, buyer documentation, communications from RERA, and approaching compliance deadlines. The page prioritizes actionable notifications so officers can quickly respond and keep sales disclosures compliant.

### Layout

Top Bar  
↓  
Notification Summary Cards  
↓  
Filters  
↓  
Priority Notifications  
↓  
Notifications List  
↓  
Upcoming Deadlines  
↓  
Recent System Announcements

### Section 1 — Notification Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Notifications | All notifications |
| Unread | Notifications not yet viewed |
| High Priority | Urgent notifications |
| RERA Requests | Requests requiring action |
| Returned Disclosures | Disclosures returned for correction |
| Buyer Verification | Buyer information requiring attention |
| Upcoming Deadlines | Due within the next 7 days |
| Completed Today | Notifications resolved today |

Selecting a KPI filters the notification list.

### Section 2 — Filters

Allow officers to quickly locate specific notifications.

#### **Components**

* Search Notifications  
* Notification Type  
* Priority  
* Status (Read / Unread)  
* Related Module  
* Date Range  
* Reset Filters

#### **Notification Types**

* Property Sale  
* Sales Disclosure  
* Buyer Verification  
* Buyer Documents  
* Regulatory Application  
* Deadline Reminder  
* RERA Announcement  
* System Notification

#### **Priority Levels**

* Critical  
* High  
* Medium  
* Low

### Section 3 — Priority Notifications

Display notifications requiring immediate attention.

Examples

* Sales disclosure returned by RERA  
* Additional buyer information requested  
* Buyer identification rejected  
* Proof of payment missing  
* Disclosure submission deadline approaching  
* Compliance review scheduled  
* Identity verification failed  
* Supporting document expired

Each notification displays:

* Priority Indicator  
* Notification Title  
* Related Sale / Disclosure  
* Due Date  
* Time Received

#### **Primary Action**

* Resolve Now

#### **Secondary Action**

* View Details

### Section 4 — Notifications List

Chronological notification list.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Notification | Title |
| Module | Related module |
| Reference | Sale / Disclosure / Application |
| Date & Time | Received |
| Status | Read / Unread |
| Priority | Priority level |
| Action | Open |

#### **Notification Actions**

* View Details  
* Mark as Read  
* Mark as Unread  
* Archive *(where permitted)*

Selecting a notification opens the related Sale, Disclosure, Application, or Document.

### Section 5 — Upcoming Deadlines

Display all upcoming sales compliance deadlines.

#### **Columns**

| Deadline | Related Record | Due Date | Days Remaining | Action |
| :---: | :---: | :---: | :---: | :---: |

Examples

* Submit Sales Disclosure  
* Respond to RERA Query  
* Upload Buyer Identification  
* Submit Proof of Payment  
* Correct Returned Disclosure  
* Complete Buyer Verification

Critical deadlines appear first.

### Section 6 — Recent System Announcements

Display organization-wide and RERA announcements.

Examples

* Updated sales disclosure requirements  
* Buyer identity verification policy changes  
* New accepted document formats  
* Planned platform maintenance  
* Disclosure processing improvements  
* Regulatory guideline updates

Each announcement displays:

* Announcement Title  
* Published Date  
* Category  
* Read More

### Empty State

#### **Message**

> You're all caught up\! There are no new notifications requiring your attention.

**Primary Button**

* Go to Dashboard

**Secondary Button**

* View Sales & Disclosures

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Notifications

├── View Notification

├── Open Sale Record

├── Open Sales Disclosure

├── Open Application

├── Open Document

├── Mark as Read

└── Configure Notification Settings

### Notes

* This is the **central operational notification hub** for the **Sales & Disclosure Officer**.  
* Notifications automatically prioritize **Critical** and **High Priority** items, followed by approaching regulatory deadlines.  
* Selecting a notification should navigate directly to the related **Sale Record, Sales Disclosure, Application, or Document**, allowing the officer to resolve issues with minimal navigation.  
* Notifications should be grouped by **Today**, **Yesterday**, **Earlier This Week**, and **Earlier** to improve readability.  
* Badge counters should update in real time as notifications are received or resolved.

### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Notifications**  
* **Other Menu Items:**  
  * Dashboard  
  * Escrow Management  
  * Applications  
  * Documents  
  * Reports  
  * **Notifications (Active)**  
  * Help & Support

### Top Bar Status

**Title:** Notifications

**Subtitle:** Stay informed about escrow activities, fund releases, milestone verification, and regulatory updates.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Mark All as Read  
* Notification Settings

### Purpose

Provide the Escrow Liaison with a centralized notification center for monitoring escrow account activities, fund release requests, milestone verification updates, communications from RERA and financial institutions, and approaching compliance deadlines. The page prioritizes notifications that require operational action.

### Layout

Top Bar  
↓  
Notification Summary Cards  
↓  
Filters  
↓  
Priority Notifications  
↓  
Notifications List  
↓  
Upcoming Deadlines  
↓  
Recent System Announcements

### Section 1 — Notification Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Notifications | All notifications |
| Unread | Notifications not yet viewed |
| High Priority | Urgent notifications |
| RERA Requests | Requests requiring action |
| Financial Institution Requests | Notifications from banks |
| Returned Fund Releases | Fund release requests returned for correction |
| Upcoming Deadlines | Due within the next 7 days |
| Completed Today | Notifications resolved today |

Selecting a KPI filters the notification list.

### Section 2 — Filters

Allow users to quickly locate specific notifications.

#### **Components**

* Search Notifications  
* Notification Type  
* Priority  
* Status (Read / Unread)  
* Related Module  
* Financial Institution  
* Date Range  
* Reset Filters

#### **Notification Types**

* Escrow Account  
* Fund Release  
* Milestone Verification  
* Document Verification  
* Financial Institution Request  
* RERA Request  
* Deadline Reminder  
* System Notification

#### **Priority Levels**

* Critical  
* High  
* Medium  
* Low

### Section 3 — Priority Notifications

Display notifications requiring immediate attention.

#### **Examples**

* Fund release returned by RERA  
* Bank requested additional documents  
* Engineer certificate missing  
* Quantity Surveyor report rejected  
* Milestone verification pending  
* Escrow account nearing compliance deadline  
* Construction inspection scheduled  
* Financial institution approval received

Each notification displays:

* Priority Indicator  
* Notification Title  
* Related Escrow Account / Fund Release  
* Due Date  
* Time Received

#### **Primary Action**

* Resolve Now

#### **Secondary Action**

* View Details

### Section 4 — Notifications List

Chronological notification list.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Notification | Title |
| Module | Related module |
| Reference | Escrow / Fund Release / Application |
| Date & Time | Received |
| Status | Read / Unread |
| Priority | Priority level |
| Action | Open |

#### **Notification Actions**

* View Details  
* Mark as Read  
* Mark as Unread  
* Archive *(where permitted)*

Selecting a notification opens the related Escrow Account, Fund Release Request, Application, or Document.

### Section 5 — Upcoming Deadlines

Display all upcoming escrow and compliance deadlines.

#### **Columns**

| Deadline | Related Record | Due Date | Days Remaining | Action |
| ----- | ----- | ----- | ----- | ----- |
| Submit Fund Release | FR-001245 | 05 Aug 2026 | 3 Days | Continue |
| Respond to RERA Query | APP-000874 | 06 Aug 2026 | 4 Days | Respond |
| Upload Engineer Certificate | ESC-000351 | 07 Aug 2026 | 5 Days | Upload |
| Bank Clarification | ESC-000218 | 08 Aug 2026 | 6 Days | Respond |
| Milestone Verification | Project A | 09 Aug 2026 | 7 Days | View |

Critical deadlines appear first.

### Section 6 — Recent System Announcements

Display organization-wide and RERA announcements.

#### **Examples**

* Planned platform maintenance  
* Updated escrow compliance requirements  
* New fund release verification process  
* Financial institution integration updates  
* Regulatory policy changes  
* Scheduled maintenance notice

Each announcement displays:

* Title  
* Category  
* Published Date  
* Summary

#### **Actions**

* Read More  
* View Announcement

### Empty State

**Illustration**

Notification Bell

**Message**

> You're all caught up. No new notifications at the moment.

**Primary Button**

* Go to Dashboard

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Notifications  
    ↓  
Review Notification Summary Cards  
    ↓  
Apply Filters  
    ↓  
Open Priority Notification  
    ↓  
Review Notification Details  
    ↓  
Navigate to Related Record  
    ↓  
Complete Required Action  
    ↓  
Mark Notification as Read

### Notes

* Notifications are generated automatically from escrow accounts, fund release requests, milestone verification, document verification, RERA activities, and financial institution interactions.  
* Critical notifications remain pinned until resolved or acknowledged.  
* Users can configure notification preferences by module and priority.  
* Notifications link directly to the relevant operational record for faster action.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations). The Escrow Liaison's is a single linear arrow diagram rooted at Notifications itself rather than the Dashboard-rooted tree diagrams used by the other three roles.

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
