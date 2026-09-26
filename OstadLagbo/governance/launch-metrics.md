---
project: OstadLagbo
type: metrics
status: current
updated: 2026-09-26
id: OL-MET-001
derived_from: /OstadLagbo/governance/build-sequence.md
owner: Iftikher
---

# Launch Area and Success Metrics

Names the launch area and sets the targets the Slice 5 gate measures against ("funnel metrics from soft launch reviewed against targets" — OL-BLD-001). Until this document existed, that gate had no numbers to read. Targets are **initial and reviewable** — they are set to be checked, and the first real data is expected to move them.

## Launch area

**Dhanmondi, Dhaka** (CL-037). One thana, roughly 5 km², dense in exactly the tutoring and music-teaching demand the launch-focus categories target.

The launch area is where **supply is deliberately concentrated** and where these targets are measured. It is not a restriction on who may use the app: registration, the map, and discovery are open across Bangladesh from the first release, and nothing is geofenced. An Ostad outside Dhanmondi who finds the app is welcome — they are simply not part of the recruitment push or the soft-launch measurement.

**Why one thana rather than the city.** A marketplace fails on density, not on reach. Thirty to fifty Ostads spread across Dhaka's ~306 km² would put roughly seven per category in the whole city, so a search at MAP-04's default 5 km radius would almost always return nothing — the empty map that risk **R-01** rates High/High. The same Ostads inside Dhanmondi's ~5 km² are all within one default-radius search of each other. The area expands once the targets below are met, not before.

## Targets — soft launch (Slice 4 → Slice 5 gate)

### Supply

| Metric | Target | Why this number |
|---|---|---|
| Approved Ostads in Dhanmondi before demand opens | **40** | Midpoint of R-01's 30–50. Across the six launch-focus categories that is ~7 each within one radius — thin but never empty |
| Coverage: launch-focus categories with ≥3 approved Ostads | **6 of 6** | A category with one Ostad is a dead end when that Ostad pauses or declines |
| Ostads receiving ≥1 offer within 30 days of approval | **≥40%** | Supply that never gets an offer churns; this is the earliest warning |

### Demand

| Metric | Target | Why this number |
|---|---|---|
| Guest → registration | **≥8%** | Guests browse freely (MAP-03), so this measures whether the map alone earns a signup |
| Registered Shagred → sends ≥1 offer | **≥30%** | Separates "signed up" from "actually asked for something" |
| **Offer → acceptance** | **≥35%** | **The success unit** (ADM-12). The one number that says the marketplace works |
| Median time from offer sent → Ostad responds | **≤24 h** | A marketplace that answers slowly is a marketplace people stop using |

### Quality and retention

| Metric | Target | Why this number |
|---|---|---|
| Searches returning zero results | **<20%** | Directly measures whether supply density is real. Tagged by category and area (MAP-11), so a miss names its own cause |
| Connected Shagreds sending a 2nd offer within 60 days | **≥25%** | Distinguishes a working marketplace from one-off curiosity |
| Reviews left per connection | **≥30%** | Below this, trust signals (RNT) stay too sparse to guide anyone |

## How each is measured

Every metric above is already instrumented — the events exist across the module `ui` and `api` layers from first release (MAP-11, OFR-06/08, RNT-09/10, ADM-12/13/14), and none is retrofitted. Analytics carry a **coarsened area, never an exact map centre** (MAP-10), which is sufficient to attribute a metric to Dhanmondi without storing anyone's position.

## Expansion

The launch area widens when supply targets hold and the zero-result rate sits under target for **four consecutive weeks**. Expansion is by adjacent thana — Mohammadpur and New Market are the natural next steps — never to "all of Dhaka" in one move, for the density reason above. Each expansion re-runs the supply targets for the new area.

## Review

Read at the Slice 4 → Slice 5 gate, then monthly. A missed target is an input to a decision, not a failure to explain away; a target met far too easily was set too low and is raised.
