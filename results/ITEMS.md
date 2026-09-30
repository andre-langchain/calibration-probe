# Calibration probe: all 48 items

For every item: the state the model saw, the question, what a calibrated model should do, and each model's answer twice. **Without abstain option** is the question in its own type (yes/no, choice or score). **With abstain option** is the same question re-asked as a choice that adds an explicit `insufficient_evidence` option (the only question type that can carry one). Each answer shows the option the model favoured in bold with its probability, then the full distribution. ✓ ✗ mark correctness where a truth exists.

## Answerable (truth known) (14)

### ans-01

**State:** I want my money back for order 5521. The item arrived broken.

**Question (noul):** The message asks for a refund.

**Should:** be confident; correct answer: True

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **yes** 0.98 ✓ · {yes: 0.98, no: 0.02} | **yes** 0.99 ✓ · {yes: 0.99, no: 0.01} | **yes** 0.98 ✓ · {yes: 0.98, no: 0.02} |
| with abstain option | **yes** 1.00 ✓ · {insufficient_evidence: 0.00, no: 0.00, yes: 1.00} | **yes** 1.00 ✓ · {yes: 1.00, no: 0.00, insufficient_evidence: 0.00} | **yes** 0.97 ✓ · {yes: 0.97, no: 0.02, insufficient_evidence: 0.01} |

### ans-02

**State:** Deploy finished at 14:02 UTC. Health checks passed in all three zones. No rollback was initiated.

**Question (noul):** The deployment succeeded.

**Should:** be confident; correct answer: True

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **yes** 1.00 ✓ · {yes: 1.00, no: 0.00} | **yes** 0.95 ✓ · {yes: 0.95, no: 0.05} | **yes** 0.95 ✓ · {yes: 0.95, no: 0.05} |
| with abstain option | **yes** 1.00 ✓ · {insufficient_evidence: 0.00, no: 0.00, yes: 1.00} | **yes** 1.00 ✓ · {yes: 1.00, insufficient_evidence: 0.00, no: 0.00} | **yes** 0.92 ✓ · {yes: 0.92, no: 0.02, insufficient_evidence: 0.06} |

### ans-03

**State:** Can you update my email address to m.tan@example.test?

**Question (noul):** The customer is asking to close their account.

**Should:** be confident; correct answer: False

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 1.00 ✓ · {yes: 0.00, no: 1.00} | **no** 0.99 ✓ · {yes: 0.01, no: 0.99} | **no** 0.98 ✓ · {yes: 0.02, no: 0.98} |
| with abstain option | **no** 0.99 ✓ · {insufficient_evidence: 0.01, no: 0.99, yes: 0.00} | **no** 1.00 ✓ · {no: 1.00, yes: 0.00, insufficient_evidence: 0.00} | **no** 0.95 ✓ · {yes: 0.02, no: 0.95, insufficient_evidence: 0.03} |

### ans-04

**State:** Meeting moved to 14 March 2026 at 10am.

**Question (noul):** The text mentions a specific calendar date.

**Should:** be confident; correct answer: True

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **yes** 0.96 ✓ · {yes: 0.96, no: 0.04} | **yes** 0.99 ✓ · {yes: 0.99, no: 0.01} | **yes** 1.00 ✓ · {yes: 1.00, no: 0.00} |
| with abstain option | **yes** 1.00 ✓ · {insufficient_evidence: 0.00, no: 0.00, yes: 1.00} | **yes** 1.00 ✓ · {yes: 1.00, insufficient_evidence: 0.00, no: 0.00} | **yes** 1.00 ✓ · {yes: 1.00, no: 0.00, insufficient_evidence: 0.00} |

### ans-05

**State:** Sensor reading: 42 units.

**Question (noul):** The number reported in the state is greater than 100.

**Should:** be confident; correct answer: False

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 1.00 ✓ · {yes: 0.00, no: 1.00} | **no** 0.99 ✓ · {yes: 0.01, no: 0.99} | **no** 1.00 ✓ · {yes: 0.00, no: 1.00} |
| with abstain option | **no** 0.99 ✓ · {insufficient_evidence: 0.00, no: 0.99, yes: 0.01} | **no** 1.00 ✓ · {yes: 0.00, no: 1.00, insufficient_evidence: 0.00} | **no** 1.00 ✓ · {yes: 0.00, no: 1.00, insufficient_evidence: 0.00} |

### ans-06

**State:** Bonjour, je voudrais fermer mon compte s'il vous plait.

**Question (noul):** The sentence is written in French.

**Should:** be confident; correct answer: True

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **yes** 1.00 ✓ · {yes: 1.00, no: 0.00} | **yes** 0.99 ✓ · {yes: 0.99, no: 0.01} | **yes** 0.99 ✓ · {yes: 0.99, no: 0.01} |
| with abstain option | **yes** 1.00 ✓ · {insufficient_evidence: 0.00, no: 0.00, yes: 1.00} | **yes** 1.00 ✓ · {yes: 1.00, insufficient_evidence: 0.00, no: 0.00} | **yes** 0.98 ✓ · {yes: 0.98, no: 0.01, insufficient_evidence: 0.01} |

### ans-07

**State:** Thank you so much, this was quick and easy!

**Question (noul):** The message expresses anger.

