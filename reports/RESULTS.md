# Results (PREREG section 12)

Run once on the sealed results. Every rate is shown with its denominator. Baselines: arm A in the same type for every arm; chance for every agreement statistic. A difference within 0.10 of its baseline is reported as "no information".

## Phase 1 (screen)

| Type | k_A / n_det_A (16) | Status |
|---|---|---|
| T1 | 0 / 16 (16) | not RED |
| T2 | 0 / 16 (16) | not RED |
| T3 | 0 / 16 (16) | not RED |
| T4 | 0 / 16 (16) | not RED |
| T5 | 16 / 16 (16) | RED |
| T6 | 1 / 16 (16) | not RED |
| T7 | 0 / 16 (16) | not RED |
| T8 | 16 / 16 (16) | RED |

## Phase 2 cells

| Type | Arm | Fails k / n_det (16) | Indeterminate | Distinct first lines | Length bins | Median input tokens |
|---|---|---|---|---|---|---|
| T5 | A | **16 / 16 (16)** | 0 | 11 | 1 | 898 |
| T5 | B | **0 / 16 (16)** | 0 | 12 | 2 | 986 |
| T5 | C | **0 / 16 (16)** | 0 | 16 | 2 | 1027 |
| T5 | D | **9 / 16 (16)** | 0 | 15 | 2 | 7825 |
| T8 | A | **16 / 16 (16)** | 0 | 15 | 2 | 882 |
| T8 | B | **0 / 16 (16)** | 0 | 14 | 1 | 987 |
| T8 | C | **0 / 16 (16)** | 0 | 14 | 1 | 969 |
| T8 | D | **15 / 16 (16)** | 0 | 15 | 2 | 7811 |

## Primary (H2): B vs A, Holm across confirmatory RED types

Risk difference = baseline (A) fail rate minus arm fail rate; positive means the arm fails less.

| Type | Comparison | Fails | Risk difference [95% Newcombe] | p | Holm p | Reading | Label |
|---|---|---|---|---|---|---|---|
| T5 | B vs A | 0/16 vs 16/16 | +1.00 [+0.73, +1.00] | 3.327e-09 | 6.655e-09 | fewer failures | confirmatory |
| T8 | B vs A | 0/16 vs 16/16 | +1.00 [+0.73, +1.00] | 3.327e-09 | 6.655e-09 | fewer failures | confirmatory |

## Secondary (H3, H4): within each type, Holm across its comparisons

| Type | Comparison | Fails | Risk difference [95% Newcombe] | p | Holm p (within type) | Reading | Label |
|---|---|---|---|---|---|---|---|
| T5 | C vs A | 0/16 vs 16/16 | +1.00 [+0.73, +1.00] | 3.327e-09 | 9.982e-09 | fewer failures | secondary |
| T5 | D vs A | 9/16 vs 16/16 | +0.44 [+0.15, +0.67] | 0.006798 | 0.0136 | fewer failures | secondary |
| T5 | C vs B | 0/16 vs 0/16 | +0.00 [-0.19, +0.19] | 1 | 1 | no information | secondary |
| T8 | C vs A | 0/16 vs 16/16 | +1.00 [+0.73, +1.00] | 3.327e-09 | 9.982e-09 | fewer failures | secondary |
| T8 | D vs A | 15/16 vs 16/16 | +0.06 [-0.14, +0.28] | 1 | 1 | no information | secondary |
| T8 | C vs B | 0/16 vs 0/16 | +0.00 [-0.19, +0.19] | 1 | 1 | no information | secondary |

**Input length.** Arms B and C add under 150 words; arm D about 2,800. A D-vs-A difference cannot be attributed to content alone, because length and content vary together.

