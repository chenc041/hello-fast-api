from fastapi import Depends, FastAPI

from app.config import settings
from app.dependencies import get_token_header
from app.routers import users

print("settings", settings)

app = FastAPI(
    title=settings.APP_NAME,
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found"}}
)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
