---
project: ERP
module: platform
type: overview
status: current
updated: 2026-08-14
derived_from:
  - reference/discovery/multi-tenancy-and-architecture.md
---

# Platform Module

Cross-cutting architecture that every other module depends on: multi-tenancy, company/letterhead configuration, the Item Master, the custom-fields layer, and roles.

## Documents

| Document | Status |
|---|---|
| [architecture.md](architecture.md) | Current — core rules defined, custom-fields layer mechanism open |
| [decisions-log.md](decisions-log.md) | Current |

## Open work

The custom-fields/metadata layer mechanism (how an industry-specific field attaches to the core Order without becoming a fixed column) is not yet designed. This blocks finalizing the Industry Variations sections in every other module until resolved.
