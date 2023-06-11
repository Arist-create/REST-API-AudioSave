from src.database.model import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_audio_db(db: AsyncSession, user_id: str, record_id: str) -> bool:
    user = await db.execute(select(User).filter(User.user_id == user_id, User.record_id == record_id))
    user = user.scalars().first()
    if user is not None:
        return True
    return False
