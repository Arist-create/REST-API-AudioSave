
from fastapi.responses import JSONResponse, FileResponse
from src.database.methods.get_audio_db import get_audio_db
from sqlalchemy.ext.asyncio import AsyncSession




async def get_audio_ctrl(db: AsyncSession, user_id: str, record_id: str) -> JSONResponse | FileResponse:
    response = await get_audio_db(db, user_id, record_id)
    if response != True:
        return JSONResponse(status_code=400, content={"NotFoundError": 'wrong data'})
    headers = {'Content-Disposition': f'attachment; filename="{record_id}.mp3"'}
    return FileResponse(status_code=201, path=f'records/{record_id}.mp3', media_type="audio/mp3", headers=headers)
