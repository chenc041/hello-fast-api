"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.health import router as health_router
from app.config import get_settings


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""
    settings = get_settings()
    app_instance = FastAPI(title=settings.name, version="0.1.0", debug=settings.debug)

    app_instance.include_router(health_router, prefix=settings.api_prefix)
    return app_instance


app = create_app()


@app.get("/")
def root():
    return {"message": "Hello World"}
