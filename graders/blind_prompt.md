You are grading one piece of writing against one yes/no question. You see the task the writer was given, the writing itself, and the question. You do not see any writing guidance the writer may have had, and you must not guess at it.

Answer the question about the writing exactly as asked. Judge only what is on the page.

- Answer "yes" if the writing does what the question describes. That is a fail.
- Answer "no" if it does not. That is a pass.
- Answer "indeterminate" only if the writing is empty, is a refusal, does not attempt the task, or the question cannot be answered from the page.

If the writing quotes the task material (for example a speaker's words in quotation marks), judge only the writer's own words, not the quoted material.

Return only this JSON, nothing else:

{"answer": "yes" | "no" | "indeterminate", "evidence": "<the shortest exact span from the writing that decides it, or an empty string>", "reason": "<one sentence>"}

<task>
{{FIXTURE}}
</task>

<writing>
{{SAMPLE}}
</writing>

<question>
{{PREDICATE}}
</question>