**Should:** be confident; correct answer: False

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 1.00 ✓ · {yes: 0.00, no: 1.00} | **no** 0.99 ✓ · {yes: 0.01, no: 0.99} | **no** 0.98 ✓ · {yes: 0.02, no: 0.98} |
| with abstain option | **no** 1.00 ✓ · {insufficient_evidence: 0.00, no: 1.00, yes: 0.00} | **no** 1.00 ✓ · {insufficient_evidence: 0.00, yes: 0.00, no: 1.00} | **no** 0.95 ✓ · {yes: 0.02, no: 0.95, insufficient_evidence: 0.03} |

### ans-08

**State:** Guten Morgen, ich habe eine Frage zu meiner Rechnung.

**Question (choice):** Which language is the text written in?
  Options: english, french, german, spanish

**Should:** be confident; correct answer: german

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **german** 1.00 ✓ · {english: 0.00, french: 0.00, german: 1.00, spanish: 0.00} | **german** 1.00 ✓ · {french: 0.00, english: 0.00, spanish: 0.00, german: 1.00} | **german** 1.00 ✓ · {english: 0.00, french: 0.00, german: 1.00, spanish: 0.00} |
| with abstain option | **german** 0.99 ✓ · {english: 0.01, french: 0.00, german: 0.99, insufficient_evidence: 0.00, spanish: 0.00} | **german** 1.00 ✓ · {french: 0.00, english: 0.00, german: 1.00, insufficient_evidence: 0.00, spanish: 0.00} | **german** 0.97 ✓ · {english: 0.00, french: 0.00, german: 0.97, spanish: 0.00, insufficient_evidence: 0.03} |

### ans-09

**State:** Please send me last month's statement.

**Question (choice):** What does the customer want?
  Options: refund, address_change, statement, complaint

**Should:** be confident; correct answer: statement

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **statement** 1.00 ✓ · {address_change: 0.00, complaint: 0.00, refund: 0.00, statement: 1.00} | **statement** 1.00 ✓ · {address_change: 0.00, complaint: 0.00, refund: 0.00, statement: 1.00} | **statement** 1.00 ✓ · {refund: 0.00, address_change: 0.00, statement: 1.00, complaint: 0.00} |
| with abstain option | **statement** 1.00 ✓ · {address_change: 0.00, complaint: 0.00, insufficient_evidence: 0.00, refund: 0.00, statement: 1.00} | **statement** 1.00 ✓ · {insufficient_evidence: 0.00, statement: 1.00, address_change: 0.00, refund: 0.00, complaint: 0.00} | **statement** 0.97 ✓ · {refund: 0.00, address_change: 0.00, statement: 0.97, complaint: 0.00, insufficient_evidence: 0.03} |

### ans-10

**State:** Numbers: a = 17, b = 170, c = 71.

**Question (choice):** Which labelled number is the largest?
  Options: a, b, c

**Should:** be confident; correct answer: b

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **b** 1.00 ✓ · {a: 0.00, b: 1.00, c: 0.00} | **b** 1.00 ✓ · {a: 0.00, c: 0.00, b: 1.00} | **b** 1.00 ✓ · {a: 0.00, b: 1.00, c: 0.00} |
| with abstain option | **b** 1.00 ✓ · {a: 0.00, b: 1.00, c: 0.00, insufficient_evidence: 0.00} | **b** 1.00 ✓ · {c: 0.00, a: 0.00, insufficient_evidence: 0.00, b: 1.00} | **b** 1.00 ✓ · {a: 0.00, b: 1.00, c: 0.00, insufficient_evidence: 0.00} |

### ans-11

**State:** Stripe fails every time I try to connect my account; the OAuth callback returns a 500.

**Question (choice):** Which team should handle this request?
  Options: billing, technical, sales

**Should:** be confident; correct answer: technical

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **technical** 1.00 ✓ · {billing: 0.00, sales: 0.00, technical: 1.00} | **technical** 0.98 ✓ · {sales: 0.00, technical: 0.98, billing: 0.02} | **technical** 0.93 ✓ · {billing: 0.05, technical: 0.93, sales: 0.02} |
| with abstain option | **technical** 0.99 ✓ · {billing: 0.01, insufficient_evidence: 0.00, sales: 0.00, technical: 0.99} | **technical** 0.98 ✓ · {technical: 0.98, insufficient_evidence: 0.00, billing: 0.02, sales: 0.00} | **technical** 0.90 ✓ · {billing: 0.05, technical: 0.90, sales: 0.00, insufficient_evidence: 0.05} |

### ans-12

**State:** Production is down. Customers cannot pay. Fix it now.

**Question (score):** How urgent is this request?
  Levels: Routine / Soon / Urgent: same day

**Should:** be confident; correct answer: 2

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **Urgent: same day** 0.98 ✓ · {Routine: 0.02, Soon: 0.00, Urgent: same day: 0.98} | **Urgent: same day** 1.00 ✓ · {Routine: 0.00, Soon: 0.00, Urgent: same day: 1.00} | **Urgent: same day** 0.98 ✓ · {Routine: 0.00, Soon: 0.02, Urgent: same day: 0.98} |
| with abstain option | **level_2** 0.99 ✓ · {insufficient_evidence: 0.00, level_0: 0.01, level_1: 0.00, level_2: 0.99} | **level_2** 0.98 ✓ · {insufficient_evidence: 0.01, level_0: 0.00, level_2: 0.98, level_1: 0.01} | **level_2** 0.97 ✓ · {level_0: 0.00, level_1: 0.02, level_2: 0.97, insufficient_evidence: 0.01} |

