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
| CL-016 | 2026-08-30 | **Bilingual MVP:** the app ships with full English **and Bangla** UI from launch, replacing "English-first, Bangla post-MVP." Localization architecture from the first commit (all strings externalized, per-locale files, Bangla rendering tested); language chosen at first launch and switchable in settings; English is the source language for specs, Bangla copy authored by the founder; Bangla versions of the Privacy Policy and Terms of Service required at launch. The admin web dashboard remains English-only. | Both languages are core to the market: seed supply (tutors, tradespeople) and guardians need Bangla for onboarding, consent comprehension (PDPA), and trust; a Bangla-first brand with an English-only interface is a mixed message. Founder authors Bangla directly and the AI-driven build maintains dual locale files cheaply, removing the usual simultaneous-launch costs. | **Pending baseline v1.2** (batched); baseline §7, all `ui/` documents when produced |
| CL-015 | 2026-08-30 | **Second-audit clarifications:** registering with a phone inside its 30-day deletion window routes to account recovery; chat messages cannot be deleted or edited by users; no per-category notification preferences in MVP (OS-level control only) | Edge behaviors made explicit so the UI layer and dev AI never guess | **Pending baseline v1.2** (batched); REG-02, OFR-03/05 |
| CL-014 | 2026-08-30 | **Ostad self-insights (basic):** private counts of profile views, offers by outcome, and connections — counts only, never viewer identities | Supply-side engagement and retention; Ostads deserve to see their funnel | **Pending baseline v1.2** (batched); OSP-12 |
| CL-013 | 2026-08-30 | **Bangla-script category matching:** every skill category carries an admin-managed Bangla name/alias; typeahead and keyword search match across both scripts with fuzzy tolerance ("গিটার" → Guitar) | Bangladesh-native discovery — a large share of Shagreds search in Bangla | **Pending baseline v1.2** (batched); ADM-11, OSP-04, MAP-06 |
| CL-012 | 2026-08-30 | **Feature-audit fix package:** consent capture at registration with versioned records and re-acceptance notices (REG-13); guest-reachable Privacy Policy and ToS; ID-number uniqueness across active accounts; Shagred profiles reportable by offer-holding Ostads; logged-in password change; offer inbox screens (OFR-09) | Feature-completeness audit — PDPA consent capture, app-store legal-access rules, identity integrity, and implied-but-unstated screens made explicit | **Pending baseline v1.2** (batched); REG-06/10/13, MAP-02/03, OFR-01/09, RNT-07, ADM-03 |
| CL-011 | 2026-08-30 | **Verified email revealed mutually on offer acceptance** (where present), alongside phone | Gives the optional email a real job as a second contact channel | **Pending baseline v1.2** (batched); OFR-04 |
| CL-010 | 2026-08-30 | **Ostad visibility pause toggle:** removes the Ostad from map/search and blocks new offers; existing chats, already-received pending offers, and direct profile access remain, with offers disabled | An Ostad at capacity needs to stop new inbound flow without vanishing on people already engaged | **Pending baseline v1.2** (batched); OSP-11, MAP-02, OFR-01 |
| CL-009 | 2026-08-30 | **In-app support ticket system added** (`support` module, SUP): Help & Support screen, categorized tickets with private threads and one screenshot, suspension-screen appeal path; admin support queue (ADM-22) | Users need help and appeals in-app; email-only support excludes many Bangladeshi users; ToS §7's appeal promise needs a door | **Pending baseline v1.2** (batched before Execution); SUP-01…06, ADM-22 |
| CL-008 | 2026-08-30 | **Address model revised for both roles:** manual street-address text plus Thana, District, Division, and Postal Code from dropdowns; replaces Division→District→Upazila/Thana→Area. Ostads keep the map pin; Shagreds gain structured address (replacing District+Area coarse location) | Cleaner, dataset-backed address structure; postal code adds locatability without coordinates | Baseline v1.1 §2; OSP-02, SGP-01/02, REG-08 |
| CL-007 | 2026-08-30 | Ostad may post one public reply per review | Fairness — an Ostad's livelihood shouldn't carry unanswered criticism | v1.1 §6; RNT-04 |
| CL-006 | 2026-08-30 | Chat content fixed to text + voice notes (no images/documents/video) | Voice-note culture fit; lower storage and moderation surface | v1.1 §4; OFR-05 |
| CL-005 | 2026-08-29 | Admin panel expanded to full control panel: analytics with charts, demand intelligence, broadcasts, audit log, retention tooling, SMS monitor, directories | Founder requires full business operation and growth control from one panel | v1.1 §5; ADM-01…21 |
| CL-004 | 2026-08-29 | Map discovery additions: gender filter, favorites (private), shareable profile deep links | Family-comfort market dynamics; comparison shopping; WhatsApp-driven growth | v1.1 §3; MAP-05/07/08 |
| CL-003 | 2026-08-29 | Guest browsing: map, search, and profiles open without an account; contact requires registration | Growth — value visible before commitment | v1.1 §3; MAP-03 |
| CL-002 | 2026-08-29 | Portfolio video: exactly one natively stored intro video, max 45 seconds; longer video via external links | Bootstrap cost control with a human touch retained | v1.1 §2; OSP-07 |
| CL-001 | 2026-08-28 | `shagred-profile` module added: minimal fields, private immutable Ostad history, strict visibility lifecycle | Ostads need something to evaluate; Shagreds must never be findable | v1.1 §2; SGP-01…06 |

## Process note

Changes CL-001 through CL-007 were approved during the requirements sessions before this log existed; they are recorded here retroactively and consolidated into baseline v1.1, restoring the baseline as the single truthful answer to scope questions. From v1.1 onward, no scope change is implemented before its entry appears here. Baseline v1.2 will be issued before the Execution phase begins, absorbing CL-009 through CL-016 and any further planning-stage changes together.
