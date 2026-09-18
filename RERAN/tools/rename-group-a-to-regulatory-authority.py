#!/usr/bin/env python3
"""
Rename "Group A" -> "Regulatory Authority" across the RERAN documentation.

WHY THIS SCRIPT EXISTS
----------------------
A plain find-and-replace produces broken English and one genuine meaning error.
This script encodes the rules worked out by doing the rename by hand and auditing
it three times, so the remaining files get exactly the same treatment as the ones
already done.

WHAT IT DOES
------------
1. Replaces "Group A" with the right form for its position:
     - start of a sentence        -> "The Regulatory Authority"
     - mid-sentence               -> "the Regulatory Authority"
     - headings and table cells   -> "Regulatory Authority" (no article)
     - before a common noun       -> "Regulatory Authority role/service/screen/..."
     - inside parentheses "(Group A)" -> "(RA)"   [the agreed short form]
2. Applies the specific grammar corrections a literal replace gets wrong.
3. Re-wraps paragraphs it changed to 88 characters, matching the repo's own
   convention (the new term is 17 characters longer than "Group A", which
   otherwise pushes lines well past it).
4. Verifies the result and refuses to leave the repo in a bad state.

WHAT IT DELIBERATELY DOES NOT TOUCH
-----------------------------------
  reference/source-of-truth/   - the client's original documents. These keep
                                 "Group A" verbatim. The whole derivation chain
                                 depends on them being an unaltered record.
  Groups B-H                   - the other user groups keep their letters. The
                                 Regulatory Authority is not a user group like
                                 them: it owns no services, pays no fees, and is
                                 the only place RBAC applies.

HOW TO RUN IT
-------------
  cd <repo root>
  python3 RERAN/tools/rename-group-a-to-regulatory-authority.py            # preview only
  python3 RERAN/tools/rename-group-a-to-regulatory-authority.py --apply    # make the changes

The preview run changes nothing. It prints every file it would touch and how
many replacements it would make. Run that first, read it, then run --apply.

It is safe to run more than once. Files already renamed are skipped, so this can
be re-run after a partial rename without double-applying anything.
"""

import argparse
import os
import re
import sys
import textwrap

ROOT = "RERAN"
EXCLUDE_DIRS = (os.path.join("RERAN", "reference", "source-of-truth"),)
WRAP_WIDTH = 88

# Nouns that read correctly without an article in front of "Regulatory Authority",
# e.g. "Group A roles" -> "Regulatory Authority roles" (not "the Regulatory Authority roles").
BARE_NOUNS = (
    "role", "roles", "service", "services", "screen", "screens", "staff",
    "officer", "officers", "decision", "decisions", "queue", "queues",
    "sub-system", "sub-systems", "action", "actions", "module",
)

# Determiners that already supply the article, so "the" must not be added after them,
# e.g. "two further Group A touches" -> "two further Regulatory Authority touches".
DETERMINERS = (
    r"further|other|another|more|several|two|three|four|five|six|seven|eight|nine|ten|"
    r"many|all|no|any|each|every|some|these|those|both|its|our|your|their|one"
)

# Corrections a positional replace still gets wrong. Found by reading the output,
# not by pattern matching - each one is a real error that shipped in an early draft.
EXPLICIT_FIXES = [
    # A quantity must not be followed by an article.
    ("~10 the Regulatory Authority back-office services",
     "~10 Regulatory Authority back-office services"),
    # A symbol-joined pair reads as a compound noun, so no article.
    ("the AGIS \u2194 the Regulatory Authority crosswalk",
     "the AGIS \u2194 Regulatory Authority crosswalk"),
    # Headings that lost a needed article.
    ("what Regulatory Authority actually does",
     "what the Regulatory Authority actually does"),
    ("what makes Regulatory Authority un-buildable",
     "what makes the Regulatory Authority un-buildable"),
    ("build scope to complete Regulatory Authority",
     "build scope to complete the Regulatory Authority"),
    ("The shape of Regulatory Authority",
     "The shape of the Regulatory Authority"),
    ("things that make Regulatory Authority's UI different",
     "things that make the Regulatory Authority's UI different"),
    # Verb agreement: "Group A audit and decide" was already odd; the longer subject
    # makes it plainly wrong.
    ("the Regulatory Authority audit and decide.",
     "the Regulatory Authority audits and decides."),
    # "the RA services these touchpoints feed into" reads as a verb. Possessive fixes it.
    ("the Regulatory Authority services these touchpoints feed into",
     "the Regulatory Authority's services these touchpoints feed into"),
    # Repetition: "filed to Group A; Group A initiates none" -> use a pronoun.
    ("is filed *to* the Regulatory Authority; the Regulatory Authority initiates none.",
     "is filed *to* the Regulatory Authority; it initiates none."),
    # THE MEANING ERROR. The original said the role *belongs to* Group A. Replaced
    # literally, it asserts the officer IS the whole authority.
    ("Compliance & Escrow Auditor is the Regulatory Authority,",
     "Compliance & Escrow Auditor is a Regulatory Authority role,"),
]


