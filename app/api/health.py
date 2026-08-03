"""Health-check endpoints."""

from datetime import UTC, datetime
from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(tags=["health"])


def _now_iso() -> str:
    """Return the current UTC time as an ISO-8601 string."""
    return datetime.now(UTC).isoformat(timespec="seconds")


class HealthResponse(BaseModel):
    """Response body for the health check."""

    status: Literal["ok"] = "ok"
    time: str = Field(default_factory=_now_iso)


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return a liveness response for probes."""
    return HealthResponse()
