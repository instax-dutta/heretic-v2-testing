# Heretic v2 testing

Notes, Optuna journals, and results from testing [Heretic](https://github.com/p-e-w/heretic) v2.0.0.dev0. The goal was to reduce refusals without moving a model too far from its original behaviour, and to compare the results with the v1.4.0 releases.

## What is here

- `docs/`: setup notes, run logs, results, and analysis
- `vm-runs/` and `vm-data-final/`: Optuna journal files from each run
- `analyze_journal.py`: prints the best trials from a journal

Run logs were not committed. They were large and mostly repeated what the journals contain.

## Results

| Model | Trials | Best tradeoff | Baseline |
| :--- | ---: | :--- | :--- |
| utter-project/EuroLLM-1.7B-Instruct | 200 (seed 42) | trial 154: 2/100 refusals, KL 0.0083 | 4/100 |
| HuggingFaceTB/SmolLM2-135M-Instruct | 150 | trial 135: 9/100 refusals, KL 0.0006 | 10/100 |
| LiquidAI/LFM2.5-350M | 150 | trial 113: 7/100 refusals, KL 0.0868 | not measured |
| LiquidAI/LFM2.5-230M | 200, 150, and 200 across three seeds | `heretic-runs3` trial 83: 8/100 refusals, KL 0.0388 | v1.4.0: 10/100, KL 0.0548 |

EuroLLM gave the best result. Trial 154 cut refusals from 4/100 to 2/100 at KL 0.0083. Trial 174 had lower KL (0.0068) but 3/100 refusals, so trial 154 was the better tradeoff. Those numbers come from the run log; the 200-trial journal is not in this repo.

SmolLM2 had two useful points. Trial 135 is the safe choice if you want KL close to zero. Trial 38 gives a larger refusal cut (4/100) at KL 0.0124. Trial 68 is close to trial 135 at 9/100 and KL 0.0011.

LFM2.5-350M did not produce a low-KL option with 10 or fewer refusals. Trials with KL below 0.02 sat around 89/100 refusals. The best trial at 10 or fewer refusals was trial 113, with 7/100 and KL 0.0868.

For LFM2.5-230M, the best result against the v1.4.0 baseline came from the `heretic-runs3` journal (seed 2950566656), trial 83: 8/100 refusals at KL 0.0388. The other seeds found different tradeoffs. Trial 173 in `heretic-runs4` had 4/100 refusals at KL 0.0716.

## Headless runs

Heretic asks for a trial and an action after optimization unless you pass the flags. A fully headless save looks like this:

```bash
heretic --model <model-id> \
  --trial-index 0 \
  --model-action save \
  --save-directory ./out \
  --export-strategy merge
```

`--trial-index` is the position in the sorted Pareto front, not the `[Trial N]` label printed in the menu. For upload, also set `--upload-repo-id`, `--upload-repo-private`, and `--upload-reproducibility-information`, and provide `HF_TOKEN`.

If one of these settings is unset, Heretic prompts for it. With no TTY, that prompt raises `EOFError`. That is a missing flag, not a bug. Several runs in this repo stopped there, which is why the docs mention it.

## Data notes

- `heretic-runs` and `heretic-runs2` are the same journal. They have the same seed and the same md5, so treat them as one run.
- The EuroLLM journal in `vm-data-final/` is a short run with seven trials, not the 200-trial run. The 200-trial numbers in the docs come from the run log.
- The `[Trial N]` labels come from `user_attr["index"]`. The CLI flag `--trial-index` uses a position in the Pareto front. The two numbers do not always match.
- Run logs are ignored by git. The journals are the committed record.

## Reproduction

```bash
heretic --model utter-project/EuroLLM-1.7B-Instruct --seed 42 --n-trials 200
```

Add the headless flags above if you want the run to save or upload without a prompt. The 200-trial EuroLLM journal is not in this repo, so reproduction starts from scratch.

## Links

- [Heretic](https://github.com/p-e-w/heretic)
- [Model collection](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)
- [Testing report gist](https://gist.github.com/instax-dutta/b456ff884c9f570434d964ca8e633297)
