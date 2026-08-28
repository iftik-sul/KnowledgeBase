---
project: OstadLagbo
type: risk-register
status: current
updated: 2026-08-28
id: OL-RSK-001
owner: Iftikher
---

# Risk Register

Risks are scored Likelihood × Impact (Low / Medium / High). Owner is the founder for all entries while the team is one person; the column exists so ownership transfers cleanly later. Reviewed at each planning milestone and before each launch gate.

| ID | Risk | L | I | Mitigation | Status |
|---|---|---|---|---|---|
| R-01 | **Supply-side cold start** — an empty map gives Shagreds nothing to find, killing the marketplace on arrival | H | H | Seed before demand: hand-recruit 30–50 Ostads in one launch area with white-glove onboarding before opening Shagred registration; focus launch on 2–3 skill categories | Open |
| R-02 | **Identity-data exposure** — NID/passport images and selfies are high-value breach targets | M | H | Encrypted storage; access restricted to admin review; audit logging; retention and deletion policy written before first document is collected; self-service account deletion honors it | Open |
| R-03 | **Trust & safety incident** — the platform leads strangers to meet in person | M | H | 18+ accounts only; identity verification + admin approval before discoverability; report and block in MVP; chat retained for moderation evidence; incident-response process defined before soft launch | Open |
| R-04 | **Exact-pin exposure** — public exact pins can point at Ostads' homes | M | H | Baseline rider: location capture must state the pin is public and encourage pinning a coaching center, shop, or landmark instead of a residence | Open |
| R-05 | **Solo-founder overload** — one person is sponsor, PM, builder, and admin reviewer | H | H | Ruthless MVP scope (enforced by baseline change control); documentation kept hire-ready; phased build order; admin workflow documented for transfer | Open |
| R-06 | **Build weight vs. capacity** — in-app chat, push notifications, full portfolio media, and a separate web dashboard are each real infrastructure | M | H | Size before building; prefer managed services (auth, messaging, storage, push) over custom builds; cut to last-responsible-moment where possible | Open |
| R-07 | **App-store rejection** — user-generated content, chat, and identity collection attract Google Play / App Store scrutiny | M | H | Compliance checklist before submission: privacy policy, report/block visible, moderation documented, data-safety forms accurate; 18+ gate already aligns with policy | Open |
| R-08 | **SMS/OTP cost and abuse** — OTP flows are a spend and spam vector | M | M | Password login keeps OTP to signup and reset only; rate-limit OTP requests per number and device | Open |
| R-09 | **Fake or low-quality profiles and reviews** — reputation fraud destroys the trust promise | L | M | Largely mitigated by design: admin approves every profile; only accepted-offer Shagreds may review, one per pair; monitor at soft launch | Mitigated by design |
| R-10 | **Bangladesh data-protection obligations** — legal requirements for identity and location data may constrain design | M | M | Research obligations during planning (stakeholder S-07); privacy policy and consent language reviewed before launch | Open |

## Review notes

R-01 and R-05 are the two existential risks; every roadmap decision should be checked against them. R-04 exists because of a deliberate founder decision (exact pins, baseline §3) — if incident reports at soft launch involve location exposure, the mitigation escalates to a baseline change proposal.
