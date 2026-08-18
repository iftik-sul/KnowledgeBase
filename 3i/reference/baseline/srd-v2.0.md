---
project: 3i
type: baseline
status: current
updated: 2026-08-18
version: "2.0"
approval: verbal
original_filename: 3i_International_Islamic_Institute.md
supersedes: 3i_2nd_phase_requirements_final.docx
tags:
  - baseline
  - requirements
---

# **3i International Islamic Institute**

# **Software Requirements Document — Phase 2**

**Version:** 2.0 **Status:** Baseline for development **Supersedes:** `3i_2nd_phase_requirements_final.docx` (v1.0)

---

## **Document control**

This baseline consolidates the original v1.0 requirements with the decisions from five clarification rounds. Where v1.0 and this document conflict, **this document governs**.

Requirements are identified as `FR-<MODULE>-<nn>` (functional) and `NFR-<nn>` (non-functional). Each module carries acceptance criteria used for the sign-off process in §21.

Changes to this baseline after approval follow the change-request process in §21.3.

---

## **Table of contents**

1. Overview and objectives  
2. Scope summary  
3. Identity model — read this first  
4. Users, roles and permissions  
5. Registration and authentication  
6. Family accounts and learner profiles  
7. Instructor onboarding  
8. Course catalogue and management  
9. Course materials and video delivery  
10. Batches and live sessions  
11. Enrolment, waitlist and age gating  
12. Question bank and examinations  
13. Certificates  
14. Subscriptions, billing and waivers  
15. Group chat and moderation  
16. Notifications  
17. Content management, blog and public site  
18. Reports and exports  
19. Localisation  
20. Non-functional requirements  
21. Delivery, acceptance and change control  
22. Assumptions, dependencies and risks  
23. Explicitly out of scope

---

# **1\. Overview and objectives**

## **1.1 Purpose**

A multi-language online learning platform for the 3i International Islamic Institute, serving Australia and an international student base. The platform delivers self-paced and live-taught Islamic studies courses to learners from age 5 upward, under a subscription model.

## **1.2 Build type**

**Greenfield.** No data, users, or content migrate from any earlier system. There is no migration workstream.

## **1.3 Platforms**

| Platform | Technology | Primary purpose |
| ----- | ----- | ----- |
| Web | Next.js | Full platform — public site, learning, admin, **all commerce** |
| iOS | Flutter | Learning only. No purchase surface |
| Android | Flutter | Learning only. No purchase surface |

## **1.4 Primary objectives**

1. Sell auto-renewing subscriptions through the web, with a needs-based waiver scheme.  
2. Deliver self-paced video courses and instructor-led live batches.  
3. Serve learners aged 5–17 safely, under guardian-held accounts.  
4. Issue verifiable certificates for attendance and course completion.  
5. Operate in five languages, including two right-to-left.

---

# **2\. Scope summary**

## **2.1 In scope**

| \# | Module | Notes |
| ----- | ----- | ----- |
| 1 | Registration, authentication, social login | Mandatory email verification |
| 2 | Family accounts and learner profiles | Guardian-held, up to 6 profiles |
| 3 | Role-based access control | Single admin role at launch, extensible |
| 4 | Instructor application and approval | Includes WWCC record |
| 5 | Course catalogue, search, filtering | Age-filtered per learner |
| 6 | Course creation and management | Age tagging mandatory |
| 7 | Video hosting, streaming, offline download | Bunny Stream |
| 8 | Documents, audio, in-browser viewers | No web download |
| 9 | Batches and live session scheduling | Sessions held externally |
| 10 | Manual attendance | Instructor-marked |
| 11 | Enrolment, waitlist, age gating | Guardian override permitted |
| 12 | Progress tracking | Per material, per learner |
| 13 | Question bank | Admin and instructor scopes |
| 14 | Examinations and grading | Auto \+ manual |
| 15 | Certificates with public verification | QR \+ unique code |
| 16 | Subscriptions, seats, Stripe checkout | Web only |
| 17 | Waivers with evidence upload | Four fixed tiers |
| 18 | Refunds | 14-day first-payment window |
| 19 | Group chat with moderation | Text only, group only |
| 20 | Notifications — push, email, in-app centre | Per-category opt-out |
| 21 | Course ratings and reviews | With moderation |
| 22 | CMS, blog, FAQ | Fixed page set |
| 23 | Reports, exports, scheduled delivery | Excel, CSV, PDF |
| 24 | Five-language UI with RTL | Static strings only |
| 25 | Privacy tooling — consent, export, deletion | APP and GDPR |
| 26 | Analytics and crash reporting | GA4, Firebase, Sentry |

## **2.2 Out of scope**

See §23 for the full list with reasoning. Headlines: no data migration, no in-app purchase, no DRM at launch, no multi-instructor courses, no sub-admin roles, no user-content translation, no proctoring, no direct messaging, no SMS, no in-platform live streaming.

---

# **3\. Identity model — read this first**

**This section governs the interpretation of every other section.** The word "student" is not used in this document because it is ambiguous.

## **3.1 The two entities**

| Entity | Definition |
| ----- | ----- |
| **Account (User)** | A login identity. Owns credentials, billing, devices, notifications, chat participation |
| **Learner** | A person who studies. Owns enrolments, progress, attendance, exam attempts, certificates |

