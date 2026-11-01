# Headless run notes

This file started as an issue report about an `EOFError` after optimization. That report was wrong, and the details are kept here so the mistake is not repeated.

## What happened

Several runs stopped after optimization with an `EOFError` from prompt_toolkit. The runs had been started without `--trial-index` or `--model-action`, so Heretic asked for a trial and an action. With no TTY, that prompt fails.

## What the journals show

Every run that hit the error stored `trial_index=null` and `model_action=null` in its settings. The prompt was the trial-selection prompt, which is the intended behaviour when the flag is unset.

## What works

Set the flags listed in the README. For a save, set `--trial-index`, `--model-action save`, `--save-directory`, and `--export-strategy`. For upload, also set the upload flags and `HF_TOKEN`.

Heretic does not need a TTY check for this. A missing flag is the cause.
