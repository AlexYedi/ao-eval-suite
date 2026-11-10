# Failure-type selection procedure

Part of the pre-registration (`prereg/PREREG.md`, section 5). Frozen with it. The list this procedure produces is pasted into PREREG.md section 5 at sign; nothing else goes into that table.

## 1. Source

Alex's inline review comments on drafts in his Notion Content Drafts database. These are the record of what he corrects when he reads what the pipeline wrote. The export is private and stays in a private state directory. Only the type names, the counts and the final list leave it.

Fallback source if the export holds fewer than 60 comments in total: the style guide's anti-patterns document, in its file order. The results page says which source was used.

## 2. Classification

1. Every comment is classified once into one of six classes: fact, voice, structure, process, judgment, taste-delta. A model does the first pass. Alex hand-labels the first 50 comments in export order. The model's agreement with Alex's 50 labels is reported against the majority-class baseline (the rate you get by labelling everything with the most common class).
2. Within the classes voice, structure and fact, each comment is further tagged with one candidate failure type. A failure type is a short name plus one yes/no predicate (for example "the post states a hedged claim as fact"). The candidate list is open while tagging and closed when tagging ends.
3. Comments in the classes process, judgment and taste-delta are not candidates. Process comments are about the pipeline, not the prose. Judgment and taste-delta comments have no predicate a stranger could answer from the sample alone.

## 3. Eligibility

A candidate type is eligible only if all of these hold:

- **Predicate-able.** One yes/no question, answerable from the sample and the fixture, by code or by a blind grader with no access to the style guide.
- **Not a policy gate.** Floors that the pipeline enforces by script or by rule rather than by prose guidance are excluded: the 3,000-character cap, the three-variant requirement, the source-check gate, PII rules, scheduled-post freezes. A control test on a policy gate measures the script, not the model.
- **Minimum frequency.** At least 5 comments and at least 3 distinct drafts.
- **Fixture-able.** A synthetic fixture can be written that gives the model the chance to make the failure without any real name, client or confidence.

## 4. Counting rule

Score = count × recurrence, where:

- **count** is the number of comments tagged with the type, after the model and Alex's labels are reconciled (Alex's label wins on the 50 he labelled);
- **recurrence** is the number of distinct drafts on which the type appears at least once.

A comment that names two types counts once for each. A thread of replies on one comment counts as one comment. Comments Alex wrote on his own edits count; comments that are only "ok" or "done" do not.

## 5. Ranking and the cut

1. Sort eligible types by score, descending.
2. Take the top 8. Fewer than 8 eligible types means fewer rows; the list is not padded.
3. Each kept type is tagged `shaping: yes` or `shaping: no`. Yes means a rule in the public-domain Strunk text plainly applies to the predicate (needless words, needless qualifiers, restating, passive where active was meant, and the like). The tag decides whether arm F runs. It is set at this step and not changed.

## 6. Tie-break

Applied in order until the tie is gone:

1. Higher recurrence (more distinct drafts).
2. More recent last comment date.
3. The type whose predicate can be checked by code ranks above one that needs the blind grader.
4. Alphabetical by type id.

## 7. Who decides

- The session proposes the candidate list, the tags, the scores and the ranked table.
- Alex labels the 50 comments, resolves any type whose predicate he thinks is wrong, and signs the final list.
- Alex may remove a type from the top 8 for one reason only: the predicate cannot be made fixture-able without real material. The removal and the reason are written in `DEVIATIONS.md` before sign, and the next-ranked type moves up.
- Alex may not add a type that the ranking did not produce. Hand-picked cases were the design this procedure replaces.

## 8. Freeze

The ranked table, the scores, the shaping tags and the predicates are written into PREREG.md section 5 and hashed at sign. After sign:

- no type is added;
- a type may be dropped only by the realism gate (PREREG.md section 8) or the indeterminate rule (section 9), and only with a deviation entry;
- a predicate's wording does not change. If a predicate turns out to be ungradeable, the type is dropped, not reworded.

## 9. What is published

The type ids, short names, predicates, shaping tags, scores, counts and recurrence numbers. The total comment count and the number of drafts. The model-vs-Alex agreement on the 50 labels with its majority-class baseline.

What is not published: any comment text, any draft text, any draft title, any date that identifies an event.
