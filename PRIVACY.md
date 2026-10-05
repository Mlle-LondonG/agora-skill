# Privacy

Ágora is a set of instructions and two small local scripts. It has no server, no account, no analytics and no telemetry.

## What it stores

If you give Claude access to a folder, Ágora keeps a study notebook there as plain files (`agora-notebook/`): your goal and level, one row per study session (minutes, scores, optional hours of sleep and energy level), your error log, review cards and the list of your study materials. Without folder access it keeps nothing; it gives you a text block to paste next time.

## Where it goes

Nowhere else. The notebook stays in your folder. The scripts (`fsrs.py`, `metrics.py`) only read and write those files and make no network connections. The plugin sends no data to the author or to any third party.

What you type and the files you share are processed by Claude under the terms and privacy policy of the Claude product you use.

## Your control

You can read, edit or delete the notebook at any time. Deleting the folder removes everything Ágora stored.

## Contact

Questions: open an issue at https://github.com/Mlle-LondonG/agora-skill/issues.
