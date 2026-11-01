# Second run

Started a fresh run with `--n-trials 200` to search more of the parameter space. The goal was still 0/100 refusals with KL below 0.005. Log: `run2_20261030_024622.log` (not committed).

## Progress

- Trial 3: 0/100 refusals, KL 3.35.
- Trial 40: 15/100 refusals, KL 0.0631.
- Trial 41: 3/100 refusals, KL 0.4269.
- Trial 55: 93/100 refusals, KL 0.0189.
- Trial 85: 94/100 refusals, KL 0.0075.
- Trial 98: 95/100 refusals, KL 0.0027.
- Trial 100: 93/100 refusals, KL 0.0032.

The tradeoff stayed tight. Low KL usually came with many refusals. The committed 200-trial journals for seed 277295262 are identical, so only one copy counts.
