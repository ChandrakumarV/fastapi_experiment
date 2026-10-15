# FastAPI Experiment

A minimal FastAPI project managed with [uv](https://docs.astral.sh/uv/).

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed
- Python >= 3.12
- Docker (optional, for containerization)

## Installation

Install project dependencies and set up the virtual environment:

```bash
uv sync
```

## Running the Project

### 1. Local Development

Run the FastAPI application with live auto-reload enabled:

```bash
uv run fastapi dev
```

or

```bash
uv run fastapi dev src/fastapi_experiment/main.py
```

- API Server: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

_(Optional) Run the CLI script:_

```bash
uv run fastapi-experiment
```

### 2. Production (Direct)

Run the FastAPI application in production mode:

```bash
uv run fastapi run src/fastapi_experiment/main.py
```

### 3. Docker (Multi-stage)

Build the Docker image:

```bash
docker build -t fastapi-experiment .
```

Run the container:

```bash
docker run -p 8000:8000 --name fastapi-app fastapi-experiment
```

### 4. Deploy to FastAPI Cloud

```bash
uv run fastapi deploy
```
