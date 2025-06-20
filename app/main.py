from fastapi import Depends, FastAPI

from app.apis import users
from app.config import settings
from app.deps import get_token_header

app = FastAPI(
    title=settings.APP_NAME,
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found"}}
)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
