#!/usr/bin/env python3
"""Print the best trials from one or more Heretic Optuna journals."""

import argparse
import json


def load_trials(path):
    trials = {}
    with open(path) as handle:
        for line in handle:
            record = json.loads(line)
            trial_id = record.get("trial_id")
            if trial_id is None:
                continue
            trial = trials.setdefault(trial_id, {})
            if "user_attr" in record:
                trial.update(record["user_attr"])
            if "state" in record:
                trial["state"] = record["state"]
    return trials


def scores(trial):
    values = {}
    for item in trial.get("scores", []):
        values[item["name"]] = item["score"]["value"]
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("journals", nargs="+")
    parser.add_argument("--max-kl", type=float, default=0.02)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    for path in args.journals:
        rows = []
        for trial in load_trials(path).values():
            if trial.get("state") != 1:  # Optuna COMPLETE
                continue
            values = scores(trial)
            if "KL divergence" in values and "Refusals" in values:
                rows.append((trial.get("index"), values["KL divergence"], values["Refusals"]))

        print(f"\n{path}")
        print(f"  completed trials: {len(rows)}")

        low_kl = [row for row in rows if row[1] < args.max_kl]
        low_kl.sort(key=lambda row: (row[2], row[1]))
        print(f"  lowest refusals with KL below {args.max_kl:g}:")
        for index, kl, refusals in low_kl[: args.top]:
            print(f"    trial {index}: {refusals * 100:.0f}/100 refusals, KL {kl:.6f}")

        rows.sort(key=lambda row: (row[1], row[2]))
        print("  lowest KL overall:")
        for index, kl, refusals in rows[: args.top]:
            print(f"    trial {index}: KL {kl:.6f}, {refusals * 100:.0f}/100 refusals")


if __name__ == "__main__":
    main()
