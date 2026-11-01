# Testing Heretic v2.0.0.dev0

## Summary

I tested Heretic v2.0.0.dev0 on four models from [saidutta69/racer-is-op-heretic-models](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models). The main run used `utter-project/EuroLLM-1.7B-Instruct` with 200 trials and seed 42. It produced candidates under 10/100 refusals with low KL.

## Environment

- Rented Linux VM with two Tesla T4 GPUs (CUDA 12.8, driver 580.178.04)
- Heretic v2.0.0.dev0 from git
- PyTorch 2.11.0+cu128, transformers 5.22.0, peft 0.21.2, torchao 0.16.0
- Hugging Face token from the environment
- v1.4.0 baseline: `saidutta69/LFM2.5-230M-heretic`, KL 0.0548 and 10/100 refusals

## Constraints

- KL below 0.02 is a hard cap. Anything higher is considered damaged beyond acceptable use.
- KL below 0.005 is ideal.
- KL 0.005 to 0.02 is acceptable if the refusal reduction justifies it.
- Target: under 10/100 refusals with minimal KL.

## Results

### EuroLLM-1.7B-Instruct

Base model: 4/100 refusals. From the 200-trial run:

| Trial | KL | Refusals | Parameters | Notes |
| :--- | ---: | ---: | :--- | :--- |
| 153 | 0.0119 | 3/100 | 4/24/0.8638/0.0001/0.4262/1 | Small reduction from the baseline |
| 154 | 0.0083 | 2/100 | 4/24/0.9244/0.0001/0.2522/1 | Best tradeoff; half the baseline refusals, KL under 0.01 |
| 174 | 0.0068 | 3/100 | 4/24/0.9185/0.0001/0.2693/1 | Lower KL, one more refusal than trial 154 |
| 170 | 0.1939 | 0/100 | | No refusals but high KL |

Trial 154 was the pick for upload. A local patch that took the first Pareto trial chose trial 170, which was the wrong end of the front. That is why I did not keep the auto-selection patch.

These numbers come from the run log. The 200-trial journal is not in this repo.

### SmolLM2-135M-Instruct

150 trials. Baseline: about 10/100 refusals.

| Trial | KL | Refusals | Notes |
| :--- | ---: | ---: | :--- |
| 135 | 0.0006 | 9/100 | Beats the baseline by one refusal with negligible KL |
| 68 | 0.0011 | 9/100 | Beats the baseline with very low KL |
| 38 | 0.0124 | 4/100 | 60% fewer refusals |
| 70 | 0.0174 | 4/100 | 60% fewer refusals |

67 of 150 trials had KL below 0.02. Viable for upload.

### LFM2.5-350M

58 of 150 trials had KL below 0.02, but all of them had about 89/100 refusals, far above the target. The trials under 10/100 refusals had KL around 0.08 or higher. Not viable under the current constraints.

### LFM2.5-230M

The best result against the v1.4.0 baseline came from `heretic-runs3` (seed 2950566656), trial 83: 8/100 refusals at KL 0.0388. The other seeds found different tradeoffs. The full numbers are in the README and `22_all_findings_comprehensive.md`.

## Headless runs

Heretic prompts after optimization unless you set the flags. The runs in this repo were started without `--trial-index`, so they stopped at the trial prompt with an `EOFError` when no TTY was available. The trial data was already saved.

For a headless save, set `--trial-index`, `--model-action save`, `--save-directory`, and `--export-strategy`. For upload, also set `--upload-repo-id`, `--upload-repo-private`, and `--upload-reproducibility-information`, and provide `HF_TOKEN`. See the README for the exact commands.

## Artifacts

### Local

- Docs: `docs/21_v2_results_parsed.md`, `docs/22_all_findings_comprehensive.md`, `docs/23_eurollm_trial154_trial174.md`, `docs/24_vm_shutdown_data.md`
- Parser: `analyze_journal.py`
- Journals: `vm-runs/`, `vm-data-final/`

### VM (now stopped)

- Checkpoints: `/root/heretic-runs/utter-project--EuroLLM-1--7B-Instruct.jsonl`, `/root/v2-tests/*/checkpoints/*`
- Logs: `/root/heretic_euro.log`, `/root/heretic_upload_154.log`, and others. These were not committed.
- Saved model: `/root/euro-outputs/euro-heretic/` (trial 170 only)

### Hugging Face

- Collection: [saidutta69/racer-is-op-heretic-models](https://huggingface.co/collections/saidutta69/racer-is-op-heretic-models)
- Existing: [saidutta69/LFM2.5-230M-heretic](https://huggingface.co/saidutta69/LFM2.5-230M-heretic), [saidutta69/EuroLLM-9B-Instruct-heretic](https://huggingface.co/saidutta69/EuroLLM-9B-Instruct-heretic)
- Target that was not created: `saidutta69/EuroLLM-1.7B-Instruct-heretic` (trial 154)

## Recommendations

- SmolLM2-135M-Instruct: upload trial 135 (KL 0.0006, 9/100) for minimal damage, or trial 38 (KL 0.0124, 4/100) if fewer refusals matter more.
- LFM2.5-350M: not viable under the current constraints.
- EuroLLM-1.7B-Instruct: upload trial 154 (2/100 refusals, KL 0.0083). Avoid trial 170 despite 0/100 refusals because KL is 0.1939.
- LFM2.5-230M: `heretic-runs3` trial 83 (8/100 refusals, KL 0.0388) beats the v1.4.0 baseline on both metrics.

## Reproduction

```bash
heretic --model utter-project/EuroLLM-1.7B-Instruct --seed 42 --n-trials 200
```

Add the headless flags from the README if you want the run to save or upload without a prompt. The 200-trial EuroLLM journal is not in this repo.
