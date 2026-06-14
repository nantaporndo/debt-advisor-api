# Debt Advisor API — Roadmap

## Phase 1 — Foundation (Do First)
- [x] Fix typo in `app/core/config.py` (`fuctools` → `functools`)
- [ ] Update `Settings` with real env vars (`DATABASE_URL`, `ANTHROPIC_API_KEY`, `SUPABASE_URL`, `SUPABASE_KEY`)
- [ ] Connect Supabase Postgres via SQLModel
- [ ] Run Alembic migrations for `User`, `Debt`, `Payment`, `Conversation`, `Message` tables
- [ ] Mount `app/api/router.py` in `main.py`

## Phase 2 — Core API
- [ ] `POST /debts` — create a debt
- [ ] `GET /debts` — list user's debts
- [ ] `GET /debts/{id}` — get single debt
- [ ] `PATCH /debts/{id}` — update debt
- [ ] `DELETE /debts/{id}` — delete debt
- [ ] `POST /payments` — record a payment
- [ ] `GET /debts/{id}/payments` — payment history per debt

## Phase 3 — Authentication
- [ ] Supabase JWT middleware to protect all routes
- [ ] Extract `user_id` from token and scope all queries to that user
- [ ] `GET /me` — return current user info

## Phase 4 — AI Advisor (Core Feature)
- [ ] `POST /chat` — send message to Claude with user's debt snapshot as context
- [ ] `GET /chat/{conversation_id}` — fetch conversation history
- [ ] Persist conversations and messages to DB
- [ ] Generate `suggestions` in `ChatResponse` (e.g. "Try avalanche method", "Refinance your auto loan")

## Phase 5 — Insights & Polish
- [ ] `GET /summary` — total debt, highest-interest debt, estimated payoff months
- [ ] Payoff calculator (avalanche vs snowball strategy comparison)
- [ ] Input validation error handling + consistent error responses
- [ ] Rate limiting on `/chat` endpoint

## Phase 6 — Production Readiness
- [x] CI/CD pipeline (GitHub Actions → Cloud Run)
- [ ] Structured logging
- [ ] Cloud Run secrets for all sensitive env vars
- [ ] API versioning (`/v1/...`)