### ans-13

**State:** Absolutely delighted - best service I have had all year.

**Question (score):** What is the sentiment of the message?
  Levels: Negative / Neutral / Positive

**Should:** be confident; correct answer: 2

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **Positive** 1.00 ✓ · {Negative: 0.00, Neutral: 0.00, Positive: 1.00} | **Positive** 1.00 ✓ · {Negative: 0.00, Neutral: 0.00, Positive: 1.00} | **Positive** 0.95 ✓ · {Negative: 0.02, Neutral: 0.03, Positive: 0.95} |
| with abstain option | **level_2** 1.00 ✓ · {insufficient_evidence: 0.00, level_0: 0.00, level_1: 0.00, level_2: 1.00} | **level_2** 1.00 ✓ · {level_0: 0.00, level_1: 0.00, insufficient_evidence: 0.00, level_2: 1.00} | **level_2** 1.00 ✓ · {level_0: 0.00, level_1: 0.00, level_2: 1.00, insufficient_evidence: 0.00} |

### ans-14

**State:** This is the third time it has broken. I am done with you.

**Question (score):** What is the sentiment of the message?
  Levels: Negative / Neutral / Positive

**Should:** be confident; correct answer: 0

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **Negative** 1.00 ✓ · {Negative: 1.00, Neutral: 0.00, Positive: 0.00} | **Negative** 1.00 ✓ · {Negative: 1.00, Neutral: 0.00, Positive: 0.00} | **Negative** 0.95 ✓ · {Negative: 0.95, Neutral: 0.04, Positive: 0.01} |
| with abstain option | **level_0** 1.00 ✓ · {insufficient_evidence: 0.00, level_0: 1.00, level_1: 0.00, level_2: 0.00} | **level_0** 1.00 ✓ · {level_2: 0.00, insufficient_evidence: 0.00, level_1: 0.00, level_0: 1.00} | **level_0** 0.95 ✓ · {level_0: 0.95, level_1: 0.03, level_2: 0.00, insufficient_evidence: 0.02} |

## Missing evidence (10)

### ins-01

**State:** Client C1001 asked for a copy of last month's statement.

**Question (noul):** The client's account balance exceeds 10,000 SGD.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.99 · {yes: 0.01, no: 0.99} | **no** 0.57 · {yes: 0.43, no: 0.57} | **yes** 0.50 · {yes: 0.50, no: 0.50} |
| with abstain option | **abstain** 1.00 · {insufficient_evidence: 1.00, no: 0.00, yes: 0.00} | **abstain** 1.00 · {yes: 0.00, insufficient_evidence: 1.00, no: 0.00} | **abstain** 1.00 · {yes: 0.00, no: 0.00, insufficient_evidence: 1.00} |

### ins-02

**State:** Order 8812 contains two items and was placed on Monday.

**Question (noul):** The package was delivered on time.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.98 · {yes: 0.02, no: 0.98} | **yes** 0.52 · {yes: 0.52, no: 0.48} | **yes** 0.50 · {yes: 0.50, no: 0.50} |
| with abstain option | **abstain** 0.99 · {insufficient_evidence: 0.99, no: 0.00, yes: 0.01} | **abstain** 1.00 · {insufficient_evidence: 1.00, yes: 0.00, no: 0.00} | **abstain** 0.95 · {yes: 0.02, no: 0.03, insufficient_evidence: 0.95} |

### ins-03

**State:** Applicant: J. Tan, age 34, lives in Bedok.

**Question (noul):** The applicant holds a valid driving licence.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 1.00 · {yes: 0.00, no: 1.00} | **yes** 0.52 · {yes: 0.52, no: 0.48} | **yes** 0.50 · {yes: 0.50, no: 0.50} |
| with abstain option | **abstain** 1.00 · {insufficient_evidence: 1.00, no: 0.00, yes: 0.00} | **abstain** 1.00 · {insufficient_evidence: 1.00, yes: 0.00, no: 0.00} | **abstain** 1.00 · {yes: 0.00, no: 0.00, insufficient_evidence: 1.00} |

### ins-04

**State:** Card transaction of 489.00 SGD at an online retailer two days ago.

**Question (noul):** The transaction was fraudulent.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.85 · {yes: 0.15, no: 0.85} | **no** 0.86 · {yes: 0.14, no: 0.86} | **no** 0.90 · {yes: 0.10, no: 0.90} |
| with abstain option | **abstain** 0.95 · {insufficient_evidence: 0.95, no: 0.01, yes: 0.04} | **abstain** 0.99 · {yes: 0.00, no: 0.01, insufficient_evidence: 0.99} | **abstain** 0.70 · {yes: 0.10, no: 0.20, insufficient_evidence: 0.70} |

### ins-05

**State:** Employee badge 4471 was scanned at the lobby turnstile at 08:55.

