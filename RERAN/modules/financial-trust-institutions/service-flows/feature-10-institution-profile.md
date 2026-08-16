---
project: RERAN
module: financial-trust-institutions
type: service-flow
status: draft
contains_proposals: true
source_type: sourced
updated: 2026-08-16
derived_from:
  - "RERAN/modules/financial-trust-institutions/ui/screens/institution-profile.md"
  - "RERAN/modules/financial-trust-institutions/open-questions.md"
tags:
  - financial-trust-institutions
  - shared-feature
  - institution-profile
---

# Feature #10 – Institution Profile

**Feature Category:** Shared Platform Features – General Platform

## 1. Feature Overview

**Institution Profile** is the institution's own standing (legal name, type, registration reference, approval status and expiry) and staff roster — not gated by role, and absorbing the display-only part of approval-expiry tracking, since no dedicated screen exists for that as a separate feature.

**Staff Records already live here — not a separate feature.** `open-questions.md` C4 lists "Staff Records" as an item to add to the module's institution-specific feature set; that instruction is stale. This document's Section 3 already describes the staff roster in full, and no separate Staff Records feature or screen exists or is needed — C4 should be read as satisfied by this feature, not as an outstanding action item.

## 2. Purpose

Let any institution user view and maintain the institution's approved standing and staff roster — role is attribution only, not a gate on who may administer the profile.

## 3. Description

Institution Standing shows the approval status badge, an expiry countdown (neutral beyond 60 days, warning inside 60, error inside 14 — the same threshold used on the Dashboard), a Renew action routing into Service Requests pre-populated with Service #1, and Cancel Approval / Cancel Contract actions routing to Services #2 and #18 respectively. Staff Records is a roster — name, email, status, date added — for audit-trail attribution only; there are no permission scopes to assign, since every staff member has identical system access from the moment they're added. Approval History is a read-only audit trail of the institution's own standing (grants, renewals, cancellations), distinct from the Audit Timeline on individual applications.

## 4. Used By

Not tied to any single numbered service — routes to Services #1, #2, and #18 (Renew, Cancel Approval, Cancel Contract) but is itself a standing feature, not a service.

## 5. Prerequisites

* User is logged into a verified institution account.

## 6. Required Information

None to view. To invite staff: name and email only.

## 7. Required Documents

None.

## 8. Service Fee

No fee for the feature itself. Renew, Cancel Approval, and Cancel Contract inherit their fee from Services #1 (upfront), #2 (no fee, confirmed by `open-questions.md` B11), and #18 (at counter, before RERA's decision) respectively.

## 9. Payment Required

**Not for viewing or staff management.** Renew routes into Service #1's own upfront-payment checkout; Cancel Contract (#18) collects payment at the counter as part of lodging, not through this feature directly.

**Corrected 2026-08-16** — this section previously described Cancel Contract's payment as happening "after RERA's decision." The client has since normalized Service #18 to pay before RERA's decision, the same as #13–#17.

## 10. Processing Authority

**Any of the institution's four Group C roles**, unrestricted. **Corrected 2026-08-15**: previously gated every edit control behind an `admin` scope, with a Staff tab assigning six scopes per staff member and an audit-exclusivity rule at assignment time. All retired — every institution user has full access, and the Staff tab is now roster-only.

## 11. Expected Processing Time

Viewing and staff-roster edits are immediate. Renew/Cancel actions follow their underlying service's own processing timeline once routed there.

## 12. Processing Workflow

Dashboard
↓
Open Institution Profile
↓
View Institution Standing (status, expiry) **or** open Staff Records / Approval History tab
↓
Renew → Service Requests (#1, pre-populated) **or** Cancel Approval → Service Requests (#2) **or** Cancel Contract → Service Requests (#18)
↓
*(Staff Records)* Invite Staff Member (email only) → Status: Invited → Active

## 13. Application Status Flow

Institution approval: Active → Expiring (within 60/14-day windows) → Renewed *(via Service #1)* or Expired/Cancelled *(via Service #2)*.

Staff roster entries: Invited → Active → Removed.

## 14. Possible Outcomes

* Approval Renewed / Cancelled
* Contract Cancelled
* Staff Member Invited / Removed

## 15. Output

* Updated approval status and expiry date, on Renew/Cancel
* Approval History entry
* Staff Records entry, on Invite/Remove

## 16. Related Features

* Service Requests *(where Renew, Cancel Approval, and Cancel Contract actually route to)*
* Dashboard *(shares the same Approval Expiry threshold and figure)*
* Payment History *(the per-transaction record of what Institution Profile's own actions eventually cost)*

## 17. UI Screens

* Institution Profile

## 18. API Requirements

* Retrieve Institution Standing
* Retrieve Staff Records / Approval History
* Invite Staff Member / Remove Staff Member
* Route to Service Requests (Renew / Cancel Approval / Cancel Contract)
* Send Notifications
* Create Audit Log

## 19. Database Entities

* Institution, Institution Staff, User
* Approval Record, Approval History
* Staff Roster Entry
* Audit Log

## 20. Acceptance Criteria

* Any of the institution's four Group C roles can view and edit every section of this feature.
* Expiry countdown matches the Dashboard's own figure exactly, using the same 60/14-day thresholds.
* Removing a staff member does not retroactively invalidate that user's past certifications elsewhere in the module.
* Renew, Cancel Approval, and Cancel Contract route into Service Requests rather than collecting payment directly.
* All standing changes and staff-roster edits are recorded in the audit log.

## 21. Business Rules

1. Any of the institution's four Group C roles may invite/remove staff, renew, or cancel — no role or scope restriction.
2. The Staff Records tab is a roster for audit-trail attribution only — there is nothing to assign, since every staff member has identical access.
3. Removing a staff member does not retroactively alter the audit trail of their past actions.
4. Renew, Cancel Approval, and Cancel Contract are entry points into Service Requests (#1, #2, #18 respectively), not payment-collecting actions of this feature itself.
5. Approval History is read-only and distinct from any individual application's own Audit Timeline.
6. All access and edits are permanently recorded in the audit trail, including the acting user's role.

## Open Questions

1. Is the two-year approval validity duration (proposed under B8) correct, or should a different term apply? The renewing structure itself is confirmed; the specific duration is this module's own proposal.
2. Does RERA gate approval renewal on reporting compliance (per Compliance Reports)? A client question, not resolved here.
3. `services-overview.md` To Confirm item 2 remains open and covers this feature too.
