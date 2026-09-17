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

The loop back was the part no document described. It, and nine other gaps this walk
exposed, are now resolved — see the table at the end. Each gap below states its
resolution and where it was applied.

---

## Step 1 — Landing *(authenticated)*

**Screen:** [Dashboard](../screens/dashboard.md) (Archetype 4).

The officer arrives and sees role-scoped tiles: Awaiting review · Breaching SLA ·
Escrow awaiting decision · Decided this month, plus short attention lists. Every tile
routes into the Work Queue, pre-filtered.

**What they do:** read the state of their workload, then click into whatever is most
urgent.

> **G1 landing destination — RESOLVED.** Every role lands on the Dashboard, not on its
> work screen: the SLA-breach tile is the triage signal that decides which queue to
> open, so the Dashboard earns the first click. Applied in `dashboard.md`.

---

## Step 2 — Entering the queue

**Screen:** [Work Queue](../screens/work-queue.md) (Archetype 1).

This role owns **two** queue views: **Transaction** (79 services) and **Escrow /
Trust** (13 services). The spec models them as views of one screen.

**What they see:** summary KPI cards, filters, and the queue table — reference,
originating service, applicant, subject, status, age/SLA, total elapsed, and (escrow
view) the trustee-assessment indicator.

**What they do:** filter by originating service, status, age/SLA state, or channel;
search by reference, applicant, or subject; scan for SLA-breaching rows.

> **G2 queue-view switching — RESOLVED.** Two sidebar entries with distinct routes,
> rendering one screen. Escrow has a different entry gate and heavier checklist, so it
> warrants its own entry point even though the layout is shared. Applied in
> `work-queue.md`.

> **G3 empty state — RESOLVED.** Required on the Queue archetype, and it must say
> *which* empty it is: you are clear / filters hide everything / nothing has arrived.
> A blank table is never acceptable. Applied in `screen-archetypes.md` (so it
> propagates to every queue) and `work-queue.md`.

---

## Step 3 — Picking up an item — **the biggest decision, now made**

**What they do:** click a row → [Application Review](../screens/application-review.md).

> **G4 — is work assigned, or self-serve?** A-3 (dispute) explicitly **assigns** a
> case to an officer. A-1 says nothing. So it is undefined whether the 92-service
> queue is:
> - **a shared pool** every auditor pulls from (self-serve), or
> - **assigned** by a supervisor / round-robin to a named auditor.
>
> This changes the screen: an assigned model needs an "assigned to" column, a "my
> items vs all items" filter, and a reassignment path. A pool model needs claim-on-
> open (see G5) and no ownership column at all.
>
> **RESOLVED: shared pool with claim-on-open.** The A-1/A-3 asymmetry is deliberate
> and explains itself — a dispute is a long-running relationship worked over multiple
> sessions, so continuity matters and it is assigned; a transaction audit is a discrete
> task, so throughput matters and it is pooled. Applied in `work-queue.md` §4.
> Client confirmation logged in open-questions A6.

> **G5 concurrency — RESOLVED.** Claim-on-open with timed release: opening claims the
> item, inactivity lapses the claim, and it returns to the pool. Opening an item another
> officer holds offers read-only. Modals `M-QUE-01/02/03` added in `modals.md` §7b; the
> rationale is in §9. Lapse period (30 min) logged for client confirmation.

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

> **G6 partial work — RESOLVED.** A draft decision note can be saved against the item,
> visible only to the claiming officer, so a considered review can span a break or a
> shift. Discarded on release. Applied in `application-review.md` §5b.

> **G7 stepping back — RESOLVED.** "Release item" (`M-QUE-01`) returns it to the pool
> with a recorded reason — the path for "this isn't mine to decide". Reassign is
> unnecessary under a pool model. **Escalation has no target:** the eight-role model has
> no senior/junior auditor tier, so an officer who cannot decide releases. If RERA
> expects supervisory review, that is a *new role*, not a screen change (open-questions
> A6). Applied in `application-review.md` §5b.

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

## Step 6 — What happens immediately after

