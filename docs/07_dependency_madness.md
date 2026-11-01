# Dependency attempts

Heretic v2.0 from git pins transformers[kernels]~=5.18, peft~=0.21, huggingface-hub~=1.33, and datasets~=5.0. Those pins do not fit an older torch stack.

Installing newer packages by hand left the environment in a mixed state. The combination that worked is in `09_final_working_env.md`.
