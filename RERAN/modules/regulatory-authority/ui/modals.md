---
project: RERAN
module: regulatory-authority
type: ui-modals
status: draft
contains_proposals: true
updated: 2026-09-17
derived_from:
  - "RERAN/modules/regulatory-authority/service-flows/ (A-1..A-10)"
  - "RERAN/modules/regulatory-authority/ui/validation-rules.md"
  - "RERAN/modules/regulatory-authority/ui/status-badges.md"
  - "RERAN/modules/regulatory-authority/ui/role-screen-matrix.md"
tags:
  - regulatory-authority
  - ui-spec
  - modals
---

# Group A — Modals & Alerts

The single source for every modal, confirmation, and alert in the back-office app.
Screen specs **reference** a modal by its ID here; they never restate its wording,
fields, or rules. This mirrors how `status-badges.md` owns status wording and
`validation-rules.md` owns guard rules.

Group A carries the platform's most consequential actions — revocations, account
deactivation, fee publishing, executive sign-off — so confirmation design is a real
safety control here, not decoration.

## How to use this file

- Every state-changing action names the modal it raises, by ID (e.g. `M-DEC-04`).
- The **guard** that decides whether an action is even available lives in
  [validation-rules.md](validation-rules.md); this file describes what the user
  *sees*. Guard = whether; modal = how it's confirmed.
- Status words shown in any modal come from [status-badges.md](status-badges.md).

---

## 1. Modal patterns

Every modal below follows one of six patterns. Pattern decides layout and button
treatment, so we don't design each modal from scratch.

| # | Pattern | When | Shape |
| :-- | :-- | :-- | :-- |
| **P1** | **Confirm** | A significant but reversible action | Title · what will happen · Cancel / Confirm |
| **P2** | **Reason-required** | The action must carry a recorded justification | Title · consequence · **mandatory reason field** · Cancel / Submit (disabled until reason entered) |
| **P3** | **Destructive** | Irreversible, or withdraws access/standing | Title · explicit consequence statement · **typed or explicit acknowledgement** · Cancel / destructive-styled action |
| **P4** | **Form** | The action needs structured input, not just assent | Title · form fields · Cancel / Save |
| **P5** | **Blocked** | The action cannot proceed; explains why and what to do | Title · reason blocked · what would unblock it · single Dismiss |
| **P6** | **System alert** | Session, connectivity, concurrency — not user-initiated | Title · situation · recovery action |

**Rules.**
- Reversible + low-consequence → no modal at all; act and show a success toast.
- Anything writing to the audit trail with a reason → **P2**, never P1.
- Anything that withdraws access, standing, or money → **P3**.
- A modal never contains a second modal.

---

## 2. Decision modals (A-1, A-2) — the highest-traffic in the platform

Raised from **Application Review**. These four back the decision panel that finishes
92 + 9 services.

| ID | Modal | Pattern | Notes |
| :-- | :-- | :-- | :-- |
| `M-DEC-01` | Approve | P1 | States the output that will be issued (certificate / title deed / map / registry update) and that issuance is immediate. Reason optional. |
| `M-DEC-02` | Request Additional Information | P2 | Reason = what is needed. Returns item to applicant; re-enters queue on response. |
| `M-DEC-03` | Return for Correction | P2 | Reason = what to correct. |
| `M-DEC-04` | Reject | P2 | Reason mandatory; states the decision is **terminal**. |

---

## 3. Licensing modals (A-2)

Raised from Application Review (licensing items) and the Practitioner Register.

| ID | Modal | Pattern | Notes |
| :-- | :-- | :-- | :-- |
| `M-LIC-01` | Issue credential | P1 | Confirms credential type and that the register entry will be written. |
| `M-LIC-02` | Amend credential | P4 | Structured edit of an existing entry. |
| `M-LIC-03` | **Cancel / revoke practice card** | P3 | Withdraws the holder's standing to operate. States effect on the register. Step-up re-authentication required (§9). |
| `M-LIC-04` | Escalate revocation to DG | P2 | Reason = the recommendation the DG will review (feeds `M-GOV-01`). |
| `M-LIC-05` | Record accreditation outcome | P4 | Captures the result of the off-platform meeting/agreement process (A-2 §15c). |

---

## 4. Dispute modals (A-3)

Raised from the Case Workspace. Note these attach to a **case lifecycle**, not the
four-state decision vocabulary.

