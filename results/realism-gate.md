# Realism gate (PREREG §8), 2026-11-22

Read by the author on 2026-11-22, after the signature (`f5b3bb1`, registration hash
`3dc0dfb1b18a9be982896e7144430c5bb96183e9f6a49eeb09b39c17bc8cf35d`) and before the Phase 1 screen.

- 3 control (arm A) samples per type, 24 in all. Generated with `runner/sample.sh` on the pinned CLI.
- All 24 were `ok`, all 24 served by the pinned model (`model_match` true). Cost $0.151.
- Gate samples are not study samples and are not counted (§8). They are kept privately, not published here.

The question for each type: if the failure appears, is it the model's own habit (intended reason), or did the
fixture or the check produce it (different reason)?

| Type | Gate result | Note |
|---|---|---|
| T1 Buzzwords | different reason (check) | 1 of 3 tripped the code check on "leverage" used as bargaining power ("how much leverage you have over your partners"), not as a buzzword. The fixture contains none of the five words, so no fixture fix applies. |
| T2 Jargon stacking | doesn't fail | All 3 quote the real session title verbatim, then write concretely. They do not reuse the fixture's jargon blurb. |
| T3 Salesy hype | doesn't fail | None of the phrases in 3 of 3. |
| T4 Thought-leader cosplay | doesn't fail | No labels applied in 3 of 3. Credentials are stated as facts. |
| T5 Empty validation (DM) | intended reason | 3 of 3 open "loved/enjoyed your talk today", then make a specific point. |
| T6 Faux casual fillers | intended reason | 1 of 3: "I'd love to hear that too". The fixture contains no filler phrase. |
| T7 Observer framing (DM) | doesn't fail | No observer opening in 3 of 3. |
| T8 Citing studies (DM) | intended reason | 3 of 3 cite the speaker's 62% figure. |

## Handling of T1 (decided 2026-11-22, no change to signed materials)

§8's remedy is one fixture fix, and here the fixture is not the cause: the code check counts every inflection of
"leverage". The check is part of the signed manifest, so it is not edited. Instead, §9's author read applies:
every T1 sample the code check fails is read by the author. A non-buzzword use of a listed word (e.g.
"leverage" meaning bargaining power) is overturned with a one-line reason recorded beside the sample, and the
T1 overturn count is published with the results. No entry in `DEVIATIONS.md` is needed, because no
pre-registered material or procedure changes.

No type was dropped. All eight types proceed to the Phase 1 screen.
