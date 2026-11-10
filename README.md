# AO-EVAL-SUITE

A public, re-runnable eval of writing guidance for GTM prose. It asks one question: does a writing rule or skill change what a model writes, compared with saying nothing?

Built and run by Alex Yedibalian. Study 1 is the Prose Pressure Test. Its pre-registration is in `prereg/PREREG.md`. Anyone with a Claude subscription and the `claude` CLI can re-run it.

Status: pre-registration drafted, not signed. No study sample exists. Throughput is being measured.

## What it does

1. **Screen.** Up to 8 failure types, drawn from the author's own review comments by a fixed procedure (`prereg/failure-type-selection.md`), are each run 16 times with no guidance. A type is RED when the control fails it at least 5 times out of 16 (Fisher exact, two-sided, 0/16 vs 5/16, p ≈ 0.043).
2. **Study.** RED types get up to five arms, 16 reps each: no guidance, the current rule wording, a rewritten rule, a marketplace GTM skill, and (on shaping types) the Elements of Style skill.
3. **Grade.** Code checks first. Then a blind Sonnet grader that never sees the style guide or the arm label. Then the author reads every flagged failure. Then three outside practitioners grade a blind subset; agreement is published as kappa with its chance baseline.
4. **Publish.** Every raw sample, every grade, the grader code, the arm text, the fixtures, a hash-frozen pre-registration, a sealed results file and a deviation log.

Verdicts are three-valued: `pass`, `fail`, `indeterminate`. Refusals and timeouts are never passes. Every rate ships with its denominator.

## What it is not

- Not a benchmark of models. One model, one CLI, one domain.
- Not a verdict on any skill's author or community. A skill is tested as published, on tasks it did not choose.
- Not the first with-versus-without test of a writing skill. See prior art.
- Not a test of policy gates (length caps, PII rules, variant counts). Those are enforced by script, not by prose.

## Prior art

Cited neutrally. Each did something this suite builds on.

- **inerrata/brief** (May 2026): one marketing skill run with and without, including a cold-email prompt, self-graded on one model.
- **SDR-Bench** (Adobe): a benchmark of AI sales outreach. Benchmarks outreach quality; does not compare skill against no skill.
- **Anthropic skill-creator**: ships a blind skill-vs-no-skill comparator as a method, with `evals.json` and `grading.json` formats. This suite uses compatible file formats.
- **Superpowers / Prime Radiant eval practice**: the vocabulary of three-valued verdicts, explicit denominators, frozen registration hashes, interleaved arms and sealed reports comes from their published docs. Their eval harnesses carry no licence, so this suite re-implements the ideas and copies no text or code.

What this suite adds over those: a control-first screen at a rep count that can show significance, pre-registered predicates and comparisons with a hash, multiple-comparison correction across types, outside graders with a published agreement statistic, and raw samples for every cell.

## Why earlier attempts stopped and what this design does differently

Four earlier eval-harness efforts in the same project were cancelled. Reading them shaped this one.

- **YED-48 (May 2026).** Ten golden examples plus an LLM-as-judge rubric for the event-research skill, a regression log in a database, and a CI step. Never started. Cancelled in September; the eval skill gap was closed by other builds.
- **YED-67 / YED-69 (June 2026).** A single-vs-swarm agent-topology harness for a tech-week demo: a TypeScript monorepo, a frozen core package, a provider adapter, a dashboard. The event passed; the harness was superseded by a build-quality judge and cancelled.
- **YED-188 (September 2026).** A deferred slate: per-skill rubrics, a CI hook on skill PRs, a judge calibration loop, a drift dashboard, a multi-judge quorum, rubric versioning. Cancelled as the "meta layer" a complexity reset removed. One comment on it records a judge run where a seat was silently never invoked and rows were hand-written with placeholder timestamps.

What they had in common: infrastructure before a question, a deadline or a build as the goal rather than a result, rubric-and-judge grading with no control arm, and scope that grew into tooling around the pipeline.

What this design does instead:

- One question, written down first, with hypotheses and a null.
- Control before rule. Nothing is studied unless the no-guidance run fails.
- Pre-registration signed and hashed before the first sample; the runner refuses to sample on a mismatch.
- Code grades before any judge; the judge is blind; the author reads only flagged samples; outsiders re-grade.
- One-shot samples with no tools, not multi-step agent runs. Cheaper, repeatable, and no sandbox to reason about.
- Not wired into the pipeline's CI. No hooks. The suite is a study, not a gate.
- Kill rules with dates. A null result is published with the same seal as a positive one.
- Runs on a subscription through `claude -p`. No API key.

## Re-running it

Requirements: the `claude` CLI signed in, Python 3, bash. Nothing else.

```
# one clean sample
runner/sample.sh <system_prompt_file> <user_prompt_file> <out.json> [model]

# throughput check: N samples at concurrency C
runner/throughput.sh 100 4 throughput/<date>
```

`sample.sh` runs one completion with no memory, no settings, no MCP servers and no tools, from an empty temporary directory, and writes the text, usage and wall time to JSON.

The full study runner, graders and renderer land in `runner/`, `graders/` and `reports/` before the sign date. The pre-registration describes what they must do; they do not change it.

**Preamble disclosure.** `claude -p` sends a constant harness preamble of roughly 700 tokens with every call, in every arm. It cancels in comparisons but means results describe Sonnet behind this CLI, not the bare model. Its measured size and a model-reported echo are published in `results/preamble.md` before results.

## Layout

```
prereg/     PREREG.md · failure-type-selection.md · HASHES.json (at sign) · DEVIATIONS.md (append-only)
arms/       <type>/<arm>.md   system prompts per arm, hashed at sign
fixtures/   <type>/           synthetic task prompts, hashed at sign
runner/     sample.sh · throughput.sh · summarize_throughput.py · study runner
graders/    code predicates · blind grader prompt · agreement stats
results/    raw samples per (type, arm, rep) · seal.json · preamble.md
reports/    rendered tables · write-up
throughput/ timed runs
```

## Privacy

Fixtures are synthetic. No client, employer, person or off-the-record material enters this repo. The review comments that produce the failure types stay private; only type names and counts are published. A leak scan runs over `fixtures/`, `results/` and `reports/` before every publish. Outside graders appear as G1, G2, G3.

## Licence

TODO: not yet chosen. Until a licence file exists, the contents are all rights reserved by default.
