---
project: 3i
type: standard
status: current
updated: 2026-08-18
tags:
  - safeguarding
  - age-gating
  - cross-cutting
---

# Age and Safeguarding

**This is the authoritative statement of every age-dependent rule in 3i.** Modules link here. They do not restate these rules, because a restated rule goes stale silently and a stale rule here is a safeguarding failure rather than a defect.

The rules are scattered across six requirement codes in the baseline — AUTH, FAM, CRS, ENR, CHAT, INST — and no single section of SRD v2.0 states them together. This document does.

---

## 1. What Age Determines

Age is not a profile attribute. It determines whether an account may exist, who may enrol, who may speak, which courses may be published, and which instructors may teach.

| Age | Account | Chat | Enrolment authority |
| :---- | :---- | :---- | :---- |
| **Under 13** | **Cannot register by any route** (FR-AUTH-03). Exists only as a learner profile under a guardian account | **Permanently none** (FR-FAM-08, FR-CHAT-06). Guardian participates on their behalf | Guardian enrols (FR-ENR-02) |
| **13–17** | May register standalone, **or** exist as a profile | Guardian-controlled toggle (FR-FAM-08, FR-CHAT-08) | Guardian approval by default; guardian toggle permits self-enrolment (FR-ENR-02) |
| **18+** | Full account. **Only 18+ may create learner profiles** (FR-FAM-01) | Unrestricted | Self-enrols |

Under-13 independent accounts are explicitly out of scope (§23 item 19). The family account model replaces them.

---

## 2. Registration

- Date of birth is a **real date entry, not an age checkbox** (FR-AUTH-02).
- An under-13 date of birth **blocks registration by any route, including social login** (FR-AUTH-03, acceptance criteria §5).
- The block message is neutral and does not disclose the threshold in a way that invites retry (FR-AUTH-03).
- Blocked attempts are recorded against a hashed session identifier, so a retry with an amended birth year is identifiable as a retry (FR-AUTH-04).
- A 13–17 registration additionally captures **guardian name and guardian email**, and sends the guardian an automatic notification naming the institute and linking to the privacy policy (FR-AUTH-05).
- Social login still requires date of birth capture on first login (FR-AUTH-07).

---

## 3. Learner Profiles

- Maximum **6 profiles** per account (FR-FAM-02).
- A profile has **no email address and no credentials** (FR-FAM-03).
- Profile date of birth is set at creation and is **not user-editable**. Corrections go through admin (FR-FAM-07).
- Profile creation and deletion are rate-limited to **2 changes per 30 days** (FR-FAM-06).
- A profile name **locks permanently once a certificate has been issued** to it (FR-FAM-05).

The non-editable date of birth is a safeguarding control, not a convenience. It is what prevents a chat restriction being lifted by editing a field.

---

## 4. Course Age Tagging

- Minimum age is **mandatory with no default**. A course cannot be saved without an explicit choice (FR-CRS-01, FR-CRS-02).
- A course cannot be published without an age tag (FR-CRS-03).
- Courses tagged **under 13 require admin approval** before publication. All others publish without approval (FR-CRS-04).
- Age bands displayed on course cards: **5–8, 9–12, 13–15, 16–17, 18+, All ages** (FR-CRS-06).
- **When a learner profile is active, the catalogue displays only courses whose age range includes that learner's age** (FR-CRS-10).

---

## 5. The Enrolment Override

- A learner cannot enrol in a course whose minimum age exceeds their age (FR-ENR-03).
- A guardian may override **upward by up to 2 years**, with explicit confirmation. Overrides are logged with the approving account and timestamp (FR-ENR-04).
- **No override is possible into a course tagged 18+, by any route** (FR-ENR-05).

### Known consequence — confirmed intended

An overridden under-13 learner in a 13+ course has **no route into the discussion at all**. Their own chat access is permanently off, and the room is not set to guardian-only because that is derived from the course's age tag, which is 13+.

The guardian cannot speak on their behalf either, because guardian-on-behalf participation exists only in guardian-only rooms.

Live sessions are unaffected — meeting links are distributed by email as well as to the room (FR-BAT-02). Confirmed as intended, 2026-08-18. Recorded here so it is not later mistaken for a defect.

---

## 6. Chat

- **Group only. No direct or 1:1 messaging anywhere in the platform** (FR-CHAT-03, §23 item 10). The acceptance criterion is that no API route exists that creates a two-participant private room.
- **Text only. No image, file, or media sharing** (FR-CHAT-02, §23 item 11).
- Where a course's minimum age is under 13, the room is **automatically guardian-only, derived from the age tag and not configurable by the instructor** (FR-CHAT-07).
- A guardian speaking for a child is displayed as *"Fatima (guardian of Aisha)"* — never as the child (FR-CHAT-06).
- A server-side profanity and content filter runs on send **across all five languages**, including link scanning (FR-CHAT-11).
- Reports enter an admin moderation queue with a **24-hour response target**, tracked and reportable, with an overdue figure on the admin dashboard (FR-CHAT-10).
- Admin may audit chat logs **across all rooms**, not only those of the owning instructor (FR-CHAT-12).
- Closed rooms become **read-only archives, never hidden** (FR-CHAT-13).
- A **safety contact** is published in-app and on the website (FR-CHAT-15).

Both exclusions above are recorded in the baseline as child-safety design decisions, not as deferred features. They are not candidates for later addition without a safeguarding review.

§22.3 risk 2: multilingual profanity filtering is expected to produce false positives on religious vocabulary. Tuning time is budgeted and admin override on filtered messages is provided.

---

## 7. Instructors

- The instructor record captures **Working With Children Check number, issuing state, and expiry date** (FR-INST-03).
- Admin is alerted **60 days before expiry** (FR-INST-03).
- An instructor whose WWCC has expired **cannot be assigned to, or continue teaching, any course tagged under 18** (FR-INST-04).
- Applications require admin approval before the instructor role is granted (FR-INST-02).
- WWCC data is private-bucket only (NFR-10).

The client's legal position on WWCC is outstanding (§22.2 item 4) and is needed before instructor onboarding is built.

---

## 8. Store and Marketing

- Age rating **13+ on both stores**, developer-assigned to match the terms of service (NFR-19).
- Store listings and marketing copy address **parents, not children**, deliberately avoiding the Families and Kids programmes and their SDK restrictions (NFR-20).
- A written **social media minimum age self-assessment** is a project deliverable, reviewed by the client's lawyer and **re-run whenever social features change** (NFR-27).

Note the tension worth holding: the store rating is 13+ and marketing addresses parents, while the platform teaches five-year-olds. That is coherent — the account holder is an adult and the apps are companions — but it means any change making the apps child-facing invalidates both the rating and the self-assessment.

---

## 9. Privacy

- Australian Privacy Act 1988 and the Australian Privacy Principles; GDPR where EU or UK learners enrol (NFR-22).
- Self-service data export and account deletion (NFR-24).
- Documented retention periods for every personal data category (NFR-26).
- Analytics run with **Google Signals and all ads-personalisation disabled**, ad ID collection disabled, and **no advertising SDKs** (NFR-25).
- Consent banner defaults to **off** for non-essential categories (NFR-23).

---

## 10. Open

See [open-questions.md](open-questions.md). The safeguarding-relevant items are:

- **Ageing up at 13** — agreed the learner is offered their own account. Not in the baseline; requires a change request under §21.3, and the chat permission handover is undefined.
- **Chat history on profile deletion** — agreed messages are removed, which conflicts with FR-CHAT-14 and would destroy moderation evidence.
