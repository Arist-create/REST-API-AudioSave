from pydantic import BaseModel


class AddAudioRequestModel(BaseModel):
    user_id: str
    token: str