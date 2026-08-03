# hello-fastapi

A FastAPI HTTP service project managed with [uv](https://docs.astral.sh/uv/),
with linting, formatting, static type checking, tests, and Docker build scripts
built in.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Docker (optional, for container builds)

## Getting started

```bash
uv sync                                   # install dependencies into .venv
uv run uvicorn app.main:app --reload      # start dev server at http://localhost:8000
```

Or copy `.env.example` to `.env` and adjust settings as needed.

## Development

```bash
uv run ruff check .        # lint
uv run ruff format .       # format
uv run basedpyright        # static type check
uv run pytest              # tests with coverage
./scripts/dev.sh           # dev server with auto-reload
```

Add a formatter check to CI/pre-commit with:

```bash
uv run ruff format --check .
```

## Docker

```bash
./scripts/docker-build.sh   # build the image
./scripts/docker-run.sh     # build and run via docker compose
```

The container listens on port `8000` and exposes a health check at
`/api/v1/health`.

## Project layout

```text
app/
├── api/          # API routers
├── config.py     # pydantic-settings based configuration
└── main.py       # FastAPI app
tests/            # pytest suite
scripts/          # dev / docker helper scripts
```
