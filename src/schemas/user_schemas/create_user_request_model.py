from pydantic import BaseModel


class CreateUserRequestModel(BaseModel):
    name: str
