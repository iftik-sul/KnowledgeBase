---
project: OstadLagbo
type: release-checklist
status: current
updated: 2026-09-26
id: OL-STR-001
derived_from: /OstadLagbo/governance/build-sequence.md
owner: Iftikher
---

# App Store Release Checklist

What Google Play and the Apple App Store require before Ostad Lagbo can be published, verified against both stores' current policies on 2026-09-26. The Slice 5 gate says "app-store compliance checklist passed" — this is that checklist. Several items are **long-lead** and must start well before Slice 5; they are marked ⏳.

Items that change the product rather than the release process are called out as **scope** and need a change-log entry before they are built.

## A. Developer accounts ⏳ — start first, this gates everything

**Current position (2026-09-26):** Ostad Lagbo is Iftikher's **personal project** — not a Technovicinity project. There is a company *name*, **Octagon Soft**, but **it is not registered**, so it is not a legal entity and cannot hold anything. An **Apple developer account exists, registered personally**. There is **no Google Play account yet**.

- [ ] **Decide whether a legal entity stands behind this project.** Apple's Guideline 5.1.1(ix): *"Apps that provide services in highly regulated fields … or **that require sensitive user information** should be submitted by a legal entity that provides the services, and **not by an individual developer**."* Ostad Lagbo collects NID/passport images and an ID-holding selfie, which is sensitive user information on any reading. The existing personal Apple account therefore carries a **real rejection risk** — "should", not "must", so it is a risk rather than a certainty, but it is the kind that surfaces at review after the build is done.
  **This is not only an app-store question.** The absence of a registered entity blocks three separate things: the org developer accounts here, the **masked SMS sender ID** (which needs a trade licence — CL-036), and **naming a data controller in the Privacy Policy** (below). One decision resolves all three.
- [ ] **D-U-N-S number** — required by both stores for organization accounts, and **only obtainable by a registered business**. Dun & Bradstreet state this *"can take up to 30 days"*, and the record must match the registered name and address **exactly**. Not applicable until Octagon Soft (or another entity) is actually registered.
- [ ] **Apple Developer Program** — $99/year. Organization enrolment needs an Apple Account with 2FA on a company-domain email, someone with legal binding authority, the legal entity name (trade names and DBAs are refused), the D-U-N-S number, and **a working public website on the company's own domain** (social links or a placeholder page are refused).
- [ ] **Google Play** — $25 one-time. Organization accounts need the D-U-N-S number, a company website, a government identity document and an official organization document. **Prepaid cards are not accepted** — a genuine international-enabled card in the entity's name is required, which from Bangladesh usually means a company or ERQ card. Budget for this friction rather than discovering it at checkout.
- [ ] **Closed-testing gate — applies, on the current personal-account path.** Play requires personal accounts created after 13 Nov 2023 to run a closed test with **at least 12 testers opted in continuously for 14 days** before production access. Google's documentation describes this for personal accounts and is silent on organization accounts, so the org exemption is **likely, not certain**.
  **This is not wasted work.** The build sequence already starts friends-and-family testing at the **Slice 3** gate, and soft launch is Slice 4. Registering the Play account early and running that testing *as* the Play closed test makes the requirement free — the 14-day clock runs during work already planned. It only becomes a two-week delay if the account is created late.

## B. Blocking build work — features that exist only because of store policy

- [ ] **A public web account-deletion page.** **Mandatory on Play** and actively enforced: *"provide a web link resource where users can request app account deletion and associated data deletion."* It applies despite guest browsing — *"If your app offers account creation in any part of the app experience, then you still need to offer app account deletion even if some features can be accessed without an account."*
  **This does not break CL-020's read-only website.** Google accepts *"a customer service email or a form they can submit a request through"* — full self-service is not required. So a **static bilingual page naming Ostad Lagbo and whoever publishes it, with the support email prominently featured**, satisfies it. The page must load without error, be non-geofenced, and make the deletion pathway *"prominently featured and easily discoverable."* The in-app delete (REG-12, Slice 1) stays as it is and satisfies Apple, which requires in-app deletion and does **not** require a URL.
