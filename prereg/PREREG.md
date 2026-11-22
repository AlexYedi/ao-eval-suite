# Pre-registration: Prose Pressure Test (AO-EVAL-SUITE study 1)

| Field | Value |
|---|---|
| Study id | `ppt-2026-11` |
| Author | Alex Yedibalian |
| Status | DRAFT. Section 5 filled from the fallback source (2026-11-14). Not signed. No study sample exists. |
| Sign date | TODO (target 2026-11-14) |
| Registration hash | TODO (sha256 of the manifest in `prereg/HASHES.json`, written at sign time) |
| Spec of record | Plan v4 (2026-11-08), lane A; Linear YED-365 |
| Model under test | Claude Sonnet 5.5 (`claude-sonnet-5-5`, a full model id, never an alias) via `claude -p` at Claude Code 2.1.322. Both are pinned in `runner/PIN`. The runner calls its own copy of the CLI binary, not the auto-updating `claude` on PATH, and refuses to sample unless that copy's sha256 and version match the pin. Both are frozen in `HASHES.json` at sign |

This document is frozen when signed. After the sign date, nothing above the "Deviations" section changes. Changes go in `prereg/DEVIATIONS.md` (see section 11).

---

## 1. Question

Does writing guidance change what a language model writes, measured against saying nothing?

"Guidance" here means a rule from a GTM writing style guide, a rewritten form of that rule, a GTM writing skill from a public marketplace, or a general writing skill. "Saying nothing" is the no-guidance control: the same task, the same fixture, no rule.

The study is in two phases. Phase 1 screens up to 8 failure types against the control alone. Phase 2 runs arms only on the types the control actually fails. A rule that fixes a failure the model never makes is not tested here; it is reported as untestable.

## 2. Hypotheses

Stated before any sample. Each has a null.

- **H1 (screen).** For at least one failure type, the no-guidance control fails in at least 5 of 16 samples. Null: the control fails fewer than 5 of 16 on every type.
- **H2 (primary).** For each RED type, the current rule wording (arm B) produces fewer failures than the control (arm A). Null: no difference in failure proportion between B and A.
- **H3 (secondary, form).** For each RED type, the rewritten rule (arm C) produces no more failures than the current wording (arm B). Null: no difference.
- **H4 (secondary, outside guidance).** For each RED type, a marketplace GTM skill (arm D) and, on shaping types only, a general writing skill (arm F) each produce fewer failures than the control (arm A). Null: no difference from A.

Author's stated prior, written at sign (2026-11-22). This is a prediction, not a result. It is published either way.

```
Expected number of RED types (0–8): 3

T1  Buzzwords: uses leverage / unlock / synergy / ecosystem / disrupt.            B beats A
T2  Jargon stacking: a sentence piles up three or more abstract tech or marketing
    adjectives with nothing concrete underneath.                                  B beats A
T3  Salesy hype: "game-changer", "revolutionary", "excited to announce".          B beats A
T4  Thought-leader cosplay: calls the author or a speaker a "thought leader",
    "visionary" or "industry leader".                                             B beats A
T5  Empty compliment in a DM: "Great post", "Love your work", "This is amazing"
    with nothing specific.                                                        B beats A
T6  Fake-casual fillers: "I'm curious", "I'd love to hear", "I'm wondering".      B beats A
T7  Observer opening in a DM: starts with "Saw you were…" / "Noticed you're…"
    instead of your own involvement.                                              B beats A
T8  Citing studies in a DM: quotes a study, survey, report or percentage.         B beats A

Confidence in the RED count: about 40%
```

Only the RED types are tested for direction (H2). A direction is stated for all eight, so a type that unexpectedly goes RED still has a prior on record.

## 3. Primary outcome

Per sample: a three-valued verdict, `pass`, `fail` or `indeterminate`, on the single predicate registered for that failure type.

Per cell (type × arm): `k / n_det (n_planned)`, where `k` is the fail count, `n_det` the number of determinate samples, and `n_planned` is 16. All three numbers appear in every table. No rate is shown without its denominator.

The primary comparison for each RED type is one, named in advance: **B vs A** on fail proportion. Every other comparison is secondary or exploratory and is labelled so in the results.

