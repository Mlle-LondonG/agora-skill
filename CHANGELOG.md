# Changelog

## 2.2.1 — 2026-10-05

**Now in Claude's plugin directory, and in five languages.**

- Ágora Learning is listed in Anthropic's plugin directory: open **Customize** in Claude and search for it. All READMEs now show this as the easiest way to install.
- README in Italian and French, contributed by [@sivaadithya25](https://github.com/sivaadithya25). Thank you!
- Privacy policy (`PRIVACY.md`), linked from every README.
- The skill itself is unchanged from 2.1.0.

## 2.2.0 — 2026-10-05

**Ready for Claude's plugin directory.**

- The plugin is now called `agora-learning` (shown as "Ágora Learning") so it can't be confused with another listing. Install it with `/plugin install agora-learning@agora-skill`. If you installed 2.1.1 as a plugin, uninstall `agora@agora-skill` first.
- The skill inside is still called `agora` and still starts when you say "Ágora".
- Plugin icon added.
- `agora.zip` is no longer stored in the repository: download it from the latest release.
- The skill itself is unchanged from 2.1.0.

## 2.1.1 — 2026-10-04

**One-command install.**

- The repository is now a Claude Code plugin and marketplace (`.claude-plugin/`): `/plugin marketplace add Mlle-LondonG/agora-skill`, then `/plugin install agora@agora-skill`. Validated with `claude plugin validate --strict`.
- Documented `npx skills add Mlle-LondonG/agora-skill` for any agent that supports skills.
- Social preview image for link sharing.
- The skill itself is unchanged from 2.1.0.

## 2.1.0 — 2026-10-04

**Attention mode (ADHD-friendly).**

- New `references/attention.md`: an opt-in mode that never diagnoses and gives no medication advice. 10–20-minute blocks with one visible task, movement breaks, a 2-minute start ritual with if-then plans, a parking list, a 10-minute micro-session, energy gating, at most 8 review cards a day, comebacks instead of streaks, time checks and a hyperfocus guard.
- Evidence added: retrieval practice in students with ADHD (Knouse et al., 2016; Minear et al., 2023), implementation intentions (Gawrilow & Gollwitzer, 2008), cognitive-behavioural programmes (Cochrane 2018; ACCESS), physical activity (Yang et al., 2025), cognitive training (Cortese et al., 2015), hyperfocus (Ashinoff & Abu-Akel, 2021).
- `metrics.py` now reports comebacks after 2+ days off.
- Diagnostic: the attention block is explicitly not an ADHD screen.
- Hyperfocus guard added to the rest rules for everyone.
- Example sessions in attention mode (English and Spanish).

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
