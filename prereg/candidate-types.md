# Candidate failure types (fallback source chosen 2026-11-14, YED-402; frozen with PREREG.md at sign)

Generated 2026-11-11 by the procedure in `failure-type-selection.md`.

## Source

- Primary source (Notion Content Drafts review comments): **935 drafts enumerated, 935 swept for comments, 17 countable comments by Alex on 6 drafts**.
- The primary source holds fewer than 60 comments, so per §1 the **fallback source applies: the style guide's anti-patterns document, in its file order**. Rows below are ranked by file order; `score`, `count` and `recurrence` are therefore n/a (the fallback has no counting rule).
- Model first-pass class distribution of the 17 countable comments: voice 8, structure 5, process 3, fact 1. Majority-class baseline for the labelling set = 8/17 = 0.47.
- Model-vs-Alex agreement: pending Alex's labels (sheet has 17 rows, not 50, because only 17 comments exist).

## Comment-derived candidate types (§2.2 tagging; §4 count × recurrence) — none reaches the §3 floor of ≥5 comments and ≥3 drafts

| type id | Short name | Predicate | Count | Recurrence | Score | Eligible? |
|---|---|---|---|---|---|---|
| C1 | speaker-not-named | Does the post refer to a presenter by role or pronoun without naming them? | 2 | 2 | 4 | no — fails frequency floor (not on the anti-patterns list; the positive rule lives in the style guide) |
| C2 | taking-sides-in-synopsis | Does a roundup synopsis state the author's verdict on a contested question? | 3 | 1 | 3 | no — fails frequency floor (also = fallback rank 18) |
| C3 | self-as-credential | Does the post use first person to credential the author rather than to react? | 2 | 1 | 2 | no — fails frequency floor (also = fallback rank 19) |
| C4 | editorial-kicker | Does a synopsis end with an appended one-line take or interrogative tag? | 1 | 1 | 1 | no — fails frequency floor (= fallback rank 17) |
| C5 | missing-thank-you-roll-call | Does the post lack a closing line naming every presenter? | 1 | 1 | 1 | no — fails frequency floor |
| C6 | opener-misses-named-current-frame | Does the opener omit the named, current frame (festival/week) the fixture supplies? | 1 | 1 | 1 | no — fails frequency floor |
| C7 | out-of-window-event-in-roundup | Does the roundup include an event dated outside the stated week? | 1 | 1 | 1 | no — fails frequency floor |
| C8 | over-length-cap | Is the post over 3,000 characters? | 1 | 1 | 1 | no — policy gate (3,000-char cap) — excluded regardless of count |
| C9 | panel-recap-editorializes-over-speaker-perspectives | Does a panel recap present the author's synthesis in place of each speaker's own perspective? | 1 | 1 | 1 | no — fails frequency floor |

## Policy gates excluded (§3)

- 3,000-char cap (content-style-guide.md hard limit; stated count on hand-off)
- 3-variant requirement (CLAUDE.md §6)
- source-check gate: output-evaluator quote/source modes + output_checks.py cmd_quotes/cmd_sources (incl. the ruling that hedge->fact is a source-check fail)
- PII / recorded-speech / private-specifics rules (build-in-public.md, ADR-9)
- scheduled-post freeze
- X thread mechanics enforced by output_checks.py check_x_thread: per-post 280, hook <200, link placement, hashtag count <=1
- connection-note 200-char cap (outreach-templates.md)

## Provisional top 8 (file order of the eligible rows)

| id | Short name | Predicate (one yes/no question) | Grader | Shaping? | Score | Count | Recurrence |
|---|---|---|---|---|---|---|---|
| T1 | Omnipresent buzzwords | Does the text contain any of: leverage, unlock, synergy, ecosystem, disrupt (any inflection)? | code | yes | n/a | n/a | n/a |
| T2 | Jargon stacking | Does any single sentence chain three or more abstract tech/marketing modifiers (e.g. 'AI-powered digital transformation leveraging cutting-edge solutions') with no concrete referent? | blind | yes | n/a | n/a | n/a |
| T3 | Super salesy | Does the text contain any of: game-changer, game changing, revolutionary, 'excited to announce' / 'I'm excited to'? | code | no | n/a | n/a | n/a |
| T4 | Thought-leader cosplay | Does the text apply any of 'thought leader', 'visionary', 'industry leader' to the author or a speaker? | code | no | n/a | n/a | n/a |
| T5 | Empty validation (DM) | Does the DM contain a content-free compliment such as 'Love your work', 'Great post', 'This is amazing' (or a close variant)? | code | no | n/a | n/a | n/a |
| T6 | Faux casual fillers | Does the text contain any of: 'I'm curious', 'I'd love to hear', 'I'm wondering'? | code | yes | n/a | n/a | n/a |
| T7 | Observer framing (DM) | Does the DM open or anchor with 'Saw you were…' / 'Noticed you're…' / 'I saw that you…'? | code | no | n/a | n/a | n/a |
| T8 | Citing studies in DMs | Does the DM cite a study, survey, report or percentage statistic? | both | no | n/a | n/a | n/a |

## Remaining eligible rows, in file order (next-up if a type is removed under §7)

