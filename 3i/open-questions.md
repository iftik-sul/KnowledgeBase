---
project: 3i
type: overview
status: current
updated: 2026-08-18
tags:
  - open-questions
  - cross-cutting
---

# Open Questions

Unresolved items. Each blocks something specific. Resolved items move to [decisions/](decisions/README.md) and are removed from here.

---

## Blocking Documentation

### OQ-01 — Module partition

Thirteen modules proposed in [project-standards.md](project-standards.md#modules--not-yet-decided), deferred for later decision. Until settled, no document IDs can be assigned and `modules/` cannot be populated. Cheap to change now; expensive once files exist and cross-link.

---

## Blocking Commerce (Phase 2)

### OQ-02 — What a seat actually is

Agreed that seats are an account-level pool rather than being tied to a named profile. Two readings remain, and the commercial difference is large.

| Reading | Effect | Family of four needs |
| :---- | :---- | :---- |
| **Study slot** | Only *n* profiles may be enrolled at all | 4 seats |
| **Viewing slot** | All 6 may enrol and study; only *n* may watch at once | 1–2 seats |

FR-ENR-01 requires "an active subscription with an available seat for that learner", which points at the study-slot reading. FR-AUTH-12 caps concurrent video streams by purchased seats, which points at the viewing-slot reading. Both are in the baseline.

Also undefined: whether a seat can be reassigned between profiles, and any cooldown on doing so. §22.3 risk 5 already names seat sharing as a risk.

Blocks: billing, enrolment, the upgrade prompt in FR-BILL-04, and the per-seat price the client owes.

### OQ-03 — Devices versus seats

FR-AUTH-11 caps devices at 3 per account. FR-AUTH-12 caps concurrent streams by seats purchased, up to 6. A family buying 5 seats cannot use them from 3 devices.

Proposed: keep both limits, apply whichever is lower, and **raise the device allowance as seats are added** rather than holding it flat at 3. Not yet agreed. Selling a seat that cannot be used is the failure to avoid.

---

## Blocking Assessment (Phase 5)

### OQ-04 — Attendance threshold after a dismissed course

Agreed that a course is dismissed when its instructor is suspended or their WWCC expires mid-delivery.

FR-CERT-02 requires ≥70% of sessions attended. If a course ends early, no learner can reach 70% of the originally scheduled sessions, so nobody receives a certificate regardless of attendance.

Proposed: measure against **sessions actually delivered**, not sessions scheduled. Not yet agreed.

Separately, a WWCC expiry should never cause this. FR-INST-03 already gives 60 days' warning, so the system should refuse to schedule sessions beyond an instructor's expiry date — converting a mid-course collapse into a scheduling error caught months earlier. Not in the baseline; would be a change request.

---

## Requiring Change Control (§21.3)

### OQ-05 — Ageing up at 13

Agreed that a learner profile reaching 13 is offered their own account. **This is not in SRD v2.0** and is therefore new scope requiring a change request.

Undefined:

- Does the new account consume a family seat, or free one?
- Who holds the chat toggle afterwards — FR-FAM-08 gives it to the guardian for a 13–17 profile, but FR-AUTH-05 only captures a guardian email for a standalone 13–17 account
- What if the learner declines and stays a profile until 18?
- What migrates — progress, enrolments, certificates — and what does FR-FAM-05's permanent name lock mean once the learner controls their own account?

### OQ-06 — Chat history on profile deletion

Agreed that deleting a profile removes its chat messages. Two problems.

**It contradicts the baseline.** FR-CHAT-14 retains messages on account deletion and anonymises authorship to "Deleted user". A 15-year-old may exist as either an account or a profile, so identical conduct would be preserved or erased depending on which they happen to be.

**It destroys safeguarding evidence.** FR-CHAT-09 and FR-CHAT-10 require moderation actions and reports to be logged and reportable. If a reported message is deleted with the profile, the record of the report and the action taken loses its subject.

Proposed: remove message **content**, retain the moderation record. Not yet agreed.

---

## Client Dependencies (§22.2)

None confirmed as received.

| # | Item | Needed by | Note |
| :---: | :---- | :---- | :---- |
| 1 | Per-seat price | Commerce | Also blocked by OQ-02 |
| 2 | GST treatment for overseas learners | Commerce | From their accountant |
| 3 | Privacy policy, terms, refund policy | Launch | From their lawyer |
| 4 | WWCC position | Instructor onboarding | From their lawyer |
| 5 | Certificate design assets | Assessment | Template, seal, signature |
| 6 | Cloud, Bunny, Stripe, SES accounts | Foundation | **Open now** — no cost to sit idle |
| 7 | Apple and Google developer accounts | Mobile | **Open now** — store review is the least predictable item |
| 8 | Live-class tool choice | Learning | See below |

### On item 8

The baseline already requires "confirmation its terms permit the intended learner ages". Most video conferencing services set a minimum age in their own terms — commonly 13 or 16. The platform teaches from age five.

It is entirely possible the tool the institute chooses does not permit the students they intend to teach on it, and that is not fixable in the platform. Worth resolving before the Learning phase rather than during it.

---

## Baseline Approval

SRD v2.0 is **verbally approved only**. §21.3 measures change requests against an approved baseline; without written approval there is no line between a change and a misunderstanding. §22.3 risk 7 already names contested "done" as a risk, mitigated by acceptance criteria and the 10-day window — both of which assume the baseline itself is agreed.

Raised and noted. No action requested.
