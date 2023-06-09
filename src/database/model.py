from src.database.main import Base
from sqlalchemy import Column, String

class User(Base):
    __tablename__ = "Users"

    user_id = Column(String, primary_key=True)
    name = Column(String)
    token = Column(String)
    record_id = Column(String)