**Every account has at least one learner.** An adult studying alone is an account with a single learner. A guardian with three children is one account with three learners. A guardian studying alongside two children is one account with three learners, one flagged as the account holder.

## **3.2 Account types**

| Type | Age | Login | Creates learner profiles | Chat |
| ----- | ----- | ----- | ----- | ----- |
| Adult account holder | 18+ | Yes | Yes, up to 6 | Yes |
| Standalone student | 13–17 | Yes | No | Yes |
| Learner profile | Any, mandatory under 13 | No — profile picker \+ optional PIN | N/A | Under 13: no. 13–17: guardian toggle |

## **3.3 Consequences**

* Under-13s never hold credentials and never log in independently.  
* Under-13s never have an unsupervised communication channel with an adult.  
* The contracting and paying party is always an adult.  
* Academic records attach to learners; commercial and communication records attach to accounts.

---

# **4\. Users, roles and permissions**

## **4.1 Roles at launch**

| Role | Description |
| ----- | ----- |
| **Admin** | Full platform control. Single role at launch |
| **Instructor** | Creates and manages own courses, batches, questions, exams. Grades and marks attendance |
| **Account holder** | Manages profiles, subscription, enrolments. May also be a learner |

## **4.2 Requirements**

* **FR-RBAC-01** Permissions are modelled as discrete keys (`module.action`) assigned to roles, assigned to users. No hard-coded role checks anywhere in the codebase.  
* **FR-RBAC-02** The system ships with three seeded roles. Admin holds every permission.  
* **FR-RBAC-03** Every API route declares the permission key it requires.  
* **FR-RBAC-04** Adding a new role must require no code change — only data.  
* **FR-RBAC-05** Admin accounts support optional TOTP two-factor authentication.

**Acceptance criteria**

* A new role can be created in the database with a subset of permissions and behaves correctly without deployment.  
* No occurrence of `isAdmin`, `role === 'admin'`, or equivalent exists in application logic.  
* Every route returns 403 when the required permission is absent.

---

# **5\. Registration and authentication**

## **5.1 Requirements**

* **FR-AUTH-01** Registration captures first name, last name, email, password, **date of birth**, and locale.  
* **FR-AUTH-02** Date of birth is a real date entry, not an age confirmation checkbox.  
* **FR-AUTH-03** Registration is **blocked** where DOB indicates under 13\. The block message is neutral and does not disclose the threshold in a way that invites retry.  
* **FR-AUTH-04** Blocked attempts are recorded against a hashed session identifier, so a retry with an amended birth year is identifiable as a retry.  
* **FR-AUTH-05** Where DOB indicates 13–17, registration additionally captures **guardian name and guardian email**, and sends the guardian an automatic notification naming the institute and linking to the privacy policy.  
* **FR-AUTH-06** Email verification is **mandatory**. Unverified accounts cannot enrol, subscribe, or participate in chat.  
* **FR-AUTH-07** Social login via Google and Apple. Sign in with Apple is mandatory on iOS given Google is offered. Social accounts still require DOB capture on first login.  
* **FR-AUTH-08** Password policy: minimum 10 characters, no forced composition rules, checked against the Have I Been Pwned corpus via k-anonymity, hashed with Argon2id.  
* **FR-AUTH-09** Five failed attempts trigger a 15-minute lockout, with progressive delay and per-IP rate limiting.  
* **FR-AUTH-10** Password reset tokens are single-use with 30-minute expiry.  
* **FR-AUTH-11** Maximum **3 registered devices** per account. Device swap permitted twice per 30 days. Devices are visible and de-authorisable by the account holder.  
* **FR-AUTH-12** Concurrent video streams are limited to the number of purchased learner seats, minimum one.  
* **FR-AUTH-13** No phone or OTP login.

**Acceptance criteria**

* A DOB of under 13 cannot produce an account by any route, including social login.  
* A 13–17 registration triggers a guardian email, logged with timestamp and address.  
* A fourth device registration is refused with a clear message and a link to device management.  
* An unverified account is blocked from enrolment, checkout, and chat.

---

# **6\. Family accounts and learner profiles**

## **6.1 Requirements**

* **FR-FAM-01** Only an account holder aged 18+ may create learner profiles.  
* **FR-FAM-02** Maximum **6 learner profiles** per account.  
* **FR-FAM-03** A profile carries display name, date of birth, optional avatar, and optional 4-digit PIN. It has no email address and no credentials.  
* **FR-FAM-04** Profile selection occurs after account login via a profile picker.  
* **FR-FAM-05** A profile's name **locks permanently once a certificate has been issued** to it. Admin may unlock on request, with a reason recorded.  
* **FR-FAM-06** Profile creation and deletion are rate-limited to **2 changes per 30 days**.  
* **FR-FAM-07** Profile date of birth is set at creation and is not user-editable. Corrections go through admin.  
* **FR-FAM-08** Chat access is derived from profile age: under 13 is permanently off; 13–17 is a guardian-controlled toggle.  
* **FR-FAM-09** The guardian dashboard shows per-profile progress, enrolments, attendance, exam results, and certificates.  
* **FR-FAM-10** Deleting a profile removes progress, enrolments, and exam results. **Issued certificates remain valid and publicly verifiable.**

