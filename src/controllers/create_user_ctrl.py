import uuid
from fastapi.responses import JSONResponse
from src.database.methods.add_user_db import add_user_db
from sqlalchemy.ext.asyncio import AsyncSession




async def create_user_ctrl(db: AsyncSession, name: str) -> JSONResponse:
    user_id: str = str(uuid.uuid4())
    token: str = str(uuid.uuid4())
    await add_user_db(db, user_id, name, token)
    return JSONResponse(status_code=201, content={"user_id": user_id, "token": token})
