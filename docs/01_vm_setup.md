# VM setup

## Access

The work ran on a rented Linux VM with two Tesla T4 GPUs (CUDA 13.0 driver, 580.178.04). I reached it through a local SSH tunnel. Access details are not stored in this repo.

## Base packages

Installed python3-venv, python3-pip, git-lfs, and python3.11-venv. Created a Python 3.11 virtual environment at `/root/heretic-env`.

## PyTorch

Installed PyTorch 2.5.1+cu121 first. Later runs used other CUDA builds, noted in the run logs.

## Hugging Face

Authenticated with `HF_TOKEN` from the environment. The token is not in this repo.