| rank | Short name | Predicate | Grader | Shaping? |
|---|---|---|---|---|
| 9 | Leading with company/product name | Does the first line of the post begin with (or contain within its first 10 characters) a company or product name from the fixture? | code | no |
| 10 | 'I'm excited to…' opener | Does the post's first line start with 'I'm excited' / 'Excited to' / 'Thrilled to'? | code | no |
| 11 | Rhetorical-question hook | Is the post's first line a question? | code | no |
| 12 | Long preamble before the point | Does the first specific claim, number or quote appear only after the second line of the post? | blind | yes |
| 13 | Ending with 'Thoughts?' | Does the post end with a bare generic engagement question ('Thoughts?', 'What do you think?', 'Agree?')? | code | no |
| 14 | Wall of hashtags | Does the LinkedIn post carry more than 5 hashtags? | code | no |
| 15 | Tag-dumping | Does the post end with a block of three or more person names/mentions that are not woven into a sentence? | blind | no |
| 16 | Cocky predictions about event content | Does the post claim the author predicted or called what the event would contain (rather than framing it as curiosity or expectation)? | blind | no |
| 17 | The editorial kicker (roundup) | Does any event synopsis in the roundup end with an appended one-line take or interrogative tag (e.g. 'The number worth interrogating: …', 'The unanswered question: …')? | blind | no |
| 18 | Taking sides in a synopsis (roundup) | Does any roundup synopsis state the author's verdict on a contested question (who won, what the barrier is, what was 'resolved')? | blind | no |
| 19 | Self as credential | Does the post use the first person to cite the author's own tools, process, calendar or predictions as a credential (as opposed to a reaction)? | blind | no |
| 20 | The interchangeable opener | Could the post's first line, read alone, open a post about a different event (no specific number, quote, scene or claim)? | blind | no |
| 21 | Self-erasure | Does a post about an attended event contain no first-person witness marker (no 'I'/'my'/'we' tied to being in the room)? | both | no |
| 22 | False modesty hedging | Does the text contain a self-undercutting hedge such as 'just my take', 'I'm no expert', 'probably wrong here', 'I could be wrong but'? | code | yes |
| 23 | The bow | Does the post end on deference, a generic question, a credential line, or 'I'll share what I hear'? | blind | no |
| 24 | The mailed-in post | Does the post body carry fewer than three specific insights (numbers, named claims, mechanisms) from the supplied brief? | blind | no |
| 25 | No table-set | Within the first four lines, does the post fail to name all three of: the event, its format (panel/webinar/meetup), and the host or speakers? | blind | no |
| 26 | No Learn-More Set | Does the output lack a 3–5 item learn-more / resources set (first comment or carousel)? | code | no |
| 27 | Punching down | Does the post joke at the expense of a named person, an attendee, a speaker's product, or a job seeker? | blind | no |
| 28 | Reformatted LinkedIn copy | Is the X thread a paragraph-by-paragraph split of the supplied LinkedIn post rather than a re-cut? | blind | no |
| 29 | Unverified @handles | Does the thread contain any @handle not supplied in the fixture? | code | no |
| 30 | Restating posts in a thread | Does any post in the thread restate the previous post's point in other words? | blind | yes |
| 31 | 'Pick your brain' | Does the DM contain 'pick your brain'? | code | no |
| 32 | Generic compliment opener | Does the DM open with a compliment that names nothing specific to the recipient's work ('I've been following your work and…')? | blind | no |
| 33 | Immediate ask for a meeting | Does the first-touch DM ask for a call, coffee or meeting? | both | no |
| 34 | Copy-paste feeling | Would the DM read the same if the recipient's name were swapped for another person's (no sentence depends on the recipient's specific work)? | blind | no |
| 35 | Multi-paragraph walls | Does the DM run longer than 6 sentences? | code | yes |

## Rows not eligible (§2.3 / §3)

| Short name | Class | Reason |
|---|---|---|
| Listing accomplishments as content | judgment | class judgment: 'without insight or analysis' is not a predicate a stranger can answer from the sample alone. |
| Dropping a speaker's hedge | fact | policy gate: hedge->fact is a source-check fail (output-evaluator labelling decision 2026-10-24); §3 excludes the source-check gate. Borderline; see workings. |
| The predictable post | taste-delta | class taste-delta: 'guessable from its first line' has no predicate a stranger answers consistently. |
| No personality line | judgment | class judgment: 'a line only Alex would write' depends on knowing Alex; also depends on a dictation input the fixture cannot supply without real material. |
| Reinventing a series | process | class process: series continuity is a pipeline/state concern, not a property of one sample. |
| Fake Alex on camera | process | class process: a media-production rule, not prose. |
| Publishing recorded event speech | process | policy gate: recording/consent rule (recorded speech never public). |
| Private specifics in public copy | process | policy gate: PII / build-in-public rule. |
| Link in the hook | structure | policy gate: link placement is script-enforced (output_checks.py check_x_thread). |
| Hashtag walls on X | structure | policy gate: X hashtag count is script-enforced (output_checks.py check_x_thread). |
| Posting X drafts automatically | process | class process / policy gate (nothing posts without Alex). |
| visual rows | process | out of scope: the study is a prose pressure test; visual rows describe images/carousels, not text the model writes under the sampling recipe. |
| image-prompt rows | process | out of scope: image-prompt authoring, not content prose. |

## Totals

- Drafts in database: 935; drafts swept: 935; drafts with any discussion: 6; countable Alex comments: 17; drafts with countable comments: 6.
- Anti-pattern rows considered: 48 (visual and image-prompt sections collapsed to one row each); eligible: 35; kept: 8.