- [ ] **A reviewer account that works from outside Bangladesh, with the OTP bypassed.** This is the single most likely cause of repeated rejection for a country-locked, OTP-gated app. Google: credentials must be *"accessible at all times, reusable, and valid regardless of user location"*, and for OTP apps you must *"provide reusable login credentials that can bypass these requirements."* Apple Guideline 2.1(a) requires demo account details and a live backend. **Scope:** a permanent reviewer account with a fixed OTP code, exempt from any geo or phone-country restriction, seeded with an approved Ostad profile and a sample chat so the features are actually reachable. Build it as a specified feature, not a last-minute hack.
- [ ] **Proactive content filtering.** Apple Guideline 1.2 requires four things of any app with user-generated content: *"A method for filtering objectionable material from being posted to the app"*, *"A mechanism to report offensive content and timely responses to concerns"*, *"The ability to block abusive users from the service"*, and *"Published contact information so users can easily reach you."* Ostad Lagbo has reporting (RNT-07), blocking (RNT-08) and will have published contact details — but **has no filter of any kind**. Google's UGC policy adds that users must accept a UGC policy *before* creating or uploading content. **Scope, v1.3:** a basic abuse/profanity filter on profile text, skill names, reviews and chat, plus pre-posting acceptance of community guidelines. *(Not yet applied — needs a change-log entry and founder approval.)*
- [ ] **Prominent disclosure before sensitive collection.** Play requires an in-app disclosure, separate from the privacy policy, shown before collection, accepted by *"affirmative user action (for example, tap to accept, tick a check-box)"*. MAP-01's public-pin consent statement already does this for location. **Confirm the same pattern covers the NID/passport upload and the live selfie** (REG-10) — a well-known rejection cause for ID-collecting apps.
- [ ] **Manual address entry when location is denied.** Apple Guideline 5.1.1(iv) requires it. MAP-01 already allows a manual pin with GPS denied, and SGP-02 uses a structured address picker — **verify, don't assume**.

## C. Platform and toolchain — already mandatory, discovered at upload not review

