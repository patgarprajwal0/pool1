# Simple Flask App (for CI/CD demo)

This repository contains a minimal Flask app with pytest tests. It is intended to run CI on a self-hosted Azure DevOps agent (pool `pool1`) using system Python 3.11.4.

Run locally:
1. python -m venv .venv
2. .venv\Scripts\activate   (Windows) or source .venv/bin/activate (Linux/macOS)
3. pip install -r requirements.txt
4. pytest -q

