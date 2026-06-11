# debt-advisor-api

FastAPI backend for the Debt Advisor app.

## Running locally

```bash
uv run uvicorn main:app --reload
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
