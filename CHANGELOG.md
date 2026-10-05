# Changelog

## 2.0.0 — 2026-10-04

**Multilingual, lighter, and with real spaced repetition.**

- The skill is now written in English and talks to each learner in their own language (Spanish, Portuguese, Italian, French, German, English…). File names stay in English so scripts keep working. Trigger words cover several languages.
- Language-learning mode: instructions in the learner's language, practice in the target language, immersion that grows with level, language-specific error tracking and a language capstone.
- New structure: a short core `SKILL.md` (≈4.5k tokens, down from ≈20k) plus `references/` loaded only when a mode needs them.
- FSRS-6 scheduling via `scripts/fsrs.py` (standard library only), verified against py-fsrs on 1,924 simulated reviews. Leitner boxes remain as a fallback without Python.
- Source intake: protocol for the learner's PDFs, notes and syllabus, with page-cited cards, isomorphic practice problems, fidelity rules and a held-out set of past exams.
- Notation: problem levels L1–L5, hints H0–H5, error types CON/PROC/READ/SLIP/STRAT/PREREQ.
- Docs: English README with Spanish and Portuguese translations; example sessions in English, Spanish and Portuguese (language learning).
- 1.x notebooks (`perfil.md`, `sesiones.csv`…) are migrated to the new format, keeping every row and a backup of the originals.

## 1.0.0 — 2026-10-04

First public release (Spanish).

- Mode router: onboarding, diagnostic, daily session, Socratic tutoring, topic cycle, review, project, blockage diagnosis and manual.
- 85-minute diagnostic with rubrics and level assignment.
- 12-week curriculum adapted to 30, 60, 120 and 180 minutes a day.
- Progress notebook with Leitner spaced repetition and a state block for environments without files.
- Adaptive difficulty rules, blockage diagnosis and burnout prevention.
- Socratic tutor prompt for any AI.