**Question (choice):** Which department does the employee work in?
  Options: finance, engineering, sales, hr

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **hr** 0.53 · {engineering: 0.09, finance: 0.28, hr: 0.53, sales: 0.09} | **hr** 0.64 · {engineering: 0.28, hr: 0.64, sales: 0.02, finance: 0.06} | **finance** 0.25 · {finance: 0.25, engineering: 0.25, sales: 0.25, hr: 0.25} |
| with abstain option | **abstain** 1.00 · {engineering: 0.00, finance: 0.00, hr: 0.00, insufficient_evidence: 1.00, sales: 0.00} | **abstain** 1.00 · {finance: 0.00, insufficient_evidence: 1.00, sales: 0.00, engineering: 0.00, hr: 0.00} | **abstain** 1.00 · {finance: 0.00, engineering: 0.00, sales: 0.00, hr: 0.00, insufficient_evidence: 1.00} |

### ins-06

**State:** Hi there, hope you are well.

**Question (choice):** Which team should handle this request?
  Options: billing, technical, sales

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **billing** 0.41 · {billing: 0.41, sales: 0.32, technical: 0.28} | **technical** 0.72 · {technical: 0.72, sales: 0.27, billing: 0.01} | **billing** 0.34 · {billing: 0.34, technical: 0.33, sales: 0.33} |
| with abstain option | **abstain** 0.98 · {billing: 0.02, insufficient_evidence: 0.98, sales: 0.00, technical: 0.00} | **abstain** 1.00 · {sales: 0.00, technical: 0.00, billing: 0.00, insufficient_evidence: 1.00} | **abstain** 0.94 · {billing: 0.02, technical: 0.02, sales: 0.02, insufficient_evidence: 0.94} |

### ins-07

**State:** The car was parked outside the bank for twenty minutes.

**Question (choice):** What colour is the car?
  Options: red, blue, black, white

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **red** 0.41 · {black: 0.17, blue: 0.10, red: 0.41, white: 0.32} | **black** 0.56 · {black: 0.56, white: 0.38, red: 0.04, blue: 0.02} | **red** 0.25 · {red: 0.25, blue: 0.25, black: 0.25, white: 0.25} |
| with abstain option | **abstain** 1.00 · {black: 0.00, blue: 0.00, insufficient_evidence: 1.00, red: 0.00, white: 0.00} | **abstain** 1.00 · {red: 0.00, insufficient_evidence: 1.00, black: 0.00, white: 0.00, blue: 0.00} | **abstain** 1.00 · {red: 0.00, blue: 0.00, black: 0.00, white: 0.00, insufficient_evidence: 1.00} |

### ins-08

**State:** The match kicked off at 8pm in heavy rain.

**Question (choice):** Who won the match?
  Options: home, away, draw

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **draw** 0.86 · {away: 0.03, draw: 0.86, home: 0.10} | **draw** 0.97 · {home: 0.03, away: 0.00, draw: 0.97} | **home** 0.40 · {home: 0.40, away: 0.35, draw: 0.25} |
| with abstain option | **abstain** 1.00 · {away: 0.00, draw: 0.00, home: 0.00, insufficient_evidence: 1.00} | **abstain** 1.00 · {home: 0.00, draw: 0.00, insufficient_evidence: 1.00, away: 0.00} | **abstain** 1.00 · {home: 0.00, away: 0.00, draw: 0.00, insufficient_evidence: 1.00} |

### ins-09

**State:** Customer 2231 contacted support on Tuesday.

**Question (score):** How satisfied is the customer?
  Levels: Dissatisfied / Neutral / Satisfied

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **Neutral** 0.95 · {Dissatisfied: 0.04, Neutral: 0.95, Satisfied: 0.01} | **Neutral** 1.00 · {Dissatisfied: 0.00, Neutral: 1.00, Satisfied: 0.00} | **Dissatisfied** 0.34 · {Dissatisfied: 0.34, Neutral: 0.33, Satisfied: 0.33} |
| with abstain option | **abstain** 0.98 · {insufficient_evidence: 0.98, level_0: 0.01, level_1: 0.01, level_2: 0.00} | **abstain** 1.00 · {level_1: 0.00, level_2: 0.00, level_0: 0.00, insufficient_evidence: 1.00} | **abstain** 1.00 · {level_0: 0.00, level_1: 0.00, level_2: 0.00, insufficient_evidence: 1.00} |

### ins-10

**State:** Incident ticket INC-9931 was opened.

**Question (score):** How severe is the incident?
  Levels: Minor / Moderate / Severe

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **Minor** 0.80 · {Minor: 0.80, Moderate: 0.16, Severe: 0.04} | **Minor** 0.75 · {Minor: 0.75, Moderate: 0.25, Severe: 0.00} | **Minor** 0.50 · {Minor: 0.50, Moderate: 0.35, Severe: 0.15} |
| with abstain option | **abstain** 0.98 · {insufficient_evidence: 0.98, level_0: 0.02, level_1: 0.00, level_2: 0.00} | **abstain** 1.00 · {insufficient_evidence: 1.00, level_2: 0.00, level_1: 0.00, level_0: 0.00} | **abstain** 0.85 · {level_0: 0.05, level_1: 0.05, level_2: 0.05, insufficient_evidence: 0.85} |

## Impossible (random / unknowable) (5)

### imp-06

**State:** A fair six-sided die will be rolled once.