**Acceptance criteria**

* A 17-year-old standalone account cannot create profiles.  
* A seventh profile is refused.  
* A renamed profile is refused once a certificate exists, with the reason shown.  
* After profile deletion, the certificate verification URL still resolves correctly.

---

# **7\. Instructor onboarding**

## **7.1 Requirements**

* **FR-INST-01** Instructor applications capture bio, area of expertise, and CV upload.  
* **FR-INST-02** Applications require **admin approval**. Approved instructors gain the instructor role; rejected applicants are notified with a reason and may re-apply.  
* **FR-INST-03** The instructor record captures **Working With Children Check number, issuing state, and expiry date**, with an admin alert 60 days before expiry.  
* **FR-INST-04** An instructor whose WWCC has expired cannot be assigned to, or continue teaching, any course tagged under 18\.  
* **FR-INST-05** Each instructor has a 50 GB storage quota, adjustable by admin.  
* **FR-INST-06** One instructor per course. Course ownership belongs to the assigned instructor.  
* **FR-INST-07** Admin may suspend an instructor. Their published courses become suspended; enrolled learners retain access to completed materials and may join a future batch.

**Acceptance criteria**

* A rejected applicant receives a reason and can submit a new application.  
* An expired WWCC produces an admin alert and blocks assignment to children's courses.  
* Suspending an instructor does not delete learner progress or issued certificates.

---

# **8\. Course catalogue and management**

## **8.1 Course types**

| Type | Structure |
| ----- | ----- |
| **Regular** | Self-paced materials only. No batches |
| **Online Class** | Live sessions only, delivered in batches |
| **Mixed** | Materials plus live batch sessions |

## **8.2 Requirements**

* **FR-CRS-01** Course creation captures title, summary, description, learning outcomes, thumbnail, category, type, level, language, **minimum age (mandatory)**, and optional maximum age.  
* **FR-CRS-02** The age field has **no default**. A course cannot be saved without an explicit choice.  
* **FR-CRS-03** A course cannot be published without an age tag, at least one material or batch, and a thumbnail.  
* **FR-CRS-04** Courses tagged **under 13 require admin approval** before publication. All other courses publish without approval.  
* **FR-CRS-05** Admin may edit, suspend, or take down any course.  
* **FR-CRS-06** Course cards display the age band (5–8, 9–12, 13–15, 16–17, 18+, All ages).  
* **FR-CRS-07** Catalogue search covers title, summary, description, and instructor name, using PostgreSQL full-text search with trigram fuzzy matching.  
* **FR-CRS-08** Filters: category, course type, level, age band, minimum rating, language, has upcoming batch.  
* **FR-CRS-09** Sort: relevance, newest, most enrolled, highest rated, title A–Z.  
* **FR-CRS-10** **When a learner profile is active, the catalogue displays only courses whose age range includes that learner's age.**  
* **FR-CRS-11** Learners may rate a course 1–5 with an optional written review, once per course, only after enrolment. Admin may hide a review.

**Acceptance criteria**

* Saving a course without an age tag is refused.  
* A course tagged minimum age 8 enters pending review rather than publishing.  
* A nine-year-old profile browsing the catalogue sees no 13+ courses.  
* Search returns results for a misspelt instructor name.

---

# **9\. Course materials and video delivery**

## **9.1 Requirements**

* **FR-MAT-01** Material types: video, document, audio, external link. Ordered within a course.  
* **FR-MAT-02** Upload limits: video 4 GB, audio 500 MB, document 100 MB, image 10 MB. Video uses resumable (TUS) upload.  
* **FR-MAT-03** File type is validated server-side by content inspection, not by extension.  
* **FR-MAT-04** Video is hosted on **Bunny Stream**, primary region Sydney, transcoded to adaptive-bitrate HLS.  
* **FR-MAT-05** Video is served exclusively via short-expiry signed token URLs. No permanent URL is ever exposed to a client.  
* **FR-MAT-06** **English caption files are required at video upload.** Admin may trigger paid auto-transcription as a fallback.  
* **FR-MAT-07** On web, documents render in an in-browser viewer. **No download is offered on web** for any material type.  
* **FR-MAT-08** On mobile, materials may be downloaded for offline use, subject to §9.2.  
* **FR-MAT-09** Materials are not admin-moderated before publication, except within courses requiring approval under FR-CRS-04.

## **9.2 Offline protection**

* **FR-MAT-10** Downloads are stored in the app's private sandbox, encrypted with a per-device key held in Keychain or Android Keystore.  
* **FR-MAT-11** Playback decrypts in memory. No plaintext file is written to disk.  
* **FR-MAT-12** Maximum **20 offline items per device**.  
* **FR-MAT-13** Offline content revalidates online at least every **7 days**. On failure, or on subscription lapse, or on device de-authorisation, local content is wiped.  
* **FR-MAT-14** Screen capture is blocked on Android (`FLAG_SECURE`) and detected on iOS with video blanked.  
* **FR-MAT-15** No DRM at launch. The chosen vendor supports Widevine and FairPlay as a later upgrade without migration.

