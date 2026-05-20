# Weather Fetch — Robust Fetching, Logging & Error Handling

A small, well-structured Python project that fetches weather data and demonstrates reliable logging, retries, validation, and error handling.

Key goals:
- Clear setup and usage instructions for developers
- Reproducible configuration and environment isolation
- Structured logging and resilient network handling

## Features
- Fetch current weather data from an external API with retries and backoff
- Config-driven behavior via `src/config.py`
- Centralized logging in `src/logger.py`
- Input validation in `src/validator.py`
- Clean client encapsulation in `src/weather_client.py`
- Simple runner in `src/main.py`

## Repository Structure

- [src](src)
	- [config.py](src/config.py) — configuration and constants
	- [logger.py](src/logger.py) — logging setup and helpers
	- [validator.py](src/validator.py) — input validation utilities
	- [weather_client.py](src/weather_client.py) — HTTP client with retries
	- [main.py](src/main.py) — entry point / example usage

## Prerequisites

- Python 3.10+ recommended
- A virtual environment (venv) or similar

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.

```bash
python -m venv .venv
# Windows
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirement.txt
```

## Configuration

Edit configuration values in [src/config.py](src/config.py) or set environment variables (the project reads configuration from `config.py`). Typical settings include API keys, endpoints, timeouts, and retry policy.

Keep secrets out of source control — use environment variables or a secrets manager for API keys.

## Usage

Run the example runner from the project root (inside the activated virtualenv):

```bash
# from project root
python -m src.main
```

Or run directly from `src` during development:

```bash
cd src
py main.py
```

## Logging

The project uses structured, configurable logging via `src/logger.py`. Logs include timestamps and severity levels; configure the handler/level in `logger.py` or via environment variables depending on your needs.

Recommended practice:
- Log at `INFO` for normal operation and `DEBUG` for troubleshooting
- Send `ERROR`/`CRITICAL` logs to alerts if running in production

## Error Handling & Retries

The HTTP client implements retry logic with exponential backoff to handle transient network failures. Non-transient errors are raised after retry exhaustion so callers can decide how to handle them.

Best practices demonstrated:
- Validate inputs early (`validator.py`)
- Retry transient failures with capped backoff (`weather_client.py`)
- Fail fast on invalid configuration

## Testing

Add tests under a `tests/` directory. Example tooling and commands:

```bash
pip install pytest
pytest -q
```

Mock external HTTP calls (e.g., with `responses` or `pytest-httpserver`) to keep tests deterministic.

## Contributing

- Fork the repo and create a feature branch
- Open a clear PR with a description of changes
- Include tests for bug fixes and new features

## License

This project is MIT-licensed. Update this section to match your desired license.

## Contact / Support

For questions or help, open an issue in this repository.

---

If you'd like, I can also:
- add badges (CI, license, coverage)
- add a `requirements.txt`/`pyproject.toml` example
- add a `tests/` scaffold and a couple unit tests

