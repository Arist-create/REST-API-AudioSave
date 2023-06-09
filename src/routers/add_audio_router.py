
import http
from fastapi import File, UploadFile, APIRouter, Depends
from src.controllers.add_audio_ctrl import add_audio_ctrl
from src.schemas.audio_schemas.add_audio_response_model import AddAudioResponseModel
from src.database.main import get_db
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter()


@router.post(
    "/api/add_audio",
    response_model=AddAudioResponseModel,
    summary="Добавить аудиозапись",
    status_code=http.HTTPStatus.CREATED,
    tags=["Аудиозапись"]
)
async def add_audio_router(user_id: str, token: str, file: UploadFile = File(), db: AsyncSession = Depends(get_db)) -> AddAudioResponseModel:
    return await add_audio_ctrl(db, user_id, token, file)
