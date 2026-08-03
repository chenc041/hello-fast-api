#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

exec docker build -t hello-fastapi:latest .
