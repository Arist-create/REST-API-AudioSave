from src.database.model import User
from sqlalchemy import select

async def get_audio_db(db, user_id, record_id) -> bool:
    user: User | None = await db.execute(select(User).filter(User.user_id == user_id, User.record_id == record_id))
    user: User | None = user.scalars().first()
    if user is not None:
        return True
    return False