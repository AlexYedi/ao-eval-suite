# Deviations

Append-only. One entry per deviation, in the format set in `PREREG.md` section 11. Entries are never edited.

```
date · what changed · why · when discovered · which cells it touches · before or after unblinding · who decided
```

## D1

2026-11-14 · The model-vs-Alex agreement on comment labels (`failure-type-selection.md` §2.1 and §9) is not reported, and Alex does not hand-label the comment export. · The export held 17 comments, below the 60-comment trigger in §1, so the fallback source supplied the failure types. The comment labels feed nothing in the selection, so labelling them would measure agreement on a step the study did not use. The model's first-pass class counts for the 17 comments (voice 8, structure 5, process 3, fact 1; majority-class baseline 8/17 = 0.47) are still published. · Discovered 2026-11-11, when the comment sweep finished. · No study cells: logged before sign and before any sample exists. · Before unblinding. · Alex Yedibalian (Linear YED-402).

## D2

2026-11-22 · The Phase 1 screen (128 arm-A samples, T1–T8 × 16 reps) runs in one session on 2026-11-22, not as blocks spread across nights (section 7, Interleaving). Samples still run in block order (rep r of every type before rep r+1), four at a time. · Alex chose to have the screen result now rather than on the night of 11/25. Phase 1 has one arm, so the rule that no arm is batched on its own cannot bind; the cost is that a time-of-day or model-rollout effect within one session is not averaged out across nights. Every sample records its start time and the model that served it, so this can be checked, and is reported with the results. · Discovered 2026-11-22, reading section 7 before the run. · All Phase 1 cells (T1–T8 × A); no Phase 2 cell. · Before any study sample exists (before unblinding). · Alex Yedibalian (Linear YED-494).