> **G8 — post-decision routing.** Nothing said where the officer goes after
> submitting a decision. Three options, and the choice materially affects throughput
> for a role processing this volume:
> - **Return to queue** (safe, one extra click per item)
> - **Auto-advance to the next item** (fastest; risks momentum-driven decisions)
> - **Stay on the decided item** with a confirmation (slowest; good for verification)
>
> **RESOLVED: return to the queue** with a success toast naming the outcome and a link
> back to the decided item (read-only). **Not auto-advance** — these decisions carry
> mandatory written reasons and legal weight, so deliberate re-entry beats momentum.
> **And no undo:** an earlier draft of this flow proposed an undo window, which
> contradicts `M-DEC-01` — approval issues the output immediately, so there is nothing
> to undo. The link returns to *view*, not to reverse. Applied in
> `application-review.md` §6.

---

## Step 7 — The return loop

An item decided **Request Additional Information** or **Returned** is not finished.
The applicant responds, and it **re-enters the queue** (A-1 §12).

> **G9 — where does a returning item land?** This matters on three counts:
> - Does it return to the **same officer** who queried it, or to the pool?
> - Does it keep its original SLA clock or start a new one?
> - Is it visually distinguished from a first-time item?
>
> **RESOLVED (routing):** returns to the officer who queried it where that officer is
> available — they hold the context — otherwise to the pool. Flagged as a resubmission
> with the original query shown; a Resubmission column was added to the queue table.
> Applied in `work-queue.md`. **SLA clock — RESOLVED: resets on resubmission**, giving the
> item a fresh full window. A non-resetting Total elapsed figure sits beside it so repeated
> query rounds cannot hide overall delay (open-questions A6).

---

## Step 8 — How the officer learns anything happened

> **G10 notifications — RESOLVED.** [Notifications](../screens/notifications.md) is
> built, role-scoped, with each event linking into the screen that acts on it. It is a
> convenience surface, not a system of record — the queues and audit trail remain
> authoritative, so a missed notification never means missed work.

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
| 8 | [Notifications](../screens/notifications.md) | ✅ specced |
| 9 | Audit Trail | ✅ specced |

The officer's core path and its connective tissue are now both specced — landing, queue
switching, claiming, releasing, post-decision routing, returns, and notification were the
gaps this walk exposed, and all ten are resolved below.

---

## Decisions this flow raises — **all resolved 2026-09-17**

| # | Decision | Resolution | Applied to |
| :-- | :-- | :-- | :-- |
| G1 | Landing destination | Dashboard for every role | dashboard.md |
| G2 | Queue view switching | Two sidebar entries + routes, one screen | work-queue.md |
| G3 | Empty state | Required on the Queue archetype; must say *which* empty | screen-archetypes.md, work-queue.md, notifications.md |
| **G4** | **Assigned vs self-serve** | **Shared pool** — discrete tasks pool, long-running cases assign (hence A-3 differs) | work-queue.md §4 |
| G5 | Concurrency | Claim-on-open, timed release; `M-QUE-01/02/03` | modals.md §7b, §9 |
| G6 | Draft/partial work | Draft note per claiming officer, discarded on release | application-review.md §5b |
| G7 | Release / reassign / escalate | **Release** added; reassign unnecessary under pool; **no escalation tier exists in the 8-role model** | application-review.md §5b |
| **G8** | **Post-decision routing** | **Return to queue + outcome toast; no auto-advance, no undo** | application-review.md §6 |
| G9 | Returning-item routing + SLA clock | Back to the querying officer if available, flagged as resubmission; **SLA clock resets on resubmission**, Total elapsed shown alongside | work-queue.md |
| G10 | Notifications | Screen built | screens/notifications.md |

### Still needing client confirmation

These are resolved with a working default so the build is not blocked, but each is a
business decision, not a design one:

| Item | Default taken | Why it needs the client |
| :-- | :-- | :-- |
| ~~SLA clock on returned items~~ | ✅ **Resolved:** resets on resubmission; Total elapsed shown alongside | — |
| Claim lapse period | 30 minutes inactivity | Operational tempo; too short interrupts review |
| Supervisory review tier | None (no such role exists) | If RERA expects one, it is a **new role**, not a screen change |
| Notification delivery | In-app only | Whether SLA breach / DG escalation also go by email or SMS |
