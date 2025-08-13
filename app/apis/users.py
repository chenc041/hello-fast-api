from fastapi import APIRouter
from app.logger import setup_logger

logger = setup_logger(__name__)
router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get("/")
async def get_users():
    logger.info("get_users")
    logger.error("get_users error")
    return [{"name": "John Doe"}, {"name": "Jane Doe"}]