- [ ] **Android: `targetSdkVersion` 36** (Android 16). Required for new apps and updates **since 31 August 2026**. An extension to 1 November 2026 can be requested in Play Console. NFR-01's Android 8.0+ *minimum* is unaffected — this is the target, not the floor.
- [ ] **iOS: built with Xcode 26 against the iOS 26 SDK** — required for all App Store Connect uploads **since 28 April 2026**; submissions must target iOS 13+ (NFR-01's iOS 15+ floor already exceeds this). **This requires a Mac running a current macOS.**
- [ ] **Privacy manifests** (`PrivacyInfo.xcprivacy`) for the app and every third-party SDK — required since 1 May 2024. Keep Firebase and other plugins current; a missing third-party manifest fails at upload.
- [ ] **Do not request `READ_MEDIA_IMAGES`.** Play restricts broad photo access to apps whose core function the system picker cannot serve, and requires a Console declaration justifying it. Ostad Lagbo only ever picks single files (profile photo, ID, selfie), so **use the Android Photo Picker and check the merged manifest** — this removes a declaration and a rejection path entirely.
- [ ] **iOS purpose strings**, feature-specific: `NSCameraUsageDescription` (selfie with ID, profile photo), `NSMicrophoneUsageDescription` (voice notes, OFR-05), `NSLocationWhenInUseUsageDescription` (the map), and `NSPhotoLibraryUsageDescription` only if a library pick is offered. Generic strings draw rejections; missing ones fail at upload before human review.

## D. Store listing forms

- [ ] **Name the data controller in the Privacy Policy.** Section 1 currently says only *"Ostad Lagbo is a Bangladesh-based platform"* — **it never says who "we" is.** Play requires the policy to name the entity, and the PDPA requires a identifiable data controller. With no registered company, that controller is **Iftikher personally**, which is a personal-liability position over a vault of national identity documents and is worth a lawyer's opinion before launch, not after. The contact address is also still a placeholder (*"[contact email — to be established before launch]"*).
- [ ] **Privacy policy URL** — public, non-geofenced, **not a PDF**, and also linked inside the app. Both stores require it; Play additionally requires it to name the entity, give contact details and state retention and deletion policy. The guest-reachable legal pages (CL-020, MAP-03) cover the in-app half.
- [ ] **Play Data safety form.** Declare: Name, Phone number, Email, Other info (date of birth; ID numbers if the digits are stored), User IDs, Address, **Approximate location**, **Precise location** (the Ostad's pin — Play defines precise as an area under 3 km²), Photos, **Voice or sound recordings** (voice notes), Other in-app messages (chat), user-generated content, Device IDs, Crash logs. Mark each collected/shared, required/optional, purpose, encrypted-in-transit, and **enter the deletion URL from section B**.
- [ ] **Apple App Privacy label.** Contact Info, Location (Precise + Coarse), User Content (photos, audio, messages, other), Identifiers, Diagnostics. Nearly everything is **Linked to You**; with no ad SDK, nothing is *Used to Track You*, so **no App Tracking Transparency prompt is needed**. Declare data collected by third-party SDKs, Firebase included. *Judgement call:* the admin-reviewed selfie is declared under User Content → Photos, **not** Sensitive Info — it is not a biometric template. **If automated face-matching is ever added, that changes and Sensitive Info must be declared.**
- [ ] **Age ratings.** Apple's system is now 4+/9+/13+/16+/18+, with **social-media-capability questions required for submissions since September 2026**. Play's IARC questionnaire is mandatory. **Answer by what the app can do, not by who is allowed in** — the 18+ gate (REG-03) does not set the store rating, and under-declaring is grounds for removal. Expect 13+ or higher on Apple from the chat and UGC questions alone, and "Users Interact" / "Shares Location" descriptors on Play.
- [ ] **Category framing.** Ostad Lagbo connects strangers for in-person meetings with map pins and private chat. No store policy governs that directly, but a reviewer can mis-bucket it as dating or social discovery — which carries much heavier rules. **Listing copy, screenshots and review notes must make the tutoring-and-skills framing unmistakable**, and the app must carry no payment UI of any kind (there are no in-app payments; keep it that way, or an in-app-purchase argument opens).

## E. Submission

- [ ] Reviewer credentials and demo notes attached to both submissions (section B).
- [ ] **Budget the time.** Play states review may take *"up to seven days or longer in exceptional cases"* for certain accounts — a new account collecting identity documents and hosting chat is exactly that. Expect at least one rejection round. **Do not announce a launch date within a week of submitting.**
- [ ] TestFlight external testing needs a Beta App Review pass; internal testing (up to 100 team testers) does not. Apple sets no minimum tester count or duration.

## Known future requirement — not a v1 blocker

**Play's precise-location Minimum Scope rule** applies to apps targeting **API 37+**: `ACCESS_FINE_LOCATION` will require a Console declaration justifying why coarse location or the one-shot Location Button is insufficient. Declarations open **November 2026**; enforcement begins **27 January 2027**. At API 36 this does not bind v1 — but it bites at the first API-37 update.

**Design around it now.** Ostad Lagbo may not need fine location at all: the **Ostad's pin is user-placed** (MAP-01), which is entered data rather than a device permission, and the **viewer's GPS only centres the map on-device and is never stored** (MAP-10). If centring works acceptably on `ACCESS_COARSE_LOCATION`, the app never needs the declaration. **Verify in Slice 2 while the map is being built**, not in 2027.

## Owners and timing

| Item | Owner | Must start by |
|---|---|---|
| **Entity decision** — register Octagon Soft or stay personal ⏳ | Iftikher | **Now** — gates the store accounts, SMS masking (CL-036) and the Privacy Policy's controller |
| D-U-N-S, **only if** an entity is registered ⏳ | Iftikher | Immediately after registration — up to 30 days |
| **Google Play account** (none exists yet) | Iftikher | **Before Slice 3**, so the 12-tester closed test runs during friends-and-family testing rather than after it |
| Apple account — exists, personal; revisit only if an entity is registered | Iftikher | — |
| Web deletion page | Iftikher | With the website, Slice 2 (CL-020) |
| Reviewer account + OTP bypass | Build | Slice 0–1, with auth |
| Content filter + UGC acceptance | Build, after a v1.3 decision | Before Slice 5 |
| Toolchain (API 36, Xcode 26) | Build | Slice 0 |
| Store forms and listing | Iftikher | Slice 5 |
