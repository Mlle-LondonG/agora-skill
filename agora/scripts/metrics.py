#!/usr/bin/env python3
"""Ágora · metrics summary from sessions.csv (Python 3.8+, standard library only).

Usage:
  python3 metrics.py                     # last 7 days, sessions.csv in the current folder
  python3 metrics.py path/sessions.csv   # another path
  python3 metrics.py --days 28           # monthly window
"""
import argparse
import csv
import datetime as dt
import statistics as st


def num(row, key):
    value = (row.get(key) or "").strip().replace(",", ".")
    try:
        return float(value) if value else None
    except ValueError:
        return None


def mean_of(rows, key):
    values = [v for v in (num(r, key) for r in rows) if v is not None]
    return f"{st.mean(values):.1f}" if values else "—"


def main():
    p = argparse.ArgumentParser(description="Ágora metrics summary")
    p.add_argument("csv", nargs="?", default="sessions.csv")
    p.add_argument("--days", type=int, default=7)
    a = p.parse_args()

    with open(a.csv, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    since = dt.date.today() - dt.timedelta(days=a.days)
    S = [r for r in rows if r.get("date") and dt.date.fromisoformat(r["date"]) > since]
    if not S:
        print(f"No sessions in the last {a.days} days.")
        return

    ok = sum(num(r, "recall_ok") or 0 for r in S)
    tot = sum(num(r, "recall_total") or 0 for r in S)
    gaps = []
    for r in S:
        pred, rok, rtot = num(r, "prediction_pct"), num(r, "recall_ok"), num(r, "recall_total")
        if pred is not None and rok is not None and rtot:
            gaps.append(pred - 100 * rok / rtot)
    valid = [int(sum(num(r, f"l{i}") or 0 for r in S)) for i in range(1, 6)]
    points = sum(n * level for level, n in enumerate(valid, start=1))
    minutes = sum(num(r, "min_actual") or 0 for r in S)

    print(f"Ágora · last {a.days} days · {len(S)} session(s) · {minutes:.0f} min")
    print(f"Recall without notes: {ok / tot:.0%}" if tot else "Recall without notes: —")
    if gaps:
        bias = st.mean(gaps)
        kind = "overconfident" if bias > 0 else "underconfident" if bias < 0 else "calibrated"
        print(f"Calibration: {st.mean(abs(g) for g in gaps):.1f} pt mean gap ({kind})")
    print(f"Valid solutions L1–L5: {'/'.join(map(str, valid))} · points: {points}")
    print(f"Explanation {mean_of(S, 'explanation')}/4 · Transfer {mean_of(S, 'transfer')}/4 · "
          f"Questions {mean_of(S, 'questions')}/4")
    print(f"Mean sleep {mean_of(S, 'sleep_h')} h · Mean energy {mean_of(S, 'energy')}/5")

    if tot:
        r = ok / tot
        if r < 0.60:
            rule = "recall <60%: no new content; retrieval, worked examples and prerequisites only."
        elif r < 0.80:
            rule = "recall 60–79%: halve new content, double retrieval."
        elif r <= 0.90:
            rule = "recall 80–90%: keep difficulty, let reviews space out."
        else:
            rule = "recall >90%: raise complexity only if transfer ≥3 on an L4 problem."
        print(f"Suggested rule (SKILL.md §8): {rule}")


if __name__ == "__main__":
    main()
