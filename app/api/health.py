"""Health-check endpoints."""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    """Response body for the health check."""

    status: Literal["ok"] = "ok"


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return a liveness response for probes."""
    return HealthResponse()
