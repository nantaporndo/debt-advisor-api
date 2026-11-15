#!/usr/bin/env bash
set -euo pipefail
PROJECT=debt-management-api

gcloud auth print-access-token >/dev/null 2>&1 \
  || { echo "Not logged in: run 'gcloud auth login --no-launch-browser'"; exit 1; }

get() {
  echo "  fetching $1..." >&2
  timeout 30 gcloud secrets versions access latest --secret="$1" --project="$PROJECT" \
    || { echo "failed: $1" >&2; exit 1; }
}

umask 077
{
  echo "DATABASE_URL=$(get database-url)"
  echo "SUPABASE_URL=https://sqmqmztwkgdiwzbrvbwo.supabase.co"
  echo "SUPABASE_SERVICE_ROLE_KEY=$(get supabase-service-role-key)"
  echo "ANTHROPIC_API_KEY=$(get anthropic-api-key)"
} > .env.tmp && mv .env.tmp .env
echo ".env written"