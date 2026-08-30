---
project: OstadLagbo
type: change-log
status: current
updated: 2026-08-30
id: OL-CHG-001
owner: Iftikher
---

# Change Log

Records every founder-approved change to the MVP scope baseline. Newest first. Each entry: what changed, why, where it now lives, and which baseline version absorbed it.

| ID | Date | Change | Rationale | Absorbed in |
|---|---|---|---|---|
| CL-008 | 2026-08-30 | **Address model revised for both roles:** manual street-address text plus Thana, District, Division, and Postal Code from dropdowns; replaces Division→District→Upazila/Thana→Area. Ostads keep the map pin; Shagreds gain structured address (replacing District+Area coarse location) | Cleaner, dataset-backed address structure; postal code adds locatability without coordinates | Baseline v1.1 §2; OSP-02, SGP-01/02, REG-08 |
| CL-007 | 2026-08-30 | Ostad may post one public reply per review | Fairness — an Ostad's livelihood shouldn't carry unanswered criticism | v1.1 §6; RNT-04 |
| CL-006 | 2026-08-30 | Chat content fixed to text + voice notes (no images/documents/video) | Voice-note culture fit; lower storage and moderation surface | v1.1 §4; OFR-05 |
| CL-005 | 2026-08-29 | Admin panel expanded to full control panel: analytics with charts, demand intelligence, broadcasts, audit log, retention tooling, SMS monitor, directories | Founder requires full business operation and growth control from one panel | v1.1 §5; ADM-01…21 |
| CL-004 | 2026-08-29 | Map discovery additions: gender filter, favorites (private), shareable profile deep links | Family-comfort market dynamics; comparison shopping; WhatsApp-driven growth | v1.1 §3; MAP-05/07/08 |
| CL-003 | 2026-08-29 | Guest browsing: map, search, and profiles open without an account; contact requires registration | Growth — value visible before commitment | v1.1 §3; MAP-03 |
| CL-002 | 2026-08-29 | Portfolio video: exactly one natively stored intro video, max 45 seconds; longer video via external links | Bootstrap cost control with a human touch retained | v1.1 §2; OSP-07 |
| CL-001 | 2026-08-28 | `shagred-profile` module added: minimal fields, private immutable Ostad history, strict visibility lifecycle | Ostads need something to evaluate; Shagreds must never be findable | v1.1 §2; SGP-01…06 |

## Process note

Changes CL-001 through CL-007 were approved during the requirements sessions before this log existed; they are recorded here retroactively and consolidated into baseline v1.1, restoring the baseline as the single truthful answer to scope questions. From v1.1 onward, no scope change is implemented before its entry appears here.
