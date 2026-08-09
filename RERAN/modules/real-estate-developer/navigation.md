---
project: RERAN
module: real-estate-developer
type: navigation
status: current
updated: 2026-08-09
derived_from:
  - "RERAN/modules/real-estate-developer/roles-and-responsibilities.md"
tags:
  - real-estate-developer
  - navigation
  - permissions
---

# Real Estate Developer Navigation & Access

The shared navigation structure and access rules for the module. Screen files reference this document rather than repeating the sidebar in every file.

## Organizational Structure

Real Estate Developer

├── Developer Principal / Director  
│  
├── Project Registration Officer  
│  
├── Sales & Disclosure Officer  
│  
└── Escrow Liaison

## Left Sidebar Navigation

The following sidebar is shared by operational users. Visibility depends on assigned role.

| Menu | Description |
| ----- | ----- |
| Dashboard | Personalized operational dashboard |
| Projects | Manage development projects |
| Property Registrations | Register and manage property registrations |
| Sales & Disclosures | Manage sales information and disclosures |
| Escrow Management | Monitor escrow activities |
| Applications | View submitted service applications |
| Documents | Upload and manage documents |
| Reports | Generate operational reports |
| Company Profile | View company information |
| Notifications | View alerts and system messages |
| Help & Support | Contact RERA support |

## Role Permission Matrix

| Feature | Principal / Director | Project Registration Officer | Sales & Disclosure Officer | Escrow Liaison |
| ----- | ----- | ----- | ----- | ----- |
| Dashboard | ✅ | ✅ | ✅ | ✅ |
| Company Profile | Full | View | View | View |
| Projects | Full | Full | View | View |
| Property Registrations | Full | Full | View | ❌ |
| Sales & Disclosures | Full | View | Full | View |
| Escrow Management | View | ❌ | View | Full |
| Applications | Full | Full | View | View |
| Documents | Full | Full | Full | Full |
| Reports | Full | Registration | Sales | Escrow |
| Notifications | ✅ | ✅ | ✅ | ✅ |

## Dashboard Overview by Role

| Role | Dashboard Focus |
| ----- | ----- |
| Developer Principal / Director | Executive overview, projects, registrations, sales, reports |
| Project Registration Officer | Project registrations, applications, document submissions |
| Sales & Disclosure Officer | Property listings, disclosures, buyer documentation |
| Escrow Liaison | Escrow activities, fund release status, coordination tasks |

