import http
from fastapi import APIRouter
from src.controllers.create_user_ctrl import create_user_ctrl
from src.schemas.user_schemas.create_user_response_model import CreateUserResponseModel
from fastapi import Depends
from src.database.main import get_db
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter()


@router.post(
    "/api/create_user",
    response_model=CreateUserResponseModel,
    summary="Создать пользователя",
    status_code=http.HTTPStatus.CREATED,
    tags=["Пользователь"]
)
async def create_user_router(name: str, db: AsyncSession = Depends(get_db)) -> CreateUserResponseModel:
    return await create_user_ctrl(db, name)
