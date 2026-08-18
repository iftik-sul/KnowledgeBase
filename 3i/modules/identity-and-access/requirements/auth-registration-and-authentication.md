---
project: 3i
module: identity-and-access
type: requirements
status: current
updated: 2026-08-18
id: 3I-IDA-REQ-001
derived_from:
  - 3i/reference/baseline/srd-v2.0.md
tags:
  - requirements
  - auth
---

# Registration and Authentication

Baseline §5. Thirteen requirements.

The age gate in FR-AUTH-03 to FR-AUTH-05 is the safeguarding boundary of the entire platform. Every rule touching age is consolidated in [age-and-safeguarding.md](/3i/age-and-safeguarding.md); this document covers the registration mechanics only.

---

## Registration

| ID | Requirement |
| :---- | :---- |
| **FR-AUTH-01** | Registration captures first name, last name, email, password, **date of birth**, and locale |
| **FR-AUTH-02** | Date of birth is a real date entry, **not an age confirmation checkbox** |
| **FR-AUTH-03** | Registration is **blocked** where DOB indicates under 13. The block message is neutral and does not disclose the threshold in a way that invites retry |
| **FR-AUTH-04** | Blocked attempts are recorded against a hashed session identifier, so a retry with an amended birth year is identifiable as a retry |
| **FR-AUTH-05** | Where DOB indicates 13–17, registration additionally captures **guardian name and guardian email**, and sends the guardian an automatic notification naming the institute and linking to the privacy policy |
| **FR-AUTH-06** | Email verification is **mandatory**. Unverified accounts cannot enrol, subscribe, or participate in chat |
| **FR-AUTH-07** | Social login via Google and Apple. Sign in with Apple is mandatory on iOS given Google is offered. Social accounts still require DOB capture on first login |

**On FR-AUTH-02 and FR-AUTH-03 together.** A checkbox asks the user to assert their age; a date asks them to state it. The difference matters because FR-AUTH-04 needs a value to compare against on retry — a checkbox produces nothing to detect a second attempt with.

**On FR-AUTH-03's neutral message.** The requirement is that the block does not teach the user how to defeat it. "You must be 13 or over" invites an amended birth year; a neutral refusal does not. FR-AUTH-04 catches the retry either way, but the message should not be the thing that prompts it. **This message is exempt from AI translation** — [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) — since a mistranslation either invites a retry or reads as an accusation, in languages the build team cannot check.

**On FR-AUTH-07.** The social login path is the one most likely to leak an under-13 account, because the provider supplies a verified identity and it is tempting to trust it. The acceptance criterion is explicit that under-13 cannot produce an account **by any route, including social login** — DOB capture on first login is not optional.

### Email changes require re-verification

Not stated in the baseline, settled in review: changing the email on an account triggers the same mandatory-verification path as FR-AUTH-06 requires at registration. The account keeps its prior verified state — and full platform access — until the new address confirms; verification does not retroactively unverify the account mid-change.

---

## Credentials

| ID | Requirement |
| :---- | :---- |
| **FR-AUTH-08** | Password policy: minimum 10 characters, **no forced composition rules**, checked against the Have I Been Pwned corpus via k-anonymity, hashed with Argon2id |
| **FR-AUTH-09** | Five failed attempts trigger a 15-minute lockout, with progressive delay and per-IP rate limiting |
| **FR-AUTH-10** | Password reset tokens are single-use with 30-minute expiry |
| **FR-AUTH-13** | **No phone or OTP login** |

FR-AUTH-08 deliberately drops composition rules in favour of length plus a breach check — current guidance, and it should not be "improved" back into requiring a symbol and a digit.

k-anonymity means the password is never sent to the breach service; only a hash prefix is. This is worth stating in the implementation notes, because the naive version of this check sends the password.

**FR-AUTH-09's lockout pattern is the model proposed for the profile PIN as well** — see [OQ-10](/3i/open-questions.md#oq-10--pin-attempt-rate-limiting). Not yet formally required there, but the two should stay consistent in shape if adopted.

---

## Devices and Streams

| ID | Requirement |
| :---- | :---- |
| **FR-AUTH-11** | Device allowance is **seats plus two, floor of three** per account, up from a flat 3 in the baseline. Device swap permitted twice per 30 days. Devices are visible and de-authorisable by the Member |
| **FR-AUTH-12** | Concurrent video streams are limited to the number of purchased learner seats, minimum one |

**FR-AUTH-11's device cap is now variable, not flat.** [3I-DEC-015](/3i/decisions/dec-015-device-allowance-scales-with-seats.md): one seat allows three devices, six seats allows eight. This resolves the conflict the flat cap created against seat purchases — a family buying five seats could not previously use them from three devices, which risked being an unenforceable term under Australian Consumer Law (FR-REF-05 already acknowledges those guarantees apply regardless of policy terms).

**FR-AUTH-12 must not be built as an independent concurrency check.** Per [3I-DEC-009](/3i/decisions/dec-009-seats-as-account-pool.md), a seat is an enrolment grant: a profile without a seat cannot enrol, therefore cannot stream. The cap is satisfied structurally. Building a second runtime check invites a conflicting enforcement path.

---

## Acceptance Criteria

From §5, with amendments noted. These are the sign-off conditions under §21.2.

1. A DOB of under 13 cannot produce an account **by any route, including social login**.
2. A 13–17 registration triggers a guardian email, **logged with timestamp and address**.
3. **A device registration beyond the account's current allowance is refused** with a clear message and a link to device management. (Amended from "a fourth device" — the threshold is now the seats-plus-two formula, not a fixed number.)
4. An unverified account is blocked from enrolment, checkout, and chat.

Criterion 2 requires the log, not just the send. An unlogged guardian notification cannot be evidenced later, which is the point of sending it.

---

## Related

| | |
| :---- | :---- |
| Data model | [3I-IDA-DM-001](../data-model.md) |
| Profiles | [3I-IDA-REQ-003](fam-family-accounts-and-profiles.md) |
| Permissions | [3I-IDA-REQ-002](rbac-roles-and-permissions.md) |
| Age rules | [age-and-safeguarding.md](/3i/age-and-safeguarding.md) |
| Device allowance scaling | [3I-DEC-015](/3i/decisions/dec-015-device-allowance-scales-with-seats.md) |
| Safeguarding string exemption | [3I-DEC-019](/3i/decisions/dec-019-safeguarding-strings-exempt-from-ai-translation.md) |
| Rate limiting on auth endpoints | NFR-08 |
