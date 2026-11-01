# Compatibility notes

Heretic v2.0 from git expects transformers[kernels]~=5.18, peft~=0.21, huggingface-hub~=1.33, and datasets~=5.0.

transformers 5.x needs huggingface-hub 1.x and did not work well with torch 2.5.1. The CUDA 13.0 driver ran cu121 wheels without trouble, so the driver was not the blocker. The problem was the Python package versions.

The final working set is in `09_final_working_env.md`.