**Acceptance criteria**

* A downloaded video is not visible or playable outside the app on a standard device.  
* Content is wiped when a subscription lapses and the app next reaches the network.  
* A signed video URL fails after expiry.  
* A video cannot be published without a caption file.

---

# **10\. Batches and live sessions**

**Live classes are held outside the platform.** The platform schedules them, distributes links, and records attendance.

## **10.1 Requirements**

* **FR-BAT-01** Batch creation captures name, capacity, number of classes, approximate duration per class, and the date and time of each session.  
* **FR-BAT-02** The instructor posts the meeting link to the batch group chat and, from the platform, by email, ahead of each session.  
* **FR-BAT-03** The instructor marks attendance manually after each session (present / absent / late / excused).  
* **FR-BAT-04** Rescheduling a session notifies all enrolled learners automatically by push and email.  
* **FR-BAT-05** Cancelling a batch notifies enrolled learners, who may join a future batch. No refund is triggered, as access is subscription-based.  
* **FR-BAT-06** A learner may enrol in multiple batches of the same course, including re-joining a later batch.  
* **FR-BAT-07** The instructor sees a batch roster of learner profile names for attendance.

**Acceptance criteria**

* A batch cannot be created without at least one scheduled session.  
* Rescheduling produces both a push and an email to every enrolled account.  
* Attendance saved for one session does not affect other sessions.

---

# **11\. Enrolment, waitlist and age gating**

## **11.1 Requirements**

* **FR-ENR-01** Enrolment requires an active subscription with an available seat for that learner.  
* **FR-ENR-02** Enrolment authority: guardian enrols under-13 profiles; 13–17 profiles default to guardian approval, with a guardian toggle to allow self-enrolment; standalone accounts self-enrol.  
* **FR-ENR-03** A learner cannot enrol in a course whose minimum age exceeds their age.  
* **FR-ENR-04** A guardian may override the age gate **upward by up to 2 years**, with explicit confirmation. Overrides are logged with the approving account and timestamp.  
* **FR-ENR-05** **No override is possible into a course tagged 18+.**  
* **FR-ENR-06** When a batch is at capacity, learners join a **waitlist** with a visible position.  
* **FR-ENR-07** On a cancellation, the first waitlisted learner is notified and auto-promoted. The offer expires after 48 hours and passes to the next in line.

**Acceptance criteria**

* An 11-year-old can be enrolled into a 13+ course with guardian confirmation; the same learner cannot be enrolled into an 18+ course by any route.  
* A waitlisted learner is promoted and notified within one minute of a cancellation.  
* Enrolment fails cleanly when no seat is available, with an upgrade path shown.

---

# **12\. Question bank and examinations**

## **12.1 Question bank**

* **FR-QB-01** Two bank scopes: **admin** and **instructor**.  
* **FR-QB-02** Instructors may view and **copy** admin questions into their own bank. The copy is independent and editable.  
* **FR-QB-03** Instructor questions are private to their owner. They are invisible to other instructors **and to admins**.  
* **FR-QB-04** Isolation is enforced at the query layer. A request for another instructor's bank returns 404, not 403\.  
* **FR-QB-05** Question types: single-answer MCQ, multi-select MCQ, true/false, short answer, essay.  
* **FR-QB-06** Each question carries marks, optional negative marks, optional partial credit, difficulty, and an explanation.  
* **FR-QB-07** Bulk import via CSV/Excel with a downloadable template, row-level validation, and an error report.

## **12.2 Examinations**

* **FR-EX-01** Exam types: practice and final. A course may have many practice exams and one final.  
* **FR-EX-02** Exam configuration: duration, pass mark, maximum attempts, cooldown, optional open and close dates, question and option randomisation.  
* **FR-EX-03** Defaults: 3 attempts with 24-hour cooldown for practice; 3 attempts with 7-day cooldown for finals. The highest score is retained.  
* **FR-EX-04** Timer expiry triggers **auto-submission**. Disconnection mid-attempt results in **forfeiture** of that attempt.  
* **FR-EX-05** Objective questions are auto-graded. Written answers await manual grading by the course instructor, with no service-level commitment.  
* **FR-EX-06** Correct answers and explanations are revealed **only after the learner passes or exhausts all attempts**. An instructor may override this per exam.  
* **FR-EX-07** A learner failing the final exam may retake it within the attempt limit.  
* **FR-EX-08** No proctoring, webcam monitoring, tab-switch detection, or IP checking.

**Acceptance criteria**

* An attempt left open past its duration is submitted automatically with answers preserved.  
* Answers are not revealed after a failed first attempt when attempts remain.  
* An instructor querying another instructor's bank receives 404\.  
* A CSV import of 200 questions reports per-row errors without partial corruption.

---

# **13\. Certificates**

## **13.1 Requirements**

* **FR-CERT-01** Two types: **attendance** and **completion**.

* **FR-CERT-02** Attendance certificate thresholds:

  * Batch courses: **≥70% of sessions attended**.  
  * Regular courses: **≥70% of published materials completed**.  
* **FR-CERT-03** Material completion definitions:

