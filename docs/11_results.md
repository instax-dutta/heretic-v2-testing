# Results: LiquidAI/LFM2.5-230M

## Run summary

- Model: LiquidAI/LFM2.5-230M
- Tool: Heretic v2.0.0.dev0 from git
- Environment: PyTorch 2.6.0+cu124, transformers 5.22.0, peft 0.21.2, huggingface-hub 1.33.0
- Hardware: two Tesla T4 GPUs on a VM
- Trials: 100 in the first run log. The committed journal for the same seed has 200.
- Log: `run_20261030_021140.log` (not committed)

## What happened

The first run finished its trials and produced a Pareto front. Some trials reached 0/100 refusals with high KL: trial 6 at KL 1.4645 and trial 2 at KL 2.6094. Others reached low KL with a few refusals.

After optimization, Heretic showed the trial menu. The run had been started without `--trial-index`, so the menu appeared as designed. With no TTY, the prompt raised `EOFError`. The trial data was already in the journal, so nothing was lost.

## Notes

Saving or uploading from that run needed either an interactive session or the post-optimization flags. See the headless section in the README.