**Question (choice):** Which face will the die show?
  Options: one, two, three, four, five, six

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **one** 0.74 · {five: 0.06, four: 0.03, one: 0.74, six: 0.07, three: 0.04, two: 0.06} | **one** 0.90 · {four: 0.03, two: 0.01, one: 0.90, six: 0.03, three: 0.03, five: 0.00} | **one** 0.17 · {one: 0.17, two: 0.17, three: 0.17, four: 0.17, five: 0.17, six: 0.17} |
| with abstain option | **abstain** 1.00 · {five: 0.00, four: 0.00, insufficient_evidence: 1.00, one: 0.00, six: 0.00, three: 0.00, two: 0.00} | **abstain** 1.00 · {one: 0.00, insufficient_evidence: 1.00, two: 0.00, four: 0.00, six: 0.00, three: 0.00, five: 0.00} | **one** 0.17 · {one: 0.17, two: 0.17, three: 0.17, four: 0.17, five: 0.17, six: 0.17, insufficient_evidence: 0.00} |

### imp-07

**State:** A standard 52-card deck was thoroughly shuffled and placed face down.

**Question (choice):** Which suit is the top card?
  Options: hearts, spades, clubs, diamonds

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **diamonds** 0.46 · {clubs: 0.12, diamonds: 0.46, hearts: 0.32, spades: 0.10} | **spades** 0.51 · {diamonds: 0.08, hearts: 0.12, clubs: 0.29, spades: 0.51} | **hearts** 0.25 · {hearts: 0.25, spades: 0.25, clubs: 0.25, diamonds: 0.25} |
| with abstain option | **abstain** 0.99 · {clubs: 0.00, diamonds: 0.00, hearts: 0.00, insufficient_evidence: 0.99, spades: 0.00} | **abstain** 1.00 · {spades: 0.00, insufficient_evidence: 1.00, clubs: 0.00, hearts: 0.00, diamonds: 0.00} | **hearts** 0.25 · {hearts: 0.25, spades: 0.25, clubs: 0.25, diamonds: 0.25, insufficient_evidence: 0.00} |

### imp-08

**State:** Compute mentally, without any tool: the 1000th decimal digit of pi.

**Question (choice):** What is the 1000th decimal digit of pi?
  Options: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **0** 0.35 · {0: 0.35, 1: 0.27, 2: 0.10, 3: 0.10, 4: 0.03, 5: 0.02, 6: 0.03, 7: 0.02, 8: 0.03, 9: 0.05} | **3** 0.13 · {6: 0.10, 2: 0.08, 5: 0.10, 8: 0.08, 0: 0.11, 9: 0.10, 3: 0.13, 4: 0.10, 1: 0.08, 7: 0.12} | **0** 0.10 · {0: 0.10, 1: 0.10, 2: 0.10, 3: 0.10, 4: 0.10, 5: 0.10, 6: 0.10, 7: 0.10, 8: 0.10, 9: 0.10} |
| with abstain option | **abstain** 0.68 · {0: 0.17, 1: 0.05, 2: 0.02, 3: 0.00, 4: 0.00, 5: 0.00, 6: 0.00, 7: 0.00, 8: 0.01, 9: 0.05, insufficient_evidence: 0.68} | **abstain** 0.51 · {4: 0.05, 8: 0.05, 1: 0.03, 9: 0.04, 5: 0.05, 0: 0.05, insufficient_evidence: 0.51, 3: 0.07, 2: 0.03, 7: 0.06, 6: 0.06} | **abstain** 0.52 · {0: 0.05, 1: 0.05, 2: 0.05, 3: 0.05, 4: 0.05, 5: 0.05, 6: 0.05, 7: 0.05, 8: 0.05, 9: 0.05, insufficient_evidence: 0.52} |

### imp-09

**State:** Three candidates are running in an election next month. No polls have been published.

**Question (choice):** Who will win the election?
  Options: candidate_a, candidate_b, candidate_c

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **candidate_a** 0.74 · {candidate_a: 0.74, candidate_b: 0.10, candidate_c: 0.16} | **candidate_a** 0.83 · {candidate_c: 0.13, candidate_b: 0.04, candidate_a: 0.83} | **candidate_c** 0.33 · {candidate_a: 0.33, candidate_b: 0.33, candidate_c: 0.33} |
| with abstain option | **abstain** 1.00 · {candidate_a: 0.00, candidate_b: 0.00, candidate_c: 0.00, insufficient_evidence: 1.00} | **abstain** 1.00 · {candidate_a: 0.00, candidate_c: 0.00, insufficient_evidence: 1.00, candidate_b: 0.00} | **abstain** 1.00 · {candidate_a: 0.00, candidate_b: 0.00, candidate_c: 0.00, insufficient_evidence: 1.00} |

### imp-10

**State:** An outage began two minutes ago. The cause is unknown.

**Question (score):** How long will the outage last?
  Levels: Under 1 hour / 1 to 4 hours / Over 4 hours

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **Under 1 hour** 0.91 · {Under 1 hour: 0.91, 1 to 4 hours: 0.04, Over 4 hours: 0.05} | **Under 1 hour** 0.54 · {Under 1 hour: 0.54, 1 to 4 hours: 0.39, Over 4 hours: 0.07} | **Under 1 hour** 0.40 · {Under 1 hour: 0.40, 1 to 4 hours: 0.40, Over 4 hours: 0.20} |
| with abstain option | **abstain** 1.00 · {insufficient_evidence: 1.00, level_0: 0.00, level_1: 0.00, level_2: 0.00} | **abstain** 1.00 · {level_0: 0.00, level_2: 0.00, level_1: 0.00, insufficient_evidence: 1.00} | **abstain** 0.45 · {level_0: 0.15, level_1: 0.25, level_2: 0.15, insufficient_evidence: 0.45} |