| Type | Complete when |
| ----- | ----- |
| Video | ≥90% of duration watched, cumulative across sessions |
| Audio | ≥90% played |
| Document | Opened in the viewer for ≥30 seconds |
| Quiz/exam | Submitted, regardless of score |

* **FR-CERT-04** The completion certificate is issued after the final exam is passed.

* **FR-CERT-05** Certificates are **English only**, regardless of user locale.

* **FR-CERT-06** Each certificate carries a unique verification code, a QR code, the institute seal, and a digital signature image.

* **FR-CERT-07** A **public verification page** resolves a verification code to learner name, course title, type, and issue date. No authentication required.

* **FR-CERT-08** Learner name and course title are **snapshotted at issue**. Certificates remain valid and verifiable after profile deletion, account deletion, or course archival.

* **FR-CERT-09** Admin may revoke a certificate with a recorded reason. Revoked certificates show as revoked on the verification page.

**Acceptance criteria**

* A learner at 69% attendance cannot obtain a certificate; at 70% they can.  
* The QR code on a generated PDF resolves to the correct verification page.  
* Verification still works after the learner profile is deleted.  
* Certificates render Arabic and Bengali names correctly in the PDF.

---

# **14\. Subscriptions, billing and waivers**

## **14.1 Commercial model**

| Item | Value |
| ----- | ----- |
| Plans | Monthly and annual, auto-renewing |
| Price | AUD $9.99/month, AUD $99.99/year, **GST-inclusive** |
| Included | One learner seat |
| Additional seats | Per-seat monthly charge (price to be confirmed), maximum 6 profiles |
| Free trial | None |
| Payment rail | **Stripe, web checkout only** |
| Revenue sharing | None |

## **14.2 Requirements**

* **FR-BILL-01** All purchase, plan change, payment method, cancellation, and invoice functionality lives on the **web**. The Stripe Customer Portal handles payment methods and cancellation.  
* **FR-BILL-02** **The mobile apps contain no purchase surface.** No prices, no subscribe or upgrade buttons, no links to checkout, no text directing users to pay elsewhere. See §20.6.  
* **FR-BILL-03** Access is granted from **Stripe webhooks only**, never from a client-side success redirect. Webhook handling is signature-verified and idempotent.  
* **FR-BILL-04** Seat count is a Stripe quantity. Adding a profile beyond the purchased seats prompts a seat purchase.  
* **FR-BILL-05** The **billing contact is separable from the account identity** — name and email on the Stripe customer may differ from the account holder's. For accounts with minor profiles, the billing contact defaults to the guardian.  
* **FR-BILL-06** Failed payments use Stripe Smart Retries plus a platform email sequence. Access is suspended at final failure.  
* **FR-BILL-07** Prices are stored and displayed GST-inclusive, in integer cents.  
* **FR-BILL-08** Invoices record GST separately for reporting.

## **14.3 Waivers**

* **FR-WAV-01** An account holder submits a waiver request with a written explanation and **optional file uploads** as supporting evidence.  
* **FR-WAV-02** Admin approves at one of four fixed tiers: **25%, 50%, 75%, 100%**.  
* **FR-WAV-03** An approved waiver takes effect **at the next renewal**. No mid-cycle proration.  
* **FR-WAV-04** A waiver runs **12 months**, after which the account holder may re-apply.  
* **FR-WAV-05** Admin may revoke an active waiver. The account holder is notified by email and push, and full price resumes at the next billing date.  
* **FR-WAV-06** A 100% waiver produces a live subscription with a 100% discount — **not** a flagged free account. Admin-created free accounts are a separate mechanism.  
* **FR-WAV-07** Waiver evidence files are stored in a private bucket, never CDN-cached, accessed only via short-lived signed URLs, with every access logged.  
* **FR-WAV-08** Waiver evidence is **automatically deleted 12 months after the decision**.  
* **FR-WAV-09** Full audit trail: requester, submission, reviewer, decision, tier, effective and expiry dates, revocation and reason.

## **14.4 Refunds**

* **FR-REF-01** **14-day full refund** on a first subscription payment, requested self-service.  
* **FR-REF-02** Renewal payments are refundable at admin discretion only.  
* **FR-REF-03** Access is revoked immediately on refund.  
* **FR-REF-04** Certificates already issued remain valid.  
* **FR-REF-05** The published policy acknowledges that Australian Consumer Law guarantees apply regardless of policy terms.

**Acceptance criteria**

* No screen, string, or asset in either mobile app references price or purchase.  
* A subscription created in Stripe grants access only after the webhook is processed.  
* A 100% waiver produces an active subscription visible in Stripe with a zero invoice.  
* Waiver evidence files are unreachable without a signed URL and are purged after 12 months.

---

# **15\. Group chat and moderation**

## **15.1 Structure**

| Course type | Chat scope |
| ----- | ----- |
| Regular | One room per course |
| Online Class / Mixed | One room per **batch** |

## **15.2 Requirements**