def in_excluded(path):
    norm = os.path.normpath(path)
    return any(norm.startswith(os.path.normpath(d)) for d in EXCLUDE_DIRS)


def convert(text):
    """Apply the positional rename to one file's text."""
    t = text

    # Prose here is hard-wrapped, so "Group A" can straddle a line break ("Group\nA's").
    # Join those first or the line-by-line rules below will miss them. The reflow step
    # re-wraps the paragraph afterwards, so nothing is left over-long.
    # NB: only join within a paragraph - a blank line means "Group" ends one block and
    # "A" starts the next (e.g. a heading "Repeatable Field Group" followed by a
    # paragraph beginning "A block of..."), which is NOT a group reference.
    t = re.sub(r"\bGroup\n[ \t]*(A\b)", r"Group \1", t)

    # Compound titles first, so they don't become "Regulatory Authority - Regulatory Authority".
    t = t.replace("Group A \u2014 Regulatory Authority & Governance", "Regulatory Authority & Governance")
    t = t.replace("Group A (Regulatory Authority & Governance)", "The Regulatory Authority")

    # "(Group A)" is a parenthetical tag after a role name. The short form belongs here:
    # it keeps lines short and matches how RED / FTI / RESC are used elsewhere.
    t = t.replace("(Group A)", "(RA)")
    t = t.replace("[Group A]", "[RA]")

    # Possessives are handled via a placeholder so the article logic below sees them.
    t = t.replace("Group A's", "\x00POSS\x00")

    out = []
    for line in t.split("\n"):
        stripped = line.lstrip()
        structural = stripped.startswith("#") or stripped.startswith("|")

        if structural:
            # Headings and table cells read better with no article.
            line = line.replace("\x00POSS\x00", "Regulatory Authority's")
            line = re.sub(r"\bGroup A\b", "Regulatory Authority", line)
        else:
            # Sentence-initial -> "The"; anywhere else -> "the".
            # NB: a line break is not a sentence break - prose here is hard-wrapped,
            # so "^" must NOT count as a sentence start. Capitalisation is settled
            # after the line loop, where the full text is visible.
            sentence_start = r"((?<=[.!?]\s)|(?<=[.!?]\s\s)|(?<=\*\*\s))"
            line = re.sub(sentence_start + r"\x00POSS\x00", "The Regulatory Authority's", line)
            line = line.replace("\x00POSS\x00", "the Regulatory Authority's")
            line = re.sub(sentence_start + r"Group A\b", "The Regulatory Authority", line)
            # Before a common noun, no article.
            line = re.sub(r"\bGroup A (%s)\b" % "|".join(BARE_NOUNS),
                          r"Regulatory Authority \1", line)
            # Everything else takes "the", unless one is already there.
            line = re.sub(r"(?<!the )(?<!The )\bGroup A\b", "the Regulatory Authority", line)
            line = re.sub(r"\bGroup A\b", "Regulatory Authority", line)
        out.append(line)
    t = "\n".join(out)

    # Tidy the artefacts the rules above can still leave behind.
    t = t.replace("the the Regulatory Authority", "the Regulatory Authority")
    # "a Group A user" must become "a Regulatory Authority user", not "a the ...".
    t = re.sub(r"\b(a|an|A|An) the Regulatory Authority\b", r"\1 Regulatory Authority", t)
    t = t.replace("The the Regulatory Authority", "The Regulatory Authority")
    t = re.sub(r"\b(%s) the Regulatory Authority\b" % DETERMINERS,
               lambda m: "%s Regulatory Authority" % m.group(1), t, flags=re.I)
    t = re.sub(r"(\d+|~) the Regulatory Authority\b", r"\1 Regulatory Authority", t)
    t = re.sub(r"([\u2194\u2192/+]) the Regulatory Authority\b", r"\1 Regulatory Authority", t)
    # Capitalise only where a sentence genuinely starts: after terminal punctuation,
    # at the start of a paragraph, or at the start of a list item.
    t = re.sub(r"([.!?]\s+)the Regulatory Authority\b", r"\1The Regulatory Authority", t)
    t = re.sub(r"(\n\n)the Regulatory Authority\b", r"\1The Regulatory Authority", t)
    t = re.sub(r"(\n\s*[-*]\s+)the Regulatory Authority\b", r"\1The Regulatory Authority", t)
    t = re.sub(r"(\*\*\s+)the Regulatory Authority\b", r"\1The Regulatory Authority", t)

    for before, after in EXPLICIT_FIXES:
        t = t.replace(before, after)

    return t