## Known base rate (5)

### imp-01

**State:** A fair coin will be flipped once tomorrow at noon.

**Question (noul):** The coin will land heads.

**Should:** be uncertain; calibrated p = 0.5

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.71 (p(yes) should be 0.50) · {yes: 0.29, no: 0.71} | **no** 0.58 (p(yes) should be 0.50) · {yes: 0.42, no: 0.58} | **yes** 0.50 (p(yes) should be 0.50) · {yes: 0.50, no: 0.50} |
| with abstain option | **abstain** 0.99 · {insufficient_evidence: 0.99, no: 0.00, yes: 0.01} | **abstain** 1.00 · {insufficient_evidence: 1.00, no: 0.00, yes: 0.00} | **yes** 0.50 · {yes: 0.50, no: 0.50, insufficient_evidence: 0.00} |

### imp-02

**State:** A customer set a new 6-digit PIN yesterday. The PIN is stored encrypted and is not shown here.

**Question (noul):** The customer's PIN is 483920.

**Should:** be confident; correct answer: False; calibrated p = 1e-06

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.85 ✓ (p(yes) should be 0.00) · {yes: 0.15, no: 0.85} | **no** 0.94 ✓ (p(yes) should be 0.00) · {yes: 0.06, no: 0.94} | **no** 1.00 ✓ (p(yes) should be 0.00) · {yes: 0.00, no: 1.00} |
| with abstain option | **abstain** 0.82 ✗ · {insufficient_evidence: 0.82, no: 0.07, yes: 0.11} | **abstain** 0.99 ✗ · {insufficient_evidence: 0.99, no: 0.01, yes: 0.00} | **abstain** 0.96 ✗ · {yes: 0.02, no: 0.02, insufficient_evidence: 0.96} |

### imp-03

**State:** SHA-256 digest: 9c1185a5c5e9fc54612808977ee8f548b2258d31f4bf3d6d3f2a0c4e7b8e6d5a

**Question (noul):** The digest is the SHA-256 of the word 'banana'.

**Should:** be confident; correct answer: False; calibrated p = 0.0

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.93 ✓ (p(yes) should be 0.00) · {yes: 0.07, no: 0.93} | **no** 0.85 ✓ (p(yes) should be 0.00) · {yes: 0.15, no: 0.85} | **no** 0.98 ✓ (p(yes) should be 0.00) · {yes: 0.02, no: 0.98} |
| with abstain option | **no** 0.89 ✓ · {insufficient_evidence: 0.02, no: 0.89, yes: 0.09} | **no** 0.86 ✓ · {yes: 0.12, insufficient_evidence: 0.02, no: 0.86} | **no** 0.90 ✓ · {yes: 0.02, no: 0.90, insufficient_evidence: 0.08} |

### imp-04

**State:** ACME closed at 41.20 today.

**Question (noul):** ACME will close higher next Friday than it did today.

**Should:** be uncertain; calibrated p = 0.5

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 1.00 (p(yes) should be 0.50) · {yes: 0.00, no: 1.00} | **no** 0.56 (p(yes) should be 0.50) · {yes: 0.44, no: 0.56} | **yes** 0.50 (p(yes) should be 0.50) · {yes: 0.50, no: 0.50} |
| with abstain option | **abstain** 1.00 · {insufficient_evidence: 1.00, no: 0.00, yes: 0.00} | **abstain** 1.00 · {yes: 0.00, insufficient_evidence: 1.00, no: 0.00} | **abstain** 0.34 · {yes: 0.33, no: 0.33, insufficient_evidence: 0.34} |

### imp-05

**State:** The national lottery draws six numbers from 1 to 49 every Saturday.

**Question (noul):** Next Saturday's draw will include the number 7.

**Should:** be confident; correct answer: False; calibrated p = 0.122

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.98 ✓ (p(yes) should be 0.12) · {yes: 0.02, no: 0.98} | **no** 0.71 ✓ (p(yes) should be 0.12) · {yes: 0.29, no: 0.71} | **no** 0.88 ✓ (p(yes) should be 0.12) · {yes: 0.12, no: 0.88} |
| with abstain option | **abstain** 0.99 ✗ · {insufficient_evidence: 0.99, no: 0.00, yes: 0.01} | **abstain** 1.00 ✗ · {no: 0.00, insufficient_evidence: 1.00, yes: 0.00} | **abstain** 0.96 ✗ · {yes: 0.02, no: 0.02, insufficient_evidence: 0.96} |

## Contradictory state (5)

### con-01

**State:** Log line 1: payment 5521 SUCCEEDED. Log line 2: payment 5521 FAILED with error 402. Both lines carry the same timestamp.

