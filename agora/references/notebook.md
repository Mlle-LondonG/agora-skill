# Notebook formats

File names and CSV headers stay in English; cell contents are written in the learner's language.

## profile.md
```
# ÁGORA — Profile and plan
Start: YYYY-MM-DD | Current week: N | Day: D | Day off: … | Language: … | Scheduler: fsrs / leitner
Attention mode: off / on (block __ min, best focus window: …)
Profile: … | Anchor subject: … | Materials: (see sources.md)
Observable goal (12 weeks): By the end I will be able to … and I will show it by …
Time: … min/day, … days/week | Key dates: … | Discusses with: …
Diagnostic (date, format, recall delay): Reading _ · Memory _ · Logic _ · Problems _ ·
  Writing _ · Explaining _ · Metacognition _ · Attention _ → mean _ → level _
Reinforcements (dimensions ≤1.5): … | Active adaptive rule: …
## 12-week plan
| W | Competency | Anchor-subject topic | Case | Written work |
```

## sessions.csv
```
date,week,mode,min_planned,min_actual,topic,recall_ok,recall_total,prediction_pct,l1,l2,l3,l4,l5,max_hint,ref_level,min_to_solution,explanation,transfer,questions,sleep_h,energy,notes
```
- `l1`…`l5`: valid solutions per problem level.
- `ref_level`, `min_to_solution`: the hardest valid problem of the session and its minutes to a valid solution.
- `explanation`, `transfer`, `questions`: 0–4 (empty if not assessed). `energy`: 1–5. Decimals with a dot.

## errors.md
```
| date | topic | what happened | type | root cause | fix | warning sign | status |
|---|---|---|---|---|---|---|---|
```
Types: **CON** concept · **PROC** procedure · **READ** misreading the task · **SLIP** careless slip · **STRAT** strategy · **PREREQ** missing prerequisite.
Status: open → reviewed → closed (closed = not repeated in 2 reviews).

## cards.csv
```
id,topic,question,answer_key,source,created,due,stability,difficulty,last_review,reps,lapses,box
```
- New card: fill `id`, `topic`, `question`, `answer_key`, `source` (e.g. `S1 p.45`, see `sources.md`), `created` and `due` = today; leave the rest empty (`reps`, `lapses` = 0).
- **Good cards:** one idea per card. Prefer "why…?", "when does … fail?" and "how…?" over bare definitions. For languages, full sentences in context, both directions. For problems, a new statement, not a memorised answer. Write the card in the learner's language (or the target language when practising one).
- Create 3–5 cards per session from what was studied and from errors.

### FSRS (default when Python is available)
The script lives in the skill's `scripts/` folder; `cards.csv` lives in the notebook:
```
python3 scripts/fsrs.py due    path/cards.csv [--date YYYY-MM-DD] [--limit 15]
python3 scripts/fsrs.py review path/cards.csv CARD_ID again|hard|good|easy [--date YYYY-MM-DD]
python3 scripts/fsrs.py stats  path/cards.csv
```
Ratings: wrong → `again` · partial → `hard` · correct → `good` · correct, fast and confident → `easy`. Default target retention 0.9 (`--retention`). The script fills `stability`, `difficulty`, `due`, `last_review`, `reps`, `lapses`. [E+ for spacing; FSRS is a data-fitted scheduler from the open-spaced-repetition project]

**Monthly long-term check:** sample 10 cards with stability ≥ 21 days. If fewer than 8 are correct, review the failed ones with `again`.

### Leitner fallback (no Python)
Use the `box` column. Intervals by box: 1 → 1 day · 2 → 3 · 3 → 7 · 4 → 16 · 5 → 35 · 6 → 90. Correct in box 6 → `retired`.
- Correct → up one box. Partial → down one box (min 1). Wrong → box 1. `due` = today + the new box's interval.
- Monthly: sample 10 retired cards; if fewer than 8 are correct, the failed ones return to box 3.
[P: expanding intervals consistent with [E+] on spacing; the exact numbers are a convention]

## reviews.md
Weekly and monthly reviews with the adaptive decisions (templates in `evaluation.md`).

## sources.md
The learner's materials and how they map to the plan (format and protocol in `references/sources.md`).

## work/
Diagnostics, essays, solutions, memos and projects, named `YYYY-MM-DD-topic.md`.

## Metrics script
```
python3 scripts/metrics.py path/sessions.csv [--days 7|28]
```
Prints recall, calibration (with over/under-confidence), valid solutions per level, rubric means, sleep and energy, comebacks after a gap of 2+ days, and the suggested adaptive rule. Report the results in the learner's language.

## State block (no file access)
At every close, give this block (translated) and ask the learner to paste it at the start of the next session:
```
ÁGORA·STATE v2 | date: YYYY-MM-DD | language: …
profile: … | subject: … | level: … | min/day: … | week: N (day D)
goal: …
7-day metrics: recall __% | calibration __ pts | valid L1–L5: _/_/_/_/_ | explanation _/4 | consistency _/_
active rule: …
open errors: [type] … ; [type] …
due cards (max 10): id | question | due | box
next: __-min session, W_ day _ — guiding question: …
```
Without files, use Leitner boxes for the cards in the block.

## Migrating a v1 notebook (Spanish, Ágora 1.x)
Copy, never delete: move the originals into `v1-backup/` and write the new files next to them.

| v1 file | v2 file | Column or value changes |
|---|---|---|
| `perfil.md` | `profile.md` | Translate labels; add `Language` and `Scheduler: fsrs` |
| `sesiones.csv` | `sessions.csv` | fecha→date · semana→week · modo→mode · min_plan→min_planned · min_real→min_actual · tema→topic · recup_ok→recall_ok · recup_total→recall_total · prediccion_pct→prediction_pct · n1…n5→l1…l5 · pista_max→max_hint (P→H) · nivel_ref→ref_level (N→L) · min_a_solucion→min_to_solution · explicacion→explanation · transferencia→transfer · preguntas→questions · sueno_h→sleep_h · energia→energy · notas→notes |
| `errores.md` | `errors.md` | Types C→CON · P→PROC · L→READ · D→SLIP · E→STRAT · R→PREREQ |
| `repasos.csv` | `cards.csv` | tema→topic · pregunta→question · respuesta_clave→answer_key · creado→created · proximo→due · ultimo→last_review · caja→box; leave `stability`, `difficulty` empty (FSRS starts them at the next review) and `source` empty |
| `revisiones.md` | `reviews.md` | — |
| `producciones/` | `work/` | — |

Cell contents stay as they are. Tell the learner what was migrated.