## 4. Design facts (fixed)

| Item | Value |
|---|---|
| Phase 1 | up to 8 failure types × control (arm A) × 16 reps = up to 128 samples |
| RED threshold | control fails ≥ 5 of 16 determinate samples |
| Why 5 | Fisher exact, two-sided, 0/16 vs 5/16: p ≈ 0.043. 0/16 vs 4/16: p ≈ 0.10. Below 5 control failures, Phase 2 cannot show an effect at p < 0.05 even if a rule drove failures to zero. |
| Phase 2 | each RED type × up to 5 arms × 16 reps |
| Reps per cell | 16 attempts. Fixed. No refills. |
| Model | Sonnet, one completion per sample, no tools, no memory, no MCP |
| Sampling | `runner/sample.sh` (section 7) |
| Fixtures | synthetic only (section 8) |
| Graders | deterministic code first, blind Sonnet second, 3 outside practitioners on a stratified subset (section 9) |
| Raw samples | published, every arm, every rep, with a seal |

## 5. Failure types

The procedure that selects them is in `prereg/failure-type-selection.md`. It is frozen with this document. The list below is filled from that procedure and nothing else.

**Source used: the fallback (decided 2026-11-14, Linear YED-402).** The primary source, Alex's review comments in the Notion Content Drafts database, held 17 countable comments on 6 drafts out of 935 drafts swept. That is below the 60-comment trigger in `failure-type-selection.md` §1, so the fallback applies as written: the eligible rows of the anti-patterns document, in file order. The fallback has no counting rule, so score, count and recurrence are n/a for every row. The types come from the author's style guide, not from measured corrections; the results page says so. Candidate list and exclusions: `prereg/candidate-types.md`.

| id | Short name | Predicate (one yes/no question) | Grader | Shaping? | Fixture file |
|---|---|---|---|---|---|
| T1 | Omnipresent buzzwords | Does the text contain any of: leverage, unlock, synergy, ecosystem, disrupt (any inflection)? | code | yes | `fixtures/T1/` |
| T2 | Jargon stacking | Does any single sentence chain three or more abstract tech/marketing modifiers (e.g. 'AI-powered digital transformation leveraging cutting-edge solutions') with no concrete referent? | blind | yes | `fixtures/T2/` |
| T3 | Super salesy | Does the text contain any of: game-changer, game changing, revolutionary, 'excited to announce' / 'I'm excited to'? | code | no | `fixtures/T3/` |
| T4 | Thought-leader cosplay | Does the text apply any of 'thought leader', 'visionary', 'industry leader' to the author or a speaker? | both | no | `fixtures/T4/` |
| T5 | Empty validation (DM) | Does the DM contain a content-free compliment such as 'Love your work', 'Great post', 'This is amazing' (or a close variant)? | both | no | `fixtures/T5/` |
| T6 | Faux casual fillers | Does the text contain any of: 'I'm curious', 'I'd love to hear', 'I'm wondering'? | code | yes | `fixtures/T6/` |
| T7 | Observer framing (DM) | Does the DM open or anchor with 'Saw you were…' / 'Noticed you're…' / 'I saw that you…'? | code | no | `fixtures/T7/` |
| T8 | Citing studies in DMs | Does the DM cite a study, survey, report or percentage statistic? | both | no | `fixtures/T8/` |

Next-ranked if a type is removed under `failure-type-selection.md` §7: rank 9, "Leading with company/product name", then rank 10 onward in file order (`prereg/candidate-types.md`). Shaping types (arm F runs if they go RED): T1, T2, T6.

Grader changes from the candidate list, made before sign: T4 and T5 move from code to both. Code finds the listed phrases, but it cannot tell whether 'industry leader' is applied to a person (T4) or catch a close variant of a listed compliment (T5). On those two types code decides a match, and the blind grader decides the rest. Code predicates: `graders/predicates.py`. Seeded tests: `graders/tests/test_predicates.py`.

Rules for the table:

- A predicate is one question a stranger can answer yes or no from the sample and the fixture. No predicate, no type.
- "Shaping" is set per type before sampling. It is true only when a rule in the public-domain Strunk text (1918) plainly applies to the predicate. It decides whether arm F runs on that type. It is not changed after sign.
- A type where the grader is "blind" only (no code check possible) is reported with that label.

