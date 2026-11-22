# Deviations

Append-only. One entry per deviation, in the format set in `PREREG.md` section 11. Entries are never edited.

```
date · what changed · why · when discovered · which cells it touches · before or after unblinding · who decided
```

## D1

2026-11-14 · The model-vs-Alex agreement on comment labels (`failure-type-selection.md` §2.1 and §9) is not reported, and Alex does not hand-label the comment export. · The export held 17 comments, below the 60-comment trigger in §1, so the fallback source supplied the failure types. The comment labels feed nothing in the selection, so labelling them would measure agreement on a step the study did not use. The model's first-pass class counts for the 17 comments (voice 8, structure 5, process 3, fact 1; majority-class baseline 8/17 = 0.47) are still published. · Discovered 2026-11-11, when the comment sweep finished. · No study cells: logged before sign and before any sample exists. · Before unblinding. · Alex Yedibalian (Linear YED-402).

## D2

2026-11-22 · The Phase 1 screen (128 arm-A samples, T1–T8 × 16 reps) runs in one session on 2026-11-22, not as blocks spread across nights (section 7, Interleaving). Samples still run in block order (rep r of every type before rep r+1), four at a time. · Alex chose to have the screen result now rather than on the night of 11/25. Phase 1 has one arm, so the rule that no arm is batched on its own cannot bind; the cost is that a time-of-day or model-rollout effect within one session is not averaged out across nights. Every sample records its start time and the model that served it, so this can be checked, and is reported with the results. · Discovered 2026-11-22, reading section 7 before the run. · All Phase 1 cells (T1–T8 × A); no Phase 2 cell. · Before any study sample exists (before unblinding). · Alex Yedibalian (Linear YED-494).

## D3

2026-11-22 · Phase 2 author read (section 9): instead of reading every sample graded fail and every code-vs-blind disagreement, the author reads (a) every item a three-judge panel raises, and (b) a 10% random audit of the items the panel auto-accepts, mixed in unmarked. The panel (`tools/panel.py`, `tools/panel_prompt.md`) gives each covered item to three judges on different models (claude-sonnet-5-5, claude-opus-5-5, claude-fable-5-2), asking the author's question: is this a genuine instance of the habit? An item is auto-accepted only if all three say yes with high confidence, code and blind agree, and the match is not only inside quoted material. Everything else is raised. The audit sample is seeded from the item ids. · Alex asked for an automated reviewer that raises only edge and borderline cases, to cut the author read to the cases that need judgment. Before use, the panel was calibrated on the 34 Phase 1 items the author had already decided (`results/phase1/panel-calibration.md`); the acceptance rule was that no author overturn is auto-accepted. · Discovered (decided) 2026-11-22, after the Phase 1 author read and before any Phase 2 sample. · Every Phase 2 cell (T5, T8 × A–D). The author overturn rate and the "exploratory" rule (author disagrees with the blind grader on more than 20% of flagged samples) are computed on the items the author read, and the results report the panel's raise rate, the audit size and the author-vs-panel agreement on the audit with its chance baseline. Phase 1 is unaffected: its author read was complete. · Before any Phase 2 sample exists (before unblinding). · Alex Yedibalian (Linear YED-501).

## D4

2026-11-22 · The Phase 2 run (128 samples, T5 and T8 × arms A, B, C, D × 16 reps) runs in one session on 2026-11-22, not as blocks spread across nights (section 7, Interleaving). Blocks keep the signed structure: one rep of every arm for one type, arms in rotated order (A B C D, then B C D A, and so on). · Alex chose to run Phase 2 now. Interleaving within each block still prevents any arm from being batched on its own; the cost, as in D2, is that a time-of-day or model-rollout effect within one session is not averaged across nights. Every sample records its start time and the model that served it. · Discovered (decided) 2026-11-22, before the Phase 2 run. · Every Phase 2 cell. · Before any Phase 2 sample exists (before unblinding). · Alex Yedibalian (Linear YED-501).
