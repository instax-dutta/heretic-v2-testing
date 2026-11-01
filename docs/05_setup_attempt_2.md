# Setup attempt 2

Tried the one-liner install suggested by the user:

```
apt-get update && apt-get install -y --no-install-recommends build-essential && \
pip uninstall -y torchaudio torchao heretic heretic-llm && \
pip install -U torch torchvision transformers accelerate datasets bitsandbytes peft safetensors sentencepiece protobuf huggingface_hub && \
pip uninstall -y torchaudio torchao && \
pip install -U "git+https://github.com/p-e-w/heretic.git" && \
hf auth login && hf auth whoami
```

The existing environment already had broken dependencies, so the install did not fix it. Recreating the venv in the right order worked better.
