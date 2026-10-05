# Example: a 30-minute session (English)

> Illustrative and fictional. It shows how Ágora runs a session: Claude does not explain before the learner tries, grades honestly and logs everything at the end.
> Also available in [Español](session-30-min.es.md) · [Português](session-30-min.pt-BR.md) (a language-learning session).

**Context:** university profile · anchor subject: Calculus I · Intermediate level · week 3 (first principles), day 2 · scheduler: FSRS.

---

**Learner:** Ágora, 30-minute session.

**Ágora:** I've read your notebook. You have 4 cards due and one open error: [PROC] forgetting the inner derivative in the chain rule. Before we start: how many hours did you sleep, and how is your energy from 1 to 5?

**Learner:** 7 hours, energy 4.

**Ágora:** Today's agenda (start a timer):
1 min define · 5 retrieve · 7 study · 9 solve · 4 explain · 2 correct · 2 log.

**Step 1.** Complete: "By the end I will be able to ___ and I will show it by ___".

**Learner:** By the end I will understand the chain rule.

**Ágora:** "Understand" can't be observed. Suggestion: "differentiate three-layer composite functions, shown by an L2 problem with no hints". Does that work?

**Learner:** Yes.

**Ágora:** **Step 2.** Without looking at anything, answer all 5, and before I grade, tell me what percentage you think you got right.
1. The definition of the derivative as a limit.
2. Why is |x| not differentiable at 0?
3. Differentiate sin(x²).
4. What does f′(a) measure on a graph?
5. (From week 1) What separates the derivative at a point from the derivative function?

**Learner:** *(answers)* I think I got 90 %.

**Ágora:** Result: 1 ✔ · 2 ✔ · 3 ✘ you wrote cos(x²); the factor 2x is missing · 4 ✔ · 5 partial. Total 3.5/5 = 70 %. You predicted 90 %: **20 points of overconfidence**. Question 3 is the same error you have open. Card c2 is rated *again* and comes back tomorrow.

**Step 3.** Before opening your book, write the guiding question. Format hint: what problem does the chain rule solve, and why does a product appear?

*(…7 minutes of study with a worked example and 2 questions of their own…)*

**Step 4.** L2 problem. You have 10 minutes of attempt before the first hint: differentiate h(x) = e^(cos(3x)).

**Learner:** −3·sin(3x)·e^(cos 3x)

**Ágora:** Correct, no hints, in 4 minutes. Valid L2 solution.

**Step 5.** Explain in 5 lines, to someone who knows no calculus, why three factors appear.

*(…explanation…)*

**Ágora:** Two follow-ups. Assumption: what must each layer satisfy for the rule to hold? Counterexample: what happens with |sin x| at x = 0?

**Step 6.** Explanation rubric: precision 3 · mechanism 2 (you name the layers but not why the rates multiply) · example and limits 2 · clarity 3 → **2.5/4**.
Strength: you break down the layers well. Priority improvement: justify the product as "a rate of a rate".

**Step 7.** Notebook:
- `sessions.csv`: recall 3.5 of 5, prediction 90, l2 = 1, max hint H0, explanation 2.5.
- `errors.md`: [PROC] inner-derivative factor, second occurrence. Warning sign: "a function inside another → look for one more factor".
- `cards.csv`: 3 new cards; `fsrs.py review` run for the 5 retrieved.

**Close:** recall 70 % with 20 pts of overconfidence · 1 valid L2 solution · main error: inner derivative · rule for next session: recall 60–79 %, so new content is halved and retrieval doubled · tomorrow's first question: "differentiate ln(cos(x³))".