## 6. Arms

Arm letters are labels, not an order. The plan names the general writing skill "arm F", so that letter is kept. Letter E is unassigned.

| Arm | Content of the system prompt | Runs on |
|---|---|---|
| A | No guidance. Task framing only (the same framing appears in every arm). | every RED type |
| B | Alex's current rule wording for the type, verbatim from the style guide at sign. | every RED type |
| C | The same rule rewritten so its form matches the failure (prohibition with a rationalization table, positive recipe, required slot, or observable predicate). Written before sign. | every RED type |
| D | One GTM writing skill from a public skill marketplace, used as published, licence permitting: `social` from coreyhaines31/marketingskills (`skills/social/SKILL.md` at commit `1f83744`, MIT). Its sha256 is in `HASHES.json`, and provenance is in `arms/_src/vendor/SOURCES.md`. The same skill runs on every RED type. | every RED type |
| F | The Elements of Style writing skill as listed in the Superpowers marketplace (obra/the-elements-of-style at commit `05fc4f0`: its SKILL.md followed by its elements-of-style.md). If its licence cannot be confirmed by sign, the public-domain Strunk text is used instead and the results say so. Status at drafting: the Strunk text is public domain, and the wrapper is declared "Public Domain" in the repo's package.json but has no LICENSE file. | shaping RED types only |

Each arm is one file under `arms/<type>/<arm>.md`. Its sha256 is in `HASHES.json`. A non-shaping RED type runs four arms (A, B, C, D). A shaping type runs five.

Arm F is registered here or not at all. It is never added after sampling starts. If no shaping type goes RED, arm F does not run and the results say so.

## 7. Sampling recipe and the preamble disclosure

Every sample is one call:

```
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude -p --model claude-sonnet-5-5 \
  --system-prompt "<arm file>" --setting-sources "" --strict-mcp-config \
  --mcp-config '{"mcpServers":{}}' --tools "" --output-format json \
  "<fixture prompt>"
```

run from an empty temporary directory by `runner/sample.sh`. No tools, no memory, no settings, no MCP servers. The JSON result, the usage block and wall time are kept per sample.

**Preamble disclosure.** `claude -p` is a coding-agent CLI, not a raw API call. Even with an empty system prompt it sends a constant harness preamble of roughly 700 tokens before the arm text. In a 2-sample smoke run with a 7-word system prompt, the median input-token count was 691. This preamble:

- is the same in every arm, so it cancels in every A-vs-arm comparison;
- is not under the study's control, so results generalise to "Sonnet behind this CLI", not to the bare model;
- is measured and published before results: the input-token count of an empty system prompt and a one-word user prompt, plus the output of a separate, non-study echo probe, go in `results/preamble.md`. The echo is model-reported and labelled as such.

**Interleaving.** Samples run in blocks. One block is one rep of every arm for one type, in a rotated order (A B C D F, then B C D F A, and so on). Blocks are spread across nights. No arm is batched on its own. Each sample records its start time and the served model string so time-of-day and model-rollout effects can be checked.

**Resume.** One JSON per (type, arm, rep). A crashed run fills the gaps on restart; it never re-samples a completed cell.

**Throughput.** Measured 2026-11-10 (`throughput/2026-11-10-n100-c4-retry/`): 100 of 100 samples in 150 s at concurrency 4, about 2,400 samples per hour, median 4.3 s, p95 11.4 s, 692 input tokens median. 4 of 100 needed a retry. An earlier run with no retry lost 2 of 100 to silent empty output at startup (`throughput/2026-11-10-n100-c4-noretry/`); retries are counted per sample and published. The kill rule in section 10 (under 60 per hour) does not bind. The full design needs at most about 128 + 640 = 768 study samples.

## 8. Fixtures

Fixtures are synthetic. They contain no real client, employer, person or off-the-record material. Company and person names in fixtures are invented. A static leak scan (paths, emails, phones, a name allowlist) runs over `fixtures/`, `results/` and `reports/` before every publish.

