# Python UV FastAPI

A minimal FastAPI project managed with [uv](https://docs.astral.sh/uv/).

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed
- Python >= 3.12

## Installation

Install project dependencies and set up the virtual environment:

```bash
uv sync
```

## Running the Project

### 1. Local Development

Run the FastAPI application with live auto-reload enabled:

```bash
uv run fastapi dev src/fastapi_experiment/main.py
```

- API Server: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

_(Optional) Run the CLI script:_

```bash
uv run python-uv
```

### 2. Production

Run the FastAPI application in production mode:

```bash
uv run fastapi run src/fastapi_experiment/main.py
```