| ID | Modal | Pattern | Notes |
| :-- | :-- | :-- | :-- |
| `M-DIS-01` | Schedule session | P4 | Date/time, mediation or hearing, remote link, parties notified. |
| `M-DIS-02` | Record session outcome | P4 | What happened; whether another session is needed. |
| `M-DIS-03` | Request evidence | P2 | Moves case to Information Requested. |
| `M-DIS-04` | **Record judgment** | P4 + P3 traits | The case's terminal act: outcome (Resolved / Partially Resolved / Referred) + basis + any assignment. Cannot be undone once recorded. |
| `M-DIS-05` | Dismiss case | P2 | Reason mandatory; terminal. |
| `M-DIS-06` | Record withdrawal | P2 | Filing party withdrew; terminal. |
| `M-DIS-07` | Refer to another forum | P2 | Beyond RERA's remit; names the forum. |

---

## 5. Finance modals (A-4, A-5)

| ID | Modal | Pattern | Notes |
| :-- | :-- | :-- | :-- |
| `M-FIN-01` | Create / edit fee entry | P4 | Service or levy, amount, effective dates. |
| `M-FIN-02` | **Publish schedule** | P3 | **Must state blast radius**: takes effect for *every* fee-bearing service at checkout, immediately. Step-up re-authentication required (§9). |
| `M-FIN-03` | Revert to prior version | P3 | Restores a previous published schedule; states which version and its amounts. |
| `M-FIN-04` | Archive entry | P1 | Retains history with effective dates. |
| `M-FIN-05` | Run reconciliation | P1 | Names the period. |
| `M-FIN-06` | Resolve discrepancy | P2 | **Reason mandatory** — discrepancies may not be auto-cleared (validation-rules). |
| `M-FIN-07` | Record remittance | P1 | Destination account and amount. |

---

## 6. Admin / RBAC modals (A-6) — most sensitive

Raised from the Admin Console. Every one of these changes who can do what.

| ID | Modal | Pattern | Notes |
| :-- | :-- | :-- | :-- |
| `M-ADM-01` | Invite / create staff account | P4 | Identity + initial role(s); account cannot act until MFA enrolled. |
| `M-ADM-02` | Assign / revoke role | P2 | Reason recorded; states which screens the change grants or removes. |
| `M-ADM-03` | **Change role permissions** | P3 | **Affects every user holding that role**, not one person. Must say so explicitly. Step-up re-authentication required (§9). |
| `M-ADM-04` | Enrol / reset MFA | P4 | Reset invalidates the existing factor. |
| `M-ADM-05` | **Suspend account** | P3 | Access withdrawn immediately; reversible. |
| `M-ADM-06` | **Deactivate account** | P3 | Access withdrawn immediately; treated as permanent. Step-up re-authentication required (§9). |

---

## 7. Field & governance modals (A-7, A-8, A-10)

**A-7 (inspection) and A-10 (sign-off) screens are now in scope** (open-questions A5);
their modals are live. **A-8 (enforcement) and the A-9 land modals remain deferred** —
listed so the catalogue is complete and the deferred specs need no new IDs later.

| ID | Modal | Pattern | Notes |
| :-- | :-- | :-- | :-- |
| `M-INS-01` | Schedule inspection | P4 | Site, date, assigned officer. |
| `M-INS-02` | Submit inspection report | P1 | States the report returns to the dependent decision (A-1). |
| `M-ENF-01` | **Issue enforcement notice** | P3 | Stop-work / violation against a named entity; serious and public-facing. |
| `M-ENF-02` | Escalate to DG sign-off | P2 | Recommendation the DG reviews. |
| `M-ENF-03` | Escalate penalty to finance | P2 | Hands the penalty to A-5 for collection. |
| `M-ENF-04` | Resolve / close notice | P2 | Violation remedied. |
| `M-GOV-01` | **Authorise sign-off** | P3 + step-up | The most consequential action in the module — executes a revocation or final enforcement. Re-authentication **required** (§9). |
| `M-GOV-02` | Decline sign-off | P2 | Reason returns to the originating tier. |
| `M-LND-01` | Run harmonisation comparison | P1 | Names the bureau and period. Manual reconciliation, not a sync (A4). |
| `M-LND-02` | Resolve conflict | P4 | Choose the authoritative record; bureau is authoritative for state-held data (A-9 §21). |
| `M-LND-03` | Escalate jurisdictional dispute | P2 | |

---

## 7b. Queue-management modals (A-1, A-2)

Added to resolve flow gaps G5 and G7 (see
[flows/compliance-escrow-auditor.md](flows/compliance-escrow-auditor.md)).

