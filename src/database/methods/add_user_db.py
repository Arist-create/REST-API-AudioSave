from src.database.model import User
from sqlalchemy.ext.asyncio import AsyncSession



async def add_user_db(db: AsyncSession, user_id: str, name: str, token: str) -> None:
    user = User(user_id=user_id, name=name, token=token)
    db.add(user)
    await db.commit()
