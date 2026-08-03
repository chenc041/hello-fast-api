"""Tests for the HTTP API."""

from datetime import UTC, datetime, timedelta

from fastapi.testclient import TestClient

from app.main import app


def test_health_check() -> None:
    """GET /api/v1/health returns 200 with an ok status."""
    with TestClient(app) as client:
        response = client.get("/api/v1/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"

    reported_at = datetime.fromisoformat(body["time"])
    assert reported_at.tzinfo is not None
    assert abs(datetime.now(UTC) - reported_at) < timedelta(minutes=1)
