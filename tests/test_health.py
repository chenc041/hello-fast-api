"""Tests for the HTTP API."""

from fastapi.testclient import TestClient

from app.main import app


def test_health_check() -> None:
    """GET /api/v1/health returns 200 with an ok status."""
    with TestClient(app) as client:
        response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
