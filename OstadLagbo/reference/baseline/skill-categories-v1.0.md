---
project: OstadLagbo
type: baseline
status: current
updated: 2026-09-13
version: "1.0"
approval: written
approved: 2026-09-13
id: OL-SKC-001
derived_from: /OstadLagbo/modules/admin-review/requirements/admin-review-requirements.md
owner: Iftikher
---

# Skill Categories — Seed Data v1.0

The launch contents of the `skill_category` table (ADM-DM). Founder-authored reference data under change control: revised by issuing v1.1, never edited in place; after launch, day-to-day additions happen through the admin panel (ADM-11) and are periodically consolidated into a new version here.

**Design rules this list follows**

1. **Categories are groups, not skills.** The category is what a Shagred filters by; the specific skill is the Ostad's free-text `skill_name` within it (OSP-04). "Guitar" is a category; "acoustic fingerstyle" is a skill name. Granularity is set so that a Shagred's likely first question ("who teaches guitar near me?") maps to exactly one category.
2. **No "Other" category.** A catch-all defeats discovery — everything in it is unfindable by filter. Ostads pick the nearest category and put specifics in the skill name (OSP-04). Genuinely missing categories will surface through ADM-14's zero-result search analytics and be added via ADM-11; that feedback loop is the mechanism, not a dumping ground.
3. **Bangla names are canonical, not translations.** Each `name_bn` is the term a Bangla-speaking Shagred would actually type or say, which is sometimes a loanword in Bangla script (গিটার, আইইএলটিএস) rather than a literary rendering. **The Bangla below was approved as v1.0 on 2026-09-13; corrections are issued as v1.1** — the founder authors Bangla copy (CL-016).
4. **Flat list.** `skill_category` has no parent field; the group headings below organize this document only.

## The list

### Academic tutoring (school and admission)

| # | name_en | name_bn | Notes |
|---|---|---|---|
| 1 | Mathematics | গণিত | SSC/HSC/O-A level and below |
| 2 | Physics | পদার্থবিজ্ঞান | |
| 3 | Chemistry | রসায়ন | |
| 4 | Biology | জীববিজ্ঞান | |
| 5 | English (academic) | ইংরেজি (একাডেমিক) | Grammar, literature, exam English — distinct from #13 |
| 6 | Bangla (academic) | বাংলা (একাডেমিক) | |
| 7 | Accounting & Business Studies | হিসাববিজ্ঞান ও ব্যবসায় শিক্ষা | Commerce stream |
| 8 | ICT (school) | তথ্য ও যোগাযোগ প্রযুক্তি | The school subject, not vocational IT |
| 9 | Primary & Junior — All Subjects | প্রাথমিক ও জুনিয়র — সকল বিষয় | Classes 1–8 general tutoring |
| 10 | Admission Test Preparation | ভর্তি পরীক্ষা প্রস্তুতি | University, medical, engineering admission |
| 11 | Job Exam Preparation | চাকরির পরীক্ষা প্রস্তুতি | BCS, bank, government recruitment |
| 12 | Quran & Arabic Studies | কুরান ও আরবি শিক্ষা | Tajweed, Hifz, Islamic studies |

### Languages

| # | name_en | name_bn | Notes |
|---|---|---|---|
| 13 | Spoken English | স্পোকেন ইংলিশ | Conversation and fluency — the largest single demand category in urban Bangladesh |
| 14 | IELTS & Test Preparation | আইইএলটিএস ও পরীক্ষা প্রস্তুতি | IELTS, TOEFL, PTE, Duolingo |
| 15 | Arabic (language) | আরবি ভাষা | Conversational/Modern Standard — distinct from #12 |
| 16 | Foreign Languages | বিদেশি ভাষা | Japanese, Korean, Chinese, German, French… — skill name specifies |

### Music and performing arts

| # | name_en | name_bn | Notes |
|---|---|---|---|
| 17 | Guitar | গিটার | |
| 18 | Keyboard & Piano | কিবোর্ড ও পিয়ানো | |
| 19 | Singing (Vocal) | কণ্ঠসংগীত | Rabindra, Nazrul, modern, classical vocal — skill name specifies |
| 20 | Tabla & Percussion | তবলা ও তালবাদ্য | |
| 21 | Harmonium & Classical Instruments | হারমোনিয়াম ও শাস্ত্রীয় বাদ্যযন্ত্র | Sitar, sarod, flute, violin — skill name specifies |
| 22 | Dance | নৃত্য | |
| 23 | Drama & Recitation | নাটক ও আবৃত্তি | |

### Technology and digital skills

