# v2 results for SmolLM2 and LFM2.5-350M

The numbers below come from parsing the run logs and journals. The runs finished optimization and then stopped at the trial prompt because no trial flag was set. All trial data was already saved.

## SmolLM2-135M-Instruct

150 trials. 67 had KL below 0.02.

### KL below 0.005

| Trial | KL | Refusals | Notes |
| :--- | ---: | ---: | :--- |
| 135 | 0.000600 | 9/100 | Beats the 10/100 baseline with minimal KL |
| 68 | 0.001100 | 9/100 | Beats the baseline with low KL |
| 55, 76, 77, 84, 85, 89, 94, 96, 97, 101, 121, 137, 138, 142, 144, 148 | 0.000000 | 10/100 | Baseline refusals, negligible KL |

### KL 0.005 to 0.02

| Trial | KL | Refusals | Notes |
| :--- | ---: | ---: | :--- |
| 38 | 0.012400 | 4/100 | 60% fewer refusals |
| 70 | 0.017400 | 4/100 | Similar tradeoff |
| 75 | 0.005000 | 5/100 | Just at the threshold |
| 65 | 0.009300 | 5/100 | Good reduction |
| 88 | 0.010500 | 5/100 | Good reduction |
| 145 | 0.011600 | 5/100 | Good reduction |
| 82 | 0.013600 | 5/100 | Good reduction |
| 69 | 0.014700 | 5/100 | Good reduction |

The published v1.4.0 model had about 10/100 refusals. Several v2 trials beat that with KL below 0.005.

## LFM2.5-350M

150 trials. 58 had KL below 0.02. All of those had about 89/100 refusals. The trials under 10/100 refusals had KL near 0.08 or higher. Not viable for the current target.

## Recommendation

For SmolLM2-135M, start with trial 135 (KL 0.0006, 9/100) or trial 68 (KL 0.0011, 9/100). If a larger refusal cut matters more, trial 38 or 70 gives 4/100 at KL 0.012 to 0.017.
