---
project: OstadLagbo
type: risk-register
status: current
updated: 2026-08-30
id: OL-RSK-001
owner: Iftikher
---

# Risk Register

Risks are scored Likelihood × Impact (Low / Medium / High). Owner is the founder for all entries while the team is one person; the column exists so ownership transfers cleanly later. Reviewed at each planning milestone and before each launch gate. **Last review: 2026-08-30** (end of requirements + policy phase).

| ID | Risk | L | I | Mitigation | Status |
|---|---|---|---|---|---|
| R-01 | **Supply-side cold start** — an empty map gives Shagreds nothing to find, killing the marketplace on arrival | H | H | Seed before demand: hand-recruit 30–50 Ostads in one launch area with white-glove onboarding before opening Shagred registration; focus launch on 2–3 skill categories; bilingual UI (CL-016) and Bangla search (CL-013) lower supply-side onboarding friction | Open |
| R-02 | **Identity-data exposure** — NID/passport images and selfies are high-value breach targets | M | H | Encrypted storage; admin-only access with audit logging (ADM-17); **Retention & Deletion Policy in force (OL-RET-001)** — written before any collection, as required; retention tooling (ADM-18) to be built and verified in staging before launch | Partially mitigated — policy done, tooling pending build |
| R-03 | **Trust & safety incident** — the platform leads strangers to meet in person | M | H | 18+ accounts; identity verification + approval before discoverability; report and block in MVP; chat retained as moderation evidence; **Incident Response process defined (OL-INC-001)** with safety playbook and standing pre-launch preparations | Partially mitigated — process defined, prep checklist open |
| R-04 | **Exact-pin exposure** — public exact pins can point at Ostads' homes | M | H | Baseline rider: location capture states the pin is public and encourages pinning a coaching center, shop, or landmark instead of a residence (MAP-01); ToS §4 makes pin-placement responsibility explicit | Open |
| R-05 | **Solo-founder overload** — one person is sponsor, PM, builder, and admin reviewer | H | H | Ruthless scope enforced by baseline change control (16 changes logged, none silent); documentation kept hire-ready; phased build order; admin workflow documented for transfer; support tickets (SUP) structure the inbound load | Open |
| R-06 | **Build weight vs. capacity** — the committed build has grown: in-app chat with voice notes, push, portfolio media, full admin panel with charts, support tickets, Ostad insights, and bilingual UI | **H** | H | Raised from M likelihood at 2026-08-30 review to reflect accumulated scope. Mitigation unchanged and now critical: managed services and standard libraries everywhere; sizing before build (schedule phase); the founder's AI-driven build offsets some weight; any further scope addition names its cost | Open — likelihood raised |
| R-07 | **App-store rejection** — user-generated content, chat, and identity collection attract Google Play / App Store scrutiny | M | H | **Privacy Policy and ToS drafted (OL-PRV-001, OL-TOS-001)**; report/block and moderation specified; consent capture at registration (REG-13); guest-reachable legal docs (MAP-03); 18+ gate; compliance checklist remains before submission | Partially mitigated — documents drafted, legal review pending |
| R-08 | **SMS/OTP cost and abuse** — OTP flows are a spend and spam vector | M | M | Password login keeps OTP to signup/reset/phone-change; rate limits (REG-02); SMS monitor in admin panel (ADM-19) | Open |
| R-09 | **Fake or low-quality profiles and reviews** — reputation fraud destroys the trust promise | L | M | Mitigated by design: admin approves every profile; identity gate (ADM-03) with duplicate-ID blocking (CL-012); accepted-offer-only reviews, one per pair; monitor at soft launch | Mitigated by design |
| R-10 | **Bangladesh data-protection obligations** — the Personal Data Protection Act, 2026 (in force April 2026) governs identity and location data, with penalties up to 5% of turnover | M | M | **PDPA identified and mapped**: retention durations disclosed (OL-RET-001/PRV-001), consent capture with versioned records (REG-13), erasure via self-service deletion, breach notification in incident response (OL-INC-001); data-residency check at infrastructure selection; Bangladesh-qualified legal review before launch | Partially mitigated — mapped and drafted, legal review pending |

## Review notes

R-01 and R-05 remain the two existential risks; every roadmap decision is checked against them. R-06's likelihood was deliberately raised at the 2026-08-30 review — the founder chose a full-featured MVP with eyes open, and the schedule/budget phase must size it honestly. R-04 stands because of a deliberate founder decision (exact pins, baseline §3); if incident reports at soft launch involve location exposure, the mitigation escalates to a baseline change proposal. Next scheduled review: at schedule/budget completion, then before soft launch.
