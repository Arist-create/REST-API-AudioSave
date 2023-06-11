from src.database.model import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def add_audio_db(db: AsyncSession, user_id: str, token: str, record_id: str) -> bool:
    user = await db.execute(select(User).filter(User.user_id == user_id, User.token == token))
    user = user.scalars().first()
    if user is not None:
        user.record_id = record_id
        await db.commit()
        return True
    return False
