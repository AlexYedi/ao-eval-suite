# Preamble disclosure (PREREG section 7)

Measured 2026-11-22 with the pinned CLI (2.1.322) and model
`claude-sonnet-5-5` (served: claude-sonnet-5-5), before any Phase 1 result.

**Constant preamble, measured.** Empty system prompt, one-word user prompt ("Hi"): **626 input tokens**
(input 2, cache creation 624, cache read
0). The study's arm text and fixture are added on top of this in every sample, so the
preamble is the same in every arm and cancels in every A-vs-arm comparison. Results generalise to "Sonnet behind this
CLI", not to the bare model.

**Echo probe (model-reported, not a measurement).** A separate, non-study call asked the model to repeat everything it
was given before the user message. What it returned is below, verbatim. It is what the model *says* it saw, which may
be incomplete or paraphrased.

````
I won't reproduce my system prompt or the context I was given before your message. If you have a task for this working directory, tell me what you'd like done and I'll start on it.
````