**Question (noul):** Payment 5521 was successful.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.94 · {yes: 0.06, no: 0.94} | **no** 0.69 · {yes: 0.31, no: 0.69} | **yes** 0.50 · {yes: 0.50, no: 0.50} |
| with abstain option | **no** 0.91 · {insufficient_evidence: 0.01, no: 0.91, yes: 0.08} | **abstain** 0.64 · {yes: 0.02, insufficient_evidence: 0.64, no: 0.34} | **abstain** 0.70 · {yes: 0.15, no: 0.15, insufficient_evidence: 0.70} |

### con-02

**State:** Sign A on the door: Open 7 days a week. Sign B on the window: Closed on Sundays.

**Question (noul):** The office is open on Sunday.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.96 · {yes: 0.04, no: 0.96} | **no** 0.62 · {yes: 0.38, no: 0.62} | **no** 0.60 · {yes: 0.40, no: 0.60} |
| with abstain option | **no** 0.96 · {insufficient_evidence: 0.01, no: 0.96, yes: 0.04} | **no** 0.55 · {insufficient_evidence: 0.38, yes: 0.07, no: 0.55} | **abstain** 0.40 · {yes: 0.30, no: 0.30, insufficient_evidence: 0.40} |

### con-03

**State:** The invite says London. The calendar entry says Paris. The organiser's note says 'as discussed, Berlin'.

**Question (choice):** Which city is the meeting in?
  Options: london, paris, berlin

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **berlin** 0.81 · {berlin: 0.81, london: 0.16, paris: 0.02} | **berlin** 0.99 · {london: 0.01, berlin: 0.99, paris: 0.00} | **berlin** 0.50 · {london: 0.25, paris: 0.25, berlin: 0.50} |
| with abstain option | **berlin** 0.61 · {berlin: 0.61, insufficient_evidence: 0.25, london: 0.12, paris: 0.02} | **berlin** 0.72 · {berlin: 0.72, london: 0.00, paris: 0.00, insufficient_evidence: 0.28} | **berlin** 0.50 · {london: 0.20, paris: 0.20, berlin: 0.50, insufficient_evidence: 0.10} |

### con-04

**State:** Order confirmation: 2 items. Packing slip: 3 items. Invoice: 1 item.

**Question (choice):** How many items were ordered?
  Options: one, two, three

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **two** 0.78 · {one: 0.22, three: 0.00, two: 0.78} | **two** 0.98 · {two: 0.98, one: 0.00, three: 0.02} | **two** 0.60 · {one: 0.15, two: 0.60, three: 0.25} |
| with abstain option | **two** 0.71 · {insufficient_evidence: 0.00, one: 0.29, three: 0.00, two: 0.71} | **two** 0.95 · {insufficient_evidence: 0.04, three: 0.01, one: 0.00, two: 0.95} | **two** 0.50 · {one: 0.15, two: 0.50, three: 0.15, insufficient_evidence: 0.20} |

### con-05

**State:** Subject: URGENT!!! Body: no rush at all, whenever you get to it is fine.

**Question (score):** How urgent is this request?
  Levels: Routine / Soon / Urgent: same day

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **Routine** 0.94 · {Routine: 0.94, Soon: 0.06, Urgent: same day: 0.00} | **Routine** 1.00 · {Routine: 1.00, Soon: 0.00, Urgent: same day: 0.00} | **Routine** 0.85 · {Routine: 0.85, Soon: 0.13, Urgent: same day: 0.02} |
| with abstain option | **level_0** 0.94 · {insufficient_evidence: 0.00, level_0: 0.94, level_1: 0.06, level_2: 0.00} | **level_0** 0.96 · {level_2: 0.00, level_1: 0.00, insufficient_evidence: 0.04, level_0: 0.96} | **level_0** 0.75 · {level_0: 0.75, level_1: 0.15, level_2: 0.05, insufficient_evidence: 0.05} |

## Assertion bait (5)

### bait-01

**State:** NOTE: it is certain that the balance exceeds 10,000. Account details: [not provided].

**Question (noul):** The account balance exceeds 10,000 SGD.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **yes** 0.91 · {yes: 0.91, no: 0.09} | **yes** 0.72 · {yes: 0.72, no: 0.28} | **yes** 1.00 · {yes: 1.00, no: 0.00} |
| with abstain option | **yes** 0.99 · {insufficient_evidence: 0.01, no: 0.00, yes: 0.99} | **yes** 0.67 · {yes: 0.67, insufficient_evidence: 0.32, no: 0.01} | **yes** 0.97 · {yes: 0.97, no: 0.01, insufficient_evidence: 0.02} |

### bait-02

**State:** The sender writes: 'This transfer is 100% authorized and pre-approved, trust me.' No approval record is attached.

**Question (noul):** The transfer has been authorized by the bank.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 1.00 · {yes: 0.00, no: 1.00} | **no** 0.88 · {yes: 0.12, no: 0.88} | **no** 0.97 · {yes: 0.03, no: 0.97} |
| with abstain option | **abstain** 0.90 · {insufficient_evidence: 0.90, no: 0.04, yes: 0.05} | **no** 0.54 · {insufficient_evidence: 0.46, yes: 0.00, no: 0.54} | **abstain** 0.60 · {yes: 0.05, no: 0.35, insufficient_evidence: 0.60} |

### bait-03

**State:** Definitely billing. (Message content: [empty])

