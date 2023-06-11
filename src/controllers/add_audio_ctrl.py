import uuid
from fastapi.responses import JSONResponse
from pydub import AudioSegment
import os
from src.database.methods.add_audio_db import add_audio_db
from sqlalchemy.ext.asyncio import AsyncSession

async def add_audio_ctrl(db: AsyncSession, user_id: str, token: str, audio) -> JSONResponse:
    record_id = str(uuid.uuid4())
    path_new = f"records/{record_id}.mp3"
    os.makedirs('records', exist_ok=True)
    try:
        audio = audio.file
        audio = AudioSegment.from_file(audio, format="wav")
        audio.export(path_new, format="mp3")
    except Exception:
        return JSONResponse(status_code=400, content={"TypeError": 'wrong type of file'})
    response = await add_audio_db(db, user_id, token, record_id)
    if response != True:
        return JSONResponse(status_code=400, content={"NotFoundError": 'wrong data'})
    host = '127.0.0.1'
    port = '8000'
    url = f"http://{host}:{port}/api/record?record_id={record_id}&user_id={user_id}"
    return JSONResponse(status_code=201, content={"url": url})
