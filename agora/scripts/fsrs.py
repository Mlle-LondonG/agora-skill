#!/usr/bin/env python3
"""Ágora · FSRS spaced-repetition scheduler for cards.csv (Python 3.8+, standard library only).

A day-based port of FSRS-6 (default parameters from the open-spaced-repetition
py-fsrs project, MIT). No learning steps and no fuzzing: every review schedules
the card a whole number of days ahead, which suits daily study sessions.

Usage:
  python3 fsrs.py due     cards.csv [--date YYYY-MM-DD] [--limit 15]
  python3 fsrs.py review  cards.csv CARD_ID RATING [--date YYYY-MM-DD]
  python3 fsrs.py stats   cards.csv [--date YYYY-MM-DD]

RATING: 1/again (wrong) · 2/hard (partial) · 3/good (right) · 4/easy (right, fast, sure)
Options: --retention 0.9 (target probability of recall when a card comes due)
"""
import argparse
import csv
import datetime as dt
import math
import sys

W = (0.212, 1.2931, 2.3065, 8.2956, 6.4133, 0.8334, 3.0194, 0.001, 1.8722, 0.1666,
     0.796, 1.4835, 0.0614, 0.2629, 1.6483, 0.6014, 1.8729, 0.5425, 0.0912, 0.0658, 0.1542)
DECAY = -W[20]
FACTOR = 0.9 ** (1 / DECAY) - 1
S_MIN, D_MIN, D_MAX, MAX_IVL = 0.001, 1.0, 10.0, 36500
FIELDS = ["id", "topic", "question", "answer_key", "source", "created", "due",
          "stability", "difficulty", "last_review", "reps", "lapses", "box"]
RATINGS = {"1": 1, "again": 1, "2": 2, "hard": 2, "3": 3, "good": 3, "4": 4, "easy": 4}


def clamp_d(d):
    return min(max(d, D_MIN), D_MAX)


def init_s(g):
    return max(W[g - 1], S_MIN)


def init_d(g, clamp=True):
    d = W[4] - math.e ** (W[5] * (g - 1)) + 1
    return clamp_d(d) if clamp else d


def retrievability(elapsed_days, s):
    return (1 + FACTOR * max(0, elapsed_days) / s) ** DECAY


def next_interval(s, retention):
    ivl = round((s / FACTOR) * (retention ** (1 / DECAY) - 1))
    return min(max(ivl, 1), MAX_IVL)


def next_d(d, g):
    delta = -(W[6] * (g - 3))
    damped = d + (10.0 - d) * delta / 9.0
    return clamp_d(W[7] * init_d(4, clamp=False) + (1 - W[7]) * damped)


def short_term_s(s, g):
    inc = (math.e ** (W[17] * (g - 3 + W[18]))) * (s ** -W[19])
    if g > 1:
        inc = max(inc, 1.0)
    return max(s * inc, S_MIN)


def recall_s(d, s, r, g):
    hard = W[15] if g == 2 else 1
    easy = W[16] if g == 4 else 1
    return s * (1 + math.e ** W[8] * (11 - d) * s ** -W[9] * (math.e ** ((1 - r) * W[10]) - 1) * hard * easy)


def forget_s(d, s, r):
    long_term = W[11] * d ** -W[12] * ((s + 1) ** W[13] - 1) * math.e ** ((1 - r) * W[14])
    short_term = s / math.e ** (W[17] * W[18])
    return min(long_term, short_term)


def schedule(card, g, today, retention):
    """Update one card (dict) in place for rating g (1-4) reviewed on `today`."""
    s = float(card["stability"]) if card.get("stability") else None
    d = float(card["difficulty"]) if card.get("difficulty") else None
    last = dt.date.fromisoformat(card["last_review"]) if card.get("last_review") else None
    if s is None or d is None:
        s, d = init_s(g), init_d(g)
    else:
        elapsed = (today - last).days if last else 0
        if elapsed < 1:
            s = short_term_s(s, g)
        else:
            r = retrievability(elapsed, s)
            s = max(forget_s(d, s, r) if g == 1 else recall_s(d, s, r, g), S_MIN)
        d = next_d(d, g)
    card["stability"] = f"{s:.6f}"
    card["difficulty"] = f"{d:.6f}"
    card["last_review"] = today.isoformat()
    card["due"] = (today + dt.timedelta(days=next_interval(s, retention))).isoformat()
    card["reps"] = str(int(card.get("reps") or 0) + 1)
    if g == 1 and int(card["reps"]) > 1:
        card["lapses"] = str(int(card.get("lapses") or 0) + 1)
    return card


def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k in FIELDS:
            r.setdefault(k, "")
    return rows


def save(path, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def due_date(card):
    return dt.date.fromisoformat(card.get("due") or card.get("created") or "1970-01-01")


def current_r(card, today):
    if not card.get("stability") or not card.get("last_review"):
        return 0.0
    elapsed = (today - dt.date.fromisoformat(card["last_review"])).days
    return retrievability(elapsed, float(card["stability"]))


def main():
    p = argparse.ArgumentParser(description="Ágora FSRS scheduler")
    p.add_argument("command", choices=["due", "review", "stats"])
    p.add_argument("csv")
    p.add_argument("card_id", nargs="?")
    p.add_argument("rating", nargs="?")
    p.add_argument("--date", default=dt.date.today().isoformat())
    p.add_argument("--limit", type=int, default=15)
    p.add_argument("--retention", type=float, default=0.9)
    a = p.parse_args()
    today = dt.date.fromisoformat(a.date)
    rows = load(a.csv)

    if a.command == "review":
        if not a.card_id or not a.rating or a.rating.lower() not in RATINGS:
            sys.exit("Usage: fsrs.py review cards.csv CARD_ID {1|2|3|4|again|hard|good|easy}")
        card = next((r for r in rows if r["id"] == a.card_id), None)
        if card is None:
            sys.exit(f"Card {a.card_id} not found")
        schedule(card, RATINGS[a.rating.lower()], today, a.retention)
        save(a.csv, rows)
        print(f"{card['id']}: next review {card['due']} · stability {float(card['stability']):.1f} d · "
              f"difficulty {float(card['difficulty']):.1f}/10")

    elif a.command == "due":
        due = [r for r in rows if due_date(r) <= today and (r.get("box") or "") != "retired"]
        due.sort(key=lambda r: (current_r(r, today) if r.get("last_review") else -1, due_date(r)))
        print(f"{len(due)} card(s) due on {today}; showing {min(len(due), a.limit)}")
        for r in due[: a.limit]:
            state = "new" if not r.get("last_review") else f"R={current_r(r, today):.0%}"
            print(f"{r['id']}\t{state}\t{r['topic']}\t{r['question']}")

    else:
        reviewed = [r for r in rows if r.get("last_review")]
        week = today + dt.timedelta(days=7)
        print(f"Cards: {len(rows)} · new: {len(rows) - len(reviewed)} · due today: "
              f"{sum(due_date(r) <= today for r in rows)} · due in 7 days: {sum(due_date(r) <= week for r in rows)}")
        if reviewed:
            rs = [current_r(r, today) for r in reviewed]
            print(f"Average predicted recall today: {sum(rs) / len(rs):.0%} · "
                  f"lapses: {sum(int(r.get('lapses') or 0) for r in rows)} · "
                  f"stable (≥21 d): {sum(float(r['stability']) >= 21 for r in reviewed)}")


if __name__ == "__main__":
    main()
