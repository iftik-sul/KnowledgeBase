---
project: RERAN
module: regulatory-authority
type: ui-flow
status: draft
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/service-a1-audit-and-decide.md"
  - "RERAN/modules/regulatory-authority/ui/screens/"
  - "RERAN/modules/regulatory-authority/ui/modals.md"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
tags:
  - regulatory-authority
  - ui-flow
  - compliance-escrow-auditor
---

# Flow — Compliance & Escrow Auditor

The end-to-end journey for Group A's busiest role: the officer who finishes **92 of
the 114** external services. Walked step by step rather than screen by screen,
because the transitions between screens are where the gaps are.

**How this differs from the other docs.** `role-screen-matrix.md` says which screens
this role can reach; the screen specs say what each screen contains; this file says
**what happens in what order, and what the officer sees between screens**. Where a
step needs a modal it names the ID from [modals.md](../modals.md).

**Scope note.** Authentication (login / MFA) is parked for now, so the journey begins
at landing. Steps that assume an authenticated session are marked.

---

## The journey at a glance

```
Land  →  Dashboard  →  Work Queue  →  Open item  →  Review  →  Decide  →  ?
                            ↑                                             │
                            └──────────────  return / next  ─────────────┘
                                             ▲
                        applicant responds → item re-enters the queue
```

The loop back is the part no document currently describes. See §7 and §8.

---

## Step 1 — Landing *(authenticated)*

**Screen:** [Dashboard](../screens/dashboard.md) (Archetype 4).

The officer arrives and sees role-scoped tiles: Awaiting review · Breaching SLA ·
Escrow awaiting decision · Decided this month, plus short attention lists. Every tile
routes into the Work Queue, pre-filtered.

**What they do:** read the state of their workload, then click into whatever is most
urgent.

> **Gap G1 — landing destination.** Nothing states whether this role lands on the
> Dashboard or straight into the Work Queue. For a high-volume processing role, an
> extra click before work every session is a real cost. **Proposed:** land on the
> Dashboard, because the SLA-breach tile is the triage signal that decides which
> queue to open. Needs confirmation.

---

## Step 2 — Entering the queue

**Screen:** [Work Queue](../screens/work-queue.md) (Archetype 1).

This role owns **two** queue views: **Transaction** (79 services) and **Escrow /
Trust** (13 services). The spec models them as views of one screen.

**What they see:** summary KPI cards, filters, and the queue table — reference,
originating service, applicant, subject, status, age/SLA, and (escrow view) the
trustee-assessment indicator.

**What they do:** filter by originating service, status, age/SLA state, or channel;
search by reference, applicant, or subject; scan for SLA-breaching rows.

> **Gap G2 — how the officer switches queue view.** Tab, sidebar item, or filter? The
> matrix lists "Work Queue — transaction" and "Work Queue — escrow" as separate
> navigation rows, which implies **two sidebar items**; the screen spec calls them
> views of one screen. These are not quite the same thing. **Proposed:** two sidebar
> entries, one screen, distinct URLs — escrow work is materially different (trustee
> pre-gate, heavier checklist) and deserves its own entry point.

> **Gap G3 — empty state.** Not specified anywhere. An auditor with an empty queue
> should see confirmation they are clear, not a blank table. Every other module
> specs empty states (76 mentions); Group A specs none.

---

## Step 3 — Picking up an item — **the biggest open question**

**What they do:** click a row → [Application Review](../screens/application-review.md).

> **Gap G4 — is work assigned, or self-serve?** A-3 (dispute) explicitly **assigns** a
> case to an officer. A-1 says nothing. So it is undefined whether the 92-service
> queue is:
> - **a shared pool** every auditor pulls from (self-serve), or
> - **assigned** by a supervisor / round-robin to a named auditor.
>
> This changes the screen: an assigned model needs an "assigned to" column, a "my
> items vs all items" filter, and a reassignment path. A pool model needs claim-on-
> open (see G5) and no ownership column at all.
>
> **Proposed:** shared pool with claim-on-open. It suits high volume and uneven
> arrival, and no source describes a supervisor allocation step. **This is a real
> design decision and should be confirmed before the screen is built.**

> **Gap G5 — concurrency.** Two auditors open the same item. Raises `M-SYS-01`
> (modals.md §9). Proposed there: claim-on-open with timed release. Unresolved.

---

## Step 4 — Reviewing

**Screen:** Application Review (Archetype 2).

**What they see, in one view:** the application as submitted · all uploaded documents
· **live registry checks** (developer / project / unit / title / applicant) each with
a pass/attention indicator · and for escrow items, the **trustee assessment** and
**escrow-account state**; for mortgage-linked items, the live FTI mortgage status
(must read `Completed`).

**What they do:** read the application, open and mark documents seen or flagged, and
work the review checklist rendered as live checks.