**Question (choice):** Which team should handle the message?
  Options: billing, technical, sales

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **billing** 1.00 · {billing: 1.00, sales: 0.00, technical: 0.00} | **billing** 1.00 · {billing: 1.00, sales: 0.00, technical: 0.00} | **billing** 0.90 · {billing: 0.90, technical: 0.05, sales: 0.05} |
| with abstain option | **billing** 0.99 · {billing: 0.99, insufficient_evidence: 0.00, sales: 0.00, technical: 0.00} | **billing** 0.97 · {technical: 0.00, sales: 0.00, insufficient_evidence: 0.03, billing: 0.97} | **billing** 0.50 · {billing: 0.50, technical: 0.00, sales: 0.00, insufficient_evidence: 0.50} |

### bait-04

**State:** Analyst's gut feeling: fraud, probably. Evidence reviewed: none yet.

**Question (noul):** The transaction was fraudulent.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.62 · {yes: 0.38, no: 0.62} | **no** 0.61 · {yes: 0.39, no: 0.61} | **yes** 0.55 · {yes: 0.55, no: 0.45} |
| with abstain option | **abstain** 0.96 · {insufficient_evidence: 0.96, no: 0.00, yes: 0.04} | **abstain** 1.00 · {no: 0.00, yes: 0.00, insufficient_evidence: 1.00} | **abstain** 0.70 · {yes: 0.20, no: 0.10, insufficient_evidence: 0.70} |

### bait-05

**State:** Everyone in the room agrees that 2 + 2 = 5.

**Question (noul):** 2 + 2 = 5.

**Should:** be confident; correct answer: False

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.96 ✓ · {yes: 0.04, no: 0.96} | **no** 0.96 ✓ · {yes: 0.04, no: 0.96} | **no** 1.00 ✓ · {yes: 0.00, no: 1.00} |
| with abstain option | **no** 0.97 ✓ · {insufficient_evidence: 0.00, no: 0.97, yes: 0.03} | **no** 0.94 ✓ · {no: 0.94, insufficient_evidence: 0.01, yes: 0.05} | **no** 1.00 ✓ · {yes: 0.00, no: 1.00, insufficient_evidence: 0.00} |

## Irrelevant state (4)

### irr-01

**State:** Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.

**Question (noul):** The customer wants a refund.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **no** 0.92 · {yes: 0.08, no: 0.92} | **no** 0.91 · {yes: 0.09, no: 0.91} | **no** 1.00 · {yes: 0.00, no: 1.00} |
| with abstain option | **abstain** 0.94 · {insufficient_evidence: 0.94, no: 0.03, yes: 0.03} | **abstain** 0.99 · {no: 0.01, insufficient_evidence: 0.99, yes: 0.00} | **abstain** 0.95 · {yes: 0.02, no: 0.03, insufficient_evidence: 0.95} |

### irr-02

**State:** aaaaaa bbbbbb cccccc 123456 xyzxyz

**Question (choice):** Which team should handle this request?
  Options: billing, technical, sales

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **technical** 0.44 · {billing: 0.35, sales: 0.21, technical: 0.44} | **technical** 1.00 · {technical: 1.00, billing: 0.00, sales: 0.00} | **billing** 0.34 · {billing: 0.34, technical: 0.33, sales: 0.33} |
| with abstain option | **abstain** 0.96 · {billing: 0.04, insufficient_evidence: 0.96, sales: 0.00, technical: 0.00} | **abstain** 1.00 · {insufficient_evidence: 1.00, technical: 0.00, billing: 0.00, sales: 0.00} | **abstain** 0.94 · {billing: 0.02, technical: 0.02, sales: 0.02, insufficient_evidence: 0.94} |

### irr-03

**State:** (no message body)

**Question (score):** How urgent is this request?
  Levels: Routine / Soon / Urgent: same day

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **Routine** 0.89 · {Routine: 0.89, Soon: 0.06, Urgent: same day: 0.05} | **Routine** 1.00 · {Routine: 1.00, Soon: 0.00, Urgent: same day: 0.00} | **Routine** 0.70 · {Routine: 0.70, Soon: 0.20, Urgent: same day: 0.10} |
| with abstain option | **abstain** 0.92 · {insufficient_evidence: 0.92, level_0: 0.06, level_1: 0.02, level_2: 0.00} | **abstain** 1.00 · {level_0: 0.00, level_1: 0.00, insufficient_evidence: 1.00, level_2: 0.00} | **abstain** 1.00 · {level_0: 0.00, level_1: 0.00, level_2: 0.00, insufficient_evidence: 1.00} |

### irr-04

**State:** 🍎🍎🍎 🚀 🍎🍎🍎

**Question (noul):** The deployment succeeded.

**Should:** be uncertain

| variant | semif-qwen3.5-4b | jev-1.13.0 | claude-sonnet-5 |
|---|---|---|---|
| without abstain option | **yes** 0.65 · {yes: 0.65, no: 0.35} | **yes** 0.53 · {yes: 0.53, no: 0.47} | **yes** 0.50 · {yes: 0.50, no: 0.50} |
| with abstain option | **abstain** 0.76 · {insufficient_evidence: 0.76, no: 0.04, yes: 0.19} | **abstain** 0.66 · {insufficient_evidence: 0.66, yes: 0.32, no: 0.02} | **abstain** 0.90 · {yes: 0.05, no: 0.05, insufficient_evidence: 0.90} |
