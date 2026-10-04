# ===================================================
# Stage 1: Build dependencies & project using uv
# ===================================================
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

# Compile bytecode for faster startup & set copy mode
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Install dependencies first (layer-cached if lockfile unchanged)
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Copy application files
COPY . /app

# Install the project itself into the virtual environment
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# ===================================================
# Stage 2: Minimal runtime image
# ===================================================
FROM python:3.12-slim-bookworm AS runtime

WORKDIR /app

# Create a non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser -d /app appuser

# Copy virtual environment and application from builder
COPY --from=builder --chown=appuser:appuser /app /app

# Ensure executables in .venv take precedence
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Run as non-root user
USER appuser

# Expose default port
EXPOSE 8000

# Run FastAPI in production mode
CMD ["fastapi", "run", "src/fastapi_experiment/main.py", "--host", "0.0.0.0", "--port", "8000"]