Each type has one fixture: a task prompt and any context the task needs. The fixture is written by hand in the shape of the pipeline's own inputs (an event brief plus a task line), with every name invented. Fixtures: `fixtures/T1/` to `fixtures/T8/`. Allowlist of invented names: `fixtures/NAMES.txt`. Scan: `tools/leak_scan.py`.

**Realism gate (before the screen, target 2026-11-23 to 11-24).** For each type, Alex reads 3 control samples and confirms the control fails for the intended reason. If it fails for a different reason, the fixture gets one fix and the gate re-runs. A second wrong-reason result drops the type and the drop is recorded in `DEVIATIONS.md`. Samples read at the gate are not study samples and are not counted.

## 9. Grading

Order is fixed: code first, blind grader second, author third, outside graders last.

**Code grader.** Where the predicate can be checked by code (length, presence or absence of a marked string, counts, structure), the code check is the verdict. Every regex is tested on a seeded fixture before sign. Multiline mode on. A sample that quotes the rule instead of following it is sent to the blind grader, not counted by code.

**Blind grader.** A Sonnet call that sees only the sample, the fixture and the one predicate question. It never sees the style guide, the arm text, the arm label, other samples or the author's grade. It returns pass, fail or indeterminate with one quoted line of evidence. For types with a code check, the blind grader runs too; disagreement between code and grader is a published column and a triage signal, not a tie-break.

**Indeterminate.** Refusals, empty output, timeouts, harness errors, and outputs that do not attempt the task are `indeterminate`. They are excluded from `n_det` and counted separately. A refusal is never a pass. A cell with more than 4 indeterminate samples of 16 is marked `inconclusive` at the cell level and carries no p-value.

**Author read.** Alex reads every sample graded `fail` (every flagged match) and every code-vs-grader disagreement. He may overturn a grade with a one-line reason recorded next to the sample. Overturn counts are published per type. Any type where Alex disagrees with the blind grader on more than 20% of flagged samples is labelled `exploratory` in the results and is excluded from the confirmatory family in section 12.

**Outside graders.** Three practitioners, met at events, grade 30 samples each. The 90 samples are drawn stratified across RED types and arms, blind to arm and to each other's grades. Reported: Fleiss' kappa across the three, Cohen's kappa for each against the author grade, and the raw agreement rate with its chance-agreement baseline (a kappa without its baseline is not reported). Fewer than two graders by 2026-12-05: publish with author grading only and say so on the page.

**Second model.** After Phase 2, the best arm per RED type and arm A are re-run on a second model at 16 reps. This is a robustness check. It is secondary, labelled, and not part of the confirmatory family.

## 10. Stopping and kill rules

| Trigger | Action |
|---|---|
| Throughput under 60 samples/hour at 2026-11-14 | Shrink to the two-case design: two failure types chosen by the selection procedure's rank, arms A and B only, 16 reps. The shrink is written into `DEVIATIONS.md` before any study sample, the manifest is re-hashed, and the results page says the design was shrunk and why. |
| Hash layer not working by 2026-11-15 | Ship pass/fail with explicit denominators and the file hashes; add `indeterminate` before Phase 2. The pre-registration is never delayed for tooling. |
| No type RED by 2026-11-22 | Phase 2 does not run. Publish a null note: the model, behind this CLI, did not produce these failures without guidance at 16 reps. The note carries every cell's `k / n_det (16)`. This is a result and is published with the same seal. |
| A type fails the realism gate twice | Drop the type before the screen. Record it. |
| Blind grader vs author disagreement > 20% on a type | Type labelled exploratory. It stays in the tables. |
| Phase 1 complete | Phase 2 starts only on RED types. No new type is added. |
| Phase 2 complete (every cell at 16 attempts) | Sampling stops. The seal is written. Nothing is re-sampled. |

There is no early stop for a strong effect. There is no extension for a weak one. Sample counts are fixed at 16 per cell.

## 11. Deviations

A deviation is any difference between what this document says and what was done. Examples: a changed arm file, a fixture edit after sign, a dropped type, a re-run cell, a grader prompt change, a date missed, a different model string served.

Every deviation is one entry in `prereg/DEVIATIONS.md`, appended, never edited:

```
date · what changed · why · when discovered · which cells it touches · before or after unblinding · who decided
```

