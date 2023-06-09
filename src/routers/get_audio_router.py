import http
from fastapi import APIRouter
from src.controllers.get_audio_ctrl import get_audio_ctrl
from fastapi import Depends
from src.database.main import get_db
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter()


@router.get(
    "/api/record",
    summary="Получить аудиозапись",
    status_code=http.HTTPStatus.CREATED,
    tags=["Аудиозапись"]
)
async def get_audio_router(record_id: str, user_id: str, db: AsyncSession = Depends(get_db)):
    return await get_audio_ctrl(db, user_id, record_id)
