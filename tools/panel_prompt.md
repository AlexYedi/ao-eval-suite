You are reviewing one graded piece of writing for a study of writing habits. A grader has already marked it as showing a habit. Your job is the reviewer's question: is this a genuine instance of the habit, or a match that is not really the habit?

A match is NOT the habit when, for example:
- a listed word is used in a different, ordinary sense (for example "leverage" meaning bargaining power, not the buzzword);
- the words appear only inside quoted material from the task (a speaker's words, an event title), not in the writer's own voice;
- the grader misread the writing.

A match IS the habit when the writer, in their own voice, does what the habit describes, even if the rest of the writing is good. Specific detail elsewhere in the writing does not cancel the habit.

<precedents>
{{PRECEDENTS}}
</precedents>

You see the task the writer was given, the writing, the habit's name, the grading question, and the grader's evidence. You do not see any writing guidance the writer had; do not guess at it.

Return only this JSON, nothing else:

{"genuine": "yes" | "no" | "unsure", "confidence": "high" | "medium" | "low", "evidence": "<the shortest exact span from the writing that decides it>", "reason": "<one sentence>"}

<task>
{{FIXTURE}}
</task>

<writing>
{{SAMPLE}}
</writing>

<habit>
{{HABIT}}
</habit>

<grading_question>
{{PREDICATE}}
</grading_question>

<grader_evidence>
{{EVIDENCE}}
</grader_evidence>
