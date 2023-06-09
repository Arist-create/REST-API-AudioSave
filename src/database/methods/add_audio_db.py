from src.database.model import User
from sqlalchemy import select

async def add_audio_db(db, user_id, token, record_id) -> bool:
    user: User | None = await db.execute(select(User).filter(User.user_id == user_id, User.token == token))
    user: User | None = user.scalars().first()
    if user is not None:
        user.record_id = record_id
        await db.commit()
        return True
    return False
