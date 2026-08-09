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

# Screen: Reports

**Roles:** Principal · Registration Officer · Sales & Disclosure Officer · Escrow Liaison

A reporting hub scoped to the viewing role. The Developer Principal / Director gets an executive business-intelligence view across the whole organization; the three operational roles (Registration Officer, Sales & Disclosure Officer, Escrow Liaison) each get an operational reporting workspace scoped to their own domain (registrations, sales disclosures, or escrow, respectively).

## Purpose

Purpose differs by role — see [Role Variations](#role-variations).

## Layout

* **Visible Sidebar:** Developer Operational Sidebar
* **Active Menu:** **Reports**
* **Top Bar Title:** Reports
* **Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

Which sidebar menu items are visible, the subtitle, top-bar page actions, and the layout diagram differ by role — see [Role Variations](#role-variations). The layout diagram is identical for the Registration Officer, Sales & Disclosure Officer, and Escrow Liaison (ending at Recent Generated Reports → **Pending Operational Insights**); the Principal's ends instead with two separate steps, **Scheduled Reports** then **Executive Insights**.

## Sections

Every section (Report Summary Cards, Report Categories, Report Filters, Saved Reports, Report Templates, Recent Generated Reports, and the closing insights/scheduling section) is role-specific — see [Role Variations](#role-variations).

## Empty State

Message and actions differ by role — see [Role Variations](#role-variations). The Escrow Liaison's version omits the "Message" sub-heading used by the other three roles, presenting the message text directly under "Empty State"; this is preserved as-is.

## Reused Components

Differs by role — see [Role Variations](#role-variations).

## Role Variations

### Developer Principal / Director

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Reports**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * Sales & Disclosures  
  * Escrow Management  
  * Applications  
  * Documents  
  * **Reports (Active)**  
  * Company Profile  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Reports

**Subtitle:** Generate executive reports and analyze organizational performance across projects, compliance, sales, and financial activities.

**Search Bar:** Search anything...

**Page Actions (Right Side):**

* Generate Report  
* Schedule Report  
* Export Dashboard

The page uses the shared **Background \+ HorizontalBorder** component.

### Purpose

Provide the Developer Principal / Director with a centralized reporting and business intelligence hub that consolidates operational, financial, regulatory, and compliance data into actionable insights for executive decision-making.

### Layout

Top Bar  
↓  
Report Summary Cards  
↓  
Report Categories  
↓  
Filters  
↓  
Saved Reports  
↓  
Report Templates  
↓  
Recent Generated Reports  
↓  
Scheduled Reports  
↓  
Executive Insights

### Section 1 — Report Summary Cards

Display eight KPI cards.

| KPI | Description |
| ----- | ----- |
| Total Reports | Available reports |
| Generated Today | Reports generated today |
| Scheduled Reports | Active report schedules |
| Custom Reports | User-created reports |
| Compliance Reports | Regulatory reports |
| Financial Reports | Financial & escrow reports |
| Operational Reports | Project & sales reports |
| Executive Dashboards | Interactive dashboards |

### Section 2 — Report Categories

Display clickable report category cards.

#### **Available Categories**

##### **Project Reports**

* Project Progress  
* Project Completion  
* Construction Milestones  
* Development Performance

##### **Property Reports**

* Property Registrations  
* Registration Status  
* Property Inventory  
* Property Availability

##### **Sales Reports**

* Sales Performance  
* Buyer Statistics  
* Sales Trends  
* Disclosure Compliance

##### **Escrow Reports**

* Escrow Balances  
* Fund Releases  
* Milestone Progress  
* Financial Institution Summary

##### **Regulatory Reports**

* Applications  
* Approval Performance  
* Processing Time  
* Compliance Overview

##### **Financial Reports**

* Revenue  
* Escrow Funds  
* Sales Value  
* Payment Summary

##### **Document Reports**

* Document Verification  
* Expiring Documents  
* Missing Documents  
* Repository Summary

##### **Executive Reports**

* Organization Performance  
* KPI Dashboard  
* Risk Summary  
* Executive Summary

### Section 3 — Report Filters

Users can customize report generation.

#### **Filters**

* Report Category  
* Project  
* Development  
* Property  
* Application Type  
* Status  
* Financial Institution  
* Date Range  
* Report Format

### Export Formats

* PDF  
* Excel  
* CSV

### Section 4 — Saved Reports

Table.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Report Name | Saved report |
| Category | Report category |
| Created By | User |
| Last Generated | Date |
| Schedule | Manual / Scheduled |
| Action | Open |

### Row Actions

* Open  
* Generate Again  
* Download

### Section 5 — Report Templates

Pre-built report library.

Examples

* Executive Monthly Report  
* Project Performance Report  
* Property Registration Report  
* Sales Performance Report  
* Escrow Summary  
* Compliance Dashboard  
* Financial Overview  
* Regulatory Activity Report

Each template displays:

* Template Name  
* Description  
* Estimated Generation Time

Action

* Generate

### Section 6 — Recent Generated Reports

Table.

#### **Columns**

* Report Name  
* Category  
* Generated By  
* Generated On  
* Format  
* Status  
* Action

Status

* Completed  
* Processing  
* Failed  
* Expired

### Section 7 — Scheduled Reports

Display scheduled reports.

#### **Columns**

* Report Name  
* Frequency  
* Next Run  
* Delivery Method  
* Status  
* Action

Frequency

* Daily  
* Weekly  
* Monthly  
* Quarterly

Delivery

* Platform  
* Email

### Section 8 — Executive Insights

A dashboard-style section containing interactive analytics.

#### **Widgets**

##### **Organization Performance**

* Projects by Status  
* Active Property Registrations  
* Sales Performance Trend

##### **Financial Overview**

* Escrow Balance Trend  
* Revenue Trend  
* Monthly Sales Value

##### **Regulatory Performance**

* Application Approval Rate  
* Average Processing Time  
* Compliance Score

##### **Risk Indicators**

* Overdue Applications  
* Delayed Projects  
* Pending Escrow Releases  
* Expiring Licenses

Each widget includes a **View Detailed Report** action.

### Empty State

#### **Message**

> No reports have been generated yet.

Primary Button

* Generate Your First Report

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Reports

├── Select Report Category

│

├── Apply Filters

│

├── Generate Report

│

├── Download Report

│

└── Schedule Report

### Notes

* This is the **executive reporting center** for the **Developer Principal / Director**.  
* Reports are generated using real-time platform data across all modules.  
* Users can create ad hoc reports, reuse saved templates, or schedule recurring reports.  
* Access to report data respects the user's role and organizational permissions.  
* Generated reports are read-only snapshots and do not modify operational records.

### Project Registration Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Reports**  
* **Other Menu Items:**  
  * Dashboard  
  * Projects  
  * Property Registrations  
  * Applications  
  * Documents  
  * **Reports (Active)**  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Reports

**Subtitle:** Generate operational reports and monitor registration performance across projects, properties, applications, and documents.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Generate Report  
* Export Report  
* Schedule Report

### Purpose

Provide the Project Registration Officer with an operational reporting workspace to analyze registration activities, monitor application progress, track document completeness, identify pending tasks, and generate reports for internal review and regulatory follow-up.

Unlike the Developer Principal's reporting dashboard, this page focuses on operational execution rather than executive analytics.

### Layout

Top Bar  
↓  
Report Summary Cards  
↓  
Report Categories  
↓  
Filters  
↓  
Saved Reports  
↓  
Report Templates  
↓  
Recent Generated Reports  
↓  
Pending Operational Insights

### Section 1 — Report Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Reports | Reports available |
| Reports Generated Today | Reports created today |
| Scheduled Reports | Active scheduled reports |
| Registration Reports | Project & property registration reports |
| Application Reports | Regulatory application reports |
| Document Reports | Document verification reports |
| Pending Task Reports | Outstanding operational tasks |
| Custom Reports | User-created reports |

Selecting a KPI filters the available reports.

### Section 2 — Report Categories

Display report category cards.

#### **Project Reports**

* Project Registration Status  
* Project Approval Progress  
* Returned Projects  
* Registration Timeline

#### **Property Reports**

* Property Registration Status  
* Registration Progress  
* Approved Properties  
* Returned Registrations

#### **Application Reports**

* Submitted Applications  
* Pending Reviews  
* Returned Applications  
* Approval Timeline

#### **Document Reports**

* Missing Documents  
* Pending Verification  
* Returned Documents  
* Expiring Documents

#### **Operational Reports**

* Officer Workload  
* Due This Week  
* Outstanding Tasks  
* Submission History

#### **Compliance Reports**

* Registration Compliance  
* Validation Errors  
* RERA Query Response Time  
* Regulatory Performance

### Section 3 — Report Filters

Allow officers to customize reports.

#### **Filters**

* Report Category  
* Project  
* Property  
* Application Type  
* Registration Status  
* Document Category  
* Date Range  
* Output Format

#### **Export Formats**

* PDF  
* Excel  
* CSV

### Section 4 — Saved Reports

Table showing saved reports.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Report Name | Saved report |
| Category | Report type |
| Created By | User |
| Last Generated | Date |
| Schedule | Manual / Scheduled |
| Action | Open |

#### **Row Actions**

* Open  
* Generate Again  
* Download  
* Edit Schedule

### Section 5 — Report Templates

Predefined report library.

Examples

* Weekly Registration Summary  
* Pending Applications Report  
* Returned Applications Report  
* Property Registration Report  
* Missing Documents Report  
* Document Verification Report  
* Monthly Operational Summary  
* RERA Response Report

Each template displays:

* Template Name  
* Description  
* Estimated Generation Time

Action

* Generate

### Section 6 — Recent Generated Reports

Table displaying recently generated reports.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Report Name | Report title |
| Category | Report category |
| Generated By | User |
| Generated On | Date & Time |
| Format | PDF / Excel / CSV |
| Status | Processing status |
| Action | Download |

#### **Status**

See [status-badges.md](../status-badges.md#report-generation-status).

### Section 7 — Pending Operational Insights

Operational dashboard highlighting items requiring attention.

#### **Registration Performance**

* Draft Projects Awaiting Submission  
* Draft Property Registrations  
* Registrations Returned by RERA  
* Average Approval Time

#### **Application Performance**

* Pending Applications  
* Information Requested  
* Applications Near Deadline  
* Average Response Time

#### **Document Performance**

* Missing Required Documents  
* Returned Documents  
* Expiring Documents  
* Verification Success Rate

#### **Workload Summary**

* Open Tasks  
* Tasks Due Today  
* Tasks Due This Week  
* Completed This Month

Each widget includes a **View Details** action.

### Empty State

#### **Message**

> No reports have been generated yet.

Primary Button

* Generate First Report

Secondary Button

* Browse Report Templates

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Reports

├── Select Report Template

├── Apply Filters

├── Generate Report

├── Export Report

├── Schedule Report

└── Download Report

### Notes

* This is the **primary operational reporting workspace** for the **Project Registration Officer**.  
* Reports focus on **registrations, applications, documents, and operational workload** rather than executive business metrics.  
* Officers can generate ad hoc reports, reuse saved templates, or schedule recurring reports for operational monitoring.  
* Reports should help identify bottlenecks such as returned applications, missing documents, pending validations, and approaching regulatory deadlines.  
* Generated reports are read-only snapshots and do not modify operational records.

### Sales & Disclosure Officer

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Reports**  
* **Other Menu Items:**  
  * Dashboard  
  * Sales & Disclosures  
  * Applications  
  * Documents  
  * **Reports (Active)**  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Reports

**Subtitle:** Generate operational reports to monitor property sales, disclosure compliance, buyer documentation, and regulatory performance.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Generate Report  
* Export Report  
* Schedule Report

### Purpose

Provide the Sales & Disclosure Officer with an operational reporting workspace to analyze property sales, monitor disclosure progress, track buyer documentation, identify pending compliance actions, and generate reports for internal management and regulatory follow-up.

Unlike the Developer Principal's reporting dashboard, this page focuses on operational execution and disclosure processing rather than executive-level business intelligence.

### Layout

Top Bar  
↓  
Report Summary Cards  
↓  
Report Categories  
↓  
Filters  
↓  
Saved Reports  
↓  
Report Templates  
↓  
Recent Generated Reports  
↓  
Pending Operational Insights

### Section 1 — Report Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Reports | All available reports |
| Reports Generated Today | Reports created today |
| Scheduled Reports | Active scheduled reports |
| Sales Reports | Property sales reports |
| Disclosure Reports | Sales disclosure reports |
| Buyer Document Reports | Buyer document verification reports |
| Compliance Reports | Regulatory compliance reports |
| Custom Reports | User-created reports |

Selecting a KPI filters the available reports.

### Section 2 — Report Categories

Display report category cards.

### **Sales Reports**

* Property Sales Register  
* Sales Performance  
* Sales Value Analysis  
* Monthly Sales Summary

### **Disclosure Reports**

* Disclosure Status Report  
* Submitted Disclosures  
* Returned Disclosures  
* Disclosure Approval Timeline

### **Buyer Reports**

* Buyer Verification Status  
* Buyer Demographics  
* Corporate Buyers  
* Joint Ownership Report

### **Document Reports**

* Buyer Identification Report  
* Missing Documents  
* Pending Verification  
* Returned Documents

### **Compliance Reports**

* Disclosure Compliance Rate  
* Pending Regulatory Actions  
* RERA Query Response Time  
* Validation Error Summary

### **Operational Reports**

* Officer Workload  
* Tasks Due This Week  
* Outstanding Disclosures  
* Submission History

### **Financial Reports**

* Property Sales Value  
* Payment Status Summary  
* Mortgage Distribution  
* Sales by Project

### **Regulatory Reports**

* Approval Performance  
* Average Processing Time  
* Applications by Status  
* Returned Case Analysis

### Section 3 — Report Filters

Allow officers to customize report generation.

#### **Filters**

* Report Category  
* Project  
* Property  
* Buyer  
* Disclosure Status  
* Application Status  
* Payment Status  
* Buyer Type  
* Date Range  
* Output Format

#### **Export Formats**

* PDF  
* Excel  
* CSV

### Section 4 — Saved Reports

Display previously saved reports.

#### **Table**

| Column | Description |
| ----- | ----- |
| Report Name | Saved report |
| Category | Report category |
| Created By | User |
| Last Generated | Date |
| Schedule | Manual / Scheduled |
| Action | Open |

#### **Row Actions**

* Open  
* Generate Again  
* Download  
* Edit Schedule

### Section 5 — Report Templates

Display predefined operational report templates.

Examples

* Weekly Sales Summary  
* Monthly Disclosure Report  
* Pending Buyer Documents  
* Returned Disclosure Report  
* Buyer Verification Report  
* Sales by Project  
* Compliance Performance Report  
* RERA Response Report

Each template displays:

* Template Name  
* Description  
* Estimated Generation Time

#### **Action**

* Generate

### Section 6 — Recent Generated Reports

Display recently generated reports.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Report Name | Report title |
| Category | Report category |
| Generated By | User |
| Generated On | Date & Time |
| Format | PDF / Excel / CSV |
| Status | Processing status |
| Action | Download |

#### **Status**

See [status-badges.md](../status-badges.md#report-generation-status).

### Section 7 — Pending Operational Insights

Operational dashboard highlighting activities requiring attention.

### **Sales Performance**

* Sales Recorded This Month  
* Sales Awaiting Disclosure  
* Average Sale Value  
* High-Value Transactions

### **Disclosure Performance**

* Draft Disclosures  
* Returned Disclosures  
* Under Review  
* Average Approval Time

### **Buyer Documentation**

* Missing Buyer IDs  
* Pending Identity Verification  
* Missing Proof of Payment  
* Expiring Buyer Documents

### **Compliance Performance**

* RERA Queries Awaiting Response  
* Applications Near Deadline  
* Compliance Rate  
* Validation Success Rate

Each widget includes a **View Detailed Report** action.

### Empty State

#### **Message**

> No reports have been generated yet.

**Primary Button**

* Generate First Report

**Secondary Button**

* Browse Report Templates

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Dashboard  
↓  
Reports

├── Select Report Template

├── Apply Filters

├── Generate Report

├── Export Report

├── Schedule Report

├── Open Saved Report

└── Download Report

### Notes

* This is the **primary operational reporting screen** for the **Sales & Disclosure Officer**.  
* Reports focus on **property sales, buyer information, disclosure compliance, supporting documents, payment status, and regulatory performance**.  
* Users can generate reports on demand, save frequently used report configurations, schedule recurring reports, and export them in multiple formats.  
* Operational insight widgets should surface items requiring immediate attention, enabling officers to quickly identify overdue disclosures, missing buyer documents, and pending RERA actions.

### Escrow Liaison

### Sidebar Status

* **Visible Sidebar:** Developer Operational Sidebar  
* **Active Menu:** **Reports**  
* **Other Menu Items:**  
  * Dashboard  
  * Escrow Management  
  * Applications  
  * Documents  
  * **Reports (Active)**  
  * Notifications  
  * Help & Support

### Top Bar Status

**Title:** Reports

**Subtitle:** Generate operational reports for escrow accounts, fund releases, milestone verification, and financial institution activities.

**Search Bar:** Search anything...

The page uses the shared **Background \+ HorizontalBorder** component.

**Page Actions (Right Side):**

* Generate Report  
* Export Report  
* Schedule Report

### Purpose

Provide the Escrow Liaison with an operational reporting workspace to monitor escrow account performance, fund release progress, construction milestone verification, financial institution interactions, and regulatory compliance. The page focuses on operational reporting that supports day-to-day escrow management.

### Layout

Top Bar  
↓  
Report Summary Cards  
↓  
Report Categories  
↓  
Filters  
↓  
Saved Reports  
↓  
Report Templates  
↓  
Recent Generated Reports  
↓  
Pending Operational Insights

### Section 1 — Report Summary Cards

Display **8 KPI cards**.

| KPI | Description |
| ----- | ----- |
| Total Reports | All available reports |
| Reports Generated Today | Reports created today |
| Scheduled Reports | Active scheduled reports |
| Escrow Reports | Escrow account reports |
| Fund Release Reports | Fund release reports |
| Milestone Reports | Construction milestone reports |
| Compliance Reports | Regulatory compliance reports |
| Custom Reports | User-created reports |

Selecting a KPI filters the available reports.

### Section 2 — Report Categories

Display report category cards.

#### **Escrow Reports**

* Escrow Account Summary  
* Active Escrow Accounts  
* Escrow Balance Report  
* Escrow Status Report

#### **Fund Release Reports**

* Fund Release Summary  
* Pending Fund Releases  
* Released Funds  
* Returned Fund Release Requests

#### **Milestone Reports**

* Construction Milestone Progress  
* Milestone Verification Status  
* Pending Milestones  
* Completed Milestones

#### **Financial Institution Reports**

* Financial Institution Performance  
* Escrow Bank Activity  
* Processing Time Analysis  
* Bank Response Summary

#### **Compliance Reports**

* Escrow Compliance Status  
* Outstanding Compliance Issues  
* RERA Query Response Time  
* Regulatory Performance

#### **Document Reports**

* Escrow Document Verification  
* Missing Supporting Documents  
* Returned Documents  
* Expiring Documents

#### **Operational Reports**

* Officer Workload  
* Due This Week  
* Outstanding Escrow Tasks  
* Activity Summary

#### **Financial Reports**

* Escrow Fund Balance  
* Funds Released by Project  
* Release Amount Analysis  
* Remaining Escrow Balance

### Section 3 — Report Filters

Allow users to customize report generation.

#### **Filters**

* Report Category  
* Project  
* Escrow Account  
* Financial Institution  
* Fund Release Status  
* Milestone Status  
* Compliance Status  
* Date Range  
* Output Format

#### **Export Formats**

* PDF  
* Excel  
* CSV

### Section 4 — Saved Reports

Display previously saved reports.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Report Name | Saved report |
| Category | Report category |
| Created By | User |
| Last Generated | Date |
| Schedule | Manual / Scheduled |
| Action | Open |

#### **Row Actions**

* Open  
* Generate Again  
* Download  
* Edit Schedule

### Section 5 — Report Templates

Predefined operational report library.

Examples

* Monthly Escrow Summary  
* Fund Release Status Report  
* Pending Milestone Report  
* Escrow Compliance Report  
* Financial Institution Performance Report  
* Escrow Balance Report  
* Returned Fund Release Report  
* Weekly Operational Summary

Each template displays:

* Template Name  
* Description  
* Estimated Generation Time

#### **Action**

* Generate

### Section 6 — Recent Generated Reports

Display recently generated reports.

#### **Columns**

| Column | Description |
| ----- | ----- |
| Report Name | Report title |
| Category | Report category |
| Generated By | User |
| Generated On | Date & Time |
| Format | PDF / Excel / CSV |
| Status | Processing status |
| Action | Download |

#### **Status**

See [status-badges.md](../status-badges.md#report-generation-status).

### Section 7 — Pending Operational Insights

Highlight operational items requiring attention.

#### **Escrow Operations**

* Fund releases awaiting submission  
* Returned fund release requests  
* Milestones pending verification  
* Escrow accounts requiring updates

#### **Compliance**

* Missing mandatory documents  
* Overdue responses to RERA  
* Pending financial institution actions  
* Escrow accounts approaching compliance deadlines

#### **Financial Summary**

* Total Escrow Balance  
* Funds Released This Month  
* Pending Release Value  
* Remaining Eligible Release Value

Each insight includes:

* Severity Indicator  
* Related Record  
* Recommended Action

### Empty State

**Message**

> No reports have been generated yet.

**Primary Button**

* Generate Report

**Secondary Button**

* Browse Report Templates

### Reused Components

See [components.md](../components.md) for definitions of every component used on this screen.

### User Flow

Reports  
    ↓  
Review Report Summary Cards  
    ↓  
Select Report Category  
    ↓  
Apply Filters  
    ↓  
Choose Report Template  
    ↓  
Generate Report  
    ↓  
Preview Report  
    ↓  
Export / Download / Schedule Report

### Notes

* Reports include only escrow-related operational data accessible to the Escrow Liaison.  
* Generated reports reflect the latest escrow account, fund release, and milestone information.  
* Scheduled reports are automatically generated according to the configured frequency.  
* Reports can be exported in PDF, Excel, or CSV formats.  
* Report permissions follow the Escrow Liaison role and do not expose data outside assigned escrow operations.

## User Flow

Differs by role — see the "User Flow" heading within each role's block under [Role Variations](#role-variations). The Escrow Liaison's is a single linear arrow diagram rooted at Reports itself rather than the Dashboard-rooted tree diagrams used by the other three roles.

## Notes

Differs by role — see the "Notes" heading within each role's block under [Role Variations](#role-variations).
