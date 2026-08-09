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

# Screen: Help & Support

**Roles:** Principal · Registration Officer · Sales & Disclosure Officer · Escrow Liaison

A support center scoped to the viewing role, combining a knowledge base, support tickets, and contact channels. The Registration Officer and Sales & Disclosure Officer share close to the same structure (a role-specific Knowledge Base, Support Tickets, System Status, a "Contact RERA Support" block, and Feedback & Suggestions). The Principal's is close but uses "Help Center" instead of "Knowledge Base" as the section name. The Escrow Liaison's is structurally the most different of the four — see [Role Variations](#role-variations).

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Help & Support**
* **Top Bar Title:** Help & Support
* **Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

Which sidebar menu items are visible, the subtitle, and the layout diagram differ by role — see [Role Variations](#role-variations). The layout diagram is identical for the Registration Officer and Sales & Disclosure Officer (Support Summary Cards → Quick Actions → Knowledge Base → Support Tickets → System Status → Contact RERA Support → Feedback & Suggestions). The Principal's is the same shape but names the knowledge-base step "Help Center". The Escrow Liaison's differs substantially in both step names and count (Support Summary Cards → Search Knowledge Base → Quick Help Categories → Knowledge Base Articles → Support Tickets → Contact Support → **Training Resources**), and has no System Status or Feedback & Suggestions step at all.

## Sections

Every section is role-specific — see [Role Variations](#role-variations). Notably: only the Escrow Liaison's version has a **Training Resources** section and a **Quick Help Categories** section; only the Principal, Registration Officer, and Sales & Disclosure Officer versions have a **System Status** section and a **Feedback & Suggestions** section, and structure regulatory contact as "RERA Support Center / Live Chat / Emergency Regulatory Support" — the Escrow Liaison's "Contact Support" section instead lists a flat set of contact options with no equivalent breakdown.

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations). Only the Escrow Liaison's version specifies an **Illustration** (a Support Agent) alongside the message, the same pattern seen on that role's Notifications screen; the other three roles specify text only.

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Help & Support**  
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
  * Notifications  
  * **Help & Support (Active)**

### Top Bar Status

**Title:** Help & Support

**Subtitle:** Access help resources, contact RERA support, and track your organization's support requests.

**Search Bar:** Search anything...

**Page Actions (Right Side):**

* Create Support Ticket  
* Contact Support

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a centralized support center for accessing documentation, reporting issues, requesting assistance, tracking support requests, and staying informed about platform availability and known issues.

### Layout

Top Bar  
↓  
Support Summary Cards  
↓  
Quick Actions  
↓  
Help Center  
↓  
Support Tickets  
↓  
System Status  
↓  
Contact Support  
↓  
Feedback & Suggestions

### Section 1 — Support Summary Cards

Display six KPI cards.

| KPI | Description |
| ----- | ----- |
| Open Tickets | Active support requests |
| Pending Response | Awaiting RERA response |
| Resolved Tickets | Successfully closed tickets |
| Knowledge Articles | Available help articles |
| System Status | Overall platform health |
| Unread Support Messages | New responses from support |

Selecting a KPI navigates to the relevant section.

### Section 2 — Quick Actions

Display shortcut cards.

#### **Available Actions**

* Create Support Ticket  
* Browse Help Center  
* View User Guides  
* Frequently Asked Questions  
* Contact RERA Support  
* Check System Status

Each card opens its respective section.

### Section 3 — Help Center

Knowledge base organized into categories.

#### **Categories**

##### **Getting Started**

* Account Setup  
* Company Registration  
* User Management

##### **Project Management**

* Register a Project  
* Update Project Information  
* Project Approval Process

##### **Property Registration**

* Register Properties  
* Required Documents  
* Registration Status

##### **Sales & Disclosure**

* Record Property Sale  
* Submit Disclosure  
* Buyer Information Requirements

##### **Escrow Management**

* Open Escrow Account  
* Milestone Fund Release  
* Escrow Compliance

##### **Applications**

* Submit Applications  
* Track Application Status  
* Respond to Queries

##### **Documents**

* Upload Documents  
* Document Verification  
* Version Management

##### **Reports**

* Generate Reports  
* Export Reports  
* Schedule Reports

Each article displays:

* Title  
* Category  
* Last Updated  
* Estimated Reading Time

Action

* Open Article

### Section 4 — Support Tickets

Displays organization support history.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Ticket ID | Support reference |
| Subject | Issue title |
| Category | Support category |
| Priority | Critical / High / Medium / Low |
| Created On | Date submitted |
| Status | Current status |
| Assigned Agent | Support representative |
| Action | View Ticket |

### Ticket Status

* Open  
* In Progress  
* Waiting for Customer  
* Escalated  
* Resolved  
* Closed

### Section 5 — System Status

Displays the health of platform services.

#### **Services**

| Service | Status |
| ----- | ----- |
| RERA Portal | Operational |
| Project Registration | Operational |
| Property Registration | Operational |
| Sales & Disclosure | Operational |
| Escrow Services | Operational |
| Document Management | Operational |
| Reports | Operational |
| Notification Service | Operational |

Possible status indicators:

* Operational  
* Maintenance  
* Partial Outage  
* Major Outage

A banner appears when maintenance or incidents are active.

### Section 6 — Contact Support

Display available communication channels.

#### **Channels**

##### **RERA Support Center**

* Phone Number  
* Email Address  
* Business Hours

##### **Live Chat *(If Enabled)***

Displays:

* Agent Availability  
* Estimated Wait Time

Button

* Start Chat

##### **Emergency Regulatory Contact**

For urgent regulatory issues.

Display:

* Contact Information  
* Availability

### Section 7 — Feedback & Suggestions

Allow executives to submit platform improvement ideas.

#### **Components**

* Feedback Category  
* Subject  
* Description  
* Attachment *(Optional)*

Buttons

* Submit Feedback  
* Save Draft

### Empty State

If no support tickets exist:

**Message**

> You haven't created any support tickets yet. If you need assistance, our support team is here to help.

Primary Button

* Create Support Ticket

Secondary Button

* Browse Help Articles

### Reused Components

* Left Sidebar  
* Top Bar  
* KPI Cards  
* Quick Action Cards  
* Search Bar  
* Data Tables  
* Knowledge Base Cards  
* Status Badges  
* System Status Widget  
* Buttons  
* Empty State

### User Flow

Dashboard  
↓  
Help & Support

├── Browse Help Articles

├── Create Support Ticket

├── View Ticket

├── Contact Support

├── Check System Status

└── Submit Feedback

### Notes

* This is the **central support portal** for the **Developer Principal / Director**.  
* Users can access documentation, contact RERA, monitor platform health, and manage support requests from a single interface.  
* Ticket visibility is organization-wide for authorized executive users, allowing leadership to monitor unresolved issues affecting operations.  
* Support interactions should be linked to related modules (Projects, Applications, Escrow, etc.) to provide context and improve resolution time.  
* The System Status section should display real-time service availability and planned maintenance announcements.


### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Help & Support**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * Applications  
  * Documents  
  * Reports  
  * Notifications  
  * **Help & Support (Active)**

### Top Bar Status

**Title:** Help & Support

**Subtitle:** Access registration guidance, contact RERA support, and track operational support requests.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Create Support Ticket  
* Contact RERA Support

### Purpose

Provide the Project Registration Officer with a centralized operational support workspace for resolving issues encountered during project registrations, property registrations, document submissions, and regulatory applications. The page also serves as the primary knowledge base for registration procedures, allowing officers to quickly find guidance and communicate with RERA support.

### Layout

Top Bar  
↓  
Support Summary Cards  
↓  
Quick Actions  
↓  
Knowledge Base  
↓  
Support Tickets  
↓  
System Status  
↓  
Contact RERA Support  
↓  
Feedback & Suggestions

### Section 1 — Support Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Open Tickets | Active support requests |
| Awaiting RERA Response | Tickets pending response |
| Waiting for My Response | Tickets requiring officer action |
| Resolved Tickets | Successfully resolved requests |
| Knowledge Articles | Available help resources |
| FAQs | Frequently asked questions |
| Platform Status | Overall service availability |
| Unread Support Messages | New replies from support |

Selecting a KPI filters the relevant section.

### Section 2 — Quick Actions

Provide shortcuts to common support activities.

#### **Available Actions**

* Create Support Ticket  
* Browse Knowledge Base  
* View Registration Guides  
* Frequently Asked Questions  
* Contact RERA Support  
* Check Platform Status

Each action opens the appropriate section.

### Section 3 — Knowledge Base

Organized collection of operational guidance.

#### **Categories**

##### **Project Registration**

* Register a New Project  
* Required Documents  
* Project Validation Rules  
* Common Registration Errors

##### **Property Registration**

* Register a Property  
* Unit Registration Guide  
* Property Validation Rules  
* Registration Certificate

##### **Applications**

* Submit an Application  
* Track Application Status  
* Respond to RERA Queries  
* Resubmitting Returned Applications

##### **Document Management**

* Upload Documents  
* Replace Documents  
* Document Verification  
* Accepted File Formats

##### **Reports**

* Generate Reports  
* Export Reports  
* Understanding Registration Reports

##### **Regulatory Guidance**

* RERA Registration Process  
* Compliance Requirements  
* Inspection Procedures  
* Regulatory Timelines

Each article displays:

* Title  
* Category  
* Last Updated  
* Estimated Reading Time

Action

* Open Article

### Section 4 — Support Tickets

Display all support requests created by the organization or assigned to the officer.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Ticket ID | Support reference |
| Subject | Issue summary |
| Category | Support type |
| Related Module | Projects, Applications, Documents, etc. |
| Priority | Critical / High / Medium / Low |
| Created On | Ticket creation date |
| Status | Current progress |
| Assigned Agent | RERA support representative |
| Action | View Ticket |

#### **Ticket Status**

* Draft  
* Open  
* In Progress  
* Waiting for Customer  
* Escalated  
* Resolved  
* Closed

### Section 5 — System Status

Display the availability of major platform services.

| Service | Status |
| ----- | ----- |
| Project Registration | Operational |
| Property Registration | Operational |
| Applications | Operational |
| Document Management | Operational |
| Reports | Operational |
| Notifications | Operational |
| Authentication | Operational |

Possible status indicators:

* Operational  
* Scheduled Maintenance  
* Partial Outage  
* Major Outage

Maintenance announcements appear at the top of this section.

### Section 6 — Contact RERA Support

Display available communication channels.

#### **RERA Support Center**

* Support Phone  
* Support Email  
* Business Hours  
* Average Response Time

#### **Live Chat *(If Available)***

Display:

* Agent Availability  
* Estimated Wait Time

Button

* Start Live Chat

#### **Emergency Regulatory Support**

For urgent registration or regulatory issues.

Display:

* Contact Number  
* Availability  
* Supported Issues

### Section 7 — Feedback & Suggestions

Allow officers to submit platform improvement ideas.

#### **Components**

* Feedback Category  
* Subject  
* Description  
* Related Module  
* Attachment *(Optional)*

Buttons

* Submit Feedback  
* Save Draft

### Empty State

#### **Message**

> You haven't created any support requests yet. If you encounter any issues during project registration or application processing, RERA Support is ready to assist you.

Primary Button

* Create Support Ticket

Secondary Button

* Browse Knowledge Base

### Reused Components

* Left Sidebar  
* Top Bar (Background \+ HorizontalBorder)  
* KPI Cards  
* Quick Action Cards  
* Search Bar  
* Data Tables  
* Knowledge Base Cards  
* Status Badges  
* System Status Widget  
* Buttons  
* Empty State

### User Flow

Dashboard  
↓  
Help & Support

├── Browse Knowledge Base

├── Open Help Article

├── Create Support Ticket

├── View Ticket

├── Contact RERA Support

├── Check Platform Status

└── Submit Feedback

### Notes

* This is the **operational support center** for the **Project Registration Officer**.  
* The knowledge base should focus on **project registrations, property registrations, applications, document management, and regulatory compliance**.  
* Support tickets should allow linking directly to a **Project**, **Property Registration**, **Application**, or **Document** to give RERA support full context.  
* The System Status section should display real-time platform health and planned maintenance notices.  
* Officers should receive notifications whenever a support ticket is updated or requires additional information.


### Sales & Disclosure Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Help & Support**  
* **Other Menu Items:**  
  * Dashboard  
  * Sales & Disclosures  
  * Applications  
  * Documents  
  * Reports  
  * Notifications  
  * **Help & Support (Active)**

### Top Bar Status

**Title:** Help & Support

**Subtitle:** Access sales disclosure guidance, contact RERA support, and track operational support requests.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Create Support Ticket  
* Contact RERA Support

### Purpose

Provide the Sales & Disclosure Officer with a centralized operational support workspace for resolving issues encountered during property sales, sales disclosures, buyer verification, document submissions, and regulatory applications. This page also serves as the primary knowledge base for disclosure procedures, allowing officers to quickly find guidance and communicate with RERA support.

### Layout

Top Bar  
↓  
Support Summary Cards  
↓  
Quick Actions  
↓  
Knowledge Base  
↓  
Support Tickets  
↓  
System Status  
↓  
Contact RERA Support  
↓  
Feedback & Suggestions

### Section 1 — Support Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Open Tickets | Active support requests |
| Awaiting RERA Response | Tickets pending response |
| Waiting for My Response | Tickets requiring officer action |
| Resolved Tickets | Successfully resolved requests |
| Knowledge Articles | Available help resources |
| FAQs | Frequently asked questions |
| Platform Status | Overall service availability |
| Unread Support Messages | New replies from support |

Selecting a KPI filters the relevant section.

### Section 2 — Quick Actions

Provide shortcuts to common support activities.

#### **Available Actions**

* Create Support Ticket  
* Browse Knowledge Base  
* View Sales Disclosure Guides  
* Frequently Asked Questions  
* Contact RERA Support  
* Check Platform Status

Each action opens the appropriate section.

### Section 3 — Knowledge Base

Organized collection of operational guidance.

#### **Sales & Disclosure**

* Record a Property Sale  
* Create a Sales Disclosure  
* Disclosure Validation Rules  
* Common Disclosure Errors

#### **Buyer Management**

* Buyer Information Requirements  
* Identity Verification  
* Corporate Buyer Registration  
* Joint Buyer Registration

#### **Applications**

* Submit a Disclosure Application  
* Track Application Status  
* Respond to RERA Queries  
* Resubmit Returned Applications

#### **Document Management**

* Upload Buyer Documents  
* Replace Documents  
* Document Verification  
* Accepted File Formats

#### **Reports**

* Generate Sales Reports  
* Export Reports  
* Schedule Reports  
* Understanding Compliance Reports

#### **Regulatory Guidance**

* RERA Sales Disclosure Process  
* Buyer Compliance Requirements  
* Payment Documentation  
* Regulatory Timelines

Each article displays:

* Title  
* Category  
* Last Updated  
* Estimated Reading Time

#### **Action**

* Open Article

### Section 4 — Support Tickets

Display all support requests created by the organization or assigned to the officer.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Ticket ID | Support reference |
| Subject | Issue summary |
| Category | Support type |
| Related Module | Sales, Applications, Documents, etc. |
| Priority | Critical / High / Medium / Low |
| Created On | Ticket creation date |
| Status | Current progress |
| Assigned Agent | RERA support representative |
| Action | View Ticket |

#### **Ticket Status**

* Draft  
* Open  
* In Progress  
* Waiting for Customer  
* Escalated  
* Resolved  
* Closed

### Section 5 — System Status

Display the availability of major platform services.

| Service | Status |
| ----- | ----- |
| Sales & Disclosure | Operational |
| Buyer Verification | Operational |
| Applications | Operational |
| Document Management | Operational |
| Reports | Operational |
| Notifications | Operational |
| Authentication | Operational |

Possible status indicators:

* Operational  
* Scheduled Maintenance  
* Partial Outage  
* Major Outage

Maintenance announcements appear at the top of this section.

### Section 6 — Contact RERA Support

Display available communication channels.

#### **RERA Support Center**

* Support Phone  
* Support Email  
* Business Hours  
* Average Response Time

#### **Live Chat *(If Available)***

Display:

* Agent Availability  
* Estimated Wait Time

**Button**

* Start Live Chat

#### **Emergency Regulatory Support**

For urgent sales compliance or disclosure issues.

Display:

* Contact Number  
* Availability  
* Supported Issues

### Section 7 — Feedback & Suggestions

Allow officers to submit platform improvement ideas.

#### **Components**

* Feedback Category  
* Subject  
* Description  
* Related Module  
* Attachment *(Optional)*

**Buttons**

* Submit Feedback  
* Save Draft

### Empty State

#### **Message**

> You haven't created any support requests yet. If you encounter any issues during property sales, buyer verification, or sales disclosure processing, RERA Support is ready to assist you.

**Primary Button**

* Create Support Ticket

**Secondary Button**

* Browse Knowledge Base

### Reused Components

* Left Sidebar  
* Top Bar (Background \+ HorizontalBorder)  
* KPI Cards  
* Quick Action Cards  
* Search Bar  
* Data Tables  
* Knowledge Base Cards  
* Status Badges  
* System Status Widget  
* Buttons  
* Empty State

### User Flow

Dashboard  
↓  
Help & Support

├── Browse Knowledge Base

├── Open Help Article

├── Create Support Ticket

├── View Ticket

├── Contact RERA Support

├── Check Platform Status

└── Submit Feedback

### Notes

* This is the **operational support center** for the **Sales & Disclosure Officer**.  
* The knowledge base focuses on **property sales, buyer verification, sales disclosures, supporting documents, disclosure applications, and regulatory compliance**.  
* Support tickets should be linked to the relevant **Sale, Sales Disclosure, Buyer Record, Application, or Document** where applicable to give RERA support full context.  
* Critical regulatory issues (such as failed disclosure submissions or buyer verification failures) should be surfaced with high-priority indicators and recommended next steps.  
* Officers should be able to continue working while waiting for support responses, except where a regulatory blocker prevents submission.


### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Help & Support**  
* **Other Menu Items:**  
  * Dashboard  
  * Escrow Management  
  * Applications  
  * Documents  
  * Reports  
  * Notifications  
  * **Help & Support (Active)**

### Top Bar Status

**Title:** Help & Support

**Subtitle:** Access user guides, contact support, report issues, and find answers to common escrow management questions.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Contact Support  
* Create Support Ticket

### Purpose

Provide Escrow Liaisons with a centralized support hub where they can access documentation, resolve operational issues, contact RERA support, monitor submitted support requests, and learn how to perform escrow-related activities efficiently.

### Layout

Top Bar  
↓  
Support Summary Cards  
↓  
Search Knowledge Base  
↓  
Quick Help Categories  
↓  
Knowledge Base Articles  
↓  
Support Tickets  
↓  
Contact Support  
↓  
Training Resources

### Section 1 — Support Summary Cards

Display **6 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Open Tickets | Active support requests |
| Resolved Tickets | Closed support requests |
| Knowledge Articles | Available help articles |
| Training Materials | User guides and videos |
| Frequently Asked Questions | FAQ collection |
| System Status | Current platform availability |

### Section 2 — Search Knowledge Base

Allow users to quickly locate support content.

#### **Components**

* Search Help Articles  
* Category Filter  
* Keyword Tags  
* Reset Search

#### **Categories**

* Escrow Management  
* Fund Release  
* Applications  
* Documents  
* Reports  
* Notifications  
* Financial Institutions  
* User Account  
* Security  
* Platform Usage

### Section 3 — Quick Help Categories

Display shortcut cards for the most commonly accessed support topics.

Examples:

* Managing Escrow Accounts  
* Processing Fund Releases  
* Uploading Documents  
* Responding to RERA Requests  
* Financial Institution Coordination  
* Report Generation  
* Account Settings  
* Platform Troubleshooting

Each card includes:

* Category Icon  
* Category Name  
* Number of Articles  
* Open Category

### Section 4 — Knowledge Base Articles

Display searchable documentation.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Article | Help topic |
| Category | Related module |
| Last Updated | Latest revision |
| Popularity | Frequently viewed |
| Action | Open |

Article Actions

* Read Article  
* Download PDF  
* Share Link  
* Print

### Section 5 — Support Tickets

Display submitted support requests.

#### **Columns**

| Ticket ID | Subject | Category | Priority | Status | Updated | Action |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |

#### **Ticket Status**

* Open  
* In Progress  
* Waiting for User  
* Resolved  
* Closed

#### **Ticket Actions**

* View Ticket  
* Reply  
* Upload Attachment  
* Close Ticket (when allowed)

### Section 6 — Contact Support

Provide multiple support channels.

#### **Contact Options**

* Submit Support Ticket  
* Live Chat (Business Hours)  
* Email Support  
* Phone Support  
* Technical Support  
* Regulatory Support

Display:

* Support Availability  
* Expected Response Time  
* Emergency Contact Information

### Section 7 — Training Resources

Provide onboarding and learning materials.

#### **Resources**

* User Manuals  
* Quick Start Guides  
* Video Tutorials  
* Process Walkthroughs  
* Release Notes  
* Platform Updates  
* Best Practices  
* Frequently Asked Questions

Each resource includes:

* Title  
* Resource Type  
* Duration or Page Count  
* Last Updated  
* Open Resource

### Empty State

**Illustration**

Support Agent

**Message**

> No support tickets have been submitted yet.

**Primary Button**

* Create Support Ticket

### Reused Components

* Developer Operational Sidebar  
* Background \+ HorizontalBorder  
* KPI Cards  
* Search Bar  
* Filter Panel  
* Knowledge Base List  
* Ticket Table  
* Contact Cards  
* Empty State  
* Pagination

### User Flow

Help & Support  
    ↓  
Search Knowledge Base  
    ↓  
Open Help Article  
    ↓  
Review Solution  
    ↓  
Issue Resolved?  
    ↓  
Yes → Return to Work  
    ↓  
No  
    ↓  
Create Support Ticket  
    ↓  
Track Ticket Status

### Notes

* Help articles are searchable by keyword and module.  
* Support tickets can include screenshots and supporting documents.  
* Frequently accessed articles appear higher in search results.  
* Users can track ticket progress and receive notifications when support staff respond.  
* System status is displayed to inform users of maintenance windows or service disruptions.


## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations). The Escrow Liaison's is a single linear arrow diagram rooted at Help & Support itself, including a Yes/No decision branch ("Issue Resolved?"), rather than the Dashboard-rooted tree diagrams used by the other three roles.

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
