---
project: RERAN
module: regulatory-authority
type: figma-prompt
screen: _app-shell
status: draft
updated: 2026-09-14
derived_from:
  - "RERAN-Web-App / Financial & Trust Institution / FI-Sidebar (1247:36043)"
  - "RERAN-Web-App / Individual user / Background+HorizontalBorder top-bar component (e.g. 252:11940)"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
  - "RERAN/modules/regulatory-authority/ui/figma-prompts/library-assets.md"
tags: [regulatory-authority, figma-prompt, back-office, app-shell]
---

# Figma build prompt — Group A App Shell (Sidebar + Top Bar)

The shared back-office shell every Group A screen sits in. Build it ONCE and reuse it. **Both pieces
are components — do not hand-build either:**
- **Sidebar:** duplicate **FI-Sidebar** (node 1247:36043), swap the nav items.
- **Top Bar:** place the **`Background+HorizontalBorder`** component (the portal header, bound to
  Foundation tokens) and override its text per screen.

## Design tokens (Foundation styles — bind to these named variables, not raw hex)
> Canonical catalogue: **library-assets.md**. Shell-relevant subset below.
| Foundation token | Value | Used for |
| :-- | :-- | :-- |
| `background/primary` | `#FFFFFF` | sidebar + top-bar surface |
| Neutral `N40` | `#DFE2E6` | sidebar right border, dividers, profile divider |
| (untokenised) | `#E4E7EC` | top-bar bottom border, card borders (RED) — confirm token |
| Neutral `N30` | `#EBEDF0` | search + notification chips |
| Primary | `#006FE8` | active nav pill, notification dot, links |
| Neutral `N900` | `#091E42` | titles, names, logo text |
| Neutral `N400` | `#505F79` | nav labels, subtitle, role, Sign Out |
| `Body Large/Medium` | Inter Medium 18/27 | top-bar title |
| `Caption/Medium` | Inter Medium 13/20 | nav label, profile name, search text |
| `Small/Regular` | Inter Regular 12/18 | subtitle, profile role |
| (logo) | IBM Plex Sans Bold 14, +0.4 | sidebar logo text |
| `Blur/20` | backdrop blur | top-bar search chip |
| Radii | 8px (nav items, chips) · full (avatar, dot) | |
| Sizes | icon 16 · avatar 32 · chips 36 · sidebar 240 · shell rows 78 | |

## RA-Sidebar (240 × full height) — duplicate of FI-Sidebar
- **SidebarHeader** (78 tall, border-bottom `N40`, px-20 py-8): RERA logo (56×60) +
  "Real Estate Regulatory Agency" (IBM Plex Sans Bold 14, `N900`). Keep exactly.
- **SidebarNav** (flex-1, px-12 py-24, gap-2): NavItem rows (gap-12, px-12 py-10, rounded-8):
  16px icon + label (`Caption/Medium`, `N400`). **Active item: `#006FE8` background, white icon + label.**
- **SidebarFooter** (border-top `N40`, pt-12 pb-20 px-12): Sign Out (log-out icon + "Sign Out", `N400`).

### Nav items — ROLE-SCOPED (Group A has real RBAC, so lists are shorter than FTI's; styling identical)
Icons drawn from the same library set the FTI sidebar uses (suggestions in brackets; finalise in build).

- **Compliance & Escrow Auditor** (Work Queue / Application Review persona):
  Dashboard [dashboard/home] · **Work Queue** [file-check-02] · Audit Trail [clipboard-check] ·
  Notifications [bell] · Help & Support [help-circle]. Footer: Sign Out.
- **Licensing & Registration Officer:** Dashboard · Work Queue · National Practitioner Register [user-check] · Audit Trail · Notifications · Help & Support.
- **Dispute Officer:** Dashboard · Case Queue [clipboard-list] · Audit Trail · Notifications · Help & Support.
- **Revenue & Finance:** Dashboard · Fee Schedule [credit-card-01] · Reconciliation [coins-hand] · Audit Trail · Notifications · Help & Support.
- **Super Admin:** Dashboard · Admin Console [account-setting-02] · Audit Trail · Notifications · Help & Support.

(Notifications, Help & Support, Sign Out are standard shell utilities carried over from the FTI pattern —
present for every role. Audit Trail is reachable by all roles per role-screen-matrix.md.)

## Top Bar — use the `Background+HorizontalBorder` component (1200×78)
**Do not hand-build it.** Place the component and override its text per screen. Structure:
- Root: surface `background/primary`, bottom border `#E4E7EC`, px-32, flex row, gap-16.
- **Left (flex-1):** Title (`Body Large/Medium`, `N900`) + Subtitle (`Small/Regular`, `N400`) — overridden per screen.
- **Right:**
  - **Search** (224 wide): bg `N30`, `Blur/20` backdrop, rounded-8, h-35, 16px magnifier + "Search anything…"
    (`Caption/Medium`, `N400`). This is a **global** search — distinct from a screen's own filter/search row;
    the two coexist.
  - **Notification bell:** 36×36, bg `N30`, rounded-8, 16px bell, blue dot (`#006FE8`, 8px, top-right).
  - **Profile** (border-left `N40`, pl-13, gap-10): Avatar 32 (round) + name (`Caption/Medium`, `N900`) +
    role (`Small/Regular`, `N400`).
- The component has **no back button** and does not hold status/meta. On detail/decision screens the back
  affordance and status live in the Workspace (breadcrumb row + item header), not the top bar —
  see application-review.md.

> The SidebarHeader (78) and this top bar (78) sit on the same baseline row.
