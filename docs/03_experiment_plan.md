# Experiment plan

Goal: reduce refusals on LiquidAI/LFM2.5-230M to 0/100 with the smallest possible KL divergence.

Heretic v2.0.0.dev0 runs an Optuna search over ablation parameters. Each trial is scored on refusal rate and KL divergence. The plan was to keep the defaults where they made sense and record the parameters Optuna chose.
