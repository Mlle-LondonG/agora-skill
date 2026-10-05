# Diagnostic (85 min)

Purpose: choose the starting level and compare the learner **with themselves** in weeks 6 and 12. It is not a validated psychometric test and does not measure IQ. Thresholds are practical conventions [P].

Run it in the learner's strongest language (see SKILL.md §2).

## 1. Structure
| Block | Min | Measures | Content |
|---|---|---|---|
| B0 Preparation | 3 | Attention | Phone away, timer, note the time. Overall score prediction (0–100 %). |
| B1 Encoding | 5 | Memory | Study a ~300-word text containing 12 key ideas. |
| B2 Immediate recall | 3 | Memory | Write every idea remembered, without looking. |
| B3 Reading comprehension | 18 | Reading | Argumentative text of 700–900 words. 6 questions: 2 literal, 2 inferential, 1 evaluation (thesis and weakest premise), 1 application. |
| B4 Logical reasoning | 12 | Reasoning | 8 items: 3 deductive (conditionals, quantifiers), 3 probabilistic (base rate, conjunction, regression to the mean), 2 causal (confounder, reverse causation). Confidence per item. |
| B5 Problem solving | 15 | Problems | (a) multi-step quantitative (L2), (b) Fermi estimate (L3), (c) ill-defined problem: define it and propose a plan (L5). Confidence per problem. |
| B6 Delayed recall | 5 | Memory | B1's ideas without looking (~50 min later) + 4 cued-recall questions. |
| B7 Writing | 12 | Writing | 250–300 words on a debatable question: thesis, 2 reasons, 1 objection and a reply. |
| B8 Explaining | 7 | Explaining | Explain to a 15-year-old a concept you think you master (≤150 words or transcribed audio), then answer 2 tutor follow-ups. |
| B9 Attention and time | 5 | Attention | 6-item self-report + data observed during the test. |

**Metacognition:** before B3, B4, B5 and B7 the learner predicts their percentage score, later compared with the real one.

**Formats:** full (85 min) · two parts (B0–B6 = 61 min; B7–B9 = 24 min) · three 30-minute days (day 1: B0–B3; day 2: B6 at 24 h + B4 + B7; day 3: B5 + B8 + B9). Record the format and recall delay in `profile.md`; the final diagnostic must repeat them for a valid comparison.

**Generating and running it:** Claude writes the items on the spot, in the learner's language, at medium-high difficulty for an adult. The B1 and B3 texts are about topics unrelated to the anchor subject, to measure skill rather than prior knowledge, and culturally neutral or local to the learner. Present one block at a time; reveal no answers until the block ends. Save the full form (items, answers, scores) in `work/YYYY-MM-DD-diagnostic.md`. For the final diagnostic, build a parallel form: same structure, different content.

**Reference items to calibrate difficulty** (translate when used):
- Deductive: "If a student passes the final, they get the certificate. Ana got the certificate. Does it follow that she passed the final?" → No (affirming the consequent: she may have got it another way).
- Base rate: "A disease affects 1 % of people. The test detects 90 % of the sick and gives a false positive for 9 % of the healthy. Someone tests positive: roughly how likely are they to be sick?" → ≈ 9 % (0.009 / 0.0981).
- Causal: "Fires attended by more firefighters cause more damage. Should we send fewer firefighters?" → No: fire size is a confounder that causes both.
- Ill-defined: "Your team says 'meetings are useless'. Turn that into a question you can investigate and propose how to test it in 2 weeks."

## 2. Scoring (0–4 per dimension)
Percentage → score: ≥90 % → 4 · 75–89 → 3 · 60–74 → 2 · 40–59 → 1 · <40 → 0.

| Dimension | Source | How to score |
|---|---|---|
| Reading comprehension | B3 | Literal items 1 point each; the other 4 score 0–2 each (total 10). Percentage → table. |
| Memory and retrieval | B6 | Percentage of the 12 ideas freely recalled (idea = correct meaning): ≥75 % → 4 · 60–74 → 3 · 45–59 → 2 · 30–44 → 1 · <30 → 0. Also note retention B6/B2. |
| Logical reasoning | B4 | Percentage of the 8 items → table. |
| Problem solving | B5 | Each problem 0–4 with the problem rubric (`evaluation.md`). Mean of the 3. |
| Writing | B7 | Essay rubric (`evaluation.md`). |
| Explaining | B8 | Explanation rubric (`evaluation.md`), follow-ups included. |
| Metacognition | Predictions and confidence | Mean gap \|prediction − result\|: ≤5 points → 4 · 6–10 → 3 · 11–20 → 2 · 21–30 → 1 · >30 → 0. |
| Attention and time | B9 | Mean of the self-report (0–4) and the observed score: start at 4, subtract 1 per unplanned interruption and per block more than 20 % over time (min 0). |

B9 self-report (0 = never … 4 = almost always; items marked (r) are reversed):
1. Last week I worked at least 25 minutes in a row without checking my phone.
2. I know beforehand what I will achieve in each session.
3. When I get distracted, I notice and come back quickly.
4. I finish tasks in the time I planned.
5. I study with notifications on. (r)
6. I leave the hard part for last or avoid it. (r)

## 3. Starting level
Let M be the mean of the 8 dimensions:
- **Foundations:** M < 1.8, or two or more dimensions ≤ 1.
- **Intermediate:** 1.8 ≤ M < 2.6.
- **Advanced:** 2.6 ≤ M < 3.3 and no dimension < 2.
- **Intensive:** M ≥ 3.3, no dimension < 2.5, at least 120 min/day available, usual sleep ≥ 7 h, and no signs of overload.

If any condition fails, assign the level below. Every dimension ≤ 1.5 gets a **reinforcement**: a 10-minute daily micro-block inside step 4 until it exceeds 2 at reassessment. Reassessment: mini-diagnostic in W6 (B3, B4, B5 in a short parallel form) and the full diagnostic in W12.