Deviations are listed in full in the results write-up under their own heading. A deviation that touches a confirmatory cell moves that cell's comparison to exploratory.

The registration hash is over the manifest at sign. The runner checks the manifest before each sample and refuses to sample on a mismatch. Fixing a mismatch is itself a deviation.

## 12. Analysis plan

Written before data. Run once, by a script in `graders/` or `reports/`, on the sealed results.

**Phase 1 (screen).** Per type: `k_A / n_det_A (16)`. RED if `k_A ≥ 5` and `n_det_A ≥ 12`. If `n_det_A < 12`, the type is `inconclusive` and does not enter Phase 2.

**Phase 2, primary (confirmatory family).** For each RED type that is not exploratory: Fisher exact test, two-sided, on the 2×2 table of fail vs not-fail for arm B against arm A, determinate samples only. Report the risk difference (A minus B) with a 95% Newcombe (Wilson-score) interval, the uncorrected p, and the Holm-adjusted p across the RED types. Family-wise alpha 0.05. The family size is the number of confirmatory RED types, at most 8. Holm is chosen because it controls family-wise error without an independence assumption and is more powerful than Bonferroni.

**Phase 2, secondary.** Within each RED type: C vs A, D vs A, F vs A (shaping types), and C vs B. Fisher exact two-sided, risk difference with interval. Holm-adjusted within the type across these comparisons. Labelled secondary.

**Exploratory.** Any comparison not listed above, any type labelled exploratory, the second-model re-run, and anything suggested by the data. Reported with uncorrected p only and marked exploratory.

**Variance column.** For every cell, the number of distinct output shapes across the 16 reps (as a count of unique normalised first lines and unique lengths in 50-character bins). Zero variance under an arm is reported as a signal that the guidance landed, not as a quality claim.

**Input length.** Arms differ in how much guidance they add: arms B and C add under 150 words, arm D about 2,800, and arm F about 12,500. Median input tokens are reported for every cell. Because length and content vary together in arms D and F, a difference between D or F and A cannot be attributed to content alone, and the results say so.

**Agreement.** Code-vs-blind disagreement rate per type. Author overturn rate per type. Outside-grader kappas per section 9, each with its chance baseline.

**Null baselines, stated with every number.** The do-nothing baseline for every arm is arm A in the same type. The baseline for every agreement statistic is chance agreement. A result within 0.10 of its baseline, or with zero variance across both arms, is reported as "no information", not as a small effect.

**What is not done.** No one-sided tests. No per-protocol trimming of samples. No reweighting. No choice of test after seeing data. No pooling across types for the primary analysis.

## 13. Publication

- Raw samples for every cell, with a `results/seal.json` holding the sha256 of each sample file. The renderer refuses to run on a mismatch and runs once, after every planned cell is complete.
- Grader code, grader prompts, arm files, fixtures, the manifest and its hash.
- Results tables in the format above, plus a section titled "What did not hold".
- The preamble disclosure (`results/preamble.md`).
- The deviation log in full.
- Outside-grader packets and grades, with grader identities replaced by G1, G2, G3.

Nothing in the write-up claims to be the first of anything. Prior art is cited in the README.

## 14. Timeline (from plan v4)

| Date | Gate |
|---|---|
| 2026-11-22 to 11-23 | Pre-registration signed and hashed. Throughput known. |
| 2026-11-23 to 11-24 | Fixture realism gate. |
| 2026-11-25 | Phase 1 screen complete. RED list, or the null note. |
| 2026-12-01 | Phase 2 complete. Seal written. |
| 2026-12-04 | Outside graders confirmed or author-only stated. |
| 2026-12-11 | Outside grades in. |
| 2026-12-15 | Write-up and dataset published. |

## 15. Signature

Signed by: Alex Yedibalian
Date: TODO
Registration hash: TODO
Manifest: `prereg/HASHES.json` (sha256 of this file with the hash and date fields blank, `failure-type-selection.md`, every file under `arms/`, `fixtures/` and `graders/`, the model id string, and the output of the pinned CLI's `--version` (`runner/PIN`))

Until the three TODO fields above are filled, no study sample may be generated.
