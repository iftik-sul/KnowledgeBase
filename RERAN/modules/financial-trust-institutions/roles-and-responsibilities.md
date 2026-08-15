---
project: RERAN
module: financial-trust-institutions
type: user-group
status: draft
updated: 2026-08-15
contains_proposals: true
derived_from:
  - "RERAN/reference/source-of-truth/RERAN_user_group_structure_v2.md"
  - "RERAN/reference/source-of-truth/RERAN_service_flows_v2.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - roles
---

# Financial & Trust Institutions — Roles & Responsibilities

Group C covers banks, mortgage institutions, account trustees and auditing bureaux that finance, secure and audit real-estate transactions. Four roles operate under a single verified institution account.

This document describes post-login responsibilities only. Account creation and onboarding are out of scope for this project.

> **Confirmed 2026-08-14 — roles are attribution only.** Client decision: none of the four roles below gates access. Every role can see and act on every screen and action in this module; the descriptions in this document say what each role *typically* does and why it exists, not what it is *permitted* to do. Every action is logged with the acting user and the role they held at the time — that's the only thing role now controls. See [navigation.md](navigation.md#audit-trail-principle) for the access model and [role-workflows.md](role-workflows.md) for the shared journey this produces. This also supersedes part of answer A1 (below) — see the note under Auditing Bureau Officer.
>
> **Confirmed 2026-08-15 — extended to service ownership.** The same principle now explicitly covers *which services* a role may act on, not just which screens: `open-questions.md` A4 confirms no service is role-specific, for any of the 18 services. The Role Summary table below no longer lists a "services owned" figure per role, since none exists.

## Role Summary

| Role | Player | Primary sub-system |
| :---- | :---- | :---- |
| Mortgage Officer | Bank lending desk | Online Mortgage System |
| Institution Relationship Manager | Bank admin | Trust-Account Approval & Renewal |
| Account Trustee | Approved escrow trustee | Escrow Request Queue (Group B-originated) |
| Auditing Bureau Officer | Approved auditor | Transaction Audit Queue |

> **Corrected 2026-08-15 — "Services owned" column removed.** This table previously reported a per-role services-owned count (Mortgage Officer 9–plus-conditional, Institution Relationship Manager 3, Account Trustee 0, Auditing Bureau Officer 0), re-derived from the source's responsible-role column per an earlier version of `open-questions.md` A4. That re-derivation is superseded, not extended: A4 now confirms Group C does not assign services to roles at all — any of the four roles may act on any of the 18 services — so there is no ownership figure left to report, correct or otherwise. The "Primary sub-system" column survives because it describes where a role's *typical* work happens, not an access restriction; see the banner note above. Account Trustee and Auditing Bureau Officer's post-login behaviour, sourced from the user group structure rather than the numbered service catalogue, is still proposed rather than sourced — see each role's own section below.

---

## 1. Mortgage Officer

**Player:** Bank lending desk

### Purpose

Registers, modifies and discharges mortgages and finance leases against registered titles, and submits completed transactions for departmental audit. The highest-volume role in the module, though not an exclusive one — any of the institution's four Group C roles may perform the same actions (A4).

### Responsibilities

* Register new mortgages against a verified title
* Amend, transfer and release existing mortgages
* Register, amend, transfer and release finance leases
* Register real estate fund companies in the register of privileges
* Execute title-deed transactions arising from financing: heirs' sale, company share sale, split ownership, title deed issuance and updates
* Attach supporting documentation and submit for internal certification
* Track submitted transactions through the RERA audit queue
* Respond to information requests raised by the Compliance & Escrow Auditor

### Practical Example

A customer completes a mortgage application at the bank. The Mortgage Officer opens the Online Mortgage System, selects the property by title reference, enters the loan particulars and attaches the executed mortgage deed and party identification. The transaction is certified internally, then routed to the RERA Transaction Audit queue. On approval, fees are deducted from the bank's account and the mortgage registration certificate is delivered to both the bank and the property owner.

---

## 2. Institution Relationship Manager

**Player:** Bank admin

### Purpose

