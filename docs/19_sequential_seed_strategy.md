# Running seeds in sequence

The two GPUs were used one run at a time to avoid contention. Each model got two or three seeds so the search would not depend on one path. The goal was under 10 refusals with minimal KL, and a result better than the published v1.4.0 model.

## Plan

1. Try two or three seeds per model (for example 42, 12345, 777) with 100 trials each.
2. If time was short, run 150 trials with one seed.
3. After each run, parse the journal for the best trial that met the criteria.
4. If a trial beat the published model, save and upload it with the full metadata.
