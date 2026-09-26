---
project: OstadLagbo
type: register
status: current
updated: 2026-09-26
id: OL-OPN-001
owner: Iftikher
---

# Open Items Register

Every unresolved item in the knowledge base, in one place. They were previously spread across ADR-001, ADR-005, the risk register, the threat model, the operations doc, the store checklist, the incident process and the test plan — eight documents for one solo builder to keep in his head.

**This register is the live view.** The source documents keep their own lists as context; when they disagree with this file, this file is right and the source is stale. Each item names its source so the reasoning is one click away.

Ordered by **when it must be resolved**, not by importance — the point is to see what is about to bite.

## Now — ahead of the build, because of lead time

| # | Item | Source | Why now |
|---|---|---|---|
| **N-1** | **Decide whether a legal entity stands behind the project** — register Octagon Soft or stay personal | OL-STR-001 | Blocks three things at once: the Apple 5.1.1(ix) risk on the existing personal account, the masked SMS sender ID (needs a trade licence, CL-036), and naming a data controller in the Privacy Policy. If you register, the D-U-N-S number takes **up to 30 days** and nothing downstream starts until it does |
| **N-2** | **Register the Google Play account** ($25) | OL-STR-001 | Free if done before Slice 3 — the 12-tester/14-day closed test then runs *during* the friends-and-family testing already planned. A two-week delay if left to Slice 4 |

## Slice 0 — resolved while building the foundation

| # | Item | Source |
|---|---|---|
| **S0-1** | Confirm whether a **legacy JWT secret** exists on the new Supabase project (60 seconds, do it first — it shapes the auth code) | ADR-005 |
| **S0-2** | Prove the **ES256 signing key against Realtime and Storage**, not just the Data API | ADR-005 |
| **S0-3** | Confirm **local-vs-hosted signing parity**; record the fallback if it fails | ADR-005 |
| **S0-4** | **Dhaka → Singapore latency test** for phone → Render → Supabase; confirm NFR-02 | ADR-001 |
| **S0-5** | Verify **Bangla fuzzy matching** against the OL-SKC-001 test set | ADR-001 |
| **S0-6** | Confirm **coordinate scrubbing** in the Render logs. The Cloudflare half waits on **S4-9** — until then Render is the only log layer there is | ADR-001, MAP-10 |
| **S0-7** | Establish the **Supabase RLS baseline** as second-line guard | ADR-001 |
| **S0-8** | **Can Cloudflare's free plan express the rate limits NFR-05 assumes?** Answerable on paper now; testable only once **S4-9** lands. If it cannot, the limits move into the API or the edge becomes a cost line — either way that is a decision, not a default | OL-THR-001 |
| **S0-9** | Choose and wire **monitoring and crash reporting** — NFR-09 names obligations, no products | OL-OPS-001, NFR-09 |
| **S0-10** | Decide where the **Storage backup** lives and what it costs — currently unbudgeted | OL-OPS-001 |
| **S0-11** | **Map tile provider bake-off** — MapTiler vs Stadia vs Google, on one Dhanmondi viewport. **Before any map screen exists** | CL-035 |
| **S0-12** | Set a **per-IP OTP limit** — does not exist; the per-number limit alone lets one source cycle thousands of numbers | OL-THR-001 |

## Slice 1–2

| # | Item | Source |
|---|---|---|
| **S1-1** | Apply for the **masked SMS sender ID** once an entity exists (3–7 business days) | CL-036 |
| **S2-1** | Set the **viewport cap and scraping rate numbers** so a full sweep of the launch area costs days, not minutes. **Implement them in the API, not only at the edge** — there is no edge yet (S4-9), and the app talks to Render directly | OL-THR-001 |

## Before soft launch (Slice 4)

