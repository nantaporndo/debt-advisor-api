FROM python:3.12-slim

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.11.7 /uv /usr/local/bin/uv

ENV UV_COMPILE_BYTECODE=1

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .

ARG GIT_SHA=dev
ENV APP_VERSION=$GIT_SHA

RUN useradd --system --no-create-home app
USER app

EXPOSE 8000
CMD exec .venv/bin/uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}