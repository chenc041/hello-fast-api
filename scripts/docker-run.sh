#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

docker compose up -d --build

echo "API is running at http://localhost:8000/api/v1/health"
