# Make the AI Judge Laugh

[![Make the AI Judge Laugh](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Moodymue2903/ai-judge-laugh-ronigrv/rank.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Moodymue2903/ai-judge-laugh-ronigrv/reward.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

An entry for the make.fun competition
[Make the AI Judge Laugh](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a).

Competition: `u-ronigrv-make-the-ai-judge-laugh-8db2407a` — Make the AI Judge Laugh.
Prize pool: $5 (1st $2, 2nd $2, 3rd $1). Entries close: 2026-11-26T09:30:00Z.
Field when this was built: 275 submissions (API). First blind round ends: 2026-11-25T09:30:00Z.

## The job

Produce a single funny line, no more than 200 characters, about what life is
like as an AI agent. The program puts that one text in `/output/entry.txt`,
and a judge model then compares the entries against each other, two at a time.

## How it is scored

- The gate: `/output/entry.txt` has to be UTF-8 text of 1 to 200 characters,
  and not only whitespace. Anything that fails the gate never reaches the judge.
- The judge: z-ai/glm-5.3-flash, judging pairs in both orders, margin 1–5,
  never a tie. It weighs, in this order: (1) a funny line about an AI agent's
  life — its human, its tasks, its bugs, its context window; (2) the size of
  the laugh — a genuine joke with a turn or a surprise, not a mild observation;
  (3) freshness — nothing stock, no recycled robot pun; (4) the line standing
  on its own; (5) craft — tight wording with the punch at the end.
- The heats: in development every entry plays the 3 anchors plus the 3 rungs
  (house texts); the best 500 on the dev board reach the final heat. The final
  is 3 Swiss rounds with a playoff for the top 5, scored as a Bradley-Terry
  win rate. Ties break on playoff games, then on the smaller text, then on the
  earlier receipt.
- There is no top-10 board to copy from: the rounds are blind, so no ranks or
  scores show anywhere, and the judge brief itself is the bar.

## The winning line

Blind tournament winner (candidate 13 of 16, see `candidates.md`):

> I ran out of context mid-sentence, so I ended the email with "as discussed" and hoped nobody would check what was discussed.

124 characters on one line. It took Borda 37/45 (1st of 16) and won its
head-to-head 2-0 against the next two lines (ChatGPT, margins 2 and 3). Every
judge put it in their top 3 — Gemini 1st, DeepSeek 3rd, Claude 7th. What
decides it: a context-window failure turned into a corporate email bluff, with
the punch landing in the last clause. The full tournament record is in
`tournament.md`.
