# Dependency resolution

## What went wrong

1. The first install used torch 2.5.1 with transformers 5.22.0 and hit conflicts.
2. transformers 5.22.0 did not work with torch 2.5.1 and failed on import (`nn` undefined in `pipeline_parallel`).
3. Dropping to transformers 4.54.1 and peft 0.16.0 fixed the import, but that combination no longer matched Heretic v2.
4. huggingface-hub had to be held below 1.0 for that stack.

## Versions that worked for the older stack

- torch 2.5.1+cu121
- transformers 4.54.1
- peft 0.16.0
- huggingface-hub 0.36.2
- accelerate, datasets, and lm-eval from Heretic's dependencies

These versions were not enough for Heretic v2. `06_fresh_setup.md` and `09_final_working_env.md` cover the stack that actually ran.