| # | Item | Source |
|---|---|---|
| **S4-9** | **Buy the domain, then put Cloudflare in front of the API** (founder decision 2026-09-26: deferred until a domain exists — no domain, no edge). ADR-001 puts Cloudflare in the stack for requirement (d) — infrastructure-level request-log control and rate limiting — and `design-foundations` requires the app's base URL to be the **Cloudflare-proxied domain, not the raw `*.onrender.com` host**, permitting the raw host *"only in early Slice 0"*. **While deferred, the app calls Render directly and there is no edge log scrubbing and no edge rate limiting at all**, so the threat model's two main mitigations (T-1 scraping, T-4 OTP abuse) rest entirely on limits inside the API — see S2-1 and S0-12. Acceptable through development, where there are no real users and no stored coordinates; **not acceptable at soft launch**, when both arrive | ADR-001, NFR-05(d), OL-THR-001, OL-UI-003 |
| **S4-10** | The **domain gates three separate things**, so buying it early unblocks more than the edge: Cloudflare (S4-9), the **public web account-deletion page Google Play mandates** (OL-STR-001 §B), and — if an entity is registered (N-1) — Apple's organization enrolment, which requires a working website on the company's own domain | OL-STR-001 |
| **S4-1** | Confirm **PDPA breach-notification deadlines** and the authority's procedure with counsel — Playbook 2 says *before* an incident, not during | OL-INC-001 |
| **S4-2** | Establish the **incident contact email** — also closes the placeholders in the Privacy Policy and Terms | OL-INC-001 |
| **S4-3** | Keep an **offline copy** of the incident process and all recovery credentials | OL-INC-001 |
| **S4-4** | Verify **legal-hold, suspension and termination tooling** end to end in staging | OL-INC-001, CL-041 |
| **S4-5** | First **full restore rehearsal — database *and* Storage**, reconciled, with the RTO recorded | NFR-07, OL-OPS-001 |
| **S4-6** | **Legal review** of the Privacy Policy and Terms (Bangladeshi counsel) | CL-029 |
| **S4-7** | **Name the data controller** in the Privacy Policy — currently it names nobody | OL-STR-001 |
| **S4-8** | **Bangla versions** of the Privacy Policy and Terms — required at launch, founder-authored, not written | CL-029, OL-TST-001 |

## Before public launch (Slice 5)

| # | Item | Source |
|---|---|---|
| **S5-1** | **PDPA data-residency ruling** on identity documents in Singapore — the CL-025 deferral comes due here | ADR-001, CL-025 |
| **S5-2** | Work the **store-release checklist** — 24 items | OL-STR-001 |
| **S5-3** | Confirm **Vercel Pro**, or move the web tier to Cloudflare Pages | ADR-001 |

## Decisions pending — v1.3 scope, each needs founder approval and a CL entry

| # | Item | Source |
|---|---|---|
| **D-1** | **Content filter.** Apple Guideline 1.2 requires *"a method for filtering objectionable material from being posted"*. None exists. Also the cheapest partial mitigation for T-6 and T-8 | CL-043, OL-THR-001 |
| **D-2** | **Review notifications.** An Ostad is never told a review was left, so RNT-04's one-reply right is unusable in practice | CL-040 |
| **D-3** | **Suspension push ordering.** Suspension revokes push tokens in the same transaction, so a suspension notice is undeliverable by construction. Defensible — but currently an accident of ordering rather than a decision | CL-040 |

## Standing risks — monitored, not closeable

| # | Risk | Status |
|---|---|---|
| **R-01** | Supply-side cold start | Open — **unvalidated by decision**; the discovery sprint was declined, so the first seeded Ostads are the first validation |
| **R-04** | Exact-pin exposure | Open — inherent to the product; mitigated by consent surfaces, not removable |
| **R-05** | Solo-founder overload | Open |
| **R-08** | OTP abuse | Reduced — cost bounded at ~৳1,280/month (CL-036); the **abuse** vector stays open pending S0-12 |
| — | AI-generated code defects | Open — the reason OL-TST-001 exists |

## Closed, but still listed in a source document

ADR-001's open-items list is **stale** and cannot be edited (accepted ADRs are immutable). These three are done:

- **Item 3** — select the SMS gateway → **Alpha SMS**, CL-036
- **Item 6** — choose the API framework → **TypeScript/Node**, ADR-003 (the RLS half remains, as S0-7)
- **Item 7** — Apple Developer account timing → an account **exists**, registered personally; superseded by N-1

## Maintenance

An item closes here when it is done, with the commit or CL that closed it. A new open item is added here **and** in its source document. If this register and a source ever disagree, this register is authoritative and the source is stale — the failure this file exists to prevent is the one ADR-001 just demonstrated.
