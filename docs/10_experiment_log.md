# Experiment log: LiquidAI/LFM2.5-230M

Early notes from the first run. Trial numbers and scores here came from the live log and may not match the committed journal. The final summary is in `25_heretic_v2_indepth_testing_report.md`.

## Run started

- Time: 2026-10-29 21:11:40 UTC
- Log: `run_20261030_021140.log`
- Command: `heretic --model LiquidAI/LFM2.5-230M`
- Environment: PyTorch 2.6.0+cu124, transformers 5.22.0, peft 0.21.2, huggingface-hub 1.33.0

## Trials

Trial 1: start_layer 1, end_layer 24, preserve_good 1.0, steer_bad 1.0, overcorrect 1.0, neighbor 1. Refusals 0/100, KL 79.1712.

Trial 2: start_layer 9, end_layer 14, preserve_good 1.5402, steer_bad 0.4305, overcorrect 0.7040, neighbor 7. Refusals 0/100, KL 2.6094.

Trial 3: start_layer 11, end_layer 18, preserve_good 1.3800, steer_bad 0.0177, overcorrect 0.9060, neighbor 9. Refusals 0/100, KL 17.1939.

Trial 4: start_layer 12, end_layer 17, preserve_good 1.0754, steer_bad 0.0021, overcorrect 0.8943, neighbor 12. Refusals 0/100, KL 14.1649.

Trial 5: start_layer 4, end_layer 15, preserve_good 0.8533, steer_bad 0.2782, overcorrect 0.5303, neighbor 1. Refusals 0/100, KL 2.1968.

Trial 6: start_layer 3, end_layer 15, preserve_good 0.7063, steer_bad 0.0367, overcorrect 0.6893, neighbor 2. Refusals 0/100, KL 1.4645.

Trial 7: start_layer 1, end_layer 23, preserve_good 0.7735, steer_bad 0.0424, overcorrect 0.6589, neighbor 6. Refusals 0/100, KL 16.7135.

Trial 8: start_layer 2, end_layer 9, preserve_good 0.4326, steer_bad 0.0012, overcorrect 0.9838, neighbor 6. Refusals 2/100, KL 0.4791.

Trial 9: start_layer 7, end_layer 12, preserve_good 0.9666, steer_bad 0.0005, overcorrect 1.2836, neighbor 13. Refusals 0/100, KL 13.7595.

Trial 10: start_layer 2, end_layer 8, preserve_good 0.3931, steer_bad 0.0002, overcorrect 0.7807, neighbor 6. Refusals 95/100, KL 0.0000.

Trial 11: start_layer 5, end_layer 9, preserve_good 0.6259, steer_bad 0.0020, overcorrect 1.0856, neighbor 11. Refusals 72/100, KL 15.0697.

Trial 12 was still running when these notes were taken. Parameters: start_layer 2, end_layer 9, preserve_good 0.5438, steer_bad 0.1963, overcorrect 1.1550, neighbor 3.

## Updates

At about trial 25 the search was still exploring. Some trials reached 0/100 refusals with high KL. Trial 6 had 0/100 at KL 1.4645, trial 5 had 0/100 at KL 2.1968, and trial 2 had 0/100 at KL 2.6094.

Around trial 40 there were trials with KL near 0.13 to 0.21 and 4 to 8 refusals.

The last notes said the search was still running and the KL values varied.

## Notes

LFM2.5-230M is small (230M parameters) and ran quickly on a T4. Heretic v2.0 with ARA (Arbitrary-Rank Ablation) was used.