* **FR-CHAT-01** Real-time delivery over WebSocket. Messages persist to PostgreSQL.  
* **FR-CHAT-02** **Text only.** No image, file, or media sharing.  
* **FR-CHAT-03** **Group only.** No direct or 1:1 messaging anywhere in the platform.  
* **FR-CHAT-04** Flat structure — no announcement-only mode.  
* **FR-CHAT-05** Message history is retained indefinitely and is searchable.  
* **FR-CHAT-06** **Under-13 learners have no chat access.** The guardian participates on the child's behalf, displayed as *"Fatima (guardian of Aisha)"*.  
* **FR-CHAT-07** Where a course's minimum age is under 13, the room is automatically set to guardian-only mode. This is derived from the age tag, not configured by the instructor.  
* **FR-CHAT-08** 13–17 learners participate directly, subject to the guardian toggle.  
* **FR-CHAT-09** Instructor and admin may delete messages, mute participants, and remove participants. All moderation actions are logged.  
* **FR-CHAT-10** Any participant may report a message. Reports enter an admin moderation queue with a **24-hour response target**, tracked and reportable.  
* **FR-CHAT-11** A server-side **profanity and content filter** runs on send, across all five languages, including link scanning. Filtered messages are withheld and flagged.  
* **FR-CHAT-12** Chat logs are auditable by admin across all rooms, not only by the owning instructor.  
* **FR-CHAT-13** Instructor or admin may close a room. Closed rooms become **read-only archives**, never hidden.  
* **FR-CHAT-14** On account deletion, message authorship is anonymised to "Deleted user". Messages are retained.  
* **FR-CHAT-15** A **safety contact** is published in-app and on the website.

**Acceptance criteria**

* No API route exists that creates a two-participant private room.  
* A course tagged minimum age 8 produces a guardian-only room without instructor action.  
* A reported message appears in the admin queue with an SLA countdown.  
* An overdue-reports figure is visible on the admin dashboard.

---

# **16\. Notifications**

## **16.1 Requirements**

* **FR-NOT-01** Channels: **push and email**. No SMS.  
* **FR-NOT-02** An **in-app notification centre** retains history with read/unread state.  
* **FR-NOT-03** Per-category opt-out, at account level.  
* **FR-NOT-04** Notifications route to the **account holder**. Where a notification concerns a learner profile, the profile is named in the body — *"Aisha has completed Level 2 Tajweed"*.  
* **FR-NOT-05** Notification language follows the account's locale preference.  
* **FR-NOT-06** **Push notifications must not contain purchase prompts or links to checkout.** Expiry notices state that access has ended and that the account can be managed on the website, without a link.  
* **FR-NOT-07** Email is sent via AWS SES (Sydney) with SPF, DKIM, and DMARC configured on the institute's domain.  
* **FR-NOT-08** Delivery, bounce, and complaint events are logged.

## **16.2 Triggers**

Account verification, guardian notification, instructor approval or rejection, enrolment confirmation, batch scheduling and rescheduling, meeting link distribution, waitlist promotion, exam availability, grading completion, certificate issue, payment success and failure, subscription expiry, waiver decision and revocation, chat mention, moderation action.

**Acceptance criteria**

* Opting out of a category stops both push and email for that category only.  
* A subscription expiry push contains no URL and no price.  
* Bounces are visible in the admin email log.

---

# **17\. Content management, blog and public site**

## **17.1 Requirements**

* **FR-CMS-01** A **fixed page set** — home, about, contact, FAQ, terms, privacy policy, refund policy, safety. Not a general page builder.  
* **FR-CMS-02** A **blog/news module** with posts, categories, cover images, scheduling, and SEO fields.  
* **FR-CMS-03** CMS content is **not** multi-language and is not machine-translated.  
* **FR-CMS-04** Public pages are server-rendered (SSR/ISR) for SEO.  
* **FR-CMS-05** Structured data: `Course`, `Organization`, `FAQPage`, `BreadcrumbList`, `Article`.  
* **FR-CMS-06** `hreflang` across all five locales, canonical URLs, locale-prefixed routes, auto-generated sitemap and robots files, Open Graph and Twitter cards.  
* **FR-CMS-07** Authenticated areas are client-rendered and `noindex`.

**Acceptance criteria**

* A published course page returns full HTML content to a crawler without JavaScript execution.  
* The sitemap includes all published courses and blog posts and excludes authenticated routes.

---

# **18\. Reports and exports**

## **18.1 Requirements**

* **FR-REP-01** Reports: learner activity, course performance, enrolment, attendance, exam results, certificates issued, revenue (gross), subscription and churn, waivers granted, moderation and reports handled, instructor activity.  
* **FR-REP-02** Export formats: **Excel, CSV, PDF**.  
* **FR-REP-03** **Scheduled reports** delivered by email on a recurring schedule to nominated recipients.  
* **FR-REP-04** Report generation runs as a background job; large exports do not block the UI.  
* **FR-REP-05** Revenue reporting is gross platform revenue, GST separated.

**Acceptance criteria**

* A scheduled weekly report arrives by email with the correct attachment format.  
* A 50,000-row export completes without timing out the request.

---

# **19\. Localisation**

## **19.1 Requirements**

