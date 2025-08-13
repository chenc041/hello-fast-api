from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager
from app.apis import users
from app.config import settings
from app.db import create_db_and_tables
from app.deps import get_token_header

@asynccontextmanager
async def lifespan(fastapi: FastAPI):
    create_db_and_tables()
    yield
app = FastAPI(
    lifespan=lifespan,
    title=settings.APP_NAME,
    dependencies=[Depends(get_token_header)],
)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
