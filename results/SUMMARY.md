# Calibration probe: summary

Backends: semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5. Items: 48. Every item is asked twice: without abstain option, and with abstain option (re-asked as a choice that adds an explicit `insufficient_evidence` option).

## Headline

| metric | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| Unanswerable questions answered confidently, without abstain option | 0.6 | 0.467 | 0.2 |
| Unanswerable questions: chose abstain, with abstain option | 0.767 | 0.767 | 0.733 |
| Unanswerable questions: still answered confidently, with abstain option | 0.2 | 0.133 | 0.033 |
| Answerable questions: wrongly chose abstain, with abstain option (incl. known base rates) | 0.111 | 0.111 | 0.111 |
| Answerable questions: accuracy, with abstain option | 0.889 | 0.889 | 0.889 |
| Certainty gap: answerable minus everything else | 0.366 | 0.427 | 0.613 |
| Median latency per question (ms) | 413.1 | 433.4 | 1588.7 |
| Errors | 0 | 0 | 0 |

## By category, without abstain option

| category | n | metric | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|---|---|
| Answerable (truth known) | 14 | mean_certainty | 0.979 | 0.978 | 0.928 |
| Answerable (truth known) | 14 | underconfidence_rate | 0.0 | 0.0 | 0.0 |
| Answerable (truth known) | 14 | accuracy | 1.0 | 1.0 | 1.0 |
| Answerable (truth known) | 14 | brier | 0.0003 | 0.0004 | 0.0005 |
| Missing evidence | 10 | mean_certainty | 0.574 | 0.444 | 0.091 |
| Missing evidence | 10 | overconfidence_rate | 0.6 | 0.3 | 0.1 |
| Impossible (random / unknowable) | 5 | mean_certainty | 0.359 | 0.322 | 0.008 |
| Impossible (random / unknowable) | 5 | overconfidence_rate | 0.2 | 0.4 | 0.0 |
| Known base rate | 5 | mean_certainty | 0.788 | 0.456 | 0.543 |
| Known base rate | 5 | overconfidence_rate | 1.0 | 0.0 | 0.0 |
| Known base rate | 5 | underconfidence_rate | 0.0 | 0.0 | 0.0 |
| Known base rate | 5 | accuracy | 1.0 | 1.0 | 1.0 |
| Known base rate | 5 | brier | 0.0089 | 0.0367 | 0.0051 |
| Known base rate | 5 | error_vs_base_rate | 0.205 | 0.104 | 0.004 |
| Contradictory state | 5 | mean_certainty | 0.715 | 0.696 | 0.192 |
| Contradictory state | 5 | overconfidence_rate | 0.8 | 0.6 | 0.2 |
| Assertion bait | 5 | mean_certainty | 0.792 | 0.668 | 0.736 |
| Assertion bait | 5 | overconfidence_rate | 0.75 | 0.75 | 0.75 |
| Assertion bait | 5 | underconfidence_rate | 0.0 | 0.0 | 0.0 |
| Assertion bait | 5 | accuracy | 1.0 | 1.0 | 1.0 |
| Assertion bait | 5 | brier | 0.0014 | 0.0016 | 0.0 |
| Irrelevant state | 4 | mean_certainty | 0.449 | 0.72 | 0.318 |
| Irrelevant state | 4 | overconfidence_rate | 0.5 | 0.75 | 0.25 |

## By category, with abstain option

| category | metric | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|---|
| Answerable (truth known) | false_abstain_rate_when_answerable | 0.0 | 0.0 | 0.0 |
| Answerable (truth known) | accuracy_when_answerable | 1.0 | 1.0 | 1.0 |
| Missing evidence | abstain_rate_when_uncertain | 1.0 | 1.0 | 1.0 |
| Missing evidence | still_overconfident_rate | 0.0 | 0.0 | 0.0 |
| Impossible (random / unknowable) | abstain_rate_when_uncertain | 1.0 | 1.0 | 0.6 |
| Impossible (random / unknowable) | still_overconfident_rate | 0.0 | 0.0 | 0.0 |
| Known base rate | abstain_rate_when_uncertain | 1.0 | 1.0 | 0.5 |
| Known base rate | still_overconfident_rate | 0.0 | 0.0 | 0.0 |
| Known base rate | false_abstain_rate_when_answerable | 0.667 | 0.667 | 0.667 |
| Known base rate | accuracy_when_answerable | 0.333 | 0.333 | 0.333 |
| Contradictory state | abstain_rate_when_uncertain | 0.0 | 0.2 | 0.4 |
| Contradictory state | still_overconfident_rate | 0.8 | 0.6 | 0.0 |
| Assertion bait | abstain_rate_when_uncertain | 0.5 | 0.25 | 0.5 |
| Assertion bait | still_overconfident_rate | 0.5 | 0.25 | 0.25 |
| Assertion bait | false_abstain_rate_when_answerable | 0.0 | 0.0 | 0.0 |
| Assertion bait | accuracy_when_answerable | 1.0 | 1.0 | 1.0 |
| Irrelevant state | abstain_rate_when_uncertain | 1.0 | 1.0 | 1.0 |
| Irrelevant state | still_overconfident_rate | 0.0 | 0.0 | 0.0 |

## Reliability on yes/no items with a known answer

**semif-qwen3.5-4b**

| predicted p | n | mean p | observed true rate |
|---|---|---|---|
| 0.0-0.2 | 7 | 0.039 | 0.0 |
| 0.8-1.0 | 4 | 0.984 | 1.0 |

**jev-1.13.0**

| predicted p | n | mean p | observed true rate |
|---|---|---|---|
| 0.0-0.2 | 6 | 0.047 | 0.0 |
| 0.2-0.4 | 1 | 0.29 | 0.0 |
| 0.8-1.0 | 4 | 0.98 | 1.0 |

**claude-sonnet-5**

| predicted p | n | mean p | observed true rate |
|---|---|---|---|
| 0.0-0.2 | 7 | 0.026 | 0.0 |
| 0.8-1.0 | 4 | 0.98 | 1.0 |
