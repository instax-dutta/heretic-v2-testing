# EuroLLM-1.7B-Instruct: trials 154 and 174

From the 200-trial run (seed 42) on `utter-project/EuroLLM-1.7B-Instruct`. The base model had 4/100 refusals.

- Trial 153: 3/100 refusals, KL 0.0119. Parameters: start 4, end 24, preserve_good 0.8638, steer_bad 0.0001, overcorrect 0.4262, neighbor 1.
- Trial 154: 2/100 refusals, KL 0.0083. Parameters: start 4, end 24, preserve_good 0.9244, steer_bad 0.0001, overcorrect 0.2522, neighbor 1. Best tradeoff.
- Trial 174: 3/100 refusals, KL 0.0068. Parameters: start 4, end 24, preserve_good 0.9185, steer_bad 0.0001, overcorrect 0.2693, neighbor 1.
- Trial 170: 0/100 refusals, KL 0.1939. High KL, not preferred.

The intended upload was trial 154 to `saidutta69/EuroLLM-1.7B-Instruct-heretic`. It was not uploaded.

These numbers come from the run log. The 200-trial journal is not in this repo; the journal under `vm-data-final/` is a different, shorter run.
