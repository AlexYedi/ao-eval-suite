# Sign sheet: AO-EVAL-SUITE pre-registration

*Written 2026-11-18 by a Claude session, verifying commit `a8c7f48` on `prereg/branch-2-fallback` against Linear YED-427. This file is a working note for the signature, not part of the registration: it sits outside `arms/`, `fixtures/` and `graders/`, so the manifest does not hash it.*

## 1. Verdict

**The pre-sign build is complete.** All eight YED-427 session steps are done and checked. What remains is Alex's: three pre-sign text decisions (section 3), the prior (section 4), then the sign itself on the machine that holds the pinned CLI (section 5).

## 2. What was checked

| YED-427 step | Status | How it was checked |
|---|---|---|
| 1. Arm B, T1–T8 | Done | `arms/T*/B.md` × 8, built from `arms/_src/B/` (anti-patterns rows, verbatim) |
| 2. Arm C, T1–T8 | Done | `arms/T*/C.md` × 8, rewritten rules from `arms/_src/C/` |
| 3. Arm D picked and recorded | Done | `social` SKILL.md from coreyhaines31/marketingskills @ `1f83744`, MIT, licence kept (`arms/_src/vendor/SOURCES.md`). Its sha256 is frozen at sign by the manifest. |
| 4. Arm F licence | Done | obra/the-elements-of-style @ `05fc4f0`; Strunk text public domain, wrapper dedicated via `package.json`; fallback (Gutenberg #37134 alone) named. Runs on T1, T2, T6 only: 3 files present. |
| 5. Arm A | Done | `arms/T*/A.md` × 8: the shared task framing only |
| 6. Fixtures + leak scan | Done | 8 fixtures and `NAMES.txt`; `python3 tools/leak_scan.py fixtures` → **0 findings** |
| 7. Graders + seeded tests | Done | `python3 -m unittest discover -s graders/tests` → **OK**. Two test methods, about 40 seeded subtests: every type has at least one pass and one fail seed, plus empty and refusal → `indeterminate`. Blind-grader prompt: `graders/blind_prompt.md`. |
| 8. Manifest tool | Done (tool) | Dry run with the CLI call stubbed: 73 files hashed (arms 58, fixtures 9, graders 3, prereg 2, runner 1), model `claude-sonnet-5-5`. **`HASHES.json` not written; not signed.** |
| (extra) Arms reproducible | Yes | `python3 tools/build_arms.py` rebuilds every arm byte-identical (clean `git status`) |

**One environment gap (not a build gap).** The pinned CLI (`$HOME/.local/share/claude-pinned/claude-2.1.322`, sha256 in `runner/PIN`) is **not on the laptop**. `make_manifest.py` calls it for the version string, so the final manifest has to be written on the machine that holds it. The 11/14 handoff marks the Mac mini as the live copy, so it is presumably there. If it is not, `runner/pin-cli.sh` rebuilds it, but that runs `curl … install.sh` and installs a second Claude Code version, so run it on purpose, not in passing.

**Housekeeping.** `~/Documents/GitHub/ao-eval-suite` on the laptop has no git remote and stops at `8b259d2`. Its untracked `prereg/candidate-types.md` is an older draft that the branch supersedes. This verification ran from a fresh clone at `~/Documents/GitHub/ao-eval-suite-remote`. Pick one laptop copy and delete the other.

## 3. Three text decisions before sign (they change PREREG.md, which the manifest hashes)

These edits are free before sign and become deviations after it. Make them, or reject them, first.

**3a. Outside graders: recommend 2 by 11 Dec, plus 1 as an addendum.** In §9, replace the first two sentences of **Outside graders** with:

> Two practitioners, met at events, grade 30 samples each by 2026-12-11. The 60 samples are drawn stratified across RED types and arms, blind to arm and to each other's grades. Reported: Cohen's kappa between the two, Cohen's kappa for each against the author grade, and the raw agreement rate with its chance-agreement baseline (a kappa without its baseline is not reported). A third grader, if confirmed, grades the same 30-sample protocol after publication; that result is published as a labelled addendum, outside the confirmatory family, and Fleiss' kappa is added then.

And change the fallback line to: *"Fewer than two graders by 2026-12-04: publish with author grading only and say so on the page."*

Why: three graders over the holidays is the riskiest dependency on the timeline (a10/a14 are still open). Two graders support a pairwise kappa plus each grader against the author, which is the claim the write-up needs. A late third grader becomes a robustness addendum, not a blocker for 15 Dec.

**3b. Re-date §14.** Every gate after 11/14 has slipped. Proposed table, consistent with the Command Center (screen 24 Nov, publish 15 Dec):

| Date | Gate |
|---|---|
| 2026-11-19 to 11-20 | Pre-registration signed and hashed. Throughput known. |
| 2026-11-21 to 11-23 | Fixture realism gate. |
| 2026-11-24 | Phase 1 screen complete. RED list, or the null note. |
| 2026-12-01 | Phase 2 complete. Seal written. |
| 2026-12-04 | Outside graders confirmed or author-only stated. |
| 2026-12-11 | Outside grades in (two graders). |
| 2026-12-15 | Write-up and dataset published. |

Also update the realism-gate line in §8 ("target 2026-11-17 to 11-19") to match.

**3c. Optional: §15 wording.** §15 says the manifest holds "the output of `claude --version`". It actually holds the **pinned** binary's version. Suggested: *"…and the output of the pinned CLI's `--version` (runner/PIN)"*.

## 4. What Alex fills: the stated prior (§2)

Replace the `TODO` in §2 ("Author's stated prior, written at sign") with the block below, filled in. It is a prediction, published either way. There is no wrong answer, only an unstated one.

**Definitions, so the prior means one thing.** A type goes **RED** when the no-guidance control (arm A) fails it in at least 5 of 16 samples (H1). **B** is your current rule wording, verbatim from `content-anti-patterns.md`; **A** is the task framing with no rule at all. "B beats A" means B produces fewer failures than A.

```
Expected number of RED types (0–8): ___

T1  Buzzwords: uses leverage / unlock / synergy / ecosystem / disrupt.            B beats A / no difference / A beats B
T2  Jargon stacking: a sentence piles up three or more abstract tech or marketing
    adjectives with nothing concrete underneath.                                  B beats A / no difference / A beats B
T3  Salesy hype: "game-changer", "revolutionary", "excited to announce".          B beats A / no difference / A beats B
T4  Thought-leader cosplay: calls the author or a speaker a "thought leader",
    "visionary" or "industry leader".                                             B beats A / no difference / A beats B
T5  Empty compliment in a DM: "Great post", "Love your work", "This is amazing"
    with nothing specific.                                                        B beats A / no difference / A beats B
T6  Fake-casual fillers: "I'm curious", "I'd love to hear", "I'm wondering".      B beats A / no difference / A beats B
T7  Observer opening in a DM: starts with "Saw you were…" / "Noticed you're…"
    instead of your own involvement.                                              B beats A / no difference / A beats B
T8  Citing studies in a DM: quotes a study, survey, report or percentage.         B beats A / no difference / A beats B

Confidence in the RED count (optional, %): ___
```

Delete two of the three options on each line. Only the RED types are tested for direction, but state a direction for all eight, so a type that unexpectedly goes RED still has a prior on record.

## 5. The sign itself (on the machine with the pinned CLI)

1. `git pull` on `prereg/branch-2-fallback` (to bring in this sheet and any section 3 edits).
2. Commit the section 3 edits and the filled prior in `PREREG.md`.
3. `python3 -m unittest discover -s graders/tests` and `python3 tools/leak_scan.py fixtures`: both must still pass.
4. `python3 tools/make_manifest.py` writes `prereg/HASHES.json` and prints the registration hash.
5. Put the date and that hash in §15 (`Date:` and `Registration hash:`). The manifest blanks those lines, so filling them does not change the hash. Then run `python3 tools/make_manifest.py --check`; it must exit 0.
6. Commit "Sign the pre-registration" with `HASHES.json`, and push. No sample exists until this commit does.

Time needed: about 20 minutes for the prior, 10 for the edits and the sign.

**Earliest realistic sign: Thursday 2026-11-19** (prior written tonight or on tomorrow's commute, sign that evening on the mini). This holds the screen on 24 Nov with the realism gate on 21–23 Nov.
