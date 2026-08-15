---
project: RERAN
module: individual-user
type: ui-spec
status: draft
contains_proposals: true
updated: 2026-08-15
derived_from:
  - "RERAN/modules/individual-user/shared-platform-features.md"
  - "RERAN/modules/individual-user/ui/README.md"
tags:
  - individual-user
  - ui-spec
  - support
---

# Screen: Help & Support

**Access:** Any authenticated Individual User.

## Purpose

Implements the "Help & Support" general platform feature named in `shared-platform-features.md` — help content and a support contact path, distinct from filing a regulatory complaint (#38), which is a formal service with its own fee and process, not a support ticket.

## Layout

```
Search Help Content
↓
FAQ / Guides by Category
↓
Contact Support
```

## Sections

### Section 1 — Search Help Content

### Section 2 — FAQ / Guides

Organized by the same 8 service categories as the Services Catalog, so a user confused about a specific service type finds relevant help without hunting through an unrelated structure.

### Section 3 — Contact Support

Standard support contact channel. **Explicitly not the same thing as Submit Complaint (#38)** — this section should say so directly, since a user with a genuine regulatory grievance against a developer, landlord, or practitioner needs #38's formal process, not a support ticket, and conflating the two would misroute real complaints into a channel with no regulatory weight.

## Empty State

Not applicable.

## Reused Components

Search Bar, Buttons.

## Validation

None specific to this screen beyond the Section 3 distinction above.

## Access

No role variation.

## User Flow

```
Sidebar → Help & Support → [search/browse] or Contact Support
```

## Notes

* If a support interaction turns out to actually be a regulatory complaint, this screen should offer to redirect to Submit Complaint (#38) rather than attempting to resolve it as a support ticket.
