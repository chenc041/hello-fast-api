from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header(..., description="用户认证token")):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