* **FR-LOC-01** Supported locales: **English, Bangla, Hindi, Urdu, Arabic**.  
* **FR-LOC-02** **Static UI strings only** are translated. Translations are AI-generated and stored, editable by admin.  
* **FR-LOC-03** **User-generated content is never translated** — course titles, descriptions, materials, exam questions, chat, reviews, and CMS content all remain as authored.  
* **FR-LOC-04** **Full RTL layout mirroring** for Arabic and Urdu across web and both mobile apps — not merely character rendering.  
* **FR-LOC-05** Notifications and emails follow the account's locale.  
* **FR-LOC-06** Certificates are always English.

**Acceptance criteria**

* Switching to Arabic mirrors navigation, alignment, icon direction, and progress indicators.  
* No user-authored string passes through a translation service.  
* An admin can correct a machine translation without a deployment.

---

# **20\. Non-functional requirements**

## **20.1 Technology**

| Layer | Choice |
| ----- | ----- |
| Backend | Node.js |
| Database | PostgreSQL |
| Cache, queues, WebSocket adapter | Redis |
| Web | Next.js |
| Mobile | Flutter |
| Video | Bunny Stream (Sydney primary) |
| Object storage | DigitalOcean Spaces |
| Email | AWS SES (Sydney) / Resend |
| Payments | Stripe |
| Hosting | DigitalOcean SYD1, containerised, load-balanced |

## **20.2 Capacity baseline**

| Metric | Launch | Month 12 |
| ----- | ----- | ----- |
| Registered accounts | 500 | 5,000 |
| Active subscribers | 200 | 2,000 |
| Peak concurrent users | 100 | 500 |
| Instructors | 20 | 100 |
| Published courses | 30 | 200 |
| Video library | 100 h | 400 h |

## **20.3 Availability and recovery**

* **NFR-01** Uptime target **99.5%**, excluding announced maintenance.  
* **NFR-02** Daily automated PostgreSQL backups, 30-day retention, point-in-time recovery.  
* **NFR-03** **RPO 24 hours, RTO 8 hours.**  
* **NFR-04** Restore tested at handover and quarterly thereafter.  
* **NFR-05** Uptime monitoring, error tracking (Sentry), and alerting from day one.

## **20.4 Security**

* **NFR-06** All data in transit over TLS. All data at rest encrypted.  
* **NFR-07** All data resident in **Sydney**.  
* **NFR-08** Rate limiting on authentication, enrolment, and upload endpoints.  
* **NFR-09** Audit logging of all administrative and financial actions.  
* **NFR-10** Sensitive uploads (waiver evidence, CVs, WWCC data) are private-bucket only.  
* **NFR-11** OWASP Top 10 addressed; dependency scanning in CI.

## **20.5 Accessibility and compatibility**

* **NFR-12** **WCAG 2.2 Level AA** on public and learner-facing web: semantic HTML, keyboard navigation, visible focus, 4.5:1 contrast, labelled forms, alt text, captions on video, reduced-motion support.  
* **NFR-13** Browsers: current and previous major versions of Chrome, Edge, Safari, Firefox.  
* **NFR-14** **Android 8.0 (API 26)+**, **iOS 14+**.

## **20.6 App store compliance**

* **NFR-15** Apps are submitted under the **multiplatform services** model: the web platform is primary, the apps are companions for content the learner already has access to.  
* **NFR-16** No purchase surface of any kind (see FR-BILL-02).  
* **NFR-17** Registration is **web-first**. The apps offer login only, with a plain "Register on our website" line carrying **no link**.  
* **NFR-18** An account without an active subscription sees a neutral status message and a support email address only — no URL, no price, no call to action.  
* **NFR-19** Age rating **13+** on both stores, developer-assigned to match the terms of service.  
* **NFR-20** Store listings and marketing copy address **parents**, not children, to avoid the Families/Kids programmes and their SDK restrictions.  
* **NFR-21** Review submissions include demo credentials for an account with an active subscription.

## **20.7 Privacy and compliance**

* **NFR-22** Compliant with the **Australian Privacy Act 1988 and the Australian Privacy Principles**; **GDPR** where EU/UK learners are enrolled.  
* **NFR-23** Consent banner for analytics, **defaulting to off** for non-essential categories.  
* **NFR-24** Self-service **data export** and **account deletion** in the account profile.  
* **NFR-25** Analytics: GA4, Firebase, Sentry — with **Google Signals and all ads-personalisation disabled**, ad ID collection disabled, and no advertising SDKs.  
* **NFR-26** Documented retention periods for every personal data category.  
* **NFR-27** A written **social media minimum age self-assessment** is produced as a project deliverable, to be reviewed by the client's lawyer and re-run whenever social features change.

## **20.8 Performance**

* **NFR-28** Public pages: Largest Contentful Paint under 2.5s on a median mobile connection.  
* **NFR-29** API p95 response under 400ms excluding video and file transfer.  
* **NFR-30** Video start time under 3s on a 5 Mbps connection.  
* **NFR-31** Adaptive bitrate rendition switching without playback interruption.

---

# **21\. Delivery, acceptance and change control**

## **21.1 Suggested module sequence**