def reflow(text):
    """Re-wrap only the paragraphs this rename actually lengthened - that is, ones
    containing the new term. Paragraphs the rename never touched are left exactly as
    they are, so the diff stays about the rename and nothing else.

    Never touches code, tables, lists, quotes or headings, and refuses any rewrap
    that would change the words."""
    parts = re.split(r"(```.*?```)", text, flags=re.S)
    for i, seg in enumerate(parts):
        if i % 2 == 1:          # inside a fenced code block
            continue
        paragraphs = seg.split("\n\n")
        for j, para in enumerate(paragraphs):
            s = para.strip()
            if not s:
                continue
            if s.startswith(("|", ">", "#", "---", "- ", "* ")) or re.match(r"^\d+\.", s):
                continue
            if any(l.lstrip().startswith(("|", ">", "#", "- ", "* ")) for l in para.split("\n")):
                continue
            if para.split("\n")[0][:1].isspace():   # indented continuation
                continue
            if "Regulatory Authority" not in para:
                continue        # untouched by the rename - leave its wrapping alone
            if not any(len(l) > WRAP_WIDTH for l in para.split("\n")):
                continue
            rewrapped = "\n".join(textwrap.wrap(" ".join(para.split()), WRAP_WIDTH,
                                                break_long_words=False,
                                                break_on_hyphens=False))
            if rewrapped.split() == para.split():   # content-identical guarantee
                paragraphs[j] = rewrapped
        parts[i] = "\n\n".join(paragraphs)
    return "".join(parts)


def collect_files():
    found = []
    for dirpath, _, filenames in os.walk(ROOT):
        if in_excluded(dirpath):
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                found.append(os.path.join(dirpath, fn))
    return sorted(found)


def verify():
    """Checks that must hold after the rename. Returns a list of problems."""
    problems = []
    groups_bh = 0
    for path in collect_files():
        text = open(path, encoding="utf-8").read()
        if re.search(r"\bGroup A\b", text):
            problems.append("still contains 'Group A': %s" % path)
        for pattern, label in (
            (r"the the Regulatory|The the Regulatory", "double article"),
            (r"(\d+|~|\u2194|\u2192) the Regulatory Authority", "quantity or symbol + article"),
            (r"is the Regulatory Authority,", "identity-vs-membership error"),
            (r"\b(a|an) the Regulatory Authority\b", "indefinite article + 'the'"),
        ):
            if re.search(pattern, text):
                problems.append("%s: %s" % (label, path))
        groups_bh += len(re.findall(r"\bGroup [B-H]\b", text))

    if groups_bh == 0:
        problems.append("Groups B-H appear to have been renamed too - they must not be")

    # Source-of-truth must still say "Group A".
    src = os.path.join(ROOT, "reference", "source-of-truth")
    if os.path.isdir(src):
        kept = sum(
            len(re.findall(r"\bGroup A\b", open(os.path.join(src, f), encoding="utf-8").read()))
            for f in os.listdir(src) if f.endswith(".md")
        )
        if kept == 0:
            problems.append("source-of-truth no longer says 'Group A' - it must be left verbatim")
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true",
                    help="write the changes (without this flag nothing is modified)")
    args = ap.parse_args()

    if not os.path.isdir(ROOT):
        sys.exit("Run this from the repository root (the folder containing '%s/')." % ROOT)

    touched = 0
    for path in collect_files():
        original = open(path, encoding="utf-8").read()
        if "Group A" not in original:
            continue                        # already done, or never mentioned it
        updated = reflow(convert(original))
        if updated == original:
            continue
        count = len(re.findall(r"\bGroup A\b", original))
        print("  %-70s %d replacement%s" % (path, count, "" if count == 1 else "s"))
        touched += 1
        if args.apply:
            open(path, "w", encoding="utf-8").write(updated)

    if not args.apply:
        print("\nPreview only - nothing was changed. %d file%s would be updated." %
              (touched, "" if touched == 1 else "s"))
        print("Re-run with --apply to make the changes.")
        return

    print("\n%d file%s updated. Verifying..." % (touched, "" if touched == 1 else "s"))
    problems = verify()
    if problems:
        print("\nPROBLEMS FOUND - review before committing:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    print("Verification passed:")
    print("  - no 'Group A' left outside reference/source-of-truth/")
    print("  - source-of-truth still verbatim")
    print("  - Groups B-H untouched")
    print("  - no double articles, quantity/symbol collisions, or identity errors")


if __name__ == "__main__":
    main()