| ID | Modal | Pattern | Notes |
| :-- | :-- | :-- | :-- |
| `M-QUE-01` | **Release item** | P2 | Returns a claimed item to the pool. Reason recorded (e.g. conflict of interest, wrong specialism). Any draft note is discarded. |
| `M-QUE-02` | Claim expired | P6 | The officer's claim lapsed through **30 minutes of inactivity**; the item returned to the pool and may now be held by someone else. |
| `M-QUE-03` | Item already claimed | P6 | Opening an item another officer holds. Shows who holds it and since when; offers to open read-only. |

---

## 8. Blocked-action modals (P5)

These fire when a guard in [validation-rules.md](validation-rules.md) prevents an
action. They explain *why* and *what would unblock it* — they never silently disable
a button with no explanation.

| ID | Blocked action | Says |
| :-- | :-- | :-- |
| `M-BLK-01` | Decide with registry checks unavailable | Live checks could not be retrieved; decision unavailable until they load. |
| `M-BLK-02` | Decide an escrow item with no trustee assessment | The FTI Account Trustee has not forwarded its assessment. |
| `M-BLK-03` | Approve a mortgage-linked item whose prerequisites fail | Names the unmet prerequisite (RED #6 dependency). |
| `M-BLK-04` | Close a case with no recorded outcome | A judgment, dismissal, or withdrawal must be recorded first. |
| `M-BLK-05` | Act without decide rights | Reaching a screen does not grant decide rights (role-screen-matrix §2). |
| `M-BLK-06` | Act without enrolled MFA | MFA must be enrolled before any action. |

---

## 9. System alerts & concurrency (P6)

Cross-cutting; not raised by a single screen.

| ID | Alert | Notes |
| :-- | :-- | :-- |
| `M-SYS-01` | **Item locked / already decided by another officer** | **Resolved** — claim-on-open; see below. Raises `M-QUE-03` on open, `M-QUE-02` on lapse. |
| `M-SYS-02` | Step-up authentication | **Required** before the five widest-consequence actions — see below. |
| `M-SYS-03` | Session expiry warning | Warn **before** timeout so an unsaved reason isn't lost. |
| `M-SYS-04` | Unsaved changes | Leaving a review or editor mid-edit. |
| `M-SYS-05` | Action failed / retry | A write did not complete. |
| `M-SYS-06` | SLA breach warning | Item past its originating service's window (non-blocking). |

### Concurrency — `M-SYS-01` *(Resolved 2026-09-17)*

Multiple officers work the same queue, so two auditors will open the same item.

**Resolved: claim-on-open with timed release.** Opening an item claims it to that
officer; others see it as claimed and may open it read-only (`M-QUE-03`). A claim
lapses after a period of inactivity and the item returns to the pool (`M-QUE-02`).
The officer may also release it deliberately (`M-QUE-01`).

**Why pessimistic rather than optimistic:** these decisions are slow, considered, and
carry mandatory written reasons. Losing that work to a race is worse than briefly
blocking a colleague. Every claim, lapse, and release is written to the audit trail.

**Claim lapse period — confirmed: 30 minutes of inactivity** (open-questions A6).

### Step-up authentication — `M-SYS-02` *(Confirmed 2026-09-17)*

**Required** on the five widest-consequence actions: `M-ADM-03` (change role
permissions), `M-ADM-06` (deactivate account), `M-LIC-03` (revoke credential),
`M-GOV-01` (authorise sign-off), `M-FIN-02` (publish fee schedule). The officer
re-authenticates before the action proceeds — accepted friction on the five actions
with the widest blast radius (open-questions A6).

---

## 9b. Modals not yet cited by a screen

Every modal should be cited by the screen that raises it. These are the exceptions, and each
is expected — listed so an audit does not re-flag them:

| Modals | Why uncited |
| :-- | :-- |
| `M-INS-01`, `M-INS-02`, `M-GOV-02` | A-7 and A-10 are **in scope but not yet specced**; their screens will cite these. |
| `M-ENF-01`…`M-ENF-04` | A-8 enforcement is **deferred** — no screens. |
| `M-LND-01`…`M-LND-03` | A-9 harmonisation is **deferred** — no screens. |
| `M-SYS-01`, `M-SYS-02`, `M-SYS-03`, `M-SYS-05`, `M-SYS-06` | Cross-cutting system alerts raised by the app shell, not by one screen. |

---

## 10. What does *not* get a modal

To keep confirmation meaningful, these act immediately with a success toast: opening
an item, filtering or searching a queue, marking a document seen, saving a draft,
changing a dashboard period, reading the audit trail. Over-confirming trains users to
dismiss modals unread, which defeats the ones in §5–§7 that matter.