Maintains the institution's standing on the platform and manages the people who act under it.

### Responsibilities

* Maintain institutional registration details and banking credentials
* Renew trustee and auditor approvals before expiry
* Add and remove staff records within the institution *(reworded 2026-08-14 — previously "provision, scope and revoke staff access"; there are no permission scopes left to provision. Every staff member has identical system access from the moment they're added — this responsibility is now purely about who is on the institution's staff list, for audit-trail attribution, not about granting capability.)*
* Submit contract cancellation applications (Service #18), typically — any of the institution's four roles may also do this (A4)
* Monitor institution-wide transaction volume and audit outcomes

> **Proposed** — not in source material. Rationale: the source describes this role as maintaining registration, renewing approvals and provisioning users, but only one numbered service exists for it, and A4 confirms even that one isn't exclusive to this role. An institution-level oversight view is implied by the responsibility for renewals and user management, which cannot be discharged without visibility of expiry dates and staff activity. Needs client confirmation.

### Practical Example

The institution's trustee approval is due to expire in 45 days. The Relationship Manager receives a renewal notification, opens the Trust-Account Approval & Renewal system, uploads the updated audited accounts and CBN standing documentation, and submits the renewal. The Compliance & Escrow Auditor reviews and approves; the institution's approved status is extended and reflected in the public register of approved trustees.

---

## 3. Account Trustee

**Player:** Approved escrow trustee

### Purpose

Manages developer project trust accounts, certifies that milestone conditions are met before funds are released, and files audited account statements.

> **Proposed** — not in source material. Rationale: the user group structure names these three functions explicitly, and the Group B developer services show the Account Trustee acting as an approval step in escrow activation, transfer, profit withdrawal and payment requests. Those developer-side services describe the Trustee as a participant but define no Group C interface for them. The responsibilities below reconstruct what that interface must provide. Needs client confirmation.

### Responsibilities

* Review and act on escrow requests routed from developers: account activation, account transfer, profit withdrawal, payment release, mortgage deposit, bank guarantee cancellation
* Assess project solvency before certifying a release
* Upload supporting documentation and forward to the RERA escrow department
* Certify that construction milestones justify the requested drawdown
* File periodic audited statements for each managed trust account
* Maintain the register of trust accounts under management

**Confirmed 2026-08-15** — the client separately confirmed that Account Trustee access is not role-restricted, consistent with A4: any of the institution's four Group C roles, not just the Account Trustee by title, may act on escrow-queue items. The responsibilities above describe this role's typical function, not an exclusive one.

### Practical Example

A developer submits a request to draw down against a completed construction milestone. The request arrives in the queue. The acting user reviews the project's solvency position and the milestone evidence, uploads the supporting assessment, and certifies the request. It is forwarded to the RERA escrow department for final audit. On approval, the transfer is executed and the developer is notified.

**Corrected 2026-08-15** — this section previously carried its own "To Confirm" list (dedicated queue vs. external system; document upload vs. structured assessment; SLA for routed requests). All three are now resolved — by A2, A3, and A6 respectively — and duplicated the "To Confirm — Summary" section below, which had already been updated to reflect A2 and A3 but not yet A6. Rather than maintain two lists that can drift out of sync, this section now points to the single Summary below: see [To Confirm — Summary](#to-confirm--summary) for the full history of what was asked here and how each was resolved.

---

## 4. Auditing Bureau Officer

**Player:** Approved auditor

### Purpose

Provides independent audit of developer escrow accounts under the institution's trusteeship, and submits independent compliance reports to RERA. This role does **not** perform the institution's own internal certification of Mortgage Officer filings — see the correction below.

> **Corrected per `open-questions.md` A1, then superseded per the 2026-08-14 client decision.** Earlier versions of this document proposed that the mortgage registration workflow's "bank's internal auditor reviews and certifies the transaction" step belonged to this role. Answer A1 corrected that by modelling internal certification as a `certify` **permission scope**, held by any delegated staff member the Institution Relationship Manager provisions under registration Flow 5 — not a fifth capability bolted onto this role, and not a duty this role performs by virtue of its title. The user group structure's own description of this role — auditing developer escrow accounts and submitting independent compliance reports — was the accurate source all along; the certification duty was removed from this role's responsibilities to match it, and stays removed below.
>
> **What's superseded:** A1's *mechanism* — a `certify` permission scope, provisioned per staff member — no longer exists; permission scopes were retired module-wide on 2026-08-14 in favour of unified access with role-as-attribution-only (see [navigation.md](navigation.md#superseded-by-this-document)). **What's not superseded:** A1's conclusion that this role does not, by virtue of its title, perform internal certification of Mortgage Officer filings — that remains true, just for a different reason. Under the unified model, certification is an action any of the four roles may take (including this one, if it happens to be the acting user); it was never this role's assigned job, and now it's simply nobody's assigned job in particular. Screen-level detail for the role, not yet reconciled against the unified model, is in [ui/screens/compliance-reports.md](ui/screens/compliance-reports.md) and [ui/screens/trust-accounts.md](ui/screens/trust-accounts.md).

### Responsibilities

* Audit developer escrow accounts and trust accounts under the institution's trusteeship
* Prepare and submit independent compliance reports to RERA, on a RERA-defined template (per answer A7)
* Raise findings against trust accounts, escalating material findings for regulatory attention
* Maintain an audit history for each trust account and compliance report reviewed
* Open and close audit engagements against trust accounts under examination

### Practical Example

A trust account's periodic statement shows a movement the Auditing Bureau Officer cannot reconcile against the certified milestones on file. The Officer opens an audit engagement against the account, raises a finding categorised as a balance discrepancy, and — because the discrepancy is material — escalates it for RERA's attention as part of the next compliance report. The finding sets the trust account to Flagged until resolved.

### To Confirm

* **Resolved by A1, mechanism superseded 2026-08-14** — whether the "bank's internal auditor" in the mortgage workflow is this role: no, and that conclusion still holds. A1's explanation (a `certify` permission scope, held by whichever delegated staff member the institution assigned it to) no longer applies now that scopes are retired — certification is simply an action any of the four roles may take, attributed by role in the audit trail. Not an open question about this role either way.
* **Resolved by A1, mechanism superseded 2026-08-14** — whether certification is per-transaction or batch-level: still moot for this role in the sense that certification isn't this role's assigned responsibility, but "moot because the `certify` scope isn't held by this role" no longer applies, since there's no scope to hold. [ui/screens/internal-certification-queue.md](ui/screens/internal-certification-queue.md) documents certification as per-record, with no bulk action — that screen has not yet been reconciled against the unified model (out of scope for this edit; see navigation.md).
* Do compliance reports follow a RERA-defined template? **Proposed answered** by A7 (Medium confidence) — RERA-defined template, structured with a free-text findings narrative. The exact structure and reporting cycle remain undetermined; see [ui/screens/compliance-reports.md](ui/screens/compliance-reports.md#notes).

---

## How They Work Together

| Stage | Role | Action |
| :---- | :---- | :---- |
| 1 | Mortgage Officer *(typically — any role may do this)* | Enters the transaction and attaches documentation |
| 2 | Any of the four roles, including the filer *(reworked 2026-08-14 — see below)* | Certifies the transaction internally, where the institution has configured this gate for the service |
| 3 | — | Routed to the RERA Transaction Audit queue |
| 4 | Compliance & Escrow Auditor (Group A) | Approves, queries or rejects |
| 5 | — | Fees settled; output document issued |
| 6 | Institution Relationship Manager *(typically — any role may do this)* | Retains oversight of institution-wide outcomes |

**Stage 2, reworked 2026-08-14.** This row previously read `certify` permission scope (itself a correction of an earlier "Auditing Bureau Officer" version, per answer A1) — a gate only a delegated staff member holding that scope could pass, with maker ≠ checker enforced against the filer of stage 1. Per the client's 2026-08-14 decision, permission scopes are retired module-wide: certification is now an action any of the four roles may perform, including the same person who filed the transaction at stage 1, with the acting user and their role recorded in the audit trail. **A1's scope-based resolution of who may certify is superseded by this decision** — flagging the supersession here rather than rewriting A1 itself, since `open-questions.md` is out of scope for this edit. See [navigation.md](navigation.md#superseded-by-this-document) for the confirmed model.

For escrow work originating with developers, the Account Trustee typically handles stages 1–2 in practice: the request arrives from Group B, the Trustee (or, under the unified model, any other Group C role acting on the queue) assesses and certifies, and it proceeds to the same RERA audit gate.

**The two-gate pattern — sourced for the mortgage and finance-lease lifecycle, not proven universal.** Services #3–#7 source an explicit internal "bank auditor" step before RERA review. The remaining Group C services do not carry the same explicit language in the master service table, and the module's service-flow documents (see `service-flows/`) do not assert a `certify` gate for them by default — each states, service by service, whether the gate is sourced, configurable, or simply not addressed. Treat "every Group C action passes through both gates" as the working design intent for services where the institution enables it, not as a sourced fact for all eighteen. This paragraph previously stated the pattern as unconditional; that overstated what rows 28–45 actually support, and the correction is carried into every screen this document informs — see [ui/README.md](ui/README.md#structural-characteristic).

---

## To Confirm — Summary

**Corrected 2026-08-15** — this section previously claimed "four survive as genuinely open" while listing five items under "Still open," two of which (items 1 and 2) already showed as resolved in their own text — an inconsistency present before today. A6's confirmation resolves item 3 as well, leaving genuinely open items down to two: item 6 (partially — A7 is Medium confidence, not fully closed) and item 7. Seven items originally listed here; two survive as genuinely open, five are resolved and kept below with pointers rather than dropped.

**Still open:**

6. Compliance report template — RERA-defined or institution's own? **Proposed answered by A7** (Medium confidence) — RERA-defined. Structure and cycle remain open; see [ui/screens/compliance-reports.md](ui/screens/compliance-reports.md#notes).
7. **Does the Institution Relationship Manager get an institution-wide oversight dashboard? — still open in the general sense**, though a proposed answer now exists in the form of a specific screen: [ui/screens/dashboard.md](ui/screens/dashboard.md#institution-relationship-manager) and [ui/screens/institution-profile.md](ui/screens/institution-profile.md) implement one. Whether this is the *right* dashboard remains for the client to confirm; that it should exist is answer A5's High-confidence position.

**Resolved, kept for record:**

1. ~~Account Trustee interface: dedicated platform queue or external system with recorded outcome?~~ **Resolved by A2** — dedicated platform queue, sourced from rows 8–12. See [ui/screens/escrow-request-queue.md](ui/screens/escrow-request-queue.md).
2. ~~Milestone certification: document upload or structured assessment?~~ **Resolved by A3** — structured assessment, confirmed by the client 2026-08-15. See [ui/screens/escrow-request-details.md](ui/screens/escrow-request-details.md#section-4--milestone-certification).
3. ~~SLA for Trustee action on routed developer requests?~~ **Resolved by A6** (client decision, 2026-08-15) — the source's two-number reading (waiting time vs. delivery time) is confirmed correct; no new SLA figure is needed. *(Corrected 2026-08-15 — previously listed as "still open," carried over from before the client's confirmation.)*
4. ~~Is the bank's internal auditor the Auditing Bureau Officer?~~ **Resolved by A1** — no. A1's mechanism (the `certify` permission scope, held by any delegated staff member) is **superseded 2026-08-14**: scopes are retired, and certification is now an unrestricted action any of the four roles may take. The "not this role by title" conclusion still stands, just for a different reason — see the Auditing Bureau Officer section above.
5. ~~Transaction certification: per-transaction or batch?~~ **Moot per A1, mechanism superseded 2026-08-14** — this was a question about the Auditing Bureau Officer's certification cadence; the role does not certify, by practice rather than by scope restriction now. The per-record, no-bulk-action cadence in [ui/screens/internal-certification-queue.md](ui/screens/internal-certification-queue.md) has not yet been reconciled against the unified model.