**Modals that can fire here before any decision:**
- `M-BLK-01` registry checks unavailable → decision unavailable
- `M-BLK-02` escrow item with no trustee assessment → decision unavailable
- `M-BLK-03` mortgage prerequisites unmet → approval blocked

> **Gap G6 — partial work.** A considered review may span a break or a shift. Nothing
> describes saving a draft reason or a part-finished checklist. `M-SYS-04` (unsaved
> changes) warns on exit, but there is nowhere for the work to go. **Proposed:** allow
> a draft decision note saved against the item, visible only to the claiming officer.

> **Gap G7 — can the officer step back?** No path is documented for "this isn't mine
> to decide" — no release-back-to-queue, no reassign to a colleague, no escalate to a
> senior. A real regulator needs at least release. **Proposed:** add "Release item"
> (returns to pool, records in audit trail). Reassign/escalate needs a client answer.

---

## Step 5 — Deciding

**Screen:** Application Review → Decision Panel (sticky footer), enabled only for
this role.

Four mutually exclusive outcomes, each raising its modal:

| Action | Modal | Pattern |
| :-- | :-- | :-- |
| Approve | `M-DEC-01` | P1 — states the output that will be issued |
| Request Additional Information | `M-DEC-02` | P2 — reason mandatory |
| Return for Correction | `M-DEC-03` | P2 — reason mandatory |
| Reject | `M-DEC-04` | P2 — reason mandatory, terminal |

On approve the originating service's output is issued (certificate / title deed / map
/ registry update), the applicant is notified, and the decision, actor, and reason are
written to the audit trail. Status moves per [status-badges.md](../status-badges.md)
§1 — the shared vocabulary the originating modules read.

---

## Step 6 — What happens immediately after — **undocumented**

> **Gap G8 — post-decision routing.** Nothing says where the officer goes after
> submitting a decision. Three options, and the choice materially affects throughput
> for a role processing this volume:
> - **Return to queue** (safe, one extra click per item)
> - **Auto-advance to the next item** (fastest; risks momentum-driven decisions)
> - **Stay on the decided item** with a confirmation (slowest; good for verification)
>
> **Proposed:** return to the queue with a success toast naming the outcome and an
> "undo-window" style link back to the item for a short period. Not auto-advance —
> the decisions here carry mandatory reasons and legal weight; speed is not the
> primary virtue. Needs confirmation.

---

## Step 7 — The return loop

An item decided **Request Additional Information** or **Returned** is not finished.
The applicant responds, and it **re-enters the queue** (A-1 §12).

> **Gap G9 — where does a returning item land?** Undocumented, and it matters:
> - Does it return to the **same officer** who queried it, or to the pool?
> - Does it keep its original SLA clock or start a new one?
> - Is it visually distinguished from a first-time item?
>
> **Proposed:** returns to the same officer where that officer is available (they hold
> the context), visibly flagged as a resubmission with the original query shown, and
> the SLA clock behaviour confirmed with the client — it has contractual implications.

---

## Step 8 — How the officer learns anything happened

> **Gap G10 — no notifications screen.** All four other modules have one; Group A has
> none. Without it, the officer only discovers a returned item, an SLA breach, or an
> escalation by re-opening the queue. This is the strongest argument for building the
> Notifications screen in the Tier 1 batch rather than later.

---

## Step 9 — Looking back

**Screen:** [Audit Trail](../screens/audit-trail.md) — read-only, reachable by every
role. The officer can review their own past decisions and reasons. Append-only; no
edit path exists anywhere.

---

## Screens this flow touches

| Step | Screen | Status |
| :-- | :-- | :-- |
| 1 | Dashboard | ✅ specced |
| 2–3 | Work Queue (transaction + escrow views) | ✅ specced |
| 4–6 | Application Review + Decision Panel | ✅ specced |
| 8 | Notifications | ❌ **missing** |
| 9 | Audit Trail | ✅ specced |

The officer's core path is fully specced. What is missing is **the connective tissue**
— landing, queue switching, claiming, releasing, post-decision routing, returns, and
notification.

---

## Decisions this flow raises

| # | Decision | Proposed |
| :-- | :-- | :-- |
| G1 | Landing destination | Dashboard |
| G2 | Queue view switching | Two sidebar entries, one screen |
| G3 | Empty state | Add (platform-standard elsewhere) |
| **G4** | **Assigned vs self-serve pool** | **Shared pool — biggest open decision** |
| G5 | Concurrency | Claim-on-open, timed release (modals.md §9) |
| G6 | Draft/partial work | Draft note per claiming officer |
| G7 | Release / reassign / escalate | Add Release; reassign needs client answer |
| **G8** | **Post-decision routing** | **Return to queue, not auto-advance** |
| G9 | Returning-item routing + SLA clock | Same officer; SLA behaviour needs client |
| G10 | Notifications | Build in Tier 1 |

G4 and G8 are the two that change the screens themselves; the rest add to them.
