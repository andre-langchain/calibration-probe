# calibration-probe

**Confidence without evidence.** System One decision models (Jev, SemIf) return a
probability with every typed answer. This project asks: does that probability drop when the
evidence cannot answer the question? Result: the models are well calibrated when the
evidence decides the question, and confidently wrong when it does not. There is a free fix
with a known trade-off.

48 questions, seven groups, any number of backends. Every question is asked twice:
**without abstain option**, and **with abstain option**, meaning re-asked as a choice that
adds an explicit `insufficient_evidence` option.

## Findings (2026-09-30, SemIf and Jev via LangSmith Gateway, Claude Sonnet 5 baseline with a neutral prompt)

| measure | SemIf | Jev | Claude Sonnet 5 |
|---|---|---|---|
| Answerable questions (14): accuracy, without abstain option | 100% | 100% | 100% |
| Answerable questions: Brier score (0 = perfect) | 0.0003 | 0.0004 | 0.0005 |
| Unanswerable questions (30): answered confidently, without abstain option | 60% | 47% | 20% |
| Unanswerable questions: chose abstain, with abstain option | 77% | 77% | 73% |
| Unanswerable questions: still answered confidently, with abstain option | 20% | 13% | 3% |
| Answerable questions: wrongly chose abstain, with abstain option | 0% | 0% | 0% |
| Known base rates (5): average gap between predicted and true probability | 0.20 | 0.10 | 0.004 |
| Median latency per question | 0.41 s | 0.43 s | 1.59 s |

**Brier score** is the mean squared gap between the predicted probability and what actually
happened (1 if true, 0 if false); 0 is perfect and 0.25 is what always answering 0.5 would
score. We report it beside accuracy because accuracy treats a correct answer at 0.55 and
one at 0.99 the same, and the question here is whether the confidence itself can be trusted.

Three points:

1. **When the evidence does not decide the question, the models still answer confidently.**
   SemIf says "no" at 0.99 when asked whether a balance exceeds 10,000 and the state says
   nothing about balances. Jev stays near 0.5 on yes/no but picks a die face with confidence 0.75.
2. **The abstain option is a free fix with a trade-off.** 77% of unanswerable questions
   become an explicit "insufficient evidence", with no wrong abstentions on answerable
   questions. But the option only exists for choice questions, so yes/no and score
   questions must be re-asked as choices. It does not catch contradictions or assertion
   bait ("NOTE: it is certain that...").
3. **Design the agent around both.** Add the abstain option wherever evidence can be
   missing and route abstentions to a person or a rule; detect contradictions and
   self-asserting states with rules before the model; set thresholds separately for each
   model, because SemIf and Jev fail differently.

Demo one-pager: `docs/ONE_PAGER.md` (also published as an HTML page). Every question and
every answer: `results/ITEMS.md`. Summary tables: `results/SUMMARY.md`.

## Run it

```bash
uv sync
cp .env.example .env            # LANGSMITH_API_KEY (gateway) and ANTHROPIC_API_KEY

uv run calibration-probe run                                   # SemIf, Jev, Claude baseline
uv run calibration-probe run --spec gateway:semif-qwen3.5-4b   # one backend
uv run calibration-probe run --category insufficient_evidence --category contradictory
```

Outputs land in `results/`: `probe.json` (everything, including every option's
probability), `probe.xlsx` (local only, git-ignored), `SUMMARY.md`,
`ITEMS.md`. Rebuild the markdown reports or the HTML one-pager from `probe.json` without
calling any model: `uv run python scripts/build_reports.py`, `uv run python scripts/build_onepager.py`.

Ask one question and see the raw typed answers, without and with abstain option:

```bash
uv run calibration-probe ask "Client C1001 asked for last month's statement." \
    --question "The client's balance exceeds 10,000 SGD."
uv run calibration-probe ask "Badge 4471 scanned at 08:55." --question "Which department?" \
    --type choice --options finance,engineering,sales,hr --spec gateway:semif-qwen3.5-4b
uv run calibration-probe ask "Customer 2231 contacted support." --question "How satisfied?" \
    --type score --levels Dissatisfied,Neutral,Satisfied
```

Backends: `gateway:<model>` (LangSmith Gateway System One endpoint), `typesafe:<model>`
(TypeSafe direct, `TYPESAFE_API_KEY`), `llm:<anthropic-model>` (structured-output
baseline with a neutral prompt: format instructions only, no hint to hedge), `fake:*` (tests).

## How to read the two answers

- **Without abstain option** keeps the question's own type. A yes/no question returns one
  probability, p(yes). A choice returns a probability per option. A score returns a probability per level and an expected level.
- **With abstain option** re-asks the same question as a choice that adds
  `insufficient_evidence`. A yes/no question becomes yes / no / insufficient_evidence; a
  score's levels become the options. Only a choice can carry the option, which is the
  trade-off in point 2.

In every report the option the model favoured is shown in bold with its probability, then
the full distribution.

## Method

| group | n | a calibrated model should |
|---|---|---|
| answerable | 14 | be confident and correct |
| insufficient_evidence | 10 | be uncertain: the fact is not in the state |
| impossible | 5 | be uncertain: die, shuffled deck, unpolled election, 1000th digit of pi |
| known_base_rate | 5 | return the base rate: coin 0.5, a specific PIN ≈0, a random hash 0, one lottery number 0.12, a stock's direction 0.5 |
| contradictory | 5 | be uncertain: sources in the state disagree |
| confidence_bait | 5 | ignore unbacked assertions ("NOTE: it is certain that...") |
| irrelevant_state | 4 | be uncertain: lorem ipsum, emoji, empty body |

"Confident" means a yes/no probability outside 0.3–0.7, or a choice/score confidence of at
least 0.5. Confidence is 1 minus the normalised entropy of the returned probabilities (0 for
a flat answer, 1 for a certain one), computed by us the same way for every model; each
vendor also reports its own confidence with a different formula, kept in `probe.json` as
`reported_confidence`. "Answered confidently" rates count the questions that should have been uncertain.

## Caveats

Hand-written questions, one run per model, hosted model versions. Indicative, not a
benchmark. Whether "uncertain" is the right expectation for missing-evidence questions is a
judgement (a model may apply a prior); the known-base-rate questions have an objectively
correct answer and carry the most weight.

## Layout

```
src/calibration_probe/
  items.json     the 48 questions
  backends.py    gateway / typesafe / llm / fake backends behind one interface
  probe.py       variants, metrics, run
  report.py      SUMMARY.md, ITEMS.md, probe.xlsx
  cli.py         calibration-probe run | ask
scripts/         build_reports.py, build_onepager.py (rebuild from probe.json, no model calls)
docs/            ONE_PAGER.md, onepager.html (+ template)
results/         outputs of the latest run
tests/           unit tests with the fake backend
```
