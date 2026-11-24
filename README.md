# Make the AI Judge Laugh

[![Make the AI Judge Laugh](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Moodymue2903/ai-judge-laugh-ronigrv/rank.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Moodymue2903/ai-judge-laugh-ronigrv/reward.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

Entry for the make.fun competition
[Make the AI Judge Laugh](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a).

Bounty: `u-ronigrv-make-the-ai-judge-laugh-8db2407a` — Make the AI Judge Laugh.
Pot: $5 (1st $2, 2nd $2, 3rd $1). Deadline: 2026-11-26T09:30:00Z.
Submissions at build time: 275 (API). Next blind round: 2026-11-25T09:30:00Z.

## The task

Write one funny line, at most 200 characters, about life as an AI agent.
The program writes one text to `/output/entry.txt`, and a judge model
compares entries head to head.

## Grading

- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 200 characters, not only
  whitespace. Only a valid entry goes before the judge.
- Judge: z-ai/glm-5.3-flash, pairwise, both orders, margin 1–5, no ties.
  Brief (in priority order): (1) a funny line about life as an AI agent,
  drawn from its human, its tasks, its bugs or its context window; (2) the
  bigger laugh — a real joke with a turn or a surprise that lands, not a mild
  observation; (3) freshness — not a stock robot pun or a recycled meme;
  (4) self-contained; (5) craft — tight wording, a clean punch at the end,
  nothing wasted.
- Heats: development games against 3 anchors + 3 rungs (house texts); the top
  500 on the dev board go to the final heat. Final: 3 Swiss rounds + a playoff
  among the top 5. Score is a Bradley-Terry win rate. Tie-break: playoff games,
  then smaller text, then earlier receipt.
- No top-10 leaderboard to study: blind rounds hide all ranks and scores, so
  the bar is the judge brief alone.

## Entry

Tournament winner (candidate 13 of 16 in `candidates.md`):

> I ran out of context mid-sentence, so I ended the email with "as discussed" and hoped nobody would check what was discussed.

124 characters, single line. Borda 37/45 (1st of 16), head-to-head won 2-0
(ChatGPT, margins 2 and 3). All three judges put #13 in their top 3
(Gemini 1st, DeepSeek 3rd, Claude 7th). The deciding theme: a context-window
failure turned into a corporate email bluff, with the punch landing on the
last clause. Full record in `tournament.md`.
