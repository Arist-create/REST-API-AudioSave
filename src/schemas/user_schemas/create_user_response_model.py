from pydantic import BaseModel

class CreateUserResponseModel(BaseModel):
    user_id: str
    token: str