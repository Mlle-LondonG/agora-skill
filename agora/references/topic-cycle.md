# Topic cycle (any subject)

Use it when starting each topic or syllabus block. Save it as `work/YYYY-MM-DD-topic-cycle.md`, written in the learner's language.

```
ÁGORA CYCLE — [Topic]                                   Start: [date]
0. Observable outcome: By the end I will be able to … and I will show it by …
1. Guiding question or problem:
2. Prerequisites: … | 3-question self-test (if <2/3: mini-cycle on the prerequisite)
3. Sources: 1 main + 1 contrasting (see sources.md).
   Quality criteria: identifiable authorship · explicit evidence or derivation ·
   right level · exercises with solutions · up to date (if the field moves fast)
4. Active retrieval: 10 questions (5 facts or definitions, 3 "why?", 2 "when does it fail?")
5. Graded exercises: L1×3 · L2×3 · L3×2 · L4×1 · L5 (optional)
6. Application case:
7. Final project or product:
8. Teach someone: who · format · 3 hard questions I expect
9. Error log: (errors.md, tagged with the topic)
10. Spaced reviews: scheduled by fsrs.py (or Leitner) → first dates
Closing criterion: recall ≥85 % after 7 days · 2 valid L3 solutions ·
transfer ≥3 on one L4 problem · explanation ≥3
```

## Worked examples (condensed)

**Calculus: the derivative**
0. I will solve optimisation and related-rates problems, shown by 3 L3 problems with no hints.
1. Why is the slope of the tangent the limit of secant slopes, and how do I use that to optimise?
2. Functions, slope, basic limits, algebra of fractions. Self-test: simplify (x²−9)/(x−3); slope between two points; lim (x→3) of that expression.
3. OpenStax *Calculus Vol. 1* (free) with MIT OpenCourseWare 18.01 as contrast.
4. Limit definition from memory · derive x² and x³ from the definition · why is |x| not differentiable at 0? · when does applying the chain rule blindly fail?
5. L1 differentiate polynomials · L2 chain rule · L3 the sliding ladder (related rates) · L4 the fixed-volume can with minimum surface · L5 model the cost of a real business.
6. With an estimated linear demand q = a − b·p, choose the revenue-maximising price and analyse what happens if b changes.
7. One-page report: model, graph and sensitivity analysis.
8. Explain to a 15-year-old why the derivative of x² is 2x, drawing secants that close in.
9. Typical errors: confusing the derivative at a point with the derivative function [CON]; forgetting the inner derivative [PROC].

**Programming: recursion in Python**
0. I will write and debug recursive functions, shown by a folder-tree walker that passes its tests.
1. How can a function solve a problem by calling itself without looping forever, and when is it worth it?
2. Functions, conditionals, lists, the call stack. Self-test: trace 3 nested calls by hand.
3. The official Python tutorial (docs.python.org) with MIT OCW 6.100L as contrast.
4. Base case + recursive case from memory · trace the stack of factorial(4) · when would Python's recursion limit blow up?
5. L1 sum a list · L2 reverse a string · L3 permutations · L4 total size of a nested folder · L5 solve a maze with backtracking.
6. A tool that finds the 10 largest files in a folder with subfolders.
7. Script, tests and a README explaining the complexity.
8. Explain recursion with nesting dolls, then trace the code.
9. AI rule: write it first without AI. Then AI reviews, proposes test cases and counterexamples; it does not rewrite the code.
Typical errors: missing base case [CON]; the problem does not shrink on each call [PROC].

**History: causes of the First World War**
0. I will explain and defend why the July 1914 crisis escalated, shown by a 1500-word essay defended in supervision.
1. Why did an assassination in Sarajevo turn into a general war within weeks?
2. Map of Europe in 1914, alliance system, nationalism, imperialism. Self-test: place the blocs and 3 earlier crises.
3. A university textbook as synthesis; primary sources (Germany's "blank cheque", the Austro-Hungarian ultimatum to Serbia); two opposing historiographical theses (Fritz Fischer, 1961, versus Christopher Clark, *The Sleepwalkers*, 2012). Use editions in the learner's language when available.
4. Timeline of the July crisis without looking · 4 structural causes and 3 triggers · what separates a cause from a trigger?
5. L1 timeline · L2 compare two primary sources · L3 assess a counterfactual (what if Russia had not mobilised?) · L4 compare with the 1962 Cuban Missile Crisis: why did that one not escalate? · L5 historiographical essay.
6. You advise the British government in late July 1914: a memo using only the information available then.
7. Cambridge-style essay: "Was the war inevitable?"
8. A 3-minute explanation with a causal diagram.
9. Typical errors: hindsight bias [STRAT]; single-cause explanation [CON]; treating a secondary source as primary [READ].

**Languages: narrating the past (any target language)**
Pick the contrast that fits the target language: English *past simple* vs *present perfect* · Spanish *pretérito indefinido* vs *imperfecto* · Portuguese *pretérito perfeito* vs *imperfeito* · Italian *passato prossimo* vs *imperfetto* · French *passé composé* vs *imparfait*.
0. I will tell a past experience with temporal precision and fluency, shown by a 3-minute recording with fewer than 3 tense errors per 100 words.
1. When do I use each form, and how do I narrate fluently?
2. Past conjugation and the 50 most frequent irregular verbs. Self-test: 10 forms without looking.
3. A grammar with an answer key, graded authentic audio (podcasts at the learner's level) and human or AI correction.
4. 10 sentences produced from memory from prompts in the learner's language · two-way cards with full sentences, not single words.
5. L1 fill the gaps · L2 transform sentences · L3 2-minute recorded anecdote · L4 conversation with unexpected follow-ups · L5 argue a position in a simulated meeting.
6. A simulated job interview with Claude as the interviewer.
7. A 5-minute recording and its corrected transcript.
8. Explain the contrast to another learner with a timeline.
9. Own metrics: errors per 100 words, words per minute, % of sentences recalled.
Typical errors: word lists without context [STRAT]; not speaking until "ready" [STRAT].
