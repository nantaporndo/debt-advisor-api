![CI/CD](https://github.com/nantaporndo/debt-advisor-api/actions/workflows/ci-cd.yml/badge.svg?branch=develop)

## CI/CD
PR → develop: `ci` (ruff, pytest, docker build) — required to merge
merge → develop: `ci` → `deploy` (WIF auth → build image tagged with SHA → Cloud Run) → smoke test (`/health` version == SHA)
Secrets: GCP Secret Manager, mounted as env by Cloud Run

# debt-advisor-api

FastAPI backend for the Debt Advisor app.

## Running locally

```bash
uv run uvicorn app.main:app --reload
```

API will be available at http://localhost:8000.

## Running with Docker

All commands below should be run from this directory (`debt-advisor-api/`).

### Development (with hot reload)

```bash
docker compose -f docker-compose.dev.yml up --build
```

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| API | http://localhost:8000 |

File changes in `debt-advisor/` and `debt-advisor-api/` are reflected immediately without rebuilding.

### Production

```bash
docker compose up --build
```

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| API | http://localhost:8000 |

### Useful commands

```bash
# Stop all services
docker compose down

# Rebuild a single service
docker compose -f docker-compose.dev.yml up --build web

# View logs
docker compose logs -f
```