| # | name_en | name_bn | Notes |
|---|---|---|---|
| 24 | Programming & Software Development | প্রোগ্রামিং ও সফটওয়্যার ডেভেলপমেন্ট | Languages and frameworks in skill name |
| 25 | Web Development | ওয়েব ডেভেলপমেন্ট | |
| 26 | Graphic Design | গ্রাফিক ডিজাইন | |
| 27 | Video Editing & Animation | ভিডিও এডিটিং ও অ্যানিমেশন | |
| 28 | Digital Marketing & Freelancing | ডিজিটাল মার্কেটিং ও ফ্রিল্যান্সিং | Very high aspirational demand |
| 29 | Basic Computer & Office Applications | বেসিক কম্পিউটার ও অফিস অ্যাপ্লিকেশন | MS Office, typing, email — entry-level |
| 30 | Photography | ফটোগ্রাফি | |

### Trades and technical work

| # | name_en | name_bn | Notes |
|---|---|---|---|
| 31 | Electrical Work | ইলেকট্রিক্যাল কাজ | House wiring, electrician training |
| 32 | Mobile & Electronics Repair | মোবাইল ও ইলেকট্রনিক্স মেরামত | |
| 33 | Motorcycle & Automobile Mechanics | মোটরসাইকেল ও গাড়ি মেকানিক্স | |
| 34 | Plumbing | প্লাম্বিং | |
| 35 | Carpentry & Furniture | কাঠমিস্ত্রি ও আসবাব | |
| 36 | Tailoring & Sewing | দর্জি ও সেলাই | |
| 37 | AC & Refrigeration Repair | এসি ও রেফ্রিজারেশন মেরামত | |
| 38 | Welding & Metalwork | ওয়েল্ডিং ও ধাতুর কাজ | |

### Crafts, arts, and lifestyle

| # | name_en | name_bn | Notes |
|---|---|---|---|
| 39 | Drawing & Painting | চিত্রাঙ্কন | |
| 40 | Handicrafts & Embroidery | হস্তশিল্প ও এমব্রয়ডারি | Nakshi kantha, jute craft, paper craft |
| 41 | Cooking & Baking | রান্না ও বেকিং | |
| 42 | Beauty & Salon Skills | বিউটি ও সেলুন | Makeup, hair, mehendi |
| 43 | Fashion Design & Block-Batik | ফ্যাশন ডিজাইন ও ব্লক-বাটিক | |

### Sports and fitness

| # | name_en | name_bn | Notes |
|---|---|---|---|
| 44 | Cricket Coaching | ক্রিকেট কোচিং | |
| 45 | Football Coaching | ফুটবল কোচিং | |
| 46 | Swimming | সাঁতার | |
| 47 | Martial Arts & Self-Defense | মার্শাল আর্ট ও আত্মরক্ষা | Karate, taekwondo, boxing |
| 48 | Fitness & Yoga | ফিটনেস ও যোগব্যায়াম | |

### Other practical skills

| # | name_en | name_bn | Notes |
|---|---|---|---|
| 49 | Driving | ড্রাইভিং | Car and motorcycle instruction |
| 50 | Agriculture & Gardening | কৃষি ও বাগান | Rooftop gardening, poultry, fish farming |
| 51 | Public Speaking & Communication | বক্তৃতা ও যোগাযোগ দক্ষতা | Presentation, interview skills |

**51 categories at launch.**

## Launch-focus categories (risk R-01, build sequence Slice 1)

The risk register commits seeding to 2–3 categories in one launch area. **Approved focus:** **(1) Academic tutoring — Mathematics, Physics, Chemistry** (#1–3, the densest, most proven tutoring demand); **(2) Spoken English** (#13, the largest single non-academic demand); **(3) Guitar and Keyboard** (#17–18, high-intent hobby learning with strong word-of-mouth). Seed recruitment targets Ostads in these categories first; every other category launches with the list but without a recruitment push.

## Fuzzy-matching test set (ADR-001 open item 4; OSP-04, MAP-06)

The matcher must resolve each input to the named category. Minimum test set for Slice 0; extend as the list grows.

| Input | Must resolve to |
|---|---|
| `gitar`, `guiter`, `gittar` | Guitar |
| `গিটার`, `গীটার` | Guitar |
| `spoken inglish`, `spokn english` | Spoken English |
| `স্পোকেন ইংলিশ`, `স্পোকেন` | Spoken English |
| `math`, `maths`, `mathmatics` | Mathematics |
| `গনিত`, `গণিত` | Mathematics (note the common vowel-sign variant) |
| `ielts`, `ILTS`, `আইইএলটিএস` | IELTS & Test Preparation |
| `ranna`, `রান্না` | Cooking & Baking |
| `tabla`, `তবলা` | Tabla & Percussion |
| `electric`, `ইলেকট্রিক` | Electrical Work |
| `programing`, `coding` | Programming & Software Development (`coding` via a synonym alias — see below) |

**Synonym aliases** are an engineering default the matcher may add per category (e.g., "coding" → Programming, "hair" → Beauty & Salon); they are not stored as separate categories.

## How this document becomes data

Slice 0 loads this list as the initial `skill_category` migration: one row per line, `active = true`, `name_en` and `name_bn` exactly as approved here. Subsequent additions through ADM-11 are consolidated into v1.1 of this document at the next planning review, so the repository always holds the current canonical list.
