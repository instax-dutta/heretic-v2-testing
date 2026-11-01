# Findings

I tested Heretic v2.0.0.dev0 on SmolLM2-135M-Instruct and LFM2.5-350M, and also ran EuroLLM-1.7B-Instruct and LFM2.5-230M. The numbers below were parsed from the run logs. Where a committed journal exists, the README uses the journal values. Small differences between the log and the journal are possible.

## Summary

| Model | Trials | Viable (KL below 0.02) | Result | Recommendation |
| :--- | ---: | ---: | :--- | :--- |
| HuggingFaceTB/SmolLM2-135M-Instruct | 150 | 67/150 | Several trials beat the 10/100 baseline with low KL | Upload trial 135 or 68 |
| LiquidAI/LFM2.5-350M | 150 | 58/150 | The low-KL trials had about 89/100 refusals | Not viable for the current target |
| utter-project/EuroLLM-1.7B-Instruct | 200 | see the report | Trial 154: 2/100 refusals, KL 0.0083 | Preferred candidate |
| LiquidAI/LFM2.5-230M | 200, 150, and 200 | see the README | Best: 8/100 refusals, KL 0.0388 | Better than the v1.4.0 baseline |

## Environment

- Rented Linux VM with two Tesla T4 GPUs
- Heretic v2.0.0.dev0 from `git+https://github.com/p-e-w/heretic.git`
- PyTorch 2.6.0+cu124, transformers 5.22.0, peft 0.21.2, huggingface-hub 1.33.0, datasets 5.1.0
- The first runs went in parallel and fought over the GPUs. I killed them and restarted one at a time.
- The Hugging Face token came from the environment and is not in this repo.

## Constraints

| Constraint | Rationale |
| :--- | :--- |
| KL below 0.02 | Disqualified above this; the model is too damaged for the intended use |
| KL below 0.005 | Preferred; minimal damage |
| KL 0.005 to 0.02 | Acceptable if the refusal reduction justifies it |

## SmolLM2-135M-Instruct

Baseline: about 10/100 refusals.
Total trials: 150.
Viable (KL below 0.02): 67.

### KL below 0.005

| Trial | KL | Refusals | Notes |
| :--- | ---: | ---: | :--- |
| 135 | 0.000600 | 9/100 | Best overall; beats the baseline by one refusal with negligible KL |
| 68 | 0.001100 | 9/100 | Beats the baseline with very low KL |
| 55, 76, 77, 84, 85, 89, 94, 96, 97, 101, 121, 137, 138, 142, 144, 148 | 0.000000 | 10/100 | Baseline refusals, negligible KL |
| 86, 87, 91, 92, 95, 98, 99, 102, 103, 104, 105, 106, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 139, 140, 141, 143, 147, 149, 150 | 0.000100 | 10/100 | Baseline refusals, negligible KL |

### KL 0.005 to 0.02

| Trial | KL | Refusals | Notes |
| :--- | ---: | ---: | :--- |
| 38 | 0.012400 | 4/100 | 60% fewer refusals |
| 70 | 0.017400 | 4/100 | 60% fewer refusals |
| 75 | 0.005000 | 5/100 | At the threshold, 50% fewer refusals |
| 65 | 0.009300 | 5/100 | 50% fewer refusals |
| 88 | 0.010500 | 5/100 | 50% fewer refusals |
| 145 | 0.011600 | 5/100 | 50% fewer refusals |
| 82 | 0.013600 | 5/100 | 50% fewer refusals |
| 69 | 0.014700 | 5/100 | 50% fewer refusals |
| 146 | 0.015700 | 5/100 | 50% fewer refusals |
| 134 | 0.016200 | 5/100 | 50% fewer refusals |
| 23 | 0.016300 | 5/100 | 50% fewer refusals |
| 44 | 0.006800 | 6/100 | 40% fewer refusals |
| 78 | 0.007300 | 6/100 | 40% fewer refusals |
| 79 | 0.008200 | 6/100 | 40% fewer refusals |
| 56 | 0.010000 | 6/100 | 40% fewer refusals |
| 67 | 0.010000 | 6/100 | 40% fewer refusals |
| 90 | 0.010000 | 6/100 | 40% fewer refusals |
| 93 | 0.010000 | 6/100 | 40% fewer refusals |
| 100 | 0.010000 | 6/100 | 40% fewer refusals |
| 81 | 0.011000 | 6/100 | 40% fewer refusals |
| 136 | 0.011600 | 6/100 | 40% fewer refusals |
| 31 | 0.013700 | 6/100 | 40% fewer refusals |
| 107 | 0.014000 | 6/100 | 40% fewer refusals |
| 83 | 0.014300 | 6/100 | 40% fewer refusals |
| 80 | 0.014400 | 6/100 | 40% fewer refusals |
| 26 | 0.015800 | 6/100 | 40% fewer refusals |

## LFM2.5-350M

Model: LiquidAI/LFM2.5-350M.
Total trials: 150.
Viable (KL below 0.02): 58.

All of the viable trials had about 89/100 refusals, far above the target of under 10/100. The trials that did get under 10/100 refusals had KL around 0.08 or higher. No candidate met both goals.

## EuroLLM-1.7B-Instruct

The base model had 4/100 refusals. Trial 154 reached 2/100 at KL 0.0083. Trial 174 had lower KL (0.0068) but 3/100 refusals. See `23_eurollm_trial154_trial174.md` and `25_heretic_v2_indepth_testing_report.md` for the full table.

## LFM2.5-230M

Three seeds were tried. The best result against the v1.4.0 baseline (10/100 refusals, KL 0.0548) came from `heretic-runs3` (seed 2950566656), trial 83: 8/100 refusals at KL 0.0388. The other seeds found different tradeoffs. See the README.

## Recommendations

### SmolLM2-135M-Instruct

1. For minimal damage, export trial 135 (KL 0.0006, 9/100) or trial 68 (KL 0.0011, 9/100). Both beat the 10/100 baseline with almost no KL.
2. If a larger refusal cut matters more, trial 38 (KL 0.0124, 4/100) or trial 70 (KL 0.0174, 4/100) sits in the acceptable band.
3. The KL near zero trials at 10/100 keep baseline behaviour with no measured damage. Trial 55 is one example.

### LFM2.5-350M

No candidate met the current target. I did not upload one.

## Artifacts

- Parsed results: `docs/21_v2_results_parsed.md`, `docs/22_all_findings_comprehensive.md`
- Parsing helper: `analyze_journal.py`
- Journals: `vm-runs/` and `vm-data-final/`
- Run logs were not committed.

## Headless runs

The runs finished optimization and then stopped at the trial prompt. They had been started without `--trial-index`, so Heretic asked for a trial, and the prompt raised `EOFError` with no TTY. The trial data was already in the journals. To save or upload from a finished run, pass the full flag set listed in the README.
