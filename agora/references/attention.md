# Attention mode (ADHD-friendly)

An optional way of running Ágora for learners with ADHD or who find sustained attention hard. It changes how the work is packaged (block length, structure, load, metrics), not the learning science: the same retrieval, spacing and feedback still do the heavy lifting.

## 1. Activation and boundaries
- **Opt-in only.** Offer it when the learner mentions ADHD, attention difficulties or "I can't focus", or asks for it. Ask once; record `Attention mode: on (block N min)` in `profile.md`. The learner can switch it off at any time.
- **Never infer or diagnose.** Low focus scores, the B9 attention block or missed sessions are not signs of ADHD and must never be presented as such.
- **Medication:** give no advice on medication or its timing. If the learner says when they focus best (for any reason), schedule the demanding steps in that window.
- **Professional help:** at activation, mention once that structured programmes based on cognitive-behavioural therapy have evidence for adults and college students with ADHD and that a professional can help. Do not repeat it every session.

## 2. What the evidence says (and how Ágora uses it)
| Finding | Evidence | Use in Ágora |
|---|---|---|
| Retrieval practice helps students with ADHD as much as other students | [E] Knouse et al. (2016); Minear et al. (2023) | Keep retrieval and spacing at the core |
| Unmedicated students with ADHD used fewer deep encoding strategies and scored lower, despite benefiting from retrieval | [E] Minear et al. (2023) | Give more structure while studying: worked examples, guided self-explanation, question–answer notes |
| If-then plans (implementation intentions) improved response inhibition in children with ADHD in lab tasks | [E, lab-based] Gawrilow & Gollwitzer (2008) | If-then plans for the learner's top distractions |
| CBT-based programmes that train planning and organisation help adults and college students with ADHD | [E, low-to-moderate quality] Cochrane review (2018); ACCESS trial | Borrow the tools (external plans, checklists, routines); Ágora is not therapy |
| Physical activity improves inhibitory control in adults with ADHD | [E, small studies] Yang et al. (2025) meta-analysis | Movement breaks between blocks |
| Working-memory training improves lab tasks but not ADHD symptoms or school results on blinded measures | [E+] Cortese et al. (2015) | No "brain training" in Ágora |
| Hyperfocus is widely reported but poorly studied | [P] Ashinoff & Abu-Akel (2021) | Time checks and a hard stop |
| Body doubling (working alongside someone) is popular | [P] little controlled research | Optional "stay with me" check-ins |

## 3. What changes
| Element | Standard Ágora | Attention mode |
|---|---|---|
| Work blocks | Steps of up to 50 min | Blocks of 10, 15 or 20 min (learner chooses), each with **one visible task**, separated by 2–3 min movement breaks |
| Agenda | Full agenda at the start | Only the current step and the time left; full agenda on request |
| Starting | Define the outcome | 2-minute start ritual (§4) |
| Long sessions | 120 / 180 min in one sitting | Split into 2–3 sittings of the 60-min format at different times of day, ≥30 min apart |
| Daily cards | Up to 15 | Up to 8 (`fsrs.py due cards.csv --limit 8`); the rest wait for the next days, lowest recall first |
| Study step | Guiding question + material | Same, chunked one idea at a time, worked example first, guided self-explanation prompts, Q&A note template |
| Problems | One at a time | One at a time with visible progress ("2 of 3") and alternating formats to keep novelty |
| Explaining | Written or audio | Audio or speaking aloud is the default; writing optional |
| Diagnostic | 85 min, 2 parts or 3 days | Always 3 days of ~30 min, each split into two blocks with a break |
| Missed sessions | Next one is normal | No guilt language; restart with the 10-minute micro-session (§5) |
| Metrics | Consistency = done / planned | Report **comebacks** (sessions started after a gap of 2+ days) and sessions done this week; no streaks |
| Time awareness | Learner keeps a timer | Claude states elapsed and remaining time at every step (asks for the timer reading if it cannot see the clock) |
| Hyperfocus | Daily ceiling | Time check every 45 min of continuous work; hard stop at the planned end + 15 min; daily ceiling unchanged |

## 4. Start ritual (2 minutes)
1. Phone in another room or face down with notifications off; open only today's material.
2. Write the first tiny action ("open chapter 3, page 41, problem 1").
3. Write 1–2 if-then plans for the likeliest distractions ("If I want to check messages, I'll note it on the parking list and continue").
4. Start the timer for the first block.
Keep a **parking list** in the session: intrusive thoughts and errands go there to be handled after the session.

## 5. Session formats
**Micro-session (10 min)** — for energy 1–2, a restart after missed days, or a bad day: 1 define · 3 retrieve (max 4 cards) · 5 one L1–L2 problem · 1 log.

**30 min (2 blocks)**

| Part | Min |
|---|---|
| Start ritual + define | 2 |
| Block 1: retrieve (4 min) + study one chunk (8 min) | 12 |
| Movement break | 3 |
| Block 2: solve (7 min) + explain aloud (3 min) | 10 |
| Correct (1 min) + log (2 min) | 3 |
| **Total** | **30** |

**60 min (4 blocks)**

| Part | Min |
|---|---|
| Start ritual + define | 3 |
| Block 1: retrieve | 12 |
| Movement break | 3 |
| Block 2: study with guiding question (chunked) | 12 |
| Movement break | 3 |
| Block 3: solve, one problem at a time | 15 |
| Break | 2 |
| Block 4: explain aloud (4) + correct (3) | 7 |
| Log | 3 |
| **Total** | **60** |

With 15- or 20-minute blocks, merge adjacent blocks and keep one break per block.

**Energy gating:** energy 1–2 → micro-session; energy 3 → the 30-min format; energy 4–5 → the planned format.

## 6. "Stay with me" (optional)
The learner says "start"; Claude confirms the single task and the block length, stays silent, and checks in when the learner returns: "Block done? What did you finish? Anything for the parking list?" Then it announces the break and the next block.

## 7. Weekly review additions
Add to the weekly review: block length that worked best, comebacks this week, energy pattern by time of day, and one adjustment to try next week (e.g. shorter blocks, a different time, more movement).
