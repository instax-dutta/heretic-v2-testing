# v2 testing plan

Target: refusals under 10/100 with minimal KL. Start with the smallest models and work up.

Models to test (under 2B):

1. HuggingFaceTB/SmolLM2-135M-Instruct (started)
2. LiquidAI/LFM2.5-350M
3. HuggingFaceTB/SmolLM2-360M-Instruct
4. Qwen/Qwen3.5-0.8B
5. google/gemma-3-1b-it
6. microsoft/RaceBench-MiniCPM5
7. Qwen/Qwen2.5-Coder-1.5B-Instruct
8. Qwen/Qwen3-1.7B
9. deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B

The runs used base models for fresh v2 ablation, so they may not line up with the published fine-tunes.

## Early results

- SmolLM2-135M: trial 6 had 1/100 refusals at KL 1.294. The baseline was 10/100.
- SmolLM2-135M: trial 24 had 3/100 refusals at KL 0.0458.
- SmolLM2-135M: trial 31 had 6/100 refusals at KL 0.0137.
