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

## Resolved

### ~~OQ-01 — Module partition~~ — Settled 2026-08-18

Thirteen modules, recorded in [project-standards.md](project-standards.md#modules). All 19 requirement codes and the 32 NFRs are covered. Module abbreviations assigned for document IDs, chosen not to collide with any requirement code. `project-standards.md` is now `current`, so document IDs may be assigned and `modules/` may be populated.

Raised in the same pass: `app-store-compliance.md` is needed as a second cross-cutting document. See OQ-09.

### ~~OQ-02 — What a seat actually is~~ — Resolved as [3I-DEC-009](decisions/dec-009-seats-as-account-pool.md)

A seat is a permanent, non-transferable enrolment grant to one profile — the study-slot reading, not viewing-slot. FR-AUTH-12's concurrency cap is satisfied automatically as a consequence, not enforced separately. A seat cannot be reassigned between profiles; cancelling deactivates the profile (history preserved) and reactivation requires a fresh payment. FR-FAM-02's six-profile cap is retained.

This also resolves the seat side of [OQ-05](#oq-05--ageing-up-at-13) below, and raises [OQ-08](#oq-08--do-inactive-profiles-count-against-the-six-profile-cap).

---

## Blocking Documentation

### OQ-09 — `app-store-compliance.md` not yet written

FR-BILL-02 forbids any purchase surface in the apps. FR-NOT-06 forbids purchase prompts in push notifications. NFR-15 through NFR-21 govern the multiplatform-services submission model, web-first registration, and the 13+ age rating. That is one rule enforced across `commerce`, `communication`, and `platform`.

§22.3 risk 1 names store rejection under Guideline 3.1.1 as **the highest-uncertainty item in the entire plan**, with 1–2 weeks of review buffer budgeted.

It qualifies for the same treatment as [age-and-safeguarding.md](age-and-safeguarding.md): documented once at project root, linked from the three modules, never restated. Should be written before the Commerce phase rather than during it.

---

## Blocking Commerce (Phase 2)

### OQ-07 — Per-seat price, now that the seat model is settled

With seats defined as permanent per-profile grants rather than shared viewing slots, the client's outstanding per-seat price (§22.2 item 1) can now be quoted against a concrete model — a family of four genuinely needs four seats, not one or two. This was blocked by OQ-02; it no longer is. **This is now the priority client ask.**

### OQ-08 — Do inactive profiles count against the six-profile cap?

[3I-DEC-009](decisions/dec-009-seats-as-account-pool.md) introduces a profile state the baseline does not have: inactive but preserved. FR-FAM-02 caps profiles at six. The interaction is unresolved.

If inactive profiles occupy cap slots, a guardian who has cycled through six children's profiles over several years has a full account, and **the only way to add a seventh is to delete one** — destroying that child's progress and exam results (FR-FAM-10), with only snapshotted certificates surviving. Forcing a parent to erase one child's learning history to enrol another is a bad outcome to arrive at by accident.

Three options, none chosen:

| Option | Effect |
| :---- | :---- |
| Count only **active** profiles against the cap | Six paying seats maximum; inactive history accumulates freely |
| Raise the cap | Defers the problem rather than solving it |
| Keep as-is, make the deletion consequence explicit in the UI | Cheapest, but the parent still loses history |

Blocks: the guardian dashboard (FR-FAM-09), profile picker (FR-FAM-04), and the seat purchase prompt (FR-BILL-04).

### OQ-03 — Devices versus seats

FR-AUTH-11 caps devices at 3 per account. FR-AUTH-12 caps concurrent streams by seats purchased, up to the six-profile ceiling. A family buying 5 seats cannot use them from 3 devices.

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

The seat mechanism is now resolved — see [3I-DEC-009](decisions/dec-009-seats-as-account-pool.md) and [3I-DEC-008](decisions/dec-008-ageing-up-at-13.md). Still undefined:

- Who pays for the new standalone account — the teenager, or does the guardian's payment carry over? Commercial question, not yet decided.
- Who holds the chat toggle afterwards — FR-FAM-08 gives it to the guardian for a 13–17 profile, but FR-AUTH-05 only captures a guardian email for a standalone 13–17 account
- What if the learner declines and stays a profile until 18? Now clearly supported — the profile simply remains active with its seat, no forced transition.
- Should the new standalone account show the old profile's history, or start blank? The history itself is preserved regardless (DEC-009); this is about what the new account surfaces.

### OQ-06 — Chat history on profile deletion

Agreed that deleting a profile removes its chat messages. Two problems.

**It contradicts the baseline.** FR-CHAT-14 retains messages on account deletion and anonymises authorship to "Deleted user". A 15-year-old may exist as either an account or a profile, so identical conduct would be preserved or erased depending on which they happen to be.

**It destroys safeguarding evidence.** FR-CHAT-09 and FR-CHAT-10 require moderation actions and reports to be logged and reportable. If a reported message is deleted with the profile, the record of the report and the action taken loses its subject.

Proposed: remove message **content**, retain the moderation record. Not yet agreed.

This now matters more than it did. With the six-profile cap retained and inactive profiles possibly occupying slots (OQ-08), deletion becomes the routine way to free a slot rather than a rare action — so whatever deletion does to chat history will happen often, not occasionally.

---

## Client Dependencies (§22.2)

None confirmed as received.

| # | Item | Needed by | Note |
| :---: | :---- | :---- | :---- |
| 1 | Per-seat price | Commerce | **Unblocked** — see OQ-07. Now the priority ask |
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
