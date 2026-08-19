---
project: RERAN
module: real-estate-developer
type: figma-prompt
status: current
updated: 2026-08-19
contains_proposals: false
derived_from:
  - "RERAN/modules/real-estate-developer/navigation.md"
  - "RERAN/modules/real-estate-developer/ui/screens/payment-history.md"
  - "RERAN/modules/financial-trust-institutions/ui/figma-prompts/README.md"
tags:
  - real-estate-developer
  - figma
  - sidebar
  - component
---

# RED-Sidebar — Component Prompt

**Built and confirmed in Figma, 2026-08-19.** This prompt was run in Figma AI and produced a working `RED-Sidebar` component; Saitama confirmed the result against this spec via screenshot the same day. Recorded here as the reference pack for this component, following the same reasoning as every other file in this folder — a prompt that already produced a correct result is the best possible sample for the next one.

## Source

Adapted from the `FI-Sidebar` component spec (Group C's equivalent sidebar, already built in the same Figma file) — same container structure, same color tokens, same active/inactive states. Only the nav item list differs, drawn from [navigation.md](../../navigation.md)'s confirmed 12-item sidebar (11 original + Payment History, added 2026-08-19).

**Assumption carried over, not yet confirmed:** the header logo asset and "Real Estate Regulatory Agency" text are assumed identical to FI-Sidebar's, since this is the same RERA platform shell rendering a different module's nav. Flag if RED should carry distinct branding.

## The Prompt

```
Create a new component named "RED-Sidebar", 240px wide, 927px tall (full viewport height), white background.

Layer structure exactly:
- RED-Sidebar
  - SidebarHeader
    - LogoContainer
      - LogoImage
      - LogoTextWrap
  - SidebarNav
    - NavItem × 12
  - SidebarFooter
    - SignOutLink

Match the exact structure, spacing, dimensions and color tokens already used in the FI-Sidebar component in this file — do not invent new values, new colors, or a new type scale. This is the same component pattern applied to a different module's nav list.

Reuse existing styles wherever one already exists in this file — the white-fill/grey-border container, the active-state blue fill, the icon and label type styles. Do not create new component definitions for anything FI-Sidebar already established; this component should feel identical in construction, only the nav item list differs.

1. Overall container

Vertical auto-layout, 240px × 927px, white fill (#FFFFFF), 1px solid right border (#DFE3E6, stroke aligned inside), 0 corner radius, 0 padding, 0 item spacing. Three sections stacked vertically: SidebarHeader, SidebarNav, SidebarFooter.

2. SidebarHeader

78px height, full width, padding 8px top/bottom, 20px left/right. Contains LogoContainer (horizontal layout):
- LogoImage: 56×60px rectangle, image fill (organization logo/crest — same asset as FI-Sidebar)
- LogoTextWrap: 136×36px frame, text "Real Estate Regulatory Agency", IBM Plex Sans Bold, 14px, letter-spacing 0.4px, color #091E42

3. SidebarNav

Takes remaining vertical space. Padding 24px top/bottom, 12px left/right, 2px item spacing between nav items. 12 nav items, each structured identically:

NavItem (inactive state):
- Size 216×36px, horizontal auto-layout
- Padding 10px top/bottom, 12px left/right
- 12px item spacing (icon to text gap)
- 8px corner radius
- Transparent background
- Left-aligned, vertically centered
- Children: IconWrapper (16×16px frame, nav icon) + Label (Inter Medium, 13px, color #505F79)

NavItemActive (active state):
- Same structure as NavItem
- Background: solid fill #006FE8
- Label color: #FFFFFF
- Icon color: white

Nav items, in this exact order:
1. Dashboard
2. Projects
3. Property Registrations
4. Sales & Disclosures
5. Escrow Management
6. Applications
7. Payment History
8. Documents
9. Reports
10. Company Profile
11. Notifications
12. Help & Support

Every item is a plain NavItem instance — none of them are locked, greyed out, badged, or role-restricted. This module has no role-based access gating: any of the four Group B roles (Developer Principal/Director, Project Registration Officer, Sales & Disclosure Officer, Escrow Liaison) sees this exact same sidebar with all 12 items enabled. Do not add a role switcher, role label, or per-role filtering control anywhere on this component.

Payment History is a reporting screen only — a per-transaction ledger of payments made across all services. Do not treat it as an account: no balance card, no top-up affordance, no funding action associated with this nav item. It only ever links to a read-only payment record view.

4. SidebarFooter

68px height, padding 12px top, 20px bottom, 12px left/right. Contains SignOutLink, same structure as NavItem: IconWrapper (16×16) + "Sign Out" text, Inter Medium 13px, color #505F79.

Keep it simple: no illustrations, no gradients, no decorative graphics, no icons or elements beyond what's specified above. Build this as a true component (not a frame) so it can be instanced across every RED screen, with the active nav item swappable per screen the same way FI-Sidebar's is.
```

## Result

Built correctly on first pass — logo, org name, all 12 items in the documented order, Dashboard shown active in blue, Sign Out pinned at the bottom. Confirmed against the spec via screenshot, 2026-08-19.

## Open follow-up

Pixel-level spacing/icon-alignment match against the actual FI-Sidebar instance in Figma has not been separately verified — only visual comparison against this written spec. Worth a direct zoom-in comparison in Figma if pixel-exact parity matters before this component is instanced across every RED screen.