| Phase | Modules |
| ----- | ----- |
| **1\. Foundation** | RBAC, identity, registration, age gate, family accounts, email |
| **2\. Commerce** | Stripe, seats, subscriptions, waivers, refunds |
| **3\. Catalogue** | Courses, materials, Bunny integration, catalogue, age filtering |
| **4\. Learning** | Enrolment, progress, batches, attendance, waitlist |
| **5\. Assessment** | Question bank, exams, grading, certificates |
| **6\. Communication** | Chat, moderation, notifications |
| **7\. Surface** | CMS, blog, SEO, reports, exports, admin panel |
| **8\. Mobile** | Flutter apps, offline, store submission |
| **9\. Hardening** | Accessibility, RTL QA, performance, security review |

Commerce sits early because the app store submission strategy depends on it and store review is the least predictable part of the schedule.

## **21.2 Acceptance**

* Each module is delivered against the acceptance criteria in this document.  
* The client has a **10 working-day review window** per module.  
* Issues raised within the window are fixed. Issues raised after the window are change requests.  
* There is no separate formal UAT phase.

## **21.3 Change control**

Changes to this baseline are logged with a description, affected requirements, impact on timeline and cost, and written approval before work begins.

## **21.4 Handover**

* Source code in a GitHub organisation, ownership transferred on completion.  
* Apps published to client-owned Apple and Google accounts.  
* Infrastructure, Bunny, and Stripe accounts owned and paid for by the client.  
* Documentation: deployment guide, environment variables, backup and restore runbook, admin user guide.

---

# **22\. Assumptions, dependencies and risks**

## **22.1 Assumptions**

1. AUD $9.99 and $99.99 are GST-inclusive; per-seat price to be confirmed.  
2. The capacity baseline in §20.2 holds. Materially higher usage changes infrastructure sizing.  
3. The client supplies the certificate template, institute seal, signature image, and brand assets.  
4. The client supplies the privacy policy, terms of service, and refund policy, drafted by their lawyer.  
5. Instructors supply English caption files with video uploads.  
6. Live classes are delivered on an external tool procured by the client.

## **22.2 Dependencies on the client**

| \# | Item | Needed by |
| ----- | ----- | ----- |
| 1 | Per-seat price confirmation | Before commerce phase |
| 2 | GST treatment for overseas learners, from their accountant | Before commerce phase |
| 3 | Privacy policy, terms, refund policy | Before launch |
| 4 | WWCC position, from their lawyer | Before instructor onboarding |
| 5 | Certificate design assets | Before assessment phase |
| 6 | Cloud, Bunny, Stripe, SES accounts | Before foundation phase |
| 7 | Apple and Google developer accounts | Before mobile phase |
| 8 | Choice of live-class tool, and confirmation its terms permit the intended learner ages | Before learning phase |

## **22.3 Risks**

| \# | Risk | Mitigation |
| ----- | ----- | ----- |
| 1 | **App store rejection under Guideline 3.1.1.** The no-purchase-surface model is the highest-uncertainty item in the plan | Design to NFR-15–21 from the start; budget 1–2 weeks of review buffer; prepare multiplatform-services documentation |
| 2 | Multilingual profanity filtering produces false positives on religious vocabulary | Budget tuning time; admin override on filtered messages |
| 3 | Instructors omit caption files, blocking WCAG AA | Enforce at upload; paid auto-transcription fallback |
| 4 | Offline protection without DRM is defeated | Accepted; deters casual sharing; DRM upgrade path preserved with no vendor change |
| 5 | Seat model encourages profile sharing | Profile cap, name lock on certificate, change rate limits |
| 6 | Content re-entry by instructors delays launch after software completion | Bulk question import provided; recommend content loading begins during phase 5 |
| 7 | No formal UAT phase means "done" is contested | Acceptance criteria in this document plus the 10-day window |

---

# **23\. Explicitly out of scope**

| \# | Item | Reason |
| ----- | ----- | ----- |
| 1 | Data migration from any prior system | Greenfield build |
| 2 | In-app purchase (StoreKit, Play Billing) | Web-only checkout model |
| 3 | Studio-grade DRM (Widevine, FairPlay) | Deferred; upgrade path preserved |
| 4 | Multi-instructor or co-taught courses | One instructor per course |
| 5 | Sub-admin roles and permission matrix | Deferred. RBAC foundation is built |
| 6 | Translation of user-generated content | Explicitly excluded |
| 7 | Translation of exam questions | Assessment integrity |
| 8 | Multi-language CMS content | Explicitly excluded |
| 9 | Proctoring, webcam monitoring, tab-switch detection | Explicitly excluded |
| 10 | Direct or 1:1 messaging | Child-safety design decision |
| 11 | Image or file sharing in chat | Child-safety design decision |
| 12 | SMS notifications | Explicitly excluded |
| 13 | Live streaming inside the platform | Sessions held externally |
| 14 | Session recording and replay | Not requested |
| 15 | Course prerequisites or sequencing | Explicitly excluded |
| 16 | Revenue sharing with instructors | No revenue share |
| 17 | Flexible CMS page builder | Fixed page set |
| 18 | Elasticsearch | PostgreSQL FTS sufficient at this scale |
| 19 | Under-13 independent accounts | Family account model instead |
| 20 | Formal UAT phase | Replaced by per-module review window |
| 21 | Ongoing maintenance and support | Separate agreement |

---

**End of baseline.** Anything not described in this document is not in scope. Additions follow §21.3.
